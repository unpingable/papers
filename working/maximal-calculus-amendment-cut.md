# Maximal calculus — the amendment cut and the mutable-value retype

**Status:** Working note, filed 2026-06-01. Forcing-case promotion of
register case #3 (self-certifying amendment, load-bearing). Carries
candidate first axiom **(A1)**: a transition from `S` to `S′` is
authorized only if its authorization witness is valid in `S`, not
introduced by `S′` — the lift of the Fixed-Value Fragment's
`AuthStep E s` type-level discipline into the regime where the
authorization predicate is itself part of state. Substrate-level
only; no Lean. Sibling to
[`maximal-calculus-forcing-cases.md`](maximal-calculus-forcing-cases.md)
(register) and
[`maximal-calculus-plan-prompt.md`](maximal-calculus-plan-prompt.md)
(plan-prompt).

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

Candidate, not ratified. The plan-prompt's refused decisions still
hold — one calculus or several, `value`'s location, retroactivity
semantics, case ordering, none pre-decided here. What the axiom
does is name the structural constraint the calculus must satisfy
at minimum, lifted from the fragment's already-checked discipline.
Whether (A1) is *the* first axiom or one of several, whether it
ratifies as stated or sharpens under contact with case #4
(standing mutation) or case #5 (crisis substitution), is open.

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
*actively worked*, per the plan-prompt's promotion gate:

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

None of these is committed work. The register's *file-now-work-never*
discipline still applies. The promotion of case #3 to *actively
worked* means the structural condition is now named; it does not
mean implementation has started.

## Related records

- Register: [`maximal-calculus-forcing-cases.md`](maximal-calculus-forcing-cases.md)
- Plan-prompt: [`maximal-calculus-plan-prompt.md`](maximal-calculus-plan-prompt.md)
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
