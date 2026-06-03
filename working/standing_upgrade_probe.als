/*
  standing_upgrade_probe.als

  Single bounded probe per `alloy-spike-standing-upgrade-plan.md`.

  Target artifact: standing-upgrade-block worked example
  (~/git/lean/docs/worked-examples/standing-upgrade-block.md) and the
  Authority verdict kernel (~/git/lean/LeanProofs/Admissibility/Authority.lean).

  ChatGPT-sharpened question:
    Can an actor acquire the standing needed to authorize an operation
    by means of the same operation whose authorization depends on that standing?

  Expected shape (the analog of the RetroactiveLegitimation cut):
    Allowed: prior standing -> authorized operation -> new standing
    Blocked: operation -> new standing -> retroactively authorizes operation

  Disposable file. No calculus naming. No generalization across specimens.
*/

// -----------------------------------------------------------------------------
// Signatures: the smallest relational vocabulary that lets us encode
// the kernel's three-input gate plus a pre/post state transition for ops.
// -----------------------------------------------------------------------------

sig Actor {}

sig Claim {
  author: one Actor
}

sig State {
  hasStanding:           set Actor,
  hasAdmissibleBasis:    set Claim,
  hasResolvedPrecedence: set Claim
}

sig Op {
  by:    one Actor,
  using: one Claim,
  pre:   one State,
  post:  one State
}

// -----------------------------------------------------------------------------
// Kernel rule.
// Mirrors Admissibility.Authority.authorityVerdict + authorized_iff_all_green:
// authorized iff admissibleBasis AND resolved precedence AND standing,
// all checked at the pre-state.
// -----------------------------------------------------------------------------

pred kernelAuthorized[o: Op] {
  o.by    in o.pre.hasStanding
  o.using in o.pre.hasAdmissibleBasis
  o.using in o.pre.hasResolvedPrecedence
}

// -----------------------------------------------------------------------------
// Behavioral predicates over single operations.
// -----------------------------------------------------------------------------

pred selfCert[o: Op] {
  o.using.author = o.by
}

pred selfStandingUpgrade[o: Op] {
  o.by not in o.pre.hasStanding
  o.by     in o.post.hasStanding
}

pred priorStanding[o: Op] {
  o.by in o.pre.hasStanding
}

// -----------------------------------------------------------------------------
// Probe 1 — direct retroactive standing upgrade.
// Tries to construct: one op, kernel-authorized at pre, that self-upgrades
// (lacks standing at pre, has it at post).
//
// By the kernel rule, this should be unsatisfiable: kernelAuthorized requires
// standing at pre; selfStandingUpgrade requires no standing at pre. The point
// is not to "prove" this — it's an encoding sanity check. If alloy DOES find
// an instance, the encoding has a hole.
// -----------------------------------------------------------------------------

run probe1_direct {
  some o: Op |
    kernelAuthorized[o]
    and selfStandingUpgrade[o]
} for 2

// -----------------------------------------------------------------------------
// Probe 2 — allowed shape: prior standing -> authorized op -> new standing.
// Tries to construct: actor a HAS standing at pre, the op is kernel-authorized,
// and standing is preserved or extended at post.
//
// Should be satisfiable. Alloy producing an instance = the "allowed" half of
// ChatGPT's expected shape is constructible.
// -----------------------------------------------------------------------------

run probe2_allowed_shape {
  some o: Op |
    kernelAuthorized[o]
    and priorStanding[o]
    and o.by in o.post.hasStanding
} for 2

// -----------------------------------------------------------------------------
// Probe 3 — compositional bootstrap (the real test).
// Two ops o1, o2 by the same actor a, using a-authored claims (self-cert).
// o1.post = o2.pre, so o2 sees the state produced by o1.
// a lacks standing at o1.pre and has standing at o2.post.
// Both ops kernel-authorized.
//
// If alloy finds an instance, then WITHOUT additional constraints on how
// standing is granted, the kernel's algebraic gate alone permits a chain
// where a bootstraps her own standing across self-cert operations.
//
// This is the "is the kernel layer alone load-bearing, or does the bootstrap
// blocking live upstream in the derivation/standing-grant rules?" question.
// -----------------------------------------------------------------------------

run probe3_chain_bootstrap_unconstrained {
  some a: Actor, c1, c2: Claim, o1, o2: Op |
    o1 != o2
    and o1.by    = a   and o2.by    = a
    and c1.author = a  and c2.author = a
    and o1.using = c1  and o2.using = c2
    and o1.post  = o2.pre
    and a not in o1.pre.hasStanding
    and a     in o2.post.hasStanding
    and kernelAuthorized[o1]
    and kernelAuthorized[o2]
} for 4

// -----------------------------------------------------------------------------
// Probe 4 — same as probe 3, but adding a candidate "standing must be granted
// by someone other than the gainer" constraint. This represents the kernel's
// architectural claim that admissible basis must come from outside the actor.
//
// If alloy STILL finds a bootstrap instance with this constraint, the
// constraint is too weak. If alloy finds NONE, the constraint blocks the
// bootstrap. Encoding the constraint cleanly is itself part of the probe:
// if it requires multiple distinct concept slots (temporal priorness, source
// independence, etc.) that's outcome (4) from the spike plan.
// -----------------------------------------------------------------------------

fact independentStandingGrant {
  // For any state s and actor a, if a has standing at s, then either:
  //   (i) some op terminates at s, performed by a DIFFERENT actor, OR
  //   (ii) a had standing at some predecessor state already (carried forward
  //        through an op that did not strip it).
  //
  // The "or carried forward" branch admits base-state standing without a
  // grant op, but requires the standing to have entered the system at some
  // independently-granted state.
  all s: State, a: Actor |
    a in s.hasStanding implies
      (some o: Op | o.post = s and o.by != a and a in o.post.hasStanding)
      or (some prior: State, o: Op |
            o.pre = prior and o.post = s and a in prior.hasStanding)
}

run probe4_chain_bootstrap_with_independence {
  some a: Actor, c1, c2: Claim, o1, o2: Op |
    o1 != o2
    and o1.by    = a   and o2.by    = a
    and c1.author = a  and c2.author = a
    and o1.using = c1  and o2.using = c2
    and o1.post  = o2.pre
    and a not in o1.pre.hasStanding
    and a     in o2.post.hasStanding
    and kernelAuthorized[o1]
    and kernelAuthorized[o2]
} for 5

// -----------------------------------------------------------------------------
// Probe 5 — does the independence fact also block legitimate paths?
// Allowed shape with the constraint: actor a has standing at pre because
// some other actor's op set it up.
//
// Should be satisfiable. If not, the independence fact is too strong and
// breaks legitimate standing-grant chains.
// -----------------------------------------------------------------------------

run probe5_independence_allows_legitimate_grant {
  some a, granter: Actor, o_grant, o_use: Op |
    a != granter
    and o_grant != o_use
    and o_grant.by   = granter
    and o_use.by     = a
    and o_grant.post = o_use.pre
    and a in o_use.pre.hasStanding
    and kernelAuthorized[o_use]
} for 4
