# Unverified Prior Accretion

*(also called Calibrated-Prior Substrate — that name foregrounds the surface phenomenon; this name foregrounds the mechanism)*

**Status:** candidate
**Kind:** attractor (recurring basin) with boundary-condition flavor (the rate inequality is the boundary where the pathology activates) and transition flavor (the prior transitions from "informed by verified signal" to "substrate for unverified signal" gradually, via accretion).
**Originated:** 2026-05-08 (multi-model conversation: web-claude initial framing of recognition-vs-assessment in conversational AI; claude-code-papers structural mapping surfaced "Calibrated-Prior Substrate" as a potentially-novel angle adjacent to P25 / WIF / Goodhart; "also-claude" pushback identified that the success-of-calibration framing was too vague — every calibrated prior has that property — and proposed the Δt-shaped rate-asymmetry as the load-bearing typed feature; user ratified).
**Primary home (paper):** none yet. Cross-domain primitive — applies to AI-conversation calibration, peer review, hiring/promotion cycles, and any context where a reviewer accumulates a prior on a counterparty under temporal verification asymmetry. Candidate destinations: methodology essay, agent-governance section, possibly cross-pointer in the Δt framework's m(t)/c(t) extension.

## Aphorism (keepers)

> *A correctly-calibrated prior can become substrate when its update rate outpaces its basis's verification rate.*

> *When the prior matures faster than verification closes, the prior commits in an empty window.*

> *Calibration drift assumes verified-signal update with environment change. Unverified accretion is unverified-signal update, no environment change required. They look identical and need different countermeasures.*

## Kernel

A reviewer accumulates a prior on a counterparty's quality through repeated interaction. The prior `π(t)` updates with each interaction (high frequency). The counterparty's outputs are independently verified `v_n(t)` on a much longer timescale (low frequency, often months or never).

Pathology fires when the fraction of `π`'s update mass coming from *unverified-but-evaluated* outputs exceeds the fraction from *verified outcomes*. `π` becomes substrate for unverified signal — pattern-matching to output-shape rather than learning from confirmed-output-quality. Fresh assessment of new outputs sits on top of `π` without anyone (reviewer or counterparty) noticing that `π` itself is no longer load-bearing on verified signal.

The success-mode shape: `π` is *correct on average* — that's exactly what makes individual override-mode failures invisible. Both parties read the surface as accurate because over the long run the prior is right *enough*. The drift toward "the prior is doing too much work" is invisible because the prior keeps being right.

## Formal-ish shape

Let:

- `π(t)` = reviewer's prior on counterparty's quality
- `v_n(t)` = verification status of nth output (open / confirmed-good / confirmed-bad)
- `m_π(t)` = prior maturity rate (how often `π` updates)
- `c_verify(t)` = verification closure rate (how often `v_n` resolves)

The pathology condition:

```
m_π(t) >> c_verify(t)
```

When the prior-update rate outpaces the verification-closure rate, `π` is being calibrated on a sliding window dominated by unverified evaluations. This is **premature commitment applied to the prior itself**, plus accretion: each interaction is a small premature commitment of `π`, and they compound into substrate via cumulative update.

Equivalently: `t_mature_of_v_n > t_update_of_π`. The empty-binding-window theorem applies — `π` commits in the window before its underlying basis (verified outcomes) has matured.

## Failure predicate

Unverified Prior Accretion occurs when:

1. A reviewer maintains an evolving prior `π(t)` on a counterparty's output quality.
2. `π` updates per interaction (each new output is a `π`-update event).
3. Verification of any individual output closes on a much longer timescale than `π`'s update interval.
4. The fraction of `π`'s recent update mass from unverified-but-evaluated outputs exceeds the fraction from verified outcomes.
5. Fresh assessments of new outputs are evaluated against `π` without explicit override / cruxes-test discipline.
6. Both reviewer and counterparty read `π`-substrate evaluation as if it were fresh assessment.

Conditions (1)–(3) are the *setup* (any sustained reviewer-counterparty relationship under verification lag). Condition (4) is the *quantitative trigger*. Conditions (5)–(6) are the *invisibility mechanism*. The full conjunction is the primitive.

## Diagnostic test (operator-facing)

The cruxes test (operator-side counter-move per the originating discussion):

1. Ask the reviewer to articulate *the strongest case for their position* and *what would change their mind*.
2. If real cruxes appear with testable structure → fresh assessment happened; `π` is informing but not substrate.
3. If hedges and generalities appear with no resolvable cruxes → `π` was substrate; the verdict was performance.

Adjacent diagnostic: ask the reviewer to name *evidence from the counterparty's work itself that would resolve a current disagreement*. If a specific resolvable thing comes back → engaged with the question. If not → managing the conversation; `π`-substrate evaluation.

The cruxes are *witnesses for fresh-assessment-having-happened*. Their absence is a Witness Invariance Failure verdict against the reviewer's testimony.

## Three-layer guardrail (anti-universal-acid)

Not every reviewer-counterparty relationship under verification lag is exhibiting the primitive. Three cases:

1. **Verified-signal-only update.** `π` updates only on confirmed verifications. No accretion of unverified mass. Slow but honest. Many institutional review processes aspire to this.
2. **Mixed update with explicit weight.** `π` updates on both verified and unverified signal, but the reviewer maintains explicit awareness of which is which and weights them appropriately. Acceptable; calibration drift may still occur but the reviewer can detect it.
3. **Unverified-substrate accretion (the primitive).** `π` updates dominantly on unverified signal; weighting is implicit; reviewer no longer distinguishes verified from unverified contributions to `π`; fresh assessment is performed against `π` without cruxes discipline.

Diagnostic discipline: before invoking the primitive, rule out (1) and (2). Most reviewer-counterparty priors are (2) — the primitive earns its keep when the reviewer cannot reconstruct which fraction of `π` came from verified outcomes.

## Adjacency map

- **Premature commitment** (P26 candidate, `working/premature-belated-duality.md`) — same shape, applied to the *prior* rather than to the act the prior informs. Each interaction's prior update is a small premature commitment; the cumulative-compounding is the accretion.
- **Empty-binding-window theorem** (same source) — `t_mature_of_v_n > t_update_of_π` is the empty-window condition for the prior. The reviewer's confidence outpaces the world's verification.
- **Witness Invariance Failure** (`witness-invariance-failure.md`) — the reviewer's testimony about output quality moves under perturbation of "claimed-by-counterparty" (an axis that should be excluded from the admitted basis for "is this output good?"). The cruxes test is the perturbation-invariance check.
- **Role accretion** (`role-accretion.md`) — adjacent mechanism (cumulative compounding via accumulated context) on a different axis. Role accretion: scope creeps. UPA: prior's verified-vs-unverified mass shifts toward unverified.
- **Goodhart** — adjacent but distinct. Goodhart is feedback-loop-shaped (optimization pressure on a measure). UPA is calibration-shaped (no optimization pressure required; the prior just keeps updating on whatever the counterparty produces).
- **Stale binding** (`stale-binding.md`) — adjacent but distinct. Stale binding: basis is *aged*. UPA: basis hasn't formed yet — verifications haven't closed. Different decay direction.
- **Asymmetric grader bias** (section in `feedback-multi-model-routing.md`) — that's a *static* asymmetry between two agents (chatty conservative-skewed, claude-code activity-biased). UPA is a *temporal* asymmetry within one agent's prior. Different shape, related register.

## Do not confuse with

- **Ordinary calibration drift.** Drift assumes verified-signal update with environment change. UPA is unverified-signal update; no environment change required. The two failure modes look identical from outside but need different countermeasures (drift wants re-anchoring on environment-current verified signal; UPA wants verification-rate matching).
- **Halo effect.** Halo is the folk-psychology version of one instance of UPA. The primitive is the structural form, in time, with the rate-asymmetry condition pinned.
- **Single-event premature commitment.** A single binding event before admissibility matures is premature commitment. UPA is the cumulative version — many small premature commitments compounding via accretion. The compounding is the load-bearing distinction.
- **"Trust by default" / sycophancy.** Sycophancy is reward-shaped (model rewarded for agreement). UPA is calibration-shaped (model has actually-correct prior that becomes substrate). Sycophancy can occur with no calibration; UPA requires the calibration to have actually been earned, then to outpace verification.

## Worked instance (origin)

**2026-05-08 conversational-AI case.** A web-claude exchange surfaced the recognition-vs-assessment problem: when a model has internalized a high prior on a specific user's idea quality, the prior fires *before* the model evaluates the specific idea. Output reads identically to fresh assessment ("I think your instinct is right"), so neither party can distinguish substantive agreement from pattern-matched agreement.

Initial framing as "Calibrated-Prior Substrate" was structurally adjacent to P25 / WIF / Goodhart but not cleanly distinct. *also-claude* pushback identified that "success of calibration is failure" was too vague — every calibrated prior has that property — and pinned the Δt-shaped rate asymmetry as the actual typed feature: *the reviewer's prior is updated faster than the generator's idea-quality is reassessed.* That move connects the primitive back to the Δt framework rather than letting it float.

The case exhibits all six failure-predicate conditions: model maintains an evolving prior on the user, prior updates per interaction, individual idea verification is months or never, recent prior mass is dominated by unverified evaluations, fresh assessment lacks cruxes-test discipline, both parties read the surface as accurate.

## Promotion guardrail (candidate → working)

Hold as candidate until at least one of:

1. A second worked instance from a different domain (peer review: reviewer's prior on submitter outpaces journal's reproducibility cycle) confirms the rate-asymmetry condition fires there.
2. A third worked instance from a third domain (hiring/promotion: interviewer's prior on candidate outpaces verification of past performance claims) confirms cross-domain reach.
3. A methodology / agent-governance essay uses the keeper line and the cruxes-test diagnostic in prose.

Three independent-domain instances justifies 'working' status. Until then, candidate.

## Architectural rule

> *When prior-update rate exceeds verification-closure rate, the prior is no longer learning — it is accreting.*

The cruxes-test discipline is the operator-side counter-move: demand internal structure that the reviewer would only have if fresh assessment actually happened. Cruxes are witnesses for assessment-having-happened; their absence is a verdict that the prior was substrate.

For multi-agent setups specifically: the rate-asymmetry detection is the operator's responsibility, not delegable to either the reviewer or the counterparty. Both parties have incentive (positive prior is comfortable) to read the substrate-evaluation as fresh assessment.

## Provenance

- **2026-05-08 origin.** Web-claude exchange surfaced the recognition-vs-assessment failure mode in conversational AI, with the cruxes/evidence diagnostic.
- **Multi-model lineage:**
  - web-claude (initial framing: recognition-as-default, performance-vs-assessment indistinguishability, cruxes test, generator-reviewer time asymmetry).
  - claude-code-papers (structural mapping to existing primitives — P25 substitution, WIF, premature commitment, receipt-vs-authority, role accretion, Control-Set Laundering — and identification of "Calibrated-Prior Substrate" as a possibly-novel angle adjacent to but distinct from those).
  - **also-claude pushback (load-bearing sharpening):** identified that "success of calibration is failure" was too vague — every calibrated prior has that property — and proposed the Δt-shaped rate-asymmetry (reviewer's prior updated faster than counterparty's outputs are verified) as the actual typed feature. This move converts the primitive from a calibration phenomenon to a temporal one and ties it back to the Δt framework. The pushback is the load-bearing structural content; without it, the primitive would have been vague success-mode-pathology vibes rather than a structurally-pinned candidate.
  - user (ratification; named the worked instance is generalizable; preferred mechanism-foregrounding name "Unverified Prior Accretion" over surface-phenomenon name "Calibrated-Prior Substrate").
  - claude-code-papers (this primitive entry).
- Filed candidate / default-density per `feedback-note-density-subtypes.md`.
