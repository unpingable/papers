# Custody Prose Audit — `LeanProofs/Admissibility/` — 2026-06-05

**Filed:** 2026-06-05. **Status:** audit. Surveys existing `Custody:` prose across the 47 `.lean` files in `LeanProofs/Admissibility/`. Companion to [`public-surface-audit-2026-06-05.md`](public-surface-audit-2026-06-05.md); precondition for the Phase 3 mechanical sweep ratified in [`custody-classes.md`](custody-classes.md).

## Summary

- **Files surveyed:** 47 (`LeanProofs/Admissibility/*.lean`).
- **Files with `Custody:` prose:** 8.
- **Files with `Custody-Class:` marker:** 0. (The marker convention is new in Phase 1.)
- **Files with neither:** 39.

Earlier informal counts ("about a dozen" carried prose) were generous. The precise number, found by matching `^[[:space:]]*Custody:` inside the module docstring, is eight.

## Files with `Custody:` prose

| File | Substance of the prose |
|---|---|
| `AxisSkew.lean` | Annex; not part of 1.0 surface; signature not promised stable. |
| `ClosureEligibility.lean` | Annex; not part of 1.0 surface. |
| `Conductance.lean` | Fenced annex; experimental. |
| `ConsequencePartition.lean` | Fenced annex; consequence-partition primitive candidate. |
| `FiatAdmissibility.lean` | Canonical only via commit hash + lake build gate + ratification rule on changes to `ArtifactKind` / `UseKind` / `classify`. Most substantive narrative of the set. |
| `Freshness.lean` | 1.0 public surface; load-bearing. |
| `NumericalAdmissibility.lean` | Annex; not part of 1.0 surface. |
| `ProjectionLaundering.lean` | Fenced annex; candidate kernel. |

The eight split: **one** is in the 1.0 public surface (Freshness); **three** are AdmissibilityKernels-annex (AxisSkew, ClosureEligibility, NumericalAdmissibility); **four** are fenced (Conductance, ConsequencePartition, FiatAdmissibility — wait, FiatAdmissibility is annex not fenced — see below, ProjectionLaundering).

Corrected: of the eight, **one** is PUBLIC-SHIPPED, **four** are AK-annex, **three** are fenced. FiatAdmissibility carries the most substantive prose despite being annex.

## Files with no custody prose at all

All 39. Includes seven of the eight PUBLIC-SHIPPED 1.0-surface modules: Authority, StateTransition, Derivation, Execution, Corrective, SurfaceAuthorization, WitnessInvariance. Only Freshness in the 1.0 surface carries narrative custody. This is the most striking gap.

It also includes the entire SafetyBridge family (10 files), the deprecated CalculusOne shim, all but four of the fenced annexes, and the AdmissibilityKernels aggregator itself (whose docstring is rich on scope but does not use the `Custody:` keyword).

## Findings

### Finding 1 — Existing prose is consistent with the Phase 1 taxonomy

Every existing custody paragraph describes one of:

- "imported into the 1.0 surface, signature promised stable" → maps to `PUBLIC-SHIPPED`
- "compiled, not promised" → maps to `ANNEX` (see Finding 4)
- "fenced, experimental, candidate" → maps to `SCRATCH` or `UNRATIFIED-CANDIDATE`

Phase 1's `Custody-Class:` markers can be added on top of the existing prose without conflict. The prose is the receipt; the class is the grep target.

### Finding 2 — The 1.0 surface is custody-prose-impoverished

Seven of the eight PUBLIC-SHIPPED files carry no `Custody:` paragraph. The aggregator's docstring carries scope discipline, but per-file custody narratives are absent. This is the inverse of the laundering risk the two-layer convention guards against: the *class* will be added by Phase 3, but the *receipt* will remain empty for the modules that most need it.

Phase 3 should write minimal one-sentence custody prose for each of the seven (`Custody:  Public 1.0 surface; imported by AdmissibilityKernels aggregator; signature promised stable until major version bump.` or equivalent). This is more work than a pure mechanical sweep, but the sweep without it would only deepen the asymmetry.

### Finding 3 — `FiatAdmissibility` is the prose-quality reference

Of the eight existing custody paragraphs, FiatAdmissibility's is the only one that names a specific binding mechanism (commit hash + build gate + ratification rule on specific type names). The other seven say variants of "annex" or "experimental." When Phase 3 writes new custody prose, FiatAdmissibility is the shape to imitate, not the seven minimum-information annex paragraphs.

### Finding 4 — The four-class taxonomy has a gap; an `ANNEX` class is needed

The Phase 1 doctrine ratified four classes: PUBLIC-SHIPPED, SCRATCH, UNRATIFIED-CANDIDATE, DEPRECATED. The audit reveals that **24 of 47 files** fall into a category none of these match: *compiled and imported by the top-level public aggregator (`LeanProofs.lean`), but explicitly not part of the AdmissibilityKernels 1.0 stability promise.*

These 24 are:

- **13** named in AdmissibilityKernels.lean's docstring as "Annex (compiled, not promised)": CorrectiveBoundary, PublicReceiptRefinement, RecoveryMargin, ClosureEligibility, FiatAdmissibility, NumericalAdmissibility, AxisSkew, CrossBoundaryExposure, CrossBoundaryDegradation, CrossBoundaryFailureMint, CrossBoundaryCascade, LocalBoundary, Composition.
- **11** imported by LeanProofs.lean but unclassified by AdmissibilityKernels.lean: AttestationLedger, AuthorizedNotSafe, AuthorizedNotSafeWitness, AuthorizedStepNotSafe, AuthorizedStepNotSafeWitness, SafetyBridge, SafetyBridgeWitness, SafetyTrajectory, ConsolidationDenial, RefusalPropagation, Examples.

These are not SCRATCH — they are wired into the public aggregator. They are not PUBLIC-SHIPPED — they are explicitly outside the 1.0 stability promise. They are not UNRATIFIED-CANDIDATE — they are settled as compiled material, not candidates for promotion. They are not DEPRECATED — they are not on a removal trajectory.

The cleanest resolution is to **add a fifth class** to the Phase 1 doctrine:

> `ANNEX` — Compiled and imported by the public build, but signatures are not part of the public stability promise. Future versions may rename, refactor, or absorb without notice.

This matches AdmissibilityKernels.lean's existing "annex" usage exactly and resolves the gap without bending the existing four classes. The user's earlier prohibition on a six-class taxonomy stands; this is a fifth class with a forcing case (24 files), not a baroque addition.

### Finding 5 — Eleven files are imported but unclassified at the aggregator

A subset of Finding 4 deserves its own line: 11 consumer-specimen files inside `Admissibility/` are imported by `LeanProofs.lean` but not classified by the AdmissibilityKernels aggregator's "Public surface" or "Annex" sections. The AK aggregator's scope-fence point 6 names consumer modules *outside* `Admissibility/` but does not enumerate the 11 inside it.

If Phase 4 follows through on the directory move, this is the set most at risk of being silently dragged along by `mv` rather than explicitly classified. The Phase 2 public-surface audit table makes the count and identities legible; Phase 3 should assign each a `Custody-Class:` (likely `ANNEX` per Finding 4) and the AK aggregator's scope-fence should be extended to enumerate them.

## Recommendations

1. **Add `ANNEX` as a fifth class** to [`custody-classes.md`](custody-classes.md). Forcing case: 24 files have no other valid class. (User decision; cannot be silently done by Phase 3.)
2. **Phase 3 should write per-file custody prose for the seven custody-impoverished 1.0-surface modules**, modeled on FiatAdmissibility's shape, not on the minimal "annex" paragraphs.
3. **The AdmissibilityKernels aggregator's scope-fence should be extended** to enumerate the 11 unclassified consumer specimens. (Aggregator edit; can be Phase 3 or Phase 4.)
4. **Phase 4 directory-move decision should be deferred** until the ANNEX-class decision is made and prose is filled. Moving files whose class is undetermined would silently launder them by `mv`.

## Validation pinned by the workflow

> Every file in `LeanProofs/Admissibility/*.lean` appears as exactly one row in the audit.

Forty-seven files exist in the directory. The public-surface audit table ([`public-surface-audit-2026-06-05.md`](public-surface-audit-2026-06-05.md)) contains exactly 47 rows, one per file, verified by row-count match against `ls LeanProofs/Admissibility/*.lean | wc -l`.
