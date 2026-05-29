# Safety bridge — ρ-drop decision with ledger evidence (2026-05-28)

**Status:** Decision record at journal density. The decision itself is *in the Lean source* at `~/git/lean/LeanProofs/Admissibility/SafetyBridge.lean` (header decision block, plus the type signatures). This file captures *why* and what evidence supports it, so re-litigation in three weeks has somewhere to land before re-arguing from first principles.

---

## The call

`SafetyBridge.SafetyEnv.bridge : σ → α → Prop` is **actor-inert**. The actor parameter `ρ` lives in `Allowed : σ → ρ → α → Prop`, not in `bridge`. Actor-sensitive bridges are deferred to a named extension (`ActorSensitiveBridgeEnv` — declared in the Open block of `SafetyBridge.lean`, not implemented).

## Why

The deciding fact: `run : σ → α → σ` does not consume `ρ`. If the transition function cannot see the actor, then `ρ` in `bridge` cannot affect safety *semantics* — it can only filter *who is permitted to call a given transition safe*, which is authorization wearing a thrift-store mustache. The cleanest place for actor-relative permissions is `Allowed`; the cleanest shape for value-preservation evidence is over the transition effect.

The escape hatch is named: if a future model genuinely needs actor identity to change the transition effect, the right move is to lift the transition itself — `run : σ → ρ → α → σ` — not to smuggle actor-dependence through `bridge`. That's a different calculus slice, done under force.

## Evidence

The ρ-drop was first proposed when both `bridge` and the trajectory induction in the receipt model ignored `ρ`. The honest caveat at that point: the receipt model has `Actor := Unit`, so the inertness was partly degenerate — `Unit` parameters are always inert.

The attestation-ledger (`LeanProofs/Admissibility/AttestationLedger.lean`, filed same day) is the non-degenerate confirmation:

- Two genuinely asymmetric actors (`Party.writer`, `Party.auditor`) with non-overlapping permitted actions.
- `Allowed : Ledger → Party → Act → Prop` genuinely reads the actor (writer cannot revoke; auditor cannot post).
- `bridge : Ledger → Act → Prop` genuinely does not — pattern-matches only on the `Act` constructor.
- The full skeleton (single-step wound + boundary + trajectory triple + forgetful map + no-lift) builds green at this signature.
- The per-hop-actor trajectory refactor (actor as field in `LedgerAuthStep`, not parameter of `LedgerAuthTraj`) makes multi-actor paths expressible as single trajectories — `protocolHappyPath` is a writer-then-auditor trajectory built from the new shape.

This is the ≥2-actor model the original ρ-drop was decided without.

## Prediction for tier 2B (quorum)

The ρ-drop is expected to survive the certificate-authorization frontier, *provided* the certificate is modeled as action payload (`commit (x : Value) (cert : Cert)`, with `cert ∈ α`) rather than as an external κ parameter. Both `Allowed` and `bridge : σ → α → Prop` then read the certificate out of `α`. This is the same logic as the ρ-drop's own escape hatch: transition-or-safety-relevant authorization data goes into the action, not a smuggled index.

The honest hard part of quorum is unrelated to ρ: bridge stops being local-structural and `preserves` has to carry an inductive state invariant (quorum-intersection). That's where the brick-2 pattern stops sufficing — but it doesn't reopen the ρ question.

See `calculus-2-tier-map-2026-05-28.md` for the design pins on tier 2B.

## Where this decision would get reopened

- A bridge candidate that genuinely needs actor identity to *change the value-preservation argument* (not just to filter eligibility). Example would be: "actor X's posts get verified differently because X holds a special key" *and* "that verification difference shows up in whether the post preserves the defended-value invariant." If the actor's identity changes what the action *does*, lift the transition; if it only changes *who may call this safe*, that's authorization and belongs in `Allowed`.
- A model where the cert/witness cannot reasonably live in `α` and must be carried externally. Hard to construct cleanly; flag if encountered.

## What is *not* claimed

- Not claimed: actor-sensitive bridges are wrong in general. Claimed: they belong in a refinement (`ActorSensitiveBridgeEnv`) that wraps the base, not in the base.
- Not claimed: this decision is irreversible. Filed at candidate density so it can be revisited under force without the friction of canon revision.
