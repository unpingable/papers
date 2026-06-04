# RetroactiveLegitimation slice — codex adversarial review

**Status:** Agent-filed 2026-06-02. Single-pass codex review of
`LeanProofs/Admissibility/RetroactiveLegitimation.lean` (at
`~/git/lean/`), Slice 1 of the substructural-sequent program
(axis 3 of the [maximal-calculus axis map](maximal-calculus-refused-map.md)).

Sibling to
[`contraction-hinge-codex-review.md`](contraction-hinge-codex-review.md)
(axis 2) and
[`maximal-calculus-codex-review-log.md`](maximal-calculus-codex-review-log.md)
(axis 1). Per-fragment review traces are kept separated.

## Build status

- `lake env lean LeanProofs/Admissibility/RetroactiveLegitimation.lean`: exit 0.
- `lake build`: exit 0, 8305 jobs (identical to baseline — annex is not imported).
- `#print axioms` output:

```
pre_valid_witness_authorizes                : no axioms
pre_authorized_transition                   : [propext]
install_witness_valid_after_apply           : [propext]
post_validated_empty_install                : [propext]
empty_not_authorized                        : [propext]
retroactive_install_not_admissible          : [propext]
post_validation_does_not_imply_authorization: [propext]
post_validation_does_not_imply_transition   : [propext]
```

No `sorry`, no `admit`, no user-introduced axioms. `propext` is Lean 4 core, used internally by `simp`.

## Codex invocation

`codex exec -c approval_policy="never" --sandbox read-only --skip-git-repo-check --cd /home/jbeck/git/lean` (model gpt-5.5). Prompt: the charter's nine review items, with explicit "do not redesign" guardrails.

## Findings (verbatim)

1. **No `sorry` / `admit` / `True` placeholders.** No issue.
2. **`AuthorizedIn` uses `ValidIn S`, not `ValidIn (apply S O)`.** No issue. `AuthorizedIn S O := ∃ W, ValidIn S O W`.
3. **`Transition` requires pre-state authorization.** No issue. `AuthorizedIn S O` is the second conjunct.
4. **`PostValidated` separate from `AuthorizedIn`.** No issue. `PostValidated S O := ∃ W, ValidIn (apply S O) O W`, visibly distinct type.
5. **T2 proves the post-state witness is real.** No issue. Membership in `(install W, W) :: empty.valid` via `simp [apply, empty]`; depends on `install` actually adding the pair.
6. **T4 refusal goes through pre-state shape.** No issue. T4 extracts `h.2 : AuthorizedIn empty ...` and applies `empty_not_authorized`.
7. **T5 is a real counterexample.** No issue. Concrete pair `empty, Operation.install (Witness.mk 0)`; `hpv` constructed first (antecedent inhabited).
8. **No scope creep.** No issue. No value mutation, valid-wait, founding-event, sequent, cut, or broader calculus.
9. **Axioms clean.** No issue. Only `propext` for simp-heavy theorems; no user axioms.

## Agent verdicts

All nine items: **AFFIRMS (no action).** Codex confirms the slice's design discipline holds at every checkpoint, including the load-bearing distinction between `ValidIn S` (pre-state) and `ValidIn (apply S O)` (post-state) that gives the slice its content.

## Integration

**None.** The slice ships as written.

## Cross-references

- Slice source: `~/git/lean/LeanProofs/Admissibility/RetroactiveLegitimation.lean`.
- Charter: [`retroactive-legitimation-charter.md`](retroactive-legitimation-charter.md).
- Axis map: [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) (axis 3 = RetroactiveLegitimation).
- Sibling slice reviews: [`contraction-hinge-codex-review.md`](contraction-hinge-codex-review.md), [`maximal-calculus-codex-review-log.md`](maximal-calculus-codex-review-log.md).
- Codex calling discipline: `~/.claude/skills/codex-exec/SKILL.md`.
