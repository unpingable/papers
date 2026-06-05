# Public Surface Audit — `LeanProofs/Admissibility/` — 2026-06-05

**Filed:** 2026-06-05. **Status:** audit. Source-of-truth table for which files are wired into the public build, which are part of the 1.0 surface promise, and which should remain public. Companion to [`custody-audit-2026-06-05.md`](custody-audit-2026-06-05.md); precondition for Phase 3 custody sweep and Phase 4 directory move.

## Scope and method

Surveys all 47 `.lean` files in `LeanProofs/Admissibility/`. For each, six questions:

1. **Imported by public aggregator?** — Does `LeanProofs.lean` import the file?
2. **Cited in README?** — Does the file's basename appear in `README.md` or `LeanProofs/Admissibility/README.md`?
3. **Has custody prose?** — Does the module docstring contain a `Custody:` paragraph?
4. **Downstream theorem citers?** — Count of files in `LeanProofs/Admissibility/`, `LeanProofs/Scratch/`, or `LeanProofs/*.lean` that import this file.
5. **In `AdmissibilityKernels.lean` 1.0 surface?** — Is the file in the eight-module public surface defined by the aggregator?
6. **Should remain public?** — Audit recommendation: should this file stay in the public build going forward?

The "imported by public aggregator?" answer carries a qualifier: `(1.0)` for files in the AdmissibilityKernels 1.0 surface, `(annex)` for files named in the AK annex section, `(other)` for files imported by LeanProofs.lean but unclassified by AK.

## Key counts

| Bucket | Count |
|---|---:|
| Total files in `LeanProofs/Admissibility/` | 47 |
| Imported by `LeanProofs.lean` (top-level public build) | 34 |
| In AdmissibilityKernels 1.0 surface | 8 |
| Named in AdmissibilityKernels annex section | 13 |
| LP-imported but unclassified by AK | 11 (+ the AK aggregator itself + CalculusOne) |
| Fenced (not imported by LP) | 13 |
| Carries `Custody:` prose | 8 |

The "8 files in AdmissibilityKernels 1.0 surface" memory claim is **confirmed** against the artifacts. The "directory does not exist on disk" finding **stands**: the 1.0 surface is currently the aggregator file `LeanProofs/Admissibility/AdmissibilityKernels.lean`, not a directory `LeanProofs/AdmissibilityKernels/`.

## The audit table

| File | Imported by LP? | Cited in README? | Custody prose? | Downstream | Should remain public? |
|---|---|---:|---|---:|---|
| AdmissibilityKernels | Y (aggregator) | 2 | N | 2 | **YES** — 1.0 surface aggregator |
| AmendmentFragment | N (fenced) | 0 | N | 0 | N — UNRATIFIED-CANDIDATE; per [project-formal-specimens-axis-1-3] |
| AttestationLedger | Y (other) | 1 | N | 0 | YES — consumer specimen; add to AK scope-fence |
| Authority | Y (1.0) | 2 | N | 6 | **YES — 1.0 surface; load-bearing** |
| AuthorizedNotSafe | Y (other) | 1 | N | 1 | YES — consumer specimen; add to AK scope-fence |
| AuthorizedNotSafeWitness | Y (other) | 1 | N | 3 | YES — consumer specimen; add to AK scope-fence |
| AuthorizedStepNotSafe | Y (other) | 1 | N | 0 | YES — consumer specimen; add to AK scope-fence |
| AuthorizedStepNotSafeWitness | Y (other) | 1 | N | 1 | YES — consumer specimen; add to AK scope-fence |
| AxisSkew | Y (annex) | 1 | Y | 0 | YES — AK-annex |
| BoundaryWitness | N (fenced) | 0 | N | 0 | N — SCRATCH; from BoundaryTransit work |
| BudgetMerge | N (fenced) | 0 | N | 2 | N — SCRATCH; imported by other fenced annexes |
| CalculusOne | Y (other) | 2 | N | 0 | **N — DEPRECATED**; explicitly marked "removed in 2.0" in `LeanProofs.lean` |
| ClosureEligibility | Y (annex) | 1 | Y | 0 | YES — AK-annex |
| Composition | Y (annex) | 1 | N | 1 | YES — AK-annex |
| Conductance | N (fenced) | 0 | Y | 0 | N — SCRATCH or UNRATIFIED-CANDIDATE (Phase 3 to decide) |
| ConsequencePartition | N (fenced) | 0 | Y | 0 | N — UNRATIFIED-CANDIDATE per [project-consequence-partition] |
| ConsolidationDenial | Y (other) | 1 | N | 0 | YES — consumer specimen per [project-consolidation-denial]; add to AK scope-fence |
| ContractionHinge | N (fenced) | 0 | N | 0 | N — UNRATIFIED-CANDIDATE per [project-formal-specimens-axis-1-3] |
| Corrective | Y (1.0) | 2 | N | 1 | **YES — 1.0 surface** |
| CorrectiveBoundary | Y (annex) | 2 | N | 0 | YES — AK-annex |
| CrossBoundaryCascade | Y (annex) | 1 | N | 0 | YES — AK-annex |
| CrossBoundaryDegradation | Y (annex) | 1 | N | 0 | YES — AK-annex |
| CrossBoundaryExposure | Y (annex) | 1 | N | 4 | YES — AK-annex; load-bearing within annex |
| CrossBoundaryFailureMint | Y (annex) | 1 | N | 1 | YES — AK-annex |
| Derivation | Y (1.0) | 2 | N | 3 | **YES — 1.0 surface** |
| Examples | Y (other) | 2 | N | 0 | YES — consumer specimen; add to AK scope-fence |
| Execution | Y (1.0) | 2 | N | 2 | **YES — 1.0 surface** |
| FiatAdmissibility | Y (annex) | 1 | Y | 1 | YES — AK-annex; reference-quality custody prose |
| Freshness | Y (1.0) | 2 | Y | 1 | **YES — 1.0 surface; only public file with prose** |
| GuardCollapse | N (fenced) | 0 | N | 0 | N — SCRATCH |
| LocalBoundary | Y (annex) | 1 | N | 0 | YES — AK-annex |
| Mandamus | N (fenced) | 0 | N | 0 | N — UNRATIFIED-CANDIDATE; sprint #2 pending per [project-refusals-need-receipts] |
| MergeConflict | N (fenced) | 0 | N | 1 | N — SCRATCH |
| NumericalAdmissibility | Y (annex) | 1 | Y | 0 | YES — AK-annex |
| ParameterizedMerge | N (fenced) | 0 | N | 0 | N — SCRATCH |
| ProjectionLaundering | N (fenced) | 0 | Y | 0 | N — UNRATIFIED-CANDIDATE |
| PublicReceiptRefinement | Y (annex) | 1 | N | 0 | YES — AK-annex |
| RecoveryMargin | Y (annex) | 1 | N | 0 | YES — AK-annex |
| RefusalPropagation | Y (other) | 0 | N | 0 | YES — consumer specimen; add to AK scope-fence |
| RetroactiveLegitimation | N (fenced) | 0 | N | 0 | N — UNRATIFIED-CANDIDATE per [project-formal-specimens-axis-1-3] |
| SafetyBridge | Y (other) | 1 | N | 10 | YES — consumer specimen; load-bearing (10 downstreams); add to AK scope-fence |
| SafetyBridgeWitness | Y (other) | 1 | N | 2 | YES — consumer specimen; add to AK scope-fence |
| SafetyTrajectory | Y (other) | 1 | N | 0 | YES — consumer specimen; add to AK scope-fence |
| StaleEvidenceMerge | N (fenced) | 0 | N | 1 | N — SCRATCH |
| StateTransition | Y (1.0) | 2 | N | 5 | **YES — 1.0 surface; load-bearing** |
| SurfaceAuthorization | Y (1.0) | 2 | N | 2 | **YES — 1.0 surface** |
| WitnessInvariance | Y (1.0) | 2 | N | 1 | **YES — 1.0 surface** |

**Row count:** 47, matching `ls LeanProofs/Admissibility/*.lean | wc -l`. Each file appears exactly once. ✓

## Interpretation

### The 1.0 surface (8 + aggregator)

The eight files in the AdmissibilityKernels 1.0 surface are:

```
Authority, StateTransition, Derivation, Execution,
Corrective, Freshness, SurfaceAuthorization, WitnessInvariance
```

Plus the AdmissibilityKernels aggregator itself. These are the files that would move to `LeanProofs/AdmissibilityKernels/` in Phase 4 if the directory move proceeds. Authority (6 internal citers) and StateTransition (5 internal citers) are the most-cited within the 1.0 surface; both are referenced by Derivation, Execution, and Corrective per the import graph.

### The annex (13 named + 11 unclassified = 24)

Twenty-four files are imported by the top-level public aggregator but explicitly outside the 1.0 stability promise. Thirteen are named annex in AdmissibilityKernels.lean's docstring; eleven are imported by `LeanProofs.lean` without any AK-level classification. The eleven unclassified are the consumer-specimen family (SafetyBridge × 5, AuthorizedNotSafe × 4, AttestationLedger, ConsolidationDenial, RefusalPropagation, Examples).

Per the custody audit's Finding 4, these 24 fall outside the four-class Phase 1 taxonomy. The recommended resolution is a fifth class `ANNEX` covering both groups uniformly.

### Deprecated (1)

`CalculusOne` is the lone DEPRECATED file. The import line in `LeanProofs.lean` already carries the marker comment `-- deprecated 1.1 shim; removed in 2.0`. Phase 3 should add `Custody-Class: DEPRECATED` and a `Custody:` paragraph noting the removal trajectory.

### Fenced (13)

Thirteen files are not imported by `LeanProofs.lean` at all. They split between SCRATCH (mechanical / experimental) and UNRATIFIED-CANDIDATE (named in working notes or memory as candidates with pending forcing-case discriminators):

- **UNRATIFIED-CANDIDATE (likely 6):** AmendmentFragment, ContractionHinge, RetroactiveLegitimation (axis-1-3 specimens), Mandamus (liveness dual; sprint #2 pending), ConsequencePartition (per memory note), ProjectionLaundering.
- **SCRATCH (likely 7):** BoundaryWitness, BudgetMerge, Conductance, GuardCollapse, MergeConflict, ParameterizedMerge, StaleEvidenceMerge.

Per-file scratch-vs-candidate decisions should be made in Phase 3 by inspecting docstrings; the audit's recommendations above are best-effort and not binding.

### Cross-check against the AK aggregator's scope-fence

The AdmissibilityKernels aggregator's docstring scope-fence enumerates the public surface (8 files) and the annex (13 files). It does **not** enumerate the 11 consumer specimens inside `Admissibility/`. Scope-fence point 6 names consumer specimens *outside* `Admissibility/` but stops at the directory boundary. This is the doctrine gap that lets 11 files exist in a custody-ambiguous state despite the rest of the aggregator's discipline.

## Phase 4 implications

The audit produces three findings that bear on the Phase 4 directory move:

1. **The set to move is precisely 9 files** (8 public + the aggregator). The 24 annex/specimen files stay in `Admissibility/`. The 13 fenced files stay where they are. The 1 deprecated file stays until 2.0 removal.
2. **The move requires updating ~30+ import sites** to point at `LeanProofs.AdmissibilityKernels.{Authority, ...}` instead of `LeanProofs.Admissibility.{Authority, ...}`. The `Authority` import alone has 6 internal citers; counting cross-LP-aggregator and downstream files, the total cite-site count is closer to 30.
3. **The move is large enough to be its own coherent unit**, and the import-update churn is the main reason the doctrine layer led the artifact layer for so long. The wiring-is-not-folder-placement discipline says the move is *not required* to make the 1.0 surface claim — the aggregator already does that. The Phase 4 decision is whether to lift folder placement into a custody claim *additionally*, given the import-update cost.

The user's earlier read landed on "do A unless it explodes imports." The audit's read is that imports do not explode (Lean handles renames cleanly with mechanical edits) but the churn is meaningful (~30 sites). The decision is real and should not be inferred from the workflow.

## Validation

Pinned by the workflow:

> Every file in `LeanProofs/Admissibility/*.lean` appears as exactly one row in the audit.

Verified: 47 files in the directory; 47 rows in the audit table; no duplicates; no omissions.
