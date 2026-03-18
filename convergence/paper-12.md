# Paper 12 — Bounded Lattice Inference — Convergence Spike

**Full title:** Bounded Lattice Inference: A Governed Reasoning Substrate with Persistent State and Non-Linguistic Authority
**Date:** 2026-01-04
**DOI:** 10.5281/zenodo.18145346

## Status: complete

## Claim Cluster
- Persistent state can be introduced to LLM systems without granting agency, goals, or self-modification by separating linguistic proposal from non-linguistic authority
- Interiority (system behaving differently based on internal state rather than just input) is confirmable via hysteresis testing, demonstrated at 16.7% divergence rate
- Two distinct phase boundaries exist: budget starvation and glass ossification
- Safety invariants can be maintained across all experimental conditions by architectural enforcement rather than training
- Epistemic constraints can be enforced by construction (architectural) rather than by alignment (training)

## Search Terms
- language model persistent state governed reasoning
- non-linguistic authority AI architecture
- hysteresis testing interiority language models
- epistemic governance constraint enforcement architecture
- safety by construction vs safety by training
- supervisory control language model reasoning
- state machine language model hybrid architecture
- architectural safety invariants AI systems

## Expected Convergence Level
hints expected
The idea of constraining LLM outputs with external state machines or structured reasoning is emerging (e.g., constrained decoding, tool use architectures), but the specific separation of linguistic proposal from non-linguistic authority with hysteresis-tested interiority is likely distinctive.

## Hits

### DIRECT CONVERGENCE (addresses same problem space with overlapping mechanisms)

**1. Bengio et al. — "Superintelligent Agents Pose Catastrophic Risks: Can Scientist AI Offer a Safer Path?"**
- Authors: Yoshua Bengio et al.
- Year: 2025 (arxiv 2502.15657); LawZero nonprofit launched June 2025
- Venue: arXiv / LawZero
- Match type: **strong thematic convergence**
- Claims touched: non-agentic AI, safe-by-design, separation of understanding from acting
- How close: Bengio proposes "Scientist AI" — non-agentic, no goals, learns to understand rather than act, with externalized transparent reasoning. This independently converges on BLI's core architectural move: persistent reasoning without agency. Key difference: Bengio's system is a world model + QA inference machine; BLI is a governor + ledger + FSM. Bengio frames it as an alternative to agentic AI; BLI frames it as a containment architecture for existing LLMs. Both reject the agent paradigm. Bengio does NOT have: NLAI separation, hysteresis testing, phase boundaries, queueing-theoretic stability, or contradiction persistence.

**2. Semantic Integrity Constraints (SICs) — Lee et al.**
- Authors: Lee et al. (Brown University / VectraFlow)
- Year: 2025
- Venue: PVLDB 18(11): 4073-4080 (arxiv 2503.00600)
- Match type: **strong structural convergence**
- Claims touched: epistemic constraints by construction, declarative enforcement, architectural safety
- How close: SICs generalize database integrity constraints to semantic LLM outputs, supporting grounding, soundness, and exclusion constraints with reactive and proactive enforcement. This is the closest independent work to BLI's "constraints enforced by construction" claim. Key difference: SICs operate in data processing pipelines (SQL-like), not in multi-turn reasoning with persistent state. No contradiction persistence, no phase boundaries, no interiority concept. But the declarative-guardrails-by-architecture philosophy is strikingly parallel.

**3. C-SafeGen — Claim-Based Streaming Guardrails**
- Authors: (multiple, see OpenReview)
- Year: 2025
- Venue: NeurIPS 2025 (poster)
- Match type: **strong mechanism convergence**
- Claims touched: claim-level safety enforcement, architectural rather than training-based safety
- How close: C-SafeGen decomposes LLM output into claims, applies a guardrail model per-claim, and uses backtracking when claims are flagged. This independently converges on BLI's claim extraction + per-claim governance pattern. Key difference: C-SafeGen focuses on content safety (harmful outputs), not epistemic coherence (contradiction). No persistent state, no interiority, no phase analysis. But the "extract claims, govern claims" pipeline is architecturally very similar.

### PARTIAL CONVERGENCE (addresses related problem, different framing)

**4. StateFlow — Wu et al.**
- Authors: Yiran Wu et al.
- Year: 2024 (arxiv 2403.11322)
- Venue: COLM 2024
- Match type: **partial structural convergence**
- Claims touched: state machine + LLM hybrid, process grounding via state transitions
- How close: StateFlow models LLM task-solving as a finite state machine with defined state transitions. Converges on BLI's FSM-governed architecture. Key difference: StateFlow uses states to track task progress (workflow), not epistemic state (beliefs/contradictions). No NLAI, no evidence gating, no contradiction persistence. The FSM is a workflow controller, not an epistemic governor.

**5. Boddy & Joseph — "Regulating the Agency of LLM-based Agents"**
- Authors: Sean Boddy, Joshua Joseph
- Year: 2025 (arxiv 2509.22735)
- Venue: arXiv / Berkman Klein Center (Harvard)
- Match type: **partial thematic convergence**
- Claims touched: agency as measurable/controllable property, separating agency from capability
- How close: Operationalizes agency along three dimensions (preference rigidity, independent operation, goal persistence) and proposes "agency sliders" via representation engineering. Converges on BLI's claim that agency and stateful reasoning are separable. Key difference: Controls agency via activation steering (training-adjacent), not architectural enforcement. No persistent state, no contradiction tracking, no NLAI.

**6. BarrierSteer — Control Barrier Functions for LLM Safety**
- Authors: (see arxiv 2602.20102)
- Year: 2026
- Venue: arXiv
- Match type: **partial mechanism convergence**
- Claims touched: safety invariants enforced by construction, architectural safety
- How close: Embeds non-linear safety constraints in latent representation space using Control Barrier Functions. Safety is enforced without modifying model weights — architectural, not trained. Converges on BLI's "safety by construction" claim. Key difference: Operates in continuous latent space, not discrete FSM + ledger. No epistemic governance, no contradiction persistence, no interiority concept.

**7. Huang et al. — "On the Failure of Latent State Persistence in Large Language Models"**
- Authors: Huang et al. (Johns Hopkins, Renmin University)
- Year: 2025 (arxiv 2505.10571)
- Venue: arXiv
- Match type: **partial convergence (problem validation)**
- Claims touched: LLMs lack persistent internal state, interiority is absent by default
- How close: Demonstrates that 17 frontier LLMs fail to maintain latent state persistence, operating as "reactive post-hoc reasoners." This directly validates BLI's premise: interiority must be constructed, not discovered. The paper identifies the LSP gap that BLI claims to fill. Key difference: Pure diagnosis (no solution architecture). Does not propose governance, persistence mechanisms, or NLAI. But confirms BLI's starting assumption empirically across frontier models.

**8. MemOS — Memory Operating System for AI**
- Authors: Shanghai Jiao Tong / Zhejiang University teams
- Year: 2025 (arxiv 2505.22101, 2507.03724)
- Venue: arXiv
- Match type: **partial structural convergence**
- Claims touched: persistent state management, lifecycle governance, access control
- How close: Treats memory as a first-class governed resource with lifecycle states (Generated, Activated, Merged, Archived, Expired), access control, and traceability. Converges on BLI's persistent state with governance. Key difference: MemOS governs memory for performance/utility, not epistemic coherence. No NLAI, no contradiction persistence, no evidence gating. Memory management, not reasoning governance.

### ADJACENT WORK (related concepts, different goals)

**9. FSM-Constrained Decoding (XGrammar, Outlines, SGLang)**
- Year: 2024-2025
- Venue: Various (LMSYS, SGLang, vLLM)
- Match type: **adjacent mechanism**
- Claims touched: FSM enforcement on LLM outputs
- How close: Uses finite state machines to constrain token-level decoding to valid outputs (JSON, regex). Shares the FSM-over-LLM pattern but operates at token level, not epistemic level. No state persistence, no contradictions, no interiority.

**10. Constrained Decoding Attacks (CDA) — arxiv 2503.24191**
- Year: 2025
- Match type: **adjacent (cautionary)**
- How close: Shows that grammar-level constraints on LLM outputs create new attack surfaces. Relevant to BLI because BLI's claim extraction layer is acknowledged as the primary vulnerability. CDA demonstrates that structural enforcement at one level can be bypassed at another — BLI acknowledges this via the EXTRACTION_COLLAPSE regime.

**11. Lattice Representation Hypothesis — ICLR 2026**
- Authors: (see arxiv 2603.01227)
- Year: 2026
- Match type: **terminological overlap only**
- How close: Uses "lattice" in the formal concept analysis sense (concept lattices in embedding space). Completely different meaning from BLI's "lattice" (belief/commitment lattice). No architectural overlap despite shared terminology.

**12. "Toward Epistemic Stability" — arxiv 2603.10047**
- Authors: (see arxiv)
- Year: 2026
- Match type: **adjacent (same problem, prompt-engineering approach)**
- Claims touched: epistemic consistency, repeatable outputs
- How close: Defines "Epistemic Stability" as consistency of engineering procedures across runs. Addresses same symptom (LLM inconsistency) but via prompt engineering, not architecture. No persistent state, no NLAI, no contradiction tracking. Five methods are all inference-time prompt strategies, not structural enforcement.

**13. "From Debate to Deliberation: Structured Collective Reasoning with Typed Epistemic Acts" — arxiv 2603.11781**
- Year: 2026
- Match type: **adjacent (multi-agent epistemic protocol)**
- How close: Introduces typed epistemic interactions for multi-agent deliberation with tension preservation and procedural closure. Shares epistemic governance vocabulary but operates in multi-agent debate, not single-system coherence.

## Notes

1. **The "non-linguistic authority" concept has no independent parallel.** No discovered work separates linguistic proposal from non-linguistic commit authority as a first-class architectural invariant. Bengio's Scientist AI is the closest in spirit (non-agentic, externalized reasoning) but does not formalize the authority separation.

2. **Hysteresis testing for interiority is novel.** The operational definition of interiority as measurable path dependence (I(Y;S|X) > 0) via hysteresis testing has no independent counterpart. Huang et al. (2025) diagnose the absence of LSP but do not propose a construction or testing protocol for its presence.

3. **Phase boundary analysis (starvation/glass) via queueing theory is novel.** No discovered work applies queueing-theoretic stability analysis (lambda vs mu) to epistemic state management in LLM systems. The queueing theory + LLM intersection (Informs 2025) addresses inference scheduling, not epistemic coherence.

4. **Contradiction persistence as first-class objects is partially converged.** C-SafeGen's claim-based streaming and SICs' declarative constraints are architecturally parallel, but neither treats contradictions as persistent, resolvable-only-with-evidence objects.

5. **"Safety by construction vs safety by training" is an emerging theme** but remains mostly rhetorical. Bengio uses it, BarrierSteer approaches it, but BLI's specific implementation (FSM + evidence gating + append-only ledger) is distinct.

6. **The cybernetic framing (Ashby, Beer, Conant-Ashby) applied to LLM governance is very rare.** One Databricks blog post (2025) discusses management cybernetics + AI; one Cambridge paper discusses AI as a constituted system with accountability. Neither applies cybernetic control theory to LLM reasoning architectures with the specificity BLI does.

## Verdict

**Confirmed: hints-to-partial convergence, with significant novelty remaining.**

The literature shows clear convergence on three background premises:
- LLMs lack persistent internal state (Huang et al. 2025 confirms this empirically)
- Architectural/declarative safety enforcement is preferable to training-only (SICs, C-SafeGen, BarrierSteer, Bengio)
- Stateful LLM systems need not be agentic (Bengio 2025, Boddy & Joseph 2025)

BLI's specific contributions remain without independent parallel:
- **NLAI as a formal invariant** — no prior art separating linguistic proposal from non-linguistic commit authority
- **Hysteresis-tested interiority** — novel operational definition and test protocol
- **Queueing-theoretic phase boundaries** (starvation, glass) — novel application domain
- **Contradiction as persistent first-class object** requiring evidence for resolution — novel
- **The integrated architecture** (governor + FSM + ledger + budget + evidence gating) — no equivalent system

The closest overall match is Bengio's Scientist AI, which independently arrives at "non-agentic reasoning" as the safe path. But BLI provides the concrete enforcement architecture that Scientist AI describes only in outline. The expected convergence level ("hints expected") is confirmed — the field is converging on the problem space but not on BLI's specific mechanisms.
