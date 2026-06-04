# Validity-spendability split — candidate architecture invariant

**Status:** Candidate architecture invariant, 2026-06-03.
NOT ratified doctrine. NOT a paper. NOT a Lean build task.
NOT an AI-safety impossibility claim.
**Discipline:** file-now-work-never. Capability inventory ≠ work
commitment.

## 1. Abstract / keepers

The formal fracture between source/temporal and multiplicity/resource
substrates (closed 2026-06-03 against unification) has an engineering
consequence: validity and spendability are different planes, and a
semantic governor cannot safely own both with the same kind of state.

> **Validity is not spendability.**
>
> **Observation of validity is not a lease on capacity.**
>
> **Validation may mint eligibility. It may not mint capacity.**
>
> **The agent may see the ration book. It may not hold the pen.**
>
> **If the syntax fractures there, the engineering must fracture there
> too.**

**Precise claim:** self-contained semantic governance is insufficient
for resource safety. Resource safety requires an **independently
authoritative** linear accountant, allocator, lease store, token store,
or equivalent mechanism whose state the agent cannot reinterpret,
regenerate, summarize into authority, or mutate. ("Out-of-band" is one
candidate implementation; the load-bearing property is authority
separation, not necessarily deployment topology.)

**Allowed claim** (what the discipline permits): a governor may
*coordinate* validity and spendability, but must not *adjudicate* both
with the same kind of state. Validity and spendability require separate
authority surfaces and a disciplined handoff.

**Note on handles vs claims.** The keeper lines above are *handles*
for the result; the defensible form is the precise claim above (and
the structural-form restatement in §2). Aphorisms run ahead of the
qualifier; cite the precise version, not the poster, downstream.

## 2. Provenance

Surfaced 2026-06-03 as the architecture-altitude cash-out of the
ContractionHinge / Alloy / disciplined-premise-production arc.

The split arises from the **encoding-substrate result**:

- Source/temporal discipline uses **boolean state predicates** (`set
  Actor`, `set Claim`, `set Verdict`).
- Multiplicity/resource discipline requires **quantitative
  occurrence/use-count substrate** (`Int`, occurrence counts,
  arithmetic `≤`).

Neither encoding can host the other's refusals without adding
substrate it didn't otherwise need. See
[`contraction-hinge-probe-result.md`](contraction-hinge-probe-result.md)
for the encoding-substrate witness.

The claim is *not* that boolean logic can never encode counting;
doing so imports quantitative substrate. The moment the validity
surface must track occurrence, reservation, or consumption, it has
crossed into spendability machinery. That crossing IS the result.

**Production-code name for the encoding cough: the laundering
surface.** The location where a unified-substrate semantic layer
pretending to handle both planes has a representational hole where the
multiplicity refusal should be. The hole is exploitable; the cough is
falsifiable; engineers can look for both at specific surfaces.

### Structural form (contraction boundary)

The substrate split states formally as a *contraction boundary*:

- **Validity facts are contractible.** Once a premise is valid,
  observing or citing that validity multiple times does not deplete
  it. `valid(x) ∧ valid(x) ≡ valid(x)`.
- **Spendable resources are non-contractible.** This is
  ContractionHinge's `[A] ⊬ A ⊗ A`: one token, lease, quota unit,
  budget allowance, or blast-radius slot cannot be duplicated into
  two consumable authorities.
- **The laundering surface appears** where a contractible validity
  artifact can be interpreted as a non-contractible spendability
  artifact without an atomic handoff.

The danger is *convertibility*, not co-location: a single surface can
hold both planes safely if types, authority boundaries, and mutation
paths are sealed. The bug shape is "contractible credential used as
linear token" — e.g., a JWT treated as reusable bearer capacity
without server-side consumption. JWT-as-validity is fine;
JWT-as-bearer-capacity-without-consumption is the laundering surface.

Theorem-shaped form of the precise claim:

> **Validity is contractible; spendability is linear. Any
> architecture that lets an agent convert the former into the latter
> without an independently authoritative allocator has created a
> laundering surface.**

The two-altitude identity is exact, not analogous: the formal
non-unification (closed 2026-06-03 against substrate unification) and
the engineering split are the same object — contraction refusing to
be shared across one surface.

## 3. The two planes

**Validity plane.** Asks whether a premise / request is eligible.

- Source, freshness, revocation, standing, scope, policy, pre-state
  visibility.
- Examples: semantic governor, validator chain, policy check, evidence
  gate, scope contract.

**Spendability plane.** Asks whether valid capacity exists and can be
consumed.

- Budgets, leases, tokens, quotas, retry allowance, blast-radius slots,
  idempotency keys.
- Examples: linear accountant, lease store, token allocator, budget
  daemon, rate limiter.

## 4. Handoff invariant

Required handoff:

```
validated premise
 → eligibility
 → linear token / lease / budget unit / reservation
 → atomic consumption
 → no semantic regeneration
```

Explicit invariant:

> A valid premise may become spendable only through a spendability
> authority. It may not become spendable merely because the semantic
> layer continues to recognize it as valid.

Companion form:

> The semantic layer may request capacity; it may not certify that
> capacity exists.

## 5. Failure mode

Core laundering move:

> **valid premise → reusable capacity**

Failure patterns this invariant is meant to detect:

- Retry loop reuses stale validation as fresh allowance.
- Agent summarizes prior allowance into semantic context and treats the
  summary as authority.
- Receipt or testimony treated as reusable lease.
- Override grants validity AND decrements TTL in the same mutable
  surface (no boundary).
- Scope grant combines eligibility and usage accounting without a hard
  boundary.
- Budget / capacity observed more than once and treated as owned more
  than once.
- Idempotency key checked before fanout but not consumed atomically.

Each is an instance of the encoding cough surfacing in production.

## 6. Candidate architecture pattern

Candidate only, not ratified:

- **Semantic governor.** Validates eligibility. May coordinate.
- **Linear accountant.** Owns consumable capacity. Out-of-band; the
  agent cannot mutate, summarize into authority, or regenerate.
- **Execution layer.** Consumes token, emits receipt.
- **Witness layer.** Records and testifies; does NOT allocate.

This four-plane split is an enforcement-pattern *candidate*, not
doctrine. The discipline holds even if specific consumer systems (AG,
Wicket, NQ, deployment platforms) instantiate it with different
component names or boundaries.

## 7. Project mappings

**Agent Governor (AG).** Cross-reference `GOV_GAP_VALIDITY_SPENDABILITY_SPLIT_001`
(filed by AG 2026-06-03 with the four-plane architecture as candidate
enforcement pattern). Likely audit surfaces: override management
(validity grant + TTL decrement in same surface); scope grants
(validity + usage count tied); quorum thresholds (vote counts vs claim
type validity); Neff / sybil accounting (counts × bloc membership);
dispatcher leases (permission + heartbeat together); budgets and
per-tool caps. AG may *coordinate* both planes, but mixed surfaces
require audit per the handoff invariant.

**Wicket / WLP.** Admission is eligibility, not spendable mutation
authority. Receiver acceptance is not reusable authority. Possible
future gap: receiver acceptance must not become replayable mutation
authority.

**NQ.** Testifies about double-spend, lease reuse, quota overrun.
Does NOT allocate or enforce capacity. Witness layer only.

**Deployment systems.** Blast-radius observation is not a lease on
capacity. Maintenance-window / rollout-slot / quota-unit double-spend
are multiplicity/resource failures. See
[`multiplicity-resource-register-seed.md`](multiplicity-resource-register-seed.md)
for the specimen family.

## 8. Relationship to LinCalc / ContractionHinge

- `~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean` is the
  minimal formal witness for non-duplication (`[A] ⊬ A ⊗ A` — T3).
- LinCalc, if ever opened, would be the *logic of non-duplication*,
  not the logic of all refusal. See
  [`lincalc-consumer-story.md`](lincalc-consumer-story.md) for the
  cage discipline.
- No `LinCalc.lean` is opened by this note.
- Capability inventory does not imply work commitment.

## 9. Prior art and contribution

Prior art includes **linear logic** (Girard 1987), **capability
systems**, **TOCTOU** failures, **quota accounting**, **rate
limiting**, **replay protection**, and **double-spend prevention**.
This note does not claim novelty for non-contraction or resource
accounting.

**Contribution:** the agent-governance framing — the
validity/spendability split as a *locatable, falsifiable laundering
surface* when semantic agent context can reinterpret, regenerate, or
summarize consumable authority. The named contribution is the
discriminator (look for the encoding cough at specific surfaces), not
the underlying linear-resource discipline.

## 10. Non-goals

Explicitly NOT claimed by this note:

- No new Lean module.
- No module rename.
- No paper. No DOI. No publication path.
- **No grand AI-safety claim.** "Safety is impossible" is rejected as
  overclaim. The precise claim is *self-contained semantic governance
  is insufficient for resource safety* — a structural design rule,
  not a doctrine.
- No unified admissibility calculus resurrection. The synthesis fork
  stays closed.
- No claim that semantic governors are useless. A semantic governor
  may coordinate; it may not adjudicate spendability with semantic
  state.
- No claim that all refusal is linear, or that all governance is
  multiplicity/resource. The source/temporal species exists, with its
  own named architecture and its own discipline.

## 11. Opening triggers

This note becomes actionable only if a concrete consumer asks for it:

- **AG:** an audit (per `GOV_GAP_VALIDITY_SPENDABILITY_SPLIT_001`)
  finds mixed validity/spendability state and needs the invariant to
  gate a refactor.
- **Wicket / WLP:** one-shot admission / effect token semantics needs
  the handoff invariant.
- **NQ:** new testimony claim shape covers budget / lease / quota
  double-spend.
- **Deployment safety:** a real blast-radius / quota / maintenance-
  window double-spend incident or near-miss surfaces and a
  specification artifact is wanted.
- **Other implementation consumer:** any real system with a named
  non-duplication invariant requesting a specification substrate.

Until one of those fires: parked.

## Cross-references

- Architectural deepening (three pillars + five-component stack +
  descriptor purity rule + Nightshift role + constitutional Lean
  route):
  [`constitutional-governor-architecture.md`](constitutional-governor-architecture.md)
- Second invariant (custody must not be silent):
  [`custody-legibility.md`](custody-legibility.md)
- Synthesis closure (the formal fracture):
  [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Alloy substrate-asymmetry evidence:
  [`contraction-hinge-probe-result.md`](contraction-hinge-probe-result.md)
- Two-species classifier:
  [`maximal-calculus-taxonomy-classification.md`](maximal-calculus-taxonomy-classification.md)
- LinCalc cage discipline:
  [`lincalc-consumer-story.md`](lincalc-consumer-story.md)
- Specimen family:
  [`multiplicity-resource-register-seed.md`](multiplicity-resource-register-seed.md)
- Sibling artifact at role-coercion altitude (laundering grammar):
  [`substructural-frame-audit.md`](substructural-frame-audit.md)
- Case-work under closed taxonomy:
  [`amendment-cut-case-classification.md`](amendment-cut-case-classification.md)
- Arc index:
  [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) §
  "Arc closure 2026-06-03"
- Kernel artifact:
  `~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean`
- Cross-system: Agent Governor `GOV_GAP_VALIDITY_SPENDABILITY_SPLIT_001`
  (filed 2026-06-03)
