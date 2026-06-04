# BoundaryWitness sub-audit — self-originating witness-definition

**Status:** bounded sub-audit, 2026-06-03. Read-only. No build.
**Question:** does `BoundaryWitness.lean` already block the self-
originating witness-definition case, or is there a missing named
invariant?
**Scope:** `~/git/lean/LeanProofs/Admissibility/BoundaryWitness.lean`
read in full + cited imports (`SafetyBridge.lean`, `BudgetMerge.lean`)
sampled only as needed for type references.

## What BoundaryWitness.lean actually covers

The module ships a *static* obstruction schema:

- `ForgetfulWitness`: a triple `(Weak, Strong, forget : Strong → Weak)`.
- `BoundaryObstruction F`: some `Weak` object has no `Strong` preimage.
- Two wired instantiations:
  - **Axis 1:** `SafeStep ↠ AuthStep` (drops `bridged`); obstruction =
    unbridged authorized step.
  - **Axis 2:** `StrongBudgetBranches ↠ WeakBudgetBranches` (drops
    `BudgetMergeOk`); obstruction = 6+6>10 joint-margin violation.

In both, the witness definition is **fixed at the type level**
(`E.bridge`, `BudgetMergeOk`). The module proves that *for a fixed env*,
some weak objects cannot be lifted to strong ones — i.e., the witness
is real evidence, not free to fabricate.

The module's own header is explicit: this is expository schema-shape,
not the cross-axis content. The actual gating content is per-axis (in
`SafetyBridge.lean` and `ParameterizedMerge.lean`).

## What it does NOT cover

The self-originating witness-definition mutation is:

> An operation O changes the witness *definition* (the field of the env
> that says "what counts as a valid bridge / merge / receipt") to one
> under which O's own claimed witness is admissible.

BoundaryWitness.lean models the env `E` (and `BudgetMergeOk`, etc.) as
**fixed parameters** of the types it defines. It does not model
mid-trajectory mutation of `E.bridge` or of `BudgetMergeOk`. There is
no theorem of the form "an operation that installs `E′` cannot use
`E′.bridge` as its bridge witness."

This is structurally identical to the **env-change ghost strut** from
the prior case-classification pass. The bridge predicate (or any
witness-defining field) lives in the env; mutating it is env mutation;
self-originating env mutation is the same shape as the evaluator
mutation candidate.

## Classification

**Bucket (2) — covered by existing pattern but unnamed.**

- The pattern matches the **meta / env-change ghost strut** filed under
  side observations in
  [`amendment-cut-case-classification.md`](amendment-cut-case-classification.md).
- BoundaryWitness.lean is **not** the named architecture that blocks
  this — it blocks static non-reconstructability, not dynamic
  redefinition.
- No *new* ghost strut surfaced. The existing filed candidate covers
  this instantiation as well as evaluator / slice-boundary /
  retroactivity-semantics mutations.

The bucket is (2), not (1) — because no Lean theorem specifically blocks
self-originating witness-definition mutation, and the relevant invariant
(env-change (A1)) is itself an unmounted candidate.

The bucket is (2), not (3) — because no *new* ghost strut is surfaced.
This is the env-change ghost strut at a different altitude.

The bucket is (2), not (4) — because no separate forcing case is needed.
A forcing case at the env-change altitude (whichever altitude it
surfaces at — value, evaluator, witness predicate) would close the
same architectural gap for all three.

## What this audit does NOT do

- Does not propose building `ValueDerivation`.
- Does not propose building `EnvDerivation` / `EnvChangeRule`.
- Does not edit `BoundaryWitness.lean` or any sibling.
- Does not open a new taxonomy or sub-axis.
- Does not promote witness-definition mutation as a distinct candidate
  case.

## What this audit DOES surface (filed, not opened)

One sub-observation worth recording without acting on:

- Witness-definition mutation belongs to the env-change ghost strut
  family alongside evaluator / slice-boundary / retroactivity-semantics
  mutation.
- If a forcing case arrives at any of those altitudes, the corresponding
  closure (the env-change analog of `revoked_standing_never_standing`)
  would discharge the architectural gap for all of them in one move.
- Until then: candidate filed, work not opened.

## Cross-references

- `~/git/lean/LeanProofs/Admissibility/BoundaryWitness.lean` (audited)
- Prior case classification (filed the env-change ghost strut):
  [`amendment-cut-case-classification.md`](amendment-cut-case-classification.md)
- Closed taxonomy (the substrate lint these gaps respect):
  [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Arc index: [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) §
  "Arc closure 2026-06-03"
- Sibling classifier pass:
  [`maximal-calculus-taxonomy-classification.md`](maximal-calculus-taxonomy-classification.md)
