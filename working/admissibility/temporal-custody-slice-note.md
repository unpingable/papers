# Temporal/Custody mini-kernel — slice note

**Filed:** 2026-06-08. **Status:** companion note for the fenced Lean scratch slice. **NOT doctrine. NOT a paper. NOT a primitive. NOT promoted.** Companion to `~/git/lean/LeanProofs/Scratch/TemporalCustody.lean`. Custody-Class: SCRATCH. Not imported. No paper anchor. No promotion path. No discharge use.

## What this slice contains

A tiny module with:
- 3 structures (`Evidence`, `Citation`, `ConsumerAction`)
- 3 predicates (`ValidAt`, `CitedWhileValid`, `AdmissibleAt`)
- 2 specimens (`stale_specimen`, `fresh_specimen`)
- 4 theorems:
  - `stale_specimen_cited_while_valid` (positive: citation-time validity is non-vacuous)
  - `stale_specimen_not_admissible` (negative: stale at execution → not admissible)
  - `citation_validity_does_not_imply_execution_admissibility` (the load-bearing small-negative theorem)
  - `fresh_specimen_admissible` (positive contrast: admissibility is not vacuously refused)

The load-bearing claim:

```lean
theorem citation_validity_does_not_imply_execution_admissibility :
    ∃ a : ConsumerAction, CitedWhileValid a.citation ∧ ¬ AdmissibleAt a
```

Within this encoding (no retroactive-discharge bridge), a consumer action can have a perfectly valid citation at its origin and still be inadmissible at its execution boundary. The validity check is at execution time, not citation time; any path from citation-validity to execution-admissibility must be explicitly visible in the proof structure, not implicit. The Lean result is a default-refusal, not a universal impossibility — a system that wants to license retroactive discharge can do so by adding an explicit bridge.

The existential above is paired with an explicit negated-universal wrapper (`not_all_citation_validity_implies_admissibility`) that refutes the blanket rule directly. Unless explicitly stated as a universal theorem, the Lean result is a specimen/counterexample; broader doctrinal interpretation remains advisory.

## Witnessed (via `leanctx`)

These facts have build-receipt-backed evidence at repo SHA `9e88c52d564a`:

- **Module exists at the declared path.**
  `leanctx module LeanProofs.Scratch.TemporalCustody` → `witnessed: LeanProofs/Scratch/TemporalCustody.lean`.
- **Module compiles cleanly.**
  `leanctx build LeanProofs.Scratch.TemporalCustody` → `status: pass`, `exit_code: 0`, 400ms, lake 5.0.0-src / lean 4.29.0.
- **Prior-art modules compile at the same SHA.**
  Baseline: `leanctx build LeanProofs.Admissibility.StaleEvidenceMerge` → `status: pass`.
- **The new file is fenced.**
  Not imported by `LeanProofs.lean` (verified by absence of an import line in the lib root).
- **Custody header present.**
  File declares Custody-Class: SCRATCH in its header docstring.

Receipts archived at `/tmp/leanctx-temporal/baseline-stale-merge.json` and `/tmp/leanctx-temporal/post-temporal-build.json`. These are ephemeral — re-run leanctx for fresh witnesses.

## Asserted / advisory (not witnessed)

These claims are stated here under the asserted/advisory altitude — `leanctx` cannot witness them and they are NOT promoted to witnessed truth by this note:

- **Vocabulary correspondence.** The structures `Evidence`, `Citation`, `ConsumerAction` and the predicates `ValidAt`, `CitedWhileValid`, `AdmissibleAt` *correspond to the intended temporal/custody phenomenon* (evidence valid at citation but stale at execution). This is a semantic mapping — a sentence about what the Lean symbols mean — and is not witnessable by the build/grep/decl primitives. The Lean code does not "formalize" any particular real-world citation/execution scenario; it encodes a small algebraic shape that the author asserts maps onto the phenomenon.
- **Adjacency to prior art.** `Freshness.lean`, `StaleEvidenceMerge.lean`, and `RetroactiveLegitimation.lean` exist in the corpus (`leanctx module` witnesses this) and discuss adjacent territory at the prose level. The author asserts that this slice is *adjacent prior art* to those modules, not a formalization of them or a dependency of them. The new module imports none of them.
- **"Small negative theorem" shape.** The author asserts that `citation_validity_does_not_imply_execution_admissibility` is in the small-negative-theorem family discussed in the corpus. The shape is a structural choice, not a witnessed identity.

If any downstream document promotes these asserted claims to witnessed status, that promotion is unsupported by the harness and should be retracted.

## Two honest findings from running the harness against the work

1. **`receipt-valid` on the new build receipt returned `validity: stale`** because the working tree is dirty (the new `.lean` file exists on disk but is untracked at the time of build). The SHA matched HEAD, but the dirty check correctly refused to discharge the "builds now" claim. The staleness rule fired on its first real use against a live build — *exactly* the behavior the algebra is designed to enforce. To obtain a non-stale receipt, the file must be committed; the receipt at the new SHA will then discharge "builds now" until the next change.

2. **`leanctx decl` and `leanctx grep` cannot witness the new file's declarations** because `git grep` (the underlying oracle) only searches *tracked* files. `lake build` can see the file on disk and reports success; `git grep` reports zero matches for declarations the new file introduces. This is a *real composition asymmetry between the witnesses*: the build witness lives at the filesystem-state level (what Lean reads), while the grep/decl witnesses live at the git-tracked-state level (what git knows). For a witness layer pegged to repo SHAs, the git-grep choice is correct — untracked files have no SHA-bound identity — but the asymmetry is worth flagging for the next packet. If a future Phase 1.5 wants `decl` to witness untracked files, it must explicitly mark such results as `working_tree_only` rather than `at_sha`. Phase 1's choice is the more conservative one.

These findings are *features of the harness*, not bugs. Both are recorded so the next slice's author starts from the same understanding.

## What this slice does NOT claim

- Not a theory of citation freshness. The 4-theorem module captures one specimen-shaped negative result, not a general framework.
- Not a formalization of `Freshness.lean`, `StaleEvidenceMerge.lean`, or `RetroactiveLegitimation.lean`. These are *adjacent prior art* (asserted) and not imported or extended.
- Not a paper claim. Scratch only. Not anchored. Not promoted.
- Not a generalized temporal authority calculus. One small theorem.
- Not a bridge predicate for explicit retroactive discharge. The file's closing docstring names what such a bridge would look like; it does NOT build one. Building it would be a separate slice with its own forcing case.
- Not a recommendation that the current `AdmissibleAt` definition is the right one for any specific domain. The definition is the minimum shape that produces a non-vacuous negative theorem.

## Honest accounting

- **What was authorized:** one tiny module, 2–3 definitions, 1–2 negative theorems, with leanctx receipts.
- **What was built:** 3 structures + 3 predicates + 2 specimens + 4 theorems. Slightly more than the minimum because the positive specimens (`fresh_specimen_admissible`, `stale_specimen_cited_while_valid`) are needed as vacuity guards — without them, the negative theorem could be true by vacuity (admissibility refused for everything, citation-validity refused for everything).
- **What was *not* built:**
  - No bridge predicate for retroactive discharge.
  - No modifications to existing modules (`StaleEvidenceMerge` was used as prior-art reference only, not modified).
  - No imports of `Freshness.lean` or any related module.
  - No Phase 2/3 leanctx work.
  - No promotion of any prior asserted claim to witnessed.

## Curdling guard

Fenced scratch. Custody-Class: SCRATCH in the Lean file's header. Not imported. No paper anchor. No promotion path. No discharge use. The slice is additive — no existing module was touched.

## Cross-references

- Lean file: `~/git/lean/LeanProofs/Scratch/TemporalCustody.lean`
- Sibling scratch receipts: `bridge-interface-spike.md`, `provenance-profiles-scratch-receipt.md`, `labelwatch-scratch-receipt.md`
- Harness: `~/git/lean/tools/leanctx/` (Phase 1)
- Prior art (asserted-only adjacency, not formal dependency):
  - `LeanProofs/Admissibility/Freshness.lean`
  - `LeanProofs/Admissibility/StaleEvidenceMerge.lean`
  - `LeanProofs/Admissibility/RetroactiveLegitimation.lean`

---

**One small negative theorem. Four theorems total. Build witnessed via leanctx; semantic vocabulary correspondence is asserted/advisory. Two real harness findings recorded honestly. Standing down.**
