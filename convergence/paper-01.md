# Paper 01 — Coherence Criterion — Convergence Spike

**Full title:** The Coherence Criterion: A Unified Framework for Stability in Hierarchical Systems
**Date:** 2025-11-26
**DOI:** 10.5281/zenodo.17726789

## Status: completed (2026-03-18)

## Claim Cluster
- System stability in hierarchical multi-timescale systems requires bounded temporal divergence between coupled layers, formalized as spectral radius ρ(M) < 1
- Violation of the coherence criterion produces two distinct failure modes: Rigidity Runaway (λ → +1) and Acceleration Runaway (λ → −1)
- These failure modes share a common bifurcation geometry across autonomous systems, learning architectures, institutions, and financial markets
- Coupled Markov processes provide the correct formalism for analyzing temporal divergence between hierarchical layers

## Search Terms
- spectral radius stability condition hierarchical systems
- multi-timescale coupling stability bifurcation
- temporal mismatch failure modes dynamical systems
- coupled Markov processes hierarchical control
- rigidity vs acceleration failure modes organizations
- spectral stability cross-scale coupling
- bifurcation geometry institutional collapse
- hierarchical dynamical systems temporal coherence

## Expected Convergence Level
partial convergence likely
Spectral radius conditions for stability are well-established in control theory and dynamical systems. The novel contribution is applying them specifically to temporal divergence across hierarchical layers and identifying the two named failure modes. Independent work on multi-scale dynamical systems likely reaches structurally similar conclusions.

## Hits

### Structural Matches (independent work reaching structurally similar conclusions)

**1. CTHA: Constrained Temporal Hierarchical Architecture for Stable Multi-Agent LLM Systems**
- Authors: (multiple), arXiv:2601.10738, January 2026
- Match type: **structural**
- Claims supported: temporal coherence across hierarchical layers as stability requirement; unbounded error propagation from inter-layer mismatch
- Summary: Proposes that unconstrained temporal hierarchies produce "severe inter-layer conflicts, unbounded error propagation, and restricted scalability." Solves via projecting inter-layer communication onto constrained manifolds. Reports 47% reduction in failure cascades. This is the closest independent convergence found — they identify the same core problem (temporal hierarchy without coherence constraints causes instability) and solve it with constraints on inter-layer divergence, though in the specific domain of multi-agent LLM systems rather than as a universal criterion.
- Gap: No spectral radius formalism; no identification of the two named failure modes; domain-specific rather than cross-domain.

**2. Ashwin, von der Heydt, Bastiaansen & Ritchie — "The role of coupling and timescales for interacting tipping elements"**
- arXiv:2509.03996, September 2025
- Match type: **structural**
- Claims supported: timescale coupling determines stability/tipping; faster downstream systems are vulnerable to upstream instability (structurally parallel to Acceleration Runaway)
- Summary: Identifies conditions on coupling strength and timescale separation that produce different tipping cascade regimes in coupled bistable systems. An "accelerating cascade" occurs when a slowly-evolving upstream system forces a faster downstream system to tip. This maps onto the Coherence Criterion's claim that timescale divergence between coupled layers produces instability, and the accelerating cascade is structurally similar to Acceleration Runaway.
- Gap: Focused on climate tipping elements; no spectral radius formalism; no symmetric treatment of rigidity vs acceleration failure; no coupled Markov process framework.

**3. Sinet, Delmeire, Ritchie, Dijkstra & von der Heydt — "A Criterion for Safe Overshoot in Coupled Tipping Systems"**
- arXiv:2602.19696, February 2026
- Match type: **structural**
- Claims supported: formal criterion for stability in coupled systems with timescale interaction
- Summary: Extends inverse-square-law criterion from isolated to coupled slow-fast systems. Investigates safe-overshoot phenomena with nonlinear interactions and coupling through time-derivatives. Directly addresses the question "when does temporal coupling cause catastrophic transition?" — the same question the Coherence Criterion addresses, but via different formalism (safe overshoot bounds rather than spectral radius).
- Gap: Climate-specific; no general hierarchical framing; no named failure modes.

**4. MTLHRL — Multi-Timescale Lyapunov-Constrained Hierarchical Reinforcement Learning**
- arXiv:2510.22420, October 2025
- Match type: **structural**
- Claims supported: hierarchical multi-timescale systems require explicit stability enforcement; Lyapunov-based stability in semi-Markov framework
- Summary: Integrates hierarchical policy within semi-Markov Decision Process with high-level (strategic) and low-level (reactive) policies operating on different timescales. Stability enforced via neural Lyapunov function. Demonstrates that without explicit stability constraints, hierarchical multi-timescale control diverges.
- Gap: Engineering solution, not a general criterion; no spectral radius condition; no failure mode taxonomy; no cross-domain claims.

**5. Hierarchical Timescale Hypothesis (HTS)**
- Cell Systems, 2025
- Match type: **structural**
- Claims supported: hierarchical timescale organization is a convergent structural principle across biological and artificial networks
- Summary: Argues that biological signaling networks, brain circuits, and deep RNNs all converge on multi-layer organization with hierarchically distributed timescales as an optimal architecture. "Decreasing bandwidth" across layers handles noise and delay accumulation. This independently supports the Coherence Criterion's premise that hierarchical timescale structure is a universal organizing principle, though it frames it as an optimality result rather than a stability criterion.
- Gap: Descriptive/explanatory, not prescriptive; no stability criterion; no failure mode analysis.

### Adjacent Matches (related work that overlaps partially)

**6. Picallo & Bolognani — "Sensitivity-Conditioning: Beyond Singular Perturbation for Control Design on Multiple Time Scales"**
- arXiv:2101.04367, 2021 (IEEE TAC 2022)
- Match type: **adjacent**
- Claims supported: singular perturbation alone is insufficient for multi-timescale stability; explicit conditioning of cross-scale coupling is needed
- Summary: Shows that standard singular perturbation requires artificially large timescale separation, limiting performance. Proposes feed-forward sensitivity conditioning as alternative. Confirms the Coherence Criterion's implicit claim that naive timescale separation is not sufficient — you need explicit management of cross-scale coupling.
- Gap: Engineering control design, not a stability criterion per se; no failure mode taxonomy.

**7. Bianchi & Dorfler — "A Stability Condition for Online Feedback Optimization without Timescale Separation"**
- arXiv:2412.10964, December 2024
- Match type: **adjacent**
- Claims supported: stability conditions for coupled multi-rate systems can be stated without requiring timescale separation
- Summary: Derives stability conditions that are independent of the plant's time constant, using composite Lyapunov functions. Shows that timescale separation is sufficient but not necessary for stability. Relevant because it demonstrates that the critical question is the coupling structure, not merely the timescale ratio — aligning with the Coherence Criterion's focus on the coupling matrix M rather than raw timescale difference.
- Gap: Narrow optimization context; no failure modes; no cross-domain generalization.

**8. De la Sen — "On Some Sufficiency-Type Stability and Linear State-Feedback Stabilization Conditions for a Class of Multirate Discrete-Time Systems"**
- MDPI Mathematics, 2018
- Match type: **adjacent**
- Claims supported: spectral radius conditions for multirate systems; coupling strength must be bounded relative to convergence radii
- Summary: Derives stability conditions for multirate discrete-time systems based on spectral radius, numerical radius, and matrix norms. Shows that coupled dynamics between multirate subsystems must be "sufficiently weak related to convergence radii." This is the closest prior art for the specific mathematical form ρ(M) < 1 as a stability condition for multi-rate coupled systems.
- Gap: Purely control-theoretic; no hierarchical framing; no failure mode taxonomy; no cross-domain claims.

**9. Carpenter & Brock — "Adaptive Capacity and Traps"**
- Ecology and Society, 2008
- Match type: **adjacent**
- Claims supported: rigidity traps as a failure mode of hierarchical social-ecological systems
- Summary: Identifies "rigidity traps" where strong self-reinforcing controls prevent adaptation, increasing risk of catastrophic breakdown, and "poverty traps" where loose connections prevent resource mobilization. The rigidity trap maps onto the Coherence Criterion's Rigidity Runaway (λ → +1), and the poverty trap maps loosely onto Acceleration Runaway (insufficient coupling leading to drift). However, this is qualitative organizational theory without mathematical formalization.
- Gap: No mathematical formalism; no spectral radius; no bifurcation geometry; qualitative rather than quantitative.

**10. Sarkar & Osiyevskyy — "Organizational change and rigidity during crisis: A review of the paradox"**
- European Management Journal, 2018
- Match type: **adjacent**
- Claims supported: rigidity as a failure mode in organizational response to crisis
- Summary: Reviews the paradox that crises can either stimulate adaptive change or trigger rigidity. Draws on Staw et al.'s (1981) threat-rigidity theory. Identifies temporal mismatch between crisis speed and organizational response capacity as a key factor. Supports the qualitative reality of Rigidity Runaway but without mathematical formalization.
- Gap: No formal model; no connection to spectral analysis or bifurcation theory.

**11. Min & Borch — "Systemic failures and organizational risk management in algorithmic trading"**
- Social Studies of Science, 2022
- Match type: **adjacent**
- Claims supported: timescale mismatch between automated trading and human oversight as a systemic failure mode
- Summary: Applies Perrow's normal accident theory to algorithmic trading. Shows that tight coupling and complex interactions at mismatched timescales render markets prone to systemic failures (flash crashes). Paradoxically, individual firms' reliability practices can exacerbate market instability. Supports the financial market application of the Coherence Criterion but without the formal framework.
- Gap: Sociological framing; no mathematical formalism; no bifurcation analysis.

**12. Otalvaro — "A Framework to Use Bifurcation Analysis for Insight into Complex Systems Resilience"**
- INCOSE International Symposium, 2024-2025
- Match type: **adjacent**
- Claims supported: bifurcation analysis as a tool for understanding complex systems resilience and failure
- Summary: Proposes using bifurcation analysis to bridge resilience engineering with systems dynamics. Applied to IEEE 9-Bus power system using eigenvalue and continuation analysis. Supports the general claim that bifurcation geometry is relevant to system failure but does not address hierarchical timescale structure specifically.
- Gap: No timescale hierarchy; no coupled layers; no named failure modes; domain-specific application.

**13. Esteban et al. — "Three-time scale singular perturbation control and stability analysis"**
- Int. J. Robust & Nonlinear Control, 2013
- Match type: **adjacent**
- Claims supported: composite Lyapunov functions for three-timescale hierarchical systems; stability requires bounded singular perturbation parameters
- Summary: Constructs composite Lyapunov functions for three-timescale singularly perturbed systems with upper bounds on perturbation parameters. Demonstrates that hierarchical stability analysis decomposes across timescales but requires cross-scale coupling constraints.
- Gap: Standard singular perturbation; no spectral radius criterion; no failure mode taxonomy.

**14. Markov Jump Linear Systems literature (multiple authors)**
- Match type: **adjacent**
- Claims supported: coupled Markov processes as formalism for switching/hierarchical systems; spectral radius of operators governing stability
- Summary: Extensive literature showing that for Markov Jump Linear Systems, mean-square stability is equivalent to spectral radius of an associated operator being < 1. Coupled Lyapunov equations describe second-moment evolution. This is well-established prior art for the mathematical machinery but not applied to temporal coherence across hierarchical layers.
- Gap: Standard MJLS theory; no hierarchical temporal divergence framing; no named failure modes.

### No Exact Matches Found

No published work was found that combines all four of the Coherence Criterion's core claims into a single framework:
1. Spectral radius ρ(M) < 1 as a unified stability condition for temporal divergence across hierarchical layers
2. Two named failure modes (Rigidity Runaway and Acceleration Runaway) as eigenvalue limits
3. Common bifurcation geometry shared across domains (autonomous systems, learning, institutions, finance)
4. Coupled Markov processes as the specific formalism for cross-layer temporal divergence

### No Contradictions Found

No work was found that directly contradicts the Coherence Criterion's claims. The closest challenge comes from the "stability without timescale separation" literature (Bianchi & Dorfler), which shows that timescale separation per se is not the critical variable — but this actually supports the Coherence Criterion's framing, which focuses on the coupling structure (M) rather than raw timescale ratio.

## Notes

**What is well-established prior art:**
- Spectral radius < 1 as a stability condition (fundamental linear algebra / control theory)
- Singular perturbation theory for multi-timescale systems (Kokotovic 1986, Naidu 2002)
- Markov Jump Linear Systems and their spectral characterization
- Rigidity traps in social-ecological systems (Carpenter & Brock 2008)
- Threat-rigidity theory in organizations (Staw et al. 1981)
- Timescale mismatch as a source of financial market instability

**What is partially converged (2024-2026 independent work):**
- CTHA (2026): temporal coherence across hierarchical layers as a stability requirement, with constraint-based solutions — closest convergence
- Ashwin et al. (2025): coupling + timescale conditions for cascading tipping — structural parallel to the acceleration failure mode
- HTS hypothesis (2025): hierarchical timescale organization as convergent optimality principle
- Sensitivity-conditioning (2021): explicit cross-scale coupling management beyond singular perturbation

**What remains novel in the Coherence Criterion:**
1. The specific formulation of ρ(M) < 1 as a criterion for *temporal divergence* (not just generic stability) across hierarchical layers
2. The symmetric identification of two named failure modes (Rigidity Runaway at λ → +1 and Acceleration Runaway at λ → −1) as eigenvalue limits of the same coupling matrix
3. The claim of shared bifurcation geometry across autonomous systems, learning architectures, institutions, and financial markets — the cross-domain unification itself
4. The use of coupled Markov processes specifically for temporal divergence analysis (vs. the standard MJLS use for mode-switching)
5. The "coherence criterion" framing as a single testable condition with named violation modes

The CTHA paper is the strongest independent convergence. It identifies the same core problem (unconstrained temporal hierarchies produce instability through inter-layer conflict) and solves it with manifold constraints. However, it works in a specific domain (multi-agent LLM systems), lacks mathematical generality (no spectral radius), and does not identify the two failure modes.

## Verdict

**Partial convergence confirmed, as predicted.** The mathematical components (spectral radius, singular perturbation, MJLS) are well-established. The qualitative observations (rigidity traps, timescale mismatch failures, temporal hierarchy as organizing principle) are independently documented across multiple fields. Recent work (CTHA 2026, Ashwin et al. 2025) independently reaches structurally similar conclusions about temporal coherence as a stability requirement.

However, the Coherence Criterion's specific synthesis remains novel: no published work combines the spectral radius condition, the two named failure modes, the cross-domain bifurcation geometry, and the coupled Markov process formalism into a single unified framework. The paper's contribution is the unification, not the components.

**Risk assessment:** The cross-domain unification claim is the most vulnerable to challenge — critics could argue it is an analogy rather than a formal isomorphism. The mathematical criterion ρ(M) < 1 itself is well-grounded in prior art. The two named failure modes are the most distinctive novel contribution and have no direct precedent in published literature.
