# Maximal calculus — discharge connection

**Status:** Candidate, agent-drafted 2026-06-02, not ratified.

Working-note sibling to
[`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md).
Records the cut between *true-but-inadmissible* (legitimate amendment,
admissible under the prior policy) and *retroactively-erased*
(laundering, blessed only by the policy the act installs). The
discharge essay candidate at
[`tooltheory/continuous-admissibility-and-discharge.md`](tooltheory/continuous-admissibility-and-discharge.md)
was already circling this cut; the maximal calculus formalizes what
the essay needs as a primitive.

## The cut, named

From the kernel specimen at
`~/git/lean/LeanProofs/Admissibility/AmendmentFragment.lean`
(scratch annex, Phase A of the autonomous run): a `Transition E S`
requires `evidence : E.Validates S.policy t.op` — the witness must
be valid under the *source* state's policy. The (A1) discipline
expressed at the type signature:

> No `Transition E S` exists for an operation `op` such that
> `¬ E.Validates S.policy op`, *regardless of whether*
> `E.Validates (E.applyOp S op).policy op` would hold under the
> post-state policy `op` itself installs.

The cut between admissible amendment and laundering is then:

- **Admissible amendment.** Evidence existed in `S` for the
  amendment-installing op. The post-state policy may differ;
  the amendment was *itself* admissible under the prior policy.
  Concretely: the discharge essay's bankruptcy reform is
  admissible because the bankruptcy procedure was ratified under
  non-bankruptcy law — the amendment installs the discharge
  primitive, and the installation is dischargeable in the
  pre-amendment regime.
- **Laundering (case #3).** No evidence in `S`; the post-state
  policy would validate the op *only because the op installs it*.
  The (A1) discipline refuses the transition. Concretely: a polity
  that abolishes its review procedure by an act for which only the
  abolished procedure could have offered standing.

The discharge essay's framing — *true but inadmissible* — is the
post-amendment shape of this cut for *individual obligations*. The
maximal calculus carries the *structural* shape for *policy
amendments themselves*.

## What the discharge essay needed as a primitive, the calculus
## now has as a theorem

Per the discharge essay candidate, the load-bearing keeper:

> A polity must know what it is forbidden to use.

The discharge essay needs this as a primitive — a *purpose-bound
routing prohibition* that the polity carries by stipulation. The
maximal-calculus reading of the same shape lives at the level of
*amendments to the routing prohibition itself*:

> An amendment to a discharge primitive is admissible iff its
> installation is admissible under the discharge primitive it
> replaces.

In the bankruptcy specimen: removing a bankruptcy discharge is
itself a policy amendment. Whether removal is admissible turns on
whether the *removal action* is itself admissible under the
pre-removal policy — *not* under the post-removal policy that would
sanction the removal because the removal will have rendered the
prior obligation enforceable.

The calculus does not say *what* the right discharge primitive is.
It says: *whichever* primitive a polity ratifies, that primitive's
amendment is itself gated by its predecessor.

## Receipt-gated decomposition: `(O₁ → wait → O₂)`

From amendment-cut.md §"Case B (delegation requiring future
acceptance)": the apparent shape *"X is admissible iff Y happens
later"* is ill-formed under (A1) when stated as a single operation,
but admits an honest decomposition into independent operations,
each of which is independently judged.

- **B1. Create pending delegation.** `Authorized_S(O_1)` holds:
  the *pending* delegation is authorized under the pre-state's
  superuser authority. The receipt-gated protocol pattern.
- **B2. Activate after receipt.** `Authorized_{S_t}(O_2)` holds
  in the later state `S_t` where the receipt exists. The
  authorization for `O_2` is in `S_t`, which post-dates `O_1`
  but pre-dates `O_2`.
- **B3 (refused).** Activate now on basis of an *anticipated*
  future receipt. `¬ Authorized_S(O)`. The future receipt has not
  yet been issued; the authority does not exist. This is
  future-witness laundering — an (A1) violation by a different
  route. The calculus refuses it for the same reason it refuses
  case #3: the witness is not in the pre-state.

The keeper line:

> A future receipt can authorize a later transition. It cannot
> authorize the transition that creates the need for the receipt.

In the discharge essay's language: the bankruptcy *court order* is
the receipt that authorizes the post-bankruptcy state in which
specific obligations are inadmissible. The court order's existence
is what authorizes the routing prohibition. The *anticipated future
court order* cannot authorize the obligor's pre-bankruptcy default
in a way that retroactively makes the default admissible — but the
court order itself, once issued, authorizes the post-discharge
state in which the default is admissible-yet-true-but-inadmissible.

## Open question: what is a valid wait?

The `(O₁ → wait → O₂)` pattern's middle term is unspecified. What
*counts* as a valid wait?

- A clock tick? Then any laundering can decompose into "wait one
  cycle, then act," collapsing the discipline.
- A specific receipt? Then the receipt's type matters: who issues
  it, under what authority, with what acceptance window?
- An observable event? Then the calculus must say what counts as
  an observation, and from whose vantage.

The discharge essay's bankruptcy specimen offers a real-world
answer: *court order with named jurisdiction*. The court order is
the receipt; the jurisdiction is what makes the order admissible
in the post-state.

But this is one specimen, not a general definition. The open
question for the maximal calculus is whether *valid wait* has a
unified shape across discharge, delegation, retroactive standing,
and other receipt-gated patterns. Filed as open. Do not attempt
to answer here; per the plan's stop conditions, that is operator
territory — and likely a paper-shaped question, not a Lean-shaped
one.

## What this note does NOT do

- Does not ratify the well-foundedness condition as *the*
  keystone of the maximal calculus. The kernel specimen at
  `LeanProofs/Admissibility/AmendmentFragment.lean` is a candidate
  test of the condition's reach; ratification awaits operator
  judgment.
- Does not redraft the discharge essay. The essay's promotion
  gates (1500–2500 word Substack scout; three worked cases beyond
  FICO) are unchanged by this note. What this note adds is the
  formal cousin the essay was already circling.
- Does not claim the maximal calculus is one paper or several.
  The forcing-case register's refusal stands: *one calculus or
  several is not decided here.*
- Does not propose new Lean modules. The kernel specimen's scope
  is the (A1) discipline at the transition signature, plus the
  case-#4 worked specimen, plus founding events. The discharge
  connection is a *substrate reading* of what the kernel already
  encodes, not a new module.

## Cross-references

- [[project-continuous-admissibility-discharge]] — discharge essay
  candidate at `working/tooltheory/continuous-admissibility-and-discharge.md`.
- [[project-reflective-adoption-parked]] — adjacent shape (later
  local adoption ≠ origin legitimation).
- [`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md) —
  the note this is sibling to.
- [`maximal-calculus-codex-review-log.md`](maximal-calculus-codex-review-log.md) —
  the Phase A milestone log; each milestone's codex pass and
  agent verdict.
