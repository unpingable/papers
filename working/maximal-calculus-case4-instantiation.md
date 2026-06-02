# Maximal calculus — case #4 instantiation test

**Status:** Candidate, agent-drafted 2026-06-02, not ratified.

Phase D of the autonomous run per
[`/home/jbeck/.claude/plans/cheeky-plotting-reef.md`](../../../.claude/plans/cheeky-plotting-reef.md):
test whether the candidate well-foundedness condition from
[`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md)
applies cleanly to register case #4 (standing mutation,
first-tractable).

## Result: **PASS**

The well-foundedness condition reaches case #4 cleanly via the
worked specimen `StandingSpecimen` in
`~/git/lean/LeanProofs/Admissibility/AmendmentFragment.lean`. The
positive theorem

```lean
def case4_pre_authorized_standing_mutation_admissible
    {S : State StandingPolicy} {A B : Nat}
    (hA : S.policy.hasStanding A) :
    Transition standingEnv S :=
  ⟨StandingOp.grant A B, hA⟩
```

inhabits `Transition standingEnv S` with `evidence := hA` — the
*pre-state* witness of actor `A`'s standing. No post-state
authority is consulted; the type signature already forbids it. The
construction type-checks; `lake build` is green; the codex
adversarial pass (A.5 in the review log) raised only honesty-gap
findings on the prose (now integrated), not on the underlying
admissibility claim.

## Setup, recapped

A `StandingPolicy` is a predicate over actor IDs (`Nat`) naming who
has standing. The operation `StandingOp.grant granter grantee`
records a grant of standing from `granter` to `grantee`. The
specimen `Validates` says: a grant is valid under a policy iff the
*granter* has standing in that policy. The specimen `applyOp`
installs the grantee in the standing predicate (extensionally
disjunctively — the post-state policy admits `grantee` and
everyone the pre-state policy admitted).

Case #4 instance: actor `A` has standing in `S` and grants standing
to actor `B`. Pre-state has `S.policy.hasStanding A`. Post-state
has `(applyOp).policy.hasStanding A ∨ a = B`. The transition's
authorization witness is `S.policy.hasStanding A` — valid under the
*pre-state* policy. The discipline of (A1) holds.

The case-#3 negative on the same specimen — actor `B` (without
standing) attempts to grant themselves standing — is refused by the
kernel-level `no_transition_without_pre_authorization` applied at
`standingEnv`. The specimen also exhibits the full case-#3 shape
(both pre-state failure *and* post-state would-validate) via
`case3_self_grant_full_shape_inadmissible` + the supporting
`case3_post_state_would_validate` lemma proven by `Or.inr rfl`.

## What this PASS means and does not mean

**Means:**

1. The candidate well-foundedness condition from
   amendment-cut.md is not only an abstract statement; it
   constructively admits a worked instance covering the
   register's first-tractable case.
2. The case-#3 / case-#4 discriminator from amendment-cut.md
   §"The invariant" — *"#4 changes who may act next; #3 tries to
   become the reason it was allowed to act now"* — is operational
   at the kernel level. Both shapes are visible in the same
   specimen; the kernel separates them by source-policy witness.
3. The structural parallel to the Fixed-Value Fragment's `AuthStep
   E s` discipline holds. The lift to mutable policy works.

**Does not mean:**

1. Case #4 reduces *in general* to this specimen. The
   `StandingSpecimen` is a *minimal* instance with `Policy := Nat
   → Prop`, `Op := grant granter grantee`. Real institutional
   standing mutations carry more structure: precedence,
   enfranchisement procedures, jurisdiction, revocation. The
   specimen establishes existence of one clean instance, not
   coverage of all instances.
2. The well-foundedness condition is *the* keystone of the maximal
   calculus. Per amendment-cut.md, the condition is a candidate;
   case-#4 reach is one piece of evidence, not the full
   ratification. Operator judgment owns the keystone question.
3. The remaining register cases (#1 value-function amendment, #2
   retroactive legitimation, #5 crisis substitution, #6 reflective
   adoption) are covered by this specimen. They are not — and the
   plan's stop conditions explicitly forbid promoting them here.

## What was tested vs what was claimed

| | Tested | Claimed in note |
|---|---|---|
| Pre-state witness inhabits `Transition` | ✓ Lean theorem | Yes |
| Post-state-only authorization is refused | ✓ Lean theorem | Yes |
| Specimen exercises policy mutation (not fixed-value) | ✓ Codex A.5 finding 1 affirmed | Yes |
| Specimen generalizes to all case-#4 instances | ✗ | No (explicit) |
| Well-foundedness condition is keystone | ✗ | No (explicit) |
| Case #5 (crisis substitution) admits same shape | ✗ | No |
| Case #1 (value amendment) admits same shape | ✗ | No |

Per `feedback-narrow-construction-on-failure`: more constraints,
fewer assumptions. The PASS is for one specimen; the operator owns
whether that's enough evidence to ratify the condition's reach.

## Cross-references

- Kernel specimen: `~/git/lean/LeanProofs/Admissibility/AmendmentFragment.lean`
  §"Case #4 worked specimen: standing mutation."
- Codex log: [`maximal-calculus-codex-review-log.md`](maximal-calculus-codex-review-log.md),
  Milestone A.5 entry.
- Register: [`maximal-calculus-forcing-cases.md`](maximal-calculus-forcing-cases.md),
  §"Case #4 — Standing mutation."
- Amendment cut: [`maximal-calculus-amendment-cut.md`](maximal-calculus-amendment-cut.md),
  §"The invariant," §"Worked examples."
- Sibling notes: [`maximal-calculus-discharge-connection.md`](maximal-calculus-discharge-connection.md),
  [`maximal-calculus-founding-events.md`](maximal-calculus-founding-events.md).
