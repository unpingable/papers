# Alloy probe: ContractionHinge substrate-shape test (result)

**Status:** spike complete 2026-06-03. Result note. Not doctrine.
**Plan provenance:** operator-locked B from `working/source-basis-discipline-synthesis.md`
**Spec:** `working/contraction_hinge_probe.als`
**Alloy run output:** `working/contraction_hinge_probe/` (receipt.json + per-probe solution files)

## Exportable keeper line

> **Standing-upgrade blocks self-originating authority.
> ContractionHinge blocks duplicated resource use.
> Same umbrella; distinct substrate; distinct relational vocabulary.**

Same suburb, different sewer line.

## Operator-locked scope

This was *not* an attempt to reproduce T2/T3's arithmetic proof in Alloy.
The question was narrower:

> Does the no-contraction refusal reduce to the same four-layer relational
> pattern as standing-upgrade (kernel + wrapper + derivation discipline +
> named invariant)?

If yes → compact reduction.
If no → document the additional apparatus required.
Bounded enumeration acceptable only as substrate-shape witness, not as
replacement proof.

## Raw results

| Probe                                          | Result      | Meaning                                                 |
|------------------------------------------------|-------------|---------------------------------------------------------|
| probe1_set_collapse_conflates_T1_and_T3        | SAT (1/1)   | Boolean encoding **cannot distinguish** T1 from T3.     |
| probe2_T3_analog_with_multiplicity             | UNSAT       | Multiplicity encoding **correctly blocks** T3-analog.   |
| probe3_legitimate_supply_multiplicity          | SAT (1/1)   | Legitimate one-to-one supply constructible (T1-analog). |
| probe4_contraction_enables_T3                  | SAT (1/1)   | Contraction-extended predicate licenses the bad move.   |

All four returned the predicted outcomes. The result that matters is
probe1's SAT: it is the substrate-mismatch witness.

## The load-bearing finding (probe 1)

**The standing-upgrade four-layer pattern cannot encode the ContractionHinge
question.**

Standing-upgrade primitives:

- `hasStanding: set Actor`
- `hasAdmissibleBasis: set Claim`
- `hasResolvedPrecedence: set Claim`

All `set`-valued. Element-wise boolean membership. No arithmetic, no
counting, no Int.

The ContractionHinge question is whether `[A] ⊢ A ⊗ A` is derivable. In
set-valued primitives:

- A claim with parts `{A}` (an atomic A) has the same set representation as
- A claim with parts `{A, A}` (an A⊗A composite), because **sets collapse
  duplicates**: `{A, A} = {A}`.

Probe 1 demonstrates this at the encoding-substrate level: two operations
with identical set-valued field configurations (`uses = A`, `parts = A`)
are both admissible under `admissibleBoolean`, yet semantically one is
T1-shape (legitimately producing A from a single A) and one is T3-shape
(illegitimately producing A⊗A from a single A). The encoding cannot
distinguish them; this is a fact about the substrate, not a theorem about
the artifact.

**The boolean-relational encoding cannot block T3 because it cannot
represent the question.** The encoding is not just inadequate; it is
referentially insufficient.

## The additional apparatus (probe 2 onward)

To make the contraction question expressible, the encoding required
primitives that the standing-upgrade probe never used:

- `count: one Int` — Int-valued occurrence count on every warrant-use
- `need.count <= have.count` — arithmetic comparison in the admissibility
  predicate
- `for 4 Int` — bounded Int scope flag at the `run` site
- A separate sig (`MUse`) to carry the warrant + count pair, because the
  set-valued relation could not encode it inline

This is **quantitative-relational** primitives, not boolean-relational.
Same family (relational logic), different vocabulary (counting vs
visibility).

Probe 2 confirmed that the new apparatus blocks the T3-analog (UNSAT).
Probe 3 confirmed it permits the legitimate T1-analog (SAT). Probe 4
mirrors ContractionHinge.lean's T3' — a separately-named
`admissibleWithContraction` predicate licenses the bad move, structurally
mirroring the Lean artifact's quarantine of `contr` inside `DerivableC`.

## Verdict — distinct family

The four-layer pattern from standing-upgrade does **not** reduce
ContractionHinge. The two specimens share metaphysics (both are forms of
disciplined premise production) but require **structurally distinct
relational substrates**:

| Specimen                       | Substrate primitive                              | Discipline expressed                                              |
|--------------------------------|--------------------------------------------------|-------------------------------------------------------------------|
| Standing-upgrade (temporal/source) | Boolean state predicates (`set Actor`, `set Claim`) | An actor's standing is *visible* to the gate or not — *source*-shaped. |
| ContractionHinge (multiplicity/resource) | Quantitative use counts (`Int`, `≤`)             | A warrant's occurrence count is *covered* by available count or not — *resource*-shaped. |

## The closed umbrella

The synthesis fork closes as predicted:

```
Disciplined premise production (umbrella)
├── Source/temporal discipline
│   - Specimens: AmendmentFragment, RetroactiveLegitimation,
│                standing-upgrade-block
│   - Substrate: boolean state predicates
│   - Blocks: self-originating authority — a premise produced by the
│             operation it authorizes
│   - Named architecture: BasisDerivation.revoked_never_admissible,
│                          StandingDerivation.revoked_standing_never_standing
│                          (closed 2026-06-03)
│
└── Multiplicity/resource discipline
    - Specimens: ContractionHinge
    - Substrate: quantitative use counts
    - Blocks: duplicated resource use — a premise spent more times than
              it was granted
    - Named architecture: T2 soundness (v C ≤ sum Γ), T3 corollary,
                          T3' contrast specimen
```

This is not synthesis-by-unification. It is synthesis-by-taxonomy: the
umbrella names a *family*, not a *layer*. Both species share the
"premise-production discipline" character but operate on different
relational substrates.

## What this is NOT

- Not a proof of T3. ContractionHinge.lean's T3 is the proof. This probe
  only witnesses substrate shape via bounded enumeration.
- Not a reduction of multiplicity to standing-upgrade. The probe
  positively rules out the reduction.
- Not authorization to build a Lean module for multiplicity discipline —
  ContractionHinge.lean already exists and is named architecture.
- Not authorization to build out the "disciplined premise production"
  umbrella as a third Lean module. The umbrella is a *taxonomic claim*
  about the two existing specimens; it is not its own object.
- Not adoption of Alloy as a calculus companion. Two probes have now run,
  each paying for itself in different ways: probe 1 (standing-upgrade)
  surfaced the implicit invariant; probe 2 (this one) confirmed the
  taxonomic split. Both bounded; both single-shot. No cathedral.

## What this IS

- A bounded probe ran, classified, and written up.
- Encoding-substrate witness that ContractionHinge cannot be encoded in
  standing-upgrade's primitive vocabulary.
- Closure of the source-basis-discipline synthesis fork: the umbrella is
  a *family of two species*, not a single common layer.
- The exportable taxonomy: source/temporal discipline + multiplicity/resource
  discipline, both species of disciplined premise production.
- A second confirmation that Alloy is useful as a substrate-shape
  diagnostic but not as a calculus companion. Two spikes, two findings,
  two checked-off probes. No ongoing adoption.

## Adoption verdict (cumulative across both spikes)

Two probes complete:

1. **Standing-upgrade probe (2026-06-03):** found the implicit standing-grant
   invariant → triggered Lean-side closure (blocker 3).
2. **ContractionHinge probe (2026-06-03):** confirmed the substrate
   asymmetry → closed the synthesis fork in favor of the umbrella reading.

Both probes were:
- Bounded (single .als file each, no project structure)
- Disposable (no AlloyAdmissibility/ directory, no Phase2/, no roadmap)
- Honest about their limitations (bounded enumeration witnesses substrate
  shape, not theorems)

**Alloy earns the description "useful for substrate-shape diagnostics."**
It does not earn adoption as a calculus-companion proof tool. If a third
spike is justified later, that's evidence for adoption; until then,
Columbus stays home.

## Cross-references

- Sibling probe: [`alloy-spike-standing-upgrade-result.md`](alloy-spike-standing-upgrade-result.md)
- Spec: [`contraction_hinge_probe.als`](contraction_hinge_probe.als)
- Alloy output: `contraction_hinge_probe/`
- Target artifact: `~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean`
- Synthesis fork (now closed): [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Sibling working notes: [`authorization-laundering-arc.md`](authorization-laundering-arc.md),
  [`boundary-by-asymmetry-pattern.md`](boundary-by-asymmetry-pattern.md)
- Arc index: [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) §
  "Arc closure 2026-06-03"
- Multiplicity/resource seed (sibling register, parked):
  [`multiplicity-resource-register-seed.md`](multiplicity-resource-register-seed.md)
- Downstream classification:
  [`maximal-calculus-taxonomy-classification.md`](maximal-calculus-taxonomy-classification.md),
  [`amendment-cut-case-classification.md`](amendment-cut-case-classification.md)
