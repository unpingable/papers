# Attack #04 — Freshness × Standing

**Filed:** 2026-06-05. **Status:** vector-mining pilot output. **Vector ID:** attack-04. **Confidence:** high (ALIAS-RISK dominant; DUPLICATE on the underlying question).

## Question (narrow)

> Does expired freshness destroy standing, or only prevent standing from discharging a particular effect at action time?

## Sources audited

- `LeanProofs/Admissibility/Freshness.lean` (PUBLIC-SHIPPED): metric-time freshness kernel; canonical consumer is `~/git/standing` (workload-identity / grant authorization tool). Five negative theorems. **Header keeper line is load-bearing for this audit.**
- `LeanProofs/Admissibility/Derivation.lean` (referenced via `[[project-no-unifier-without-laundering]]`): houses `StandingDerivation` with `standingRevoked` field and chained theorem `revoked_standing_never_authorized` (Derivation.lean:97-203 per the federation note).
- `[[project-commitment-standing-decay]]` memory + `working/signal-authority-candidate.md`: candidate primitives about standing-as-operational-fact vs standing-as-rhetoric.
- `[[project-signal-authority]]` memory: silence ≠ revocation; missing ACK ≠ NACK; the protocol-level frame.
- `[[project-admissibility-decay-family]]` memory: **the explicit family designation covering five "license persists after admissibility failure" primitives**.

Memory entries flagged as 25 days old; verified against current Lean tree (no `SignalAuthority.lean`, no `CommitmentStanding.lean` — consistent with the "reserved, not built" status the memories declared).

## The relay's question rests on a vocabulary collision

The word "standing" does at least **three distinct jobs** in the corpus, each pointing at a different relation. Single-altitude review at any one of them would have answered the relay's question; the answer disagrees at each altitude unless the senses are disambiguated.

| Sense | Where it lives | Relation it names |
|---|---|---|
| **Standing-as-state-fact** | `StandingDerivation.standingRevoked` (Derivation.lean) | A propositional predicate on a derivation: revoked or not. State-evolution discipline (ordinal time). |
| **Standing-as-operational** | [[project-commitment-standing-decay]]: `C ∩ A(t) ≠ ∅` | Set-membership of the commitment in the admissible-action set at time t. Operational revocation = the intersection becomes empty while rhetoric persists. |
| **Standing-as-provable-now** | Freshness.lean header keeper: *"Expired evidence cannot prove current standing."* | What time-bearing evidence licenses about standing-claims at metric time `now`. Metric-time discipline. |

Three relational vocabularies for one word. **This is the [[project-no-unifier-without-laundering]] § The relational-vocabulary fracture pattern, instantiated at the `standing` token.** Same fracture shape as the project-level five-vocabulary fracture; this is its lexical micro-cousin.

## Direct answer in the corpus (the relay's question, already answered)

Freshness.lean's header keeper:

> *Expired evidence cannot prove current standing.*

That single sentence is the answer the relay was asking for. Disambiguated against the three senses above:

- **Expired freshness does NOT destroy standing-as-state-fact.** That's `standingRevoked`'s job, and revocation is a state-evolution event, not a horizon expiry.
- **Expired freshness does NOT destroy standing-as-operational.** That's the admissibility-set-membership question handled by [[project-commitment-standing-decay]]'s `C ∩ A(t)` formalism.
- **Expired freshness DOES destroy *this evidence's* ability to license standing-as-provable-now.** `expired_not_fresh : ¬ (now ≤ expires + skew) → ¬ Fresh ...` exactly.

So the answer to the narrow question:

> **Expired freshness does not destroy standing; it destroys this evidence's discharge of standing-claims at metric time `now`.** A standing-fact may still hold; a standing-claim may still be true; this carrier is no longer the licensing relation for `now`.

That is precisely the polarity distinction the relay was reaching for. The corpus already carries it.

## Multi-altitude DUPLICATE table

| Relay-shaped concern | Corpus location | Verdict |
|---|---|---|
| "Expired freshness ⇒ no standing" (collapse) | Freshness.lean header keeper distinguishes evidence-side from fact-side cleanly | DUPLICATE on shape; corpus is more precise |
| "Standing as state predicate" | `StandingDerivation.standingRevoked` + `revoked_standing_never_authorized` (Derivation.lean) | DUPLICATE; Lean substrate already has this layer |
| "Standing decays over time even though declared" | [[project-commitment-standing-decay]] + four-branch typology (emergent / managed / successor / transparent) | DUPLICATE at doctrine altitude; candidate primitive, name reserved |
| "Absence of fresh evidence ≠ revocation" | [[project-signal-authority]]: silence ≠ revocation unless protocol says so | DUPLICATE; candidate primitive, name reserved |
| Cross-cutting frame for all of the above | [[project-admissibility-decay-family]]: five primitives + family-invariant + structural-vs-conditional sub-axis | DUPLICATE; the corpus has the explicit family-level cross-reference |

The family designation is *descriptive-not-primitive*. It refuses promotion to a higher-order construct precisely because each axis stands independently and the unifier would be laundering. **That refusal IS the corpus's answer to "should this be one primitive?"** Exactly what attack-05's federation-doctrine gate found, applied to the standing axis.

## Federation-doctrine gate

Same gate, third firing. The relay's claim — if it had proposed minting a single `FreshStanding` primitive or `StandingFreshness` lattice — would have:

- Collapsed three relational vocabularies for "standing" into one type.
- Erased the structural-vs-conditional sub-axis the admissibility-decay-family memory explicitly names.
- Created a new atom that the existing five-primitive admissibility-decay family ratification gate would have to be re-litigated against.

Outcome 2 (laundering) or Outcome 3 (unlicensed bridge structure) from [[project-no-unifier-without-laundering]] § Modal/dependent false rescue. Gate fires; reclassification BRIDGE-CANDIDATE → LAUNDERING.

But: **the relay did not actually propose minting a new primitive on this axis.** The relay's broader work (effect-indexed admissibility) doesn't have a dedicated standing-freshness object; the question was framed in attack-04 because the conceptual collision lives in the relay's `Fresh` + `Discharges` interaction. So the gate fires preventively, not against a relay-shipped target.

## Verdict

- **ALIAS-RISK (dominant).** The word "standing" carries three distinct relations across the corpus. This is the lexical micro-instance of the project-level relational-vocabulary fracture pattern.
- **DUPLICATE.** Each of the three relations is already operationalized: Freshness.lean (evidence-side metric time), StandingDerivation (state-fact ordinal time), commitment-standing-decay (operational admissibility-set). The relay's question is answered by Freshness.lean's header keeper.
- **NOT MISSING-PRECONDITION.** The composition across the three "standing" senses is explicitly governed by [[project-admissibility-decay-family]] as a descriptive family — and the family's deliberate *refusal* to become a primitive is part of the architecture.
- **NOT BRIDGE-CANDIDATE.** Any bridge connecting the three senses would owe the 5-element bridge tax per [[project-no-unifier-without-laundering]]. None is on offer; none has a forcing case.
- **Gate fires preventively** against the implied "let's name this collision with a new primitive" move that did not actually arrive but would have.

## Survivors

**Survivor 1: vocabulary disambiguation worth filing.** The three senses of "standing" in the corpus are not currently disambiguated in any single place. The closest is the admissibility-decay-family memory's table-of-axes, which orients by *primitive*, not by *word*. A small disambiguation note — `working/vocabulary/standing-three-senses.md` or as an entry in an existing glossary if one exists — would close the gap. **Mechanical, low-blast-radius, no new primitive.** Roughly:

> *"Standing" in the corpus carries three distinct relations: standing-as-state-fact (StandingDerivation, ordinal time), standing-as-operational (commitment-standing-decay, admissibility-set membership at time t), standing-as-provable-now (Freshness, metric-time evidence horizon). Expired freshness destroys the third, not the first two. Standing-fact and standing-operational may persist after evidence freshness expires; standing-claim discharge does not.*

Not authorized to file without user signal. Candidate for one of the [[documentation-keepers]] entries OR a glossary section that doesn't yet exist.

**Survivor 2: cross-reference micro-patch (same pattern as attack-02).** Freshness.lean's docstring lists sibling modules but does not cross-reference [[project-admissibility-decay-family]] or [[project-commitment-standing-decay]]. The decay-family memory lists five primitives but does not cross-reference Freshness.lean as the *evidence-side instance* of the family invariant. Mechanical bidirectional patch worth ~5 min; same shape as the loop-capture × witness-carrier-model patch from attack-02.

The patch should land where the existing cross-references live, in the same register, without elevating Freshness to family-primitive status (it's a specific kernel; the family is descriptive).

**No Survivor 3.** No new theorem, no new atom, no new module. The composition is governed by the federation doctrine; the disambiguation is lexical.

## Recommended next action

- **Do not** mint `FreshStanding` / `StandingFreshness` / any new atom on this axis.
- **Do not** promote admissibility-decay-family to a primitive. The memory entry's ratification gate has not cleared (and the corpus's federation discipline says it should not clear via laundering).
- **Do** consider filing the vocabulary disambiguation (Survivor 1) — small, mechanical, addresses a genuine readability gap.
- **Do** consider the cross-reference patch (Survivor 2) — same shape as attack-02's patch; ~5 min.

## Method validation (cumulative, 3 pilots)

| Attack | Verdict | Pattern | Survivors |
|---|---|---|---|
| #5 effect vs obligation | DUPLICATE + ALIAS-RISK + LAUNDERING | single-altitude (relay claim re-skinned bridge-obligation-set) | 2 prose-altitude |
| #2 boundary × feedback | DUPLICATE at three altitudes + LAUNDERING | multi-altitude (relay bundled three atoms into one) | cross-ref patch + future-Lean vocab |
| #4 freshness × standing | ALIAS-RISK dominant + DUPLICATE | lexical fracture (one word, three relations) + descriptive family | disambiguation note + cross-ref patch |

The method has now demonstrated three distinct failure-modes of relay-shape attacks:

1. **Vocabulary re-skin** (attack-05): same lattice, different abstract type.
2. **Multi-altitude bundle** (attack-02): single proposed primitive absorbs N existing atoms.
3. **Lexical fracture** (attack-04): single word carries N distinct relations; relay's question presumes one.

Each failure mode has the same disposition under the federation doctrine: refuse the unification, name the fracture, leave the cross-cutting frame descriptive.

**Methodological keeper** (workflow hygiene, not new doctrine):

> *Relay claims must be audited across Lean substrate, substrate-discipline doctrine, paper-candidate synthesis, watchlist, AND lexical-collision altitudes before being treated as novel. Single-altitude novelty is inadmissible for promotion.*

This is now the operating procedure for vector-mining pilots. Not a paper, not a doctrine update — just the workflow rule the method enforces.

## Cross-references

- `LeanProofs/Admissibility/Freshness.lean` — the evidence-side metric-time kernel whose header keeper is the load-bearing answer.
- `LeanProofs/Admissibility/Derivation.lean` (StandingDerivation) — the state-fact ordinal-time kernel.
- [[project-commitment-standing-decay]] — the operational-standing candidate primitive.
- [[project-signal-authority]] — silence ≠ revocation candidate primitive.
- [[project-admissibility-decay-family]] — the descriptive family that governs the cross-cutting frame.
- [[project-no-unifier-without-laundering]] — the federation doctrine the implicit relay laundering would violate.
- `working/vector-mining/2026-06-05-attack-05-effect-vs-obligation.md` — first pilot.
- `working/vector-mining/2026-06-05-attack-02-boundary-feedback.md` — second pilot.

## Provenance

Pilot run 2026-06-05 of the corpus-archaeology vector-mining method. Attack #4 selected over attack #1 (Mandamus × refusal-as-effect) per user's framing that the polarity-trap potential made #4 more methodologically interesting. Result: ALIAS-RISK dominant — first pilot where ALIAS-RISK is the load-bearing classification rather than DUPLICATE. Method now demonstrates three distinct failure-modes of relay-shape attacks. Workflow-hygiene rule extracted from cumulative pattern.
