# Amendment-cut case-work — under closed taxonomy

**Status:** case-work pass, 2026-06-03. Classifications and reduction
notes only. NOT a synthesis essay. NOT new-axis promotion.
**Operator constraints (locked):**

- Treat the amendment-cut register as source/temporal unless a specimen
  actively refuses classification.
- Use boolean state predicates + named premise-production invariants.
- No Int / counts / budgets / consumption / linear availability.
- No new axis unless a case cannot be honestly modeled as source/temporal.
- **Brake:** if expressible as revoked / stale / self-originating /
  retroactive / independent-basis failure, classify source/temporal and
  stop.

**Output format per case (6 fields):**
1. Mutation being tested
2. Source/temporal failure mode (named pattern)
3. Relevant named invariant / missing invariant
4. Minimal Lean specimen candidate (if any)
5. Reduces to existing standing/basis pattern?
6. Do-not-promote notes

The brake fires on every case below. None refused source/temporal
classification. No new axis triggered.

---

## Registered cases

### Case #1 — value-function amendment (self-reach)

1. **Mutation:** the value function itself (`value : State → Nat` in the
   bounded fragment) is replaced.
2. **Failure mode:** self-originating. The post-amendment value function
   would validate the amendment that installs it. `value_{P_{n+1}}` cannot
   be the authority for `(P_n → P_{n+1})`.
3. **Named / missing invariant:** missing. The basis side has
   `revoked_never_admissible`; standing side has
   `revoked_standing_never_standing` (closed 2026-06-03). The
   *value* side has no analog. **Architecture gap.**
4. **Lean specimen candidate:** `ValueDerivation` structure mirroring
   `BasisDerivation` / `StandingDerivation` with `valueRevoked` predicate
   and `revoked_value_never_admissible` obligation. Sibling theorem
   `revoked_value_never_authorized`. Same C-style structural closure.
5. **Reduces?** Pattern reduces to standing-grant shape. Architecture does
   not — the structure isn't there yet.
6. **Do not auto-promote:** classified source/temporal, so this case pass does
   not by itself schedule or ratify `ValueDerivation`. The structural gap may
   nevertheless be formalized before a runtime amendment specimen once its
   model, non-vacuity controls, and overlap with the standing-grant shape are
   explicit. Public promotion remains separate.

### Case #2 — retroactive legitimation (backward-reach)

1. **Mutation:** post-state validation applied to pre-state operation.
2. **Failure mode:** retroactive. `PostValidated` vs `AuthorizedIn` —
   boundary-by-asymmetry.
3. **Named invariant:** RetroactiveLegitimation kernel theorem.
4. **Lean specimen candidate:** exists —
   `~/git/lean/LeanProofs/Admissibility/RetroactiveLegitimation.lean`.
5. **Reduces?** Yes — this case **is** its specimen.
6. **Do not promote:** brake fires. Already mounted.

### Case #3 — self-certifying amendment (load-bearing)

1. **Mutation:** amendment that authorizes itself via the authority it
   installs.
2. **Failure mode:** self-originating. (A1): witness valid in `S`, not
   introduced by `S′`.
3. **Named invariant:** AmendmentFragment specimen's type-discipline
   (`AuthStep E s`).
4. **Lean specimen candidate:** exists —
   `~/git/lean/LeanProofs/Admissibility/AmendmentFragment.lean`.
5. **Reduces?** Yes — already its specimen.
6. **Do not promote:** brake fires. Already mounted.

### Case #4 — standing mutation (first-tractable)

1. **Mutation:** standing changed for later operations by an operation
   whose admissibility depends on the new standing.
2. **Failure mode:** self-originating at the standing dimension.
3. **Named invariant:** `revoked_standing_never_standing` +
   `revoked_standing_never_authorized` — closed 2026-06-03.
4. **Lean specimen candidate:** standing-upgrade-block worked example
   exists. No new specimen needed.
5. **Reduces?** Yes — directly to the just-mounted standing obligation.
6. **Do not promote:** brake fires. Already mounted via the C closure.

### Case #5 — crisis-mode value substitution (self-reach)

1. **Mutation:** value function substituted under crisis conditions.
2. **Failure mode:** self-originating. The crisis-installed evaluator
   would validate the substitution that installed it. Subcase of #1.
3. **Named invariant:** same value-side gap as #1.
4. **Lean specimen candidate:** subsumed by #1's `ValueDerivation`
   candidate. No separate specimen needed if `ValueDerivation` mounts.
5. **Reduces?** Yes — to #1 directly. Crisis is a triggering condition,
   not a distinct mutation shape.
6. **Do not promote:** brake fires. Inherits #1's architecture gap; not
   independently promoted.

### Case #6 — reflective adoption without origin legitimation

1. **Mutation:** post-adoption receipt cited as origin authority.
2. **Failure mode:** retroactive at receipt layer. Backward-reach sibling
   of #2.
3. **Named invariant:** RetroactiveLegitimation pattern lifted to receipt
   layer. Existing kernel theorem covers shape; no new theorem required.
4. **Lean specimen candidate:** could be a sibling specimen at receipt
   layer; reuses RetroactiveLegitimation.lean's structure. Optional.
5. **Reduces?** Yes — to #2's pattern, applied at a different altitude.
6. **Do not promote:** brake fires. Pattern reduction known; sibling
   specimen is optional housekeeping, not architecture gap.

---

## Candidate maximal cases (from non-pruning verdict)

### Evaluator mutation

1. **Mutation:** the evaluator (any of `BasisDerivation` /
   `PrecedenceDerivation` / `StandingDerivation`) replaced mid-trajectory
   by an operation whose admissibility the new evaluator validates.
2. **Failure mode:** self-originating, at the meta-altitude of derivation
   strategy.
3. **Named / missing invariant:** the `DerivationEnv` is a parameter of
   `decideAuthority`, but there is no theorem forbidding mid-trajectory
   replacement of the env by an operation that the new env would
   authorize. **Meta-altitude architecture gap.**
4. **Lean specimen candidate:** would require an `EnvDerivation` or
   `EnvChangeRule` structure carrying the constraint that env changes
   are admissible under the *prior* env. Same shape as (A1) lifted to
   the env-replacement altitude.
5. **Reduces?** Pattern reduces to (A1); architecture is unmounted at
   meta-altitude.
6. **Do not auto-promote:** the case pass files the architecture gap but does
   not choose the `EnvChangeRule` model. A bounded formal probe may make that
   choice and lead later code; it does not need a runtime forcing case.

### Value location mutation

1. **Mutation:** the field in `State` that the value function reads is
   relocated.
2. **Failure mode:** self-originating + boundary-by-asymmetry — the new
   location is post-state structure; pre-state reading cannot see it.
3. **Named invariant:** missing. Would require a value-location-stability
   invariant or a compositional value-derivation across location changes.
4. **Lean specimen candidate:** open. Likely a subcase of #1's
   `ValueDerivation` — location is a structural component of how value
   is derived from state.
5. **Reduces?** To #1's value architecture gap.
6. **Do not promote:** brake fires. Inherits #1's gap.

### Retroactivity-semantics mutation

1. **Mutation:** the meta-rule about what counts as retroactive is
   changed.
2. **Failure mode:** retroactive at meta-altitude. New rule applied to
   validate prior operations.
3. **Named invariant:** RetroactiveLegitimation at meta-altitude. Same
   kernel pattern lifted by one altitude.
4. **Lean specimen candidate:** open. Probably reuses
   RetroactiveLegitimation.lean's predicate structure, parameterized over
   "what counts as post-state."
5. **Reduces?** Yes — to #2 at meta-altitude.
6. **Do not promote:** brake fires. Pattern reduction known.

### Slice-boundary mutation

1. **Mutation:** what counts as a slice is changed.
2. **Failure mode:** self-originating — the new slice definition validates
   operations within the slice it defines.
3. **Named invariant:** missing. Would require slice-definition stability
   or a sliced-(A1) variant.
4. **Lean specimen candidate:** open. Possibly subsumed by env-mutation
   if slice definitions live in the env.
5. **Reduces?** To (A1) plus a compositional argument about slice
   definitions. Pattern reduces; architecture not specifically mounted.
6. **Do not promote:** brake fires. Borderline — slice boundaries may be
   a structural variant rather than a distinct dimension. Note but do not
   elaborate.

### Receipt/witness-definition mutation

1. **Mutation:** what counts as a valid receipt or witness is changed by
   an operation whose admissibility cites the new definition's receipt.
2. **Failure mode:** self-originating — new witness definition validates
   the operation that introduces the witness.
3. **Named invariant:** none specific. Sub-audit complete 2026-06-03
   (see [`boundary-witness-self-origination-audit.md`](boundary-witness-self-origination-audit.md)).
   `BoundaryWitness.lean` ships *static* obstruction for fixed envs —
   it proves witnesses are real evidence (not fabricable), not that
   the env defining the witness cannot be self-replaced. **Witness-
   definition mutation reduces to the env-change ghost strut, not to a
   separate witness-definition ghost strut.**
4. **Lean specimen candidate:** none required. The env-change ghost
   strut, if/when closed, covers this instantiation as a side effect.
5. **Reduces?** Yes — to the env-change ghost strut. NOT to
   BoundaryWitness.lean (different problem: static obstruction in a
   fixed env vs dynamic redefinition of the env).
6. **Do not promote:** brake fires; sub-audit classifies as bucket (2)
   covered-by-existing-pattern-but-unnamed. No Lean work opened.

---

## Side observations (do not auto-promote)

The case-work pass surfaced two architecture gaps in the source/temporal
species that mirror the standing-grant gap C closed:

1. **Value side.** `BasisDerivation` and `StandingDerivation` carry
   structural obligation fields (`revoked_never_admissible`,
   `revoked_standing_never_standing`). The bounded fragment held `value`
   environmentally; the maximal calculus needs a `ValueDerivation` or
   equivalent structure with the symmetric obligation. Cases #1, #5,
   value-location mutation all reduce to this gap.
2. **Meta / env-change side.** `DerivationEnv` is a parameter; there is
   no named theorem forbidding mid-trajectory replacement of the env by
   an operation the new env would authorize. (A1) at meta-altitude is
   unmounted. Evaluator mutation, slice-boundary mutation,
   retroactivity-semantics mutation, **and receipt/witness-definition
   mutation** (per the 2026-06-03 BoundaryWitness sub-audit) all
   touch this gap. A single closure at the env-change altitude — the
   meta-altitude analog of `revoked_standing_never_standing` — would
   discharge all four instantiations in one move. Not opened.

**These gaps are filed, not scheduled by this case pass.** Case classification
does not auto-promote either gap, but formalization may open a bounded
`ValueDerivation` or env-change probe on its own theorem merits before a
consumer exists. The standing-grant history (Alloy probe → codex flag → Lean
obligation) is useful provenance, not a required authorization sequence.

The gaps are **structural homologs**, not new species. They confirm the
substrate lint: every gap above is closable with boolean state predicates
+ named premise-production invariants. No multiplicity/resource apparatus
needed at any of them.

## Cross-references

- Closed taxonomy: [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Classification pass (the taxonomy as classifier on the register):
  [`maximal-calculus-taxonomy-classification.md`](maximal-calculus-taxonomy-classification.md)
- Amendment cut (case substrate):
  [`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md)
- Multiplicity/resource seed (sibling register parked):
  [`multiplicity-resource-register-seed.md`](multiplicity-resource-register-seed.md)
- Named architecture cited:
  - `~/git/lean/LeanProofs/Admissibility/Authority.lean`
  - `~/git/lean/LeanProofs/Admissibility/Derivation.lean`
    (basis + standing obligations)
  - `~/git/lean/LeanProofs/Admissibility/AmendmentFragment.lean`
  - `~/git/lean/LeanProofs/Admissibility/RetroactiveLegitimation.lean`
  - `~/git/lean/LeanProofs/Admissibility/BoundaryWitness.lean`
