# Maximal calculus (refused) — forcing-case register

> *Historical working note. "Maximal calculus" here names the unified object this stack refuses to be; the register catalogues cases that would have forced its construction. Post-2026-06-03 synthesis closure, no unified calculus is the target — the cases below remain valid as per-kernel forcing material, not as gates on a unification target.*

**Status:** Forcing-case register, filed 2026-06-01. NOT a roadmap.
NOT a plan. NOT an Axis-3 promotion. NOT to be worked.

The register's job is to be the container that catches forcing cases
when they show up. Cases will surface during the value-sound-gates
paper drafting (or from adversarial review, or in the wild); the
register's existence prevents losing them. *File now, work never
(until something forces it).*

**Provenance:** Multi-model collaboration 2026-06-01. ChatGPT drafted
the six candidate cases and the structural shape. Claude-web (Opus
4.8) tightened with: case #3 flagged load-bearing, #4 noted as first
formally tractable, the self-reach / backward-reach geometry split,
the can't-reduce-to-fixed-value test as required per-case field, and
*"refuse to decide whether maximal is one or several"* added to the
refusal list. Both converged on **file-now-work-never** timing.

## The fuse sentence

> Every gate in the value-sound-gates paper is sound relative to an
> externally supplied value.

This is the assumption every forcing case below is trying to break.
Stated this precisely so that the moment something forces it, the
break is named, not rebuilt from scratch.

## Current closed fragment (what the bounded paper assumes)

- A fixed evaluator.
- Externally supplied defended value (`E.value : σ → Nat`, a function
  of state, not part of mutable state).
- Witnesses gate weak objects into value-sound transition/composition
  families.
- Necessity is slice-indexed, not universal.

The maximal calculus opens when one or more of these assumptions
becomes untenable.

## Maximal calculus claim candidate

> A maximal admissibility calculus must *account for* cases where the
> evaluator, value function, standing rule, or admissibility predicate
> is itself mutable.

"Account for" is deliberately weaker than "absorb" — see refusals.

## The discriminator (required per-case)

A case forces the maximal calculus *only if* it cannot be represented
as ordinary transition or merge under a fixed value function —
including representations in a product state space `(mode, s)` where
`value` reads mode. Required field on each case below; without it,
the goblin admits cases that *feel* frontier but actually reduce
(the fake unary merge dual).

## Forcing cases — two axes of variation

### Geometry split

- **Self-reach:** the act reaches its own evaluator. Cases #1, #3,
  #4, #5.
- **Backward-reach:** the act reaches across a boundary backward in
  time. Cases #2, #6.

Self-reach and backward-reach are different frontier geometries.
Pre-unifying them is a cathedral risk. Hold them separate.

### Most-important vs first-tractable (these are different cases)

- **#3 (self-certifying amendment) is load-bearing.** Its resolution
  determines whether the maximal calculus is even a consistent
  object. If self-certifying amendment can ever be admissible, gating
  collapses (the gate certifies its own dissolution); if it is never
  admissible, you have a foundational no-go theorem — probably the
  actual keystone of the maximal calculus, parallel to how
  value-sound gating was the keystone here.
- **#4 (standing mutation) is first formally tractable.** The
  substrate already gestures at standing through the actor /
  `Allowed` layer. Most-important and first-tractable being different
  cases is itself worth noting.

### Per-case fields

Each forcing case carries five fields:

1. **Failure shape** — what breaks under the bounded paper's
   assumptions.
2. **Cannot reduce to** — why Axes 1–2 cannot absorb it (the
   discriminator).
3. **Forced question** — the question the case opens, stated
   precisely.
4. **Refused decision** — what the register explicitly refuses to
   decide yet.
5. **Geometry** — self-reach or backward-reach.

---

### Case #1 — Value-function amendment

- **Failure shape.** The system mutates not state but `value` itself:
  what counts as defended changes mid-trajectory.

  ```
  Before: value = preserve audit trail
  After:  value = preserve throughput
  ```

- **Cannot reduce to.** A transition in product space `(value_id, s)`
  works if the *set* of available value functions is fixed at design
  time. Forces only when amendment introduces a value function that
  did not exist in advance.
- **Forced question.** Can a transition be admissible if it mutates
  the evaluator that will judge it?
- **Refused decision.** Whether value amendments are admissible at
  all; whether they require a meta-bridge; whether they have a
  fixed-point semantics.
- **Geometry.** Self-reach.

### Case #2 — Retroactive legitimation

- **Failure shape.** A later policy change attempts to make a
  previously inadmissible action admissible.

  ```
  t0: action fails bridge
  t1: policy changes
  claim: action was always fine
  ```

- **Cannot reduce to.** Axes 1–2 evaluate against the policy in force
  at action time; the bounded calculus has no backward-reach across a
  time boundary.
- **Forced question.** Amendment may govern future admissibility; may
  it launder prior failure without an explicit retroactivity witness?
- **Refused decision.** Whether retroactivity witnesses exist;
  whether they're admissible under restricted conditions; whether
  they require the original failure to be reclassified vs. truly
  repaired.
- **Geometry.** Backward-reach.
- **Connects to:** [[project-reflective-adoption-parked]] — the
  human-facing version ("adoption is not legitimation") is the same
  shape at a different altitude.

### Case #3 — Self-certifying amendment **(LOAD-BEARING)**

- **Failure shape.** The rule that authorizes amendment is itself
  amended by the same act.

  > "This action is valid because it changes the rules so that this
  > action is valid."

- **Cannot reduce to.** No fixed-value transition models this. The
  act IS the amendment of the standard that would judge it.
  Fixed-point / diagonalization regime.
- **Forced question.** Is self-certifying amendment ever admissible?
  If yes, gating collapses. If no, that's the foundational no-go
  theorem and probably the keystone of the maximal calculus.
- **Refused decision.** Everything. This case decides whether the
  maximal calculus is even consistent; the register refuses to
  pre-commit either way.
- **Geometry.** Self-reach (most pure form).
- **Status.** Load-bearing. Resolution shapes every other case.
  **Promoted to actively-worked 2026-06-01** via
  [`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md).
  Candidate no-go shape: well-foundedness via temporal priority
  (`P_i → P_{i+1}` admissible iff the act of amending is admissible
  *under `P_i`*, never under `P_{i+1}`). Distinguished failure
  named: founding events, structurally describable but
  non-blessable.

### Case #4 — Standing mutation

- **Failure shape.** The system changes who has standing to testify,
  authorize, bridge, or amend.

  ```
  Before: witness W has no standing
  After:  W is granted standing
  claim:  W's earlier testimony now counts
  ```

- **Cannot reduce to.** Standing is already in the substrate (actor /
  `Allowed` layer); mutating it is not a state transition under fixed
  standing. Forces when the *set* of admitted actors changes, not
  just which actor acts.
- **Forced question.** Does new standing attach prospectively only,
  or can it revive prior inadmissible evidence?
- **Refused decision.** Whether retroactive standing exists; whether
  it requires explicit witnesses; how it composes with retroactive
  legitimation (#2).
- **Geometry.** Self-reach (the system reaches into its own
  authorization layer).
- **Status.** First formally tractable case. Most likely the first to
  get Lean work, when forced. Bridges between formal calculus and
  institutional reading (enfranchisement, recognition, who counts as
  a witness).

### Case #5 — Crisis-mode value substitution

- **Failure shape.** A crisis condition swaps the defended value.

  ```
  Normal: value = preserve accuracy
  Crisis: value = preserve continuity
  ```

- **Cannot reduce to.** *Reduces to Axis 1* if the set of available
  values is fixed in advance — a transition in `(mode, s)` with
  `value` reading mode is just ordinary transition. **Forces only
  under value creation, not value selection.** The dual of the fake
  unary merge: if crisis introduces a value that did not exist at
  design time, it is frontier; if crisis selects from a fixed set, it
  is bounded.
- **Forced question.** What evidence licenses the *introduction* (not
  just the *selection*) of a new value basis?
- **Refused decision.** Whether crisis-driven value creation is
  admissible; whether it requires specific evidence shapes
  (proportionality, reversibility, sunset); how mode-transition
  admissibility interacts with the existing transition bridge.
- **Geometry.** Self-reach (if frontier) or Axis 1 (if reducible).
  The discriminator is itself load-bearing for this case.

### Case #6 — Reflective adoption without origin legitimation

- **Failure shape.** Human-facing relative of #2.

  ```
  Imposed obligation fails ingress.
  Subject later reflectively adopts it locally.
  Origin tries to claim the adoption as legitimation.
  ```

- **Cannot reduce to.** The bounded calculus has no "later adoption"
  predicate; locally-binding-without-origin-legitimation is a binary
  distinction the bounded paper does not formalize.
- **Forced question.** Can later local adoption create binding
  commitment without legitimating the originating structure?
- **Refused decision.** Whether reflective adoption is a primitive
  or composite; whether it has a Lean shape at all; whether it
  belongs in the maximal calculus or in a separate human-facing
  layer.
- **Geometry.** Backward-reach.
- **Connects to:** [[project-reflective-adoption-parked]] (full
  parked doctrine candidate); [[project-leased-coercion]].
- **Status.** Likely not first Lean. Likely belongs in the
  human-facing layer, not the formal calculus.

---

## Refused decisions (load-bearing)

The register explicitly refuses to decide:

- **Whether the maximal calculus is one object or several.** It is
  entirely possible the maximal "calculus" is plural — self-reach
  and backward-reach as different papers with different keystones,
  parallel to how transition and merge stayed plural in the bounded
  paper. Pre-committing to *the* maximal admissibility calculus as a
  single future object is itself a cathedral assumption.
- Whether `value` should be a field in state, an external parameter,
  a family over regimes, or something else.
- Retroactivity semantics: whether retroactive witnesses exist, what
  shape they have, when they're admissible.
- Whether self-certifying amendment is ever admissible (this is
  exactly #3's load-bearing question).
- Whether reflective adoption belongs in the formal calculus or in a
  separate human-facing layer.
- Which case is "first." Most-important (#3) and first-tractable
  (#4) are different cases; the order opens when a forcing case
  forces it.
- Any Lean shape. No modules, no predicates, no theorems.

## Promotion gate

A case promotes from "registered" to "actively worked" only when all
three hold:

1. A forcing case shows up in writing the value-sound-gates paper,
   in adversarial review, or in the wild.
2. The forcing case satisfies the discriminator (cannot reduce to
   ordinary transition/merge under fixed value).
3. The case clarifies *which* of the register's refused decisions it
   is forcing — i.e., the forcing case itself names which assumption
   broke.

Until all three: registered, not worked. The register stays a
register.

## Related records

- Paper spine:
  [paper-value-sound-gates-spine-2026-06-01.md](paper-value-sound-gates-spine-2026-06-01.md)
  (especially *"For the pocket — Axis 3 boundary as seam, not wall"*).
- Paper draft v1:
  [paper-value-sound-gates-draft-2026-06-01.md](paper-value-sound-gates-draft-2026-06-01.md).
- Keystone verdict:
  [axis-2-cross-axis-keystone.md](axis-2-cross-axis-keystone.md).
- Reflective adoption (parked):
  [tooltheory/reflective-adoption-not-origin-legitimation.md](tooltheory/reflective-adoption-not-origin-legitimation.md).
- Memory: [[project-cross-axis-keystone]] (value-sound gating; Axis 3
  OUT); [[project-paper-naming-stack]] (current paper ≠ maximal
  calculus); [[project-reflective-adoption-parked]].
