# Charter — Slice 1: No Authorization from the Future

**Status:** Substrate / charter, agent-filed 2026-06-02. NOT an
execution packet for Claude Code. This file captures the slice's
shape so it can be fed verbatim to Claude-web (the cabinet's
charter-shaping role) without the substrate being trapped in a
chat transcript.

Axis 3 of the [maximal-calculus axis map](maximal-calculus-refused-map.md),
working name **RetroactiveLegitimation**. Third in the
immediate-research program — behind
[AmendmentFragment](../../lean/LeanProofs/Admissibility/AmendmentFragment.lean)
(axis 1, shipped) and
[ContractionHinge](../../lean/LeanProofs/Admissibility/ContractionHinge.lean)
(axis 2, shipped). The survival gate from the map: *"if those three
survive, then it becomes fair to ask what the common calculus
actually is."* This slice tests whether RetroactiveLegitimation
survives as its own fragment or collapses into AmendmentFragment.

## The keeper sentence

> A later-valid witness may explain the result, but it cannot
> authorize the operation that produced the result.

## Purpose

Show that a witness valid only *after* an operation cannot
authorize that operation.

## The load-bearing distinction (four judgments)

The slice exists to separate four judgments that get conflated
when retroactive legitimation slides in:

- **Prediction.** *"Given S and O, what is S′?"* Forward, with
  whatever evidence is available pre-O.
- **Explanation.** *"Given S′, why is it this way?"* Backward,
  with evidence in S′.
- **Validation.** *"Given S′ and a property P, does P hold?"*
  Sideways, evidence in S′.
- **Authorization.** *"Was O admissible in S?"* Anchored at S,
  with evidence in S.

Retroactive legitimation is the laundering move that lets
explanation or validation get read backward as authorization.
The slice's content is showing the boundary at which that read
becomes illegal.

## Objects

Minimal vocabulary:

```text
State
Operation
apply : State → Operation → State
Witness
ValidIn : State → Operation → Witness → Prop
AuthorizedIn : State → Operation → Prop
```

## Positive

A pre-state valid witness licenses the operation:

```text
∀ S O W, ValidIn S O W → AuthorizedIn S O
```

(Or whichever shape AuthorizedIn ends up taking — the constraint
is that the witness's index is `S`, not `apply S O`.)

## Negative headline

> Post-state validity does not retroactively authorize the
> transition that made it valid.

## Refusal — the load-bearing existential

```text
∃ S O W,
  ValidIn (apply S O) O W ∧ ¬ ValidIn S O W ∧
  ¬ AuthorizedIn S O
```

The first conjunct: post-state validity holds. The second: pre-
state validity fails. The third: authorization fails. Together,
post-state-only evidence cannot rescue authorization.

## Guards

Strict scope, per the operator:

- Do **not** define `AuthorizedIn` using post-state validity. That
  would bake the result into the definition; the boundary
  disappears.
- Do **not** bake refusal into the constructor. The negative
  result must follow from the *shape* of `AuthorizedIn`, not from
  a `¬` in its premises.
- Do **not** generalize into protocol waiting (`O₁ → wait → O₂`).
  Receipt-gated patterns are axis 5; out of scope here.
- Do **not** touch value mutation. That is axis 4; out of scope.
- Do **not** open founding events / exceptional substitution.
  Axis 6; out of scope.
- Do **not** let the slice become *"future evidence is useless."*
  That would be false (and false in a productive-looking way).
  The boundary is narrower:

  > Later evidence can support later judgments; it cannot serve
  > as the missing precondition for its own enabling transition.

## Why this is not just AmendmentFragment again

AmendmentFragment refuses case #3 (self-certifying amendment):
*the act installs the authority that judges it.* The witness's
type is anchored at `S.policy`; the type rejects evidence at
`S'.policy`.

RetroactiveLegitimation attacks the same invariant *from the
other side*: the witness is *made valid by* the post-state, but
that later validity is not pre-state authorization. The witness
exists in `S'`; it does not authorize the act that produced `S'`.
Sharper: the witness is *post-state-valid*, not
*pre-state-authorizing*. This is a different shape:

- AmendmentFragment: *the authority's grammar itself is new in S′
  — the policy mutates, and the act installs the rule that would
  judge it.*
- RetroactiveLegitimation: *the grammar is fixed; the witness
  record changes — the post-state contains a valid witness, but
  the act installed it, so it cannot retroactively license the
  act.*

If the executor reduces this to "AmendmentFragment with extra
prose," stop. The whole point of the slice is to prove the
neighboring distinction has its own boundary. If it does not — if
the slice collapses constructively into AmendmentFragment — that
is a finding worth reporting; it would falsify the plural
posture's case for this axis. But the collapse must be *proven*,
not assumed by drafting the wrong type signature.

## Sibling fragments — for cross-fragment seam awareness

The axis-3 work is part of the three-fragment survival test in
the [axis map](maximal-calculus-refused-map.md):

- Axis 1: AmendmentFragment — pre-state authorization / standing
  mutation / self-certification refusal.
- Axis 2: ContractionHinge — occurrence accounting / structural
  collapse / warrant duplication refusal.
- Axis 3: RetroactiveLegitimation — post-state witness refusal /
  "true later" ≠ "authorized then."

If all three survive as distinct fragments, the question of the
common calculus opens. Until then, no synthesis.

## Stop conditions

- This file is NOT an execution packet. Claude Code should not
  open a Lean file from this. The next move is Claude-web, which
  shapes the charter further (judgment-shape choices, type
  signatures, what `AuthorizedIn` should look like) before a
  later execution slice goes to Claude Code.
- If Claude Code is invoked on this slice, the trigger should be
  a follow-up execution packet (structured like the
  ContractionHinge packet), not this charter.

## Cross-references

- [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) — axis map;
  axis 3 entry links here.
- [`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md) —
  upstream substrate (the §"Connection" reading is adjacent to
  this slice).
- [`maximal-calculus-discharge-connection.md`](maximal-calculus-discharge-connection.md) —
  axis-1 sibling note; the discharge essay's *true-but-inadmissible*
  cut is structurally adjacent to this slice's *true-later-but-
  not-authorized-then* cut.
- [[project-continuous-admissibility-discharge]] — adjacent doctrine.
- [[project-reflective-adoption-parked]] — adjacent shape ("later
  local adoption ≠ origin legitimation") at the human-facing layer.
