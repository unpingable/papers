# Maximal calculus — founding events

**Status:** Candidate, agent-drafted 2026-06-02, not ratified.

Working-note sibling to
[`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md).
Records the well-foundedness condition's *distinguished failure
mode* — the transition for which no prior policy exists. Sibling to
[`maximal-calculus-discharge-connection.md`](maximal-calculus-discharge-connection.md);
both notes track structural features the kernel specimen at
`~/git/lean/LeanProofs/Admissibility/AmendmentFragment.lean` carries
but cannot themselves resolve.

## The shape

From amendment-cut.md §"The distinguished failure":

> The well-foundedness condition has exactly one distinguished
> failure mode: the transition for which no prior policy exists.

The founding of a polity. The revolutionary establishment of a new
order. The coup that installs a regime by an act not authorized
under the regime it replaces. Each is a *real* transition — the
regime that follows actually exists; the polity it constitutes
actually constitutes — but no prior policy authorizes the act that
installed it.

The (A1) discipline at the kernel level is *binary*: either the
witness is at the source policy, or no `Transition E S` exists. The
founding case is the one structural shape this binary cannot
handle: there is no source policy to be the witness's index, so
neither inhabits.

The calculus's structural admission: *describable, not blessable*.

## The kernel's encoding

In `LeanProofs/Admissibility/AmendmentFragment.lean`, the founding
case lives in a separate type:

```lean
structure FoundingTransition (Policy Op : Type) (S : State Policy) where
  op : Op
  newPolicy : Policy
```

with three load-bearing absences:

1. **No `evidence` field.** Unlike `Transition E S`, a
   `FoundingTransition` carries no `AuthEvidence`. The type
   literally cannot record "authorized under …"
2. **No env parameter.** `FoundingTransition` has no `E :
   AmendmentEnv …` in its type. Founding transitions are
   meta-environment — they precede the env that would later
   describe them. The `newPolicy` field records what was installed;
   it is *not* constrained to equal `E.applyOp S op` for any `E`.
3. **No constructor route from `FoundingTransition` to
   `Transition`.** The two types are not coerced; the
   non-blessability lives in this structural silence.

The kernel proves the negative half:

```lean
theorem founding_does_not_bless (f : FoundingTransition Policy Op S)
    (hno_pre : ¬ E.Validates S.policy f.op) :
    ¬ ∃ t : Transition E S, t.op = f.op
```

— *given* the founding record and the failure of pre-state
authorization, no transition with the founding's op exists. This is
non-blessability under failed pre-authorization; it is not a
no-coercion theorem (per the codex A.6 review log; that would
overclaim, since external evidence could in principle exist for the
same op).

## The cost the calculus pays

The maximal calculus distinguishes legitimate amendment from
laundering, but the cost is acknowledging that some transitions in
history are neither — they are *foundings*, structurally
describable and structurally non-blessable. A calculus that
pretends to bless foundings is laundering generalized; a calculus
that pretends foundings do not exist is the fixed-value fragment
fenced too tightly.

The founding case is the calculus's confession that its scope is
legitimacy, not history. History contains transitions the calculus
calls real but cannot license. That confession is what the calculus
offers in exchange for being able to draw the
amendment-vs-laundering cut at all.

## Adjacent shape: reflective adoption at the constitutional layer

Per [[project-reflective-adoption-parked]], the human-facing
non-arrow is *"adoption ↛ origin legitimation."* The shape rhymes
with the founding case at the constitutional layer:

- **Reflective adoption (human-facing):** local actor accepts
  imposed obligation; system tries to read acceptance as
  legitimation of the imposing structure. The non-arrow blocks the
  laundering.
- **Founding (constitutional):** new regime is installed without
  pre-state authority; later operations under the new regime are
  *internally* admissible. The non-arrow blocks reading "post-
  founding admissibility" as "founding was authorized."

The open question: is the founding case *reflective adoption at the
constitutional layer*? Or is it a separate primitive — describable
non-blessability — that happens to share the structural shape of
"later admissibility ↛ origin legitimation"?

The parked-adoption note explicitly says *guard the door, don't
furnish the room.* The founding case is the door's other side: the
room exists, the room is real, but the door's certificate of
admission cannot be issued retroactively. Whether that's the same
primitive or a sibling is filed as open.

Per the plan's stop conditions, this is operator territory. Do not
attempt to merge or distinguish here.

## What this note does NOT do

- Does not claim foundings are admissible. The calculus's whole
  point is that they are not — and that this non-admissibility is a
  feature.
- Does not propose new Lean modules. The kernel specimen's
  `FoundingTransition` is the founding case's full kernel-level
  treatment. Anything richer would require operator ratification
  of the well-foundedness condition as keystone.
- Does not reify the founding case as a paper. The founding case
  is one structural feature of the maximal calculus; whether it
  earns its own paper or sits inside a larger one is the same
  one-calculus-or-several question the register refuses to
  pre-decide.
- Does not enumerate historical foundings. The point of
  *describable, not blessable* is that the calculus can name any
  founding — but the calculus has nothing distinctive to say about
  *which* foundings to name. That's historiography, not formal
  semantics.

## Cross-references

- [`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md) —
  §"The distinguished failure," the founding case's structural
  surfacing.
- [`maximal-calculus-discharge-connection.md`](maximal-calculus-discharge-connection.md) —
  sibling note on the true-but-inadmissible cut.
- [`maximal-calculus-codex-review-log.md`](maximal-calculus-codex-review-log.md) —
  Phase A.6 codex review of the `FoundingTransition` type and the
  `founding_does_not_bless` theorem, including the integration of
  codex's findings on theorem-prose mismatch and operational
  under-specification.
- [[project-reflective-adoption-parked]] — the adjacent
  human-facing shape; open question whether it's the same primitive
  or a sibling.
- [[project-cross-axis-keystone]] — Axes 1–2 closure context;
  reminder that Axis 3 is OUT and this note does not promote
  toward it.
