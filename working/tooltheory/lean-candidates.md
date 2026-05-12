# Lean escape candidates from tooltheory

Candidate predicate names worth considering for the Admissibility kernel modules *if* the doctrine cooked in this directory survives to Lean-formal stage. Names are first-pass; the math should sniff them and reject the decorative ones.

## P25 family

- `proxy_evidence_does_not_authorize_target_closure` — from [consequence-scoping](consequence-scoping.md)
- `advisory_basis_does_not_authorize_mutation` — from [consequence-scoping](consequence-scoping.md)
- `homogeneous_replication_preserves_kernel` — already proven in `~/git/lean/LeanProofs/Paper25EpistemicBorderControl.lean` as `ker_replicateRows_eq_ker`; restated here as the predicate-name pattern for sibling claims
- `collective_observability_necessary_not_sufficient` — from [heterogeneous-witness-cohorts](heterogeneous-witness-cohorts.md); the sufficiency part is open
- `proxy_shock_does_not_authorize_target_closure` — from [proxy-shock-mismatch](proxy-shock-mismatch.md) (relative of consequence-scoping)
- `dashboard_quiet_not_recovered_reliability` — from [dashboard-quiet-is-not-recovery](dashboard-quiet-is-not-recovery.md); domain-flavored, unlikely to land as-is

## Abstraction candidates

Several of the names above are domain-flavored (SLIs, dashboards, recoveries). Those are unlikely to land as Lean predicates directly; they probably refactor into abstract predicates about *witness scope* and *closure authorization* that domain-specific cases instantiate.

The cleanest abstractions, if they survive cooking:

- `witness_scope` — what a witness can testify to
- `closure_authorization` — whether evidence can authorize target-binding action
- `consequence_scope_preservation` — aggregation / control-allocation must preserve the scope tags

These look like the family of predicates a *Witness*-themed Admissibility module would carry, complementary to the existing Authority / StateTransition / Derivation / Execution / Corrective / WitnessInvariance / FiatAdmissibility / SurfaceAuthorization / RecoveryMargin / ClosureEligibility / NumericalAdmissibility / PublicReceiptRefinement / CorrectiveBoundary modules.

## Promotion gate to Lean

Don't mint a kernel predicate from a tooltheory note alone. Per kernel discipline:

1. Tool implementation has cited or relied on the doctrine in non-trivial code (downstream forcing case).
2. The predicate has a generator (it makes a distinction the kernel currently can't express).
3. The predicate has a real proof target (not a `True`-placeholder discharge).
4. The predicate names the physics, not a particular instance (per primitive-ontology classification).

Until those are met, the candidate stays here.

## Sim candidate (lane-1+4)

If the heterogeneous-cohort simulation lane ever earns its keep, the spec from chatty's lane-mapping:

```
- agents with replicated proxy sensors only;
- agents with one slow/noisy T-sensor;
- aggregation rule that preserves heterogeneity;
- aggregation rule that collapses it;
- compare whether q ∉ ker(Ō_T) survives into action.
```

Could inform:

- NQ witness-registry design;
- labelwatch / driftwatch aggregation caution;
- Governor evidence-basis rules;
- future P24/P25 bridge paper if it earns one.

No DOI required. Quietly improves three tools and one future paragraph if it works.
