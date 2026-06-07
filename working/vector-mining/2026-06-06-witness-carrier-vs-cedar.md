# Pilot #12 — Witness Carrier Model × Cedar Analysis differential testing

**Filed:** 2026-06-06. **Status:** vector-mining receipt. **NOT doctrine. NOT a paper. NOT a primitive. NOT a Lean module.** Operating under [`method-note.md`](method-note.md) discipline.

## Setup

The relay-shaped framing under audit:

> *Run a differential-testing pilot between the Witness Carrier Model (WCM) and Cedar Analysis. See whether the instrument can find a real bridge between the substrate carrier model and the closest external neighbor.*

Inputs read:

- [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) — the candidate carrier model under test
- [`../admissibility-as-pre-authorization-layer.md`](../admissibility-as-pre-authorization-layer.md) — positioning note with explicit Cedar-relative section
- [`../tooltheory/admissibility-related-work-map.md`](../tooltheory/admissibility-related-work-map.md) — Cedar row + § Adjacent methodological theft
- [`../tooltheory/documentation-keepers.md`](../tooltheory/documentation-keepers.md) — two Cedar-relative keeper sentences
- [`../where-admissibility-fits.md`](../where-admissibility-fits.md) — PDP-role placement with "deliberate refusal to grow into a policy DSL"
- `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` (lines 50–75) — substrate-gap header naming Cedar Lean/Rust as the worked template

## Verdict

> **PREVENTIVE GATE + ALIAS-RISK + INTERNAL-REFUTATION GAP.**

Three failure modes fire, none of them new:

1. **PREVENTIVE GATE (failure mode #4).** The corpus has already built four structures that block the relay-shape collapse before it lands:
   - `admissibility-as-pre-authorization-layer.md` § Falsifier names the *reification gambit* as the specific way Cedar Analysis could absorb the layer; declares this the falsifier of the positioning, not a synthesis path.
   - Same file § Cedar-relative positioning supplies the 7-row obligation map (upstream-questions ↔ bridge-obligation atoms) that locates Cedar one altitude downstream of WCM.
   - `admissibility-related-work-map.md` § Adjacent methodological theft names Cedar's Lean↔Rust differential randomized testing as the methodological template *for the BoundaryTransit substrate gap*, not for WCM-Cedar unification.
   - WCM § 7 guardrail #5: *"Differential harness is future Level 4. Cedar's Lean ↔ Rust differential randomized testing is the methodological template; the harness is not built. Do not promote."*

2. **ALIAS-RISK on "differential testing".** Two distinct senses fight under one phrase:
   - *Cedar-internal sense:* Lean model ↔ Rust production engine, same artifact two implementations, **correctness check across implementations of the same semantics**. This is what Cedar's published differential-randomized-testing methodology does.
   - *Vector-mining sense:* WCM refusal set vs Cedar Analysis encodable set, **coverage check across two different tools at different layers**. This is what "WCM × Cedar differential testing" sounds like at first read.

   Both are legitimate; they are not the same instrument. The WCM § 7 guardrail #5 reference is the first sense; the relay-framing of this pilot is the second sense. Conflating them imports a "build the harness" obligation from sense 1 into sense 2, which is not what either party signed up for.

3. **INTERNAL-REFUTATION GAP (failure mode #6).** Same shape as pilot #10 (Composition substrate × LGVG). The corpus's *own* substrate work has already done the federation-doctrine refusal of WCM-Cedar unification:
   - The pre-auth-layer note literally says *"Cedar trusts the application to supply the witness facts. The hard problem moves outside Cedar."*
   - The keepers file enshrines *"Cedar guards the door. This asks whether the door is where everyone says it is..."* as the strongest external-pitch keeper of the round.
   - The federation doctrine ([[project-no-unifier-without-laundering]]) is the doctrinal frame that makes unification across this seam refused-by-default rather than open-by-default.

   The audit's job here is to *record the existing refusal*, not produce a new one.

## Row-by-row differential (the vector-mining-sense version)

For each of WCM § 6's seven refusal rows, can Cedar Analysis encode the refusal? *Conjectured pending Cedar reading per related-work-map status caveat — first column claim-shape, last column observation-shape only when the literature gets witnessed.*

| WCM refusal row | Cedar-encodable? | Note |
|---|---|---|
| **self-minted** | Partly via reification | Cedar can model `issuer` as an entity and check `MayMint` over entity attributes. Cannot prove the fact's origin — Cedar treats supplied facts as inputs. *Layer-honest answer: the reification just relocates the admissibility check upstream of Cedar.* |
| **replayed** | No (without extension) | No native nonce / spendability primitive in Cedar's policy semantics. The reification gambit (model spent-set as entity attribute) works, but converts the question into authz-over-enriched-input. |
| **wrong-surface** | Partly | `surface` can be a resource attribute; Cedar checks resource match. The bind-vs-advisory distinction (signed-coverage vs labelled-string) is outside Cedar's frame — Cedar trusts the label. |
| **stale** | Yes-ish | Standard Cedar pattern: `context.now in policy.valid_window`. Cedar Analysis can prove the temporal property holds across modeled scenarios. The freshness-of-`now` itself is supplied input. |
| **widened-after-issue** | No | Cedar evaluates a single policy at a single time; chain-narrowing requires history of derivations. Outside the single-decision frame. |
| **post-hoc laundering** | No | `issued_at` vs `transition_history` is a time-axis property over multiple events; Cedar's frame is single-evaluation. Reification possible but does the relocation again. |
| **wrong-attempt** | Partly | `attempt_id` can be an entity attribute; Cedar checks match. Cryptographic binding of `attempt_id` to signature coverage is outside Cedar's frame. |

**Pattern in the rows.** Where Cedar can encode at all, it does so via *the reification gambit*: model the witness-fact as an enriched-entity attribute and check that attribute. The corpus's own falsifier already names this: *"making the admissibility layer instrumentally invisible rather than absent."* The layer doesn't go away; it gets moved one step earlier in the pipeline (the application now owes the *correctly-minted* entity attribute before Cedar can usefully check it). WCM is the discipline for the step Cedar pushes upstream.

This is not a contradiction. This is the layer-separation working exactly as the pre-auth-layer note positions it.

## Altitude scan

Per [`method-note.md`](method-note.md) § Altitude scan requirements:

1. **Lean substrate.** BoundaryTransit.lean (Scratch/) names the Cedar template explicitly. No other Lean module owns WCM-Cedar territory. Conflict surface: none. The Lean witness ≠ production witness gap is openly declared in the file header.
2. **Substrate-discipline doctrine.** WCM file + pre-auth-layer file + related-work map all cite Cedar by name. Three independent treatments converge on layer-separation; no internal contradiction.
3. **Paper-candidate synthesis.** `where-admissibility-fits.md` places admissibility kernel at PDP role, *explicitly with a refusal to grow into a policy DSL.* That is the paper-altitude statement of the same boundary.
4. **Watchlist.** [[project-laundering-move-watchlist]] does not currently name a Cedar-specific row; the DeepSeek typed-provenance warning (§ embedded in pre-auth-layer note + related-work-map) does the equivalent work — labels-without-minting-discipline is the watchlist-altitude refusal that fires here.
5. **Lexical-collision altitude.** No `working/vocabulary/` glossary currently disambiguates "differential testing." The ALIAS-RISK above is a candidate glossary entry — earned, not auto-promoted.

Cross-altitude survival: layer-separation between WCM (admissibility) and Cedar (authorization) is consistent at four altitudes and silent at one (no glossary entry). No single-altitude novelty; no claim of a Cedar-collapse-opportunity.

## What the pilot did NOT find

- No DUPLICATE — WCM and Cedar are at distinct, complementary altitudes that the corpus has already mapped. They are not the same object under different vocabulary.
- No LAUNDERING (in the federation sense) — the corpus has already refused the unifier here via the falsifier paragraph and the federation doctrine.
- No MISSING-PRECONDITION — Cedar's preconditions (witness facts as supplied input) are explicitly declared in the corpus's Cedar positioning, not silently assumed.
- No BRIDGE-CANDIDATE survives — the bridge from WCM to Cedar would be the 7-row obligation map already in `admissibility-as-pre-authorization-layer.md`; it is filed and route-signed, not a fresh discovery here.
- No COUNTEREXAMPLE-CANDIDATE — Cedar Analysis does not break WCM's invariants; it shadow-encodes about half of them via the reification gambit. The other half are outside Cedar's frame by construction.
- No COMPOSITION-GAP — the composition `Cedar(application_supplied(WCM-bound_witness))` is exactly the architecture the pre-auth-layer note already names: WCM upstream, Cedar downstream, application bridges with minting discipline.

## Common-mode check

Per [[feedback-claude-common-mode-synthesis]]: the proposing voice for the pilot framing is Claude-family. The corpus check came from reading corpus documents authored across mixed-model exchanges (ChatGPT-led Cedar positioning, DeepSeek-named typed-provenance warning, operator-named four-element discipline banner). The audit-side reference is not Claude-on-Claude; the load-bearing claims of layer-separation come from non-Claude voices in the corpus. Common-mode immunity holds at this pilot's altitude.

The pilot itself is, however, a Claude-Code reading of mostly-Claude-written substrate notes (pre-auth-layer is documented as Claude-Code-authored). If a future synthesis pass *over* this pilot's findings is contemplated, that pass should go through a non-Claude reference before any promotion is considered. Not in scope here.

## Patch queue (refusal-biased; user authorization required before landing)

Two candidates surfaced. Both mechanical, both navigability-only, neither performs doctrine motion. **None landed yet.**

1. **Glossary entry: `working/vocabulary/differential-testing-two-senses.md`** — disambiguates Cedar-internal Lean↔Rust correctness DT vs. vector-mining-altitude WCM-vs-Cedar coverage DT. Same template as `receipt-and-witness-senses.md` / `custody-five-senses.md` / `standing-three-senses.md`. The ALIAS-RISK above is the forcing example. *Earnable, not auto-promoted; user authorizes if wanted.*

2. **Bidirectional cross-reference: WCM § 7 guardrail #5 ↔ pre-auth-layer § Falsifier.** Both files name the federation-doctrine refusal of WCM-Cedar unification, but they don't cite each other on that specific point. A short cross-ref in each direction would surface that the guardrail and the falsifier are doing the same work at different altitudes. Wording draft (does NOT perform reframe): *WCM* → *"The federation-doctrine version of this guardrail lives in [`../admissibility-as-pre-authorization-layer.md`](../admissibility-as-pre-authorization-layer.md) § Falsifier as the reification-gambit fence."* *pre-auth-layer* → *"WCM § 7 guardrail #5 is the substrate-altitude statement of the same fence."*

Patch queue items expire if not landed within ~1 week of pilot. Staleness = deauthorization.

## Curdling guard

This pilot operates at vector-mining altitude only. No Lean implication. No primitive minted. No new file authorized. The Level 4 differential harness remains explicitly unbuilt and explicitly unpromoted per WCM § 7 guardrail #5. The arms-control / heterogeneous-turtles 2026-06-07 timer is not touched by this pilot.

## Cumulative-pilots update

To be appended to [`method-note.md`](method-note.md) § Cumulative pilots table when user authorizes:

| # | Pilot | Verdict | Survivors |
|---|---|---|---|
| 12 | WCM × Cedar Analysis differential | PREVENTIVE GATE + ALIAS-RISK + INTERNAL-REFUTATION GAP | 2 candidate patches (glossary + cross-ref pair), neither landed |

Failure-mode list unchanged. Mode #6 (Internal-Refutation Gap) recurs — same shape as pilot #10, now with a second specimen. Two-specimen recurrence is route-sign that mode #6 is real and stable; it does NOT authorize promotion.

## What this pilot tells the instrument

The boring outcome is the right outcome. The corpus's Cedar positioning has been built deliberately, exhaustively, and across at least four altitudes by mixed authorship over multiple sessions. The instrument did not find a bridge because the corpus does not believe one exists at this layer and has the architecture to back the refusal. Vector mining is doing what it was built for: surfacing that the corpus's existing refusals already cover the territory the relay frame would have promised to deliver.

Honest negative result. File and move on.

## Cross-references

- [`method-note.md`](method-note.md) — operating procedure
- [`2026-06-05-composition-substrate-vs-lgvg.md`](2026-06-05-composition-substrate-vs-lgvg.md) — pilot #10, the first INTERNAL-REFUTATION GAP specimen
- [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) — subject of the audit
- [`../admissibility-as-pre-authorization-layer.md`](../admissibility-as-pre-authorization-layer.md) — falsifier paragraph + Cedar-relative positioning + 7-row obligation map
- [`../tooltheory/admissibility-related-work-map.md`](../tooltheory/admissibility-related-work-map.md) — Cedar row + methodological-theft section
- [[project-no-unifier-without-laundering]] — federation discipline framing the refusal
- [[feedback-claude-common-mode-synthesis]] — methodology check
- [[project-witness-carrier-model]] — memory pointer for the subject

---

**PROMOTE NOTHING. PATCH QUEUE ONLY. NEXT HIGH-RISK TARGETS NAMED.**

Next high-risk targets (named, not authorized):

- **Negative Inclusivity × sacrifice-class** — explicitly held by user; offered as future target.
- **Paper-shape reauthorization** — explicitly held by user.
- **LGVG family-designation reframe** — explicitly held by user.
- **NoSilentException.lean** — held from earlier batch.
- **Aura / PCA (proof-carrying authorization) × WCM minting predicate** — natural next neighbor after Cedar; related-work-map flags Aura as "the most dangerous unread literature" (Priority 1 #1). Would test whether dependent-types-as-receipts in Aura covers WCM's minting predicate shape. Out-of-scope here; would require Aura reading first.
- **Bridge-obligation atoms × Cedar 7-row map** — second-order pilot: does the 7-row map's mapping of Cedar's upstream-questions to bridge obligation atoms hide any laundering, or is it a clean federation-aligned map? Out-of-scope here; would require fresh-context audit of the map itself.
