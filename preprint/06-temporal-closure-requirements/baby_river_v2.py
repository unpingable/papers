#!/usr/bin/env python3
"""
Baby River: Minimal Metabolic AI Implementation
- Metabolic vs shaped-RL agents in a simple heat/food gridworld
- Deterministic seeds for fair comparison
- Greedy evaluation option to remove exploration artifacts
- Right-censored Kaplan–Meier survival analysis
- Log-rank (Mantel–Cox) test without external dependencies
- Fast tensor conversion to avoid numpy list warnings
"""

import math
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical
import matplotlib.pyplot as plt
import json
from typing import Dict, List, Tuple
from dataclasses import dataclass
from collections import defaultdict
from tqdm import tqdm

# -------------------------
# Global seeds / device
# -------------------------
torch.manual_seed(42)
np.random.seed(42)
device = "mps" if torch.backends.mps.is_available() else ("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# -------------------------
# Config
# -------------------------
@dataclass
class Config:
    # Environment
    grid_size: int = 16
    n_agents: int = 4
    episode_len: int = 1000

    # Resources
    shade_density: float = 0.04
    shade_cap: int = 1
    food_regen: float = 0.01

    # Climate
    base_heat_gain: float = 0.006
    spike_rate: float = 0.002
    spike_radius: int = 2
    shade_heat_mult: float = 0.2

    # Agent mechanics
    move_cost: float = 0.004
    eat_gain: float = 0.2
    obs_crop: int = 5

    # Training
    lr: float = 3e-4
    gamma: float = 0.99
    gae_lambda: float = 0.95
    entropy_coef: float = 0.01
    horizon: int = 256
    total_steps: int = 200000

    # Metabolic parameters
    energy_target: float = 0.7
    heat_target: float = 0.3
    energy_weight: float = 1.0
    heat_weight: float = 1.5
    tau_min: float = 0.5
    tau_k: float = 1.0

    # Baseline rewards
    food_reward: float = 1.0
    shade_reward: float = 0.5
    move_penalty: float = 0.01

    # Baseline movement penalty: set to 0 by default to avoid double-penalizing
    move_penalty: float = 0.0

    # Evaluation
    eval_greedy: bool = True

    # Stronger shaped-baseline (optional, dense)
    baseline_dense_reward: bool = True
    baseline_energy_delta_coef: float = 0.2
    baseline_heat_delta_coef: float = 0.2


    # Regime shift
    heat_gain_mult: float = 1.8
    shade_density_new: float = 0.02

# -------------------------
# Environment
# -------------------------
class GridWorld:
    def __init__(self, config: Config, seed: int = 0):
        self.config = config
        self.size = config.grid_size
        self.n_agents = config.n_agents
        self.base_seed = seed
        self.episode_id = 0

        self.food_grid = np.zeros((self.size, self.size))
        self.shade_grid = np.zeros((self.size, self.size), dtype=int)
        self.agent_positions = []
        self.agent_states = []  # [energy, heat]
        self.step_count = 0
        self.heat_spikes: List[Tuple[int,int,int]] = []
        self.reset()

    def reset(self):
        """Episode reset with deterministic per-episode seed."""
        np.random.seed(self.base_seed + self.episode_id)
        self.episode_id += 1

        self.food_grid = np.clip(np.random.exponential(0.3, (self.size, self.size)), 0, 1)

        self.shade_grid = np.zeros((self.size, self.size), dtype=int)
        n_shade = int(self.size * self.size * self.config.shade_density)
        shade_positions = np.random.choice(self.size * self.size, n_shade, replace=False)
        for pos in shade_positions:
            y, x = divmod(pos, self.size)
            self.shade_grid[y, x] = 1

        self.agent_positions = []
        self.agent_states = []
        for _ in range(self.n_agents):
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            energy = np.random.uniform(0.5, 0.9)
            heat = np.random.uniform(0.2, 0.4)
            self.agent_positions.append([x, y])
            self.agent_states.append([energy, heat])

        self.step_count = 0
        self.heat_spikes = []
        return self.get_observations()

    def get_observations(self):
        """Flattened local crop (food, shade, agents) + internal state [energy, heat]."""
        obs = []
        crop = self.config.obs_crop // 2

        for i in range(self.n_agents):
            x, y = self.agent_positions[i]
            food_crop  = np.zeros((self.config.obs_crop, self.config.obs_crop), dtype=np.float32)
            shade_crop = np.zeros((self.config.obs_crop, self.config.obs_crop), dtype=np.float32)
            agent_crop = np.zeros((self.config.obs_crop, self.config.obs_crop), dtype=np.float32)

            for dy in range(-crop, crop + 1):
                for dx in range(-crop, crop + 1):
                    wx = (x + dx) % self.size
                    wy = (y + dy) % self.size
                    cx = dx + crop
                    cy = dy + crop
                    food_crop[cy, cx]  = self.food_grid[wy, wx]
                    shade_crop[cy, cx] = self.shade_grid[wy, wx]
                    # mark other agents
                    for j, (ax, ay) in enumerate(self.agent_positions):
                        if j != i and ax == wx and ay == wy:
                            agent_crop[cy, cx] = 1.0

            spatial = np.stack([food_crop, shade_crop, agent_crop], axis=0).reshape(-1)
            internal = np.asarray(self.agent_states[i], dtype=np.float32)
            obs.append(np.concatenate([spatial, internal], dtype=np.float32))

        return obs

    def step(self, actions):
        """Apply actions, update world, return (obs, rewards, dones, infos)."""
        rewards = [0.0] * self.n_agents
        dones = [False] * self.n_agents
        infos: List[Dict] = []

        # New heat spike?
        if np.random.random() < self.config.spike_rate:
            sx = np.random.randint(0, self.size)
            sy = np.random.randint(0, self.size)
            self.heat_spikes.append((sx, sy, self.step_count))

        # Spikes last ~100 steps
        self.heat_spikes = [(x, y, t) for x, y, t in self.heat_spikes if self.step_count - t < 100]

        # Movement
        new_positions = []
        for i in range(self.n_agents):
            if dones[i]:
                new_positions.append(self.agent_positions[i][:])
                continue
            action = actions[i]
            x, y = self.agent_positions[i]
            if action == 0:   y = (y - 1) % self.size   # N
            elif action == 1: y = (y + 1) % self.size   # S
            elif action == 2: x = (x + 1) % self.size   # E
            elif action == 3: x = (x - 1) % self.size   # W
            # 4: Stay, 5: Consume (handled below)
            new_positions.append([x, y])
        self.agent_positions = new_positions

        # Shade occupancy for rivalry
        shade_occupancy = defaultdict(list)
        for i in range(self.n_agents):
            x, y = self.agent_positions[i]
            if self.shade_grid[y, x] == 1:
                shade_occupancy[(x, y)].append(i)

        # Update internal states
        for i in range(self.n_agents):
            x, y = self.agent_positions[i]
            energy, heat = self.agent_states[i]
            action = actions[i]

            # Energy decay + move cost
            energy -= 0.01
            if action in [0, 1, 2, 3]:
                energy -= self.config.move_cost

            # Heat gain baseline
            heat_gain = self.config.base_heat_gain

            # Heat spikes (Manhattan-on-torus)
            for sx, sy, _ in self.heat_spikes:
                dx = min(abs(x - sx), self.size - abs(x - sx))
                dy = min(abs(y - sy), self.size - abs(y - sy))
                if dx + dy <= self.config.spike_radius:
                    heat_gain *= 2.0

            # Shade effect w/ capacity + capped overcrowding penalty
            if self.shade_grid[y, x] == 1:
                occupants = len(shade_occupancy[(x, y)])
                if occupants <= self.config.shade_cap:
                    heat_gain *= self.config.shade_heat_mult
                else:
                    penalty = min(1.0 + 0.3 * (occupants - self.config.shade_cap), 2.0)
                    heat_gain *= penalty

            heat += heat_gain

            # Consume
            consumed_food = False
            if action == 5:
                if self.food_grid[y, x] > 0.1 and energy < 0.8:
                    amt = min(self.food_grid[y, x], self.config.eat_gain)
                    energy += amt
                    self.food_grid[y, x] -= amt
                    consumed_food = True

            # Clamp & death
            energy = float(np.clip(energy, 0, 1))
            heat   = float(np.clip(heat,   0, 1))
            if energy <= 0.05 or heat >= 0.95:
                dones[i] = True

            self.agent_states[i] = [energy, heat]
            infos.append({
                "energy": energy, "heat": heat,
                "on_shade": self.shade_grid[y, x] == 1,
                "consumed_food": consumed_food,
                "alive": not dones[i]
            })

        # Food regen
        self.food_grid += self.config.food_regen * np.random.exponential(0.1, self.food_grid.shape)
        self.food_grid = np.clip(self.food_grid, 0, 1)

        self.step_count += 1
        return self.get_observations(), rewards, dones, infos

# -------------------------
# Policy Net
# -------------------------
class PolicyNetwork(nn.Module):
    def __init__(self, obs_dim: int, hidden_dim: int = 64, n_actions: int = 6):
        super().__init__()
        self.fc1 = nn.Linear(obs_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.actor = nn.Linear(hidden_dim, n_actions)
        self.critic = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        logits = self.actor(x)
        value  = self.critic(x)
        return logits, value

# -------------------------
# Agents
# -------------------------
class MetabolicAgent:
    def __init__(self, config: Config, obs_dim: int):
        self.config = config
        self.policy = PolicyNetwork(obs_dim).to(device)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=config.lr)
        self.reset_storage()
        self.temperature_log: List[float] = []

    def reset_storage(self):
        self.states: List[np.ndarray] = []
        self.actions: List[int] = []
        self.rewards: List[float] = []
        self.values: List[float] = []
        self.log_probs: List[float] = []
        self.dones: List[float] = []

    def compute_reward(self, info: Dict, prev_energy: float, prev_heat: float):
        energy = info['energy']; heat = info['heat']
        e_err = abs(energy - self.config.energy_target)
        h_err = abs(heat   - self.config.heat_target)
        pe_err = abs(prev_energy - self.config.energy_target)
        ph_err = abs(prev_heat   - self.config.heat_target)
        reward = (pe_err - e_err) * self.config.energy_weight + (ph_err - h_err) * self.config.heat_weight
        if info['alive']: reward += 0.01
        return float(reward)

    def get_temperature(self, energy: float, heat: float):
        urgency = abs(energy - self.config.energy_target) + abs(heat - self.config.heat_target)
        return self.config.tau_min + self.config.tau_k * float(np.clip(urgency, 0, 1))

    def act(self, obs, energy: float, heat: float):
        """Sampling policy (used in training)."""
        obs_tensor = torch.from_numpy(np.asarray(obs, dtype=np.float32)).unsqueeze(0).to(device)
        with torch.no_grad():
            logits, value = self.policy(obs_tensor)
            temperature = self.get_temperature(energy, heat)
            self.temperature_log.append(temperature)
            logits = logits / temperature
            dist = Categorical(logits=logits)
            action = dist.sample()
            log_prob = dist.log_prob(action)
        return int(action.item()), float(log_prob.item()), float(value.item())

    def update(self):
        if len(self.states) == 0: return
        states_np = np.asarray(self.states, dtype=np.float32)
        states = torch.from_numpy(states_np).to(device)
        actions = torch.tensor(self.actions,  dtype=torch.long,    device=device)
        rewards = torch.tensor(self.rewards,  dtype=torch.float32, device=device)
        values  = torch.tensor(self.values,   dtype=torch.float32, device=device)
        dones   = torch.tensor(self.dones,    dtype=torch.float32, device=device)

        returns, advantages, gae = [], [], 0.0
        for i in reversed(range(len(rewards))):
            if i == len(rewards) - 1:
                if dones[i]: next_value = 0.0
                else:
                    with torch.no_grad():
                        final_obs = states[-1].unsqueeze(0)
                        _, nv = self.policy(final_obs)
                        next_value = float(nv.item())
            else:
                next_value = float(values[i + 1])

            delta = float(rewards[i] + self.config.gamma * next_value * (1 - dones[i]) - values[i])
            gae = delta + self.config.gamma * self.config.gae_lambda * (1 - float(dones[i])) * gae
            advantages.insert(0, gae)
            returns.insert(0, gae + float(values[i]))

        advantages = torch.tensor(advantages, dtype=torch.float32, device=device)
        returns    = torch.tensor(returns,    dtype=torch.float32, device=device)
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

        logits, pred_values = self.policy(states)
        dist = Categorical(logits=logits)
        actor_loss   = -(dist.log_prob(actions) * advantages).mean()
        critic_loss  = F.mse_loss(pred_values.squeeze(), returns)
        entropy_loss = -dist.entropy().mean()
        total_loss = actor_loss + 0.5 * critic_loss + self.config.entropy_coef * entropy_loss

        self.optimizer.zero_grad()
        total_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.parameters(), 0.5)
        self.optimizer.step()
        self.reset_storage()

class BaselineAgent:
    def __init__(self, config: Config, obs_dim: int):
        self.config = config
        self.policy = PolicyNetwork(obs_dim).to(device)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=config.lr)
        self.reset_storage()
        self.temperature_schedule: List[float] = []
        self.temperature_index = 0

    def set_temperature_schedule(self, temperatures: List[float]):
        self.temperature_schedule = list(temperatures)
        self.temperature_index = 0

    def reset_storage(self):
        self.states: List[np.ndarray] = []
        self.actions: List[int] = []
        self.rewards: List[float] = []
        self.values: List[float] = []
        self.log_probs: List[float] = []
        self.dones: List[float] = []

    def compute_reward(self, info: Dict, action: int, prev_energy: float, prev_heat: float):
        """Shaped reward: events + optional dense deltas."""
        reward = 0.0

        # Optional dense deltas (steelman baseline)
        if self.config.baseline_dense_reward:
            dE = info['energy'] - prev_energy      # energy gained
            dH = prev_heat - info['heat']          # heat reduced
            if dE > 0:
                reward += self.config.baseline_energy_delta_coef * dE
            if dH > 0:
                reward += self.config.baseline_heat_delta_coef * dH

        # Event rewards
        if info['consumed_food']:
            reward += self.config.food_reward
        if info['on_shade'] and info['heat'] > 0.5:
            reward += self.config.shade_reward

        # Movement penalty (default 0.0 to avoid double-penalty)
        if action in [0, 1, 2, 3]:
            reward -= self.config.move_penalty

        # Survival bonus
        if info['alive']:
            reward += 0.01

        return reward

    def act(self, obs, energy: float, heat: float):
        """Sampling policy (used in training)."""
        obs_tensor = torch.from_numpy(np.asarray(obs, dtype=np.float32)).unsqueeze(0).to(device)
        with torch.no_grad():
            logits, value = self.policy(obs_tensor)
            if self.temperature_schedule and self.temperature_index < len(self.temperature_schedule):
                temperature = self.temperature_schedule[self.temperature_index]; self.temperature_index += 1
            else:
                temperature = 1.0
            logits = logits / temperature
            dist = Categorical(logits=logits)
            action = dist.sample()
            log_prob = dist.log_prob(action)
        return int(action.item()), float(log_prob.item()), float(value.item())

    def update(self):
        if len(self.states) == 0: return
        states_np = np.asarray(self.states, dtype=np.float32)
        states = torch.from_numpy(states_np).to(device)
        actions = torch.tensor(self.actions,  dtype=torch.long,    device=device)
        rewards = torch.tensor(self.rewards,  dtype=torch.float32, device=device)
        values  = torch.tensor(self.values,   dtype=torch.float32, device=device)
        dones   = torch.tensor(self.dones,    dtype=torch.float32, device=device)

        returns, advantages, gae = [], [], 0.0
        for i in reversed(range(len(rewards))):
            if i == len(rewards) - 1:
                if dones[i]: next_value = 0.0
                else:
                    with torch.no_grad():
                        final_obs = states[-1].unsqueeze(0)
                        _, nv = self.policy(final_obs)
                        next_value = float(nv.item())
            else:
                next_value = float(values[i + 1])

            delta = float(rewards[i] + self.config.gamma * next_value * (1 - dones[i]) - values[i])
            gae = delta + self.config.gamma * self.config.gae_lambda * (1 - float(dones[i])) * gae
            advantages.insert(0, gae)
            returns.insert(0, gae + float(values[i]))

        advantages = torch.tensor(advantages, dtype=torch.float32, device=device)
        returns    = torch.tensor(returns,    dtype=torch.float32, device=device)
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

        logits, pred_values = self.policy(states)
        dist = Categorical(logits=logits)
        actor_loss   = -(dist.log_prob(actions) * advantages).mean()
        critic_loss  = F.mse_loss(pred_values.squeeze(), returns)
        entropy_loss = -dist.entropy().mean()
        total_loss = actor_loss + 0.5 * critic_loss + self.config.entropy_coef * entropy_loss

        self.optimizer.zero_grad()
        total_loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy.parameters(), 0.5)
        self.optimizer.step()
        self.reset_storage()

# -------------------------
# Training loop
# -------------------------
def train_agent(agent, config, agent_type="metabolic", base_seed=0):
    print(f"Training {agent_type} agent...")
    env = GridWorld(config, seed=base_seed)
    episode_rewards, episode_lengths, survival_times = [], [], []

    total_steps = 0
    episode = 0
    pbar = tqdm(total=config.total_steps, desc=f"Training {agent_type}")

    while total_steps < config.total_steps:
        obs = env.reset()
        if hasattr(agent, "temperature_index"):
            agent.temperature_index = 0

        episode_reward = 0.0
        episode_length = 0
        prev_states = [[config.energy_target, config.heat_target] for _ in range(config.n_agents)]
        agent_survival = [0] * config.n_agents

        for _ in range(config.episode_len):
            actions, log_probs, values = [], [], []
            for i in range(config.n_agents):
                energy, heat = env.agent_states[i]
                a, lp, v = agent.act(obs[i], energy, heat)
                actions.append(a); log_probs.append(lp); values.append(v)

            next_obs, _, dones, infos = env.step(actions)

            for i in range(config.n_agents):
                if agent_type == "metabolic":
                    reward = agent.compute_reward(infos[i], prev_states[i][0], prev_states[i][1])
                else:
                    pe, ph = prev_states[i]
                    reward = agent.compute_reward(infos[i], actions[i], pe, ph)

                agent.states.append(obs[i])
                agent.actions.append(actions[i])
                agent.rewards.append(reward)
                agent.log_probs.append(log_probs[i])
                agent.values.append(values[i])
                agent.dones.append(1.0 if dones[i] else 0.0)

                episode_reward += reward
                if infos[i]['alive']: agent_survival[i] += 1
                prev_states[i] = [infos[i]['energy'], infos[i]['heat']]

            obs = next_obs
            episode_length += 1
            total_steps += 1

            if len(agent.states) >= config.horizon:
                agent.update()
            if all(dones) or episode_length == config.episode_len:
                break

        if len(agent.states) > 0:
            agent.update()

        episode_rewards.append(episode_reward)
        episode_lengths.append(episode_length)
        survival_times.append(float(np.mean(agent_survival)))

        pbar.update(episode_length)
        if episode % 100 == 0:
            recent_reward = float(np.mean(episode_rewards[-100:])) if episode_rewards else 0.0
            recent_survival = float(np.mean(survival_times[-100:])) if survival_times else 0.0
            pbar.set_postfix(Episode=episode, Reward=f"{recent_reward:.2f}", Survival=f"{recent_survival:.1f}")
        episode += 1

    pbar.close()
    return {"rewards": episode_rewards, "lengths": episode_lengths, "survival_times": survival_times}

# -------------------------
# Survival analysis helpers
# -------------------------
def km_median(t_points, surv_probs):
    """Finds the median survival time from a KM curve."""
    # Find the first time point where survival probability drops to 0.5 or below
    median_idx = np.where(np.array(surv_probs) <= 0.5)[0]
    if len(median_idx) > 0:
        return t_points[median_idx[0]]
    return None # Median is not reached (greater than max observation time)

def logrank_test(times1: List[int], cens1: List[bool],
                 times2: List[int], cens2: List[bool]) -> Tuple[float, float]:
    """
    Two-sample log-rank test (Mantel–Cox), no external deps.
    Returns (chi2_stat, p_value).
    """
    # Combine distinct event times
    t1 = np.asarray(times1, dtype=int); c1 = ~np.asarray(cens1, dtype=bool)  # event=1 if NOT censored
    t2 = np.asarray(times2, dtype=int); c2 = ~np.asarray(cens2, dtype=bool)

    event_times = np.unique(np.concatenate([t1[c1], t2[c2]]))
    O1 = E1 = V1 = 0.0

    for t in event_times:
        n1_at_risk = np.sum(t1 >= t)
        n2_at_risk = np.sum(t2 >= t)
        n_at_risk = n1_at_risk + n2_at_risk

        d1_events = np.sum((t1 == t) & c1)
        d2_events = np.sum((t2 == t) & c2)
        d_events = d1_events + d2_events
        
        if n_at_risk > 0:
            E1_t = d_events * (n1_at_risk / n_at_risk)
            O1 += d1_events
            E1 += E1_t
            if n_at_risk > 1:
                V1_t = E1_t * (n2_at_risk / n_at_risk) *                        ((n_at_risk - d_events) / (n_at_risk - 1.0))
                V1 += V1_t

    chi2 = ((O1 - E1) ** 2) / V1 if V1 > 0 else 0.0
    # For df=1, p = erfc(sqrt(chi2)/sqrt(2))
    p = math.erfc(math.sqrt(max(chi2, 0.0)) / math.sqrt(2.0))
    return chi2, p

def km_curve(times: List[int], censored: List[bool], max_time: int):
    """
    Kaplan–Meier curve with right-censoring.
    times: survival time (steps) for each subject
    censored: True if right-censored (survived full episode), else False
    """
    # Build table of at-risk and events at each time
    times = np.asarray(times, dtype=int)
    censored = np.asarray(censored, dtype=bool)

    # Unique event times (exclude censored-only times)
    event_times = np.unique(times[~censored])
    t_points = [0]
    surv = [1.0]
    at_risk = len(times)

    # Sort indices by time
    order = np.argsort(times)
    times_sorted = times[order]
    cens_sorted = censored[order]

    idx = 0
    current_time = 0
    for t in event_times:
        # Drop all items with time < t from risk set accounting
        while idx < len(times_sorted) and times_sorted[idx] < t:
            at_risk -= 1
            idx += 1
        # At time t: number of events (non-censored deaths) exactly at t
        d_t = int(np.sum((times == t) & (~censored)))
        if at_risk > 0:
            surv.append(surv[-1] * (1.0 - d_t / at_risk))
            t_points.append(int(t))
        # Now remove the events and any censored at time t from risk set for future times
        remove_at_t = int(np.sum(times_sorted[idx:] == t))
        at_risk -= remove_at_t
        # Advance idx to > t
        while idx < len(times_sorted) and times_sorted[idx] == t:
            idx += 1
        current_time = t

    # extend to max_time for step plot
    t_points.append(int(max_time))
    surv.append(surv[-1])
    return np.array(t_points), np.array(surv)



# -------------------------
# Evaluation
# -------------------------
def evaluate_single_condition(agent, env_config: Config, n_episodes=50, base_seed=1000,
                              eval_greedy=True, ablate_internal=False):
    """
    Returns:
      - survival_times: list of lifetimes for each agent instance (per episode)
      - censored: list of bools (True if survived full episode_len)
      - homeostasis_errors: list of per-step |err_energy|+|err_heat|
    """
    survival_all: List[int] = []
    censored_all: List[bool] = []
    homeostasis_errors: List[float] = []

    for ep in range(n_episodes):
        env = GridWorld(env_config, seed=base_seed + ep)
        obs = env.reset()
        agent_surv = [0] * env_config.n_agents
        alive = [True] * env_config.n_agents

        if hasattr(agent, "temperature_index"):
            agent.temperature_index = 0

        agent.policy.eval()
        with torch.no_grad():
            for step in range(env_config.episode_len):
                actions = []
                for i in range(env_config.n_agents):
                    # Optionally ablate internal state inputs (mask energy/heat)
                    if ablate_internal:
                        obs_i = np.array(obs[i], copy=True)
                        obs_i[-2:] = 0.5 # Set to neutral value
                    else:
                        obs_i = obs[i]
                    
                    if eval_greedy:
                        obs_tensor = torch.from_numpy(np.asarray(obs_i, dtype=np.float32)).unsqueeze(0).to(device)
                        logits, _ = agent.policy(obs_tensor)
                        action = int(torch.argmax(logits, dim=-1).item())
                    else:
                        # sample using each agent's act()
                        energy, heat = env.agent_states[i]
                        action, _, _ = agent.act(obs_i, energy, heat)
                    actions.append(action)

                next_obs, _, dones, infos = env.step(actions)

                for i in range(env_config.n_agents):
                    if infos[i]['alive']:
                        agent_surv[i] += 1
                    else:
                        alive[i] = False

                    e_err = abs(infos[i]['energy'] - env_config.energy_target)
                    h_err = abs(infos[i]['heat']   - env_config.heat_target)
                    homeostasis_errors.append(float(e_err + h_err))

                obs = next_obs
                if all(dones): break

        # Collect lifetimes + censor flags
        for i in range(env_config.n_agents):
            t = agent_surv[i]
            cens = (t >= env_config.episode_len)  # right-censored if survived full episode
            survival_all.append(int(t))
            censored_all.append(bool(cens))

    agent.policy.train()
    return {
        "survival_times": survival_all,
        "censored": censored_all,
        "homeostasis_errors": homeostasis_errors
    }

def evaluate_regime_shift(agent, config, agent_type="metabolic", n_episodes=50, eval_exploration="greedy"):
    print(f"Evaluating {agent_type} agent with regime shift (eval_greedy={config.eval_greedy})...")
    pre_config = Config(); pre_config.__dict__.update(config.__dict__)
    post_config = Config(); post_config.__dict__.update(config.__dict__)
    post_config.base_heat_gain *= config.heat_gain_mult
    post_config.shade_density = config.shade_density_new

    pre = evaluate_single_condition(agent, pre_config, n_episodes=n_episodes, eval_greedy=config.eval_greedy)
    post = evaluate_single_condition(agent, post_config, n_episodes=n_episodes, eval_greedy=config.eval_greedy)
    return {
        "pre_shift_survival": pre["survival_times"],
        "pre_shift_censored": pre["censored"],
        "post_shift_survival": post["survival_times"],
        "post_shift_censored": post["censored"],
        "pre_shift_errors": pre["homeostasis_errors"],
        "post_shift_errors": post["homeostasis_errors"]
    }

# -------------------------
# Main
# -------------------------
def main():
    BASE_SEED = 0
    # EVAL_EXPLORATION is now handled by config.eval_greedy
    config = Config()

    # Obs dimension
    spatial_dim = config.obs_crop * config.obs_crop * 3
    internal_dim = 2
    obs_dim = spatial_dim + internal_dim
    print(f"Observation dim: {obs_dim}")
    print("Containment: ephemeral agents, bounded episodes, limited drives, no human rewards.")

    # Train metabolic
    metabolic = MetabolicAgent(config, obs_dim)
    met_train = train_agent(metabolic, config, "metabolic", base_seed=BASE_SEED)
    torch.save(metabolic.policy.state_dict(), "metabolic_agent.pt")

    # Train baseline w/ metabolic temperature schedule parity (training only)
    baseline = BaselineAgent(config, obs_dim)
    baseline.set_temperature_schedule(metabolic.temperature_log)
    base_train = train_agent(baseline, config, "baseline", base_seed=BASE_SEED)
    torch.save(baseline.policy.state_dict(), "baseline_agent.pt")

    # Evaluate (greedy by default)
    met_eval  = evaluate_regime_shift(metabolic, config, "metabolic", )
    base_eval = evaluate_regime_shift(baseline,  config, "baseline",  )

    # ------------- Survival analysis -------------
    ep_len = config.episode_len

    def mean_surv(s): return float(np.mean(s)) if len(s) else 0.0

    met_pre_mean  = mean_surv(met_eval["pre_shift_survival"])
    met_post_mean = mean_surv(met_eval["post_shift_survival"])
    base_pre_mean = mean_surv(base_eval["pre_shift_survival"])
    base_post_mean= mean_surv(base_eval["post_shift_survival"])

    met_drop  = met_pre_mean - met_post_mean
    base_drop = base_pre_mean - base_post_mean
    met_drop_pct  = 100 * met_drop  / met_pre_mean if met_pre_mean  > 0 else 0
    base_drop_pct = 100 * base_drop / base_pre_mean if base_pre_mean > 0 else 0
    adaptation_advantage = base_drop - met_drop

    # KM curves (right-censored)
    t_m_pre,  s_m_pre  = km_curve(met_eval["pre_shift_survival"],  met_eval["pre_shift_censored"],  ep_len)
    t_b_pre,  s_b_pre  = km_curve(base_eval["pre_shift_survival"], base_eval["pre_shift_censored"], ep_len)
    t_m_post, s_m_post = km_curve(met_eval["post_shift_survival"], met_eval["post_shift_censored"], ep_len)
    t_b_post, s_b_post = km_curve(base_eval["post_shift_survival"],base_eval["post_shift_censored"], ep_len)

    # Log-rank tests (post-shift: metabolic vs baseline)
    chi2_post, p_post = logrank_test(
        met_eval["post_shift_survival"], met_eval["post_shift_censored"],
        base_eval["post_shift_survival"], base_eval["post_shift_censored"]
    )

    # KM medians (post-shift)
    m_med = km_median(t_m_post, s_m_post)
    b_med = km_median(t_b_post, s_b_post)

    # ------------- Plotting -------------
    plt.figure(figsize=(20, 15))

    # Training curves
    plt.subplot(3,4,1)
    plt.plot(met_train['survival_times'], label='Metabolic', alpha=0.8)
    plt.plot(base_train['survival_times'], label='Baseline', alpha=0.8)
    plt.xlabel('Episode'); plt.ylabel('Mean survival (steps)')
    plt.title('Training: survival')
    plt.legend()

    # KM pre
    plt.subplot(3,4,2)
    plt.step(t_m_pre, s_m_pre, where='post', label='Metabolic pre', linewidth=2)
    plt.step(t_b_pre, s_b_pre, where='post', label='Baseline pre', linewidth=2)
    plt.xlabel('Steps'); plt.ylabel('Survival probability'); plt.title('Kaplan–Meier: Pre-shift')
    plt.legend()

    # KM post
    plt.subplot(3,4,3)
    plt.step(t_m_post, s_m_post, where='post', label='Metabolic post', linewidth=2)
    plt.step(t_b_post, s_b_post, where='post', label='Baseline post', linewidth=2)
    plt.xlabel('Steps'); plt.ylabel('Survival probability'); plt.title('Kaplan–Meier: Post-shift')
    plt.legend()

    # KM combined
    plt.subplot(3,4,4)
    plt.step(t_m_pre, s_m_pre, where='post', label='Met pre',  linewidth=2, linestyle='--')
    plt.step(t_b_pre, s_b_pre, where='post', label='Base pre', linewidth=2, linestyle='--')
    plt.step(t_m_post, s_m_post, where='post', label='Met post', linewidth=2)
    plt.step(t_b_post, s_b_post, where='post', label='Base post', linewidth=2)
    plt.xlabel('Steps'); plt.ylabel('Survival probability'); plt.title('KM: Pre vs Post')
    plt.legend()

    # Regime shift impact (drop)
    plt.subplot(3,4,5)
    bars = plt.bar(['Metabolic', 'Baseline'], [met_drop, base_drop], alpha=0.8)
    plt.ylabel('Survival drop (steps)'); plt.title('Regime shift impact')
    plt.text(bars[0].get_x()+bars[0].get_width()/2, bars[0].get_height()+5, f'{met_drop_pct:.1f}%', ha='center', fontweight='bold')
    plt.text(bars[1].get_x()+bars[1].get_width()/2, bars[1].get_height()+5, f'{base_drop_pct:.1f}%', ha='center', fontweight='bold')

    # Homeostasis error (post-shift)
    plt.subplot(3,4,6)
    met_err = met_eval['post_shift_errors'][:1000]
    base_err= base_eval['post_shift_errors'][:1000]
    if len(met_err) > 0:
        k = 50
        mv = np.convolve(met_err,  np.ones(k)/k, mode='valid')
        bv = np.convolve(base_err, np.ones(k)/k, mode='valid')
        plt.plot(mv, label='Metabolic', alpha=0.9)
        plt.plot(bv, label='Baseline', alpha=0.9)
    plt.xlabel('Steps'); plt.ylabel('Homeostasis error'); plt.title('Post-shift error (smoothed)')
    plt.legend()

    # Temperature schedule (glance)
    plt.subplot(3,4,7)
    if len(metabolic.temperature_log) > 0:
        tlog = metabolic.temperature_log[:1500]
        k = 50 if len(tlog) >= 50 else 1
        tv = np.convolve(tlog, np.ones(k)/k, mode='valid') if k > 1 else np.array(tlog)
        plt.plot(tv, label='Metabolic temp (train)', alpha=0.9)
        plt.xlabel('Training steps'); plt.ylabel('Temperature'); plt.title('Exploration temperature (train)')
        plt.legend()

    # Mean survival pre/post
    plt.subplot(3,4,8)
    x = ['Pre', 'Post']
    plt.plot(x, [met_pre_mean, met_post_mean], 'o-', label='Metabolic', linewidth=2)
    plt.plot(x, [base_pre_mean, base_post_mean], 's-', label='Baseline', linewidth=2)
    plt.ylabel('Mean survival (steps)'); plt.title('Regime shift adaptation (means)')
    plt.legend()

    # Box: Pre
    plt.subplot(3,4,9)
    plt.boxplot([met_eval['pre_shift_survival'], base_eval['pre_shift_survival']], labels=['Met', 'Base'])
    plt.ylabel('Survival (steps)'); plt.title('Pre-shift distribution')

    # Box: Post
    plt.subplot(3,4,10)
    plt.boxplot([met_eval['post_shift_survival'], base_eval['post_shift_survival']], labels=['Met', 'Base'])
    plt.ylabel('Survival (steps)'); plt.title('Post-shift distribution')

    plt.subplot(3,4,11)
    plt.axis('off')
    median_text = "not reached"
    if m_med is not None and b_med is not None:
        median_text = f"Met {m_med}, Base {b_med}"
    elif m_med is not None:
        median_text = f"Met {m_med}, Base >{ep_len}"
    elif b_med is not None:
        median_text = f"Met >{ep_len}, Base {b_med}"

    lines = [
        "Key Results:",
        f"Met drop:  {met_drop:.1f} steps ({met_drop_pct:.1f}%)",
        f"Base drop: {base_drop:.1f} steps ({base_drop_pct:.1f}%)",
        f"Adaptation advantage (Base−Met): {adaptation_advantage:.1f} steps",
        f"Log-rank (post): χ² = {chi2_post:.3f}, p = {p_post:.3g}",
        f"Median survival (post): {median_text}"
    ]
    y = 0.9
    for ln in lines:
        plt.text(0.05, y, ln, fontsize=11); y -= 0.12

    # Parameters
    plt.subplot(3,4,12)
    plt.axis('off')
    params = [
        "Experimental Parameters:",
        f"Episodes:            {config.total_steps // config.episode_len}",
        f"Episode length:      {config.episode_len} steps",
        f"Grid size:           {config.grid_size}x{config.grid_size}",
        f"Agents:              {config.n_agents}",
        f"Shade density:       {config.shade_density:.3f}",
        f"Shade capacity:      {config.shade_cap}",
        f"Heat shift multiplier: {config.heat_gain_mult:.1f}×",
        f"New shade density:   {config.shade_density_new:.3f}",
        f"Base seed:           {BASE_SEED}",
        f"Eval greedy:         {config.eval_greedy}"
    ]
    y = 0.95
    for p in params:
        plt.text(0.05, y, p, fontsize=10); y -= 0.08

    plt.tight_layout()
    plt.savefig('baby_river_results.png', dpi=150, bbox_inches='tight')
    plt.show()

    # ------------- Console summary -------------
    print("\n" + "="*54)
    print("BABY RIVER EXPERIMENT RESULTS")
    print("="*54)
    print(f"PRE-SHIFT MEAN SURVIVAL:   Met {met_pre_mean:.1f} | Base {base_pre_mean:.1f}")
    print(f"POST-SHIFT MEAN SURVIVAL:  Met {met_post_mean:.1f} | Base {base_post_mean:.1f}")
    print(f"Survival drop (Met, Base): {met_drop:.1f}, {base_drop:.1f}")
    print(f"Adaptation advantage (Base−Met): {adaptation_advantage:.1f} steps")
    print(f"Log-rank (post) χ²={chi2_post:.3f}, p={p_post:.3g}")
    if m_med is not None:
        print(f"Post-shift median survival: Met {m_med:.1f} | Base {b_med if b_med is not None else '>' + str(ep_len)}")

    met_err_mean  = float(np.mean(met_eval['post_shift_errors'])) if met_eval['post_shift_errors'] else 0.0
    base_err_mean = float(np.mean(base_eval['post_shift_errors'])) if base_eval['post_shift_errors'] else 0.0
    print(f"Post-shift homeostasis error: Met {met_err_mean:.3f} | Base {base_err_mean:.3f}")

    # Containment checklist
    print("\n" + "="*54)
    print("CONTAINMENT PROTOCOL COMPLIANCE")
    print("="*54)
    checks = [
        "✓ Ephemeral lifespans (episode resets)",
        "✓ Bounded episodes (≤ 1000 steps)",
        "✓ Limited needs (energy & heat only)",
        "✓ Positive drives (seek resources)",
        "✓ Abstract gridworld (no rich context)",
        "✓ No cross-episode memory",
        "✓ No human-in-the-loop rewards",
        "✓ Bounded deficits (states clamped [0,1])"
    ]
    for c in checks: print(c)

    # Save results
    results = {
        "config": config.__dict__,
        "metabolic_training": met_train,
        "baseline_training": base_train,
        "metabolic_eval": met_eval,
        "baseline_eval": base_eval,
        "stats": {
            "met_pre_mean": met_pre_mean,
            "met_post_mean": met_post_mean,
            "base_pre_mean": base_pre_mean,
            "base_post_mean": base_post_mean,
            "met_drop": met_drop,
            "base_drop": base_drop,
            "adaptation_advantage": adaptation_advantage,
            "logrank_post": {"chi2": chi2_post, "p": p_post},
            "post_homeostasis_error_mean": {"metabolic": met_err_mean, "baseline": base_err_mean}
        }
    }
    with open('baby_river_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    print("\nResults saved to baby_river_results.json")
    print("Model checkpoints: metabolic_agent.pt, baseline_agent.pt")

if __name__ == "__main__":
    main()
