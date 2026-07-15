# Maximal calculus — the amendment cut and the mutable-value retype

**Status:** Working note, filed 2026-06-01. Forcing-case promotion of
register case #3 (self-certifying amendment, load-bearing). Carries
candidate first axiom **(A1)**: a transition from `S` to `S′` is
authorized only if its authorization witness is valid in `S`, not
introduced by `S′` — the lift of the Fixed-Value Fragment's
`AuthStep E s` type-level discipline into the regime where the
authorization predicate is itself part of state. Operational form of
(A1) landed via multi-model exchange 2026-06-01: `Authorized_S(O)`
vs. `Authorized_{S′}(O)` as the working test, with pre-authorized
mutation named as superclass (#4 = standing-mutation subcase),
receipt-gated decomposition for future-witness laundering, and the
explicit non-pruning verdict that other pre-authorized mutations
remain maximal candidates pending the reduction discriminator.
Substrate-level only; no Lean. Sibling to
[`maximal-calculus-forcing-cases.md`](maximal-calculus-forcing-cases.md)
(register) and
[`maximal-calculus-decomposition-trigger.md`](maximal-calculus-decomposition-trigger.md)
(forcing-gated decomposition protocol, dormant).

**Provenance.** Claude-web analysis (2026-06-01), surfaced after the
DeepSeek-class adversarial review of the bounded fragment closed
out. ChatGPT independently arrived at the same fork between
standalone publication and substrate posture and recommended
walking through to the actual calculus rather than polishing the
fragment further. This note captures the structural obstruction
that claude-web identified as the calculus's first content.

The fragment review wave's load-bearing finding was that the
fragment's value was substrate discipline, not theorem heroics. The
work that follows is what the substrate exists to enable — the
regime where the value function itself becomes part of what
mutates, and the comparison operator the fragment relied on is no
longer well-typed.

## The obstruction: `≤` is ill-typed under mutable value

In the bounded fragment, soundness theorems compare value across
states using `≤`:

```
bridge_implies_safe : bridge s a → value s ≤ value (run s a)
bridgedTraj_preserves : BridgedTraj E s s' → value s ≤ value s'
```

§5.1 of the fragment makes the implicit hypothesis explicit: *the
function is the same function at each reading*. The `≤` relation
compares quantities computed by the same value function applied to
different states.

The moment `value` becomes mutable — when amendment can replace the
value function itself — that comparison is ill-typed. `value_{P₀} s`
and `value_{Pₙ} s'` are measured under different evaluators. The
expression `value_{P₀} s ≤ value_{Pₙ} s'` is not a proposition the
fragment defines; it is a category error the fragment has been
quiet about because the fragment fenced it off.

The first structural fact of the maximal calculus is that this
category error cannot be silently elided. Retyping `≤` is not a
stylistic choice. *Each available retyping is a stance on
retroactive legitimation.*

## The three retypings

**Source-relative.** Judge every state by `P₀`, the policy in force
at the trajectory's start. Comparison is `value_{P₀} s ≤ value_{P₀}
s'`. No amendment can ever change what is preserved or improved by
the lights of the original evaluator — the trajectory is frozen at
t = 0 forever.

This retyping forbids all legitimate evolution, not just laundering.
Constitutional amendments to clean up obvious injustices fail by the
old lights, even when the new lights are unambiguously better. The
source-relative retyping is the maximally conservative reading of
the fragment's fence; it is degenerate because it confuses *the
function does not mutate* with *the function from t = 0 is always
the right reading*.

**Sink-relative.** Judge every state by `Pₙ`, the policy in force at
the trajectory's end. Comparison is `value_{Pₙ} s ≤ value_{Pₙ} s'`.
Any historical decrease is blessable by amending the evaluator to
bless it.

This is laundering *as the type signature*. The retyping does not
permit laundering as an edge case; it makes laundering the default.
Sink-relative legitimation is teleological: the present rewrites the
past by changing the lights you are reading the past by. The
fragment's fence against retroactive legitimation is not a separate
prohibition; it is an artifact of the fragment's refusal to type
`≤` this way.

**Trajectory-coherent.** Judge each step by the policy in force at
that step. The hop from `s` under policy `P_i` to `s'` under policy
`P_{i+1}` is preserved when `value_{P_i} s ≤ value_{P_{i+1}} s'`,
modulo a characterization of when the policy-shift `P_i → P_{i+1}`
is itself an admissible amendment.

This is the only live retyping. And it carries its own recursion:
the gate on policy-changes is itself a policy — call it `Q` — and
`Q` is itself subject to amendment. The recursion does not stop at
any finite depth by syntactic restriction. The fragment's
fixed-value fence is the boundary condition that makes the
recursion vacuous (no value changes, no recursion).

## The break: well-foundedness via temporal priority

The recursion is broken not by stopping at depth but by changing the
direction of the dependency. The amendment `P_i → P_{i+1}` is
admissible iff the *act of amending* — the transition that installs
`P_{i+1}` — is admissible **under `P_i`**, never under `P_{i+1}`.

> Authority is temporally prior to the rule it authorizes.

Constitutional language: ratify under the old procedure, not the
one you are installing. The well-foundedness is in time and
authority, not in syntax: each amendment points backward, never
forward, for its admissibility. The recursion terminates because
each step's admissibility is delegated to a strictly earlier
policy.

This is the formalization the register's case #3 (self-certifying
amendment) predicted would shape the calculus's content. The
register identified case #3 as the case whose resolution determines
whether the maximal calculus is even a consistent object. The
well-foundedness condition is a candidate answer:

> An amendment is admissible iff its installation is admissible
> under the policy it amends.

In contrapositive: an amendment that authorizes itself — the *"this
action is valid because it changes the rules so that this action is
valid"* pattern from the register's case #3 — is *not* admissible.
The well-foundedness condition is constructive; it says when
amendments are admissible. The exclusion of self-certifying
amendment is a corollary.

## The candidate first axiom

The fragment's `AuthStep E s` already enforces this discipline at
the type level. The `allowed : E.Allowed s actor act` field is
typed against `s` (the source state), not the destination. The
authorization witness must be constructible from `S`, full stop.
When `E.Allowed` is environmental — a field of `SafetyEnv`, not of
`σ` — the constraint is automatic: no `Allowed` from `S′` can
substitute, because none exists at that altitude. The fragment's
fence keeps the authorization predicate environmental so the
constraint never has to be stated. It only has to be honored by the
type.

The maximal calculus's candidate first axiom is the lift of the
fragment's type-level discipline into the regime where the
authorization predicate is itself part of state:

> **(A1)** A transition from `S` to `S′` is authorized only if its
> authorization witness is valid in `S`, not introduced by `S′`.

This is the well-foundedness condition above, stated at the
transition altitude the fragment already operates at, with no
separate policy object required. When `S` carries the policy `P_i`
and `S′` carries `P_{i+1}`, "valid in `S`" means "valid under
`P_i`," and "introduced by `S′`" means "validated by `P_{i+1}` for
the first time." The user's transition-level statement and the
policy-level well-foundedness condition are the same constraint at
different altitudes — the axiom lives at the cleaner one because it
generalizes the fragment's existing type signature directly rather
than positing a new structural object.

The axiom is the explicit form of what the fragment kept implicit
by holding the policy still. Lifting `AuthStep E s` into the
mutable-policy regime: the same type-level constraint becomes the
calculus's first content. *The witness must be valid in `S`, not
introduced by `S′`.* The fragment's authorization gate,
generalized.

Candidate, not ratified. The register's refused decisions still
hold — one calculus or several, `value`'s location, retroactivity
semantics, case ordering, none pre-decided here. What the axiom
does is name the structural constraint the calculus must satisfy
at minimum, lifted from the fragment's already-checked discipline.
Whether (A1) is *the* first axiom or one of several, whether it
ratifies as stated or sharpens under contact with case #4
(standing mutation) or case #5 (crisis substitution), is open.

## Operational form of (A1): the #3/#4 discriminator

The abstract form of (A1) and the structural distinction between
cases #3 and #4 were both stated above. A multi-model exchange
(DeepSeek-style adversarial fresh context + ChatGPT-style
refinement + author intervention, 2026-06-01) operationalized the
discriminator into a falsifiable invariant, then caught two
symmetric over-corrections: a tendency to let #4 absorb every
pre-authorized mutation, and a tendency to prune the maximal
register down to *"only #3 and #4 survive."*

The keeper statement:

> **The decisive question is not whether admissibility inspects the
> post-state. The decisive question is whether the authority used to
> admit the operation existed before the operation, or is produced
> by the operation itself.**

### The invariant

Let `Authorized_S(O)` denote that operation `O` is admissible under
the authority / evaluator valid in pre-state `S`. Let
`S′ = apply(O, S)`. Then:

- **Pre-authorized mutation.** `Authorized_S(O)` holds. `O` may
  alter any future structure in `S′` — standing, procedure,
  threshold, evaluator, value location, jurisdiction, what counts as
  a receipt or witness. *Pre-authorized mutation is a superclass,
  not itself a verdict that the operation is bounded-paper work.*
  - **#4 Standing mutation** (subcase). `O` alters standing,
    eligibility, or jurisdiction for later operations.
- **#3 Self-certifying amendment.** `¬ Authorized_S(O)`, yet
  `Authorized_{S′}(O)` would hold under the new authority that `O`
  itself installs in `S′`. The operation's admissibility flows from
  authority it brings into existence.
- **Invalid laundering.** `¬ Authorized_S(O)`, and the claimed
  witness is neither valid in `S` nor validly produced by a
  receipt-gated later transition.

Keeper line for the core seam:

> **#4 changes who may act next. #3 tries to become the reason it
> was allowed to act now.**

This is (A1)'s working test. The axiom said: a transition's witness
must be valid in `S`, not introduced by `S′`. The discriminator
says: when the witness is missing in `S` but present in `S′` as a
consequence of `O`, the operation is #3 — exactly the (A1)
violation.

### The first-pass invariant and why it failed

The exchange's first candidate — *"admissibility depends essentially
on `S′` in a self-referential way"* — caught too much. Post-state
dependence is not the villain. The narrow villain is *post-state
authority being used to authorize the transition into that
post-state*. The refined invariant locates the discrimination at
the evaluator, not at the predicate's reference. (A1) is consistent
with predicates that examine `S′`; it is not consistent with
authorities that only exist in `S′`.

### Worked examples

**Case A — threshold amendment.** Current rule: amendments need
60%. Proposed: *"From now on, amendments need 50%. This amendment is
valid if it receives 50%."*

- ≥60%: `Authorized_S(O)` under the old 60% rule. **Pre-authorized
  mutation of procedural authority** — the threshold is
  procedural-rule structure, not standing. Not automatically #4;
  only #4 if this system treats threshold as standing (it usually
  doesn't).
- 50–59%: `¬ Authorized_S(O)` (fails 60%); `Authorized_{S′}(O)`
  under the new 50% rule `O` installs. → **#3**.
- <50%: invalid under both.

The case demonstrates the superclass/subtype distinction: a single
operation can be pre-authorized at one vote level and
self-certifying at another, but pre-authorized ≠ #4. #4 applies
only when the mutation specifically targets standing.

**Case B — delegation requiring future acceptance.** *"Delegate
authority to `D` now, valid only if `D` confirms within 1 minute."*

The single-step form ("delegate now, contingent on future receipt")
is ill-formed under (A1). The honest decomposition is three
sub-operations:

- **B1. Create pending delegation.** `Authorized_S(O_1)` is true
  under pre-state superuser authority. Not #3, not #4 (unless the
  pending status itself mutates standing). Receipt-gated protocol
  pattern.
- **B2. Activate delegation after the acceptance receipt arrives.**
  `Authorized_{S_t}(O_2)` holds in the later state `S_t` where the
  receipt exists. Receipt-gated transition.
- **B3. Activate the delegation now on the basis of an anticipated
  future receipt.** `¬ Authorized_S(O)`. The future receipt has not
  yet been issued; the authority does not exist. **Future-witness
  laundering** — an invalid laundering attempt that mimics
  admissibility by deferring its witness to a future state. Not a
  new maximal category; just an (A1) violation by a different route.

Keeper line:

> **A future receipt can authorize a later transition. It cannot
> authorize the transition that creates the need for the receipt.**

"Receipt-gated" is not a new maximal entry. It is a protocol
pattern `(O_1 → wait → O_2)` under which each phase is independently
judged by the discriminator.

**Case C — postcondition rule.** *"A rule change is admissible iff
the changed rule's value > 0."*

- If the postcondition predicate is *already in* `S`:
  `Authorized_S(O)` evaluated by pre-state authority whose predicate
  examines `S′`. The evaluator stays in `S`. → **postcondition-gated
  mutation**.
- If the postcondition predicate is *introduced by* `O`:
  `¬ Authorized_S(O)`; `Authorized_{S′}(O)` under the new rule. →
  **#3**.

The postcondition-gated form is *only* maximal if it fails the
reduction discriminator:

> Can the postcondition be expressed as an ordinary transition
> invariant under fixed value, including product-space encodings
> such as `(mode, s)`?

If yes (the password-length example: *"valid iff length ≥ 12"*), it
belongs to bounded-paper territory. If no, it remains a maximal
candidate distinct from #3 and #4.

### The non-pruning verdict

A symmetric failure mode threatened the consolidation. Just as the
first-pass invariant caught too much by treating post-state
dependence as the villain, the consolidation tried to land on
*"only #3 and #4 survive as distinct maximal categories."* That
over-prunes.

Pre-authorized mutations of structures the bounded Fixed-Value
Fragment does *not* hold environmentally — the evaluator, value
location, retroactivity semantics, slice boundaries, the definition
of receipt or witness — may still be maximal. They are not
automatically maximal; each must pass the reduction discriminator
independently. The invariant separates #3 from #4. It does not
decide the whole register.

> **#3 and #4 are now cleanly distinguished. Other candidates are
> not automatically maximal; they must pass the reduction
> discriminator independently.**

### Decision procedure

For any candidate operation:

1. **Is `Authorized_S(O)` true?**
   - *No.* Check: would `Authorized_{S′}(O)` be true only because
     `O` installs or alters the authority/evaluator structure by
     which `O` itself is judged?
     - If yes → **#3 self-certifying amendment**.
     - If no → **invalid laundering**, unless decomposable as a
       receipt-gated protocol where the first phase is pre-authorized
       (Case B's B1/B2 form).
   - *Yes.* `O` is pre-authorized.
     - Does `O` mutate standing / eligibility / jurisdiction? →
       **#4 standing mutation candidate; it still owes the
       maximal/bounded reduction argument.**
     - Otherwise → apply the reduction discriminator. If `O` reduces
       to ordinary transition or merge under fixed value (including
       product-space `(mode, s)` representations), it is
       bounded-paper work. If not, it is a candidate maximal case
       distinct from #3 and #4 — name it by what it mutates
       (evaluator, value location, retroactivity semantics, slice
       boundaries, receipt definition, etc.).

The "only because" wording is load-bearing. Self-certification is
not that the new authority is the *exclusive* input to `O`'s
admissibility; it is that the new authority is *necessary* — that
without `O`'s own installation, `O` would not authorize. A mix of
pre-existing substrate and newly installed authority still counts
as #3 if the new authority is what carries the verdict over the
line.

The #4 caveat is the symmetric guard. Some standing mutations may
still encode cleanly under fixed value or `(mode, s)` product-space;
#4 owes the reduction argument like everything else. The number
does not make the case sacred.

> **The invariant distinguishes #3 from #4. The discriminator
> distinguishes maximal from bounded. Do not conflate the two.**

That sentence is the whole point.

### What this clarifies

(A1) in its abstract form: *witness valid in `S`, not introduced by
`S′`*. The operational discriminator gives the working test:
*locate the evaluator*. If the evaluator is in `S` (even when its
predicates examine `S′`), the operation is on (A1)'s good side. If
the evaluator only becomes valid as a consequence of `O` and judges
from `S′`, the operation is on (A1)'s bad side — and that is the
precise structural shape of #3.

The decision procedure leaves space for pre-authorized mutations of
the bounded fragment's environmental fences — the evaluator, value
location, and so on — to remain maximal candidates pending the
reduction test, rather than auto-demoting them. The fragment kept
those structures still by environmental fencing; the maximal
calculus must inherit a decision about each. The discriminator does
not pre-decide which are bounded-reducible and which are not.

### Falsifiability

The invariant is falsifiable. It fails if:

- An operation exists with `¬ Authorized_S(O) ∧ Authorized_{S′}(O)`
  that does *not* count as self-certifying amendment under
  intuitive reading.
- #4 collapses into #3 under some constructive reduction (for
  example, if mutating standing turns out to always implicitly
  install the standing-evaluator).
- A pre-authorized mutation of an environmental structure
  (evaluator, value location, etc.) turns out to *always* reduce to
  ordinary transition or merge under fixed value — collapsing the
  "candidate maximal" space back to {#3, #4} and validating the
  symmetric over-pruning the verdict above rejected.

None has been exhibited. All remain open tests.

## The distinguished failure: founding events

The well-foundedness condition has exactly one distinguished failure
mode: the transition for which no prior policy exists.

The founding of a polity. The revolutionary establishment of a new
order. The coup that installs a regime by an act not authorized
under the regime it replaces. Each of these transitions is *real* —
the regime that follows actually exists; the polity it constitutes
actually constitutes — but no prior policy authorizes the act that
installed it. There is no `P_0` to certify the amendment that
installs `P_1`.

The calculus can *describe* this transition. It can name it: the
non-admissible-but-actual transition. It cannot *bless* it. An
honest calculus carries the founding case as a named exception, not
as a gap pretended away.

This is the load-bearing structural finding: the maximal calculus
distinguishes legitimate amendment from laundering, but the cost is
acknowledging that some transitions in history are neither — they
are *foundings*, structurally describable, structurally
non-blessable. A calculus that pretends to bless foundings is
laundering generalized; a calculus that pretends foundings do not
exist is the fixed-value fragment fenced too tightly.

The founding case is the calculus's confession that its scope is
not history but legitimacy. History contains transitions the
calculus calls real but cannot license. That confession is what the
calculus offers in exchange for being able to draw the
amendment-vs-laundering cut at all.

## Connection: discharge as sink-relative legitimation

The discharge tension already carried this structure, scoped to
obligations rather than to value functions. Per
[[project-continuous-admissibility-discharge]], the
corporate-bankruptcy-discharge primitive declares prior obligations
void by post-amendment policy: the policy in force after discharge
says the obligation no longer exists, and the past comparison "did
the obligor preserve their obligation?" is read by the new lights,
not the old.

This is sink-relative legitimation living inside the discharge
primitive. The question "is corporate bankruptcy laundering or
legitimate?" is the question "is the discharge amendment
well-founded under the policy it replaces?" — exactly the maximal
calculus's cut.

The discharge memory's framing — *true but inadmissible*, mercy is
jurisdictional, not epistemic — is the calculus's content in
miniature. Discharge says: the prior obligation was real, but the
post-discharge policy makes it inadmissible. The amendment is
well-founded under the prior policy (bankruptcy procedure is itself
ratified under non-bankruptcy law). The cut between *true but
inadmissible* (legitimate amendment) and *retroactively erased*
(laundering) is exactly what the well-foundedness condition
formalizes.

The maximal calculus, in this reading, is the generalization of the
discharge primitive from obligations to value functions. The
discharge essay was already circling the calculus's first theorem.
What the discharge essay needs as a primitive — *purpose-bound
routing prohibition, true info retained under a rule forbidding
specified future uses* — the maximal calculus needs as a theorem:
the prior obligation is real, the new policy makes it inadmissible,
and the move from old policy to new policy is itself admissible
under the old.

## Mapping onto the forcing-case register

This note constitutes forcing-case promotion of **case #3
(self-certifying amendment, load-bearing)** from *registered* to
*actively worked*, per the register's promotion gate:

1. **Forcing case shows up.** ✓ — claude-web's analysis identifies
   the structural obstruction.
2. **Satisfies the discriminator.** ✓ — the ill-typed `≤` cannot be
   represented as ordinary transition or merge under fixed value,
   nor as a `(mode, s)` product-space transition where value reads
   mode. The value function itself mutates; no fixed-value
   representation suffices.
3. **Names which refused decision broke.** ✓ — the externality of
   `value` from `σ`. The maximal calculus needs `value`'s function
   identity, not just its outputs, to be part of what the gate
   gates.

The note also engages neighboring register entries without
promoting them:

- **Case #1 (value-function amendment, self-reach).** This is the
  regime claude-web's analysis directly addresses. The mutable-value
  retype *is* case #1's failure mode. Case #1's resolution is
  downstream of the well-foundedness cut: amendment is admissible
  iff its installation is admissible under the prior value function.
- **Case #2 (retroactive legitimation, backward-reach).**
  Sink-relative retyping IS retroactive legitimation as type
  signature. The "later policy change makes earlier failure
  admissible" pattern is what sink-relative reads as default.
- **Case #5 (crisis-mode value substitution, self-reach).** Lives
  inside trajectory-coherent retyping. Crisis substitution is
  admissible iff the substitution is itself admissible under the
  pre-crisis value function — which sometimes it isn't, and the
  calculus has to name when.
- **Case #6 (reflective adoption without origin legitimation,
  backward-reach).** Sibling of case #2 at the human-facing layer;
  same well-foundedness shape, different substrate. The
  [[project-reflective-adoption-parked]] memory's *"adoption ↛
  origin legitimation"* non-arrow is the well-foundedness condition
  expressed at the receipt layer.

The remaining open register entry — **case #4 (standing mutation,
first-tractable)** — is not directly addressed here but is
constrained by the same shape: standing mutation is admissible iff
installed under the prior standing policy. Whether the
well-foundedness condition applies cleanly to standing is an open
test of the condition's reach.

## What this note does NOT do

- Does not build kernel specimens. *Court first, map later* per
  [[feedback-kernel-vs-process-calculus]]. The next move is at most
  a small specimen exploring the well-foundedness condition's
  type — not a process-calculus namespace.
- Does not propose a paper. The fragment's review wave settled that
  the next artifact is not a publication; it is substrate.
- Does not ratify the well-foundedness condition as *the* keystone
  of the maximal calculus. The condition is a candidate articulated
  by claude-web's analysis and confirmed against the register's
  case-#3 prediction. Ratification waits on either a kernel specimen
  or a second independent surface that confirms the condition's
  reach.
- Does not absorb case #4. Case #4 is the first-tractable case per
  the register; the well-foundedness condition is a candidate for
  case #3's no-go but its application to case #4's standing layer
  is not pre-decided here.
- Does not preempt the maximal calculus's title. The
  [[project-paper-naming-stack]] slot reservation stands; the title
  remains reserved until the calculus's content is established
  beyond a single forcing-case promotion.

## Next moves (candidate, not committed)

1. **Kernel specimen of well-foundedness.** A minimal Lean specimen
   carrying a state type with a current policy, a transition that
   may amend the policy, and a soundness theorem stating the
   amendment is admissible iff the amendment-action is admissible
   under the prior policy. Small. Scratch / not-promoted-to-1.0.
   Probably sibling to existing `LeanProofs/Admissibility/` modules.
2. **Discharge connection note.** A short note formalizing the
   discharge-as-sink-relative-legitimation reading and the cut
   between *true-but-inadmissible* (legitimate amendment) and
   *retroactively-erased* (laundering). Check the discharge essay
   candidate before duplicating.
3. **Founding-event handling.** A separate note on the distinguished
   failure: how the calculus carries the founding case as a named
   non-blessable transition. The reflective-adoption-parked memory
   has adjacent shape; check whether the founding case is reflective
   adoption at the constitutional layer.
4. **Case #4 instantiation.** Test whether the well-foundedness
   condition applies cleanly to standing mutation. If it does, that
   is evidence the condition's reach is general; if not, the
   condition needs refinement.

None of these is committed work or an automatic queue. A coherent per-kernel theorem
or countermodel may be developed before a runtime case and may lead implementation;
the unified maximal calculus remains refused. The promotion of case #3 to *actively
worked* means the structural condition is now named; it does not itself establish
runtime integration or public promotion.

## Related records

- Register: [`maximal-calculus-forcing-cases.md`](maximal-calculus-forcing-cases.md)
- Decomposition trigger:
  [`maximal-calculus-decomposition-trigger.md`](maximal-calculus-decomposition-trigger.md)
  (forcing-gated protocol; dormant artifact)
- Fragment (closed against the seam this note crosses):
  [`paper-value-sound-gates-spine-2026-06-01.md`](paper-value-sound-gates-spine-2026-06-01.md),
  [`paper-value-sound-gates-draft-2026-06-01.md`](paper-value-sound-gates-draft-2026-06-01.md)
  (parked as working axis note)
- Memory:
  - [[project-continuous-admissibility-discharge]] — the existing
    instance the calculus generalizes from
  - [[project-reflective-adoption-parked]] — backward-reach sibling
    at the human-facing layer
  - [[project-cross-axis-keystone]] — fragment's value-sound gating
    keystone (Axes 1–2 closure)
  - [[project-boundary-calculus-program]] — broader program at a
    different altitude
  - [[project-paper-naming-stack]] — title reservation preserved
  - [[feedback-kernel-vs-process-calculus]] — court first, map later
  - [[feedback-forcing-case]] — forcing-case discipline
