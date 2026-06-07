# Vector Mining: Corpus-Level Attack Method

**Filed:** 2026-06-05. **Status:** method note. **NOT doctrine.** **NOT a paper.** **NOT a primitive.** Records the operating procedure that emerged from pilots #1–#10 (2026-06-05). Lives here so it does not become folklore.

## What this is

A corpus-level adversarial-discovery procedure that uses Claude Code as an instrumented prober of the existing repository. The goal is *negative*: surface seams, lexical fractures, multi-altitude duplicates, and laundering attempts before they become unauthorized doctrine motion. The procedure produces classified receipts, not theorems.

Slogan: **Prospecting with refusal receipts.** Not synthesis. Not promotion. The corpus's own architecture does the rejection work; vector mining makes the rejection legible.

## Goal

> Find seams, not synthesize.

Concretely:

- locate places where two or more existing artifacts may secretly compose, conflict, duplicate, or expose a missing theorem;
- classify the relationship using verdict classes (below);
- record the receipt at `working/vector-mining/`;
- patch the navigability gap if the verdict warrants it, with hard scope controls.

The procedure refuses to promote, synthesize, or mint primitives. It outputs verdicts and small patch-queue items only.

## Verdict classes

Allowed classifications, in roughly increasing rarity:

- **DUPLICATE** — the proposed object already exists in the corpus under different vocabulary or at a different altitude.
- **ALIAS-RISK** — single word carries multiple distinct relations; the proposed object conflates them.
- **LAUNDERING** — proposed object would collapse refusal surfaces the federation doctrine ([[project-no-unifier-without-laundering]]) requires to be kept separate.
- **MISSING-PRECONDITION** — one corpus artifact silently assumes what another formalizes; the proposed object names the assumption but does not surface the dependency cleanly.
- **BRIDGE-CANDIDATE** — possible cross-kernel theorem; subject to the bridge tax (source surface / target surface / witness / licensed claim / residual scope per [[project-no-unifier-without-laundering]]).
- **COMPOSITION-GAP** — individually valid artifacts fail under composition; may indicate a real gap held open by the federation doctrine.
- **COUNTEREXAMPLE-CANDIDATE** — combination may break an existing assumption; deserves a tiny scratch probe with explicit reason.
- **GAP CONFIRMED + RELAY-FRAMING REFUSED** — real gap exists; the proposed framing is not authorized to fill it.
- **INTERNAL-REFUTATION GAP** — real gap exists; the corpus has already done the federation-doctrine refusal of the tempting unifier internally; the audit *records the existing refusal* rather than producing a new one.
- **DEAD-END** — no real connection; the audit was a false positive.

The default outcome is DUPLICATE, ALIAS-RISK, or LAUNDERING. Anything farther up the list requires explicit citations and survives the multi-altitude scan rule below.

## Altitude scan requirements

> Single-altitude novelty is inadmissible for promotion.

A relay claim must be audited across **all** of the following altitudes before being treated as novel:

1. **Lean substrate** — `LeanProofs/Admissibility/`, `LeanProofs/Scratch/`, and any companion modules. Custody-class markers tell you what's promised vs. fenced.
2. **Substrate-discipline doctrine** — working notes that govern how a substrate is supposed to behave (e.g., `bridge-obligation-lattice.md`, `axis-2-composition-boundary.md`, `witness-carrier-model-candidate-2026-06-06.md`).
3. **Paper-candidate synthesis** — working notes filed under the paper-candidate register (e.g., `loop-capture.md`, `causality-control-plane.md`).
4. **Watchlist** — [[project-laundering-move-watchlist]] and the anti-laundering doctrine map.
5. **Lexical-collision altitude** — the vocabulary glossaries under `working/vocabulary/`. A relay claim that uses a corpus word (standing, custody, receipt, witness, etc.) must be checked against the senses inventory there.

A claim that looks novel at altitude *n* may be old at altitude *m*. Vector mining catches multi-altitude duplicates only if the scan runs across the full set.

## Failure modes characterized (so far)

Six distinct relay-shape failure modes have surfaced in pilots #1–#13:

1. **Vocabulary re-skin** (pilot #1) — same structure, new costume. Different abstract type, same lattice.
2. **Multi-altitude bundle** (pilot #2) — one proposed primitive absorbs multiple existing atoms across altitudes.
3. **Lexical fracture** (pilots #3, #6, #7, #11, #13, #15 — **standing**, 6 specimens; first external recurrence in #15 Claims B + C) — one word carries multiple distinct relations; relay collapses them.
4. **Preventive gate** (pilots #8, #12) — corpus already contains the disambiguation that blocks the collapse; gate fires before the relay-shaped claim lands.
5. **Gap-shape laundering** (pilot #9) — real gap exists; relay tries to fill it with the wrong frame.
6. **Internal-refutation gap** (pilots #10, #12, #13, #15 — **standing**, 4 specimens; first external recurrence in #15 Claims B + E) — real gap exists; the corpus's *own* substrate work has done the federation-doctrine refusal of the tempting unifier internally; audit records that refusal. **Promoted 2026-06-06 from candidate pattern to standing verdict class** after Pilot #13 produced the third specimen. **External recurrence in Pilot #15** is stronger evidence the mode is substrate-portable, not cave-local.

This list is open. New failure modes earn their entry when they recur or when a single pilot surfaces something the existing six cannot describe. **Standing** marker (modes #3 and #6 as of 2026-06-06) signals the instrument can reliably *predict* the mode rather than merely catch it; the corpus's federation-doctrine refusal habit and lexical-fracture surface area are stable enough to be method-catalogue entries, not one-off categories.

## Promotion rule

> **Single-altitude novelty is inadmissible for promotion.** A claim that survives audit at only one altitude is at best a candidate; promotion requires multi-altitude survival, citations, and a forcing case the corpus actually carries.

The rule applies regardless of how compelling the single-altitude finding looks. The instrument's whole purpose is to refuse fake novelty.

Promotion-eligible findings (when they happen):

- new theorem: only if **MISSING-PRECONDITION** or **COUNTEREXAMPLE-CANDIDATE** with exact file names AND explicit forcing case;
- new cross-reference: navigability patches authorized per-pilot, with wording that *does not perform doctrine motion*;
- new disambiguation note: ALIAS-RISK or lexical-fracture survivors may earn a glossary entry under `working/vocabulary/`, *if* the user authorizes — never auto-promoted.

Promotion paths that should be refused or routed elsewhere:

- new paper section — vector-mining pilots do not authorize paper motion; that requires a separate authorization pass against PAPER-MAP / CLAIM-REGISTER / current paper spine;
- new Lean module — vector-mining pilots do not authorize Lean motion unless the verdict is MISSING-PRECONDITION or COUNTEREXAMPLE-CANDIDATE AND the corpus carries a concrete forcing case;
- new primitive — vector-mining pilots never authorize primitive promotion. Promotion of a primitive is a doctrine decision with its own gate.

## Batch footer (mandatory)

Every pilot or batch report ends with:

> **PROMOTE NOTHING. PATCH QUEUE ONLY. NEXT HIGH-RISK TARGETS NAMED.**

The footer is not optional. It is the reminder that vector mining is prospecting, not coronation.

## When a result may become a forcing case

A vector-mining result may *eventually* become a forcing case for promotion when:

1. The verdict is MISSING-PRECONDITION, COUNTEREXAMPLE-CANDIDATE, or BRIDGE-CANDIDATE — i.e., not a duplicate or laundering refusal;
2. AND the surviving claim is cross-validated by a second pilot from a *different altitude or angle*;
3. AND a downstream consumer (paper section, Lean theorem, public claim) genuinely needs the move — speculative expansion is still YAGNI;
4. AND the move passes the federation-doctrine bridge tax;
5. AND the user explicitly authorizes via the normal ratification path.

All five must hold. The vector-mining receipt is one piece of evidence among the five — never the ratifying step.

## Readiness-audit pattern (Track A, complementary)

A complementary pilot pattern surfaced 2026-06-06 in Pilot #14: instead of probing a relay-shape claim, the audit targets a *named-not-built artifact in the corpus* (e.g., a future Lean candidate, a named-but-deferred kernel, a candidate primitive that has been carried across multiple pilots without being built) and asks:

> *Does the corpus now have a forcing case for this artifact, or is the current material still only prose-altitude positioning?*

Verdicts use the standard palette, with **NOT_READY** and **FORCING_CASE_CANDIDATE** as the most-likely outcomes. Output is a receipt that includes a *forcing-case predicate* — the conjunction of conditions that would tip the verdict on future re-check — so subsequent audits do not have to re-derive the criteria.

Pilot #14 (NoSilentException.lean) is the first instance: NOT_READY; five-part forcing-case predicate recorded in [`2026-06-06-nosilentexception-readiness-audit.md`](2026-06-06-nosilentexception-readiness-audit.md) § "What 'would tip' the verdict".

**Status:** candidate pattern, not promoted. Earns its own method-note section if it recurs; recurrence threshold matches the standing-mode threshold for failure modes (three specimens).

## External portability pilot pattern (Track C, complementary)

A complementary pilot pattern surfaced 2026-06-06 in Pilot #15: instead of probing the papers/Lean corpus, the audit runs on a *real external soft corpus* (foreign institutional substrate, no formal proof layer) with five-or-so plausible novelty/unification claims constructed against a frozen manifest. The audit question is whether the method retains discrimination outside its native habitat.

Hard discipline:

- **Freeze the corpus manifest BEFORE generating claims.** This is the single most load-bearing piece of methodology. Without it, the audit unconsciously picks claims that make the method look good — *little prosecutor selecting its own crime scene.*
- **Existing verdict labels only.** If they fail, record why; do not silently extend the method.
- **No comparison with internal pilots until at least two external pilots exist** (per serial-pilot discipline). Avoids the escape hatch "method worked / failed because corpus selection was weird."
- **Mark explicitly:** where operator judgment substitutes for mechanical refusal; where a mechanical altitude would have helped; where verdict stability under deeper reading was a real failure mode of the instrument.

Pilot #15 (PEP 634 family) is the first instance: **RETAINS DISCRIMINATION** with named caveats; existing labels sufficient; Mode #3 and Mode #6 fired externally; LAUNDERING-as-verdict surfaced where internally suppressed by federation doctrine; one verdict was revised on re-read.

**Status:** candidate pattern, *not* promoted. Method is *not* proven portable on a single external corpus. Deep comparison with internal pilots is *deferred* until at least Pilot C2 (Rust RFC or Kubernetes KEP) provides serial replication. Earns its own method-note section and a stronger portability claim *only* if C2 also retains discrimination. If C2 collapses or degrades, the cave-vs-PEP convergence is partly coincidence and the method has a substrate dependency the instrument did not anticipate.

## Anti-patterns

What vector mining is **not**:

- **Not a relay-judge.** It does not adjudicate external claims by accepting them; it tests against the corpus.
- **Not a synthesis engine.** It refuses synthesis; the federation doctrine is the architecture.
- **Not a paper draft.** Pilot reports are receipts, not paper drafts.
- **Not a Lean spike authorizer.** Lean work is gated separately, by forcing cases and the bridge tax.
- **Not a doctrine generator.** Doctrine motion has its own ratification path.
- **Not exhaustive.** A pilot covers one or a few attacks; it does not claim the corpus is fully audited.

## Operational discipline (lessons from pilots #1–#10)

- **Run small first.** Single-attack pilots earn the method; batch pilots scale once polarity is confirmed.
- **Parallelize corpus reads.** Most pilots need 5–10 file reads; batch them at the start.
- **Cite every cell.** Every verdict cell in a comparison table must point at a corpus location. "I sense convergence" is the warning sign that the instrument has failed.
- **Refuse the synthesis goblin.** Even when a finding looks promotable, the right move is to file it as a candidate and wait for a forcing case from a *different* angle.
- **Cross-altitude before publication.** A finding that looks novel at altitude *n* almost certainly has a sibling at altitude *m*; check before reporting.
- **Common-mode immunity:** when the proposing voice is Claude-family, the corpus check must come from a non-Claude reference (the corpus itself, in this case). Pilot receipts are written against the corpus, never against the relay.

## Patch queue rules

When a pilot produces a survivor (a navigability patch, glossary entry, or cross-reference), it joins the patch queue. Rules:

- Each item is one mechanical operation: cross-reference, glossary entry, navigation breadcrumb.
- No item performs doctrine motion.
- No item is authorized without explicit user signal.
- Wording is reviewed for reframe-avoidance language ("filed as candidate, NOT ratified" / "this note does not ratify that reframe").
- Patch-queue items expire if not landed within ~1 week of pilot — staleness is treated as deauthorization.

## Cumulative pilots (as of 2026-06-06)

| # | Pilot | Verdict | Survivors |
|---|---|---|---|
| 1 | Attack #5 (solo): effect vs obligation | DUPLICATE + ALIAS-RISK + LAUNDERING | 2 prose-altitude |
| 2 | Attack #2 (solo): boundary × feedback | DUPLICATE×3 + LAUNDERING | cross-ref patch + future-Lean vocab |
| 3 | Attack #4 (solo): freshness × standing | ALIAS-RISK dominant | standing-three-senses glossary + cross-ref patch |
| 4 | Attack #1 (batch): Mandamus × refusal | DUPLICATE (literal) | none |
| 5 | Attack #2 (batch): Exception × anti-precedent | DUPLICATE on doctrine + UNRATIFIED-CANDIDATE | vocab carry; separation-of-custody patch held |
| 6 | Attack #3 (batch): witness × receipt | ALIAS-RISK | receipt-and-witness-senses glossary |
| 7 | Attack #4 (batch): custody × provenance | ALIAS-RISK (5 senses) | custody-five-senses glossary + cross-ref patches |
| 8 | Attack #5 (batch): authority × authorization | ALIAS-RISK + DUPLICATE on disambiguation | none |
| 9 | Attack #6 (batch): sacrifice floor × Mist | GAP CONFIRMED + RELAY-FRAMING REFUSED | none |
| 10 | Composition substrate × LGVG | INTERNAL-REFUTATION GAP | LGVG ↔ axis-2 / decay-family cross-refs |
| 11 | Heterogeneous-turtles × independent-custody | DUPLICATE on structural claim + minor ALIAS-RISK on "type" | receipt-and-witness-senses transversal-meta-axis + cross-ref to heterogeneous-turtles |
| 12 | WCM × Cedar Analysis differential | PREVENTIVE GATE + ALIAS-RISK + INTERNAL-REFUTATION GAP | differential-testing-two-senses glossary + WCM ↔ pre-auth-layer bidirectional cross-ref |
| 13 | NI × sacrifice-class (containment) | INTERNAL-REFUTATION GAP + ALIAS-RISK | NI ↔ AAG navigability cross-ref; sacrifice glossary HELD by deliberate refusal |
| 14 | NoSilentException readiness audit (Track A) | NOT_READY (named lacuna persists; no specimen forces the discriminator) | none — readiness predicate recorded in receipt; lattice line 148 forward-pointer patch held by recommendation |
| 15 | Track C portability pilot #1: PEP 634 family (external soft corpus) | RETAINS DISCRIMINATION on external substrate with named caveats | none — method-validation only; external corpus archived at `~/git/track-c-pep634/sources/`; comparison with internal pilots deferred to post-C2 |

Patch queue empty as of 2026-06-06. Held-by-deliberate-refusal: `sacrifice-three-senses.md` (relay-introduced sense (c) does not get a glossary cell); bridge-obligation-lattice line 148 forward-pointer (Pilot #14; lattice is currently clean, holding maintains).

## Cross-references

- [`2026-06-05-attack-05-effect-vs-obligation.md`](2026-06-05-attack-05-effect-vs-obligation.md), [`2026-06-05-attack-02-boundary-feedback.md`](2026-06-05-attack-02-boundary-feedback.md), [`2026-06-05-attack-04-freshness-vs-standing.md`](2026-06-05-attack-04-freshness-vs-standing.md) — solo pilots #1–#3.
- [`2026-06-05-batch-six-attacks.md`](2026-06-05-batch-six-attacks.md) — mixed batch pilots #4–#9.
- [`2026-06-05-composition-substrate-vs-lgvg.md`](2026-06-05-composition-substrate-vs-lgvg.md) — single-target pilot #10.
- [`../vocabulary/`](../vocabulary/) — disambiguation glossaries (`standing-three-senses.md`, `custody-five-senses.md`, `receipt-and-witness-senses.md`).
- [[project-no-unifier-without-laundering]] — federation discipline.
- [[feedback-claude-common-mode-synthesis]] — methodology check that this procedure operationalizes.
- [[feedback-verdict-compression]] — the freshness-on-relays principle this procedure depends on.

## Provenance

Method emerged in pilots #1–#10 (all 2026-06-05). Surfaced as method-shape during pilot #3 ("the method is starting to scale. Carefully. With gloves."); ratified as workflow-hygiene rule during the batch pilots; filed as a standing method note here on 2026-06-05.

Not folklore. Not doctrine. Operating procedure.
