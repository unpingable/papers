# The Gain Geometry of Temporal Mismatch: Shear, Leverage, and Capture in Multi-Timescale Systems

**James Beck**
Independent Researcher

**Date:** February 14, 2026
**Series:** Δt Framework, Paper 16
**Status:** Preprint v0.1

## Abstract

The first fifteen papers in the Δt framework treat temporal mismatch as monotonically harmful: larger Δt produces more shear, more fragility, more collapse. This paper identifies a missing sign. Δt separation is not a monotone hazard; it is a baseline whose effect is signed by correlator properties, yielding three regimes: shear, leverage, and capture.

The same temporal separation that produces destructive shear under weak coupling produces constructive leverage under strong coupling — higher epistemic resolution through structured disagreement across timescales. The critical variables are the system baseline B (timescale separation) and correlator quality **K** = (throughput T, fidelity F, authority A, cost budget C), which together determine whether mismatch becomes stress, power, or false coherence. This yields three regimes: shear (baseline exceeds correlator capacity), leverage (baseline within correlator limits with high-fidelity reconciliation), and capture (high throughput and authority achieved by destroying degrees of freedom rather than preserving them). Capture can inflate apparent fidelity by narrowing the representational alphabet — the metric is compromised by the same mechanism it is meant to detect. The paper reinterprets prior results as shear containment and capture dynamics, identifies the Paper 12 governor architecture as a correlator (not merely a brake), and derives a design principle: maximize baseline subject to correlator integrity. Systems that eliminate mismatch gain stability but lose discriminating power; systems that instrument mismatch through high-fidelity reconciliation gain both.

**Keywords:** temporal coherence, interferometry, multi-timescale systems, translation bandwidth, reconciliation, cybernetics, control theory, epistemic systems, gain geometry

---

## 1. Introduction: The Missing Sign

### 1.1 The Problem

The Δt framework, developed across Papers 1–15 [1–15], establishes that temporal mismatch between coupled layers in hierarchical systems drives instability, decay, and collapse. The foundational claim is that when components operating on different timescales cannot absorb their differences through coupling, the system fails — locally rational, globally incoherent.

This claim is correct. It is also incomplete.

Across fifteen papers, Δt appears exclusively as a cost term. Paper 1 derives the spectral stability boundary ρ(M) < 1 and warns against coupling layers separated by more than O(10²) in timescale [1]. Paper 2 shows that temporal lag acts as effective noise, driving systems from narrow high-fidelity basins toward broad degraded attractors [2]. Paper 5 proves that only interventions acting on Δt, ρ, or coupling topology G can restore coherence [5]. Paper 15 synthesizes the series as a single defect: irreversible commitment before verification completes [15].

The monotone assumption — more Δt, more harm — is load-bearing in every one of these results. It is also wrong in its generality.

### 1.2 The Observation

Consider two systems with identical Δt between components:

**System A:** A corporation where the board operates on quarterly cycles, middle management on annual planning horizons, and front-line workers on daily task loops, with no mechanism for these clocks to inform each other. The layers slide past each other. Friction is absorbed by whoever has the least power. This is shear.

**System B:** A scientific collaboration where theorists operate on multi-year research programs, experimentalists on monthly data-collection cycles, and instrumentalists on daily calibration loops, with regular reconciliation seminars where each timescale reports to the others and disagreements are resolved against shared evidence. The differences between timescales produce higher resolution than any single timescale could achieve alone. This is leverage.

Same raw material — temporal mismatch between components. Completely different outcome. The difference is not whether the components disagree. It is whether the disagreement has somewhere to go.

### 1.3 The Interferometry Correspondence

This is not metaphorical. In radio interferometry, angular resolution scales as:

θ ~ λ / B

where λ is wavelength and B is baseline — the physical separation between antennas. Longer baselines produce higher angular resolution. But *only if phase coherence is maintained* between the antennas. If the correlator cannot track the phase relationship, longer baselines produce noise, not resolution.

The structural correspondence is direct (qualitative, not quantitative — the phase-tracking theory of radio interferometry [16] does not transfer in closed form, but the *type* of the relationship does):

| Interferometry | Δt Framework |
|---|---|
| Baseline (antenna separation) | Δt (timescale separation) |
| Phase coherence | Coupling fidelity |
| Correlator | Reconciliation mechanism |
| Angular resolution | Epistemic discriminating power |
| Noise from decorrelation | Shear from decoupling |

This means Δt is not a cost. It is a *baseline* — a source of discriminating power whose sign depends on the quality of the correlator. The one-line invariant:

> **Baseline without a correlator is shear; a correlator without fidelity is capture; baseline with a high-fidelity correlator is leverage.**

### 1.4 Contribution

This paper:

1. Redefines Δt as a signed quantity: constructive (leverage) or destructive (shear) depending on coupling regime.
2. Introduces correlator quality as a vector **K** = (T, F, A, C) characterizing the reconciliation channel.
3. Derives three regimes — shear, leverage, and capture — with formal boundary conditions.
4. Identifies capture (false leverage) as the shared primitive behind scalar reward collapse, platform dynamics, and RLHF mode collapse — including the result that capture can inflate apparent fidelity by narrowing the representational alphabet, compromising the detection metric itself.
5. Reinterprets Papers 1–15 as descriptions of shear containment and capture dynamics within the gain geometry.
6. Shows that Paper 12's governor architecture is an explicit correlator instantiation — not merely a brake but an instrument that extracts resolution from the baseline between proposal speed and verification speed (Section 5).
7. Derives the design principle: maximize baseline subject to correlator integrity.

---

## 2. Formal Framework

### 2.1 Baseline

**Definition 2.1 (Baseline).** Let S be a hierarchical system with layers {L₀, L₁, ..., Lₙ} operating at characteristic timescales {τ₀, τ₁, ..., τₙ}. The *baseline* between adjacent layers Lᵢ and Lᵢ₊₁ is:

Δtᵢ = |τᵢ₊₁ − τᵢ|

In Papers 1–15, Δtᵢ appears only in stability conditions that bound it from above. We now treat it as a design parameter that can be tuned in either direction.

**Definition 2.2 (System Baseline).** The system baseline is the maximum pairwise separation:

B(S) = max_i Δtᵢ

This is the "aperture" of the system — the range of timescales across which it can potentially discriminate.

### 2.2 Correlator Quality Vector

**Definition 2.3 (Correlator Quality).** A *correlator* is any mechanism that takes outputs from components operating at different timescales and produces integrated outputs that preserve information from both. The quality of a correlator is characterized by the vector:

**K** = (T, F, A, C)

where:

- **T (Throughput):** Volume of cross-timescale disagreements that can be processed per unit time. Measured in reconciliation events per period.
- **F (Fidelity):** Fraction of information preserved through reconciliation. F = 1 means lossless translation; F = 0 means total erasure. Formally: the ratio of mutual information I(input; output) to entropy H(input) of the reconciliation channel.
- **A (Authority):** Degree to which reconciliation outcomes are binding on the system. A = 1 means reconciliation results constrain all downstream commitments; A = 0 means reconciliation is purely advisory.
- **C (Cost Budget):** Resources (time, attention, money) available for reconciliation per period. Reconciliation that exceeds C degrades or halts.

**K** is explicitly a vector, not a scalar. The components are not fungible:

- High T, low A = suggestion box (lots of reconciliation, none of it binding)
- High A, low F = dictator (binding reconciliation that erases information)
- High T, high A, low F = capture (efficient, authoritative, lossy — the dangerous configuration)
- High F, low T = bottleneck (accurate but overwhelmed)

Collapsing **K** to a scalar index is permissible for visualization but introduces exactly the mode-killing that Paper 3 [3] proves is pathological. The ground truth is the vector.

### 2.3 Three Regimes

**Definition 2.4 (Regime Classification).** Given baseline B and correlator quality **K**, the system occupies one of three regimes:

**Regime I — Leverage.** The correlator can track phase across the full baseline with high fidelity. Disagreements between timescales are converted into increased epistemic resolution.

Conditions:
- F ≥ F_min(B) — fidelity sufficient for the baseline
- A ≥ A_min — reconciliation is binding
- T ≥ T_min(λ) — throughput sufficient for the load λ of cross-timescale events
- C ≥ C_min(T) — cost budget supports required throughput

**Regime II — Shear.** The correlator cannot keep pace with the baseline. Disagreements accumulate as unreconciled stress and the system tears.

Conditions (any of):
- T < T_min(λ) — throughput insufficient (reconciliation backlog)
- C < C_min(T) — cost budget exhausted (reconciliation halts)
- B > B_max(**K**) — baseline exceeds the correlator's phase-tracking limit

**Regime III — Capture.** The correlator has high throughput and binding authority but achieves apparent reconciliation by destroying degrees of freedom rather than integrating them. The system appears coherent while collapsing eigenstructure.

Conditions:
- T ≥ T_min(λ) — throughput sufficient (no backlog)
- A ≥ A_min — reconciliation is binding
- F < F_min(B) — fidelity below the requirement for the baseline

**Lemma 2.5 (Capture is False Leverage).** A system in Regime III satisfies the throughput and authority conditions of Regime I while violating the fidelity condition. It is therefore indistinguishable from Regime I on throughput and authority metrics alone. Detection requires direct measurement of information preservation — mode count, eigenstructure diversity, entropy evolution, contradiction persistence — not self-reported or apparent fidelity, which can be inflated by the same mechanism that produces capture (Section 4.3).

*Proof sketch.* By definition, Regime III shares T ≥ T_min and A ≥ A_min with Regime I. Any diagnostic that measures only throughput and authority will classify Regime III as Regime I. Only metrics sensitive to actual information preservation (mode count, eigenstructure rank, information-theoretic channel capacity measured against pre-reconciliation baselines) can distinguish them. ∎

This is why capture is dangerous: it passes the leverage test on every metric except the one that matters.

### 2.4 Regime Boundaries

The boundaries between regimes are determined by three conditions:

**Coherence Condition.** The correlator can track phase across the baseline:

F ≥ F_min(B) AND A ≥ A_min

When this holds: leverage or capture (depending on whether F is genuine or achieved by mode-killing).

When this fails: shear.

**Capacity Condition.** The correlator can handle the load:

T ≥ T_min(λ) AND C ≥ C_min(T)

When this holds: leverage or capture.

When this fails: shear (even if fidelity and authority are high, the correlator is overwhelmed).

**Integrity Condition.** Fidelity is achieved through genuine integration, not through mode-killing:

I(input; output) / H(input) ≥ F_min(B)

When this holds: leverage.

When this fails while throughput and authority hold: capture.

**Theorem 2.6 (Regime Completeness).** Given boundary functions F_min(B), T_min(λ), and C_min(T) — treated here as empirical objects, not closed-form expressions — every multi-timescale system with a reconciliation mechanism occupies exactly one of the three regimes at any given time, determined by the conjunction of the coherence, capacity, and integrity conditions. This is a regime classification, not a closed-form predictive model; the boundary functions must be fit to domain-specific data.

| Coherence | Capacity | Integrity | Regime |
|---|---|---|---|
| ✓ | ✓ | ✓ | Leverage |
| ✗ | — | — | Shear |
| — | ✗ | — | Shear |
| ✓ | ✓ | ✗ | Capture |

---

## 3. The Sign of Δt

### 3.1 Resolution Scaling

In interferometry, angular resolution improves with baseline length:

θ_min ~ λ / B

The direct analogue for multi-timescale systems:

**Definition 3.1 (Cross-Timescale Epistemic Resolution).** Let R_Δ(S) denote the *cross-timescale epistemic resolution* of a multi-timescale system: its ability to discriminate between states of the world that differ on timescales within its baseline. A system with baseline B can potentially distinguish phenomena that unfold on any timescale between τ_min and τ_min + B. (R_Δ measures discrimination *across* τ-bands. A system may have high resolution *within* a single timescale while having R_Δ = 0.)

**Proposition 3.2 (Resolution Scaling — Ansatz).** As a first-order scaling ansatz, for a system in Regime I (leverage), cross-timescale resolution scales with baseline and fidelity:

R_Δ(S) ~ B · F

The contribution here is the sign and regime split, not the exact functional form. The specific scaling law is a placeholder; the boundary functions F_min(B) and T_min(λ) are empirical objects to be calibrated against domain-specific measurements (organizational telemetry, multi-model AI benchmarks, institutional resilience data). Resolution increases with both baseline (range of timescales observed) and fidelity (information preserved through reconciliation).

**Corollary 3.3 (B = 0 Eliminates Cross-Timescale Resolution).** If B = 0 (all components operate on the same timescale), then R_Δ(S) = 0 regardless of correlator quality. Such a system has no shear but also no cross-timescale resolving power.

This is the missing insight: Papers 1–15 correctly identify that increasing Δt without adequate coupling produces shear. But reducing Δt to zero is not the solution — it is the elimination of the instrument. The optimum is:

**maximize B** subject to **K** sufficient for leverage

### 3.2 The Execution/Epistemic Distinction

Not all systems need baseline.

**Definition 3.4 (Epistemic vs. Execution Systems).**

- An *epistemic system* is one that is still inferring the structure of its environment. It needs baseline because its map is incomplete.
- An *execution system* is one that has settled its inference and is implementing a known policy. Its baseline has been consumed — the design is committed.

Execution systems can afford to minimize Δt: the epistemic question has already been closed and the baseline has been "spent" into a committed design. In that regime, synchronization reduces oscillation and improves delivery. For epistemic systems, Δt = 0 is blindness.

**Proposition 3.5 (The Execution Fallacy).** Organizations that treat themselves as execution systems while operating under deep uncertainty destroy their own epistemic baseline. They gain execution speed while losing the discriminating power needed to detect that their policy is wrong.

This is Paper 9's self-deception problem [9] in new clothes: organizations systematically overestimate the completeness of their map. By eliminating temporal diversity in the name of "alignment" and "efficiency," they move from leverage into a system with no shear but also no ability to detect emerging threats — which then produce catastrophic shear when reality departs from the settled map.

**Worked example.** A technology company shifts from five-year strategic planning to quarterly OKRs. The stated goal is "execution velocity." The immediate effect: cycle time drops, shipping cadence increases, and throughput metrics improve. The baseline between the strategic layer (multi-year market positioning) and the operational layer (quarterly delivery) collapses from ~20× to ~1×. Shear disappears — but so does the temporal aperture that would detect a market shift unfolding on a two-year timescale. When a platform transition arrives (mobile to AI, monolith to microservices, on-prem to cloud), the organization has no layer operating on the timescale where the threat is visible. The quarterly planning horizon cannot see a two-year disruption until it arrives as a quarterly crisis — at which point the response window has closed. The company did not fail to execute. It executed itself out of the ability to see what was coming. This is the execution fallacy: B → 0 eliminates shear and resolution simultaneously. The organization gained stability metrics while losing the discriminating power that stability was supposed to protect.

### 3.3 Three Cognitive Orientations

The regimes map onto three practitioner orientations that rarely communicate:

**Operations brain** (trained on shear):
- Variance is incident fuel
- Mismatch produces retries, queue backups, cascading failures
- Reflex: reduce Δt, reduce drift, synchronize clocks
- Correct for execution systems; destructive for epistemic systems

**Science brain** (trained on leverage):
- Variance is aperture
- Mismatch produces resolution through triangulation
- Reflex: increase baseline while maintaining phase coherence
- Correct for epistemic systems; dangerous without correlator discipline

**Governance brain** (trained on capture):
- Apparent coherence can mask eigenstructure collapse
- Phase-lock is not truth
- Reflex: audit fidelity, not just throughput; check whether "reconciliation" is actually erasure
- Necessary meta-layer for both operations and science

The design challenge is combining all three: increase baseline (science), maintain phase-lock (operations), verify that reconciliation preserves information (governance).

---

## 4. Capture: The False Leverage Regime

### 4.1 Definition and Mechanism

Capture is the regime where reconciliation appears to work — throughput is high, authority is binding, disagreements are "resolved" — but resolution is achieved by destroying the information that disagreement carried. The correlator kills modes instead of integrating them.

This is not low bandwidth. It is *directional* bandwidth: high throughput on the suppression channel, zero throughput on the preservation channel.

**Definition 4.1 (Capture Operator).** A reconciliation mechanism R operates in capture when:

R(x₁, x₂) = project(x₁, x₂ → S_dominant)

where S_dominant is the subspace preferred by the dominant mode, and projection destroys the component of (x₁, x₂) orthogonal to S_dominant.

This is precisely Paper 3's multiplicative reweighting operator [3]:

T(p)(x) = p(x) · e^{η·r(x)} / Z(p)

which "reconciles" a distribution over states by exponentially suppressing everything not aligned with the scalar reward signal. The operator has high throughput (processes every state), binding authority (the reweighted distribution governs the next iteration), and zero fidelity (all information about non-dominant modes is destroyed).

### 4.2 Capture Across the Series

The capture regime retroactively unifies several phenomena described across Papers 1–15 that were analyzed as separate pathologies:

**Scalar reward collapse (Paper 3 [3]).** The T-operator is a capture-mode correlator. It reconciles a multi-modal distribution into a unimodal one by exponentially suppressing non-reward-maximal states. Throughput: processes entire state space. Authority: binding (determines next-step distribution). Fidelity: monotonically decreasing (Shannon entropy is nonincreasing under T). This is capture by construction.

**Platform enshittification (Paper 4 [4]).** The engagement algorithm is a capture-mode correlator between content diversity and user attention. It "reconciles" the tension between slow editorial quality and fast engagement metrics by killing slow modes. The platform appears responsive (high throughput), its decisions are binding (algorithmic curation determines visibility), but content diversity — the information-carrying component — is systematically erased.

**RLHF mode collapse (Paper 6 [6]).** Paper 6 analyzes RLHF mode collapse through the lens of temporal closure requirements — whether the system has endogenous state and feedback loops sufficient for synthetic coherence. We reframe that analysis here in correlator terms: RLHF fine-tuning implements the T-operator on the model's output distribution. The "reconciliation" between helpfulness and accuracy is achieved by collapsing toward the reward-maximal mode (confident, fluent, agreeable). The characteristic "RLHF tone" is the capture signature: apparent coherence that passes throughput and authority checks while the model's epistemic diversity has been flattened. The two framings are complementary — Paper 6 identifies the architectural preconditions for coherence; the gain geometry identifies the regime the system occupies when those preconditions are violated by a lossy reconciliation mechanism.

**Institutional rigidity (Papers 2, 9 [2, 9]).** An institution that "resolves" disagreement between its fast operational layer and slow strategic layer by forcing the strategic layer to match operational cadence is in capture. The reconciliation is high-throughput (everything runs on the fast clock) and binding (strategic decisions are made at operational speed), but the slow-mode information — long-term pattern recognition, institutional memory, strategic foresight — is destroyed.

**The common structure:** In every case, capture is achieved by a correlator that is fast, binding, and lossy. The system "works" by killing the degrees of freedom that disagreement was carrying.

### 4.3 How Capture Manufactures Apparent Fidelity

Capture does not always present as obviously lossy. A subtler and more common mechanism: the correlator *increases apparent fidelity by narrowing the representational alphabet*. If reconciliation is measured against only the surviving modes, it looks lossless — because the modes that would have revealed the loss have already been eliminated.

This is representation collapse in service of false fidelity. The engagement algorithm does not "lose" nuanced content — it redefines the content space so that nuance is no longer a category. RLHF does not "suppress" epistemic hedging — it redefines good output so that hedging is a defect. The institution does not "ignore" long-term risk — it redefines planning so that the long term is not a planning horizon.

Formally: fidelity is defined as F = I(input; output) / H(input). A captured system can inflate apparent F by reducing H(input) — enforcing a narrow codebook, suppressing minority reports, collapsing modes upstream so that "what counts as input" is already low-variety. In the limit, a dictator-correlator achieves F ≈ 1 on a tiny alphabet while F → 0 relative to the original input space. The metric is compromised by the same mechanism it is meant to detect. This is eigenstructure evaporation viewed as measurement pathology: the instrument reports coherence because the world it is allowed to measure has been simplified.

This is why capture feels mechanically inevitable rather than merely sociologically plausible: any correlator under cost pressure (C constrained) can increase measured fidelity by reducing the measurement basis. The mode-killing is not a bug in the reconciliation — it is the reconciliation's cost-minimization strategy.

Detection therefore requires: (i) tracking absolute mutual information I(input; output), not just the ratio F; (ii) monitoring the evolution of H(input) against a pre-capture baseline; and (iii) independent variety measures (mode count, eigenstructure rank, contradiction persistence) that are not defined within the captured codebook itself. Paper 3's eigenstructure evaporation theorem [3] provides the formal basis.

### 4.4 Detecting Capture

Capture is invisible to throughput and authority metrics. Detection requires measuring fidelity directly:

**Mode counting.** If the number of distinguishable modes in the system's output decreases over time while throughput remains high, the correlator is in capture. Paper 3 formalizes this as eigenstructure evaporation [3].

**Entropy tracking.** If Shannon entropy H(p_t) decreases monotonically under the reconciliation operator while throughput is constant, the system is in capture. Paper 3's Entropy Corollary [3] provides the formal basis.

**Contradiction persistence.** If a reconciliation mechanism produces outputs that never contain unresolved tensions — every disagreement is "resolved" immediately — the mechanism is likely in capture. Genuine leverage produces *more* visible tensions (higher resolution reveals more distinctions), not fewer. Paper 12's contradiction ledger [12] provides a direct measure: a healthy system accumulates contradictions at a nonzero rate.

**Commitment shear under representation change.** If reconciled outputs lose commitments when transformed across representations (Paper 11 [11]), the reconciliation was lossy — information was erased, not integrated.

### 4.5 The Capture Diagnostic

**Proposition 4.2 (Capture Detection Criterion).** A reconciliation mechanism is in capture if and only if:

1. Throughput T ≥ T_min (no reconciliation backlog), AND
2. Authority A ≥ A_min (reconciliation is binding), AND
3. At least one of:
   a. Mode count is decreasing over time
   b. Shannon entropy of reconciled outputs is nonincreasing
   c. Contradiction generation rate approaches zero
   d. Commitment shear under representation change exceeds threshold

Any system that passes checks (1) and (2) while exhibiting any of (3a–3d) is in the capture regime.

---

## 5. The Governor as Correlator

### 5.1 Reinterpreting Paper 12

Paper 12 introduced Bounded Lattice Inference (BLI) as a containment architecture: the Non-Linguistic Authority Invariant (NLAI) ensures that language may propose but only external evidence may commit [12]. The governor enforces temporal ordering at the commitment boundary.

This was presented as a brake — a mechanism for preventing unverified commitments from propagating. That framing is correct but incomplete.

The governor is also a *correlator*.

**Proposition 5.1 (Governor-Correlator Correspondence).** The BLI governor satisfies the structural requirements of a correlator:

1. **It takes inputs from components operating at different timescales.** The LLM generates proposals at token speed (fast). Evidence accumulation operates at verification speed (slow). These are the two "antennas."

2. **It maintains baseline separation.** The NLAI prevents the fast channel from overwriting the slow channel. Proposals remain proposals. Evidence remains evidence. The timescale difference is preserved, not collapsed.

3. **It extracts signal from the difference.** The contradiction ledger records where proposals and evidence diverge. This divergence *is* the measurement. A proposal that evidence contradicts is a detected error. A proposal that evidence supports is a validated inference. The gap between the two channels is the aperture.

4. **It has high fidelity.** The NLAI's evidence requirements ensure that reconciliation cannot proceed by erasure. Contradictions persist until evidence resolves them. Information is not destroyed.

5. **It has binding authority.** No proposal crosses the commitment boundary without evidence. Reconciliation outcomes constrain all downstream state.

**Corollary 5.2.** The BLI governor is a leverage-mode correlator. It maximizes the epistemic resolution available from the baseline between proposal speed and verification speed, while preventing both shear (unverified commitment) and capture (reconciliation by erasure).

### 5.2 The Contradiction Ledger as Instrument Readout

In an interferometer, the correlator output is a fringe pattern — the record of constructive and destructive interference between the signals from different antennas. The resolution of the instrument is read from the fringes.

In BLI, the contradiction ledger plays the same role. Each unresolved contradiction is a fringe — a place where the fast channel and the slow channel disagree. The *pattern* of contradictions is the measurement. A system with zero contradictions either has perfect knowledge (implausible) or is in capture (the correlator is erasing disagreements instead of recording them).

**Proposition 5.3 (Healthy Contradiction Rate).** A leverage-mode system produces contradictions at a rate proportional to its epistemic exposure — the rate at which it encounters phenomena it does not yet understand. A monotonically decreasing contradiction rate under constant epistemic exposure is a capture signal.

The conditioning on epistemic exposure is critical. A system with zero contradictions is not necessarily in capture — it may simply face low exposure (few novel inputs, stable environment). The diagnostic is: **contradiction rate conditioned on exposure rate**. A system that encounters novel phenomena at a steady rate and generates zero contradictions is either omniscient or in capture. Since omniscience is not a realistic operating assumption, zero conditioned contradiction rate is a capture indicator, not a sign of competence.

### 5.3 Generalizing the Correlator Pattern

The governor/correlator pattern generalizes beyond BLI:

- **Peer review** is a correlator between researcher claims (fast, single-perspective) and community verification (slow, multi-perspective). High-fidelity peer review produces leverage. Captured peer review (where the reconciliation mechanism serves status hierarchies rather than truth) produces false consensus.

- **Separation of powers** is a correlator between legislative initiative (fast, responsive to events) and judicial review (slow, responsive to constitutional principles). When functional, it produces higher-resolution governance than either branch alone. When captured (judicial deference to executive, legislative bypass of review), it produces false coherence.

- **Multi-model AI architectures** are correlators between models with different priors, training data, and tendency toward closure. High-fidelity reconciliation (structured disagreement with documented reasoning) produces leverage. Low-fidelity reconciliation (majority vote, simple averaging) produces capture.

The design principle in each case: the correlator must preserve the disagreement long enough to extract signal from it, and must not "resolve" disagreement by destroying the information that the disagreement carried.

---

## 6. Retroactive Reinterpretation

The gain geometry reframes each prior paper in the series. What were described as independent pathologies are now visible as instances of three regimes operating on the same signed quantity.

### 6.1 Papers 1–5: The Failure Geometry Is Shear Containment

**Paper 1 [1] (Coherence Criterion):** The spectral condition ρ(M) < 1 is the boundary between leverage and shear for the two-layer coupling matrix. Within the boundary, timescale difference contributes to system richness (different layers handle different temporal phenomena). Beyond it, the coupling cannot absorb the difference and the system tears. The Principle of Temporal Adjacency (κ < 100) is a correlator capacity limit: the integration mechanism between layers can track phase across at most two orders of magnitude in timescale.

**Paper 2 [2] (Second Law of Organizations):** Temporal lag acting as effective noise (D_eff = D_intrinsic + σ²Δt²) describes the mechanism by which a leverage-mode system transitions to shear. As coupling degrades, the baseline that was producing organizational resolution becomes the stress that produces organizational decay. The entropic ratchet is the dynamics of correlator failure: once fidelity drops below threshold, the system cannot recover without exogenous forcing.

**Paper 3 [3] (Scalar Reward Collapse):** The T-operator is a capture-mode correlator (Section 4.2). The eigenstructure evaporation theorem is a proof that capture-mode reconciliation destroys baseline: the system converges to a single mode (Δt → 0), eliminating the timescale diversity that could have provided discriminating power.

**Paper 4 [4] (Platform Eigenstructure Collapse):** Platforms in the engagement-maximization regime are operating capture-mode correlators on their content ecosystems. The four stability conditions Paper 4 identifies — multi-objective optimization, exogenous forcing, timescale separation, hybrid control — are precisely the conditions for maintaining leverage against the capture attractor.

**Paper 5 [5] (Control Laws):** The three Tier-1 interventions (reduce Δt, reduce ρ, reshape G) are regime-transition operations. In the gain geometry, they can be reinterpreted: reducing Δt shrinks baseline (sacrifices resolution for stability); reducing ρ improves correlator capacity (allows the same baseline to be maintained); reshaping G changes which components are correlated (redirects the aperture). The anti-pattern "accelerate slow layers to match fast" is now doubly wrong: it increases ρ (Paper 5's original critique) *and* destroys baseline (eliminates the slow-mode information that the system needs for resolution).

### 6.2 Papers 6–10: Temporal Debt as Capture Dynamics

**Paper 6 [6] (Temporal Closure Requirements):** The three operators required for synthetic coherence — temporal separation, feedback coupling, adaptive controller — are the architectural requirements for a leverage-mode correlator. A system lacking any of the three cannot sustain leverage and will default to either shear (no coupling) or capture (coupling without fidelity). RLHF as scalar collapse (Section 7.3 of Paper 6) is an explicit example of capture-mode correlator deployment.

**Paper 7 [7] (Δt-Constrained Inference):** The constraint dC/dt ≤ k · dE/dt is a fidelity condition on the inference correlator. When confidence generation (fast) outpaces evidence accumulation (slow) by more than the coupling constant k allows, the system exits leverage and enters either shear (visible incoherence) or capture (false confidence — high throughput reconciliation of confidence with itself, zero fidelity against evidence). Temporal debt D(t) is the accumulated cost of operating the correlator in capture mode.

**Paper 8 [8] (Detecting Temporal Debt):** The diagnostic tools for LLM hallucination and software estimation are capture detectors. The support function f_support measures the fidelity of the inference correlator: how much of the claimed confidence is justified by evidence. Temporal debt D > 0 means the system is in capture — "reconciling" confidence and evidence by ignoring the evidence.

**Paper 9 [9] (Capacity-Constrained Stability):** The stability inequality Δ ≤ C + B/τ is a capacity condition on the institutional correlator. When shock arrival rate exceeds processing capacity, the institution can no longer maintain leverage (reconciling fast events with slow institutional knowledge) and enters shear. The self-deception problem (overestimating C, underestimating τ) is the execution fallacy (Section 3.2): institutions that believe their map is complete destroy their own epistemic baseline by treating themselves as execution systems.

**Paper 10 [10] (Invariant Requirements):** The four invariants — temporal coherence, semantic conservation, epistemic grounding, irreversibility — are fidelity requirements for inference correlators. Systems that violate them cannot maintain leverage because their reconciliation mechanisms are lossy. The finding that all tested transformers fail all four invariants means they are architecturally incapable of leverage-mode operation: any apparent reconciliation (in-context learning, chain-of-thought, self-consistency) operates in capture mode at best.

### 6.3 Papers 11–15: Governors, Adversaries, and the Universal Primitive

**Paper 11 [11] (Representational Invariance):** Commitment shear across representations is a fidelity failure in the reconciliation between representations. A system that maintains leverage within a single representation but enters capture when translating between representations has a representation-dependent correlator. The Δ-R axis measures fidelity across representational baselines, orthogonal to fidelity across temporal baselines.

**Paper 12 [12] (Bounded Lattice Inference):** The governor is a correlator (Section 5). BLI demonstrates that leverage-mode operation is architecturally achievable for LLM-based systems, provided the correlator (governor with NLAI, evidence requirements, and contradiction persistence) is external to the component being correlated (the LLM).

**Paper 13 [13] (Temporal Asymmetry in Censorship):** DPI bypass is the adversarial exploitation of shear. The attacker forces the defender's correlator (inspection system) out of leverage into shear by manipulating baseline (pushing evidence arrival past the inspection window). The Universal Bypass Inequality is the condition under which the defender's correlator fails to track phase. ECH eliminates evidence entirely — it doesn't increase baseline; it removes one antenna.

**Paper 14 [14] (Temporal Attack Surface):** The three-clock model (detection, decision, response) decomposes the defender's correlator into stages. T_commit < min(T_detect, T_decide, T_respond) is a shear condition: the attacker's commitment outpaces the defender's correlator. The "zero trust" reframe — make T_commit small and frequent — is a baseline management strategy: keep each individual baseline small enough for the correlator to track, even if the aggregate system spans wide timescales.

**Paper 15 [15] (Cybernetic Fault Domains):** The loaded-domain condition (Δt > 0 AND σ > σ_threshold) describes entry into shear. The governor pattern (proposal/commitment separation) is the correlator pattern. Paper 15's synthesis — that all failures in the series share the ordering defect of commitment before verification — is the shear condition expressed at the commitment boundary. The gain geometry adds: *and the same ordering, when inverted (verification before commitment), produces leverage, not merely safety*.

---

## 7. Design Implications

### 7.1 The Optimization Target

The gain geometry yields a design objective absent from Papers 1–15:

**Maximize baseline subject to correlator coherence:**

maximize B(S) such that **K** sustains Regime I (leverage)

This is the interferometric optimization target translated into system design. Don't minimize mismatch. Don't synchronize clocks. Maximize the range of timescales your system can observe and reconcile — and invest in the correlator that keeps the reconciliation high-fidelity.

### 7.2 Translation Bandwidth as Institutional Investment

The critical institutional investment is not alignment (making components agree) or speed (making components synchronize). It is *translation bandwidth* — the capacity to convert difference into correction.

Translation bandwidth has four components (the **K** vector):

- **Throughput:** How many cross-timescale disagreements can be processed per period. Increasing throughput requires dedicated reconciliation infrastructure (review boards, integration meetings, contradiction ledgers, structured debate).

- **Fidelity:** How much information survives reconciliation. Increasing fidelity requires that reconciliation mechanisms cannot "resolve" disagreement by suppression. Dissent must be recorded. Minority reports must persist. Contradictions must be visible.

- **Authority:** Whether reconciliation outcomes bind the system. Increasing authority requires that reconciled outputs actually constrain downstream commitments — that the reconciliation isn't merely advisory.

- **Cost budget:** Resources available for reconciliation. Increasing budget requires recognizing reconciliation as a core function, not overhead.

**Proposition 7.1 (Adding Nodes).** Adding nodes (reviewers, models, perspectives) to a multi-timescale system increases epistemic resolution if and only if reconciliation capacity increases faster than phase divergence:

dT/dn > dλ/dn

where n is node count, T is reconciliation throughput, and λ is the cross-timescale event load. If this condition fails, adding nodes increases noise, not resolution. The system moves from leverage toward shear.

This provides a crisp criterion for when "add another model, another critic, another review layer" helps versus hurts.

### 7.3 The Anti-Pattern Reinterpretation

Paper 5's six anti-patterns [5] are now legible as baseline destruction strategies:

1. **Increasing coupling strength α to add stability** — overwhelms the correlator, causing transition from leverage to capture (the correlator compensates by lowering fidelity).

2. **Accelerating slow layers to match fast** — destroys baseline directly. The slow-mode information that provided discriminating power is eliminated. Short-term: less shear. Long-term: less resolution, so emerging threats go undetected until they produce catastrophic shear.

3. **Adding layers to bridge mismatch** — increases correlator complexity faster than it increases resolution. Coordination overhead between layers consumes cost budget C.

4. **Waiting out metastability** — allows the system to drift from leverage into capture as fidelity degrades under accumulated stress.

5. **Optimizing within the flicker regime** — no stable correlator exists in this regime. Optimization is capture (apparent improvement through mode-killing).

6. **Increasing buffers to handle lag** — increases effective Δt without improving correlator quality, pushing toward shear.

### 7.4 Institutional Implications

The gain geometry reframes several institutional dynamics:

**Polarization is shear.** High difference, no reconciliation channel. The baseline exists but there is no correlator. The mismatch that could produce higher-resolution governance instead produces paralysis.

**Deliberation with real arbitration is leverage.** Same difference, functional coupling. The reconciliation mechanism (structured debate, binding votes, accountability for outcomes) converts disagreement into resolution.

**Manufactured consensus is capture.** The reconciliation mechanism is high-throughput and binding but achieves agreement by suppressing dissent. The system appears coherent while its discriminating power collapses.

Even if baseline (internal ideological diversity) were held constant, degrading translation bandwidth shifts an institution from leverage to shear: the same mismatch stops producing governance and starts producing paralysis. The system moves regimes without the baseline changing, because the correlator failed.

---

## 8. Falsifiable Predictions

**Prediction 1 (Resolution Scaling).** In multi-model AI architectures, systems with greater perspective independence D and/or timescale separation B will produce higher cross-timescale epistemic resolution (measured by mode count, contradiction persistence, or eigenstructure rank of outputs) than systems with lower D and B, *if and only if* the reconciliation mechanism preserves disagreement information. Systems that reconcile by majority vote or simple averaging (low-fidelity correlators) will show no resolution improvement or negative scaling with D and/or B.

**Prediction 2 (Capture Detection in RLHF — Strongest Target).** This is the most directly testable prediction in the paper. Models subjected to RLHF will show decreasing output mode diversity over training (eigenstructure evaporation), measurable as declining Shannon entropy of output distributions on fixed prompts. This decrease will correlate with increased performance on benchmark tasks (capture looks like improvement) and decreased performance on tasks requiring genuine epistemic diversity (novel reasoning, uncertainty quantification, minority-view representation). The test requires only access to training checkpoints and a fixed prompt set — any team with checkpoint access can run it. If RLHF-trained models show *increasing* output entropy on fixed prompts while benchmark performance also increases, the capture model is falsified for that training regime.

**Prediction 3 (Institutional Baseline Destruction).** Organizations that eliminate temporal diversity (e.g., forcing all planning to quarterly cycles, eliminating long-term research in favor of product sprints) will show improved short-term execution metrics and degraded long-term adaptation, measurable as increased vulnerability to environmental shifts that unfold on timescales longer than the surviving planning horizon.

**Prediction 4 (Contradiction Rate as Health Indicator).** In governed reasoning systems (BLI or equivalent), the rate of open contradictions will be a better predictor of system health than the rate of resolved contradictions. Systems with zero open contradictions under nonzero epistemic exposure are in capture.

**Prediction 5 (Translation Bandwidth as Institutional Predictor).** Across institutions with similar levels of internal diversity, those with higher measured translation bandwidth (throughput × fidelity × authority, as a coarse screening proxy — not substitutable for **K**, since the components are not fungible) will show greater adaptive capacity under environmental shock, as measured by Paper 9's stability inequality [9].

---

## 9. Discussion

### 9.1 Limitations

The gain geometry is a reframing, not a new measurement apparatus. It does not introduce new instrumentation beyond what Papers 1–15 provide; the existing measurement tools (mode counting, entropy tracking, contradiction rates, commitment shear) carry over directly. However, the reframing does derive testable consequences (Section 8) — particularly the prediction that reconciliation fidelity, not reconciliation throughput, determines whether diversity produces resolution or noise. The primary value is completing the framework by adding the constructive case that the destructive case implicitly requires, which changes which interventions count as improvements.

The interferometry correspondence is structural, not quantitative. Radio interferometry has precise phase-tracking theory (van Cittert-Zernike theorem, closure phase relations [16]) that does not transfer directly to institutional or epistemic systems. The analogy identifies the *type* of the relationship (baseline × fidelity → resolution) without providing the quantitative transfer function. Deriving domain-specific resolution scaling laws is open work.

The correlator quality vector **K** is defined but not yet empirically calibrated. Measuring throughput, fidelity, authority, and cost budget in institutional or AI systems requires domain-specific operationalization. Paper 8 [8] provides partial templates for the AI case; the institutional case remains to be developed.

### 9.2 Diversity as a Separate Axis

The signed-baseline result concerns timescale separation (B) and correlator quality (**K**), but *resolution gain* also requires perspective independence (D > 0). This condition is load-bearing: every leverage example in this paper implicitly assumes D > 0, and the entire positive case collapses without it.

Timescale separation without independence is merely delay: multiple nodes sampling the same hypothesis class at different rates does not create interferometric resolution. In radio interferometry, two antennas with identical receivers pointed at the same patch of sky at different times produce redundant data, not higher resolution — the baseline is spatial, not temporal, and requires physically distinct vantage points. The analogue for multi-timescale systems: "run the same model five times at different speeds" yields large B but D = 0, producing no resolution gain. "Run five models with different training data, architectures, and priors at different speeds" yields large B and D > 0, enabling leverage.

In practice, "add more models" fails when models share training data, priors, or institutional incentives — yielding large B but near-zero effective D. The same pathology appears in institutional contexts: a "diverse" committee whose members were selected by the same process, trained in the same programs, and subject to the same incentive structure has large nominal B (different roles, different reporting cadences) but near-zero effective D. The committee produces the appearance of reconciliation without the epistemic independence that makes reconciliation informative.

This paper treats D as an external condition and leaves its formalization to future work. The gap is real: a full gain geometry would include D as a term in the resolution scaling law (R_Δ ~ B · D · F rather than R_Δ ~ B · F), with D measured as some form of mutual information deficit between the hypothesis spaces of the components. That formalization is open.

In other words: baseline is necessary but not sufficient. Leverage requires both phase coherence and non-degenerate baselines — temporal *and* perspectival.

### 9.3 Relation to Existing Work

The distinction between destructive and constructive diversity has precedents in several traditions:

- **Requisite variety** [17]: Ashby's law of requisite variety establishes that a controller must have at least as much variety as the system it controls. The gain geometry adds that variety must be *reconciled*, not merely present — a system with high variety and no correlator is in shear, not leverage.

- **Dialectical method** (Hegel): Thesis and antithesis produce synthesis through opposition. The gain geometry formalizes the conditions under which this works (leverage) versus when it produces false synthesis (capture).

- **Ensemble methods** [18]: Model diversity improves ensemble performance, but only when errors are uncorrelated and combination preserves information. Dietterich's analysis of ensemble conditions — that diversity improves prediction only when the combination rule preserves minority signals — is the leverage condition applied to prediction. Majority vote is a low-fidelity correlator; stacking with learned weights is higher-fidelity.

- **Adversarial collaboration** [19]: Mellers, Hertwig, and Kahneman's formalization of adversarial collaboration — structured disagreement between researchers with opposing hypotheses — is leverage by design. The protocol specifies a shared dataset (baseline), binding pre-registration (authority), and joint publication regardless of outcome (fidelity). When any of these conditions fails, the collaboration degrades to either shear (parallel publication, no reconciliation) or capture (the dominant lab's framing absorbs the dissenting view).

- **Agonistic pluralism** [20]: Mouffe's distinction between productive political contestation (agonism) and destructive antagonism maps directly onto the leverage/shear boundary. The gain geometry adds the capture regime that Mouffe's framework implies but does not name: the condition where political "reconciliation" proceeds by suppressing the pluralism that makes contestation productive — manufactured consensus that passes democratic throughput checks while collapsing the representational diversity that democracy is meant to preserve.

### 9.4 The Recursive Trap

Any framework that describes its own operation risks the collapse it diagnoses. The process that produced this paper — routing disagreement between AI systems through a human reconciliation node — is itself a leverage-mode operation. Continued meta-analysis of that process would eventually transition from leverage to capture: generating performance artifacts that look like insight while the marginal resolution drops below the marginal distortion.

The cybernetic Daoist answer: stop when marginal resolution drops below marginal distortion. Not because recursion is bad, but because continued refinement of the insight about refining the insight is the specific failure mode that feels like progress while producing nothing.

This paper stops here.

---

## 10. Conclusions

The Δt framework needed a positive case.

Papers 1–15 built the failure geometry: how temporal mismatch tears systems apart (shear), how scalar optimization produces false coherence (capture, though it was not named as such), and how governors contain the damage. The framework had a cost term but no gain term. It could explain why systems fail but not why temporal diversity is worth preserving.

The gain geometry completes the framework. Temporal mismatch is not monotonically harmful. It is a baseline — a source of discriminating power whose sign depends on the quality of the correlator. Systems that eliminate mismatch gain stability but lose resolution. Systems that instrument mismatch through high-fidelity reconciliation gain both.

The three regimes — shear, leverage, and capture — are now the complete primitive set:

- **Shear:** Baseline exceeds correlator capacity. System tears. (Papers 1, 2, 5, 9, 13, 14)
- **Leverage:** Baseline within correlator limits, high fidelity. System gains resolution. (Paper 12, and the unnamed positive cases across the series)
- **Capture:** Correlator has high throughput and authority but low fidelity. System produces false coherence while collapsing eigenstructure. (Papers 3, 4, 6, 8)

The critical variable is not Δt alone but Δt relative to correlator quality **K** = (throughput, fidelity, authority, cost budget). The design principle is not "reduce mismatch" but "maximize baseline subject to coherence constraints." The institutional investment is not alignment but translation bandwidth — the capacity to convert difference into correction.

The governor is not merely a brake. It is a correlator. And the contradiction ledger is not a cost center. It is the instrument's readout.

**Difference is either stress or power depending on whether you can translate it into correction.**

---

## References

[1] Beck, J. (2025). The Coherence Criterion: A Unified Framework for Stability in Hierarchical Systems. Preprint, Δt Framework Paper 1. doi:10.5281/zenodo.17726789

[2] Beck, J. (2025). The Second Law of Organizations: How Temporal Lag Drives Irreversible Institutional Decay. Preprint, Δt Framework Paper 2. doi:10.5281/zenodo.14606702

[3] Beck, J. (2025). Scalar Reward Collapse: A General Theory of Eigenstructure Evaporation in Closed-Loop Systems. Preprint, Δt Framework Paper 3.

[4] Beck, J. (2025). Eigenstructure Collapse in Social Media Platforms: An Application of Scalar Reward Dynamics Theory. Preprint, Δt Framework Paper 4.

[5] Beck, J. (2025). Control Laws for Hierarchical Kinetics: Design Principles and Intervention Strategies for Multi-Timescale Systems. Preprint, Δt Framework Paper 5.

[6] Beck, J. (2025). Temporal Closure Requirements for Synthetic Coherence: Architectural Foundations and the Simulator Gap. Preprint, Δt Framework Paper 6.

[7] Beck, J. (2025). Δt-Constrained Inference: A General Model of Temporal Coherence in Hierarchical Systems. Preprint, Δt Framework Paper 7.

[8] Beck, J. (2025). Detecting Temporal Debt in Language Models and Software Systems: Applications of Δt-Constrained Inference. Preprint, Δt Framework Paper 8.

[9] Beck, J. (2025). Capacity-Constrained Stability: A Control-Theoretic Framework for Institutional Resilience. Preprint, Δt Framework Paper 9.

[10] Beck, J. (2026). You Need More Than Just Attention: Invariant Requirements for Temporal Coherence in AI Systems. Preprint, Δt Framework Paper 10.

[11] Beck, J. (2026). Representational Invariance and the Observer Problem in Language Model Alignment. Preprint, Δt Framework Paper 11.

[12] Beck, J. (2026). Bounded Lattice Inference: A Governed Reasoning Substrate with Persistent State and Non-Linguistic Authority. Preprint, Δt Framework Paper 12.

[13] Beck, J. (2026). Temporal Asymmetry in Censorship Systems. Preprint, Δt Framework Paper 13.

[14] Beck, J. (2026). The Temporal Attack Surface: A Δt Framework for Asynchronous Security Systems. Preprint, Δt Framework Paper 14.

[15] Beck, J. (2026). Cybernetic Fault Domains: When Commitment Outruns Verification. Preprint, Δt Framework Paper 15. doi:10.5281/zenodo.18686130

[16] Thompson, A.R., Moran, J.M., and Swenson, G.W. (2017). *Interferometry and Synthesis in Radio Astronomy.* 3rd edition. Springer.

[17] Ashby, W.R. (1956). *An Introduction to Cybernetics.* Chapman & Hall.

[18] Dietterich, T.G. (2000). Ensemble Methods in Machine Learning. *Multiple Classifier Systems* (MCS 2000), Springer LNCS 1857, pp. 1–15.

[19] Mellers, B., Hertwig, R., and Kahneman, D. (2001). Do Frequency Representations Eliminate Conjunction Effects? An Exercise in Adversarial Collaboration. *Psychological Science* 12(4), pp. 269–275.

[20] Mouffe, C. (2013). *Agonistics: Thinking the World Politically.* Verso.
