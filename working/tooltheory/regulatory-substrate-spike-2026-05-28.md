# Regulatory / legal substrate — forbidden-inference spike (first-pass solo)

**Status:** First-pass solo survey + triage. **Not** ratified onto the canonical register. Awaits multi-model triangulation (ChatGPT survey extension + DeepSeek sanity check + operator routing) before any C-bucket candidate is promoted to register row or sketch pack entry.

**Filed:** 2026-05-28. Second slice under [[prior-art-spike-plan]] following [[internet-substrate-failure-map]] / [[forbidden-inference-register]] / [[annex-sketch-pack]] (internet substrate slice, 2026-05-26).

**Slice rationale:** Regulatory / adversarial-procedural substrate is maximally distant from internet substrate (different failure topology) and from in-flight NS-NQ work (different vocabulary). "Admissibility" is literally a term of art in evidence law — this slice tests whether the corpus framing has converged independently with centuries of doctrinal substrate.

**Methodology caveat:** Solo survey by a language model with broad-but-shallow legal knowledge. Likely hits classical doctrine cleanly; likely misses niche / circuit-specific / specialized doctrine. ChatGPT extension should specifically probe administrative law, securities law, IP-specific doctrine, and international arbitration — those are weak in this pass.

**Doctrine header (inherited from canonical register):**

> **Formalize only where a substrate blocks a distinct forbidden inference your current corpus does not already block.**

---

## The slice register

Format mirrors [[forbidden-inference-register]]. Triage buckets: **A** (already covered) / **B** (adjacent extension) / **C** (new structural axis) / **D** (glossary / explicit rejection) / **E** (forcing-case revisit).

| # | Forbidden inference | Substrate specimen | Existing primitive overlap | Residue | Bucket |
|---|---|---|---|---|---|
| R1 | *Past wrong is presently actionable* — "harm occurred, therefore claim lives" | Statute of limitations; statutes of repose; laches | freshness + transition authority + FencedEpochAuthority sketch | Time-bar as license-expiry; confirms FencedEpochAuthority's temporal axis under legal vocabulary | **A** (covered; confirmation evidence) |
| R2 | *Anyone may sue* — "I care about this, therefore I have a claim" | Article III standing (injury-in-fact, causation, redressability); prudential standing; third-party standing limits | standing (literal corpus primitive) | None novel; legal substrate is the source of the corpus's "standing" vocabulary | **A** (refines existing kernel) |
| R3 | *Case still live because once filed* — "the docket exists, therefore the controversy lives" | Mootness (case-or-controversy); ripeness; capable-of-repetition-yet-evading-review exception | freshness + standing + transition | Temporal standing decay; covered by composition of freshness + standing | **B** (Freshness/standing composition) |
| R4 | *Forum chose to hear, therefore forum is competent* — "the court took the case, so it had jurisdiction" | Personal jurisdiction (minimum contacts, Int'l Shoe); subject-matter jurisdiction; forum non conveniens; sua sponte SMJ dismissal | authority + scope | Jurisdictional authority is bounded by external substrate facts not by court's self-assertion; covered by scope-bound authority | **B** (authority + scope composition) |
| R5 | *Absence of evidence proves absence of fact* — "they didn't produce it, so it doesn't exist" — **with spoliation twist:** when party had preservation duty, absence yields adverse inference, not neutral silence | FRCP 37(e) adverse-inference instructions; spoliation sanctions; duty to preserve under reasonable anticipation of litigation | silence + witness + duty-to-preserve | **Asymmetric silence:** duty-bound absence ≠ neutral absence. Covered by AuthenticatedDenial sketch's duty axis, but the *adverse inference* flip (silence becomes evidence *against*) is sharper than the corpus carves today. | **B** or **C** (sharpening of AuthenticatedDenial: duty-bound silence yields admissible inverse witness) |
| R6 | *Out-of-court statement admissible for its truth* — "she said it, therefore we can use it to prove what she said" | Federal Rules of Evidence 802 (hearsay default exclusion) + ~20 named exceptions (present-sense impression, excited utterance, business records, statement against interest, dying declaration, etc.) | witness + authority + cross-examination | **Purpose-bound admission:** a statement may be admitted for some uses but not others (e.g., to show notice but not to show truth). This is *Refusal Narrowing at the evidence layer* — distinct from the corpus's existing action-kind narrowing. | **C candidate — purpose-bound admission** |
| R7 | *Evidence admissible for use X is admissible for use Y* — "we let the document in, so it's in for everything" | FRE 105 (limiting instructions); FRE 404(b) (prior bad acts admissible for purpose-but-not-propensity); privilege exceptions that turn on use | refusal narrowing (existing) | Same shape as R6; both are evidence-layer narrowing | **C candidate — same as R6** |
| R8 | *Communication's factual content makes it admissible* — "it's true, so we can use it" | Attorney-client privilege; doctor-patient; spousal; work-product doctrine; clergy-penitent; psychotherapist-patient | scope + authority + custody | **Use-bound inadmissibility despite factual veridicality.** Privileged communication is factually true and not contested; it is inadmissible for *relational-channel* reasons. Distinct shape from R6/R7 — those carve admission scope; this carves communication channels exempt from any litigative use. | **C candidate — relational-channel exemption** |
| R9 | *Previously adjudicated claim still litigable* — "I'm bringing it again, this time it'll go differently" | Res judicata (claim preclusion); collateral estoppel (issue preclusion); finality requirement; full faith and credit | settlement + consolidation + authority | **Finality as preclusive authority within scope.** ConsolidationDenial says fluency doesn't settle. Res judicata says *actual adjudication does settle*, and the settlement-receipt has specific shape (court of competent jurisdiction, on the merits, between same parties). Positive sibling to ConsolidationDenial. | **C candidate — settlement-receipt has structure** |
| R10 | *Forum's substantive law governs* — "they filed here, so we apply our law" | Choice of law / conflict of laws; Erie doctrine (federal courts applying state substantive law); Restatement (Second) Conflict of Laws | authority + scope + transition + FencedEpochAuthority sketch | **Cross-jurisdictional substantive authority.** Procedural authority (forum competence) is distinct from substantive authority (which body of law governs). Confirms the two-axis caveat already named in FencedEpochAuthority sketch (propagation scope ≠ epoch fencing). | **B** (already noted in sketch); reinforces the split-pressure |
| R11 | *Evidence integrity assumed* — "we have the document, therefore it's authentic" | Chain of custody; FRE 901 (authentication); chain of evidence in criminal cases | provenance + custody (literal corpus vocabulary) | None novel; legal substrate is the source of the corpus's "custody" vocabulary | **A** (refines existing) |
| R12 | *Uncontested = true* — "no one objected, so it's settled" | Default judgment limits; due process notice + opportunity to be heard; required adversarial testing | adversarial-system structure + settlement | Covered by consolidation-denial under different vocabulary; "decision by default" is not "decision on the merits" | **B** (sibling to ConsolidationDenial) |
| R13 | *Uninformed party bound by action* — "we acted, you didn't know" | Service of process; notice provisions in statutes; constructive notice doctrines; mailbox rule | witness + freshness + reachability | Covered by witness reachability composition; "constructive notice" is a fiction that admits the gap | **B** |
| R14 | *Regulator's interpretation binds courts* — "agency said it, therefore it's law" | Chevron deference (pre-Loper Bright 2024); Skidmore deference; agency interpretive authority limits | authority + scope + non-reciprocal admissibility flow | **Scope-bound interpretive authority** is interesting but largely covered by NRAF composition. Post-Loper Bright (2024 SCOTUS), Chevron is overruled; interesting historical specimen of *interpretive authority laundering* under deference framework. | **B** (NRAF composition + historical specimen) |
| R15 | *Reasonable person standard applies uniformly* — "the law says reasonable, we'll figure out what that means" | Negligence (duty/breach/causation/damages); reasonable person construct; community standards; Hand formula (B<PL) | authority + scope + (interesting partial coverage) | The "reasonable person" is a *construct that allows scope-blind aggregation*. Connects to mean-aggregation masking (Paper 24). Probably out of slice scope but worth flagging | **D** (out of slice scope; flag for Paper 24 author) |
| R16 | *State can be sued without consent* — "I have a cause of action, therefore the state will answer" | Sovereign immunity (federal + state); Eleventh Amendment; Federal Tort Claims Act waivers; Ex parte Young exception | authority + standing + non-reciprocal admissibility flow | NRAF instance — state shapes what counts for plaintiffs while denying reciprocal accountability | **A** (covered; refines NRAF) |
| R17 | *Act alone constitutes crime* — "the act happened, the crime is proven" | Mens rea (criminal intent); affirmative defenses; specific vs. general intent | (none — quality of authority, not existence) | Too narrow for the framework; criminal-law specific | **D** (out of scope) |
| R18 | *Settlement bars all related claims forever* — "we settled, you can never raise anything connected" | Release language scope; carve-outs; doctrine of merger; specific-vs-general release | settlement + scope | **Settlement-receipt scope.** Sibling to R9 — settlement has both *preclusive effect* (R9) and *scope boundaries* (R18). Together: settlement-receipt structure has finality axis + scope axis. | **C candidate — settlement-receipt scope** (composes with R9) |
| R19 | *Procedural compliance equals substantive validity* — "we followed the procedure, therefore the outcome is just" | Procedural due process (notice + hearing) does NOT guarantee substantive correctness; "just enough process" is not "right outcome" | adversarial-system + authority | Connects to existing materialism / control / admissibility triad — procedure as substrate for control but not for correctness | **B** (composition of procedural and substantive admissibility) |
| R20 | *Old precedent still controls* — "the case from 1923 is on point, therefore it governs" | Stare decisis; overruling sub silentio; intervening statutory/constitutional change; super-precedent debate | freshness + authority + transition | **Precedent as freshness-bounded authority.** Stare decisis IS authority; it is also temporally degradable through overruling, distinguishing, and statutory supersession. Sibling to R14 (interpretive authority) but in common-law substrate. | **B** (freshness + authority composition over precedential substrate) |

---

## C-bucket candidates (awaiting triangulation)

Three structural axes surfaced this slice that the corpus does not already block:

### C1 — Purpose-bound admission (R6 + R7)
> *Evidence admitted for use X is not thereby admitted for use Y.*

**Substrate convergence:** FRE 802/803/804 exception system + FRE 105 limiting instructions + FRE 404(b) propensity rule.

**Distinction from existing corpus Narrowing:** The existing `Composition.Narrowing` in `RefusalPropagation.lean` concerns *action-kind* narrowing (binding use refused but advisory use permitted). Purpose-bound admission is *evidentiary-use* narrowing — the same artifact is admissible for purpose X (e.g., to show notice) and inadmissible for purpose Y (e.g., to prove truth of the matter asserted).

**Sketch candidate:** `PurposeBoundAdmission` — given evidence E, admissible-purpose set P, and use U, E witnesses U iff U ∈ P. Refusal kernel: admission for *some* purpose does not authorize use for *any* purpose.

**Existing-corpus risk:** May reduce to action-kind narrowing under a richer action-kind ontology. Triangulation should test whether evidence-purpose narrowing is truly orthogonal or just a vocabulary refinement.

### C2 — Settlement-receipt structure (R9 + R18)
> *Settlement is not a single binary event — it has both a finality axis (what claims are precluded) and a scope axis (which subject-matter is covered).*

**Substrate convergence:** Res judicata + collateral estoppel + claim/issue distinction + release scope law + merger doctrine.

**Distinction from existing ConsolidationDenial:** ConsolidationDenial is *one-way negative* — fluency does not constitute settlement. Settlement-receipt structure is *positive sibling* — when settlement DOES occur (via adjudication, release, or admission), it has formal shape: which claims, between which parties, with what preclusive effect, over what scope.

**Sketch candidate:** `SettlementReceiptStructure` — a settlement-receipt carries (parties P, claim-scope S, finality-mode F). Future admissibility of claim C between parties Q is blocked iff Q ⊆ P ∧ C ∈ S ∧ F = on-merits. Refusal kernel: claim-substance overlap does not by itself imply preclusion; specific structure must match.

**Forcing-case watch:** consumer-side incidents where settlement language is overread (releases interpreted to bar unrelated claims) or underread (settled claim re-litigated under different label).

### C3 — Relational-channel exemption (R8)
> *Some communications are factually true and topically relevant but inadmissible because of the relational channel they were carried on.*

**Substrate convergence:** Privilege law (attorney-client, doctor-patient, clergy, spousal, psychotherapist, work-product).

**Distinction from existing corpus:** Existing primitives handle scope-bound authority, custody, witness narrowing. Privilege is none of those — it is *channel-bound exemption from any litigative use* on policy grounds. The factual content is admissible elsewhere (the same conversation about the same facts with a non-privileged party would be admissible); the *relational channel* triggers exemption.

**Sketch candidate:** `RelationalChannelExemption` — communication C carried on relational channel R is exempt from litigative use iff R is privileged, independent of C's factual content or relevance.

**Distinguishing test:** does the corpus already have a primitive that says "this artifact can witness X in one channel but cannot witness X in another channel"? If yes, C3 reduces to that. If no, C3 names a genuinely new axis: *channel-conditioned admissibility*.

---

## A/B confirmations

The following register entries confirmed existing corpus primitives under regulatory vocabulary. **Useful evidence**, not new structure:

- R1 (statute of limitations) → confirms FencedEpochAuthority sketch's temporal axis
- R2 (standing) → confirms corpus's existing standing primitive (legal substrate is source)
- R3 (mootness/ripeness) → freshness + standing composition
- R4 (jurisdiction) → authority + scope
- R10 (choice of law) → confirms FencedEpochAuthority two-axis caveat from internet substrate
- R11 (chain of custody) → literal source of corpus's "custody" vocabulary
- R13 (notice) → witness + freshness + reachability composition
- R14 (Chevron) → NRAF composition; historical specimen now overruled
- R16 (sovereign immunity) → NRAF instance
- R19 (procedural ≠ substantive validity) → composition of procedural + substantive admissibility
- R20 (stare decisis) → freshness + authority composition over precedential substrate

R5 (spoliation / adverse inference) is borderline B/C. The *adverse inference flip* — duty-bound silence becomes admissible inverse witness — is a sharpening the corpus does not currently express. If triangulation surfaces additional substrates where duty-bound silence flips polarity (regulatory non-response with statutory consequence; required reporting failures), promote to C.

## D-bucket / out of scope

- R15 (reasonable person standard) — connects to mean-aggregation masking from Paper 24 but is too criminal/tort-specific to lift. Flag for Paper 24 author as substrate confirmation.
- R17 (mens rea) — too narrow.

## E-bucket

None this slice. The internet-substrate register's E-bucket entry (R10: linearizable vs serializable reads) remains the only conditional Public Phase D revisit trigger.

---

## Bucket distribution

Of 20 slice entries:

- **A (already covered):** 5 entries (R2, R11, plus implicit refinements at R1, R10, R16)
- **B (adjacent extension):** 11 entries (R1, R3, R4, R5-borderline, R10, R12, R13, R14, R16, R19, R20)
- **C (new structural axis):** 3 candidates (C1 from R6+R7, C2 from R9+R18, C3 from R8) covering 5 entries
- **D (out of scope):** 2 entries (R15, R17)
- **E (forcing-case revisit):** 0 entries

Roughly 25% A / 55% B / 15% C / 10% D / 0% E.

**Comparison to internet-substrate slice (27/27/27/13/6):** lower C-count and higher B-count is expected. Regulatory substrate has been adjacent to admissibility framing for centuries; convergence is high. The framework is doing more *confirmation work* and less *axis-naming work* in this slice. **That is healthy** — it indicates the framework is mature in the adjacent domain, not under-developed.

The three C candidates (purpose-bound admission, settlement-receipt structure, relational-channel exemption) are the slice's primary contribution to attention. None are forcing-case-ready; all need triangulation before promotion.

---

## Doctrine keepers (candidates; survive triangulation if landed)

> *Admissibility law was the corpus's nominal sibling all along. Confirmation is rich; new structure is sparse.*

> *Purpose carves admission. Channel carves exemption. Settlement carves preclusion.* (The three C candidates, compressed.)

> *Procedural compliance is not substantive correctness.* (R19 — already implicit in materialism/control/admissibility triad.)

> *Duty-bound silence flips polarity. Neutral silence stays neutral.* (R5 — sharpening of AuthenticatedDenial.)

---

## What triangulation should specifically probe

- **C1 (purpose-bound admission)** — does the FRE 105 + 404(b) shape reduce to action-kind narrowing under a richer action-kind ontology, or is evidence-purpose orthogonal? ChatGPT/DeepSeek prompt: *"Is purpose-bound admission a special case of capability narrowing, or a distinct axis?"*
- **C2 (settlement-receipt structure)** — does the finality-axis × scope-axis decomposition hold across non-litigative settlement substrates (regulatory consent decrees, arbitration awards, mediation agreements, plea bargains)? ChatGPT prompt: *"Does settlement-receipt structure carve uniformly across adjudicative, administrative, and contractual settlement?"*
- **C3 (relational-channel exemption)** — does privilege reduce to an extreme case of scope-bound authority, or is the channel-conditioning genuinely orthogonal? DeepSeek prompt: *"Is privilege a kind of scope, a kind of standing, or a third thing?"*
- **R5 borderline (adverse inference)** — does duty-bound silence flip polarity in non-litigative substrates? Prompt: *"In what non-litigation settings does required silence become admissible inverse witness?"*

## What weak coverage this pass admits

Solo survey is weak on:
- **Administrative law specifics** beyond Chevron/Loper Bright (formal vs informal rulemaking, APA procedural requirements, hard-look review, arbitrary-and-capricious standard).
- **Securities law** (materiality standards, scienter, reliance, fraud-on-the-market).
- **IP-specific doctrine** (claim construction, doctrine of equivalents, prior-art bars, on-sale bar).
- **International arbitration** (New York Convention, public-policy exceptions, manifest disregard).
- **Specific privilege exceptions** (crime-fraud exception; in-house counsel limits; common-interest privilege; joint defense).

These are the ChatGPT-extension priority areas.

---

## Cross-references

- [[prior-art-spike-plan]] — parent plan; this is the second slice output.
- [[forbidden-inference-register]] — canonical register; slice output not yet ratified into it.
- [[annex-sketch-pack]] — sketch pack; C1/C2/C3 are sketch-pack candidates pending triangulation.
- [[internet-substrate-failure-map]] — first slice; FencedEpochAuthority sketch's two-axis caveat is reinforced by R10.
- [[cross-kernel-disposition]] — Path C bracketing applies the same way here (no cross-kernel jurisdictional merge).

## Provenance

- 2026-05-28. Solo first-pass slice on regulatory / adversarial-procedural substrate. No multi-model triangulation yet. Operator authorized "next prior-art spike slice"; regulatory chosen on grounds of (a) maximal distance from in-flight NS-NQ work, (b) maximal distance from internet substrate slice, (c) nominal sibling status (admissibility is a legal term of art).
- Slice produced 20 register entries, 3 C candidates, 11 A/B confirmations, 2 D rejections.
- ChatGPT extension + DeepSeek sanity check are the next routing step before any C candidate moves to canonical register or sketch pack.

> *Regulatory substrate is the corpus's nominal sibling. Confirmation is dense; new structure is sparse but sharp.*
