# Substructural-frame audit — shipped refusal kernels

**Status:** bounded audit, 2026-06-03. Tests a new candidate unifier:
*admissibility as refusal of illicit structural rules in an unrestricted
authorization logic.* Different candidate from the one closed earlier
today (one-substrate / one-refusal-discipline). Prior synthesis closure
does not pre-decide this frame.

**Provenance:** new candidate surfaced 2026-06-03 by Agent-Governor
Claude ("oldest Claude" instance) during operator venting; calibrated
by ChatGPT; audit protocol locked by operator.

**Mapping-strength legend:**

- **structural** — kernel literally refuses a named structural rule of a
  sequent calculus.
- **plausible** — kernel maps to a refused rule of some authorization
  logic, but the proof-theoretic apparatus is not in the current
  substrate; the mapping would be structural under a different
  formalization.
- **analogy-only** — X-is-not-Y refusal is real but does not correspond
  to a structural rule; mapping requires inventing or vague-stretching
  a "rule" to fit.
- **failed** — no clean structural-rule analog.

## Per-kernel classification

### ContractionHinge
- **Refusal form:** `[A] ⊬ A ⊗ A`
- **Refused rule:** contraction (literal)
- **Laundering blocked:** one warrant occurrence licensing two
- **Substrate:** quantitative / multiplicity-resource
- **Mapping:** **structural**
- **Frame support:** substructural calculus (the one specimen that does)

### Authority gate (basis × precedence × standing → verdict)
- **Refusal form:** verdict is not authorized unless all three inputs
  are green
- **Refused rule:** no clean structural rule. Positive content is a
  conjunction definition; negative invariants are corollaries
  (no_basis_never_authorized, no_standing_never_authorized, etc.). The
  closest structural framing — "weakening on inputs" — would require
  treating the positive definition as a derived rule, not a refusal.
- **Laundering blocked:** verdict-without-component
- **Substrate:** authority algebra (boolean three-input gate)
- **Mapping:** **analogy-only**
- **Frame support:** taxonomy / authority algebra

### BasisDerivation.revoked_never_admissible
- **Refusal form:** revoked basis cannot derive admissible
- **Refused rule:** spec obligation on derivation strategies. Could be
  cast as "no weakening over revocation" but the kernel is a typing
  constraint on derivation environments, not a sequent-calculus rule.
- **Laundering blocked:** stale/revoked premise smuggled to admissible
- **Substrate:** boolean / source-temporal
- **Mapping:** **analogy-only**
- **Frame support:** laundering grammar (canonical: stale-premise
  refusal)

### StandingDerivation.revoked_standing_never_standing
- **Refusal form:** revoked standing cannot derive standing
- **Refused rule:** spec obligation, symmetric to basis side
- **Laundering blocked:** revoked standing smuggled
- **Substrate:** boolean / source-temporal
- **Mapping:** **analogy-only**
- **Frame support:** laundering grammar

### RetroactiveLegitimation
- **Refusal form:** post-state validation cannot license pre-state
  authorization (`AuthorizedIn` is not `PostValidated`)
- **Refused rule:** plausibly a *temporal cut* or *non-causal
  entailment* — using a later sequent's conclusion as an earlier
  sequent's premise. No sequent calculus with explicit time in scope;
  the mapping is structurally adjacent but not literal.
- **Laundering blocked:** post-state witness substituted for pre-state
  authority
- **Substrate:** boolean / source-temporal
- **Mapping:** **plausible** (would be structural under a temporal
  sequent calculus; not in current substrate)
- **Frame support:** laundering grammar; potentially structural in a
  temporal-logic substrate

### AmendmentFragment
- **Refusal form:** policy mutation cannot self-authorize (operation O
  cannot use the policy O installs to license O)
- **Refused rule:** plausibly a refused *self-installed fixed-point* —
  refusing a recursion rule that uses the operation's own output as a
  premise for the operation. No standard structural-rule name.
- **Laundering blocked:** self-installed authority used to authorize
  installation
- **Substrate:** boolean / source-temporal
- **Mapping:** **plausible** (refuses a kind of reflexivity with
  side-effects; not a standard structural rule)
- **Frame support:** laundering grammar

### AuthorizedStepNotSafe (Frontier 1)
- **Refusal form:** authorization does not entail safety preservation
  (`Authorized ⊬ Safe` over an externally-defined defended value)
- **Refused rule:** no structural-rule analog. This refuses a
  *domain-specific implication* between two predicates that share a
  context but not a definition.
- **Laundering blocked:** verdict treated as safety claim
- **Substrate:** witness/evidence (the bridge primitive)
- **Mapping:** **analogy-only** for structural-rule framing
- **Frame support:** laundering grammar (canonical: verdict → safety)

### BoundaryWitness
- **Refusal form:** weak object cannot uniformly lift to strong object
  (non-surjective forgetful map; no section)
- **Refused rule:** no structural-rule analog. The kernel is
  category-theoretic — failed surjectivity / lack of section. Living
  at the wrong level for a sequent-rule refusal.
- **Laundering blocked:** reconstructing strong-witness data from
  weak-side observations
- **Substrate:** witness/evidence (forgetful-map shape)
- **Mapping:** **failed**
- **Frame support:** taxonomy only

### Freshness (metric time)
- **Refusal form:** stale evidence cannot authorize current action
- **Refused rule:** plausibly *unrestricted temporal weakening* (the
  rule "if valid at t, valid at t+δ"). Mapping would need a temporal
  sequent calculus; in this corpus the kernel is a metric-admissibility
  check, not a sequent rule.
- **Laundering blocked:** decayed authority used at present time
- **Substrate:** boolean / source-temporal with metric overlay
- **Mapping:** **plausible** (structural in a temporal logic;
  plausible-only here)
- **Frame support:** laundering grammar

### StateTransition / mutation-store partitioning
- **Refusal form:** a step targeting store X cannot mutate store Y
- **Refused rule:** the discipline is bunched/separation-logic-shaped
  (contexts split by region, each rule respects region boundaries).
  But the kernel encodes the discipline as a *built-in invariant* on
  step constructors, not as a *refused rule* in a calculus that would
  otherwise admit it.
- **Laundering blocked:** cross-store mutation without explicit
  composition
- **Substrate:** authority algebra (partitioned state)
- **Mapping:** **analogy-only** for structural-rule framing (separation-
  logic shape is real; "refused rule" framing requires inversion)
- **Frame support:** laundering grammar

### Projection ≠ Predicate
- **Refusal form:** projection (observation map) cannot be conflated
  with predicate (logical condition)
- **Refused rule:** no structural-rule analog. Type-level distinction
  between two object kinds.
- **Laundering blocked:** type confusion across observation vs
  propositional content
- **Substrate:** witness/evidence
- **Mapping:** **analogy-only**
- **Frame support:** laundering grammar

### Selectivity ≠ Encapsulation (WitnessInvariance)
- **Refusal form:** selective behavior under perturbation does not
  entail encapsulation
- **Refused rule:** refused logical implication
  `Selective ⊬ Encapsulated`. Not structural.
- **Laundering blocked:** selectivity evidence cited as encapsulation
  evidence
- **Substrate:** witness/evidence
- **Mapping:** **analogy-only**
- **Frame support:** laundering grammar

### Reachability ≠ Recoverability
- **Refusal form:** graph reachability does not entail dynamic
  recoverability
- **Refused rule:** no structural-rule analog. Distinction between two
  evidence domains (static graph vs dynamic process).
- **Laundering blocked:** static reach evidence cited as dynamic
  recovery evidence
- **Substrate:** graph/reachability vs topology/recovery
- **Mapping:** **failed** for structural-rule framing
- **Frame support:** laundering grammar (cross-domain coercion refusal)

### Seal ≠ Outcome (CrossBoundary family)
- **Refusal form:** sealed boundary blocks specific artifact moves;
  does not guarantee external safety outcomes
- **Refused rule:** graph + artifact discipline. Not structural-rule
  shaped.
- **Laundering blocked:** boundary-seal cited as outcome guarantee
- **Substrate:** graph/reachability + artifact
- **Mapping:** **failed** for structural-rule framing
- **Frame support:** taxonomy

### Handle ≠ Standing
- **Refusal form:** having a handle/capability does not entail having
  standing
- **Refused rule:** refused type-level coercion between two role
  labels. Not structural.
- **Laundering blocked:** capability handle treated as invocation
  standing
- **Substrate:** authority algebra
- **Mapping:** **analogy-only**
- **Frame support:** laundering grammar (canonical role-coercion
  refusal)

### CrossBoundaryExposure / Degradation
- **Refusal form:** under sealed boundary, no Internal-origin
  External-target exposure reachable; exposure-attributed degradation
  cannot cite Internal-origin exposure
- **Refused rule:** reachability + artifact discipline (each `expose`
  constructor requires `Boundary.authorized origin target = true`)
- **Laundering blocked:** internal failure leaking as external exposure
- **Substrate:** graph/reachability + artifact
- **Mapping:** **failed** for structural-rule framing
- **Frame support:** taxonomy

## Tally

| Mapping strength | Count | Kernels |
|------------------|-------|---------|
| structural       | 1     | ContractionHinge |
| plausible        | 3     | RetroactiveLegitimation, AmendmentFragment, Freshness |
| analogy-only     | 8     | Authority gate, basis-revoked, standing-revoked, AuthorizedStepNotSafe, StateTransition, Projection≠Predicate, Selectivity≠Encapsulation, Handle≠Standing |
| failed           | 4     | BoundaryWitness, Reachability≠Recoverability, Seal≠Outcome, CrossBoundaryExposure |

Total: 16. (The basis/standing derivation obligations could be merged
or split with the Authority gate; the structure of the tally doesn't
change.)

## Decision rule applied

- **"Substructural calculus" frame:** earns "calculus candidate" only if
  MOST core kernels map structurally. **1/16 ≈ 6%. FAILS decisively.**
- **"Laundering grammar" frame:** earns if the X-is-not-Y pattern is
  real and stable across the corpus, even with heterogeneous rule
  mappings. **11/16 entries are forms of "refused coercion between
  authorization-adjacent role labels." HOLDS as descriptive pattern.**
- **"Taxonomy only" frame:** backstop for what laundering grammar
  doesn't cover. **3-4 entries are category-theoretic / graph-
  topological, neither structural nor laundering-grammar.**

## Verdict

> **Substructural calculus: fails. Laundering grammar: holds.
> Taxonomy: backstop.**

The corpus does not form a sequent calculus of refusals. It does form
a coherent *grammar of forbidden promotions between authorization-
adjacent role labels* —

- verdict ↛ safety (AuthorizedStepNotSafe)
- post-validation ↛ pre-authorization (RetroactiveLegitimation)
- mutation ↛ self-authorization (AmendmentFragment)
- revoked-basis ↛ admissible (BasisDerivation obligation)
- revoked-standing ↛ standing (StandingDerivation obligation)
- selectivity ↛ encapsulation (WitnessInvariance)
- projection ↛ predicate
- reachability ↛ recoverability
- seal ↛ outcome
- handle ↛ standing
- (and others not in this audit: fluency ↛ settlement, visible-green ↛
  recovery-capacity, survival ↛ closure, etc.)

Most kernels are "authorization type errors": refused coercions between
roles that authorization layers habitually confuse. Only
**ContractionHinge** has proof-theoretic bones in this corpus; the rest
is grammar, not calculus.

The substrate split from the earlier synthesis closure (source/temporal
vs multiplicity/resource) **intersects** this audit but doesn't replace
it. The laundering grammar is the *role-coercion* axis; the species
split is the *substrate* axis. Most laundering-grammar entries sit on
source/temporal substrate; ContractionHinge sits on multiplicity/
resource substrate; the cross-boundary / reachability entries sit on
graph/topology substrate that is mostly taxonomy. Two independent axes,
not nested.

## Keeper phrasing (if needed for cross-reference)

> **A calculus of laundering refusals, if it exists, will not be a
> sequent calculus. It is a grammar of forbidden promotions between
> evidentiary roles.**

## What this is NOT

- Not a re-opening of the unified-calculus question. Different
  candidate; the original question (one-substrate / one-discipline)
  stays closed.
- Not authorization to promote the laundering-grammar frame as new
  theory. The grammar is descriptive, not generative — same
  diagnostic-not-proof-theoretic status as the "disciplined premise
  production" genus.
- Not authorization to build a `LaunderingGrammar.lean`, rename
  modules, or open new Lean work. Capability inventory ≠ work
  commitment.
- Not a synthesis essay.

## What this IS

A bounded structural test that returned a clean negative for *calculus*
and a tentative positive for *grammar*. The grammar isn't proof theory.
It's a stable pattern of refused role-coercions, demonstrably present
in 11 of 16 audited kernels, with 1 structural specimen (ContractionHinge)
and 4 taxonomy-only kernels at the edges.

## Cross-references

- Closed taxonomy:
  [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Taxonomy classifier pass:
  [`maximal-calculus-taxonomy-classification.md`](maximal-calculus-taxonomy-classification.md)
- Case classification under closed taxonomy:
  [`amendment-cut-case-classification.md`](amendment-cut-case-classification.md)
- Calculus-capable fragment register (the one structural specimen):
  [`lincalc-consumer-story.md`](lincalc-consumer-story.md)
- Arc index:
  [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) §
  "Arc closure 2026-06-03"
