# Keystone question — no-lift and no-compose

**Status:** verdict note (2026-06-01, revised same day). Multi-model
convergence (ChatGPT + Claude) on the schema; verdict subsequently
corrected by Claude-web after drafting the section-level Lean falsified
the "non-reconstructability is the keystone" framing. The corrected
verdict is now load-bearing; the earlier image-obstruction framing is
preserved below as audit trail, not as the live position.

## Correction summary (2026-06-01 revision)

- **Earlier verdict (superseded):** the keystone is "boundary-witness
  obstruction" — a weak object exists without the witness, the strong
  object requires it, the witness is irreducible.
- **Why earlier verdict was wrong:** the formal content of "irreducible
  witness" is the *section-level* statement `¬ HasSection`. Drafting the
  Lean revealed that under the classical substrate
  (`Classical.byContradiction` in `SafetyBridge.lean`),
  `HasSection ↔ surjective`, so `¬ HasSection ↔ BoundaryObstruction`.
  Section framing is **clarity, not strength** — it does not
  distinguish the bridge/merge gates from arbitrary non-surjective
  maps like `Nat.succ` (which also lacks a section).
- **Corrected verdict:** the keystone's content is **value-sound
  gating, per-axis**. In both axes, strong-membership entails a
  defended-value floor that the corresponding operation respects;
  `Nat.succ` gates nothing value-relevant. That soundness IS the
  cross-axis structure — and it does NOT lift to one clean schema
  field because the value floor attaches to different operations per
  axis (transition vs. merge). Forcing it would repeat the arity /
  `Obs` distortion already rejected twice.
- **Form of closure:** the keystone is **a schema with value-sound
  instantiations**, not a calculus with a load-bearing abstract
  keystone theorem. Section framing kept in `BoundaryWitness.lean` as
  exposition (`HasSection`, `axis1_no_step_section`,
  `boundaryObstruction_implies_no_section`) with annotations that it
  is clarity, not strength.

The rest of this note is structured to preserve the earlier shape
(slogan / Claim A vs. B) for audit, with the corrected verdict
overlaid where it matters.

## Slogan under test

> "No-lift is the n=1 base case of no-compose."

## Verdict

- **Claim A (literal base-case): REJECTED.** Making sequential no-lift a special
  case of merge no-compose requires bending `merge` into a unary operation
  (`merge a ε = a` for some neutral `ε`) so that a single trajectory becomes a
  degenerate merge. Merge is irreducibly binary — its whole content is the
  *joint* condition over two branches (joint usage, joint freshness, owner
  compatibility). A unary merge has no joint condition, so the construction
  discards exactly the thing Axis 2 is about. Elegant, forced, cursed. Reject.

- **Claim B (shared shape exists): ACCEPTED at the schema level.** Both axes
  instantiate the boundary-witness obstruction schema without distorting their
  definitions. The Axis 1 instantiation is already green in the substrate.

- **Claim B (the shape carries the keystone's content): REJECTED on revision.**
  The image-level statement "a non-surjective map has something outside its
  image" is a tautology; the section-level statement "no uniform reconstruction"
  is equivalent classically — both fail to distinguish the bridge / merge
  gates from `Nat.succ`. The schema is shape, not content.

- **Mere analogy: still RULED OUT.** Not analogy. There IS a real shared
  structure — but it is not the obstruction schema. It is value-sound gating.

- **Corrected form of closure (live position).** The keystone is **a schema
  shape (boundary-witness obstruction) plus per-axis value-sound gating
  theorems** — the soundness is what makes the gates non-trivial, and it does
  not lift to one schema field because the value floor attaches to different
  operations per axis. The honest structure:

  - **Axis 1:** bridge witness gates *transition* value-soundness
    (`SafetyEnv.preserves`: `bridge ⟹ value non-decrease over transition`).
  - **Axis 2:** `MergeOk` gates *reconciliation* value-soundness
    (the `*_restores` family: `MergeOk ⟹ merged value/basis restoration`).

  Different operations, parallel structure, no forced unification. *Not every
  theorem arrives wearing a cape* — the worse hat is the true hat.

## The schema — boundary-witness obstruction (shape only)

```
Weak     W            -- constructible without the boundary witness
Strong   S            -- carries the boundary witness as a field
forget   f : S → W    -- drops the witness
witness  the data in S but not in W
Obstruction:  ∃ w : W, ¬ ∃ s : S, f s = w
```

**Earlier framing (superseded):** the "irreducible information" clause is
what makes this load-bearing.

**Corrected framing:** the obstruction clause is trivial as stated, and the
section-level rephrasing (`¬ HasSection`) is equivalent classically — also
trivial. Both fail to distinguish the bridge / merge gates from arbitrary
non-surjective maps. So this schema is *shape*, used to type the two axes
against a shared signature for paper exposition; it is not the content. The
content is value-soundness of the gates, articulated next.

## The content — value-sound gating per-axis

In both axes, the strong-membership predicate entails a defended-value
floor that the corresponding operation respects. This is what
distinguishes the bridge / merge gates from a contentless map like
`Nat.succ` (which is non-surjective but gates nothing value-relevant).

### Axis 1: bridge witness gates transition value-soundness

```
Strong family:        SafeStep / BridgedTraj
Gate witness:         bridge : σ → α → Prop
Soundness theorem:    SafetyEnv.preserves
                      (bridge s a ⟹ value s ≤ value (run s a))
Atomic statement:     SafeStep.toAuthStep drops `bridged : Prop`,
                      so the strong family is a strict sub-family of
                      the weak (witness GATES, does not ENRICH).
```

The bridge witness is what makes a `SafeStep` value-sound for the
transition; `AuthStep` carries no such guarantee. The gating IS the
content.

### Axis 2: `MergeOk` gates reconciliation value-soundness

```
Strong family:        locally bridged branches + MergeOk witness
Gate witness:         MergeOk (per-slice: BudgetMergeOk, StaleMergeOk,
                                          ConflictMergeOk)
Soundness theorem:    *_restores family (value layer + basis layer)
                      (MergeOk p a b ⟹ merged endpoint admissible at
                       the slice's layer)
Iff characterization: per-slice (*_iff_admissible); see
                      ParameterizedMerge.lean's necessity verdict for
                      the layer-by-layer schema.
```

`MergeOk` is what makes a merge value-sound for the reconciliation
operation; locally bridged branches alone do not determine merge
admissibility. Same gating pattern as Axis 1, different operation.

### Why this doesn't lift to one schema field

The value floor attaches to different operations per axis (transition
vs. merge). Forcing it into a single `Soundness : ...` field on
`ForgetfulWitness` would require either (a) parametrizing by the
operation (a per-axis layer indicator on the frame), or (b) collapsing
the two operations into one abstract "step." Both are the same arity /
`Obs` distortion the Axis 2 work rejected twice. **The soundness stays
per-axis. The schema stays shape-only.**

## Axis 1 instantiation — ALREADY GREEN in the substrate

This half is not new work. `SafetyBridge.lean` already carries it:

```
W        = AuthStep E s            -- authorized step, no bridge field
S        = SafeStep E s            -- authorized + `bridged : E.bridge s act`
f        = SafeStep.toAuthStep     -- drops the bridge witness
witness  = the `bridged` field (bridge evidence)
```

- Forgetful map: `SafeStep.toAuthStep` (and at the trajectory layer,
  `BridgedTraj.toAuthorizedTraj`). Real, in-substrate.
- Non-reconstructability: `bridge` is a separate predicate the kernel does not
  constrain (the Frontier-1 wound). An `AuthStep` does not determine whether its
  action is bridged — that is the definition of `AuthorizationBridgeGap`.
- Obstruction theorem (the schema's `∃ w, ¬ InImage f w`):
  **`gap_blocks_safeStep_lift`** —
  `∃ (s) (x : AuthStep E s), ¬ ∃ (h : SafeStep E s), h.toAuthStep = x`.
  Atomic form: `no_safeStep_for_unbridged_authStep`.
- The substrate even names the doctrinal reading: *"Loop Capture is precisely an
  authorized trajectory that does not lift to a bridged one"* — and
  `HasForgetfulSection` is the negation the gap obstructs.

So Axis 1 instantiates the schema with zero distortion and zero new Lean.

## Axis 2 instantiation — the negative keepers ARE the obstruction

```
W        = a pair of locally bridged branches:
           (BridgedTraj E s sA) × (BridgedTraj E s sB)
S        = that pair PLUS a merge-admissibility witness:
           ... × MergeOk p sA sB
f        = drop the MergeOk witness
witness  = MergeOk (joint-resource ∧ freshness-basis ∧ policy, per slice)
```

- Non-reconstructability: `MergeOk` is a *joint* condition. Two local
  `BridgedTraj` witnesses certify each branch against its own local scope; they
  do not determine joint usage (Slice 0), joint freshness at reconciliation time
  (Slice 1), or owner compatibility (Slice 2). This is exactly the per-slice
  "scope insufficiency" already proven — the local witnesses cannot compute the
  joint one.
- Obstruction (the schema's out-of-image witness): the bust pairs already
  proven —
  `locally_bridged_branches_can_merge_to_global_bust` (6+6 > 10, ¬BudgetMergeOk),
  `locally_bridged_branches_can_merge_with_stale_evidence` (t=12 > horizon),
  `locally_bridged_fragments_can_merge_to_value_loss` (incompatible owners).
  Each is a weak object (two bridged branches) for which no strong lift exists
  (no `MergeOk` witness can be supplied), i.e. outside the forgetful image.

The Axis 2 obstruction content is done at the instance level. What is missing is
re-expressing it in the schema's forgetful-map shape (define the paired strong
object and its forgetful map), so the two axes visibly plug into one schema.

## Closure inventory — what is shipped and what is content

Originally framed as a "gap list to close the Axes 1–2 calculus." Re-cast under
the corrected verdict: items 1–5 are *exposition* (schema + image-level
instantiations), items 6–7 are *content* (per-axis value-sound gating), item 8
is *scope* (paper-level).

**Schema / exposition layer (closed):**

1. **Axis 1 image obstruction.** DONE — pre-existing
   `gap_blocks_safeStep_lift` / `no_safeStep_for_unbridged_authStep`.
2. **Schema definitions.** DONE — `ForgetfulWitness` / `InImage` /
   `BoundaryObstruction` in `BoundaryWitness.lean`. Tautological by design;
   shared signature for paper exposition.
3. **Axis 1 in schema shape.** DONE — `axis1_boundary_obstruction` (env-level)
   and `axis1_no_step_section` (pointwise atomic).
4. **Axis 2 forgetful map.** DONE — `WeakBudgetBranches` /
   `StrongBudgetBranches` / `forgetBudget` in `BoundaryWitness.lean`.
5. **Axis 2 in schema shape.** DONE — `axis2_budget_boundary_obstruction`
   (BudgetMerge specimen).
   *Section-level rephrasing.* DONE — `HasSection`,
   `boundaryObstruction_implies_no_section`, with annotations that this is
   clarity, not strength (classically equivalent to the image form).

**Content / value-sound gating (per-axis; lives outside `BoundaryWitness.lean`):**

6. **Axis 1 value-soundness.** DONE in substrate — `SafetyEnv.preserves`
   (`SafetyBridge.lean`); bridge witness gates transition value non-decrease.
7. **Axis 2 value-soundness.** DONE per-slice — the `*_restores` family in
   `ParameterizedMerge.lean` (`MergeRestoresValue`, `MergeRestoresBasis`),
   instantiated for all three slices at the appropriate per-slice layer
   (Budget/Conflict at value, Stale at basis). Necessity layer also
   formalized (`MergeOkNecessaryAtValue`, `MergeOkNecessaryAtBasis`) with
   per-slice instantiations; verdict there is *schema not generic theorem*,
   composing exactly with this note's corrected verdict.

**Scope fence (paper-shaped):**

8. **Axis 3 (self-amendment) is OUT.** It mutates the evaluator, not the
   evaluated transition/composition. Axes 1–2 are "evaluation evidence fails
   to survive transition/composition"; that is the closed shape. State the
   fence explicitly in the paper draft.

All of items 1–7 are landed in the Lean substrate; none of this is Axis 3.
The calculus is the per-axis value-sound gating, not the schema.

## Decision criterion (revised)

Original (ChatGPT's): *If both Axis 1 and Axis 2 instantiate the schema
without distorting their definitions, the calculus closes over Axes 1–2.*

Met for schema-shape (image obstruction); but the schema being met is the
worse hat. Revised criterion: **If both axes carry value-sound gating
under the same shape, with the soundness theorems proven per-axis without
distorting their definitions, the calculus closes as a schema with
value-sound instantiations.**

**Met.** Axis 1's `SafetyEnv.preserves` and Axis 2's `*_restores` family
deliver value-sound gating in both axes; the cross-axis schema (image
obstruction + section equivalent) types both against the same shape. The
calculus is closed in the sense of *schema-with-instantiations*, not in
the sense of *one calculus theorem*.

## Title implication (revised)

Original candidate (superseded): **"Boundary Witnesses for Admissible
Transition and Composition."** Risk: reads as a promise of an abstract-
map theorem that, on inspection, is a tautology. The "boundary witness"
framing makes the obstruction sound like the content; it isn't.

Better candidates (value-soundness foregrounded):

- **Value-Sound Gates for Authorization and Composition**
- **Admissibility as Value-Sound Gating**
- **Authorization, Composition, and Value-Sound Witnesses**
- **Witness-Gated Admissibility for Transition and Composition**

The title should foreground that the witness's role is to make the gated
operation value-sound, not to be unreconstructable in some abstract
sense. Ugly? A little. But less likely to promise a cape theorem the
paper doesn't have. Decide at draft time.

## What did NOT change

- The boundary-witness obstruction schema is still useful as
  exposition — it names the shared shape so the paper can talk about
  "two value-sound gates with the same obstruction signature" without
  conflating signature with content.
- The keystone work in `BoundaryWitness.lean` stays. `HasSection` and
  `axis1_no_step_section` are kept as expository clarity (with the
  annotations marking them so).
- The Axis 2 calculus body in `ParameterizedMerge.lean` is unchanged
  by this revision — its layer-aware schema (value / basis) and
  necessity verdict (schema not theorem) compose cleanly with the
  corrected keystone framing.
- Axis 3 remains out of scope.

## Audit trail — what the correction overruled

The earlier framing treated "non-reconstructability of the boundary
witness" as the keystone's content, with `BoundaryObstruction F`
formalizing it. Drafting the section-level Lean falsified this: the
section-level rephrasing is classically equivalent to the image-level
one, so neither carries content beyond non-surjectivity, which is too
weak (`Nat.succ` has it). The corrected verdict identifies value-sound
gating as the content; this is what the schema's instantiations
*always already* needed to be — the earlier framing simply didn't say
it out loud.
