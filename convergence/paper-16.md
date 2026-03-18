# Paper 16 — Signed Geometry — Convergence Spike

**Full title:** The Gain Geometry of Temporal Mismatch: Shear, Leverage, and Capture in Multi-Timescale Systems
**Date:** 2026-02-20
**DOI:** 10.5281/zenodo.18717619

## Status: spiked 2026-03-18

## Claim Cluster
- Δt separation is not a monotone hazard; its effect is signed by correlator properties, yielding three distinct regimes: shear, leverage, and capture
- The same temporal separation that produces destructive shear under weak coupling produces constructive leverage under strong coupling (higher epistemic resolution through structured disagreement)
- Capture inflates apparent fidelity by narrowing the representational alphabet — the metric is compromised by the same mechanism it is meant to detect
- The critical variables are system baseline B (timescale separation) and correlator quality K = (throughput, fidelity, authority, cost budget)
- The design principle is: maximize baseline subject to correlator integrity, rather than minimizing mismatch

## Search Terms
- multi-timescale structured disagreement epistemic resolution
- temporal mismatch constructive vs destructive
- diversity-stability tradeoff multi-scale systems
- correlator quality coupling strength information gain
- capture metric corruption representational narrowing
- interferometry structured disagreement measurement
- epistemic leverage timescale separation
- Goodhart metric corruption self-reference

## Expected Convergence Level
hints expected
The idea that diversity of timescales can be beneficial is present in ecology and some organizational theory, but the specific three-regime classification (shear/leverage/capture) with correlator quality as the sign-determining variable is likely novel. Capture as metric corruption through representational narrowing may overlap with Goodhart literature.

## Hits

### STRONG CONVERGENCE — Capture as representational narrowing / metric corruption

1. **"On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization"**
   - Authors: Xie et al.
   - Year: 2024 (arxiv), 2025 (JASA)
   - Venue: arXiv:2405.16455; Journal of the American Statistical Association Vol 120
   - Match type: Strong convergence on the capture regime
   - Claims matched: Capture inflates apparent fidelity by narrowing representational alphabet; high throughput + high authority + low fidelity = capture
   - How close: Proves that KL-regularized RLHF creates "preference collapse" where minority preferences are asymptotically driven to 0% — the optimization achieves high apparent alignment by destroying representational diversity. This is Paper 16's capture regime instantiated in a specific domain. They do not generalize to the three-regime framework or use the correlator/baseline vocabulary, but the mechanism is identical: high-throughput, high-authority, low-fidelity reconciliation produces false coherence.

2. **"Strong Model Collapse"**
   - Authors: Dohmatob, Feng, Niu et al.
   - Year: 2024 (arxiv), 2025 (ICLR)
   - Venue: ICLR 2025
   - Match type: Strong convergence on capture dynamics
   - Claims matched: Capture narrows representational alphabet; metric is compromised by the mechanism it should detect
   - How close: Proves that even 0.1% synthetic data in training causes irreversible model collapse — the model reinforces its own oversimplifications recursively. This is capture in Paper 16's terms: the training loop has high throughput and authority but low fidelity (synthetic data lacks real-world diversity), and the output metric (loss/perplexity) cannot detect the collapse because it is measured on the same narrowed distribution.

3. **"Epistemic Destabilization: AI-Driven Knowledge Generation and the Collapse of Validation Systems"**
   - Authors: Singh
   - Year: 2025
   - Venue: AAAI/ACM AIES-25
   - Match type: Strong convergence on capture dynamics and correlator overload
   - Claims matched: Capture as false coherence; shear from correlator overload (throughput < load); metric corruption
   - How close: Models destabilization as three interacting mechanisms: epistemic inflation (oversupply vs verification capacity = Paper 16's throughput overload), recursive drift (self-reinforcing deviation = capture's lossy self-reference), and validation fatigue (degradation of validators = correlator cost budget exhaustion). Provides operational diagnostics (resilience gradient, drift divergence, validator fatigue thresholds). Very close to Paper 16's framework but framed as AI-specific rather than as a general multi-timescale architecture. Does not have the signed-baseline concept or the leverage regime.

4. **"Epistemic Diversity and Knowledge Collapse in Large Language Models"**
   - Authors: Wright et al.
   - Year: 2024–2025
   - Venue: arXiv:2510.04226
   - Match type: Strong convergence on capture and representational narrowing
   - Claims matched: Capture narrows representational alphabet; diversity is the countermeasure
   - How close: Empirically shows all 27 tested LLMs are less epistemically diverse than a basic web search; model size has *negative* impact on epistemic diversity. This is a measurement of capture in operation. The complementary paper (arXiv:2512.15011) shows epistemic diversity across models mitigates collapse "but only up to an optimal level" — which hints at Paper 16's leverage regime (diversity as constructive) with a boundary condition.

5. **"Categorizing Variants of Goodhart's Law"**
   - Authors: Manheim & Garrabrant
   - Year: 2018 (MIRI)
   - Venue: arXiv:1803.04585
   - Match type: Strong convergence on capture taxonomy
   - Claims matched: Capture as metric corruption; four mechanisms (regressional, extremal, causal, adversarial)
   - How close: The four-variant taxonomy describes mechanisms by which optimizing on a proxy destroys the proxy-goal correlation. Paper 16's capture regime is a superset that explains *why* these failures share a common structure (high T, high A, low F) and connects them to the broader signed-baseline framework. Manheim & Garrabrant lack the timescale dimension and the constructive (leverage) counterpart.

### MODERATE CONVERGENCE — Disagreement as epistemically valuable

6. **"The Value of Disagreement in AI Design, Evaluation, and Alignment"**
   - Authors: Fazelpour & Fleisher
   - Year: 2025
   - Venue: ACM FAccT 2025
   - Match type: Moderate convergence on leverage regime
   - Claims matched: Structured disagreement produces epistemic gain; elimination of disagreement (homogenization) is harmful
   - How close: Argues that "perspectival homogenization" — suppressing disagreement in AI pipelines — is epistemically and ethically harmful. Identifies three stages where disagreement adds value. This converges on Paper 16's leverage regime (structured disagreement = higher resolution) and its warning against eliminating mismatch (= destroying baseline). However: no timescale framing, no formal regime classification, no correlator quality vector, no capture/shear distinction. The insight is domain-specific (AI annotation/alignment) rather than architectural.

7. **"Disagreement and epistemic improvement"**
   - Authors: (Synthese, 2021)
   - Year: 2021
   - Venue: Synthese
   - Match type: Moderate convergence on leverage concept
   - Claims matched: Disagreement can be constructive for knowledge production
   - How close: Social epistemology argument that disagreement under certain conditions improves collective inquiry. Supports the leverage regime's core insight but has no formal framework, no timescale dimension, no regime classification.

### MODERATE CONVERGENCE — Diversity-stability across scales

8. **"Diversity-stability relationships become decoupled across spatial scales"**
   - Authors: Wisnoski et al.
   - Year: 2023
   - Venue: Ecology (Wiley)
   - Match type: Moderate convergence on signed-baseline concept
   - Claims matched: The effect of diversity on stability is not monotone — it is scale-dependent and can decouple
   - How close: Shows that diversity-stability relationships that hold locally do not persist at broader scales, across multiple taxa and ecosystem types. This is the ecological analogue of Paper 16's claim that Δt is not a monotone hazard — the same structural variable (diversity/separation) has different signs at different scales. But the mechanism is spatial scale, not timescale, and there is no correlator/reconciliation framework.

### MODERATE CONVERGENCE — Timescale separation in control theory

9. **"Consensus control and performance recovery via two-time-scale separation"**
   - Authors: Mohammadalizadeh, Arefi & Khayatian
   - Year: 2026
   - Venue: Scientific Reports
   - Match type: Moderate convergence on beneficial timescale separation
   - Claims matched: Timescale separation as a design tool (not just a hazard); performance recovery through separation
   - How close: Uses two-timescale separation constructively to achieve consensus AND recover transient performance in multi-agent systems. This is the control-theory analogue of leverage: separation is the tool, not the problem. But: purely technical (no epistemic framing), no regime classification, no capture concept.

10. **"Multiscale spatiotemporal control of neuronal networks: a complex systems perspective"**
    - Authors: (Frontiers in Computational Neuroscience, 2018)
    - Year: 2018
    - Venue: Frontiers in Computational Neuroscience
    - Match type: Moderate convergence on gain regimes from timescale interaction
    - Claims matched: High-gain regimes in multi-timescale systems produce qualitatively different dynamics (chaotic vs stable)
    - How close: Shows that recurrent networks at high gain show chaotic dynamics sensitive to noise, while at lower gain they are stable. This is a regime classification based on gain, but it is a single axis (gain magnitude), not the two-axis (baseline x correlator quality) framework of Paper 16.

### WEAK CONVERGENCE — Viable System Model / organizational cybernetics

11. **Beer's Viable System Model (VSM)**
    - Authors: Stafford Beer
    - Year: 1972–1985 (classic); recent applications 2024
    - Venue: various
    - Match type: Weak convergence on correlator concept
    - Claims matched: Variety attenuation/amplification as a reconciliation mechanism between organizational levels operating at different timescales
    - How close: VSM's variety engineering (attenuate variety downward, amplify upward) is a proto-correlator architecture. The requirement that "communication along channels must be fast enough to keep up" is the throughput constraint. But VSM does not formalize the signed-baseline concept, does not identify capture as a distinct failure mode, and does not derive the "maximize baseline subject to correlator integrity" design principle. The VSM's instinct is to match variety (minimize mismatch), not to maximize baseline.

12. **Singular perturbation theory / geometric singular perturbation theory**
    - Authors: Fenichel, Tikhonov, many others
    - Year: 1960s–present
    - Venue: SIAM, various
    - Match type: Weak convergence on timescale separation as a design tool
    - Claims matched: Timescale separation enables model reduction and control design
    - How close: GSPT treats timescale separation as structure to be exploited for analytical simplification (slow manifold reduction). This is "leverage" in a narrow mathematical sense — separation enables something you could not do without it. But it is about mathematical tractability, not epistemic resolution, and has no concept of correlator quality, capture, or regime classification.

### NO CONVERGENCE FOUND

- No published work found that uses the specific three-regime classification (shear/leverage/capture)
- No published work found that formalizes correlator quality as a vector K = (T, F, A, C)
- No published work found that derives the "maximize baseline subject to correlator integrity" design principle
- No published work found that uses the interferometry-to-social-systems structural correspondence as a formal analogy for multi-timescale system design
- No published work found that identifies capture as a regime where metric corruption is endogenous to the reconciliation mechanism itself (rather than external gaming)

## Notes

The convergence landscape is exactly as predicted: individual fragments exist across multiple fields, but they are siloed and none assembles the full architecture.

**Capture is the most convergent claim.** The RLHF preference collapse literature (Xie et al. 2024), strong model collapse (ICLR 2025), epistemic destabilization (Singh 2025), and Goodhart taxonomy (Manheim & Garrabrant 2018) all describe mechanisms that Paper 16 would classify as capture. But none of them:
- Recognize capture as one regime in a three-regime framework
- Identify a constructive counterpart (leverage)
- Formalize the correlator quality vector that determines regime boundaries
- Connect capture to timescale separation as the baseline variable

**Leverage is moderately convergent.** Fazelpour & Fleisher (FAccT 2025) argue for disagreement as epistemically valuable; Wisnoski et al. (2023) show diversity-stability is scale-dependent; control theory uses timescale separation constructively. But none frames this as a regime within a unified signed-baseline framework.

**The signed-baseline concept itself is novel.** No published work treats Δt (timescale separation) as a variable whose effect is signed by correlator quality, yielding distinct regimes. The closest is GSPT's exploitation of separation for analytical purposes, but this is a different level of abstraction entirely.

**The interferometry correspondence is novel.** No published work maps baseline/correlator/resolution from radio interferometry onto organizational or epistemic systems.

## Verdict

**Expected convergence level confirmed: hints present, core architecture novel.**

The individual components — capture as metric corruption, disagreement as epistemic resource, timescale separation as exploitable structure, diversity-stability scale-dependence — all have independent support in the literature. What remains novel in Paper 16 is:

1. The **signed-baseline reframing**: Δt as a design parameter whose sign depends on correlator quality, not as a monotone hazard
2. The **three-regime classification** (shear/leverage/capture) with formal boundary conditions
3. The **correlator quality vector** K = (T, F, A, C) as the sign-determining variable
4. The **capture-as-endogenous-metric-corruption** framing (not external gaming, but the reconciliation mechanism itself destroying the degrees of freedom it claims to preserve)
5. The **design principle**: maximize baseline subject to correlator integrity (vs. the intuitive "minimize mismatch")
6. The **interferometry structural correspondence** as a formal analogy

The paper's claims are well-supported by converging independent work but the synthesis is original. The strongest external validation comes from the RLHF/model-collapse literature, which independently discovered capture dynamics without the unifying framework. The paper should cite Xie et al. (2024), Singh (2025), Fazelpour & Fleisher (2025), and the strong model collapse work as convergent evidence.
