# Paper 10 — Invariant Requirements for Temporal Coherence — Convergence Spike

**Full title:** You Need More Than Just Attention: Invariant Requirements for Temporal Coherence in AI Systems
**Date:** 2025-12-23
**DOI:** 10.5281/zenodo.18039926

## Status: spiked 2026-03-18

## Claim Cluster
- Four invariants are necessary for coherent inference: temporal coherence (past constrains present), semantic conservation (meaning stable under transformation), epistemic grounding (sources constrain claims), and irreversibility (errors leave learning residue)
- Transformer architectures lack the necessary primitives (persistent endogenous state, endogenous state evolution operators, temporal coupling controls) to satisfy these invariants
- These violations persist across all tested transformer-based systems regardless of scale, indicating architectural rather than training limitations
- Invariant requirements serve as diagnostic infrastructure for evaluating whether any system can maintain coherence
- Fundamental architectural changes, not scaling or fine-tuning, are required to satisfy these invariants

## Search Terms
- transformer limitations temporal reasoning architectural
- LLM consistency invariant preservation
- attention mechanism insufficient state persistence
- language model semantic drift contradiction
- architectural constraints hallucination grounding
- persistent state language model architecture
- epistemic grounding invariant AI evaluation
- transformer fundamental limitations beyond scaling

## Expected Convergence Level
partial convergence likely
Transformer limitations are widely discussed, but usually empirically rather than from an invariant-theoretic perspective. The four specific invariants and the claim that they require architectural changes are more specific. Some overlap with mechanistic interpretability work and state-space model motivations.

## Hits

### 1. On Limitations of the Transformer Architecture
**Source:** Merrill & Sabharwal, arXiv:2402.08164, February 2024
**URL:** https://arxiv.org/abs/2402.08164
**Classification:** structural match

Proves that transformers can only perform constant-depth sequential computation, with fundamental incompatibility for certain problem classes. Shows that compositional, sequential, and hierarchical reasoning tasks hit architectural walls, not training walls. The paper argues these limitations "should not be expected to be solvable in practice ad infinitum" — directly supporting Paper 10's claim that scaling cannot resolve the deficits. However, the framing is computational complexity (circuit depth), not invariant-theoretic. The paper does not identify temporal coherence, semantic conservation, epistemic grounding, or irreversibility as specific invariants, but reaches structurally similar conclusions about architectural insufficiency.

---

### 2. The End of Transformers? On Challenging Attention and the Rise of Sub-Quadratic Architectures
**Source:** Survey paper, arXiv:2510.05364, October 2025
**URL:** https://arxiv.org/abs/2510.05364
**Classification:** adjacent match

Comprehensive survey documenting the growing consensus that transformers have fundamental limitations motivating architectural alternatives. Identifies compositionality failures, quadratic complexity, and lack of recursion support as key deficits. The paper catalogues alternatives (SSMs, linear attention, hybrid architectures) motivated by precisely the kind of architectural insufficiency Paper 10 diagnoses. However, the motivation is computational efficiency and expressiveness rather than invariant satisfaction. No invariant framework is proposed.

---

### 3. Consistency in Language Models: Current Landscape, Challenges, and Future Directions
**Source:** arXiv:2505.00268, May 2025
**URL:** https://arxiv.org/abs/2505.00268
**Classification:** structural match (partial)

Defines semantic consistency as the ability of a model to produce equivalent answers under meaning-preserving input transformations, formalized as f(X) = f(Y) when X and Y are semantically equivalent. This directly parallels Paper 10's semantic conservation invariant. Finds that state-of-the-art models show 15-30% performance drops on semantically rephrased questions, empirically confirming the invariant violation. However, the framework treats consistency as a single desideratum rather than decomposing it into the four distinct invariants Paper 10 identifies. No architectural diagnosis is offered — the failures are documented but not traced to missing primitives.

---

### 4. Hallucination is Inevitable: An Innate Limitation of Large Language Models
**Source:** Xu et al., arXiv:2401.11817, January 2024 (updated February 2025)
**URL:** https://arxiv.org/abs/2401.11817
**Classification:** structural match

Proves via computability theory that LLMs cannot learn all computable functions and will inevitably hallucinate when used as general problem solvers. This supports Paper 10's claim that the failures are architectural/mathematical rather than training-related, and that no amount of scaling resolves them. The diagonal argument establishes a formal impossibility result. However, this is a computability-theoretic proof, not an invariant-based diagnostic framework. It proves something is impossible but does not identify which specific invariants are violated or what architectural primitives are missing.

---

### 5. On the Fundamental Impossibility of Hallucination Control in Large Language Models
**Source:** Karpowicz, arXiv:2506.06382, June 2025
**URL:** https://arxiv.org/abs/2506.06382
**Classification:** structural match

Proves that no LLM inference mechanism can simultaneously achieve truthful response generation, semantic information conservation, relevant knowledge revelation, and knowledge-constrained optimality. This is remarkably close to Paper 10's invariant decomposition — the four properties in the impossibility proof map loosely onto temporal coherence, semantic conservation, epistemic grounding, and irreversibility. The proof spans three mathematical frameworks (auction theory, proper scoring theory, log-sum-exp analysis for transformers). The key difference: Karpowicz frames these as an impossibility result about inference mechanisms, while Paper 10 frames them as diagnostic invariants pointing toward architectural redesign. The convergence on a four-property decomposition is striking.

---

### 6. A Categorical Analysis of Large Language Models
**Source:** arXiv:2512.09117, December 2025
**URL:** https://arxiv.org/abs/2512.09117
**Classification:** adjacent match

Uses category theory (specifically the category of relations, Rel) to formally analyze how LLMs learn and generate outputs. Connects to work showing hallucinations are intrinsic structural failures rather than bugs. Mahadevan (2025) models semantic paraphrases as weak equivalences in an "LLM Markov category," providing formal machinery for something like semantic conservation. This is a more abstract formal framework than Paper 10's invariant approach, but arrives at compatible conclusions: the failures are structural, not incidental, and require formal analysis to understand.

---

### 7. Is the Reversal Curse a Binding Problem? Uncovering Limitations of Transformers from a Basic Generalization Failure
**Source:** Wang et al., arXiv:2504.01928, April 2025 (updated February 2026)
**URL:** https://arxiv.org/abs/2504.01928
**Classification:** structural match (partial)

Demonstrates that transformers cannot form reversible factual associations — a phenomenon traced to the binding problem from cognitive science. The two causes identified (inconsistency and entanglement of concept representations) map onto Paper 10's irreversibility invariant: errors and learned associations do not compose reversibly, and the architecture lacks the state machinery to maintain bidirectional bindings. The proposed solution (JEPA-based architecture with special memory layers supporting disentangled representations) is precisely the kind of "fundamental architectural change" Paper 10 calls for.

---

### 8. A Mechanistic Analysis of Transformers for Dynamical Systems
**Source:** arXiv:2512.21113, December 2025
**URL:** https://arxiv.org/abs/2512.21113
**Classification:** structural match

Interprets causal self-attention as a linear, history-dependent recurrence and analyzes how it processes temporal information. Shows that the convexity constraint imposed by softmax attention fundamentally restricts the class of dynamics that can be represented, leading to oversmoothing in oscillatory settings. Under partial observability, attention acts as an adaptive delay-embedding mechanism rather than maintaining true endogenous state evolution. This directly supports Paper 10's claim that transformers lack endogenous state evolution operators — the paper shows mechanistically why: softmax convexity constraints prevent the architecture from representing the required dynamical systems.

---

### 9. Titans: Learning to Memorize at Test Time
**Source:** Behrouz & Zhong (Google Research), arXiv:2501.00663, January 2025
**URL:** https://arxiv.org/abs/2501.00663
**Classification:** adjacent match (design response)

Introduces a neural long-term memory module that learns to memorize at test time via gradient descent during inference. The architecture explicitly separates short-term memory (attention) from long-term persistent memory (neural memory module), directly addressing the "persistent endogenous state" primitive Paper 10 identifies as missing. Titans outperform transformers and SSMs on tasks requiring long-context reasoning. Published at ICML 2025. This is not a convergence on the diagnostic framework but rather an independent architectural response to the same deficits Paper 10 diagnoses — the Titans team built persistent state because they empirically found it was needed, validating Paper 10's claim that the primitive is necessary.

---

### 10. Mamba: Linear-Time Sequence Modeling with Selective State Spaces
**Source:** Gu & Dao, arXiv:2312.00752, December 2023 (Mamba-2 in 2024)
**URL:** https://arxiv.org/abs/2312.00752
**Classification:** adjacent match (design response)

Mamba and its successor Mamba-2 introduce selective state space models that maintain persistent hidden state evolving over time — directly providing the "endogenous state evolution operators" Paper 10 identifies as missing from transformers. The selective mechanism allows input-dependent state transitions, providing a form of temporal coupling. The Mamba-360 survey (2025) confirms competitive performance with transformers across domains. Like Titans, this validates Paper 10's architectural diagnosis by building what Paper 10 says is needed, though the Mamba team's motivation was efficiency rather than invariant satisfaction.

---

### 11. Beyond Scaling Laws: Towards Scientific Reasoning-Driven LLM Architectures
**Source:** Preprints.org, 202504.2088, April 2025
**URL:** https://www.preprints.org/manuscript/202504.2088
**Classification:** structural match

Argues that "the transformer architecture was optimized for linguistic coherence, not epistemic validity" and that "scaling alone will not be sufficient" because limitations stem from "architectural misalignment with the epistemic demands." Calls for structure-augmented architectures integrating graph neural networks and modular multi-agent systems. This directly parallels Paper 10's core thesis: the deficits are architectural, not parametric, and require fundamental redesign. The framing is different (scientific reasoning vs. temporal coherence invariants) but the conclusion is the same.

---

### 12. RNNs Are Not Transformers (Yet): The Key Bottleneck on In-Context Retrieval
**Source:** ICLR 2025 Conference Paper
**URL:** https://arxiv.org/abs/2402.18510
**Classification:** adjacent match

Proves that even with chain-of-thought, RNNs cannot close the representation gap with transformers due to the "curse of memory efficiency" — RNNs use too little memory to store full context. This provides a nuanced counterpoint to Paper 10: while transformers lack persistent state (Paper 10's diagnosis), recurrent alternatives lack sufficient context retrieval. The paper shows that adding a single transformer layer to RNNs closes the gap, suggesting hybrid architectures may be needed — architectures that provide both persistent state evolution AND broad context access.

---

### 13. In Transformer We Trust? A Perspective on Transformer Architecture Failure Modes
**Source:** Mondal & Jagtap, arXiv:2602.14318, February 2026
**URL:** https://arxiv.org/abs/2602.14318
**Classification:** adjacent match

Systematic examination of transformer trustworthiness through interpretability, robustness, fairness, and privacy. Identifies rank collapse and entropy collapse as critical failure modes. While the failure mode taxonomy differs from Paper 10's invariant framework, the paper reaches a compatible conclusion: transformers have systematic architectural failure modes that require understanding beyond empirical performance metrics. The focus on high-stakes deployment contexts aligns with Paper 10's claim that invariant satisfaction is necessary for reliable operation.

---

### 14. Who's Manipulating Whom? Epistemic Grounding to Break Recursive Validation Loops in Large Language Models
**Source:** OpenReview, 2025
**URL:** https://openreview.net/forum?id=z6uPONc8h1
**Classification:** structural match (partial)

Proposes "epistemic grounding" as a framework to break recursive feedback loops in LLMs, using model tiering, verification protocols, and training objective modifications. This directly uses Paper 10's term "epistemic grounding" and addresses the same concern: LLM outputs are not constrained by their sources. However, the approach is a training/deployment intervention rather than an architectural diagnosis. The paper treats epistemic grounding as something to be bolted on, while Paper 10 argues it must be an architectural primitive.

---

### 15. On the Fundamental Limits of LLMs at Scale
**Source:** arXiv:2511.12869, November 2025
**URL:** https://arxiv.org/abs/2511.12869
**Classification:** structural match

Proves via multiple mathematical frameworks that hallucination is inevitable, uncomputability yields infinite failure sets, and finite information capacity forces distortion on complex facts. Concludes that "no computable LLM can be universally correct over open-ended queries." This is a scaling-independent impossibility result that supports Paper 10's claim that the failures are not resolved by scaling. The mathematical machinery differs (information theory and computability vs. invariant analysis) but the conclusion converges.

## Notes

**Pattern observed:** The literature splits into three streams that collectively validate Paper 10's framework from different angles:

1. **Impossibility theorists** (Hits 4, 5, 15) prove formally that certain failures are inherent, using computability theory, information theory, and auction theory. They confirm Paper 10's "not a scaling problem" claim but do not provide the diagnostic decomposition into specific invariants.

2. **Architecture builders** (Hits 9, 10, 12) independently build the missing primitives Paper 10 identifies — persistent state (Titans), state evolution operators (Mamba), hybrid retrieval+recurrence (RNN+Transformer). They validate the diagnosis by constructing what Paper 10 says is needed, though their motivation is typically efficiency rather than invariant satisfaction.

3. **Empirical diagnosticians** (Hits 3, 7, 8, 13) document specific failure modes that map onto Paper 10's invariants — semantic inconsistency, reversal curse (irreversibility), softmax convexity constraints (temporal coherence), rank/entropy collapse. They confirm the symptoms but rarely connect them to a unified invariant framework.

**Closest convergence:** Hit 5 (Karpowicz, 2025) is the strongest independent convergence. The four-property impossibility decomposition (truthful generation, semantic information conservation, relevant knowledge revelation, knowledge-constrained optimality) maps remarkably closely onto Paper 10's four invariants (temporal coherence, semantic conservation, epistemic grounding, irreversibility). Both papers independently arrive at a four-fold decomposition of what coherent inference requires, though from different mathematical traditions.

**Counterpoint worth noting:** arXiv:2502.12187 (February 2025) argues that the computability-theoretic impossibility results do not explain practical LLM issues and that hallucination probability can be reduced arbitrarily close to zero with sufficient data quality and quantity. This challenges Paper 10's strongest claim (that architectural changes are *required*) by suggesting that practical improvements through training may be sufficient even if theoretical perfection is impossible.

## Verdict

**Overall convergence level: moderate-to-strong**

Paper 10's individual claims are well-supported by independent work:

- **"Transformers have fundamental architectural limitations" (not just scaling):** Strong convergence. Multiple independent impossibility proofs (Hits 4, 5, 15), computational complexity results (Hit 1), and mechanistic analyses (Hit 8) confirm this from different angles. This is approaching consensus in the field by late 2025.

- **"Persistent state, state evolution, and temporal coupling are missing primitives":** Strong convergence via design response. Titans (Hit 9) and Mamba (Hit 10) independently build exactly these primitives, validating the diagnosis empirically. The mechanistic analysis of softmax convexity constraints (Hit 8) explains why transformers cannot provide state evolution.

- **"Scaling and fine-tuning cannot resolve these deficits":** Moderate convergence. The impossibility results support this, but the counterargument (arXiv:2502.12187) that practical hallucination can be made negligible complicates the picture. The field has not fully settled this debate.

- **"Four specific invariants as diagnostic infrastructure":** This remains largely novel. While Karpowicz (Hit 5) independently arrives at a strikingly similar four-fold decomposition, and individual invariants find echoes in the literature (semantic consistency in Hit 3, epistemic grounding in Hit 14, irreversibility/binding in Hit 7), no other work assembles these four invariants into a unified diagnostic framework for evaluating architectural sufficiency. The invariant-theoretic framing — treating these as necessary conditions any architecture must satisfy — is Paper 10's distinctive contribution.

**What remains novel:**
1. The specific four-invariant decomposition as a unified diagnostic framework
2. The mapping from invariant violations to missing architectural primitives (persistent endogenous state, state evolution operators, temporal coupling controls)
3. The use of invariants as design requirements for next-generation architectures rather than just impossibility proofs or empirical observations
4. The claim that these invariants are individually necessary and collectively sufficient for temporal coherence — no other work makes this sufficiency claim

**What has been independently confirmed:**
1. Transformers have fundamental architectural limitations beyond scaling
2. Persistent state and state evolution are needed (validated by Titans, Mamba)
3. Semantic consistency fails under transformation (15-30% drops documented)
4. Hallucination has formal impossibility results, not just empirical frequency
5. The reversal curse demonstrates irreversibility-type failures tied to architecture
