# Reflective adoption is not origin legitimation

**Status:** PARKED doctrine candidate (2026-06-01). Out of current Lean scope.
Not part of BoundaryWitness / Axis 2 extraction. Not an Axis 3 promotion.
Filed here to preserve the primitive without contaminating the in-flight
Axes 1–2 closure.

**Scope fence (load-bearing — read first):**

- NO Lean changes for this primitive yet.
- NO modification of `BoundaryWitness.lean` or `ParameterizedMerge.lean` to
  accommodate it.
- NO Axis 3 (self-amendment) promotion; this primitive is *neighboring* to
  the human-facing / HITL / self-amendment layer but is NOT a license to
  open Axis 3 work.
- NO paper reframe around it.
- Promotion gate: current Axes 1–2 calculus closes first. After that, this
  candidate gets a generator test like any other primitive
  ([[project-boundary-calculus-program]], [[feedback-primitive-ratification-gate]]).

---

## Core claim

> **Adoption is not legitimation.**

Reflective adoption can mint *scoped local commitment*, but it must not
legitimate the origin, create precedent, or convert imposed burden into
general duty.

## Distinction

Two registers an obligation can sit in. Collapsing them is the laundering
move this primitive guards against.

### Imposed / extractive obligation

The obligation arrives without authority over the subject. The proper
disposition is:

- Containerize (don't let it spread).
- Mark debt (the obligation is on someone's ledger, not the subject's).
- Deny authority creation (carrying the obligation does not grant the
  source authority over the subject or class).
- Require exit criteria (the obligation is not perpetual; conditions for
  release are nameable).

### Reflectively adopted obligation

The subject, after the fact and with the cost visible, chooses to carry
the obligation as locally binding. The proper disposition is:

- Locally binding (yes, the subject is committed).
- Scoped to subject and terms (not a universal duty for similar
  subjects).
- Without retroactive legitimation of the origin (the source is not
  vindicated by the adoption).
- Revocable / renegotiable under named conditions.
- Non-precedent: adoption does not authorize future dumping on the same
  subject or others.

## Candidate predicate shape (informal — NOT Lean yet)

```
ReflectiveAdoption(subject, obligation)
  → LocallyBinding(subject, obligation)

ReflectiveAdoption(subject, obligation)
  ↛ OriginLegitimate(obligation.origin)

LocallyBinding(subject, obligation)
  ↛ GeneralizableDuty(class(obligation))
```

The first arrow is what makes adoption real (the yes does mint
commitment). The second and third are what keep it from being laundered
into authority for the origin or duty for the class.

## Candidate primitive — `ReflectiveAdoption`

Fields (informal, parking only):

- `object` — what is being carried.
- `subject` — who adopts it.
- `cost_seen` — adoption is post-cost-visible, not pre-cost-blind.
- `origin_status` — illegitimate / accidental / tragic / exploitative /
  unknown. NOT erased by adoption.
- `scope` — what exactly is adopted.
- `terms` — limits of the commitment.
- `revocation` — how it stops or is renegotiated.
- `non_precedent` — adoption does not authorize future dumping.
- `no_origin_laundering` — adoption does not legitimate the source.

The last two fields are load-bearing. Without them, the adoption receipt
becomes a laundering receipt.

## HITL hosts this; does not supply it

Human-in-the-loop is just where a human enters the control loop. It does
not tell you whether the human is consenting, complying, being cornered,
choosing, enduring, blessing, dissociating, or clicking "approve" because
the pager is screaming.

> "Human approved" is not adoption. At most, a witnessed intervention.

The trap is treating HITL as a moral adapter: machine creates bad
obligation → human touches it → now it is legitimate. That is laundering
with a warm mammal in the loop.

What good HITL design *can* distinguish (each producing a different
receipt):

- **Approve as authorized** — the system may proceed.
- **Accept as local burden under protest** — proceed now, no authority
  created.
- **Adopt as scoped commitment** — I choose this as mine, within scope.
- **Reject / escalate**.

Most systems collapse all four into "approved." That's the laundering
machine wearing a UX badge.

The formalism's job is *authority routing*, not encoding belovedness /
vocation / love. The formalism can guard the door; it cannot furnish the
room. That line is the scope boundary — keeping it is the point.

## Why this is parked, not built

Three reasons:

1. **Current closure is Axes 1–2.** Building this now would contaminate
   the in-flight `BoundaryWitness.lean` keystone work and the
   `ParameterizedMerge.lean` calculus body. One beast at a time
   ([[feedback-forcing-case]]).
2. **Adjacent but not constitutive.** This primitive sits next to the
   future human-facing / HITL / self-amendment layer, which is
   *explicitly out of scope* per the Axes 1–2 closure decision
   ([[project-cross-axis-keystone]]). Promoting it now would smuggle
   Axis 3 in under a different name.
3. **Generator-test discipline.** A primitive earns ratification by
   discriminating cases the existing vocabulary blurs
   ([[feedback-primitive-ratification-gate]]). The case this primitive
   discriminates (adoption vs. legitimation, with HITL receipts) is real
   but hasn't been forced by current paper work. Park, don't mint.

## Related records

- [[project-cross-axis-keystone]] — Axes 1–2 closure shape;
  Axis 3 explicitly OUT (this primitive lives in that explicitly-OUT
  neighborhood).
- [[project-leased-coercion]] — composite framing for leased / logged /
  split / sunset obligations; similar register-discipline shape, also
  parked.
- [[project-signal-authority]] — null-laundering / missing ACK ≠ NACK;
  same family of authority-routing primitives.
- [[project-laundering-move-watchlist]] — laundering-move inventory; this
  primitive guards against the *adoption-launders-origin* move.
- [[feedback-primitive-ratification-gate]] — generator + kind + seven
  supporting tests; gate for any future promotion.

## Theorem-shaped slogan (for later, if forced)

> **Adoption is not legitimation.**

Or more formally:

```
ReflectiveAdoption(subject, obligation)
  ⇒ LocallyBinding(subject, obligation)

ReflectiveAdoption(subject, obligation)
  ⇏ OriginAuthority(obligation.origin)

LocallyBinding(subject, obligation)
  ⇏ GeneralizableDuty(class(obligation))
```

That last non-arrow blocks the "you chose this once, therefore people like
you should carry this forever" move — the path by which vocation gets
turned into staffing model.

## Boundary rule, not total model

The formalism's role here is a **boundary rule**, not a total model of
human attachment.

> The formalism should protect the *later yes* from being stolen by the
> *earlier imposition*.

That is the whole move. Keep it narrow when (if) the time comes.
