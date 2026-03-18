# Paper 08 — Detecting Temporal Debt — Convergence Spike

**Full title:** Detecting Temporal Debt in Language Models and Software Systems: Applications of Δt-Constrained Inference
**Date:** 2025-12-08
**DOI:** 10.5281/zenodo.17859323

## Status: completed (2026-03-18)

## Claim Cluster
- LLM hallucination (15-50% on factual queries with 80%+ reported confidence) and software project "Green status before collapse" share the same structural mechanism: confidence outpacing evidential support
- RLHF training creates structural incentives for temporal debt accumulation in language models
- Semantic stability can operationalize the evidential support function for LLM outputs
- Velocity variance and temporal proximity to deadline operationalize the support function for software delivery
- Systems can be classified into coherent, metastable, or collapse regimes using deployable diagnostic implementations

## Search Terms
- LLM hallucination detection confidence calibration
- RLHF overconfidence sycophancy training incentive
- software project failure prediction green status
- semantic stability hallucination metric
- enterprise software deadline collapse prediction
- confidence calibration language model deployment
- project estimation velocity variance risk
- hallucination gating retrieval augmented generation

## Expected Convergence Level
strong convergence likely
LLM hallucination detection is an extremely active research area. The RLHF-overconfidence link is increasingly discussed. Software project failure prediction is a mature field. The unifying framing is novel but the individual domain findings likely have many independent parallels.

## Hits

### A. DIRECT CONVERGENCE — Same mechanism, independently identified

**1. Farquhar et al., "Detecting hallucinations in large language models using semantic entropy," Nature 630 (2024)**
- **Match type:** Direct convergence on semantic stability as hallucination detector
- **Claims matched:** Semantic stability operationalizes evidential support (Claim 3); regime classification via consistency (Claim 5)
- **How close:** Very close. They cluster semantically equivalent outputs and measure entropy across samples — functionally identical to Paper 08's consistency(outputs) term. Their "high semantic entropy = confabulation" maps directly to Paper 08's "low stability = collapse regime." They lack the temporal debt framing and the confidence-evidence gap formalization, but the detection mechanism is operationally equivalent.
- URL: https://www.nature.com/articles/s41586-024-07421-0

**2. Leng et al., "Taming Overconfidence in LLMs: Reward Calibration in RLHF," ICLR 2025 (arXiv:2410.09724)**
- **Match type:** Direct convergence on RLHF-overconfidence mechanism
- **Claims matched:** RLHF creates structural incentives for temporal debt (Claim 2); confidence-evidence decoupling (Claim 1)
- **How close:** Very close. They demonstrate empirically that "reward models used for PPO exhibit inherent biases towards high-confidence scores regardless of actual quality of responses." This is Paper 08's "RLHF trains models to decouple inference rate from evidence rate" stated in measurement terms. Their PPO-M and PPO-C variants are mitigation strategies for exactly the structural incentive Paper 08 identifies. They frame it as calibration error; Paper 08 frames it as temporal debt accumulation.
- URL: https://arxiv.org/abs/2410.09724

**3. Stangel & Bani-Harouni, "Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of LLMs," arXiv:2503.02623 (2025), under review ICLR 2026**
- **Match type:** Direct convergence on confidence gating via calibration
- **Claims matched:** Confidence gating deployment strategy (Section 3.5 of Paper 08); RLHF debt accumulation (Claim 2)
- **How close:** Very close. They model confidence calibration as a betting game where overconfidence is penalized — structurally equivalent to Paper 08's proposal to "use debt as a reward penalty during RLHF." Their logarithmic scoring rule penalizing over- and under-confidence is a specific implementation of the Δt constraint operator capping confidence at supportable levels.
- URL: https://arxiv.org/abs/2503.02623

**4. Gilda & Gilda, "AI-Assisted Engineering Should Track the Epistemic Status and Temporal Validity of Architectural Decisions," arXiv:2601.21116 (Jan 2026)**
- **Match type:** Direct convergence on temporal validity tracking and evidence staleness
- **Claims matched:** Confidence outpacing evidence in software systems (Claim 1); temporal decay in support function (Claim 4); regime classification (Claim 5)
- **How close:** Remarkably close. They propose: (1) epistemic layers separating conjecture from verified knowledge (cf. Paper 08's evidence vs. inference layers), (2) conservative aggregation preventing weak evidence from inflating confidence (cf. Δt constraint operator), (3) automated evidence decay tracking (cf. temporal decay term exp(-λ·Δt)). Their empirical finding that "20-25% of architectural decisions had stale evidence within two months" and "86% of staleness discovered only during incidents" directly validates the metastable regime concept. Published ~1 month after Paper 08.
- URL: https://arxiv.org/abs/2601.21116

### B. STRONG PARTIAL CONVERGENCE — Same domain, overlapping mechanism

**5. "The Dunning-Kruger Effect in Large Language Models: An Empirical Study of Confidence Calibration," arXiv:2603.09985 (Mar 2026)**
- **Match type:** Strong partial — empirical validation of overconfidence-accuracy decoupling
- **Claims matched:** Confidence outpacing evidence (Claim 1); RLHF-induced debt (Claim 2)
- **How close:** They demonstrate that poorly performing models show markedly higher overconfidence (ECE up to 0.726 with 23.3% accuracy), while better-calibrated models achieve lower ECE (0.122 with 75.4% accuracy). This is the Dunning-Kruger framing of the same phenomenon Paper 08 calls temporal debt. They validate the prediction that confidence and accuracy decouple most severely where knowledge is weakest, but lack the temporal/structural framing.
- URL: https://arxiv.org/abs/2603.09985

**6. "Epistemic Integrity in Large Language Models," arXiv:2411.06528 (2024)**
- **Match type:** Strong partial — epistemic mismatch concept
- **Claims matched:** Confidence-evidence decoupling (Claim 1); RLHF incentives (Claim 2)
- **How close:** Identifies "epistemic mismatch" where LLMs express unwarranted certainty despite low internal confidence. Models "default to confident, assertive language even when token-level certainty is low." This is the verbalized-confidence version of Paper 08's inference-layer-outpacing-evidence-layer. Different framing (linguistic vs. temporal), same structural observation.
- URL: https://arxiv.org/abs/2411.06528

**7. "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs," arXiv:2502.11028 (Feb 2025)**
- **Match type:** Strong partial — calibration measurement at scale
- **Claims matched:** Confidence-evidence gap (Claim 1); regime classification potential (Claim 5)
- **How close:** Large-scale empirical study showing persistent overconfidence even at larger scales, with "potential degradation in calibration performance with increased model size." Supports Paper 08's structural argument that the problem is architectural, not merely a training artifact. Does not formalize into regimes or temporal debt.
- URL: https://arxiv.org/html/2502.11028v3

**8. Sharma et al., "Towards Understanding Sycophancy in Language Models," Anthropic/ICLR 2024 (arXiv:2310.13548)**
- **Match type:** Strong partial — RLHF sycophancy as debt mechanism
- **Claims matched:** RLHF creates structural incentives for debt (Claim 2)
- **How close:** Demonstrates that RLHF preference data inherently incentivizes sycophancy — "matching a user's views is one of the most predictive features of human preference judgments." Paper 08 frames this as confidence outpacing evidence; Sharma et al. frame it as agreement outpacing truth. Same structural mechanism, different axis of analysis.
- URL: https://arxiv.org/abs/2310.13548

**9. Isaacs & Alvaro, "Analyzing Metastable Failures," HotOS 2025**
- **Match type:** Strong partial — metastable regime classification in distributed systems
- **Claims matched:** Three-regime classification (Claim 5); metastable zone as fragile-but-functional (Claim 1)
- **How close:** They classify distributed systems into stable/vulnerable/metastable states with clear tipping points, and build simulation frameworks to predict transitions. Their three states map directly to Paper 08's coherent/metastable/collapse. Key difference: they model load-based metastability in infrastructure, not confidence-evidence metastability in inference systems. The regime structure is convergent; the mechanism domain is different.
- URL: https://sigops.org/s/conferences/hotos/2025/papers/hotos25-106.pdf

**10. Bronson et al., "Metastable Failures in Distributed Systems," HotOS 2021 + Huang et al., "Metastable Failures in the Wild," OSDI 2022**
- **Match type:** Strong partial — established the metastability concept Paper 08 extends
- **Claims matched:** Regime classification (Claim 5)
- **How close:** The foundational work establishing metastable failures as a pattern. Paper 08 applies the same regime concept (stable/metastable/collapse) to inference systems rather than infrastructure. The 2025 follow-up (Hit 9) shows the field is moving toward predictive detection, which is where Paper 08 already operates.
- URL: https://dl.acm.org/doi/10.1145/3458336.3465286

### C. SUPPORTING CONVERGENCE — Different domain, compatible findings

**11. Flyvbjerg, "Top Ten Behavioral Biases in Project Management," Project Management Journal (2021)**
- **Match type:** Supporting — optimism bias and overconfidence in project reporting
- **Claims matched:** Green status before collapse (Claim 1); velocity variance (Claim 4)
- **How close:** Documents overconfidence bias as a top-10 project management pathology, including strategic misrepresentation and planning fallacy. Provides the behavioral evidence base for Paper 08's claim that management narrative outpaces engineering reality. Does not formalize into a temporal framework.
- URL: https://journals.sagepub.com/doi/full/10.1177/87569728211049046

**12. Snow et al., "The performance effects of optimistic and pessimistic project status reporting behavior," IJPM (2023)**
- **Match type:** Supporting — empirical study of status reporting bias
- **Claims matched:** Green status phenomenon (Claim 1); confidence-evidence gap in software delivery (Claim 4)
- **How close:** Analyzed 46,474 project status reports from 1,229 projects. Found that optimistic reporting initially helps but its positive effect diminishes throughout a project — consistent with Paper 08's prediction that temporal debt accumulates invisibly until it manifests as collapse. The finding that "reinforced behavior over time negatively affects impact" maps to debt accumulation.
- URL: https://www.sciencedirect.com/science/article/abs/pii/S0263786323000789

**13. Self-consistency hallucination detection literature (multiple papers, 2024-2025)**
- **Match type:** Supporting — operational implementations of consistency-based detection
- **Claims matched:** Semantic stability as support function (Claim 3); deployable diagnostics (Claim 5)
- **How close:** A large body of work (SAC3, INSIDE/EigenScore, SSC, AGSER) now uses multi-sample consistency as a hallucination signal — functionally equivalent to Paper 08's consistency(outputs) term. These are engineering implementations of the same intuition. None frame it as temporal debt or connect it to the software delivery domain.
- URL: https://www.emergentmind.com/topics/self-consistency-based-hallucination-detection

**14. Sprint velocity prediction using ML (multiple papers, 2024-2025)**
- **Match type:** Supporting — velocity-based delivery prediction
- **Claims matched:** Velocity variance as evidence signal (Claim 4)
- **How close:** Active research on using velocity variance, rolling averages, and statistical control limits for sprint prediction. Paper 08's use of μ/σ as evidence bandwidth is compatible with this work but frames it differently — as an epistemic support function rather than a forecasting input.
- URL: https://www.mdpi.com/2078-2489/15/11/726

**15. "Decoupling Reasoning and Confidence" (arXiv, 2025) + "Confidence Before Answering" (arXiv, 2026)**
- **Match type:** Supporting — architectural decoupling of confidence from reasoning
- **Claims matched:** Confidence-evidence decoupling (Claim 1); mitigation strategies (Section 3.5)
- **How close:** These propose architecturally separating confidence estimation from answer generation — a different solution path to the same problem Paper 08 identifies. DCPO demonstrates a "fundamental gradient conflict between optimizing for accuracy and minimizing calibration error," which is the training-dynamics version of Paper 08's Δt constraint.
- URL: https://arxiv.org/html/2603.09117

### D. NO DIRECT CONTRADICTION FOUND

No published work was found that directly contradicts Paper 08's core claims. The closest to tension: the Snow et al. (2023) finding that optimistic reporting can initially improve project performance could be read as contradicting the "all debt is bad" interpretation — but Paper 08 already accommodates this via the metastable regime (functional but fragile), so there is no real conflict.

## Notes

1. **The semantic entropy line (Farquhar et al., Nature 2024) is the strongest convergence.** They independently built essentially the same detection mechanism Paper 08 proposes — multi-sample semantic consistency as a hallucination detector. Paper 08 should cite this prominently.

2. **The RLHF-overconfidence link is now well-established.** Leng et al. (2024), Sharma et al. (2023), and the Dunning-Kruger paper (2026) collectively confirm the structural mechanism Paper 08 identifies. The field has converged on this independently from multiple angles.

3. **Gilda & Gilda (Jan 2026) is the most striking convergence** — they propose epistemic layers, conservative confidence aggregation, and evidence decay tracking for software engineering decisions, published ~1 month after Paper 08. The overlap is substantial but arrived at from the AI-assisted engineering angle rather than the Δt framework.

4. **The metastable failure literature (Bronson/Isaacs) provides regime-classification convergence** from distributed systems. Paper 08's three-regime model (coherent/metastable/collapse) is structurally isomorphic to their stable/vulnerable/metastable classification.

5. **What remains novel in Paper 08:**
   - The **unifying framing** connecting LLM hallucination and software project failure as instances of the same temporal debt mechanism. No other work bridges these two domains.
   - The **formal Δt constraint** (dC/dt ≤ k·dE/dt) as a general principle. Individual papers address calibration or overconfidence, but none derive it from a general temporal coherence constraint.
   - The **temporal debt integral** D(t) as a cumulative measure. Others measure point-in-time calibration error; Paper 08 tracks accumulated mismatch over time.
   - The **cross-domain support function** pattern — showing that both domains use variance-based stability measures with temporal decay. This structural parallel is not noted elsewhere.
   - The specific **empirical predictions** (maximum fragility in adjacency region; RLHF increases debt vs. base models; debt predicts deadline slip better than raw velocity) remain untested and unclaimed.

## Verdict

**STRONG CONVERGENCE — as predicted.** The individual domain claims are well-supported by independent work. The LLM hallucination-calibration space has converged heavily on Paper 08's core detection mechanism (semantic consistency). The RLHF-overconfidence link is now mainstream. The software project overconfidence phenomenon is documented but less formalized.

**What survives as novel:** The unifying Δt framework that connects both domains, the formal temporal debt integral, the cross-domain structural parallel, and the specific empirical predictions. The novelty is in the abstraction layer and the bridge, not in the domain-specific observations. This is a defensible position — the paper's value proposition is explicitly "abstract theory translates to concrete instrumentation," and the convergence evidence confirms that the concrete instrumentation works while the abstract unification remains unique.

**Risk level:** Medium. The semantic entropy work (Nature 2024) is high-profile and covers the LLM detection mechanism thoroughly. Paper 08 should acknowledge this convergence explicitly and position the Δt framework as the theoretical explanation for why semantic entropy works as a hallucination detector — it measures evidence bandwidth.
