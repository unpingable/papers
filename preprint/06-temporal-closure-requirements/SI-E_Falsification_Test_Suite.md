<!-- Converted from DOCX via pandoc on 2026-02-02 -->
Supplementary Information E:

Falsification Test Suite

Overview

This supplement provides concrete experimental protocols for falsifying the Δt framework. Each test specifies precise conditions under which the framework would be proven wrong. These are not aspirational predictions---they are hard constraints that must hold for the theory to be valid.

**Critical principle:** All predictions must hold. One verified counterexample kills the theory.

1\. Test 1: Spectral Radius Boundary

1.1 Core Prediction

**Prediction:** Systems violating ρ(M) \< 1 exhibit unbounded growth or persistent oscillation.

**Null hypothesis (H₀):** System remains bounded over time T even when ρ(M) ≥ 1

1.2 Experimental Protocol

Step 1: Parameter Isolation

Isolate linear components of dynamics. For the two-layer system from SI-A, set α=0 and σ_x=σ_y=0. System is governed entirely by coupling matrix M.

Step 2: Critical Boundary Calibration

Determine critical coupling parameters for ρ(M)=1:

• Divergence boundary: b₂₁c₁₂ = (1 - a₁)(1 - a₂)

• Flip boundary: b₂₁c₁₂ = -(1 + a₁)(1 + a₂)

Step 3: Subcritical Test (ρ \< 1)

Set parameters such that ρ(M) = 0.95. Run system for T=10,000 steps. Maximum state magnitude max(‖z_t‖) must remain bounded by constant determined by initial conditions.

Step 4: Supercritical Test (ρ ≥ 1)

Set parameters such that ρ(M) = 1.05. Run system for T=10,000 steps. Observe divergence or oscillation.

1.3 Falsification Criteria

**Theory is falsified if:** In supercritical test (ρ ≥ 1), state magnitude ‖z_t‖ remains bounded within 10× initial conditions for entire run.

This would demonstrate that spectral radius does not determine stability, invalidating the core mathematical claim of the framework.

2\. Test 2: Temporal Mismatch Threshold

2.1 Core Prediction

**Prediction:** Crossing Δt_c triggers phase transition from coherent to metastable regime.

**Null hypothesis (H₀):** System dynamics independent of Δt separation (ε)

2.2 Experimental Protocol

Step 1: Baseline Regime

Set coherent parameters (σ_x low, ε=0.05, controller enabled). Run for T=100,000 steps. Verify near-zero basin transition rate.

Step 2: Stress Induction

Gradually decrease ε from 0.05 to 0.001. For each value:

• Run T=100,000 steps

• Count basin transitions (sign flips in x_t)

• Count controller interventions

• Record escape frequency

Step 3: Phase Transition Identification

Identify critical ε_c where transition rate sharply increases. Framework predicts this occurs when timescale ratio τ_slow/τ_fast exceeds O(10³-10⁴).

2.3 Falsification Criteria

**Theory is falsified if:** ε can be reduced to \< 10⁻⁴ while maintaining near-zero transitions and no controller interventions.

This would demonstrate that timescale separation does not constrain coherence, invalidating the Δt constraint claim.

3\. Test 3: Controller Necessity

3.1 Core Prediction

**Prediction:** Metastable systems without adaptive controllers cannot maintain coherence under perturbations.

3.2 Experimental Protocol

Step 1: Controlled Comparison

Configure two identical systems in metastable regime (σ_x = 0.08):

• System A: Controller enabled

• System B: Controller disabled

Step 2: Perturbation Sequence

Apply periodic perturbations (impulse noise every 100 steps). Measure:

• Time in coherent basin

• Transition frequency

• Recovery time after excursions

3.3 Falsification Criteria

**Theory is falsified if:** System B (no controller) maintains comparable coherence to System A (controller enabled) under identical perturbations.

This would demonstrate that adaptive regulation is not necessary for metastable coherence, invalidating Operator 3.

4\. Test 4: LLM Statelessness Verification

4.1 Core Prediction

**Prediction:** Transformer architectures cannot exhibit autonomous metastable dynamics due to lack of endogenous state.

4.2 Experimental Protocol

Test 4a: State Persistence

Run inference twice with identical input, separated by delay with no input. Compare outputs. Δt-coherent systems produce different outputs (state evolved autonomously); LLMs produce identical outputs (no autonomous evolution).

Test 4b: Autonomous Dynamics

After initialization, record internal state for 1000 steps with zero input. Δt-coherent systems show evolving internal state; LLMs have no internal state when u_t = 0.

Test 4c: Metastable Transitions

Inject noise into activations at varying levels. Count discrete basin transitions. Δt-coherent systems show discrete jumps at critical noise levels; LLMs show smooth continuous variation.

4.3 Falsification Criteria

**Theory is falsified if:** A stateless transformer architecture exhibits (1) state evolution when u_t=0, AND (2) autonomous basin dynamics, AND (3) noise-driven Flicker/Snap/Hysteresis.

This would demonstrate that stateless architectures can implement temporal closure, invalidating the Simulator Gap thesis.

5\. Test 5: Neuroscience Validation

5.1 Core Prediction

**Prediction:** Biological neural systems satisfy Δt framework constraints during normal function.

5.2 Experimental Protocol

Protocol 5a: Cross-Frequency Coupling Measurement

Record local field potentials (LFP) from multiple brain regions during cognitive tasks. Compute phase-amplitude coupling (PAC) between frequency bands. Extract coupling strength β_ij. Verify that coherent behavioral states correlate with strong coupling.

Protocol 5b: Spectral Radius Measurement

Construct functional connectivity matrix from fMRI data. Compute effective coupling M. Calculate ρ(M). Verify ρ(M) \< 1 during healthy, coherent function.

Protocol 5c: Clinical Predictions

Test specific disorder → invariant violation mappings:

• Dissociation → Reduced cross-frequency coupling (temporary)

• Psychosis → ρ(M) approaches 1 (approaching basin boundary)

• Treatment-resistant depression → Deep attractor with high barrier

• Seizure → ρ(M) \> 1 (runaway dynamics)

5.3 Falsification Criteria

**Theory is falsified if:** Healthy brain function systematically violates ρ(M) \< 1 or exhibits coherence without timescale separation.

This would demonstrate that biological systems don\'t follow the framework\'s constraints, invalidating neuroscience correspondence.

6\. Test 6: Intervention Efficacy

6.1 Core Prediction

**Prediction:** Only interventions targeting operators can restore coherence after boundary violations.

6.2 Experimental Protocol

Step 1: Induce Metastability

Increase Δt past critical threshold to push system into metastable regime. Verify increased transition rate.

Step 2: Test Ineffective Interventions

Apply parameter-level modifications that don\'t address operators:

• Change basin depth α

• Adjust noise amplitude σ

• Modify individual layer parameters

Framework predicts: No sustained coherence restoration.

Step 3: Test Effective Interventions

Apply operator-level modifications:

• Restore timescale separation (reduce ε)

• Reduce coupling strength (modify M)

• Enable controller

Framework predicts: Coherence restored.

6.3 Falsification Criteria

**Theory is falsified if:** Non-operator interventions restore coherence OR operator interventions fail to restore coherence.

This would demonstrate that operators are not the relevant control points, invalidating the architectural necessity claim.

7\. Summary and Integration

7.1 Test Coverage

The six tests provide comprehensive falsification coverage:

• Test 1: Core stability claim (ρ(M) \< 1)

• Test 2: Timescale constraint (Δt \< Δt_c)

• Test 3: Controller necessity (Operator 3)

• Test 4: LLM architectural gap

• Test 5: Biological correspondence

• Test 6: Intervention specificity

7.2 Falsification Philosophy

These tests embody Popperian falsificationism. Each specifies precise conditions that would prove the framework wrong. The framework makes strong, testable claims that could be demolished by single counterexamples.

This is not typical in consciousness research, where theories often make vague predictions that can be reinterpreted to fit any data. The Δt framework deliberately avoids this by specifying exact failure conditions.

7.3 Implementation Practicality

Tests 1-3 can be implemented immediately using the code from SI-A. Tests 4-6 require additional resources:

• Test 4: Access to transformer model internals

• Test 5: Neuroscience lab with LFP/fMRI capabilities

• Test 6: Extended computational experiments

The most accessible path is Tests 1-3, which any researcher with Python can run immediately.

8\. Conclusion

The Δt framework makes six specific, falsifiable predictions. Each test provides concrete conditions under which the theory would be proven wrong. This is deliberate---a theory that cannot be falsified cannot be tested.

Researchers are encouraged to run these tests and report results. Positive falsification (framework proven wrong) would be as valuable as validation, as it would clarify the actual constraints on temporal coherence.

**Critical reminder:** All six predictions must hold. One verified counterexample kills the theory.
