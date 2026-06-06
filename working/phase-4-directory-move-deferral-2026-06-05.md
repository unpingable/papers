# Phase 4 Decision (2026-06-05): Defer Directory Move

**Filed:** 2026-06-05. **Status:** decision record. Closes Phase 4 of the custody-discipline workflow by recording that the directory move is *deferred*, not *forgotten*. Sibling to [`public-surface-audit-2026-06-05.md`](public-surface-audit-2026-06-05.md), [`wiring-is-not-folder-placement.md`](wiring-is-not-folder-placement.md), [`custody-classes.md`](custody-classes.md), [`promotion-claims-require-custody-witnesses.md`](promotion-claims-require-custody-witnesses.md).

## The decision

> **The `LeanProofs/Admissibility/*.lean` → `LeanProofs/AdmissibilityKernels/*.lean` directory move is deferred. The 1.0 public surface claim is carried by the existing `LeanProofs/Admissibility/AdmissibilityKernels.lean` aggregator file plus per-file `Custody-Class:` markers, not by directory placement.**

## Why deferring is the right call

The Phase 2 public-surface audit found that:

1. The 1.0 surface is precisely 8 modules + the aggregator, confirmed against the AdmissibilityKernels.lean docstring's "Public surface (8 modules)" table.
2. A directory move would touch ~30 import cite sites and rename eight+ namespaces (`LeanProofs.Admissibility.Authority` → `LeanProofs.AdmissibilityKernels.Authority`, etc.).
3. The custody claim the move would carry is already discharged at the artifact layer by:
   - the AdmissibilityKernels aggregator's scope-fence (Phase 3A extension enumerates all 24 ANNEX files in two sub-groups);
   - per-file `Custody-Class:` markers across all 47 files (Phase 3B, verified by `scripts/check-custody-classes.sh`);
   - per-file `Custody:` prose paragraphs on the 8 PUBLIC-SHIPPED modules + the aggregator (Phase 3B).

Per [`wiring-is-not-folder-placement.md`](wiring-is-not-folder-placement.md) ([[project-wiring-vs-folder-placement]]): physical location, build coverage, and custody / public claim status are three independent concepts. Phase 3 placed the custody receipts at the artifact level. The directory move would have done the same work at the path level. Doing both is redundant. Doing only the cheaper one is correct.

The companion doctrine [`promotion-claims-require-custody-witnesses.md`](promotion-claims-require-custody-witnesses.md) is satisfied: the promotion claim ("X is in the 1.0 surface") now has artifact-level witnesses (`Custody-Class: PUBLIC-SHIPPED` in each file, plus AdmissibilityKernels.lean's aggregator import and scope-fence enumeration). No witness gap remains for the directory move to close.

## What re-opens this decision

Phase 4 is *deferred*, not *closed*. The following are concrete forcing cases that would re-open the directory move:

1. **A downstream consumer needing the 1.0 surface as a separate namespace** — e.g., an external Lean project or paper-companion library that wants `import LeanProofs.AdmissibilityKernels` to bring in only the 8-module surface without pulling in the 24 ANNEX files. Currently no such consumer exists.
2. **A major-version cut (2.0).** A directory boundary may be useful as a versioning anchor that imports cannot accidentally cross. The current 1.0 surface aggregator carries this discipline at the import-list level; a 2.0 split could promote it to the directory level.
3. **CI / build tooling that wants directory-level scoping.** If a future check needs "run only the 1.0 surface tests" or "lint only the public API," directory structure becomes load-bearing for tooling.
4. **Public surface growth past ~15–20 modules.** Eight files fit in one aggregator file legibly; a larger surface may want directory structure for navigation.

If one of these arrives, the move becomes a real Phase 4 and the audit table in [`public-surface-audit-2026-06-05.md`](public-surface-audit-2026-06-05.md) provides the per-file go/no-go data. Until then: no move.

## What Phase 4 closes

- **The "`LeanProofs/AdmissibilityKernels/` directory doesn't exist on disk" finding from the 2026-06-05 self-audit.** The finding stands; the resolution is that the directory does not need to exist. The artifact-level witnesses installed in Phase 3 are sufficient.
- **The workflow's Phase 4 slot.** No longer open; the question is settled until one of the forcing cases above appears.
- **The wiring-vs-folder-placement scar opened against the corpus itself on 2026-06-05.** The framework caught itself making a promotion claim whose witness lived only in memory/doctrine. The fix landed at the cheaper layer (per-file markers + aggregator enumeration), demonstrating that *wiring-is-not-folder-placement* is operational, not just doctrinal.

## What Phase 4 does not do

- Does not delete or refactor `LeanProofs/Admissibility/`. Files stay where they are.
- Does not break or update any import paths. All current imports continue to work.
- Does not preclude the move. The decision is reversible; nothing in Phase 3 forecloses a future directory-level reorganization.
- Does not require user action. The deferral is the artifact.
