# RetroactiveFigLeaf — slice note

**Filed:** 2026-06-08. Companion to `~/git/lean/LeanProofs/Scratch/RetroactiveFigLeaf.lean`. Custody-Class: SCRATCH. Not imported. No paper anchor. No promotion path. No discharge use.

## Witnessed (via `leanctx`)

- HEAD at slice start: `84caaf63` (clean) — pre-work decl probes returned `at_sha`.
- Prior-art modules resolved: `RetroactiveLegitimation`, `TemporalCustody`, `StaleEvidenceMerge`.
- `decl PostValidated` → witnessed at `RetroactiveLegitimation.lean:115` (tracked, `at_sha`).
- `decl Authorized` and `decl AuthorizedAt` → `gap_blocks` (no top-level matches at HEAD).
- New module compiles cleanly: `lake build LeanProofs.Scratch.RetroactiveFigLeaf` → `status: pass`, 363ms, lean 4.29.0.
- Build receipt's `custody_scope: working_tree_only` (the new file is untracked at build time); `discharges: ['build_passes_in_worktree']`. **NOT** a discharge of `build_passes_at_sha`. Honest.

## Asserted / advisory (NOT witnessed)

- Vocabulary correspondence: that `Decision`, `Evidence`, `AuthorizedBy`, `PostValidatedAt` map onto the intended fig-leaf / retroactive-justification phenomenon. The Lean code encodes a small temporal-ordering algebra; the *interpretation* as fig-leaf is the author's claim, not the harness's.
- Adjacency to `RetroactiveLegitimation.lean` (which contains its own `PostValidated` def). This slice does NOT import or extend that module. The adjacency is in the prose / specimen-shape, not in the type signatures.
- Small-negative-theorem shape: the author asserts the theorem belongs to that family. Structural choice, not witnessed identity.

## What landed

```text
3 types (+ 1 abbrev):   Time, Decision, Evidence
2 predicates:           AuthorizedBy, PostValidatedAt
3 specimens:            early_decision, pre_existing_evidence, late_evidence
4 theorems:
  positive (vacuity guards):
    pre_existing_authorizes_early_decision
    late_evidence_post_validates_at_25
  negative (instance):
    late_evidence_does_not_authorize_early_decision
  negative (THE theorem):
    post_validation_does_not_imply_authorization
```

Load-bearing claim:

```
∃ d e t. PostValidatedAt d e t ∧ ¬ AuthorizedBy d e
```

Later-arriving evidence does not authorize an earlier decision. The closing docstring names the explicit bridge predicate (`AllowsRetroactiveAuthorization`) that would be required to license retroactive discharge, and refuses to build it here.

## Non-goals honored

- No import of `RetroactiveLegitimation`, `TemporalCustody`, or `StaleEvidenceMerge`.
- No modifications to any existing module.
- No bridge predicate built — only described in docstring.
- No generalized temporal-authority calculus.
- No "this formalizes prose doctrine X" claim emitted as witnessed.

## Curdling guard

Fenced scratch. Custody-Class: SCRATCH per Lean file header. Not imported. No paper anchor. No promotion. Specimen sibling to `RetroactiveLegitimation`, not a v2.

---

**One small negative theorem. Build witnessed via leanctx (worktree-scope, honestly demoted). Vocabulary correspondence advisory. Standing down.**
