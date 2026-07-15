# LinCalc — resource-refusal calculus candidate (parked)

**Status:** register seed, 2026-06-03. Calculus-capable fragment of the
multiplicity/resource species. **Parked.** NOT a Lean module. NOT a paper.
NOT the logic of all refusal.
**Provenance:** surfaced 2026-06-03 across a three-node exchange (DeepSeek
→ ChatGPT → Claude Code) that independently converged on the same
cage discipline — the first stable cross-model convergence of the
2026-06-03 synthesis-closure arc.

## Keeper lines (verbatim, both load-bearing)

> **LinCalc is not the logic of refusal. It is the logic of non-duplication.**

> **Capability inventory ≠ work commitment.**

The second is the brake. It is the difference between this note
existing and `LinCalc.lean` existing.

## 1. What it is

A small linear sequent calculus over a multiplicative tensor fragment,
with multiset contexts, no contraction, no weakening (or weakening
explicit and tagged). The bones already exist in
`~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean`:

- Judgment form: `Γ ⊢ F` (linear entailment with multiset Γ)
- Soundness lemma: `T2 : Derivable Γ C → v C ≤ sum Γ`
- Refusal corollary: `T3 : ¬ Derivable [A] (A ⊗ A)`
- Quarantined extension: `T3'` (contraction restored in `DerivableC`,
  the boundary-by-asymmetry pattern)

Promoting to a standalone calculus would add explicit syntax,
cut elimination, optional `⊸` and `!`. None of that is opened here.

## 2. What it is NOT (the cage)

- **NOT a unified admissibility calculus.** The synthesis fork closed
  against unification 2026-06-03; LinCalc is one species's
  calculus-capable fragment, not a reduction of the source/temporal
  species into the multiplicity/resource species. See
  `source-basis-discipline-synthesis.md` § "Closure of blocker 1."
- **NOT the logic of all refusal.** The genus "disciplined premise
  production" has *diagnostic content*, not proof-theoretic content.
  Refusal patterns outside non-duplication (stale, revoked,
  self-originating, retroactive, missing-independent-basis) belong to
  the source/temporal species and have their own named architecture in
  Lean (`BasisDerivation.revoked_never_admissible`,
  `StandingDerivation.revoked_standing_never_standing`).
- **NOT the foundation of NQ.** NQ's contradiction model is
  epistemic/operational ("dashboard says healthy, substrate says
  sick"); not all NQ contradictions are linear-resource violations.
- **NOT a runtime enforcement mechanism.** LinCalc is a *specification
  substrate* for policy compilers and testimony schemas, not a runtime
  allocator.
- **NOT a candidate paper.** No DOI cycle. No formal-methods venue.

## 3. The core invariant

```
[A] ⊬ A ⊗ A
```

In words: one occurrence of resource `A` cannot license two
occurrences of `A` in a conclusion. Contraction is the rule that would
permit this; the base calculus refuses to include it.

Operational paraphrase (from the multiplicity/resource register seed):

> A shared safety budget is not a reusable premise.

> A valid allowance is not duplicable merely because multiple
> admissible actors can observe it.

> Observation of remaining capacity is not a lease on that capacity.

## 4. Consumer stories

Where the invariant maps onto real systems with named non-duplication
needs. None of these is an active consumer requirement; each is a
*candidate consumer pathway*.

### Governor (agent_gov)

- **Budgets:** USD / token / wall-clock caps. A budget allowance is a
  linear resource; double-spending the same allowance is the headline
  failure.
- **Per-tool caps:** one issued cap, one consumption.
- **Sequence gates involving consumed capabilities:** e.g.,
  *secret read → network egress*. A secret read produces a linear
  capability; egress consumes it. The capability cannot be reused.
- **Policy-time static check:** a budget/sequence policy that admits
  double-spending could be rejected at authoring time by a
  LinCalc-aware policy compiler.

### Wicket (admission control sibling)

- **Admission tokens:** one token, one admission.
- **Action leases:** time-bounded exclusive hold; LinCalc encodes that
  two parallel actions cannot both cite the same lease as authority.
- **Mutation authority with single-use standing:** standing that
  authorizes exactly one mutation, not arbitrary reuse.

### NQ (testimony, NOT enforcement)

NQ would *witness* multiplicity/resource failures, not enforce
linearity. Specifically:

- Claim: *"deployment budget was not double-spent"*
- Claim: *"lease was not reused"*
- Claim: *"quota consumption did not exceed issued allowance"*
- Claim: *"idempotency key was consumed once"*
- Claim: *"blast-radius cap was not exceeded by parallel jobs"*

These are NQ's existing four-part-proof claim shape (Observed /
Contradiction / Diagnosis / Next checks) instantiated for the
multiplicity/resource species. NQ stays a testimony system.

### Deployment systems (the canonical specimen family)

Per `multiplicity-resource-register-seed.md`:

- Canary cohort budget reused by parallel rollout jobs
- Maintenance window capacity double-booked
- Rack / POP / cell blast-radius cap exceeded by independent schedulers
- Error-budget "available" snapshot consumed by multiple releases
- Database migration lock treated as advisory evidence instead of
  exclusive lease
- Rate-limit / API quota checked before fanout but not consumed
  atomically

All share the same shape: a valid budget observed by multiple actors
who each consume it as if exclusively held. Fix family: reservation,
lease, token consumption, accounting, uniqueness of use, atomic
claim/check/use boundary.

## 5. Hard boundaries (do not absorb)

- **NQ is a witness, not an enforcer.** LinCalc near NQ supplies a
  claim schema for multiplicity/resource findings, not a runtime
  allocator. Crossing this boundary turns NQ into something it isn't.
- **Receipts are not automatically linear.** Audit evidence is
  designed to be reusable, citable, copyable. LinCalc applies to
  receipts only when the receipt is explicitly typed as a *consumption
  token*. Default: receipts duplicate freely; the linear thing is the
  authority/effect-claim derived from them.
- **LinCalc does not absorb the source/temporal axis.** Stale,
  revoked, self-originating, retroactive failures belong to the
  source/temporal species; encoding them via linear logic would be the
  failed unification attempt re-entering through a back door.
- **The genus is diagnostic, not proof-theoretic.** "Disciplined
  premise production" is a triage protocol; LinCalc is the species's
  proof-theoretic core, not the genus's.

## 6. Calculus-capable status

ContractionHinge already has the proof-theoretic bones (judgment +
structural-rule refusal + soundness lemma + refusal corollary +
quarantined contrast). Promoting to a standalone *LinCalc* would add:

- Explicit linear sequent calculus syntax (init / exch / ⊗L / ⊗R;
  optional `⊸`, `!`)
- Cut elimination (the hard but doable part; trivial for the
  fragment without `!`)
- Optional `Lean 4` formalization, sibling to ContractionHinge.lean
- Renaming the artifact out of the authority domain
  (`Admissibility/ContractionHinge` → `Resource/LinCalc` or similar)

This note does not automatically schedule that work. Capability inventory ≠ work
commitment. A coherent LinCalc model, theorem, or countermodel may nevertheless be
developed before a runtime consumer exists, and may lead the implementation.

## 7. Runtime integration and priority signals

The following concrete consumers would make runtime integration actionable and
would supply priority, instantiation, or promotion evidence. They are not permission
to begin formal work:

- **Governor:** an actual budget/sequence/idempotency policy needs
  static checking that LinCalc would provide. Implementer asks for
  the specification substrate.
- **Wicket:** an action-lease or admission-token specimen needs a
  formal non-duplication guarantee in its specification.
- **NQ:** a multiplicity/resource testimony schema is being authored
  and the claim shape needs a formal underwriter.
- **Deployment safety:** a real blast-radius / quota / maintenance-
  window double-spend incident or near-miss surfaces and the operator
  wants a specification artifact to cite.
- **Independent forcing case:** any other concrete consumer with a
  named non-duplication invariant they want statically checked.

### Trigger status (updated 2026-06-03)

- **Governor — partially fired.** Agent Governor filed
  `GOV_GAP_VALIDITY_SPENDABILITY_SPLIT_001` on 2026-06-03 (status:
  proposed / audit-required). The gap names the four-plane
  architecture (semantic governor / linear accountant / execution /
  witness) as a *candidate enforcement pattern*, not ratified. It does
  not yet constitute an "implementer asks for the specification
  substrate" — it's gap-level recognition of the invariant, with
  audit targets (override management, scope grants, quorum, Neff /
  sybil accounting, dispatcher leases). Runtime integration remains **parked**
  pending AG audit findings; a formal LinCalc probe may proceed independently
  when its fragment, soundness claim, and non-vacuity controls are precise. See
  [`validity-spendability-split.md`](validity-spendability-split.md)
  for the architecture-altitude framing.
- Wicket, NQ, Deployment safety, Independent forcing case — no
  triggers fired.

Until a full signal fires: runtime integration, paper promotion, and a DOI cycle
remain parked. A checked Scratch `LinCalc.lean` is not public promotion and does not
wait for one of these signals.

## 8. Cross-references

- Parent register seed (the multiplicity/resource species,
  pre-LinCalc): [`multiplicity-resource-register-seed.md`](multiplicity-resource-register-seed.md)
- Synthesis closure (the taxonomy LinCalc sits inside as the second
  species's calculus-capable fragment):
  [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Empirical substrate-shape evidence:
  [`contraction-hinge-probe-result.md`](contraction-hinge-probe-result.md)
- Closed taxonomy classifier pass:
  [`maximal-calculus-taxonomy-classification.md`](maximal-calculus-taxonomy-classification.md)
- Arc index:
  [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) §
  "Arc closure 2026-06-03"
- Kernel artifact (the existing bones):
  `~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean`
- Sibling diagnostic kernel (source/temporal species architecture):
  `~/git/lean/LeanProofs/Admissibility/Derivation.lean`
  (`StandingDerivation.revoked_standing_never_standing` — closed
  2026-06-03, the structural homolog of LinCalc's place inside its
  species)

## 9. What this note prevents

Without this register seed, the calculus-capable status of
ContractionHinge would either:

- Drift back into the unified-calculus ambition (kabuki re-entry), or
- Get rediscovered later under a new vocabulary (kernel-overlap-audit
  failure).

With this note, both failure modes are pre-blocked: the cage is
documented, the consumer story is named, the opening triggers are
explicit, and the next visitor sees both the lark and the cage.
