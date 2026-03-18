# Paper 03 — Scalar Reward Collapse — Convergence Spike

**Full title:** Scalar Reward Collapse: A General Theory of Eigenstructure Evaporation in Closed-Loop Systems
**Date:** 2025-12-02
**DOI:** 10.5281/zenodo.17791872

## Status: spiked

## Claim Cluster
- Multiplicative reweighting under scalar reward causes all non-reward-maximal modes to decay exponentially (Eigenstructure Evaporation)
- Closed-loop scalar optimization converges to fixed points concentrated on reward-maximal states with reduced entropy
- Once collapse occurs, the same optimization operator cannot restore suppressed modes without exogenous forcing or structural modification (irreversibility)
- Scalar optimization forces multi-timescale systems into single-mode temporal collapse
- This mechanism unifies platform content homogenization, AI mode collapse, market herding, and institutional monoculture

## Search Terms
- mode collapse reinforcement learning scalar reward
- multiplicative weights convergence fixed point
- Goodhart's Law formal model dynamical systems
- RLHF mode collapse eigenstructure
- reward hacking optimization monoculture
- scalar objective function diversity loss
- closed-loop optimization entropy reduction
- winner-take-all dynamics replicator equation

## Expected Convergence Level
strong convergence likely

## Hits

### Exact Matches

**GX-Chen et al., "KL-Regularized Reinforcement Learning is Designed to Mode Collapse" (2025)**
arXiv:2510.20817. Proves mathematically that standard KL-regularized RL settings specify unimodal target distributions — "by construction, non-diverse." Same conclusion as eigenstructure evaporation, different notation.
- Claims: 1, 2
- Match: very close — different formalism (KL families vs eigenstructure) but identical core conclusion

**GX-Chen et al., "Expected Return Causes Outcome-Level Mode Collapse in Reinforcement Learning" (2026)**
arXiv:2601.21669. Shows under idealized learning dynamics, log-probability ratio between any two outcomes evolves linearly in their reward difference, implying exponential ratio divergence and inevitable collapse independent of exploration, entropy regularization, or algorithm choice. Identifies probability multiplier as source of pathology.
- Claims: 1, 3
- Match: **extremely close** — exponential ratio divergence is mathematically equivalent to exponential decay of non-maximal modes. Strongest independent convergence found.

**Shumailov et al., "AI models collapse when trained on recursively generated data" (Nature, July 2024)**
doi:10.1038/s41586-024-07566-y. Demonstrates iterative self-consumption causes irreversible tail loss. Uses "irreversible" explicitly.
- Claims: 2, 3
- Match: strong on irreversibility and convergence to reduced-entropy fixed points. Different mechanism (iterative retraining vs closed-loop optimization) but structurally identical math — tail loss under iterated lossy operator.

### Structural Matches

**Xie et al., "On the Algorithmic Bias of Aligning LLMs with RLHF: Preference Collapse and Matching Regularization" (2024)**
arXiv:2405.16455; JASA Vol 120 No 552, 2025. KL-based regularization passes bias from reference model, causing "preference collapse" where minority preferences virtually disregarded. Proposes PM-RLHF fix.
- Claims: 1, 2
- Match: identifies same collapse dynamic but attributes to reference model bias channel rather than scalar reward structure per se. Complementary framing.

**Song et al., "Reward Collapse in Aligning Large Language Models" (2023/2025)**
arXiv:2305.17608; Journal of Data Science, Oct 2025. Ranking-based reward training converges to identical reward distributions across diverse prompts. Ranking objective fails to incorporate prompt-related information.
- Claims: 1, 2
- Match: different level of analysis (reward model training vs policy optimization) but structurally analogous — scalar ranking squashes multi-modal reward into single mode.

**Kirk et al., "Understanding the Effects of RLHF on LLM Generalisation and Diversity" (ICLR 2024)**
arXiv:2310.06452. Empirically demonstrates RLHF significantly reduces output diversity vs SFT across syntactic, semantic, and logical measures.
- Claims: 1, 2
- Match: strong empirical validation without the formal eigenstructure framework. Observes the phenomenon Paper 03 claims to explain.

**Karimi et al., "Goodhart's Law in Reinforcement Learning" (ICLR 2024)**
arXiv:2310.09144. Geometric explanation: policy optimization is linear maximization in convex polytope. Goodharting when angle between true and proxy reward exceeds critical threshold.
- Claims: 1, 2
- Match: complementary geometric framing — both identify convergence-to-boundary phenomenon.

**Replicator Dynamics (classical literature + ongoing 2024 work)**
Sorin, "Replicator Dynamics: Old and New" (2020); Bielawski et al., arXiv:2402.09824 (2024). Replicator equation is continuous-time limit of multiplicative weights. Non-optimal strategies exhibit exponential decay in population share.
- Claims: 1
- Match: the mathematical mechanism is **identical**. Paper 03's contribution is applying this known dynamic to AI/platform/institutional context and naming the cross-domain pattern.

**Maier et al., "Take Goodhart Seriously: Principled Limit on General-Purpose AI Optimization" (2025/2026)**
arXiv:2510.02840. Argues approximation/estimation/optimization errors guarantee systematic deviations; Goodhart breaking point cannot be located in advance.
- Claims: 2, 3, 5
- Match: error-theoretic rather than eigenstructure perspective but same conclusion — unchecked scalar optimization produces irreversible collapse. Supports unification claim.

**Karwowski et al., "Catastrophic Goodhart" (NeurIPS 2024)**
arXiv:2407.14503. Proves with heavy-tailed reward misspecification, KL regularization fails completely: policies exist with infinite proxy reward but vanishing KL from base model. Standard tools provably cannot prevent or reverse collapse.
- Claims: 1, 2, 3
- Match: the "catastrophic" regime is precisely where Paper 03's irreversibility claim holds.

### Adjacent Matches

**Yun et al., "The Price of Format: Diversity Collapse in LLMs" (EMNLP 2025 Findings)**
arXiv:2505.18949. Formatting templates (not reward optimization) induce diversity collapse persistent even at high temperature.
- Claims: 2 (partial)
- Different mechanism, same phenomenology — suggests the problem is overdetermined.

**"Failure Modes of Maximum Entropy RLHF" (2025)**
arXiv:2509.20265. Entropy regularization fails to prevent reward hacking; effective KL budgets model-dependent with no principled way to set them.
- Claims: 1, 2
- Documents entropy-based defenses failing in practice, consistent with irreversibility claim.

**Gao et al., "Scaling Laws for Reward Model Overoptimization" (ICML 2023)**
arXiv:2210.10760. Empirical scaling relationship between proxy reward optimization and gold reward degradation.
- Claims: 1, 2
- Empirical characterization without the mechanistic eigenstructure explanation.

**Bommasani et al., "Picking on the Same Person: Does Algorithmic Monoculture lead to Outcome Homogenization?" (NeurIPS 2022)**
arXiv:2211.13972. Formalizes "outcome homogenization" from shared components.
- Claims: 5 (partial)
- Different mechanism (component sharing vs scalar optimization convergence).

**Manheim & Garrabrant, "Categorizing Variants of Goodhart's Law" (2018)**
arXiv:1803.04585. Taxonomy of four Goodhart failure modes (regressional, extremal, causal, adversarial).
- Claims: 1, 5
- Prior art on formalizing Goodhart. Eigenstructure framing could be positioned as unifying mechanism generating all four modes.

**Majka & El-Mhamdi, "The Strong, Weak and Benign Goodhart's Law" (2025)**
arXiv:2505.23445. Formal proof Goodhart's effect depends on tail distribution of goal/proxy discrepancy.
- Claims: 1, 2
- Tail-distribution dependence could support or constrain universality claims.

**DiMaggio & Powell, "The Iron Cage Revisited" (1983)**
American Sociological Review 48, 147-160. Classic institutional isomorphism theory — organizations converge via coercive, mimetic, normative pressures.
- Claims: 5 (institutional monoculture arm)
- Same convergence phenomenology, different mechanism.

**Bikhchandani & Sharma, "Herd Behavior in Financial Markets" (IMF Staff Papers, 2000)**
Informational cascades and herding suppress diverse private signals.
- Claims: 5 (market herding arm)
- Different mechanism (information cascades vs multiplicative reweighting), same macroscopic effect.

### Potential Contradictions / Caveats

**Schaeffer et al., "Is Model Collapse Inevitable?" (2024)**
Shows accumulating synthetic data alongside original real data keeps models stable. Suggests collapse is avoidable with proper data management.
- Challenge to claim: 3 (irreversibility)
- **Moderate.** Consistent with Paper 03's own caveat — adding real data is exactly the "exogenous forcing or structural modification" the paper says is required.

**"RLHF does not appear to differentially cause mode-collapse" (LessWrong post)**
Argues mode collapse attributable to RLHF specifically vs SFT may be overstated.
- Challenge to claims: 1, 2
- **Weak.** Blog post, not peer-reviewed. Kirk et al. (ICLR 2024) provides stronger contrary evidence.

## Notes
- Core mathematical mechanism (multiplicative reweighting → exponential decay) is well-established via replicator dynamics since 1970s-80s
- ML community independently rediscovered same math in RLHF context in 2024-2026
- The one "contradiction" (Schaeffer) actually confirms the paper's own caveat about needing exogenous forcing
- Multi-timescale temporal collapse (claim 4) is NOT addressed by any found work — still novel
- Cross-domain unification (claim 5) is NOT attempted by any single paper — still novel
- Eigenstructure evaporation as specific framing/terminology — still novel

## Verdict
**Strong convergence.** The paper was early, not alone. Core math independently rediscovered. What remains novel: the eigenstructure evaporation terminology, the cross-domain unification (AI/platforms/markets/institutions), and the multi-timescale temporal collapse claim. The paper should cite GX-Chen (2025, 2026), Karwowski (NeurIPS 2024), Karimi (ICLR 2024), and the replicator dynamics literature as the strongest convergences.
