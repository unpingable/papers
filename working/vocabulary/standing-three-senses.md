# "Standing" — three senses in the corpus

**Filed:** 2026-06-05. **Status:** vocabulary disambiguation note. **NOT a primitive.** **NOT doctrine.** Records a lexical fracture so the senses do not silently collapse.

## Why this note exists

The word "standing" appears across the corpus in at least three distinct relations. Single-altitude review at any one of them produces a coherent-looking answer to questions that span the three. Silent collapse produces fake primitives like "FreshStanding" with the false rule *expired evidence destroys standing*. The correct rule is more conditional and lives in three places.

This note does not introduce a new primitive. It records which sense lives where, so future cross-cutting work does not relitigate from confusion.

## The three senses

### 1. Standing-as-state-fact

**Where it lives:** `~/git/lean/LeanProofs/Admissibility/Derivation.lean`, specifically `StandingDerivation` with the `standingRevoked` field and the chained theorem `revoked_standing_never_authorized`.

**What it names:** A propositional predicate on a derivation. Standing is or is not revoked as a discrete state-evolution event. The time axis is ordinal (event sequence), not metric.

**What destroys it:** explicit revocation events. Not the passage of evidence-horizon time.

### 2. Standing-as-operational

**Where it lives:** [`../commitment-standing-decay-candidate.md`](../commitment-standing-decay-candidate.md) (candidate doctrine) and the checked, fenced formal slice at `~/git/lean/LeanProofs/Scratch/CommitmentStanding.lean`.

**What it names:** Set-membership of a declared commitment in the admissible-action set at time `t`: `standing(C, t) := C ∩ A(t) ≠ ∅`. Operational revocation = the intersection becomes empty while rhetoric still asserts `C`. Time axis is the viability / action-selection axis.

**What destroys it:** a state in which no admissible action satisfies `C`. A viability-set shift may produce that state, but monotone shrinking alone does not guarantee it eventually occurs; the Scratch countermodel makes this explicit. Not evidence-horizon expiry; not an explicit revocation event.

### 3. Standing-as-provable-now

**Where it lives:** `~/git/lean/LeanProofs/Admissibility/Freshness.lean`. Header keeper: *"Expired evidence cannot prove current standing."*

**What it names:** What time-bearing evidence licenses about standing-claims at metric time `now`. The predicate is `Fresh now issued expires skew maxDiv`. Time axis is metric (real-time clock with skew tolerance).

**What destroys it:** evidence horizon expiry, clock divergence, incoherent issued/expires interval. Not state-revocation events; not viability-set shifts.

## The key rule

When "expired freshness" is asserted to do something to "standing":

> Expired evidence prevents *this carrier* from discharging current standing.
> It does NOT by itself destroy standing-as-state-fact (sense 1).
> It does NOT by itself destroy standing-as-operational membership (sense 2).

The carrier becomes a non-licensing relation at `now`. A different carrier — fresh re-attestation, alternative witness, an independent custody channel — may still discharge the standing-claim. Sense 1 (state-fact) and sense 2 (operational) are governed by their own axes and require their own destroying events.

## Composition across the three senses

The three axes are governed at the doctrine layer by [`../admissibility-decay-family-note.md`](../admissibility-decay-family-note.md), which is **descriptive, not a primitive**. The family invariant — *"X licenses U under Γ₀; under Γ₁ no longer; system continues acting as if it does"* — instantiates at each axis with different `X`, different `U`, different `Γ`. The family note's deliberate refusal to mint a sixth higher-order primitive is the architecture, not a gap. See also [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) for the federation-level discipline that governs why these axes do not collapse.

## What this note is NOT

- **NOT a new primitive.** No new atom, no new kernel, no new family axis.
- **NOT doctrine.** A glossary cannot legislate; it can only disambiguate.
- **NOT a Lean module.** No Lean target, no theorem, no proof obligation.
- **NOT authorization** to mint `FreshStanding`, `StandingFreshness`, or any cross-axis collapse type.
- **NOT a renaming** of any existing primitive.

This is a vocabulary entry. If a future work needs to refer to "standing" across more than one axis, it should cite this note for which sense it means at each site.

## Provenance

Surfaced 2026-06-05 in [`../vector-mining/2026-06-05-attack-04-freshness-vs-standing.md`](../vector-mining/2026-06-05-attack-04-freshness-vs-standing.md) as Survivor 1 of attack-04 (vector-mining method, third pilot). The audit found that the relay-shape question *"does expired freshness destroy standing?"* presumes a single sense of "standing"; the corpus disambiguates the question across three senses with different answers. Filed as workflow hygiene — no doctrine change, no primitive added, no Lean module.

## Cross-references

- `~/git/lean/LeanProofs/Admissibility/Freshness.lean` — sense 3 (evidence-side, metric time).
- `~/git/lean/LeanProofs/Admissibility/Derivation.lean` — sense 1 (state-fact, ordinal time), via `StandingDerivation.standingRevoked`.
- [`../commitment-standing-decay-candidate.md`](../commitment-standing-decay-candidate.md) — sense 2 (operational, admissibility-set membership at `t`).
- [`../admissibility-decay-family-note.md`](../admissibility-decay-family-note.md) — descriptive family that runs through the three.
- [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) — federation discipline; why the senses must not collapse.
- [`../signal-authority-candidate.md`](../signal-authority-candidate.md) — adjacent: silence ≠ revocation; the protocol-level version of "absence of evidence is not destruction of standing."
- [`../vector-mining/2026-06-05-attack-04-freshness-vs-standing.md`](../vector-mining/2026-06-05-attack-04-freshness-vs-standing.md) — the pilot that surfaced the disambiguation.
