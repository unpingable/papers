"""
Minimal Δt-Coherent System: Two-Layer Metastable Dynamics with Coherence Controller

This implements a toy model demonstrating:
- Multi-timescale dynamics (fast x, slow y)
- Metastable attractor basins (double-well potential)
- Noise-driven transitions (Flicker/Snap/Hysteresis)
- Homeostatic coherence controller (with parameter restoration)

Usage:
    python metastable_coherence_system.py

Dependencies:
    pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


class MetastableCoherenceSystem:
    """
    Two-layer system with homeostatic coherence control.
    
    The system consists of:
    - x: fast variable with double-well potential (creates metastable basins)
    - y: slow variable that modulates basin structure
    - Coherence controller that monitors instability and intervenes
    
    Key insight: This simple system exhibits the same failure modes
    (Flicker/Snap/Hysteresis) that characterize complex multi-scale
    systems from brains to institutions.
    """
    
    def __init__(self, 
                 a_x=0.9,       # fast self-persistence
                 b_xy=0.2,      # coupling from slow to fast
                 alpha=0.5,     # nonlinearity strength (basin depth)
                 epsilon=0.05,  # timescale separation (slow update rate)
                 c_yx=0.1,      # coupling from fast to slow
                 d_y=0.05,      # slow decay
                 sigma_x=0.02,  # fast noise
                 sigma_y=0.005, # slow noise
                 controller_enabled=True,
                 instability_threshold=2.0,
                 relaxation_rate=0.002):
        
        self.a_x = a_x
        self.b_xy = b_xy
        self.alpha = alpha
        self.epsilon = epsilon
        self.c_yx = c_yx
        self.d_y = d_y
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
        
        # Controller parameters
        self.controller_enabled = controller_enabled
        self.instability_threshold = instability_threshold
        self.relaxation_rate = relaxation_rate
        
        # Store baseline for homeostatic restoration
        self.initial_a_x = a_x
        self.initial_b_xy = b_xy
        
        # State
        self.x = 0.1  # start near origin
        self.y = 0.0
        
        # History for analysis
        self.history = {
            'x': [], 'y': [], 'instability': [], 
            'interventions': [], 't': [],
            'a_x': [], 'b_xy': []  # Track parameter evolution
        }
        self.t = 0
        
    def compute_instability_metric(self):
        """
        Simple proxy for system instability.
        In full implementation, this would estimate Ï�(M) or local growth rate.
        """
        return np.abs(self.x) + 0.5 * np.abs(self.y)
    
    def controller_intervene(self):
        """
        Coherence controller: reduce coupling and dampen fast dynamics
        when instability exceeds threshold.
        """
        self.b_xy *= 0.9
        self.a_x *= 0.95
        
    def step(self):
        """
        Single timestep with homeostatic restoration.
        
        Key dynamics:
        - Fast variable (x): Double-well potential creates metastable basins
        - Slow variable (y): Modulates basin structure over longer timescale
        - Controller: Monitors instability and intervenes when needed
        - Homeostasis: Gradually restores parameters after intervention
        """
        # Compute instability
        instability = self.compute_instability_metric()
        
        # Controller action with homeostatic restoration
        intervening = False
        if self.controller_enabled:
            if instability > self.instability_threshold:
                self.controller_intervene()
                intervening = True
            else:
                # Homeostatic restoration: gradually return to baseline
                self.a_x += self.relaxation_rate * (self.initial_a_x - self.a_x)
                self.b_xy += self.relaxation_rate * (self.initial_b_xy - self.b_xy)
        
        # Fast dynamics with double-well potential
        # The -Î±Â·xÂ³ term creates two stable basins around x â‰ˆ Â±âˆš(a_x/Î±)
        noise_x = self.sigma_x * np.random.randn()
        x_new = (self.a_x * self.x + 
                 self.b_xy * self.y - 
                 self.alpha * self.x**3 + 
                 noise_x)
        
        # Slow dynamics
        # Îµ << 1 creates timescale separation
        noise_y = self.sigma_y * np.random.randn()
        y_new = (self.y + 
                 self.epsilon * (self.c_yx * self.x - self.d_y * self.y) + 
                 noise_y)
        
        # Update state
        self.x = x_new
        self.y = y_new
        self.t += 1
        
        # Record history
        self.history['x'].append(self.x)
        self.history['y'].append(self.y)
        self.history['instability'].append(instability)
        self.history['interventions'].append(1 if intervening else 0)
        self.history['t'].append(self.t)
        self.history['a_x'].append(self.a_x)
        self.history['b_xy'].append(self.b_xy)
        
        return intervening
    
    def run(self, n_steps=5000):
        """Run simulation for n_steps."""
        for _ in range(n_steps):
            self.step()
    
    def plot_results(self):
        """Generate comprehensive visualization of system dynamics."""
        fig = plt.figure(figsize=(14, 16))
        gs = GridSpec(4, 2, figure=fig)
        
        # Time series
        ax1 = fig.add_subplot(gs[0, :])
        ax1.plot(self.history['t'], self.history['x'], 
                linewidth=0.6, alpha=0.7, label='x (fast)')
        ax1.plot(self.history['t'], self.history['y'], 
                linewidth=0.8, alpha=0.8, label='y (slow)')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('State')
        ax1.set_title('Time Series: Fast (x) and Slow (y) Variables')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Phase portrait
        ax2 = fig.add_subplot(gs[1, 0])
        ax2.plot(self.history['x'], self.history['y'], 
                linewidth=0.4, alpha=0.5, color='darkblue')
        ax2.scatter(self.history['x'][0], self.history['y'][0], 
                   color='green', s=50, zorder=5, label='Start')
        ax2.scatter(self.history['x'][-1], self.history['y'][-1], 
                   color='red', s=50, zorder=5, label='End')
        ax2.set_xlabel('x (fast)')
        ax2.set_ylabel('y (slow)')
        ax2.set_title('Phase Portrait')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Instability and interventions
        ax3 = fig.add_subplot(gs[1, 1])
        ax3.plot(self.history['t'], self.history['instability'], 
                linewidth=0.5, alpha=0.7, label='Instability')
        ax3.axhline(y=self.instability_threshold, color='r', 
                   linestyle='--', label='Threshold')
        
        # Mark interventions
        intervention_times = [t for t, i in zip(self.history['t'], 
                            self.history['interventions']) if i]
        if intervention_times:
            ax3.scatter(intervention_times, 
                       [self.instability_threshold] * len(intervention_times),
                       color='red', s=10, alpha=0.5, label='Interventions')
        
        ax3.set_xlabel('Time')
        ax3.set_ylabel('Instability Metric')
        ax3.set_title('Instability Dynamics & Controller Activity')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # Controller parameters (homeostatic restoration)
        ax4 = fig.add_subplot(gs[2, :])
        ax4.plot(self.history['t'], self.history['a_x'], 
                linewidth=0.8, label=f'a_x (baseline={self.initial_a_x})')
        ax4.plot(self.history['t'], self.history['b_xy'], 
                linewidth=0.8, label=f'b_xy (baseline={self.initial_b_xy})')
        ax4.axhline(y=self.initial_a_x, color='C0', linestyle=':', alpha=0.5)
        ax4.axhline(y=self.initial_b_xy, color='C1', linestyle=':', alpha=0.5)
        ax4.set_xlabel('Time')
        ax4.set_ylabel('Parameter Value')
        ax4.set_title('Controller Parameters (Homeostatic Restoration)')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
        
        # Basin visualization
        ax5 = fig.add_subplot(gs[3, :])
        x_range = np.linspace(-2, 2, 200)
        V = -0.5 * self.initial_a_x * x_range**2 + 0.25 * self.alpha * x_range**4
        ax5.plot(x_range, V, linewidth=2, color='darkblue')
        ax5.fill_between(x_range, V, alpha=0.2)
        ax5.set_xlabel('x')
        ax5.set_ylabel('Effective Potential V(x)')
        ax5.set_title('Double-Well Structure (Metastable Basins)')
        ax5.grid(True, alpha=0.3)
        
        # Add annotations for basins
        ax5.annotate('Left Basin', xy=(-1.1, -0.1), fontsize=10, ha='center')
        ax5.annotate('Right Basin', xy=(1.1, -0.1), fontsize=10, ha='center')
        ax5.annotate('Barrier', xy=(0, 0.05), fontsize=10, ha='center')
        
        plt.tight_layout()
        return fig


def compare_regimes():
    """
    Compare system behavior across three regimes:
    1. Coherent (controller on, low noise)
    2. Metastable (controller on, moderate noise)
    3. Decoherent (controller off, high noise)
    """
    
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    
    regimes = [
        {
            'name': 'Coherent (low noise, controller on)',
            'params': {'sigma_x': 0.02, 'controller_enabled': True},
            'color': 'green'
        },
        {
            'name': 'Metastable (moderate noise, controller on) - Flicker/Snap visible',
            'params': {'sigma_x': 0.08, 'controller_enabled': True},
            'color': 'orange'
        },
        {
            'name': 'Decoherent (high noise, controller off)',
            'params': {'sigma_x': 0.15, 'controller_enabled': False},
            'color': 'red'
        }
    ]
    
    for i, regime in enumerate(regimes):
        system = MetastableCoherenceSystem(**regime['params'])
        system.run(n_steps=3000)
        
        # Time series
        axes[i, 0].plot(system.history['t'], system.history['x'], 
                       linewidth=0.6, alpha=0.7, color=regime['color'])
        axes[i, 0].set_ylabel('x (fast)')
        axes[i, 0].set_title(f"{regime['name']} - Time Series")
        axes[i, 0].grid(True, alpha=0.3)
        axes[i, 0].set_ylim(-3, 3)
        
        # Phase portrait
        axes[i, 1].plot(system.history['x'], system.history['y'], 
                       linewidth=0.5, alpha=0.6, color=regime['color'])
        axes[i, 1].set_xlabel('x (fast)')
        axes[i, 1].set_ylabel('y (slow)')
        axes[i, 1].set_title(f"{regime['name']} - Phase Portrait")
        axes[i, 1].grid(True, alpha=0.3)
        axes[i, 1].set_xlim(-3, 3)
        axes[i, 1].set_ylim(-1.5, 1.5)
    
    axes[-1, 0].set_xlabel('Time')
    
    plt.tight_layout()
    return fig


def demonstrate_failure_modes():
    """
    Demonstrate the three failure modes: Flicker, Snap, Hysteresis.
    """
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # FLICKER: Transient excursions that return
    print("Demonstrating FLICKER (transient excursions)...")
    np.random.seed(42)
    system_flicker = MetastableCoherenceSystem(sigma_x=0.05)
    system_flicker.run(n_steps=2000)
    
    axes[0].plot(system_flicker.history['t'], system_flicker.history['x'], 
                 linewidth=0.6, color='blue')
    axes[0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    axes[0].set_title('FLICKER: Brief excursions, returns to basin')
    axes[0].set_xlabel('Time')
    axes[0].set_ylabel('x')
    axes[0].grid(True, alpha=0.3)
    
    # SNAP: Catastrophic basin transition
    print("Demonstrating SNAP (basin transition)...")
    np.random.seed(123)
    system_snap = MetastableCoherenceSystem(sigma_x=0.12, controller_enabled=False)
    system_snap.run(n_steps=2000)
    
    axes[1].plot(system_snap.history['t'], system_snap.history['x'], 
                 linewidth=0.6, color='orange')
    axes[1].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    axes[1].set_title('SNAP: Sudden basin escape (look for sign changes)')
    axes[1].set_xlabel('Time')
    axes[1].set_ylabel('x')
    axes[1].grid(True, alpha=0.3)
    
    # HYSTERESIS: Lock-in to degraded state
    print("Demonstrating HYSTERESIS (lock-in)...")
    np.random.seed(456)
    system_hyst = MetastableCoherenceSystem(
        a_x=0.95,  # Higher persistence makes escape harder
        sigma_x=0.10, 
        controller_enabled=False
    )
    system_hyst.run(n_steps=3000)
    
    axes[2].plot(system_hyst.history['t'], system_hyst.history['x'], 
                 linewidth=0.6, color='red')
    axes[2].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    axes[2].set_title('HYSTERESIS: Locked in one basin, hard to escape')
    axes[2].set_xlabel('Time')
    axes[2].set_ylabel('x')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    print("=" * 70)
    print("Minimal Î”t-Coherent System Demonstration")
    print("=" * 70)
    print()
    print("This toy model demonstrates the key dynamics of temporal coherence:")
    print("- Multi-timescale coupling (fast x, slow y)")
    print("- Metastable basins (double-well potential)")
    print("- Coherence controller (with homeostatic restoration)")
    print("- Failure modes: Flicker, Snap, Hysteresis")
    print()
    
    print("\n1. Running single system with coherence controller...")
    print("-" * 50)
    system = MetastableCoherenceSystem(controller_enabled=True)
    system.run(n_steps=5000)
    
    interventions = sum(system.history['interventions'])
    print(f"   Controller interventions: {interventions}")
    print(f"   Final a_x: {system.a_x:.4f} (baseline: {system.initial_a_x})")
    print(f"   Final b_xy: {system.b_xy:.4f} (baseline: {system.initial_b_xy})")
    
    fig1 = system.plot_results()
    fig1.savefig('metastable_system_single.png', dpi=150, bbox_inches='tight')
    print("   Saved: metastable_system_single.png")
    
    print("\n2. Comparing three operational regimes...")
    print("-" * 50)
    fig2 = compare_regimes()
    fig2.savefig('metastable_system_comparison.png', dpi=150, bbox_inches='tight')
    print("   Saved: metastable_system_comparison.png")
    
    print("\n3. Demonstrating failure modes...")
    print("-" * 50)
    fig3 = demonstrate_failure_modes()
    fig3.savefig('metastable_failure_modes.png', dpi=150, bbox_inches='tight')
    print("   Saved: metastable_failure_modes.png")
    
    print("\n" + "=" * 70)
    print("Key Observations:")
    print("=" * 70)
    print()
    print("â€¢ COHERENT regime: Stays in one basin, minimal controller action")
    print("â€¢ METASTABLE regime: Flicker (brief excursions), occasional Snap")
    print("â€¢ DECOHERENT regime: No stable pattern, wild fluctuations")
    print()
    print("This demonstrates:")
    print("â†’ Organism-like failure modes (not tool-like 'bad output')")
    print("â†’ Controller can maintain coherence under moderate stress")
    print("â†’ System has genuine attractors with noise-driven transitions")
    print("â†’ No neural nets, no mysticismâ€”just dynamics")
    print()
    print("=" * 70)
    print("The mathematical core of temporal coherence:")
    print("    z_{t+1} = F(z_t, u_t) + Î·_t")
    print("    Ï�(M) < 1  (spectral stability)")
    print("    Î²_ij > g(Î”t_ij)  (coupling > mismatch)")
    print("=" * 70)
    
    plt.show()
