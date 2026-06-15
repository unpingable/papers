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

## The public noun — provisional preference recorded (mint deferred)

The nucleus relation `Consumer → Artifact → Verdict` is called `Force` in scratch.
`Force` is a loaded reading (enforcement), not the neutral foundation word — the
constellation says *consumer-relative verdict production*.

**Operator decision 2026-06-14 (provisional, not minted):** the Lean-facing neutral noun
is **`VerdictFor : Consumer → Artifact → Verdict`** — names the output, codomain-aware
(works for `Allowed`/`Denied`/`Unknown`). Fallback: `AssignsVerdict`. **`Relies` is
rejected for the nucleus** (reserved for paper prose / reliance-specific application
lemmas) because the codomain includes negative/unknown verdicts — `Relies … = Denied`
reads as "relies on a denial." Do **not** mint a public module yet; the scratch `Force`
label stays a fossil. Full rationale in
[`observer-foundation-promotion-preflight.md`](observer-foundation-promotion-preflight.md)
§ Operator Decision.

Note for *this* sketch's prose: `Relies` remains fine **here** (paper-facing reliance
language) — the rejection is specifically about the *nucleus* identifier, not paper text.

## Status / boundaries

- Paper-facing sketch only. Not register-promoted; not a public claim.
- No shared foundation module exists (deliberately — see the subgate in
  `wiring-is-not-folder-placement.md`).
- Promotion to `CLAIM-REGISTER.md` and the public-noun decision are both
  ratification-tier and deferred to the operator.
