# Paper 27: Ephemerality Is a Transition Property — Obligation-Unsound Reconciliation in Kubernetes and Other Control Loops

**Author:** James Beck
**Status:** Scaffold (2026-04-28). Queue-jumped per dependency-discovery argument: P27 supplies the constructive endpoint for the P22–P26 negative spine.

## Center of gravity

*Controller-correct, operator-unsound.* Reconciliation controllers may converge to desired state while silently degrading obligations required for diagnosis, governance, or operator reliance. Transition admissibility is the safety property complementary to convergence. Ephemerality is a transition property under declared obligations and retention horizons, not an object property.

## Position in the series

P22→P26 is escalating negative results. P27 is the constructive answer. Spine line:

> **P25 says you can't recover what isn't sensed; P27 says govern transitions so the controller does not silently destroy what was sensed.**

## Imports without absorption

P27 imports from P25 and P26 selectively:

- **From P25:** projection α: B → K, observability-null-space framing. Obligations live in or across the null space when not first-class control-plane objects.
- **From P26:** retention horizons (H : Obligation → Horizon) for evidence, causality, substrate-accusation. P27 borrows the horizon machinery, *not* the full premature/belated duality.
- **From P23:** hidden compensation as one downstream consequence of audit destruction (operator H_t carries causal continuity in memory when reconciliation strips it from the system).

P27 *adds*: transition admissibility predicate, obligation accounting (preserved / transferred / discharged / degradedWithReceipt / openFinding under accounted/unaccounted wrapper), audit states (Masked / Orphaned / DegradedWithReceipt), receipt durability invariant.

## Companion artifacts

| Artifact | Location | Role |
| --- | --- | --- |
| Lean skeleton | `~/git/lean/LeanProofs/Admissibility.lean` | Obligation/Outcome/Accounting algebra; theorem statements with deferred proofs |
| Conversation precursor | (multi-model riff 2026-04-28) | Kernel produced via DeepSeek/Gemini/Claude/chattY synthesis; no working/ note yet |

## Files

| File | Description |
| --- | --- |
| `metadata.yaml` | Series metadata + abstract stub |
| `CANDIDATES.md` | Claim container (status, imports, dependencies, risks) |
| `NOTES.md` | Scope discipline, drafting plan, lit-differential sketch |
| `README.md` | This file |

This is a claim container, not a draft. No prose draft yet. Lean skeleton is sorry-only.
