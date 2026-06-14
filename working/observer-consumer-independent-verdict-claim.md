# Claim sketch — consumer-independent verdict exists iff consumers agree

**Filed:** 2026-06-14. **Status:** paper-facing CLAIM SKETCH. **NOT** in
`CLAIM-REGISTER.md`. **NOT** promoted. This is the prose statement of the observer
center for eventual paper use; it does not change any register status.

## The claim

> In a system where verdicts about an artifact are produced *by consumers* (each relative
> to its own frame), a **consumer-independent verdict** — a single verdict per artifact
> that every consumer would agree with — exists **if and only if all consumers already
> agree** on every artifact.

Equivalently: there is no neutral, frame-free "what this artifact *is*" unless the frames
have already converged. Disagreement on even one artifact destroys the global section.

Corollary (the sharp, citable negative): **no absolute stamp.** A producer cannot mint a
verdict on the artifact that binds every consumer; enforceability/admissibility is derived
by the catcher, not stamped on the envelope. (This is the PCAA / receipt-stamping category
error stated as a theorem.)

## Lean anchor (scratch, not register)

`~/git/lean/LeanProofs/Scratch/ConsumerRelativeVerdict.lean`:
`has_global_section_iff_consumers_agree`, abstract codomain `Verdict`, `lake`-green,
**zero-axiom**, codex-clean. The Prop-codomain specimens
(`NoUniversalRoot.lean` etc.) are the `Verdict := Prop` instance.

## Why this is not a vacuum theorem — the empirical grounding

The claim is the shared invariant of seven independent shipping systems (NQ, nightshift,
wicket, continuity, standing, verifier, WLP): every one produces force/admissibility as
`Consumer → Artifact → Verdict`, none has a bare `Force(artifact)`, and WLP exhibits it
literally — the *same artifact* is `Accepted` by one consumer and `Unsupported` by another
on the consumer's own policy set. Excavation, not invention (see
[`excavation-vs-yagni.md`](excavation-vs-yagni.md) and the
[promotion preflight](observer-foundation-promotion-preflight.md)).

## OPEN — the public noun (decide at module-mint, not now)

The nucleus relation `Consumer → Artifact → Verdict` is currently called `Force` in
scratch. **`Force` is a loaded reading**, not the neutral foundation word — the
constellation says *consumer-relative verdict production*; "force" is one interpretation of
the verdict (enforceability), and the chosen noun determines what future lemmas
accidentally claim. Candidates if/when a public module is minted:

```
Force · Adjudicates · Evaluates · AssignsVerdict · Admits · Relies · Consequence
```

Do **not** freeze this by minting a public module yet. The scratch name `Force` is a
fossil label, not a ratified noun.

## Status / boundaries

- Paper-facing sketch only. Not register-promoted; not a public claim.
- No shared foundation module exists (deliberately — see the subgate in
  `wiring-is-not-folder-placement.md`).
- Promotion to `CLAIM-REGISTER.md` and the public-noun decision are both
  ratification-tier and deferred to the operator.
