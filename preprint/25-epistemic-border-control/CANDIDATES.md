# Paper 25 — Candidate Claims

## Primary candidate

**Candidate claim:** Under observability asymmetry where no real-time sensor on the target V exists and the available observables load on a fast proxy V′, the controller is *structurally forced* to substitute V′ for V. The rhetoric remains fixed on V. Sincere regulators facing the same sensor set produce the same substitution. The mechanism is structural; the action is agential.

**Status:** ready-for-formalization. Single-agent sim done; Paper 23 Gramian bridge operationalized. Literature differential remains as the only outstanding gate item.

**Imports:**
- Paper 23 §3.3 case (ii) — closed-loop dynamical dual of measurement null-space masking. P25 inherits the formal apparatus rather than reconstructing it.
- Observability subspace algebra (standard control theory).

**Depends on:**
- Literature differential (Perdomo et al. — performative prediction; Pagan et al. — feedback-loop classification; Sprenger et al. — recommenders as closed-loop control; Dwork et al. — moderation trade-offs).
- Sibling-vs-§N adjudication: resolved 2026-04-22 by algebraic argument (aggregation reduces variance as O(σ²/N) but does not rotate the observability subspace). Settled — sibling, not §N.

**Risk:**
- Necessity-framing (substitution is forced) collapsing back into Goodhart (possibility — substitution is contingent corruption). The whole contribution depends on holding the necessity edge.
- Discourse-moderation worked example becoming the paper's emotional center. Scope: applies to informal discourse regulators where no formal V-sensor exists, *not* to formal platform moderation (which has its own literature).
- Heterogeneous-agent case (different C_obs per agent) is its own object — belongs to a Paper 24/25 follow-on, not this paper.

**Do not accidentally merge with:**
- Paper 24 (aggregation-layer masking). Same family, distinct mechanism. Paper 24 *freezes* V; P25 *swaps* V for V′. Sibling, not nested.
- Goodhart's Law literature. Possibility-framed; P25 is necessity-framed.
- Performative prediction literature. Adjacent but distinct: performativity is about the model determining its training distribution; P25 is about observability asymmetry forcing target substitution.

## Descendant relation

P27 imports P25's projection α: B → K and observability-null-space framing, but adds transition admissibility, obligation accounting, and receipt durability. P27 is *constructive*; P25 is *necessity-framed negative*. P25 says you can't recover what isn't sensed. P27 says govern transitions so the controller does not silently destroy what *was* sensed.

## Attribution

Control-theory framing, state decomposition, classic-control-pathology list, and worked data-center example came from chatty in the 2026-04-21 riff. Necessity-framing sharpening from agent-governor-claude review (2026-04-21 late). Sibling-vs-§N algebraic adjudication 2026-04-22.
