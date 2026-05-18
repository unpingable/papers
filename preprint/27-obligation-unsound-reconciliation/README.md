# Paper 27: Ephemerality Is a Transition Property — Obligation-Unsound Reconciliation in Kubernetes and Other Control Loops

**Author:** James Beck
**Status:** v1.0 (2026-05-18). Pending Zenodo deposit.

## Center of gravity

*Convergence-correct, operator-unsound.* Reconciliation controllers may converge to desired state while silently degrading obligations required for diagnosis, governance, or operator reliance. Transition admissibility is the safety property complementary to convergence. Ephemerality is a transition property under declared obligations and retention horizons, not an object property.

## Position in the series

P22→P26 is escalating negative results on what controllers cannot achieve under partial information. P27 is not a constructive completion of that spine — it specifies a design constraint for controllers acting under those limits. Spine line:

> **P25 says you can't recover what isn't sensed; P27 says govern transitions so the controller does not silently destroy what was sensed.**

## Imports without absorption

P27 imports from P25 and P26 selectively:

- **From P25:** projection α: B → K, observability-null-space framing. Obligations live in or across the null space when not first-class control-plane objects.
- **From P26:** retention horizons (H : Obligation → Horizon) for evidence, causality, substrate-accusation. P27 borrows the horizon machinery, *not* the full premature/belated duality.
- **From P23:** hidden compensation as one downstream consequence of audit destruction (operator H_t carries causal continuity in memory when reconciliation strips it from the system).

P27 *adds*: transition admissibility predicate, obligation accounting (preserved / transferred / discharged / degradedWithReceipt / openFinding under accounted/unaccounted wrapper), audit states (Masked / Orphaned / DegradedWithReceipt / CannotTestify), three-horizon receipt durability invariant (persistence / retrieval / authority-separation), distributed-admissibility property over controller + receipt substrate + audit authority, three enforcement modes (hard gate / soft gate / audit-only).

## Companion artifacts

| Artifact | Location | Role |
| --- | --- | --- |
| Lean skeleton | `~/git/lean/LeanProofs/Admissibility.lean` | Obligation/Outcome/Accounting algebra. Three real proofs against the local `admissible` definition (`unaccounted_implies_inadmissible`, `short_receipt_horizon_inadmissible`, `open_finding_admissible_with_durability`); two `True`-placeholder theorems (`masked_recovery_not_resolved`, `orphaned_causality_inadmissible`) pending substrate-accusation / causal-binding vocabulary. Scoped as local accounting core; distributed-admissibility framing carried by paper model (§8). |
| Worked-case scaffolding | `WORKED_CASES.md` | Per-case structural fields (substrate state, projection gap, destroyed obligations, predicate forced, receipt requirement) for §5's three Kubernetes scenarios. |
| Working note | `working/admissible-recovery-semantics.md` | Corrective monotonicity / non-laundering recovery semantics. |

## Files

| File | Description |
| --- | --- |
| `obligation_unsound_reconciliation.md` | Main paper |
| `obligation_unsound_reconciliation.pdf` | Rendered PDF |
| `WORKED_CASES.md` | Supplementary structural per-case fields |
| `metadata.yaml` | Series metadata + abstract |
| `CANDIDATES.md` | Historical claim container (status, imports, dependencies, risks) |
| `NOTES.md` | Historical scope discipline, drafting plan, lit-differential sketch |
| `README.md` | This file |
