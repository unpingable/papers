# Paper 06 — Temporal Closure Requirements — Convergence Spike

**Full title:** Temporal Closure Requirements for Synthetic Coherence: Architectural Foundations and the Simulator Gap
**Date:** 2025-12-07
**DOI:** 10.5281/zenodo.17849277

## Status: untouched

## Claim Cluster
- Three architectural operators (timescale separation, endogenous state, adaptive control) are jointly necessary and sufficient for maintaining coherent identity across perturbations
- The Simulator Gap: LLMs can simulate temporal reasoning without implementing temporal closure, and this distinction is architecturally identifiable
- Temporal closure is a testable architectural property, not a philosophical claim about consciousness or understanding
- Biological and artificial systems can be evaluated against the same temporal closure criteria with falsifiable predictions

## Search Terms
- temporal reasoning language models simulation vs implementation
- architectural requirements coherent identity AI
- endogenous state persistent memory language models
- consciousness necessary conditions computational architecture
- simulator gap artificial intelligence temporal
- timescale separation adaptive control autonomy
- synthetic coherence architectural invariants
- LLM limitations temporal reasoning state persistence

## Expected Convergence Level
partial convergence likely
The claim that LLMs lack genuine temporal reasoning is increasingly discussed. The specific three-operator framework and "Simulator Gap" terminology are likely original, but the observation that LLMs simulate rather than implement temporal processes has been made independently by several researchers.

## Hits

### STRUCTURAL MATCH (same problem, convergent architecture, different formalism)

**1. Huang et al., "On the Failure of Latent State Persistence in Large Language Models" (2025, arXiv 2505.10571)**
- Authors: Jen-tse Huang, Kaiser Sun, Wenxuan Wang, Mark Dredze
- Venue: arXiv, revised Jan 2026
- Match type: **structural**
- Claims supported: Simulator Gap (Claim 2), statelessness as architectural rather than parametric (Claim 3)
- Closeness: HIGH. Formalizes "Latent State Persistence (LSP) gap" — LLMs cannot internally maintain or manipulate transient information. Chain-of-thought works only by externalizing state into manifest tokens, which they call "an architectural bypass rather than genuine latent persistence." This is essentially Paper 06's system-boundary fallacy (Section 3.1.1) arrived at empirically. They do NOT frame it in terms of dynamical systems, timescale separation, or coherence operators — they demonstrate the same limitation via behavioral experiments (number guessing, yes-no games, mathematical mentalism).

**2. Archer, "The End of Bicameral AI: Scale Solved Capability, Not Continuity" / Continuity-Regulated Intelligence (CRI) (2025, blog/framework)**
- Author: Darin Archer
- Venue: darinarcher.com
- Match type: **structural**
- Claims supported: All four claims — three-operator necessity, simulator gap, architectural (not philosophical) framing, cross-domain applicability
- Closeness: HIGH. CRI explicitly argues that "scale is an amplifier, not a substitute for architecture" and requires: execution + consolidation + governance in closed control loops preserving identity across time. Calls for "homeostatic regulation, typed memory, and governed promotion as co-equal infrastructure." This is remarkably close to Paper 06's three operators (timescale separation ≈ typed memory/consolidation, endogenous state ≈ execution continuity, adaptive control ≈ governance/homeostatic regulation). Key difference: CRI is framed as engineering prescription, not dynamical-systems proof. No spectral stability formalism, no metastability analysis, no scalar collapse theorem.

**3. Zhang et al., "Comprehension Without Competence: Architectural Limits of LLMs in Symbolic Computation and Reasoning" (2025, TMLR)**
- Authors: Zheng Zhang et al.
- Venue: Transactions on Machine Learning Research, Nov 2025
- Match type: **structural**
- Claims supported: Simulator Gap (Claim 2), architectural type boundary
- Closeness: MEDIUM-HIGH. Identifies "computational split-brain syndrome" — LLMs can articulate correct principles without reliably applying them. Instruction and action pathways are "geometrically and functionally dissociated." This is a different angle on the simulator gap: they show simulation of competence without implementation of competence. Does NOT address temporal persistence, timescale separation, or dynamical systems — focuses on symbolic computation failure modes. But the diagnosis ("pattern completion rather than computation") converges on Paper 06's core claim that simulation ≠ instantiation.

**4. Jennings, "A Computational-Functional Theory of Consciousness" (2025, PhilArchive)**
- Author: B. Jennings
- Venue: PhilArchive (manuscript, revised Nov 2025)
- Match type: **structural**
- Claims supported: Architectural necessity conditions (Claim 1), substrate-independence (Claim 4)
- Closeness: MEDIUM. Proposes five necessary and jointly sufficient conditions for consciousness: complex pattern-matching, densely integrated recursive feedback, self-modification, autonomous initiation, information integration. Consciousness as architectural threshold, not continuum. Substrate-independent. Paper 06 is more specific (three operators vs. five conditions) and explicitly avoids consciousness claims, but the structural logic — necessary architectural conditions, substrate-independence, threshold-based — is convergent. Jennings explicitly predicts that LLMs lacking complete architectural requirements will show partial but not full capacities, which aligns with Paper 06's predictions.

**5. Letta/MemGPT, "Stateful Agents: The Missing Link in LLM Intelligence" (2024-2025)**
- Authors: Letta team (Charles Packer et al.)
- Venue: Blog + open-source framework
- Match type: **structural**
- Claims supported: Simulator Gap (Claim 2), endogenous state requirement (part of Claim 1)
- Closeness: MEDIUM. Explicitly diagnoses LLMs as "trapped in an eternal present moment" — stateless compute units that cannot form new memories or learn from experience. MemGPT/Letta builds persistent memory as architectural addition. But their solution (external memory management via tool calls) is precisely what Paper 06 would classify as the system-boundary fallacy — adding memory scaffolding rather than implementing endogenous state dynamics with F(z_t, u_t). They identify the problem Paper 06 formalizes but propose a solution Paper 06 would reject as insufficient.

### ADJACENT (related problem domain, partial overlap)

**6. Shanahan, "Talking About Large Language Models" + "Role-Play with Large Language Models" (2023-2024, Nature)**
- Author: Murray Shanahan
- Venue: Nature (2023), arXiv update Dec 2024
- Match type: **adjacent**
- Claims supported: Simulator Gap (Claim 2) — conceptual framing
- Closeness: MEDIUM. Frames LLM as "non-deterministic simulator capable of role-playing an infinity of characters." Urges distinguishing simulation from genuine understanding. Paper 06 formalizes what Shanahan observes philosophically: the simulator/agent distinction is not just conceptual but architecturally identifiable via temporal closure operators. Shanahan does not provide architectural criteria or dynamical-systems formalism.

**7. Hancock & Kelso, "Metastability Demystified" (2024, Nature Reviews Neuroscience)**
- Authors: Hancock, Rosas, et al.
- Venue: Nature Reviews Neuroscience, Dec 2024
- Match type: **adjacent**
- Claims supported: Metastability framework (theoretical foundation for Claim 1), cross-domain applicability (Claim 4)
- Closeness: MEDIUM. Comprehensive review of metastability in brain dynamics — the balance between integration and segregation. Clarifies that switching between distinct states is necessary but not sufficient for metastability (need to distinguish from multi-stability). Paper 06 builds on this neuroscience foundation and extends it to synthetic systems as architectural requirement. This paper validates the neuroscience correspondence (Section 5) but does not address AI architecture.

**8. "On the Fundamental Limits of LLMs at Scale" (2025, arXiv 2511.12869)**
- Venue: arXiv, under review at TMLR
- Match type: **adjacent**
- Claims supported: Architectural type boundary (Claim 2), scaling insufficiency
- Closeness: MEDIUM. Proves that LLM failure modes (hallucination, reasoning degradation, context compression, retrieval fragility) are "intrinsic properties of the transformer architecture and the next-token prediction objective," not transient data artifacts. Formalizes via computability theory and information theory. Converges on Paper 06's claim that limitations are architectural not parametric, but from a completely different theoretical direction (computability/information theory vs. dynamical systems/spectral stability).

**9. Active Inference / FEP and Consciousness (Whyte et al. 2024, Laukkonen et al. 2025)**
- Authors: Various (Whyte, Laukkonen, Sandved-Smith)
- Venue: Neuroscience & Biobehavioral Reviews, ScienceDirect
- Match type: **adjacent**
- Claims supported: Temporal hierarchy requirement (part of Claim 1), architectural necessity
- Closeness: MEDIUM-LOW. Active inference framework requires hierarchical generative models with timescale separation — "higher levels encoding more abstract and longer-term predictions." Consciousness arises at interface between continuous perception and discrete policy selection. Paper 06's Operator 1 (temporal separation) is convergent with FEP's hierarchical generative model requirement, but Paper 06 explicitly avoids consciousness claims and focuses on temporal coherence as engineering specification rather than phenomenological theory.

**10. Mamba/SSM Architecture (Gu & Dao, 2023-2024)**
- Authors: Albert Gu, Tri Dao
- Venue: ICLR 2024
- Match type: **adjacent**
- Claims supported: Partial — demonstrates alternative architecture with persistent state
- Closeness: LOW-MEDIUM. State space models maintain a continuous hidden state that evolves recurrently, satisfying Paper 06's Operator 2 (endogenous state) more naturally than transformers. However, Mamba still lacks Operator 3 (adaptive coherence monitoring) and does not implement explicit timescale hierarchy (Operator 1). Interesting as partial architectural step toward temporal closure but not framed in those terms. Paper 06 would classify Mamba as architecturally closer to agent-type than transformers but still incomplete.

**11. "The Temporal Coherence Field Psi_t" (2025, ResearchGate)**
- Venue: ResearchGate preprint
- Match type: **adjacent**
- Claims supported: Coherence monitoring (part of Claim 1)
- Closeness: LOW-MEDIUM. Introduces scalar coherence field for monitoring internal alignment in neural architectures. Can "anticipate performance collapse" before it manifests. This maps loosely to Paper 06's Operator 3 (coherence monitoring via chi metric), but the framework is grounded in field theory rather than dynamical systems and focuses on monitoring existing architectures rather than specifying architectural requirements.

**12. Time-Aware World Model (TAWM) (2025, arXiv 2506.08441)**
- Venue: arXiv
- Match type: **adjacent**
- Claims supported: Timescale separation (Operator 1)
- Closeness: LOW-MEDIUM. Explicitly conditions on time-step size (delta-t) and trains across diverse delta-t values to learn both high- and low-frequency dynamics. Grounded in information-theoretic insight that optimal sampling rate depends on underlying dynamics. This is convergent with Paper 06's Operator 1 but applied to world models for control rather than identity persistence.

**13. RLHF Mode Collapse / Diversity Loss (Turpin et al. 2023, Kirk et al. 2024 ICLR)**
- Venue: ICLR 2024, various
- Match type: **adjacent**
- Claims supported: RLHF scalar collapse (Section 7.3)
- Closeness: MEDIUM. Empirically demonstrates that RLHF reduces output diversity, with tradeoff between generalization and diversity. Paper 06's scalar collapse theorem (imported from Paper 4) provides the formal mechanism — exponential eigenmode evaporation via T-operator — that explains these empirical observations. The empirical work validates the prediction without providing the dynamical-systems explanation.

### CONTRADICTION / TENSION

**14. "Large Language Models Can Learn Temporal Reasoning" (2024, ACL)**
- Venue: ACL 2024
- Match type: **tension (not full contradiction)**
- Claims challenged: Simulator Gap (Claim 2) — partially
- Nature: Shows LLMs can improve temporal reasoning through training. But "temporal reasoning" here means event ordering, timeline construction, temporal NLI — not temporal closure in Paper 06's sense (endogenous state persistence, autonomous dynamics, coherence monitoring). The paper addresses temporal reasoning about content, not temporal coherence of the system itself. Paper 06 would classify these improvements as better simulation of temporal reasoning, not implementation of temporal closure.

**15. "Are Language Models Mere Stochastic Parrots? SkillMix Test Says NO" (Princeton, 2023-2024)**
- Venue: Princeton PLI
- Match type: **tension**
- Claims challenged: Simulation ≠ implementation distinction
- Nature: Argues LLMs demonstrate compositional skill that goes beyond pattern matching. Does not address temporal persistence or architectural type boundaries. The challenge is to the "stochastic parrot" framing, not to Paper 06's specific claims about temporal closure operators.

## Notes

1. **The LSP gap paper (Huang et al.) is the closest independent convergence.** It arrives at essentially the same diagnosis — LLMs cannot maintain internal state, and externalizing state into context is a bypass not a solution — through behavioral experiments rather than dynamical-systems theory. This is strong independent validation of the core simulator gap claim.

2. **CRI (Archer) is the closest convergence on the three-operator architecture.** The execution/consolidation/governance triad maps remarkably well to endogenous state/timescale separation/adaptive control. The key differentiator for Paper 06 is the formal dynamical-systems grounding (spectral stability, metastability barriers, scalar collapse theorem).

3. **No one uses the term "Simulator Gap" or "temporal closure" in Paper 06's specific sense.** Shanahan uses "simulator" language but philosophically, not architecturally. The formal three-operator framework with spectral stability conditions appears to be original.

4. **The scalar collapse analysis of RLHF (Section 7.3) has strong empirical support** from the mode collapse literature but no one else provides the eigenstructure evaporation mechanism. The empirical community observes the phenomenon; Paper 06 provides the dynamical-systems explanation.

5. **Metastability as organizing principle for brain dynamics is well-established** (Hancock & Kelso 2024 in Nature Reviews Neuroscience confirms this). Paper 06's contribution is extending it as an architectural requirement for synthetic systems.

6. **The "fundamental limits" literature converges** on the conclusion that LLM limitations are architectural not parametric, but from information-theoretic and computability-theoretic directions rather than dynamical systems. Multiple independent theoretical frameworks reaching the same conclusion strengthens the claim.

7. **SSM/Mamba architectures partially address Operator 2** (endogenous state) but do not implement Operators 1 or 3. No existing architecture implements all three operators as Paper 06 specifies. This validates the claim that the required architectural transformation is "paradigmatic, not incremental."

8. **No full contradictions found.** The "LLMs can learn temporal reasoning" work addresses a different sense of "temporal" (reasoning about time-stamped events) than Paper 06 (maintaining temporal coherence as a system property). The stochastic-parrot counterarguments challenge the weakest version of the simulation claim but do not address temporal closure specifically.

## Verdict

**PARTIAL CONVERGENCE — as predicted, but stronger than expected on the simulator gap claim.**

**What is independently supported:**
- LLMs lack genuine latent state persistence (Huang et al. 2025 — direct empirical confirmation)
- LLM limitations are architectural, not parametric (multiple independent theoretical frameworks)
- Simulation of competence ≠ implementation of competence (Zhang et al. 2025, Shanahan 2023-2024)
- RLHF causes mode collapse / diversity loss (empirically well-established)
- Metastability and timescale hierarchy are fundamental organizing principles in biological cognition (Hancock & Kelso 2024)
- Architectural thresholds (not continua) determine system capabilities (Jennings 2025)
- Continuity/coherence requires architectural support beyond memory addition (CRI, Letta)

**What remains novel to Paper 06:**
- The specific three-operator framework (temporal separation, endogenous state, adaptive control) as jointly necessary and sufficient
- The "Simulator Gap" as a formal architectural classification with spectral stability criteria
- The scalar collapse theorem as explanatory mechanism for RLHF mode collapse (dynamical-systems formalization of empirical observations)
- Unification of RLHF collapse and platform recommendation collapse as instances of same T-operator
- Metastability extension from neuroscience to synthetic architectural requirement with falsification criteria
- The system-boundary fallacy as formal argument against context-as-state and memory-as-state objections
- The complete falsification test suite (SI-E)

**Overall assessment:** The intellectual territory is increasingly populated, with multiple independent research streams converging on the conclusion that LLM limitations are architectural and that temporal/state persistence is a fundamental gap. Paper 06's distinctive contribution is the formal dynamical-systems framework that unifies these observations under spectral stability theory, provides the three-operator specification, and delivers falsifiable predictions. The convergence pattern is: many people see the problem; Paper 06 provides the most complete architectural specification and formal mechanism.
