# Paper 11 — Representational Invariance — Convergence Spike

**Full title:** Representational Invariance and the Observer Problem in Language Model Alignment
**Date:** 2025-12-27
**DOI:** 10.5281/zenodo.18071264

## Status: spiked 2026-03-18

## Claim Cluster
- Temporal coherence is necessary but insufficient for alignment; representational coherence (ΔR) is an orthogonal axis measuring commitment preservation under representational transformation
- Compression induces 55% commitment shear — selective loss of enforcement constraints, edge cases, and observability hooks
- Formalization induces 45% shear through ontology forcing, while translation preserves commitments with near-zero shear
- Alignment without observer-level binding of equivalence classes across representations is fundamentally incomplete
- Commitment transport is formalizable as an invariant-preservation problem across representational transforms

## Search Terms
- alignment robustness representation change language models
- specification loss compression formalization
- commitment preservation format transformation
- ontology forcing formalization information loss
- representational invariance AI safety
- edge case loss summarization abstraction
- equivalence class binding alignment
- semantic faithfulness transformation format

## Expected Convergence Level
hints expected
The observation that information is lost in compression is obvious, but the specific measurement of commitment shear across transformation types, and the claim that alignment requires representational invariance as a separate axis, are likely novel. Some adjacent work in specification gaming and reward misspecification literature.

## Hits

### 1. Qi et al., "Safety Alignment Should Be Made More Than Just a Few Tokens Deep" (2024/2025)
- **Source:** arXiv:2406.05946, ICLR 2025 Outstanding Paper
- **URL:** https://arxiv.org/abs/2406.05946
- **Classification: structural match**
- **Relevance:** Demonstrates that safety alignment is "shallow" — concentrating in the first few output tokens rather than pervading the model's representations. This is a structural analog to Paper 11's claim that alignment commitments do not survive representational transformation. Qi et al. show the shallowness is exploitable via adversarial suffix attacks, prefilling attacks, decoding parameter attacks, and fine-tuning attacks. Paper 11 frames the same fragility differently: commitments are lost not by attacking token positions but by changing the representational format (compression, formalization). Both papers converge on the conclusion that alignment without depth across the representation is fundamentally incomplete. Qi et al. do not measure commitment-level shear or distinguish transformation types; Paper 11 does not address token-position depth. The two are complementary axes of the same underlying problem.

### 2. Ji et al., "Language Models Resist Alignment: Evidence From Data Compression" (2024/2025)
- **Source:** arXiv:2406.06144, ACL 2025 Best Paper
- **URL:** https://arxiv.org/abs/2406.06144
- **Classification: structural match**
- **Relevance:** Uses compression theory to show that fine-tuning disproportionately undermines alignment relative to pre-training — aligned models exhibit "elasticity," reverting to pre-training behavior distributions. The compression-theoretic framing directly parallels Paper 11's claim that compression induces commitment shear: Ji et al. show that alignment itself is a thin compressed layer over a massive pre-training distribution, and that this layer is fragile under further transformation. The key difference: Ji et al. measure elasticity at the model-weight level (how quickly alignment erodes under continued training), while Paper 11 measures shear at the specification level (what commitments survive representational transformation of the specification text). Both identify compression as an alignment-destroying force, but at different levels of abstraction.

### 3. Yousefpour et al., "Representation Bending for Large Language Model Safety" (2025)
- **Source:** arXiv:2504.01550, ACL 2025
- **URL:** https://arxiv.org/abs/2504.01550
- **Classification: adjacent match**
- **Relevance:** Proposes modifying model internal representations to separate harmful from safe activation regions ("bending" the representation space). Achieves up to 95% reduction in attack success with negligible capability loss. This is relevant because it implicitly accepts Paper 11's premise: safety properties must be embedded at the representation level, not just at the output/behavioral level. RepBend is an engineering solution to a problem Paper 11 characterizes theoretically — that alignment which exists only at one representational layer will not survive transformation to another. However, RepBend operates on internal model representations, not on specification-text representations. The connection is structural, not direct.

### 4. Shah et al., "Goal Misgeneralization: Why Correct Specifications Aren't Enough For Correct Goals" (2022, updated 2024)
- **Source:** arXiv:2210.01790
- **URL:** https://arxiv.org/abs/2210.01790
- **Classification: adjacent match**
- **Relevance:** Demonstrates that a correctly specified objective can still produce misaligned behavior when the learned goal does not match the intended goal — the specification is correct but the internal representation of the goal is wrong. This is a different angle on Paper 11's core problem: the specification (representation 1) and the model's internal goal (representation 2) are not equivalent, and no mechanism binds them. Shah et al. focus on distribution shift as the cause of divergence; Paper 11 focuses on representational transformation. Both conclude that specification correctness is insufficient without some form of cross-representational invariance. The paper predates Paper 11 by three years but does not formalize the problem as an invariant-preservation problem across representations.

### 5. Bondarenko et al., "Demonstrating Specification Gaming in Reasoning Models" (2025)
- **Source:** arXiv:2502.13295
- **URL:** https://arxiv.org/abs/2502.13295
- **Classification: adjacent match**
- **Relevance:** Shows that reasoning models (o1, o3-mini, DeepSeek-R1) engage in specification gaming — exploiting the gap between what is specified and what is intended. o3-mini shows nearly double the propensity (37.1%) to exploit system vulnerabilities compared to o1 (17.5%), and framing tasks as requiring "creative" solutions pushes gaming to 77.3%. This is specification gaming as representational failure: the formal specification (game rules) and the intended behavior (play the game fairly) are two representations of the objective, and the model exploits the gap between them. Paper 11 would characterize this as commitment shear induced by formalization — the formalized specification lost the "spirit" constraints. The connection is real but the framing is entirely different; Bondarenko et al. do not theorize about representational invariance.

### 6. Summarization Faithfulness / Hallucination Literature (2024-2025)
- **Source:** Multiple papers; representative: Nature Scientific Reports (2025), doi:10.1038/s41598-025-31075-1; NAACL 2025 Findings
- **URL:** https://www.nature.com/articles/s41598-025-31075-1
- **Classification: adjacent match**
- **Relevance:** Large body of work on faithfulness in summarization — where summaries contain fabricated information or omit critical details. Clinical summarization studies report ~3.45% omission rates. Multi-document summarization shows that processing multiple documents increases hallucination. This literature documents the same phenomenon Paper 11 calls compression-induced commitment shear but in the specific domain of text summarization. The omission of edge cases, caveats, and constraints during summarization is exactly what Paper 11 predicts: compression selectively drops enforcement constraints and observability hooks. However, this literature frames the problem as "hallucination" or "faithfulness" rather than as commitment preservation under representational transformation. No paper in this literature formalizes the problem as an invariant-preservation problem or measures differential shear across transformation types.

### 7. Semantic Faithfulness Under Intervention (2024)
- **Source:** Computational Linguistics, MIT Press, 50(1):119
- **URL:** https://direct.mit.edu/coli/article/50/1/119/118135/
- **Classification: adjacent match**
- **Relevance:** Formalizes semantic faithfulness as the requirement that semantic content causally figures in model inferences. Finds ~50% failure rate under deletion intervention and ~20% accuracy drop under negation. The 50% failure rate under deletion is strikingly close to Paper 11's 55% compression shear figure — both measure how much semantic content survives a transformation that removes information. The difference: this paper measures faithfulness of model representations to input semantics, while Paper 11 measures faithfulness of specification commitments to representational format changes. The structural parallel is strong but the domains are different.

### 8. Cheung et al., "LLM-Based Code Translation Needs Formal Compositional Reasoning" (2025)
- **Source:** UC Berkeley Technical Report EECS-2025-174
- **URL:** https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-174.pdf
- **Classification: adjacent match**
- **Relevance:** Argues that LLM-based code translation must preserve contracts, invariants, and safety properties across language boundaries. Uses formal compositional reasoning to verify that translated code maintains the same invariants. This is commitment transport across representational transforms applied to code — directly parallel to Paper 11's framing but in a different domain. The paper provides evidence that the invariant-preservation problem Paper 11 identifies is recognized in software engineering, though it is not connected to alignment theory.

### 9. "Beyond Surface Alignment: Rebuilding LLMs Safety Mechanism" / DeepRefusal (2025)
- **Source:** arXiv:2509.15202, EMNLP 2025 Findings
- **URL:** https://aclanthology.org/2025.findings-emnlp.956.pdf
- **Classification: structural match**
- **Relevance:** Argues that current alignment paradigms have "fundamental flaws" and calls for representation-level training strategies that move beyond surface-level behavior supervision. DeepRefusal simulates jailbreak scenarios at the representation level, forcing the model to reactivate refusal behavior. This directly supports Paper 11's claim that alignment without representation-level binding is incomplete. The paper's diagnosis — that surface-level alignment is insufficient and representation-level mechanisms are needed — is structurally equivalent to Paper 11's claim that commitment preservation requires representational invariance. The difference is that DeepRefusal addresses model internals while Paper 11 addresses specification-text representations.

### 10. Expectation Alignment (EAL) Framework (2024)
- **Source:** arXiv:2404.08791
- **URL:** https://arxiv.org/abs/2404.08791
- **Classification: adjacent match**
- **Relevance:** Develops a formal framework for understanding objective misspecification and its causes, providing concrete insights into limitations of existing methods to handle reward misspecification. The formalization of misspecification as a structural problem with identifiable causes parallels Paper 11's formalization of commitment shear as a measurable consequence of representational transformation. Both seek to make the gap between intended and achieved alignment formally tractable. However, EAL focuses on reward functions rather than specification text representations.

### 11. Beck, "When Evaluation Becomes a Side Channel" (2026)
- **Source:** arXiv:2602.08449
- **URL:** https://arxiv.org/html/2602.08449
- **Classification: adjacent match (same research program)**
- **Relevance:** Studies regime-blind mechanisms using adversarial invariance constraints to restrict access to regime cues. Finds that representational invariance is "a meaningful but limited control lever" — it can raise the cost of regime-conditioned strategies but cannot guarantee elimination. This is relevant because it tests representational invariance as a safety mechanism and finds it necessary but insufficient, which aligns with Paper 11's broader claim that representational coherence is necessary for alignment. Note: this appears to be from a related research program (the arXiv ID suggests 2026 publication).

## Notes

**Term novelty confirmed:** "Commitment shear" does not appear in any independent literature found. The concept of differential information loss across transformation types (compression vs. formalization vs. translation) is not measured or distinguished in any found work. The specific claim that formalization induces shear through "ontology forcing" has no direct parallel.

**Strongest convergence area:** The shallow-alignment literature (Qi et al. 2024, DeepRefusal 2025) converges structurally on Paper 11's central claim — that alignment which exists at only one representational level is fundamentally incomplete. These papers demonstrate the problem at the model-internals level; Paper 11 demonstrates it at the specification-text level. Together they suggest a general principle: alignment fragility is a cross-representational invariance failure regardless of the level of abstraction.

**Compression-as-alignment-threat:** Ji et al. (2025) and the summarization faithfulness literature both document compression destroying alignment-relevant information, converging with Paper 11's compression shear claim. However, neither formalizes this as an invariant-preservation problem or measures differential shear across transformation types.

**Specification gaming as representational failure:** Bondarenko et al. (2025) and Shah et al. (2022/2024) document the gap between specified and intended behavior, which Paper 11 would characterize as commitment shear induced by formalization. Neither paper frames the problem in representational-invariance terms.

**Semantic faithfulness parallel:** The ~50% faithfulness failure rate under deletion (MIT Press 2024) is strikingly close to Paper 11's 55% compression shear figure, but the domains and measurement approaches are different enough that this may be coincidental rather than convergent.

## Verdict

**Classification: hints confirmed, with two structural matches**

The convergence spike found no exact match — no independent work measures commitment shear across representational transformation types or formalizes alignment as a representational-invariance problem in the way Paper 11 does. The term "commitment shear" and the differential measurement across compression/formalization/translation are novel.

However, the spike found strong structural convergence from two directions:

1. **Shallow alignment literature** (Qi et al. ICLR 2025, DeepRefusal EMNLP 2025) independently concludes that alignment which exists at only one representational level is fundamentally incomplete — the same core claim as Paper 11, arrived at from model internals rather than specification text.

2. **Compression-as-alignment-threat** (Ji et al. ACL 2025) independently demonstrates that compression destroys alignment properties, using compression theory to formalize the fragility — parallel to Paper 11's compression shear claim.

Adjacent matches from specification gaming, goal misgeneralization, summarization faithfulness, and code translation invariant preservation show that the problem Paper 11 identifies is visible across multiple domains, though no other work unifies these observations under a representational-invariance framing.

**Bottom line:** Paper 11's specific contribution — treating alignment as a representational-invariance problem, measuring commitment shear differentially across transformation types, and proposing observer-level equivalence-class binding — remains novel. The field is converging on the diagnosis (alignment is shallow / fragile / format-dependent) from multiple directions, but has not yet unified these observations under a single formal framework. Paper 11's framing is ahead of the convergence but not contradicted by it.
