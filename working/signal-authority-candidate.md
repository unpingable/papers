# Signal Authority — Candidate Doctrine

**Status:** Candidate / exploration phase, not ratified, with a checked formalization-leading slice at `~/git/lean/LeanProofs/Scratch/SignalAuthority.lean`. Platform-mediated, interpersonal, and bureaucratic silence are worked cases, not authorization tokens. The Scratch module is unwired and not imported by `LeanProofs.lean`; it formalizes the bounded no-objection/solicitation seam rather than the entire doctrine below.

## The protocol-level reframe (keeper stack)

The recurring failure mode is treating silence as a verdict when the channel does not define it as one. The reframe is protocol-level:

- **Missing ACK ≠ NACK.** Absence of confirmation is not rejection.
- **Timeout ≠ verdict.** A waiting limit is not the other side's judgment.
- **Silence ≠ revocation unless the protocol explicitly says so.**
- **If the protocol does say so, the protocol itself may be the problem.**
- **Instrumented silence ≠ meaningful silence.** Platform metrics make the null look like data.
- **Telemetry-looking signals ≠ authority.** Dashboards do not automatically have standing.
- **A collapsed public surface cannot carry cause-specific authority.** When a render function maps distinct causes to the same surface, the surface cannot license inferences about which cause acted. *This is observation-equivalence (Paper 25, also Paper 23 §observational-masking, Paper 24 §alias-compatibility), applied to platform render. Already in the corpus; see "Relation to observation-equivalence" below.*

The bridge into the broader corpus is the last line, sharpened:

> **The dashboard had no standing.**

Same disease as the existing admissibility / authority / receipt-based work, applied to an axis the kernel doesn't currently cover: the misclassification of *absence* as *event*.

## The deepest move: null-laundering

Recurring chain:

```
no signal
  → interpreted as negative signal
  → treated as verdict
  → used to revoke standing
  → self-correction / state-mutation fires
```

This is structurally distinct from artifact-misuse (which FiatAdmissibility covers) — it's *non-event misclassified as event*. The controller manufactures an evidentiary object out of a null, then treats the fabricated object as authoritative.

Sharper version:

> **A non-event cannot authorize a state change unless the governing protocol classifies the non-event as an event.**

That theorem has range across personal-controller, platform-controller, and bureaucratic-controller domains — the same bug instantiated three different ways.

## Two failure modes (different repairs)

The protocol distinction has two variants with materially different repair operators:

**Unauthorized protocol extension** (personal / platform):

- The channel does NOT define silence as revocation.
- The internal controller hallucinates that rule.
- *Repair: reject the inference.* The clause being installed isn't part of the channel; the controller is running an unauthorized protocol extension on top of the actual channel semantics.

**Authorized-but-illegitimate protocol clause** (bureaucratic / institutional):

- The channel DOES define silence as revocation.
- But the clause itself may be coercive, obscure, inaccessible, or never consented to.
- *Repair: contest the protocol.* The clause is part of the channel, but its legitimacy is the real problem.

Examples of authorized-but-illegitimate:

- "We never heard back so we proceeded as if denied."
- "The form was never returned so the standing lapsed."
- "No one objected in the comment period so it became policy."
- *qui tacet consentire videtur* deployed against parties who never knew the protocol applied.

The personal version repairs by rejecting the inference. The bureaucratic version repairs by contesting the protocol. Same shape, different countermeasure, different leverage point. Conflating them produces wrong repairs in both directions.

## Platform-as-pseudo-telemetry

The interesting observation about social/platform media specifically:

> **The environment formats the null as a measurement.**

Silence in a notebook contains zero bits of information. Silence in a Substack analytics view, a Bsky thread, a GitHub issue, contains zero bits of information *displayed inside an authority-shaped interface*. The interface makes silence look measured. Once something looks measured, the nervous system starts treating it as admissible evidence.

The platform doesn't merely fail to respond — it places non-response inside dashboards, counters, engagement surfaces, timestamps, and adjacency cues:

| Surface event | Could mean | Gets misread as |
|---|---|---|
| No likes | no one saw it, niche topic, ranking suppression, timing | rejection |
| No replies | nothing to add, agreement, fatigue, invisible reach | nobody cares |
| Quote post | amplification, status play, adversarial framing | public verdict |
| Someone else gets reach | network luck, simpler phrasing, existing audience | proof your version failed |
| Follower silence | normal passivity, private agreement, not online | withheld recognition |

The platform exposes just enough telemetry to make the operator feel they're running a measured system, but not enough to make the measurements admissible. The operator becomes an SRE for their own standing using garbage dashboards run by a slot machine.

Keeper for this specific case:

> **The problem isn't silence. It's silence displayed inside an authority-shaped interface.**

## Relation to observation-equivalence (2026-05-11 — corrects an earlier overclaim)

An earlier draft of this note proposed extending Signal Authority to cover "collapsed surfaces" (e.g. Bsky tombstones rendering distinct causes — user deletion, platform suspension, legal restriction, viewer filter, infrastructure failure — to the same `notFound` UI state). The proposal treated this as a new signal-shape family with new theorem candidates `collapsed_surface_not_identifying` and `public_receipt_refines_observation`.

**That framing was redundant rediscovery.** The corpus already has this apparatus:

- **Paper 23 §observational-masking.** Three formal conditions under which distinct controller compositions are observationally indistinguishable through the authority projection and measurement map. "Controller-family confounding (local gain aliasing)" is exactly the render-non-injective-on-causes claim.
- **Paper 24 §alias-compatibility.** Public alignment to a shared prior is alias-compatible between cohesive and hiddenly-divergent agent populations under stationary conditions; the divergence surfaces only under strategic shift. Proposition 2.
- **Paper 25 §observation-equivalence.** Theorem 1 (`obsEquiv_policy_same`): any policy depending only on the observation trace is constant on observation-equivalence classes. Plus the target-distinct corollary: observation-equivalent states with distinct targets still receive identical control sequences. Formalized in `~/git/lean/LeanProofs/Paper25EpistemicBorderControl.lean`, lake build green.

So the Bsky tombstone case is an *instance of observation-equivalence applied to platform render*, not a new Signal Authority extension. The structural result already exists, already proven.

**The distinction that survives:**

Signal Authority's *original* scope (null/silence/timeout misclassified as verdict) is genuinely different from observation-equivalence:

- *Null-as-verdict (Signal Authority):* there is no signal; controller manufactures a verdict from the null
- *Observation-equivalence (Paper 25 et al.):* there is a signal; it is compatible with multiple distinct causes; controller manufactures a cause-attribution from a non-discriminating signal

Same broader family ("the signal cannot license the inference drawn from it") but sibling primitives, not nested. The collapsed-surface case lives in the Paper 25 lane.

**Useful unification (prose register, not formal):**

> A deficient signal surface is treated as authority-bearing evidence.

This is the family-level claim that covers both Signal Authority's null cases and Paper 25's observation-equivalence cases. *Not promoted to primitive* — it's a descriptive cross-reference, similar to the admissibility-decay family note. The formal load is already carried by Papers 23/24/25 + Signal Authority candidate.

**Bsky as specimen cluster for Paper 25, not single anecdote:**

The tombstone case is not one specimen — it's a *recurring lab specimen cluster* you've been circling across multiple Bsky moderation surfaces over more than a year:

- Tombstone-collapses-causes (the render non-injectivity case originally proposed)
- December 2024 likes-bot / developer-ban with no public audit trail
- Labelers as soft blacklist machinery ("we don't ban, we label" with weak provenance)
- Ozone / strike opacity (account-level state transitions, threshold enforcement, mostly mod-facing)
- No reliable state-at-time-T primitive — outsiders cannot reconstruct what was visible / removed / labeled / appealed / state-changed when
- Relay / AppView / PDS choke points where selective omission or state loss may be hard to detect downstream
- Concern-report and self-harm-reporting tools that can be weaponized without public receipts
- Repeated cases where backend says one thing and public sees another

The broader theorem target is therefore wider than just "render function non-injective on causes." It is **forensic underdetermination by design**:

> Authority-distinct state transitions that collapse to the same public surface cannot support authority-specific inference without receipts or discriminating history.

This still lands in Paper 25's lane (observation-equivalence + receipt-lineage from Paper 24), but the corpus pressure is broader: missing state-at-time-T, no public action class, no cause-class receipt, no public appeal/reversal markers, and no provenance for who acted (user, platform, labeler, legal, app bug, infra path). Each one is a *separate failure of discriminating structure*, not just one missing dimension.

Keeper for the platform-domain summary:

> **Opaque moderation does not merely hide decisions. It destroys the public's ability to distinguish decision, deletion, disappearance, filtering, and failure.**

Filing recommendation: if/when written up, the natural home is a *Paper 25 platform-instance working note* or §addendum, not Signal Authority. Reserving title: `working/paper25-platform-moderation-specimen.md` (or similar) — not creating it now; flagging that the specimen cluster exists and is mature enough to write up as an applied instance of existing Paper 25/23/24 apparatus.

**Adjacent observation worth flagging, not in this note's lane:**

A distinct pattern showed up in the same thread: when a platform's public explainer answers a distributional / pattern-of-enforcement challenge in an individual-conduct frame ("identity doesn't excuse harassment" in response to "is enforcement disproportionate?"), the response *does not engage the challenge as posed.* This is closer to FiatAdmissibility shape (kind-of-response licensing engagement with kind-of-challenge) than to Signal Authority. Possibly an instance of existing apparatus: a conduct-frame artifact does not license a pattern-frame response. Flagging only; not Signal Authority's territory.

**Lean theorems already exist:**

The theorem `obsEquiv_policy_same` in `Paper25EpistemicBorderControl.lean` is the formal core. `collapsed_surface_not_identifying` and `public_receipt_refines_observation` as I proposed them earlier are not new — `obsEquiv_policy_same` is the first; the second (receipt-refines-observation) is implicit in Paper 24's receipt-lineage discussion ("preserving per-witness receipts for downstream interpretation") as the constructive complement to the witness-filter pathology. The Lean module names I reserved should be retired in favor of pointing at the existing kit.

## Recovery side: breaking collapsed observation

A collapsed surface cannot identify cause from the surface alone. Recovery requires a discriminating channel outside the collapsed render.

Known recovery paths:

1. **Preserved history.** Receipts, lineage, state-at-time-T records, or provenance that preserve distinctions the public surface erased. *Partial corpus home:* Paper 24's receipt-lineage / per-witness preservation discussion.
2. **Independent measurement.** Another witness/sensor whose observations add rank rather than replicate the same collapsed surface. *Partial corpus home:* Paper 25's Gramian scaling under inhomogeneous-witness stacking (`ker_replicateRows_eq_ker`, `replicateRows_transpose_mul`).
3. **Admissible perturbation.** Controlled excitation that produces distinguishable response traces — system-identification-style — without treating harm or coercion as measurement. *Newly named here; underspecified; not in corpus formally.* The "admissible" qualifier is doing real work: not all perturbations are licensed measurement, and conflating them produces its own laundering pattern.

> **Reading the tombstone harder does not recover the body.**

**Status:** held synthesis / deferred theorem family. Preserved-history and independent-measurement cases have partial homes in P24/P25. Admissible perturbation is newly named here and remains underspecified. The three-part shape is stable enough across repeated cross-primitive surfacing (testimony-vs-self-theory, Signal Authority, CollapsedSurface) to preserve as doctrine; not stable enough to formalize as Lean theorem machinery. Captured here as deferred recovery doctrine, not as `public_receipt_refines_observation.lean`.

The discipline this expresses:

> *Deferral should prevent premature proof, not erase repeated convergence.*

## Relation to existing kit

This *brushes* FiatAdmissibility without becoming a new UseKind. The difference is the axis:

| Admissibility axis | What gets misclassified |
|---|---|
| Authority × state-mutation (existing kernel) | Operator's right to mutate state |
| Witness × invariance (WitnessInvariance) | Whether testimony survives perturbation |
| Artifact-kind × use-kind (FiatAdmissibility) | Whether artifact's category licenses demanded use |
| **Signal-shape × authority-status (this candidate)** | **Whether absence/timeout/silence licenses standing change** |

The shared shape: a controller treating something as evidence that the protocol does not grant evidentiary status. *Unauthorized protocol extension* is exactly what FiatAdmissibility refuses for artifacts — extended inward to the signal layer.

Other connections:

- **`working/testimony-vs-self-theory.md`** — same "admit the signal, don't let the signal appoint itself system diagram" shape, with absence as the witness. The keeper "admitting testimony does not admit the testimony's preferred theory of itself" applies: admitting a null does not admit any preferred reading of the null.
- **`project-admissibility-doctrine-stubs.md`** — declared-substitution stubs ("the tractable thing will always try to wear the name of the true thing"). Null-laundering is the same crime with absence as the tractable thing wearing the name of a verdict.
- **Laundering-pattern family** (attack-surface, control-set, scope, evidentiary-exclusion) — null-laundering is the *signal-side* sibling.
- **P17 Receipt the Compiler, P19 Shadow Governance** — bureaucratic-silence-as-verdict is what the second failure mode names formally.

## Lean extraction and broader formal reserve

The checked Scratch slice was extracted from the field-guide's
`NoObjectionRequiresSolicitation` shape. It formalizes before any runtime
checker exists and repairs the source sketch by requiring:

- exact group, decision, and numeric response-window binding;
- solicitation coverage for every group member;
- a closed response window and complete objection ledger;
- absence of in-scope recorded objections;
- positive, paired-world, and collapsed-empty-list specimens.

It claims no consent, agreement, decision correctness, or completeness for
unmodeled channels. If custody review later promotes the broader candidate, the
possible public home remains:

```
~/git/lean/LeanProofs/Admissibility/SignalAuthority.lean
```

Module name discipline: *SignalAuthority*, not *SilenceAsRevocation*. The latter is essay-title shaped — too hot, too likely to wear eyeliner. *SignalAuthority* is neutral, technical, durable. The current file is Scratch; the `Admissibility/` path is not reserved by consumer demand.

Three-layer structure (sketch, not final):

1. **Signal shape:** `ack | nack | silence | timeout | partialSignal | ambiguousSignal`
2. **Protocol authority:** does this channel grant this signal-shape standing-changing semantics?
3. **Weight / consequence:** even with interpretive weight, what kind — evidence of delay, evidence of non-delivery, evidence of refusal, procedural lapse, revocation, no standing effect?

The Boolean form (`silenceMeansNothing | silenceMeansRejection`) is too coarse. Real channels have **time-indexed, channel-indexed, relationship-indexed** silence-semantics: email-silence-after-three-business-days reads differently than email-silence-after-three-minutes — same protocol, time-indexed interpretation. The Lean shape needs to handle that without exploding.

Broader theorem family (not claimed by the checked no-objection slice):

- `missing_ack_is_not_nack`
- `timeout_is_not_verdict_without_semantics`
- `silence_preserves_standing_by_default`
- `revocation_requires_explicit_protocol_rule`
- `non_event_cannot_authorize_state_change` — deepest; trans-domain reach
- `unauthorized_protocol_extension` vs `authorized_but_illegitimate_clause` as distinct verdict pathways with distinct repair operators

*Earlier draft also proposed `collapsed_surface_not_identifying` and `public_receipt_refines_observation`. Both were redundant with existing corpus — see "Relation to observation-equivalence" section above. Retired from this theorem family in favor of pointing at Paper 25's `obsEquiv_policy_same` (already proven in Lean) and Paper 24's receipt-lineage discussion.*

The last pair is the structurally important one: the verdict space probably needs to distinguish "this controller is hallucinating a clause" from "this controller is correctly applying a clause the protocol shouldn't have."

## What's still open (explicit)

- **The broad doctrine is not fully formalized.** Boolean verdicts, weighted evidence, protocol-defined lapse, and illegitimate authority clauses remain discriminating prose questions. A further theorem needs a coherent non-duplicative statement; it does not need a consumer to ask.
- **Primitive not promoted.** An independent worked case outside personal/social/bureaucratic settings would strengthen doctrine review. Candidates: distributed-systems liveness/silence semantics; financial-market silence-as-confirmation patterns; security-incident-silence-as-resolved patterns. *Note (2026-05-11, corrected):* an earlier draft treated the Bsky tombstone as a signal-shape extension to this candidate. That was rediscovery of Paper 25's observation-equivalence framework, not a Signal Authority extension. See "Relation to observation-equivalence" section. The Bsky case is a platform-domain instance of Paper 25, not a Signal Authority case.
- **Composition with FiatAdmissibility not explored.** Whether SignalAuthority needs `outOfScope` for cases handled by FiatAdmissibility's artifact-kind axis is open. Likely yes, on the same custody-recursion logic that makes `mutateState → outOfScope` in FiatAdmissibility.

## Posture rule (durable regardless of application context)

The discipline that surfaced alongside the doctrine:

> **Explore the primitive at protocol level. Do not use the primitive to adjudicate the live self.**

Protocols are tested against channels, not against an operator's state. Doctrine work survives daylight regardless of the generating mood-state; introspective work doesn't, and shouldn't carry the doctrine's weight. The protocol-framing primitive is the part that does not depend on whether the operator is doing it right at any given moment.

## Ratification gate

Conditions for promoting candidate → doctrine:

- An independent worked case outside the originating cluster (distributed-systems, market, security, regulatory)
- **Generator test:** does it cut sharply enough to disqualify a candidate or rule out a category of inferences?
- **Kind test (per primitive ontology):** tentatively a *boundary* — between what signal-shapes can license standing-change authority and what cannot. Possibly an axis if it composes cleanly with FiatAdmissibility.
- Decision on whether Boolean form is genuinely too coarse for v0 or sufficient
- Composition audit with FiatAdmissibility — overlapping coverage or sibling axes?

Not promoted. Filed.

---

**Cross-references:**

- [testimony-vs-self-theory.md](testimony-vs-self-theory.md) — sibling on the testimony-axis (witness reliability about state vs. substrate)
- [collaborator-entry-map.md](collaborator-entry-map.md) — corpus entry framing
- [corpus-map-internal.md](corpus-map-internal.md) — internal diagnostic map
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — the artifact-kind × use-kind sibling kernel
- `project-admissibility-doctrine-stubs.md` (memory) — declared-substitution family
