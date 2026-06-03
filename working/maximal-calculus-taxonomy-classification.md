# Maximal calculus — taxonomy classification pass

**Status:** classification pass, 2026-06-03. Not promotion. Not new axis.
**Filed under:** operator-locked D (case work resumed under the closed
synthesis fork from `working/source-basis-discipline-synthesis.md` and
`working/contraction-hinge-probe-result.md`).
**Hard rule observed:** no new axis promoted unless a specimen refuses
classification under both source/temporal and multiplicity/resource
discipline.

## Method

Apply the **disciplined premise production** taxonomy as a *classifier* to
the open cases in `working/maximal-calculus-amendment-cut.md` and
`working/maximal-calculus-forcing-cases.md`. For each case, ask:

- **Source/temporal discipline?** — does the refusal block self-originating
  authority (a premise produced by the operation that depends on it)?
- **Multiplicity/resource discipline?** — does the refusal block duplicated
  resource use (a premise spent more times than granted)?
- **Refusal of classification?** — neither shape fits naturally.

The classifier is *descriptive*, not generative. Cases get tagged with the
species that names their refusal shape. Cases that refuse both tags
trigger the hard rule and force a re-look. Cases that fit cleanly do not
generate new axes; they confirm the register's structural locus.

## Per-case classification (amendment-cut register)

| Case                                                | Species              | Reasoning                                                                                                                                                              |
|-----------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| #1 — value-function amendment (self-reach)          | source/temporal      | The mutating value function judges its own installation. Authority (post-state value function) produced by the operation. Direct (A1) violation shape.                 |
| #2 — retroactive legitimation (backward-reach)      | source/temporal      | Sink-relative retyping reads earlier states by post-state lights. RetroactiveLegitimation.lean is the formal specimen. Boolean visibility of "valid-in-S vs valid-in-S′". |
| #3 — self-certifying amendment (load-bearing)       | source/temporal      | The case the synthesis arc was driven by. (A1) directly addresses it. Standing-upgrade is its near-sibling; AmendmentFragment.lean is its specimen.                    |
| #4 — standing mutation (first-tractable)            | source/temporal      | Subcase of pre-authorized mutation. Standing-upgrade-block specimen + the now-named `revoked_standing_never_standing` obligation are the architecture.                  |
| #5 — crisis-mode value substitution (self-reach)    | source/temporal      | "Substitute the evaluator under crisis." Admissibility iff substitution admissible under pre-crisis evaluator. Same well-foundedness shape; same species.              |
| #6 — reflective adoption without origin legitimation | source/temporal      | Post-adoption receipt cannot create origin authority. Backward-reach sibling of #2 at human-facing layer. Same boundary-by-asymmetry shape.                            |

## Per-case classification (candidate maximal cases)

The non-pruning verdict in the amendment-cut note left these as candidate
maximal cases pending the reduction discriminator:

| Candidate                          | Species              | Reasoning                                                                                                                                  |
|------------------------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Evaluator mutation                 | source/temporal      | Mutating *who/what* judges. The new evaluator was produced by the operation it now judges. Same shape as #1.                              |
| Value location mutation            | source/temporal      | Mutating *where* the value field lives in state. The new location is post-state; pre-state evaluator cannot see it. Boolean visibility.    |
| Retroactivity semantics mutation   | source/temporal      | Meta-rule about what's retroactive. Meta-level instance of #2; same backward-reach pattern.                                                |
| Slice-boundary mutation            | source/temporal      | Mutating *what counts as a slice*. About premise visibility, not premise count. Source/temporal.                                          |
| Receipt/witness-definition mutation | source/temporal      | Mutating *who counts as a witness*. Classic boundary-by-asymmetry instance. Source/temporal.                                              |

## Verdict — register is single-species

**Every case in the amendment-cut register classifies as source/temporal
discipline.** No specimen refuses classification. No new axis promoted.

The hard rule from the operator is observed: nothing forces a third
species. The taxonomy works as a classifier on this register.

## What this clarifies

1. **The amendment-cut register's structural locus is source/temporal
   discipline.** It is not coincidental that all cases fit one species —
   the register is about *authority installation* and *policy mutation*,
   which are fundamentally about premise production over time. Multiplicity/
   resource concerns (occurrence counting, linear consumption, contraction)
   live in a different register.

2. **Multiplicity/resource discipline has its own (currently implicit)
   register.** ContractionHinge is the only known specimen. Whether other
   instances exist is an open question, but they do *not* live in the
   amendment-cut register. If they exist as case-work artifacts, they
   would constitute a parallel forcing-case register on the multiplicity
   axis.

3. **The four-layer pattern from standing-upgrade should apply cleanly to
   every amendment-cut case work** — because they are all source/temporal
   discipline instances, the standing-upgrade probe's substrate (boolean
   state predicates + named premise-production invariants) is the right
   shape for any Lean specimen built from this register. Multiplicity-
   substrate apparatus (Int, counts, ≤) should NOT be required for any
   amendment-cut specimen.

## What this does NOT do

- Does NOT promote a new axis. The taxonomy classifies; it does not
  enumerate beyond two species.
- Does NOT propose a new register. Multiplicity/resource discipline may
  have one, but inventing it now is out of scope (forcing-case discipline
  applies — wait for instances).
- Does NOT pre-commit to building Lean specimens for any of these cases.
  Per the amendment-cut note's "next moves (candidate, not committed)"
  — that decision sits with the operator.
- Does NOT rename or rework anything in the existing register. The
  classification is a *tag*, not a *replacement*.
- Does NOT promote the taxonomy to paper form. Per operator instruction:
  capture the taxonomy, let case work stress it, do not write the
  paper-shaped object yet.

## Pickup point

The pickup point in the amendment-cut note (case #4 standing mutation as
first-tractable, plus the reduction-discriminator open for each candidate
maximal) is now augmented by:

> Every amendment-cut case (registered or candidate) classifies as
> source/temporal discipline. Lean specimens built from this register
> should use the standing-upgrade four-layer substrate (boolean state
> predicates + named premise-production invariants). The recently-mounted
> `revoked_standing_never_standing` obligation is the structural template
> for the obligations these specimens will carry.

The classifier observation is itself a useful constraint on future
case-work scope: it tells specimen builders what substrate to use and
warns against accidentally importing multiplicity-discipline apparatus
where it doesn't belong.

## Substrate lint (operator-issued, 2026-06-03)

The classifier doubles as a substrate-correctness lint for specimens
built under either species. Wrong-substrate imports are now flaggable by
name.

**For source/temporal specimens (amendment-cut family):**

```
Expected vocabulary:
  pre/post state
  standing / basis visibility
  revocation
  source independence
  retroactivity blocking
  named premise-production invariant

Suspicious vocabulary:
  counts
  resource budgets
  multiplicity
  consumption accounting
  linear availability
```

**For multiplicity/resource specimens (ContractionHinge family):**
invert. Suspicious vocabulary becomes expected; expected vocabulary
becomes suspicious.

A specimen that needs *both* vocabularies has likely either (a) crossed
a species boundary without naming the crossing, or (b) surfaced a
genuinely new category — at which point the hard rule fires and forces
a review.

## The frame line (worth keeping)

> **The amendment-cut register is not maximal-calculus-general. It is
> source/temporal-specific.**

Prevents the category error of dragging arithmetic substrate into an
amendment specimen because ContractionHinge made counting feel newly
important. Wrong pipe.

## Cross-references

- Synthesis fork (closed): [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Probe results: [`alloy-spike-standing-upgrade-result.md`](alloy-spike-standing-upgrade-result.md),
  [`contraction-hinge-probe-result.md`](contraction-hinge-probe-result.md)
- Amendment cut (the case substrate): [`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md)
- Forcing-case register: [`maximal-calculus-forcing-cases.md`](maximal-calculus-forcing-cases.md)
- Named Lean architecture for the species:
  - Source/temporal: `LeanProofs/Admissibility/Derivation.lean`
    (`BasisDerivation.revoked_never_admissible`,
    `StandingDerivation.revoked_standing_never_standing`,
    `revoked_basis_never_authorized`,
    `revoked_standing_never_authorized`)
  - Multiplicity/resource: `LeanProofs/Admissibility/ContractionHinge.lean`
    (T2, T3, T3')
