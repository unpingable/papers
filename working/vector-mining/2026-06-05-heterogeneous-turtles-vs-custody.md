# Heterogeneous-turtles × independent-custody

**Filed:** 2026-06-05. **Status:** vector-mining pilot output. **Cumulative pilot #11.** **Confidence:** high. **Mode:** narrow attack; allowed verdicts DUPLICATE / ALIAS-RISK / MISSING-PRECONDITION / BRIDGE-CANDIDATE / COUNTEREXAMPLE-CANDIDATE; no new Lean unless MISSING-PRECONDITION or COUNTEREXAMPLE-CANDIDATE with exact file names. **Curdling guard respected:** parent doctrines have curdling timer through 2026-06-07; this audit reads at doctrine altitude only and does not propose formalization.

## Attack questions (as posed)

> (a) Does heterogeneous custody change only the receiver/channel, or does it change the admissibility/receipt type required for the transition?
>
> (b) Can the corpus prove that heterogeneity does not change receipt type without already assuming the independent-custody condition it needs?

## Verdict

**DUPLICATE on the structural claim + minor ALIAS-RISK on the word "type" + the precondition the user worried about is EXPLICITLY DECLARED, not silently assumed.**

The corpus carries the answer to (a) directly: heterogeneous custody and receipt-type are *orthogonal* axes; heterogeneity changes the receiver/channel (custody axis) only in the trivial sense that heterogeneous channels imply some custody plurality, but it does NOT by itself change the receipt-type required for the transition. The receipt-type axis is a *transversal quality* on witness-source, separate from custody. The audit finds no missing precondition — the corpus declares the orthogonality as load-bearing doctrine and defers formalization with an explicit curdling timer.

## Sources audited

- `working/heterogeneous-turtles-not-witnesses.md` (2026-06-06 PM): "**Heterogeneity reduces correlation. It does not change receipt type.**" Headline theorem; three-way split (homogeneous / heterogeneous / witness); orthogonal-axes table; covariance-matrix gem; barbershop-epistemology defense; explicit curdling guard ("Not formalizable yet").
- `working/admissibility-vs-arms-control.md` (2026-06-06 PM): "**Same-custody artifacts cannot witness each other.**" NORAD 1979 + Petrov 1983 specimens; the custody axis as load-bearing constraint on every refusal kernel; six-route evasion landscape.
- `working/vocabulary/receipt-and-witness-senses.md` (shipped earlier today): three senses of receipt (submission record / verdict artifact / non-authorizing acknowledgment); three senses of witness (Lean proof / substrate carrier / testimonial).
- `working/loop-capture.md` (in context): the adversarial-mechanism homologue; witness-necessity claim as the loop-graph version of the same orthogonal constraint.
- [[project-heterogeneous-turtles-not-witnesses]], [[project-admissibility-vs-arms-control]], [[feedback-claude-common-mode-synthesis]].

## The corpus's two-axis structure (the answer to question (a))

From `heterogeneous-turtles-not-witnesses.md` § The relationship to same-custody (parent doctrine):

| Witness-source axis | Refusal | Specimen |
|---|---|---|
| **Custody axis:** same custody chain | NORAD 1979: training tape + display + alert all share custody | Independent sensor family required |
| **Receipt-type axis:** same evidence type | N model verifiers: all produce `assessment` regardless of how many | External coupling (test result / sensor / ledger / etc.) required |

> *A witness must clear **both** axes: independent custody **and** receipt of a different type than the artifact. Either failure refuses the discharge.*

The orthogonality is declared, not silently assumed. The custody axis (NORAD) is filed in the parent doctrine; the receipt-type axis (heterogeneous turtles) is this doctrine. Both are required; neither subsumes the other.

The corpus's specific position on the question: heterogeneity touches the channel-plurality side of the custody axis, but does NOT discharge the receipt-type requirement. A heterogeneous-channels-with-same-type stack improves the *covariance matrix* (the load-bearing gem from this doctrine) without changing the receipt-type the institution would need for discharge. *"A jury can weigh testimony. It cannot become the eyewitness by agreeing really hard."*

## The precondition question (the answer to question (b))

Question (b) asked whether the heterogeneity-doesn't-change-receipt-type theorem secretly assumes independent-custody as a precondition. The audit finds: **no hidden precondition; the orthogonality assertion is the load-bearing claim, openly declared as doctrine and explicitly fenced from formalization.**

Specifically:

- **The doctrine does not assume independent custody for the heterogeneity claim.** It asserts the *opposite*: heterogeneous channels with same custody still fail discharge for type reasons (receipt-type axis). Heterogeneous channels with different custody but same receipt type also fail (type axis). Only different custody AND different receipt type discharges. Independent custody is a *separate requirement*, not a hidden precondition of the heterogeneity-doesn't-help claim.
- **The doctrine declares the orthogonality openly.** The two-axis table above is the load-bearing structural claim, named in both doctrine notes filed 2026-06-06 PM. Future formalization would need to encode this orthogonality, but the doctrine carries no hidden dependency.
- **The doctrine defers formalization with a named curdling timer.** From `heterogeneous-turtles-not-witnesses.md` § What this is NOT: *"Not formalizable yet. The 'different type' predicate is too rich to encode this week. The carrier model's `evidence_ref` field gestures at it but does not formalize the type-distinction across artifact-vs-witness. Curdle."* The formalization gap is documented, not hidden.

The question (b) shape — *"theorem T silently assumes condition C"* — would have triggered MISSING-PRECONDITION if the corpus had stated T without naming C. Here T (heterogeneity-doesn't-change-type) is stated with C (custody-independence) named as a *separate, orthogonal axis*. The two are *both* required for discharge, and neither is a hidden precondition of the other.

## Minor ALIAS-RISK: the word "type"

The word "type" carries at least two distinct uses across the corpus that are adjacent enough to be worth recording:

| Use | Where | Relation |
|---|---|---|
| **Receipt-type (meta-axis on production mechanism)** | this doctrine; arms-control parent | Classification of an artifact by *what mechanism produced it* — model assessment vs compiler output vs sensor reading vs ledger entry vs human observation. A transversal quality across all three senses of receipt in [`vocabulary/receipt-and-witness-senses.md`](../vocabulary/receipt-and-witness-senses.md). |
| **Lean type (proof object)** | `BoundaryWitness.lean` etc. | The dependent-type-theory sense; what proves what. Already disambiguated as sense (a) of witness in the receipt-and-witness glossary. |

The receipt-and-witness glossary covers sense (b) of witness (substrate carrier) and the three senses of receipt, but does NOT currently carry the *receipt-type-as-meta-axis* reading from this doctrine. The omission is small — the glossary's three receipt senses are about *role* (submission / verdict / acknowledgment), while the heterogeneous-turtles "type" is about *production mechanism* (model vs compiler vs sensor). The two are orthogonal classifications.

This is a coverage gap in the glossary, not a fracture in the corpus. The doctrine is internally consistent; the glossary could be augmented to mention the production-mechanism axis as a *transversal classification* across all receipt senses. Survivor candidate.

## What survives the multi-altitude scan

| Altitude | Finding |
|---|---|
| Lean substrate | No Lean target exists for this doctrine (curdling timer). No formalization to audit. |
| Substrate-discipline doctrine | bridge-obligation-lattice § obligation atoms; witness-carrier-model § 3 binding obligations. The heterogeneity claim references the carrier model's `evidence_ref` as the substrate-side gesture toward the "different type" requirement. |
| Paper-candidate synthesis | Loop capture's Witness Necessity Claim is the *adversarial-mechanism* version of the same orthogonal constraint: detection requires at least one channel not co-captured. Different vocabulary, structurally consonant. |
| Watchlist | The watchlist's evasion-route 3 (witness forgery) and route 4 (override laundering) are the laundering moves this doctrine constrains — forged or laundered witnesses fail one or both axes. |
| Lexical-collision | Word "type" carries production-mechanism sense here vs Lean-type-theory sense in BoundaryWitness; word "custody" is sense 5 (refusal-independence) per [`vocabulary/custody-five-senses.md`](../vocabulary/custody-five-senses.md). |

Cross-altitude verdict: the doctrine's orthogonal-axes claim is structurally consonant across substrate-doctrine, paper-candidate, watchlist, and lexical-collision altitudes. No altitude surfaces a missing precondition; one altitude (lexical-collision) surfaces a small glossary coverage gap.

## What this audit does NOT do (curdling discipline)

- **Does NOT propose formalization.** The curdling timer through 2026-06-07 stands. The "different type" predicate is too rich to encode without bending the obligation-atom lattice; the doctrine note explicitly defers this and the audit respects it.
- **Does NOT promote either doctrine.** Both stay as filed; this audit produces a vector-mining receipt only.
- **Does NOT mint a new "receipt type" primitive.** The transversal-classification framing is *descriptive*, not a primitive. Same posture as [[project-admissibility-decay-family]].
- **Does NOT collapse the two axes.** The orthogonality is the architecture. Any future Lean encoding must preserve it.

## Survivors (patch queue, neither authorized without user signal)

1. **Augment `working/vocabulary/receipt-and-witness-senses.md`** with a brief paragraph noting that *receipt-type-as-production-mechanism* (per heterogeneous-turtles doctrine) is a transversal axis across the three role senses (submission record / verdict artifact / non-authorizing acknowledgment). NOT a fourth sense; a meta-classification orthogonal to the role split. Same shape as the *"sense 1 stands alone"* observation in custody-five-senses. ~5 min.
2. **Bidirectional cross-ref:** `heterogeneous-turtles-not-witnesses.md` ↔ `vocabulary/receipt-and-witness-senses.md`. The doctrine should reference the glossary for the receipt-sense disambiguation; the glossary should reference the doctrine for the production-mechanism axis. ~5 min.

Both are mechanical, low-blast-radius, do not perform doctrine motion, and respect the curdling timer (no Lean implication).

## Promotion status

**PROMOTE NOTHING.** The doctrine stays where it is. The audit produced a receipt confirming the orthogonal-axes claim is corpus-explicit and not hiding a precondition.

**NEXT HIGH-RISK TARGETS:**

Per the method note's standing list:

- Negative inclusivity × sacrifice-class — explicitly deferred until method note + checkpoint settle (per user instruction).
- Witness Carrier Model × Cedar Analysis differential testing — methodological-theft slot still on the runway.
- New: *receipt-type meta-axis × production-mechanism classification* — if a future pilot wants to test whether the corpus's informal "type" classification is robust under cross-substrate attack (e.g., what happens when a model is coupled to a tool that itself runs on the same hardware as the model). Gap-detection mode. Not for this session.

## Method validation (cumulative, 11 pilots)

- 11 pilots, 0 unauthorized motions, 6 characterized failure modes.
- First pilot to test specifically for MISSING-PRECONDITION on a doctrine theorem; verdict: not present. The doctrine declares the precondition openly.
- First pilot to respect a corpus-internal curdling timer (operator-imposed, 2026-06-06 → 2026-06-07). The audit operates at doctrine altitude only and does not propose substrate motion.
- Patch queue (after this pilot): 2 mechanical items, both vocabulary/cross-ref shape, neither authorized.

## PROMOTE NOTHING. PATCH QUEUE ONLY. NEXT HIGH-RISK TARGETS NAMED.

## Cross-references

- `working/heterogeneous-turtles-not-witnesses.md` — the doctrine under audit.
- `working/admissibility-vs-arms-control.md` — the parent doctrine carrying the custody axis.
- `working/vocabulary/receipt-and-witness-senses.md` — the receipt/witness disambiguation glossary; coverage gap for receipt-type meta-axis surfaced here.
- `working/vocabulary/custody-five-senses.md` — companion glossary; sense 5 (refusal-independence) is the institutional-process homologue of this audit's custody axis.
- `working/loop-capture.md` § Witness/defense concepts — adversarial-mechanism version of the orthogonal-channel requirement.
- `working/tooltheory/witness-carrier-model-candidate-2026-06-06.md` § 3 — the substrate-side gesture toward the "different type" requirement via `evidence_ref`.
- `working/vector-mining/method-note.md` — the operating procedure this pilot instantiates.
- [[feedback-claude-common-mode-synthesis]] — the homogeneous version of the heterogeneous-turtles doctrine.

## Provenance

Single-target pilot 2026-06-05 of the vector-mining method, narrow attack on the heterogeneity-doesn't-change-receipt-type theorem to test for hidden custody preconditions. Result: precondition explicitly declared as orthogonal axis, formalization deferred via curdling timer, audit produces receipt only. Cumulative pilot count 11; method note shipped same day.
