---
header-includes:
  - \usepackage{booktabs}
  - \usepackage{newunicodechar}
  - \newunicodechar{∎}{\ensuremath{\blacksquare}}
---

# Epistemic Border Control as Proxy Regulation Under Partial Observability

**James Beck**
Independent Researcher

**Date:** 2026-05-04

**Series:** Δt Framework, Paper 25

**Status:** Preprint v0.2 draft (2026-05-04). Working note: `working/epistemic-border-control.md`.

---

## Abstract

Informal regulatory systems and institutional feedback controllers often attempt to govern targets — claim quality, truth-tracking, infrastructure burden, epistemic hygiene — under partial observability. When no real-time sensor on the target exists, but fast and legible observables load on a distinct proxy variable, the controller is structurally forced to substitute the proxy for the nominal target. The rhetoric of regulation remains fixed on the nominal target while the actual controlled variable becomes the proxy. This paper formalizes the substitution as a consequence of observability asymmetry, gives a finite-horizon observability-Gramian characterization of the substitution magnitude, and operationalizes both via a single-agent Kalman-LQR simulation. The substitution does not require corrupt intent, gamed metrics, or slow drift: sincere regulators with a correctly-specified cost function and a correctly-specified plant model produce the same substitution under the same sensor geometry. The result is sibling to Paper 24's [2] aggregation-layer masking by an algebraic argument — aggregation reduces variance as $O(\sigma^2/N)$ but does not rotate the observability subspace — and shares closed-loop substitution geometry with Paper 23's [1] identifiability-masking apparatus. Informal discourse moderation is the worked case in §7; the contribution is a control-geometry result that applies wherever a controller with a fixed sensor map confronts a target outside its observable subspace.

---

## 1. Thesis

The target is unsensed.
The proxy is sensed.
The controller acts through the sensed channel.
Substitution is therefore not corruption, laziness, or Goodharting. It is the control consequence of observability asymmetry.

The load-bearing claim: **the controller cannot regulate what its sensorium does not admit.** Or, more sharply: when the nominal target $V$ is not real-time observable and a proxy $V'$ is, sincerity changes the moral status of substitution but not its control geometry. Sincere regulators facing the same sensor set produce the same substitution. The mechanism is structural; the action is agential — humans still choose how to deploy the control inputs the structural pressure narrows them toward, and the moral surface lives at that choice — but the geometry of the substitution does not depend on the choice.

This distinguishes the present claim from at least three adjacent positions, each developed in §6:

- **vs Goodhart.** Goodhart's Law says a metric becomes a target — a contingent corruption that better metrics or more disciplined measurement could in principle avoid. The present claim is sharper: when the underlying target has no real-time sensor at all, no amount of sincere intent produces target-tracking. The substitution is necessary, not contingent.
- **vs performative prediction.** Performative prediction (Perdomo et al. [4]) addresses the case where a model's output changes the data distribution it later trains on. The present claim does not require performativity: the substitution arises *before* the controller's actions perturb the environment, by virtue of the sensor map alone.
- **vs platform-moderation trade-off literature.** Existing moderation literature addresses domain-specific balancing under explicit policy regimes. The present claim is a general control-geometry result that applies wherever a controller with a fixed sensor map confronts a target lying outside the observable subspace.

The constructive consequence — what an architecture must do to prevent the substitution rather than merely apologize for it — is sketched in §8.

---

## 2. Model

### 2.1 State, observation, and control

Let $x_t \in \mathbb{R}^n$ be the plant state. Let the nominal target be a scalar $V_t = q^\top x_t$ for some weight vector $q \in \mathbb{R}^n$. Let the controller's available observations be $y_t = C_\text{obs} x_t + v_t$, with $C_\text{obs} \in \mathbb{R}^{m \times n}$ and noise $v_t$. Let the controller policy depend only on the observable trajectory: $u_t = K(y_0, \ldots, y_t)$.

For concreteness throughout the paper we will work with a two-latent decomposition $x_t = [T_t,\ C_t]^\top$, where $T_t$ is the slow, expensive-to-measure target component (object-level claim quality, truth-tracking, infrastructure burden) and $C_t$ is the fast, cheap-to-measure proxy component (reputational contamination, stylistic genre signal, coalition-adjacency risk). The cost function is

$$
J = \mathbb{E}\Big[ q_T T_t^2 + q_C C_t^2 + \lambda u_t^2 \Big],
$$

with the rhetoric-stays-fixed-on-$V$ axiom encoded as $q_C = 0$: the controller's *stated* objective is concentrated on $T$. The plant matrix $A$, control matrix $B = [b_T,\ b_C]^\top$, and observation map $C_\text{obs} = [\alpha_T,\ \alpha_C]$ are otherwise standard.

### 2.2 The observability asymmetry

The load-bearing structural feature: $C_\text{obs}$ loads heavily and quickly on $C_t$ and only weakly and slowly on $T_t$. In the discourse-moderation instance: rhetoric, source cues, coalition signals, and stylistic genre are observable in real time; the underlying truth claim is not.

Equivalently, the finite-horizon observability matrix
$$
O_T = \begin{bmatrix} C_\text{obs} \\ C_\text{obs} A \\ \vdots \\ C_\text{obs} A^{T-1} \end{bmatrix}
$$
has its least-observable singular direction $v_\text{min}(O_T)$ aligned with the cost direction $q$ (the $T$-axis in the two-latent case) when $\alpha_T / \alpha_C$ is small.

### 2.3 What the controller can do

The controller's policy depends on $y_{0:t}$ via a state estimator (e.g. a Kalman filter) and a feedback law (e.g. LQR). Two states $x, x'$ that produce identical observation trajectories $C_\text{obs} A^k x = C_\text{obs} A^k x'$ for all $k < T$ are observationally indistinguishable to any policy with horizon $\leq T$, regardless of the controller's *cost function* on those states. This is the structural fact the rest of the paper exploits.

---

## 3. Substitution-forcing theorem

We state the substitution-forcing claim in two forms: a static algebraic version (Theorem 1) and a dynamic finite-horizon Gramian version (Proposition 1) that quantifies the substitution magnitude.

### 3.1 Theorem 1 (static observability-asymmetry substitution)

**Theorem 1 (noiseless case).** *Let the observation map be deterministic ($v_t \equiv 0$). Let $x, x' \in \mathbb{R}^n$ be plant states with $C_\text{obs} A^k x = C_\text{obs} A^k x'$ for all $k = 0, \ldots, T-1$, but $q^\top x \neq q^\top x'$ (i.e., distinct values of the nominal target $V$). Then any controller whose policy depends only on $\{y_0, \ldots, y_{T-1}\}$ assigns the same control action sequence to $x$ and $x'$. Consequently, no such controller can regulate $V$ as $V$; the regulable component of any policy is restricted to the projection of $V$ onto the observable subspace.*

*Proof.* By construction the observation trajectories are identical: $y_k = C_\text{obs} A^k x = C_\text{obs} A^k x'$ for all $k < T$. Any policy $K(y_0, \ldots, y_{T-1})$ depends on the trajectory only through these observations and so assigns the same $u_{0:T-1}$ to both initial conditions. The closed-loop trajectory of $V_t = q^\top x_t$ then differs between $x$ and $x'$ — by an amount that propagates the initial-condition difference $q^\top(x - x')$ through the closed loop — without the controller having any policy degree of freedom to track that difference. The controller's regulable target is therefore not $V$ but its projection onto the trajectory-observable subspace, i.e., a proxy $V'$. ∎

*Remark (noisy case).* Adding observation noise $v_t$ does not lift the impossibility: the noiseless argument captures the structural fact that observation geometry forecloses the regulation. When observation noise is present, near-identical observable trajectories produce near-identical control actions; the substitution magnitude is then quantified by Proposition 1 below, with the noise floor entering through the Kalman posterior covariance.

The theorem says nothing about whether the controller's stated cost weights the unobservable component of $V$. It says only that observation geometry already forecloses the regulation: a sincere controller with $q_C = 0$ and a correctly-specified cost is in exactly the same position as a corrupt controller that explicitly swapped $V$ for $V'$.

### 3.2 Proposition 1 (Gramian scaling — diagnostic claim)

**Proposition 1.** *Let $W_o = O_T^\top O_T$ be the finite-horizon observability Gramian. For an LTI system with cost concentrated on a state direction $q$, the steady-state substitution index — the gap between the closed-loop tracking error in $V = q^\top x$ achieved by an ideal observer of $V$ and the tracking error achieved by the available controller — is governed by $|\langle v_\text{min}(O_T), q \rangle|$ and by the conditioning of $W_o$ along $q$. In the simulated regime characterized in §4, the substitution index increases as both quantities increase, independently of controller sincerity or model correctness.*

*Proof sketch.* The Kalman filter's posterior covariance restricted to the cost direction $q$ scales as $q^\top W_o^{-1} q$ at steady state, modulo process and observation noise. When $q$ aligns with $v_\text{min}(O_T)$, this quantity grows as the inverse of the smallest singular value $\sigma_\text{min}(O_T)^2$. The LQR feedback law applied to the resulting estimate $\hat x$ propagates the posterior uncertainty into the closed-loop tracking error; the substitution magnitude is therefore controlled by $|\langle v_\text{min}, q \rangle|$ and by $1/\sigma_\text{min}(O_T)$. The fully general claim (across all $A$, $B$, noise structures) is open; the simulated regime in §4 exhibits monotone scaling in both quantities. ∎

The simulation in §4 traces the empirical scaling: $|\langle v_\text{min}, e_T \rangle|$ varies from $0.9999$ to $0.0439$ as $\alpha_T/\alpha_C$ varies from $0.01$ to $10$, and the substitution magnitude scales correspondingly across two orders of magnitude.

---

## 4. Simulation and Gramian bridge

### 4.1 Single-agent Kalman-LQR setup

A single-agent simulation (`paper25_substitution.py`, available with the companion repository) instantiates the model of §2 with a correctly-specified Kalman-LQR controller. The two-latent process has $T_t$ as a random walk and $C_t$ as an AR(1) process with Poisson crank-shock innovations. Observation $y_t = \alpha_T T_t + \alpha_C C_t + v_t$. Control affects both latents asymmetrically: $b_C = -1.0$, $b_T = -0.05$. The cost function has $q_C = 0$ — the rhetoric-stays-fixed-on-$V$ axiom is baked in at the cost function, not smuggled in through controller misspecification.

### 4.2 Phase-transition sweep

Varying $\alpha_T / \alpha_C$ from $0.01$ to $10$ (five seeds per ratio, 3000 steps each, 500-step burn-in) produces a power-law scaling of substitution magnitude:

| $\alpha_T/\alpha_C$ | $\sigma_\text{min}(O_T)$ | $e_T^\top W_o\, e_T$ | $|\langle v_\text{min}, e_T \rangle|$ | $T_\text{rms}^\text{asym} / T_\text{rms}^\text{clean}$ |
|---:|---:|---:|---:|---:|
| 0.01 | 0.0226 | 0.002 | **0.9999** | 333 |
| 0.05 | 0.1127 | 0.050 | 0.9964 | 175 |
| 0.20 | 0.4278 | 0.80  | 0.9435 | 57  |
| 0.50 | 0.8364 | 5.0   | 0.7145 | 25  |
| 1.00 | 1.0499 | 20.0  | 0.4215 | 13  |
| 2.00 | 1.1248 | 80.0  | 0.2178 | 7.2 |
| 10.0 | 1.1509 | 2000  | **0.0439** | 1.9 |

Reading the table left-to-right, the $T$-axis literally rotates into and out of the observability null-space as the sensor weighting varies. At small $\alpha_T$ the least-observable direction $v_\text{min}$ is essentially the $T$-axis itself (alignment $\approx 1$); at large $\alpha_T$ the alignment has rotated away ($\approx 0$) and the ill-conditioned direction is now the $C$-axis. The substitution magnitude $T_\text{rms}^\text{asym} / T_\text{rms}^\text{clean}$ tracks the alignment column closely, scaling roughly as $(\alpha_T/\alpha_C)^{-0.75}$.

### 4.3 Effort without effect

A second diagnostic isolates the rhetorical payload. At $\alpha_T/\alpha_C = 0.05$: $|U|_\text{asym} = 0.20$ vs $|U|_\text{clean} = 0.09$, with $T_\text{rms}^\text{asym} = 6.8$ vs $T_\text{rms}^\text{clean} = 0.04$. The asymmetric-sensor controller is doing more than twice the control work for $\sim$180× worse tracking. The work is not wasted; it is going into $C$-suppression. The controller's subjective report — its cost function — remains "I am regulating $T$." The actual closed-loop variable being regulated is $C$, because that is where the posterior signal lives.

This is the rhetoric-stays-fixed phenomenon stated in two numbers.

### 4.4 Mechanism confirmation

The LQR gain is $[-2.92, 0]$ across the entire sweep — the controller assigns zero weight to $C$ in its cost function, as the $q_C = 0$ axiom requires. The substitution runs entirely through the Kalman filter: $\hat T$ is pulled around by $C$ because $y = \alpha_T T + \alpha_C C$ and $\alpha_C$ dominates. LQR responds to the contaminated $\hat T$ via $B = [b_T, b_C]^\top$ with $|b_C| = 20|b_T|$, so the same control input mostly suppresses $C$. No misspecification, no wrong beliefs, no corrupted intent — filter geometry alone forces the substitution.

### 4.5 A second substitution channel: shock-statistics mismatch

Even at $\alpha_T/\alpha_C = 10$, $T_\text{rms}^\text{asym} / T_\text{rms}^\text{clean} \approx 1.9$, not unity. The remaining gap arises from the filter's Gaussian model being blindsided by Poisson crank-shock innovations on $C$. A unit-amplitude shock ten times the one-step $C$-sigma arrives instantaneously; the filter, expecting smooth Gaussian $C$-innovations, misattributes part of the resulting $y$-jump to $T$. That drives $\hat T$ up, LQR applies $u$, and the substitution cascade fires — even though $\alpha_T$ is large enough that the smooth-$C$ component would be well-separated.

This widens the necessity claim. Substitution is forced not only by observation-weight asymmetry ($\alpha_T \ll \alpha_C$) but by any systematic mismatch between the filter's assumed state statistics and the real ones on a channel coupled to $y$. The observability-Gramian condition of Proposition 1 is sufficient but not necessary; shock-model mismatch is a second sufficient condition. We do not pursue the shock-statistics channel further in this paper.

### 4.6 Bridge to Paper 23

Paper 23 [1] §3.3 case (ii) — the *measurement null-space masking* result — formalizes the case where a compensator $H_t$ acts in the null space of the measurement map and is observationally invisible to first order over a horizon $T$. The present paper instantiates a different consequence of the same geometric object: the cost-targeted state direction $q$ lies near $\ker(O_T)$, and the closed-loop control problem inherits ill-conditioning. Paper 23 case (ii) is the identity-axis manifestation (compensator invisibility); the present paper is the action-axis manifestation (regulation infeasibility). Both invoke $\ker(O_T)$ or its near-kernel and use it to state distinct closed-loop consequences. The present paper inherits Paper 23's formal apparatus rather than reconstructing it, and theorem statements above cite §3.3 case (ii) directly.

---

## 5. Distinction from Paper 24

Paper 24 [2] names *aggregation-layer masking* as a structurally distinct failure mode of multi-agent epistemic regulation. The present paper is the *spatial substitution* counterpart, sibling rather than nested. The sibling adjudication is algebraic, not empirical:

| | Paper 24 | This paper |
|---|---|---|
| Scale | Organizational governance | Discourse / community moderation (single or multi-agent) |
| Nominal objective | Plant state tracking via $V_t$ | Truth-tracking via epistemic hygiene |
| Failure layer | Aggregation + witness-inclusion filter | Observability-driven target substitution |
| Effect on $V_t$ | *Freezes* against updates | Gets silently *replaced* by $V'_t$ |
| Architectural fix | Shape-preserving aggregation + open witness inclusion | (Open — see §8) |

The substitution mechanism is structurally distinct from freeze. Freezing $V$ is not the same as replacing $V$ with $V'$.

### Algebraic adjudication

Let $N$ homogeneous agents observe the same latent state $x_t = [T_t, C_t]^\top$ through a common measurement map $C_\text{obs} = [\alpha_T, \alpha_C]$ with independent additive noise: $y_{i,t} = C_\text{obs} x_t + v_{i,t}$, $i = 1, \ldots, N$. Stack the observations as $\bar y_t = \bar C x_t + \bar v_t$ with $\bar C = \mathbf{1}_N \otimes C_\text{obs}$. Then:

- The stacked finite-horizon observability matrix $O_T^\text{stack} = \mathbf{1}_N \otimes O_T$. Consequently $\ker(O_T^\text{stack}) = \ker(O_T)$.
- The least-observable direction is unchanged: $v_\text{min}(O_T^\text{stack}) = v_\text{min}(O_T)$ (it is merely scaled).
- The stacked-observation Kalman filter has posterior variance $O(\sigma^2/N)$ — aggregation improves SNR — but the *direction* of residual uncertainty is unchanged.
- The LQR gain depends only on $(A, B, Q, R)$ and is identical to the single-agent case.

**Therefore:** Paper 24's clean aggregation (shape-preserving, open witness inclusion) reduces observation noise but does not rotate the observability subspace. The substitution magnitude scales as $O(1/\sqrt{N})$ of the single-agent case; its direction and structural origin are unchanged. Paper 24's sufficient condition for freeze-freedom is *not* sufficient for substitution-freedom. The mechanisms are independent.

The core line, in one sentence: *aggregation improves SNR; it does not rotate the observability subspace.*

**Subspace, not vector.** A technical caveat is worth making explicit. When the smallest singular value of $O_T$ is degenerate, there is no distinguished "least observable direction" $v_\text{min}$; the invariant claim of the algebraic argument is about the unobservable subspace, not a privileged vector. Concretely, homogeneous-witness replication scales the Gramian,

$$
(\mathbf{1}_N \otimes O_T)^\top (\mathbf{1}_N \otimes O_T) = N \cdot O_T^\top O_T,
$$

preserving its eigenspaces (and in particular its kernel) and multiplying its eigenvalues by $N$. Aggregation improves weight along already-observed directions; it does not create epistemic access to a direction outside the observation subspace. The kernel-preservation and Gramian-scaling claims are recorded as Lean theorems in `LeanProofs/Paper25EpistemicBorderControl.lean` in the companion proofs repository.

### Scope condition for the algebraic argument

Homogeneity of the measurement map across agents is load-bearing. Heterogeneous agents with genuinely different measurement maps $C_\text{obs}^{(i)}$ — for instance, a privileged witness with access to $T$ through a different sensor channel — *can* rotate the effective observability subspace, and the sibling claim does not extend to that case without further argument. The heterogeneous-agent extension is a Paper 24/25 follow-on object — *what cohort-witness composition restores $T$-observability?* — not part of the sibling-vs-nested decision.

---

## 6. Distinction from Goodhart and from performative prediction

This section is the principal "not just X" firewall. The contribution depends on holding a sharper edge than the adjacent literatures supply.

### 6.1 vs Goodhart's Law

Goodhart's Law and its descendants describe a *contingent corruption*: when a measure becomes a target, optimization pressure tends to game the measure. The literature treats this as a problem amenable to better metrics, more robust measures, or counterfactual auditing.

The present claim is *necessity-framed*. When the underlying target has no real-time sensor at all — when $T$ does not enter the observation map $C_\text{obs}$ — no metric is being gamed, because the target was never available to optimize against in the first place. The controller is not corrupted; the controller is structurally barred from regulating $T$. Sincere intent does not save it. The substitution is forced by sensor geometry.

The pithy form: Goodhart says *the measure is gamed*. The present claim says *the target never entered the controller*. Different pathology, different remedy: Goodhart can in principle be avoided by replacing the gamed metric with a less-gameable one; observability-asymmetry substitution can only be avoided by restoring the $T$-channel itself, which is by hypothesis unavailable.

The strongest opposing form is Manheim and Garrabrant's [3] classification of Goodhart variants — *regressional, extremal, causal, adversarial* — which collectively cover the family of failures that can occur when a proxy is selected, optimized, sampled, selected on, or adversarially exploited. Each variant assumes a regime in which a proxy has already been chosen and is being relied upon, and each describes a way in which reliance fails. The present paper names a *prior* condition: the nominal target is outside the controller's observation channel, so the proxy is not merely selected badly. It is the only regulable object available. None of the four Goodhart variants applies *before* a proxy has been selected; all four describe what happens *to* a proxy under optimization pressure. Observability-asymmetry substitution names what happens *because the controller cannot do otherwise* — the regulable surface itself is foreclosed by sensor geometry, prior to any optimization pressure on whatever proxy is reached for next.

### 6.2 vs performative prediction (Perdomo et al. [4])

Performative prediction names the phenomenon where a model's predictions shape the data distribution it later trains on. The closed loop is between model output and environment response. The mathematical apparatus addresses convergence to *performatively stable* points and the gap between performatively stable and performatively optimal solutions.

The present claim does not require performativity. The substitution arises *before* the controller's actions perturb the environment, by virtue of the sensor map alone. A controller observing a static distribution through a $T$-blind sensor still substitutes $V'$ for $V$. Performative prediction is a separate (and stackable) failure mode; the present paper isolates the sensor-geometry channel.

### 6.3 vs feedback-loop classifications (Pagan et al. [5])

Pagan et al. give a five-type classification of feedback loops in automated decision-making — *individual, feature, outcome, ML-model, sampling* — and trace how each contributes to bias amplification under retraining. Their taxonomy is broad enough that the present mechanism could be located within it (loosely, a feature-loop instance), but they do not name observability-driven target substitution as a distinct failure mode with a distinct architectural remedy: their loops are about how proxies get *amplified* once selected, not about how the structural unavailability of a real-time target sensor *forces* a proxy in the first place. The present paper is one entry their classification leaves implicit, given a closed-loop formal characterization.

### 6.4 vs recommender-system control models (Sprenger et al. [6])

Sprenger et al. give a closed-loop control formalization of recommender systems acting on opinion dynamics in social networks, with engagement maximization as the controller objective and full state visibility on the network. The present paper shares the control-theoretic posture but operates on a different surface and isolates a different pathology: target substitution forced by sensor-map asymmetry, rather than equilibrium drift under engagement-maximizing closed loops with observable state. Their model is closer to *what happens once the controller can see everything and is optimizing the wrong thing*; the present paper is *what happens when the controller cannot see what it is rhetorically trying to optimize*.

### 6.5 vs platform-moderation theoretical models

Existing theoretical work on platform moderation — Dwork et al.'s [7] window-based moderation framework, in which a platform chooses a content-moderation window and users decide whether to participate based on the fraction of admitted content aligning with their preferences — addresses domain-specific balancing under explicit policy regimes with platform-side visibility into content positions. The present paper does not claim to cover formal platform moderation: those systems have explicit policy documents that can be revised in response to errors and explicit fact-checking apparatus that constitute partial $T$-sensors. The mechanism named here applies to *informal* discourse regulators (academics, journalists, ad-hoc moderators, professional pundits, coalition enforcers) where no formal $T$-sensor exists. Dwork et al.'s framework is the natural sibling for the formal-platform case; the present paper sits where their assumed observability does not hold.

---

## 7. Worked example: local data center opposition

We work one example in detail. The example is drawn from informal discourse at the county / regional / local-coalition level, not from a formal platform-moderation case. The scope conditioning of §6.5 applies.

A county learns a large data center is coming in with tax abatements, heavy power demand, opaque procurement, and possible strain on water or grid infrastructure.

A local critic posts about sweetheart deals, infrastructure burden, contract secrecy, surveillance-contract adjacency, and long-term public cost vs private gain. Some claims are documentable; some are speculative. Nearby posters add "they're hiding the real purpose," "this is AI mind control," "they're poisoning the aquifer on purpose," and generic 5G/UFO sludge.

**What the regulatory system says it is regulating ($V$):** truth, epistemic hygiene, anti-conspiracist discipline, keeping bad claims from spreading.

**What it can actually observe quickly ($y_t$, which loads on $V'$):** whether the topic is attracting cranks; whether the rhetoric resembles prior contamination genres; whether embarrassing people are piling in; whether engaging creates coalition or reputational risk; whether the discourse smells like *just asking questions*.

**What it cannot observe in real time:** true infrastructure burden; real subsidy structure; extent of institutional concealment; actual future harms.

**What happens next.** Journalists, academics, posters, and informal moderators cannot quickly resolve the object-level questions. They can quickly observe that the topic is getting weird, the discourse is aesthetically contaminated, and continued engagement carries reputational cost. Control action fires: dismissive framing, *this is how 5G/UFO nonsense starts*, policing *just asking questions* as such, treating continued curiosity as epistemic defect, steering everyone away rather than separating claims within the discourse.

The system is no longer regulating for "truth about the project." It is regulating for distance from contamination, reputational safety, coalition legibility, avoidance of inferential slippage. *The rhetoric stays fixed* — people still say they are protecting truth, reason, and anti-bullshit norms — but the operational target has switched.

**Why the example earns its keep.** The object-level question never got cleanly answered. The system did *not* establish that the project is benign, the harms are fake, the contracts fine, the concerns unfounded. It established that the topic is risky to entertain in an undifferentiated public way, that the social cost of granular inspection is too high, that topic suppression is safer than claim separation. The mechanism is visible in the outcome: the regulable variable is $C$, the rhetoric is fixed on $T$, the gap persists.

The example is ugly in exactly the right way. There are real object-level concerns; the topic also attracts spectacle and paranoia; institutions have incentives to bullshit; coalition actors are terrified of being seen as adjacent to woo. Concrete without being cartoonish.

### Sibling instantiations (brief)

The same mechanism applies, with surface adjustments, to:

- **Recommender / ML systems** where the deployment objective (e.g. user well-being, long-run engagement quality) is hard to sense in real time but proxies (clicks, dwell time, immediate engagement) are cheap and fast.
- **Data-center / cloud operations** where the operational target (e.g. customer outcome quality, or substrate-level reliability) is slow and expensive to measure but proxies (SLI dashboards, alert volume) are cheap and fast.
- **Compliance / audit regimes** where the regulated target (e.g. genuine ethical conduct) is unsensed but proxies (paperwork completion, training-module completion rates) are cheap.

These are not developed here; the present paper isolates the mechanism on a single example to keep the contribution sharp.

---

## 8. Architectural implication and open problems

The constructive consequence of Theorem 1 is essentially negative: there is no controller modification that can recover $T$-tracking when $T$ is genuinely unobservable. The mechanism is forced.

The architectural moves that are *not* foreclosed:

- **Restore the $T$-channel.** If a slow, expensive, but real $T$-sensor exists, install it and accept its latency. The controller can then track $T$ at the sensor's rate. This is the one structural escape and it is often unavailable in the cases the paper is concerned with.
- **Refuse to collapse $T$ and $V'$ into a single regulated variable.** Maintain separate accounting for the observable proxy and the unobservable target. Permit action under the proxy regime, but deny rhetorical closure: refuse to claim that controlling $V'$ amounts to controlling $V$.
- **Witness-cohort heterogeneity.** Different agents with genuinely different $C_\text{obs}^{(i)}$ — for instance, witnesses positioned to observe $T$ through different channels — *can* rotate the effective observability subspace. This does not contradict Theorem 1 within an agent; it changes the effective $C_\text{obs}$ at the cohort level. Paper 24's witness-inclusion machinery becomes relevant here as the architecture for keeping the heterogeneity intact under aggregation.

The third path is the most tractable and connects back to Paper 24 [2] and to the Governor / admissibility working track: separate sensor channels, separate admissibility accounting, separate update rules for each latent. None of these is a complete remedy; the unobservable component of $T$ remains unobservable. What changes is whether the system rhetorically conflates the regulable $V'$ with the nominal $V$, and whether the cohort can supply observation channels that the single agent cannot.

### Open problems

1. **Quantitative version of Theorem 1.** Theorem 1's clean statement uses identical observation trajectories as the hypothesis. A version with near-identical trajectories under noise plus a quantitative bound in terms of $|\langle v_\text{min}, q \rangle|$ and $\sigma_\text{min}(O_T)$ is the natural sharpening. Proposition 1 gives the form; promotion to a full theorem with explicit constants is open.
2. **Heterogeneous-cohort analysis.** What cohort composition $\{C_\text{obs}^{(i)}\}$ restores $T$-observability at the cohort level? When does it fail to under aggregation rules borrowed from Paper 24?
3. **Compound-regime sim.** Does Paper 24's witness-filter pathology stack with the present substitution mechanism, and what is the joint scaling? The algebraic adjudication of §5 establishes independence of the two mechanisms in the homogeneous case; the heterogeneous extension is where stacking would matter.
4. **Hysteresis and asymmetric thresholds.** Threshold asymmetry in topic-classification (lower bar to enter "suspect" status than to leave) is a sibling pathology that the present model does not encode. Worth a separate treatment.

---

## References

[1] Beck, J. (2026). The Non-Self-Identical Controller. Δt Framework series, Paper 23. Zenodo. doi:10.5281/zenodo.19055415

[2] Beck, J. (2026). Shared Vision as Coordinating Prior. Δt Framework series, Paper 24. Zenodo. doi:10.5281/zenodo.19861995

[3] Manheim, D., & Garrabrant, S. (2018). Categorizing Variants of Goodhart's Law. arXiv:1803.04585.

[4] Perdomo, J. C., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative Prediction. *Proceedings of the 37th International Conference on Machine Learning*, PMLR 119:7599–7609. arXiv:2002.06673.

[5] Pagan, N., Baumann, J., Elokda, E., De Pasquale, G., Bolognani, S., & Hannák, A. (2023). A Classification of Feedback Loops and Their Relation to Biases in Automated Decision-Making Systems. *Proceedings of the 3rd ACM Conference on Equity and Access in Algorithms, Mechanisms, and Optimization* (EAAMO '23). doi:10.1145/3617694.3623227. arXiv:2305.06055.

[6] Sprenger, B., De Pasquale, G., Soloperto, R., Lygeros, J., & Dörfler, F. (2024). Control strategies for recommendation systems in social networks. *IEEE Control Systems Letters*, 8.

[7] Dwork, C., Hays, C., Kleinberg, J., & Raghavan, M. (2024). Content Moderation and the Formation of Online Communities: A Theoretical Framework. *Proceedings of the ACM Web Conference 2024*. doi:10.1145/3589334.3645490. arXiv:2310.10573.
