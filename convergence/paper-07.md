# Paper 07 — Δt-Constrained Inference — Convergence Spike

**Full title:** Δt-Constrained Inference: A General Model of Temporal Coherence in Hierarchical Systems
**Date:** 2025-12-08
**DOI:** 10.5281/zenodo.17857541

## Status: completed 2026-03-18

## Claim Cluster
- Confidence growth rate must not exceed evidence accumulation rate, formalized as the differential inequality dC/dt ≤ k·dE/dt
- Violations of this constraint accumulate as temporal debt D(t), a measure of structural fragility invisible in local observations
- Three distinct regimes exist: coherent inference, metastable inference, and collapse, with phase boundaries determined by the confidence-evidence inequality
- Metastable inference states appear functional but are structurally fragile and will collapse under perturbation
- Meta-plausibility (appearing plausible without grounding) is one instantiation of the general temporal debt principle

## Search Terms
- confidence calibration evidence accumulation rate
- epistemic overconfidence fragility hidden risk
- metastability inference systems phase transition
- confidence-evidence gap measurement
- calibration debt technical debt analogy
- Bayesian inference rate constraints hierarchical
- hidden fragility metastable systems
- overconfidence accumulation systemic collapse

## Expected Convergence Level
partial convergence likely
Calibration research and overconfidence detection are active fields. The specific differential inequality framing and temporal debt as a measurable quantity are likely novel, but the underlying observation that confidence can outrun evidence is well-recognized in epistemology and decision science.

## Hits

### STRONG CONVERGENCE (same problem, overlapping formalism or diagnosis)

**1. Okutomi (2025) — "Stable but Miscalibrated: A Kantian View on Overconfidence from Filters to Large Language Models"**
- Authors: Akira Okutomi
- Year: 2025 (arXiv: 2510.14925, revised Dec 2025)
- Venue: arXiv preprint
- Match type: STRONG — independently identifies stable-but-fragile epistemic states
- Claims matched: metastable inference (Claim 4), confidence-evidence decoupling, hidden fragility
- How close: Formalizes "H-Risk" as a composite instability index (spectral margin, conditioning, temporal sensitivity, innovation amplification). Finds that LLM hallucinations behave as "robust but misaligned attractors" — confidently wrong answers are at least as locally stable as correct ones, creating "stable miscalibration." This is Paper 07's metastable inference zone described from a control-theoretic angle. Does NOT frame this as temporal debt accumulation or provide the differential inequality, but arrives at the same structural diagnosis: systems can be simultaneously stable and epistemically broken.
- Gap: No integral debt measure. No conservation-law framing. No three-regime taxonomy. The Kantian framing is philosophical scaffolding rather than mathematical formalism.

**2. Viteri & DeDeo (2022) — "Epistemic Phase Transitions in Mathematical Proofs"**
- Authors: Scott Viteri, Simon DeDeo
- Year: 2022 (arXiv: 2004.00055)
- Venue: Cognition, Volume 225, August 2022
- Match type: STRONG — independently formalizes epistemic phase transitions and metastable states
- Claims matched: three regimes (Claim 3), metastability (Claim 4), phase transitions in epistemic systems
- How close: Under belief formation combining deductive and abductive reasoning, proofs exhibit phase transitions from uncertainty to near-complete confidence. Critically, they identify metastable states ("domain walls" that freeze into all-true or all-false states) and cascade failures driven by small-number statistics. Overconfidence in one reasoning mode frustrates transitions — directly analogous to confidence outrunning evidence bandwidth. The network structure that enables phase transitions maps onto the hierarchical layers in Paper 07.
- Gap: Applies to proof networks, not general inference systems. No temporal debt integral. No dC/dt <= k*dE/dt constraint. The metastability is structural (network topology) rather than temporal (rate mismatch).

**3. Williams (2025) — "From Temporal Decay to Epistemic Fragility: A Structural Reconstruction of Discounting through Entropic Valuation"**
- Authors: Clayton Fraser Williams
- Year: 2025 (SSRN: 5277737, posted May 2025)
- Venue: SSRN preprint
- Match type: STRONG — identifies the same categorical error (conflating temporal distance with epistemic uncertainty)
- Claims matched: confidence decay with temporal lag (Claims 1-2), temporal debt concept
- How close: Argues classical discounting conflates temporal distance with epistemic uncertainty. Reinterprets value attenuation as a function of "entropic fragility" — the quantifiable disorder in inferential structure. Constructs an entropy-derived confidence coefficient that replaces time-based discounting. This is structurally parallel to Paper 07's support function f_support(E, dt) which bounds confidence by evidential support at a given temporal separation. Both papers identify the same fundamental error: treating time as a direct cause of epistemic degradation rather than as a proxy for evidential thinning.
- Gap: Focused on financial discounting, not general inference systems. Uses information-theoretic (Shannon entropy) rather than differential-inequality formalism. No three-regime taxonomy or metastability concept.

**4. Gilda & Gilda (2026) — "AI-Assisted Engineering Should Track the Epistemic Status and Temporal Validity of Architectural Decisions"**
- Authors: Sankalp Gilda, Shlok Gilda
- Year: 2026 (arXiv: 2601.21116, January 2026)
- Venue: arXiv preprint
- Match type: STRONG — independently proposes tracking temporal validity of confident claims, evidence decay, and trust inflation
- Claims matched: temporal debt (Claim 2), confidence-evidence decoupling, evidence staleness
- How close: Proposes three requirements closely mirroring Paper 07's framework: (1) epistemic layers separating unverified hypotheses from validated claims (cf. hierarchical layers), (2) conservative aggregation preventing weak evidence from inflating confidence (cf. dC/dt <= k*dE/dt), (3) automated evidence decay tracking (cf. temporal debt). Finds ~25% of architectural decisions had evidence expire within two months. Uses Godel t-norm for conservative aggregation. Empirically demonstrates that without temporal tracking, stale assumptions cause failures — a concrete instantiation of temporal debt triggering collapse.
- Gap: Domain-specific (software architecture). No differential inequality formalism. No metastability concept or three-regime taxonomy. Practical engineering rather than theoretical framework.

### MODERATE CONVERGENCE (same problem area, different formalism or partial overlap)

**5. Huang et al. (2024) — "Confidence is not Timeless: Modeling Temporal Validity for Rule-based Temporal Knowledge Graph Forecasting"**
- Authors: Rikui Huang, Wei Wei, Xiaoye Qu, Shengzhe Zhang, Dangyang Chen, Yu Cheng
- Year: 2024
- Venue: ACL 2024 (62nd Annual Meeting)
- Match type: MODERATE — models temporal decay of rule confidence
- Claims matched: confidence decay with temporal separation (Claim 1 partially)
- How close: Title directly states Paper 07's core insight. Designs time functions modeling interaction between temporal information and confidence for knowledge graph forecasting. Demonstrates that rule confidence must be temporally indexed — static confidence scores are insufficient. However, this is applied to knowledge graph link prediction, not general inference systems.
- Gap: Purely empirical/applied (knowledge graphs). No differential inequality. No debt accumulation. No metastability or regime classification.

**6. Bayesian Epistemic Zoning / BEZ Framework (2025) — "Uncertainty-Calibrated Decision Thresholds in Bayesian AI Systems"**
- Authors: (from Research Square preprint rs-8991228)
- Year: 2025
- Venue: Research Square preprint
- Match type: MODERATE — classifies decisions by epistemic stability and fragility
- Claims matched: regime classification (Claim 3), hidden fragility (Claim 2)
- How close: Introduces Bayesian Epistemic Zoning that classifies decisions as "sufficiently stable for action," "exploratory," or "epistemically misleading despite favorable numerical appearance." The third category directly maps to Paper 07's metastable inference zone. Replaces convention-based cutoffs with uncertainty-calibrated limits derived from posterior variance.
- Gap: Static classification rather than dynamic (no temporal evolution). No rate constraints. No debt accumulation. Bayesian posterior framework rather than differential inequality.

**7. Sculley et al. (2015, extended) — "Hidden Technical Debt in Machine Learning Systems"**
- Authors: Sculley, Holt, Golovin, et al.
- Year: 2015 (NeurIPS), with ongoing influence through 2025
- Venue: NeurIPS 2015
- Match type: MODERATE — "technical debt" as hidden fragility accumulation
- Claims matched: debt accumulation (Claim 2), hidden fragility
- How close: Introduced the metaphor of ML systems as "high-interest credit cards of technical debt." Identifies calibration layers, glue code, and pipeline jungles as debt that silently accumulates. The metaphor of invisible-until-crisis fragility is structurally identical to temporal debt. However, this is organizational/engineering debt, not formalized as a mathematical quantity.
- Gap: Metaphorical rather than formal. No differential inequality. No temporal dynamics. No phase transitions or regime classification.

**8. Hagar (2025) — "Not Wrong, But Untrue: LLM Overconfidence in Document-Based Queries"**
- Authors: Nick Hagar
- Year: 2025 (arXiv: 2509.25498, September 2025)
- Venue: arXiv preprint
- Match type: MODERATE — empirically demonstrates "interpretive overconfidence"
- Claims matched: confidence-evidence gap (Claims 1-2), meta-plausibility (Claim 5)
- How close: Finds 30% of LLM outputs contain hallucinations, but most are NOT invented facts — they are "interpretive overconfidence" where models add unsupported characterizations and transform attributed opinions into general statements. This is precisely meta-plausibility: outputs that appear plausible without evidential grounding. The distinction between "not wrong" (locally coherent) and "untrue" (evidentially unsupported) maps directly to the metastable inference zone.
- Gap: Empirical observation without theoretical framework. No formalization. No rate constraints or debt accumulation. Journalism-focused evaluation.

**9. Active Inference / Free Energy Principle — Hierarchical Temporal Models (Friston et al., ongoing)**
- Authors: Karl Friston and collaborators
- Year: Ongoing (key papers 2017-2025)
- Venue: Various (Neuroscience of Consciousness, PLoS ONE, etc.)
- Match type: MODERATE — hierarchical systems with precision-weighted prediction errors across timescales
- Claims matched: hierarchical temporal constraints (Claims 1, 3), confidence bounding
- How close: Active inference models process information across hierarchical layers at different timescales, with precision (inverse variance) weighting prediction errors at each level. High precision amplifies influence of prediction errors; low precision attenuates them. This is structurally analogous to the coupling constant k in dC/dt <= k*dE/dt, where precision plays the role of evidence bandwidth. The free energy principle bounds beliefs by evidence in a way that parallels the temporal coherence constraint.
- Gap: Different formalism (variational inference / free energy minimization vs. differential inequality). No explicit "temporal debt" integral. No three-regime taxonomy. The framework assumes organisms minimize free energy rather than characterizing what happens when they fail to do so.

### WEAK CONVERGENCE (tangential or different problem with shared vocabulary)

**10. "Mind the Confidence Gap" (2025) — Overconfidence, Calibration, and Distractor Effects in LLMs**
- Year: 2025 (arXiv: 2502.11028)
- Match type: WEAK — measures calibration gaps but no temporal dynamics
- Claims matched: confidence-evidence gap measurement only

**11. Strong Model Collapse (2024) — Shumailov et al.**
- Year: 2024 (arXiv: 2410.04840)
- Match type: WEAK — collapse from synthetic data, not from temporal debt
- Claims matched: collapse regime only (Claim 3), and only superficially

**12. OpenAI (2025) — "Why Language Models Hallucinate"**
- Year: 2025
- Match type: WEAK — acknowledges training objectives reward confident guessing over calibrated uncertainty
- Claims matched: meta-plausibility (Claim 5), but no formalization

## Notes

**What converges:**
- The observation that confidence can decouple from evidence is widely recognized (Okutomi, Hagar, Gilda, Williams, calibration literature broadly)
- Metastable epistemic states — appearing functional while being fragile — are independently identified in at least three distinct domains: control theory (Okutomi), proof networks (Viteri & DeDeo), software architecture (Gilda & Gilda)
- Temporal decay of confidence validity is being actively modeled (Huang et al., Williams)
- The active inference literature provides a parallel hierarchical framework with precision-weighted prediction errors across timescales

**What remains novel in Paper 07:**
1. The specific differential inequality dC/dt <= k*dE/dt as a universal constraint on inference systems — no one else formalizes this as a rate constraint with coupling constant
2. Temporal debt D(t) as an integral measure of accumulated confidence-evidence mismatch — Williams comes closest with "entropic fragility" but uses a different formalism
3. The three-regime taxonomy (coherent / metastable / collapse) as a unified classification with formal boundary conditions — BEZ comes closest but is static, not dynamic
4. The support function f_support(E, dt) with its three required properties (monotonicity, boundedness, locality) — this specific formalization appears to be original
5. The conservation-law analogy (debt as epistemic potential energy) — no existing work frames this explicitly
6. The coherence gradient (dC/dL) as a diagnostic for layer decoupling — this specific measure is novel
7. The unification: treating meta-plausibility, LLM hallucination, calibration failure, and institutional overconfidence as instantiations of ONE underlying temporal mismatch principle

**Key observation:** The convergence pattern is "many groups see the elephant from different angles." Okutomi sees it through control theory, Viteri/DeDeo through network phase transitions, Williams through information-theoretic discounting, Gilda through software engineering, the calibration community through statistical measures. Paper 07's contribution is the claim that these are all the same elephant, formalized as a single differential inequality with measurable consequences.

## Verdict

**PARTIAL CONVERGENCE — as predicted.** The underlying observation (confidence can outrun evidence, creating hidden fragility) is well-recognized across multiple fields. However, the specific formalization as a differential inequality with integral debt, three-regime classification, support function properties, and cross-domain unification appears to be genuinely novel as of March 2026.

**Strongest independent support:** Okutomi (2025) and Gilda & Gilda (2026), both of which arrive at structurally similar diagnoses from different starting points — Okutomi showing stable miscalibration as an attractor state, Gilda showing evidence decay and trust inflation in engineering decisions. Neither provides the unifying mathematical framework that Paper 07 offers.

**Strongest challenge:** The active inference / free energy principle literature (Friston et al.) provides an alternative and more established framework for bounding beliefs by evidence in hierarchical systems. A reviewer could argue that Paper 07's framework is a special case of free energy minimization failure. Paper 07 should address this relationship explicitly — it currently references Kuehn (multiscale dynamics) but not Friston (active inference), which is a gap in the related work section.

**Recommendation:** Cite Okutomi (2025), Viteri & DeDeo (2022), Williams (2025), Gilda & Gilda (2026), and Huang et al. (2024) as independent convergent work. Address the active inference relationship. The differential inequality formalism, temporal debt integral, and cross-domain unification remain the paper's defensible novel contributions.
