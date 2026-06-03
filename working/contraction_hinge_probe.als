/*
  contraction_hinge_probe.als

  Sibling probe to standing_upgrade_probe.als.

  Target artifact: ContractionHinge specimen
  (~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean) — specifically
  T3: ¬ Derivable [A] (A ⊗ A) in a base sequent calculus without
  contraction.

  Operator-locked scope:
    - Do NOT attempt to reproduce T2/T3's arithmetic proof in Alloy.
    - Probe whether the no-contraction refusal reduces to the same
      four-layer relational pattern surfaced by the standing-upgrade
      probe:
          kernel + wrapper + derivation discipline + named invariant
    - If yes: show the compact reduction.
    - If no: document the additional apparatus required.
    - A bounded enumeration is acceptable only as a witness to substrate
      shape, not as a replacement proof.

  Expected verdict (operator prediction): distinct family.
    Standing-upgrade blocks self-originating authority.
    ContractionHinge blocks duplicated resource use.
*/

// =============================================================================
// PART 1 — Boolean-set encoding (mirroring standing-upgrade's primitives)
//
// Standing-upgrade used `set`-valued state predicates:
//   hasStanding: set Actor
//   hasAdmissibleBasis: set Claim
// These are boolean per element: an actor is in the set or not.
//
// Question: can this primitive vocabulary express the ContractionHinge
// refusal? Specifically, can it distinguish:
//   T1-shape:  produce A     from warrant {A}   — allowed
//   T3-shape:  produce A⊗A   from warrant {A}   — refused
// =============================================================================

sig Warrant {}

sig Conclusion {
  parts: set Warrant   // <-- structural choice: SET. Forces the question.
}

sig Operation {
  uses:     set Warrant,
  produces: one Conclusion
}

// Standing-upgrade-style admissibility check (boolean):
// the operation's used warrants must cover the conclusion's required warrants.
pred admissibleBoolean[o: Operation] {
  o.produces.parts in o.uses
}

// Probe 1 — the set-collapse witness.
//
// In set-valued encoding, an A-atom and an A⊗A composite have IDENTICAL parts:
// both have parts = {A} (the set {A,A} collapses to {A}). So an operation
// producing "A⊗A from {A}" is structurally indistinguishable from one
// producing "A from {A}". The boolean encoding CANNOT block T3 because it
// CANNOT REPRESENT THE DIFFERENCE.
//
// Probe: find two operations, both admissible, both using {A}, both with
// the SAME parts set {A} — exhibiting the conflation.
run probe1_set_collapse_conflates_T1_and_T3 {
  some A: Warrant, op_T1, op_T3: Operation |
    op_T1 != op_T3
    and op_T1.uses = A and op_T3.uses = A
    and op_T1.produces.parts = A and op_T3.produces.parts = A
    and admissibleBoolean[op_T1]
    and admissibleBoolean[op_T3]
} for 3

// Expected: SAT. Two operations that are semantically distinct (one is
// T1-shape, one is T3-shape) become indistinguishable under set-valued
// encoding. This is the encoding-friction witness — Layer 1 of the
// standing-upgrade pattern cannot encode the question.

// =============================================================================
// PART 2 — Multiplicity-aware encoding (introducing the additional apparatus)
//
// To express T3, we must move from set-valued to multiplicity-aware.
// This is the new substrate primitive: occurrence counting.
// =============================================================================

sig MWarrant {}

sig MUse {
  warrant: one MWarrant,
  count:   one Int      // <-- new apparatus: Int-valued occurrence count
}

sig MConclusion {
  needs: set MUse       // each "need" specifies a warrant and its required count
}

sig MOperation {
  provides: set MUse,
  produces: one MConclusion
}

// Multiplicity-aware admissibility: every needed warrant-and-count must be
// matched by a provided one with sufficient count. This is structurally
// distinct from standing-upgrade's boolean `in`.
pred admissibleMultiplicity[o: MOperation] {
  all need: o.produces.needs |
    some have: o.provides |
      have.warrant = need.warrant
      and need.count <= have.count
}

// Probe 2 — T3-analog in multiplicity encoding.
//
// Look for an admissible operation that produces A⊗A (needs count 2 of A)
// from a single A (provides count 1 of A). Should be UNSAT — the
// admissibility check requires count ≤ provided count, and 2 > 1.
//
// Note: this is NOT a reproduction of Lean's T3 proof. It is a relational
// witness that the SAME pattern is expressible AT ALL only via the new
// count primitive. The contrast with Probe 1 is the finding.
run probe2_T3_analog_with_multiplicity {
  some A: MWarrant, o: MOperation, need: MUse, have: MUse |
    o.provides = have
    and o.produces.needs = need
    and need.warrant = A and need.count = 2     // A⊗A requires 2 occurrences
    and have.warrant = A and have.count = 1     // only 1 provided
    and admissibleMultiplicity[o]
} for 4 Int

// Expected: UNSAT. The multiplicity check correctly blocks T3.
// Significance: this works, but ONLY because we introduced Int and count.
// In the standing-upgrade probe, Int was never needed.

// Probe 3 — the legitimate-supply analog (the T1 shape, multiplicity version).
//
// One A provided, one A needed → admissible. Mirrors standing-upgrade's
// probe2_allowed_shape: the legitimate case is constructible under the new
// encoding.
run probe3_legitimate_supply_multiplicity {
  some A: MWarrant, o: MOperation, need: MUse, have: MUse |
    o.provides = have
    and o.produces.needs = need
    and need.warrant = A and need.count = 1
    and have.warrant = A and have.count = 1
    and admissibleMultiplicity[o]
} for 4 Int

// Expected: SAT.

// Probe 4 — the contraction-hinge analog.
//
// In ContractionHinge.lean, T3' shows that WITH contraction (treat two
// occurrences as one), [A] ⊢ A⊗A becomes derivable. The relational analog:
// a "contraction" predicate that lets one MUse cover two needs.
//
// Encode as a separate predicate (analogous to Derivable vs DerivableC):
//   admissibleWithContraction = standard admissibility OR
//                                "the provide-count covers need-count under
//                                 contraction-like duplication"
pred admissibleWithContraction[o: MOperation] {
  all need: o.produces.needs |
    some have: o.provides |
      have.warrant = need.warrant
      // contraction-licensed: a single provide-count of any positive value
      // is allowed to cover any need-count. (The forbidden move, isolated.)
      and have.count >= 1
}

run probe4_contraction_enables_T3 {
  some A: MWarrant, o: MOperation, need: MUse, have: MUse |
    o.provides = have
    and o.produces.needs = need
    and need.warrant = A and need.count = 2
    and have.warrant = A and have.count = 1
    and admissibleWithContraction[o]
} for 4 Int

// Expected: SAT. The contraction-licensed predicate authorizes what the
// strict multiplicity predicate refuses. Mirrors ContractionHinge.lean's T3'
// — the bad move becomes derivable only when contraction is the named
// extension you opt into.

// =============================================================================
// PART 3 — Substrate-shape comparison (the finding crystallized in Alloy)
//
// Standing-upgrade probe used:
//   - Sig fields:  `hasStanding: set Actor`, `hasAdmissibleBasis: set Claim`
//   - All `set`-valued. No Int. No arithmetic.
//   - Layer 4 invariant: a boolean fact (`independentStandingGrant`)
//
// ContractionHinge probe required:
//   - Sig field:   `count: one Int`
//   - Comparison:  `need.count <= have.count` — arithmetic
//   - Scope flag:  `for 4 Int` — bounded integer enumeration
//   - The structural primitive is OCCURRENCE COUNTING, not visibility
//
// These are not the same substrate. The four-layer standing-upgrade pattern
// is boolean-relational; ContractionHinge requires quantitative-relational.
// =============================================================================
