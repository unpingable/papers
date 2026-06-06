# Vector-Mining Batch — Mixed Six-Pack

**Filed:** 2026-06-05. **Status:** vector-mining batch output. **Batch rules applied:** max 8 attacks (6 actual); no new Lean modules (none warranted); no doctrine edits; survivors are patch-queue only; every verdict cites; every "novel" claim multi-altitude scanned. **Cumulative pilot count:** 9 (three solo + six batch).

## Rollup table

| # | Attack | Verdict | Failure mode | Survivor | Recommended action |
|---|---|---|---|---|---|
| 1 | Mandamus × refusal-as-effect | **DUPLICATE (literal)** | doctrine just-shipped | none — corpus equal-or-stronger | none |
| 2 | Exception × anti-precedent | **DUPLICATE on doctrine + UNRATIFIED-CANDIDATE on Lean** | bridge-obligation-lattice already names it | already-deferred Lean spike + relay's separation-of-custody as vocab candidate | defer; carry vocab for future spike |
| 3 | Witness × receipt | **ALIAS-RISK** | "receipt" carries ≥3 senses; "witness" ≥3 senses; relay assumes one | disambiguation entry in standing-three-senses or sibling glossary | optional glossary extension |
| 4 | Custody × provenance | **ALIAS-RISK (high)** | "custody" carries ≥4 senses across the recently-shipped custody discipline + substrate-binding + loop-capture + memory candidate | disambiguation entry; one cross-ref patch | optional glossary + 5-min cross-ref |
| 5 | Authority × authorization | **ALIAS-RISK + DUPLICATE on the distinction itself** | pre-authorization-layer note explicitly disambiguates; relay collapses | none — the corpus's positioning note IS the disambiguation | none |
| 6 | Sacrifice floor × Mist/composition | **GAP CONFIRMED + relay-framing REFUSED** | corpus has LGVG candidate as composition-axis primitive (not Lean-built); relay's sacrifice-floor framing is laundering on top of the legitimate gap | none — gap is named, relay's filling refused | leave LGVG candidate undisturbed |

---

## Attack 1 — Mandamus × refusal-as-effect

**Question:** Does the corpus already treat refusal as an effect with its own discharge discipline?

**Sources:** `LeanProofs/Admissibility/Mandamus.lean` (UNRATIFIED-CANDIDATE, built green 2026-06-06, three sprint-#1 theorems); `working/refusals-need-receipts.md`; `working/mandamus-liveness-dual.md`; [[project-refusals-need-receipts]].

**Direct hit.** Mandamus.lean encodes refusal-as-effect literally:
- `DeemedRefusal m h currentTime := ¬ Decided m ∧ h.deadline < currentTime` — non-decision past horizon IS refusal.
- `Owes` is the obligation-effect; `Violation` produces an `EvidentiaryRecord` — *record, not compulsion.*
- `theorem nondecision_past_horizon_implies_deemed_refusal` — the corpus's literal NoBurdenLaundering theorem at the temporal axis.
- Eight dual-list refusals enumerated in the doctrine note, including "refusal without reachable cure is discretion."

The relay's `RefusalEffect` + `MayRefuse with burden β` + `CurePath reachable-by β.class` is Mandamus.lean's `Owes` + `BlockingPredicate` + `Reachable` (with claimant-capability indexing per correction #2). Same content, one day apart, corpus shipped first.

**Verdict:** DUPLICATE (literal). The corpus is strictly stronger: it has admin-law mapping, eight dual-list refusals, ministerial/discretionary type-level split, and a recursive scar (the first Mandamus draft caught its own author's unbound-receipt bug). No survivor; no action.

---

## Attack 2 — Exception × anti-precedent

**Question:** Is anti-precedent already the load-bearing distinction for Exception, or does the relay's "ExceptionDebt / non-self-discharge / precedent-barred" propose something new?

**Sources:** `working/bridge-obligation-lattice.md` (in context); [[project-bridge-obligation-lattice]].

**Already named.** The lattice's NoSilentConversion gate (worked 2026-06-06) explicitly:

> **Exception ≠ Deformation: FAILS.** A deformation changes the surface; an exception leaves the rule intact and bypasses it for a bounded window. Its defining invariant is the one Deformation structurally cannot have: **anti-precedent** — the bypass must not become precedent. An exception that changes future meaning is an illegal deformation with a siren taped to it.

Exception's obligation set: `{temporal-bounding, anti-precedent}`. The relay's "precedent_barred / escalation_barred / debt cannot discharge itself" lands as `anti-precedent` + a separation-of-custody refinement.

`NoSilentException` is listed in the lattice as a future Lean candidate (alongside `NoSilentDelegation`, `NoSilentProjection`) — *"named, not built."* Same status as attack-05's "separation-of-custody on exception discharge" survivor.

**Verdict:** DUPLICATE on the obligation-set classification + UNRATIFIED-CANDIDATE on the Lean spike. The relay's `ExceptionDebt` structure could inform field names *if* and *when* `NoSilentException.lean` earns a forcing case. Not authorized to build. Carry as a vocabulary candidate, same as attack-05's Survivor 2.

**Survivor:** the separation-of-custody refinement of anti-precedent (already on the candidate queue from attack-05); no new action this pilot.

---

## Attack 3 — Witness × receipt

**Question:** Do "witness" and "receipt" denote distinct, jointly-spanning relations in the corpus, or are they used interchangeably in places?

**Sources:** `working/bridge-obligation-lattice.md` (in context); `working/tooltheory/witness-carrier-model-candidate-2026-06-06.md` (in context); `LeanProofs/Admissibility/Mandamus.lean` (just read); `LeanProofs/Admissibility/BoundaryWitness.lean` (in context).

**Lexical fracture, second instance.** Both words carry multiple roles:

| Word | Sense | Where |
|---|---|---|
| Receipt | (a) submission record (timestamped artifact) | `Mandamus.Receipt.submittedAt` |
| Receipt | (b) refusal/reasoned-decision verdict artifact | Mandamus refusals-need-receipts doctrine |
| Receipt | (c) acknowledgment whose mere existence does not authorize | `ReceiptIsNotAuthority` static refusal kernel |
| Witness | (a) Lean proof object (dependent type inhabitant) | `BoundaryWitness.lean`'s forgetful-map / `CouplingWitness` / `BridgeWitness` |
| Witness | (b) substrate carrier (signed JSON, ledger entry) | witness-carrier-model § Non-claim |
| Witness | (c) testimonial admissibility object | refusals-need-receipts; mandamus's "evidentiary record"; loop-capture's "fail differently" |

The receipt/witness distinction is structurally maintained where it matters: a witness *supports* an admissibility claim; a receipt *records* an act (submission, refusal, debt). But the words alias enough across registers that single-altitude review can confuse them.

The receipt-vs-witness boundary is closest to load-bearing in: `ReceiptIsNotAuthority` (receipt of a transaction ≠ authorization to perform it) and witness-carrier-model § 3 ("Label is not witness" — the field name is the label, the binding obligation is the witness). These two sentences carry the genus boundary.

**Verdict:** ALIAS-RISK. Survivor candidate: a follow-on glossary entry analogous to standing-three-senses, mapping receipt and witness senses to corpus locations. Smaller than standing-three-senses (the role boundary is sharper); could be ~1-section glossary append rather than a new file.

**Survivor:** add a "receipt / witness" disambiguation section to `working/vocabulary/` — either extend the standing-three-senses file or sibling file. Not authorized without user signal.

---

## Attack 4 — Custody × provenance

**Question:** Does "custody" name one or many relations in the corpus, and how does it relate to "provenance"?

**Sources:** [[project-lean-custody-state]]; `working/custody-classes.md` (recently shipped); `working/tooltheory/witness-carrier-model-candidate-2026-06-06.md` (binding obligations); `working/loop-capture.md` (independent custody); [[project-custodian-binding-accountability-candidate]].

**Highest-cardinality fracture so far.** "Custody" carries at least four distinct roles:

| Sense | Where | Relation |
|---|---|---|
| (a) File/artifact custody class | `working/custody-classes.md` | PUBLIC-SHIPPED / ANNEX / SCRATCH / UNRATIFIED-CANDIDATE / DEPRECATED — role in institutional discharge |
| (b) Custody-affecting changes | [[project-lean-custody-state]] § Option C | changes that require explicit ratification authority |
| (c) Independent custody (channel) | loop-capture witness-necessity claim | non-co-captured channel; "fail differently" |
| (d) Substrate-binding custody | witness-carrier-model § 3 | identity + time + authority + substrate jointly covered |
| (e) Same-custody refusal | refusals-need-receipts dual-list | "same-custody appeal is not independent review" |

Provenance, by contrast, has fewer senses: causal lineage of an artifact (often time-indexed). It appears in: witness-carrier-model row 6 (post-hoc laundering / `antiRetroactive`); bridge-obligation-lattice's freshness-atom temporal locus; and (per attack-02) loop-capture's downstream-evidence-cannot-discharge requirement.

The relay's "BoundaryIntegrity = preserve provenance metadata" would collapse senses (b), (c), (d) into one provenance-preservation primitive — exactly the federation-doctrine refusal pattern.

**Verdict:** ALIAS-RISK (high — five senses of custody). Survivor candidates:
- Sibling glossary `working/vocabulary/custody-five-senses.md` (or extend standing-three-senses); same shape as Survivor 1 in attack-04.
- Cross-reference patch: `working/custody-classes.md` does not currently cross-reference witness-carrier-model (substrate-binding sense) or loop-capture (independent-channel sense). Mechanical, ~5 min.

**Survivor:** glossary entry + cross-ref patch. Neither authorized without user signal.

---

## Attack 5 — Authority × authorization

**Question:** Do "authority" and "authorization" denote distinct corpus relations, or has the relay collapsed them?

**Sources:** `LeanProofs/Admissibility/Authority.lean` (PUBLIC-SHIPPED, just read); [[project-admissibility-as-pre-authorization-layer]]; `working/admissibility-as-pre-authorization-layer.md`.

**Distinction is corpus-explicit; relay collapses it.** From the pre-authorization-layer memory:

> *Authorization reasons from premises. Admissibility governs whether those premises may count.*

The corpus carefully distinguishes:

| Word | Sense | Where |
|---|---|---|
| Authority (verdict) | output of the three-input gate `Basis × Precedence × Standing → AuthorityVerdict` | `Authority.lean`'s `AuthorityVerdict.{denied, advisory, authorized}` |
| Authority (binding-obligation) | output authority/capability ≤ input — non-amplification atom | bridge-obligation-lattice's non-amplification atom; witness-carrier-model's authority-binding |
| Authority (source/principal) | the issuer in MayMint(issuer, subject, surface, attempt, now, standing_basis) | witness-carrier-model § 4 |
| Authorization (policy layer) | upstream category (Cedar, RBAC, capabilities, etc.) | pre-authorization-layer note as the *adjacent layer*, not this work |
| Authorization (verdict-as-act) | the `AuthorityVerdict.authorized` value as a binding act | Authority.lean output |

The pre-authorization-layer note (filed 2026-06-04) IS the disambiguation: the corpus's work is NOT in the authorization layer; it's the admissibility layer that gates whether premises *may count* before authorization reasons over them. The relay's "Authority" and "Authorization" alias each other and erase the layering.

**Verdict:** ALIAS-RISK + DUPLICATE on the disambiguation itself. The corpus already has the positioning note that names the layer boundary. The relay's collapse would either (a) put the work into competition with Cedar/RBAC/capabilities (which the pre-authorization-layer note explicitly avoids) or (b) erase Authority.lean's three-input gate by collapsing dimensions.

**Survivor:** none. The pre-authorization-layer note already does the work. The relay's collapse is preventively refused by that note's existence.

---

## Attack 6 — Sacrifice floor × Mist/composition (gap-detection mode)

**Question — re-framed per batch rules as gap detection, not doctrine repair:** Does the corpus have a named composition-axis gap that the relay's "diffuse conversion / Mist Problem / sacrifice floor" is pointing at? If yes, does the relay's framing match the gap?

**Sources:** [[project-local-global-validity-gap]]; `working/local-global-validity-gap.md` (exists per ls; not loaded — gap-detection mode does not require deep read of the candidate to confirm it's a candidate); `working/admissibility-decay-family-note.md` (in context, composition/scope axis row); ls confirms `axis-2-composition-boundary.md`, `axis-2-composition-forcing-cases.md`, `boundary-composition-audit.md`, `boundary-composition-investigation.md` exist; [[project-prosecutorial-decomposition]].

**Gap confirmed.** The corpus has a named composition-axis primitive:

- **Local-Global Validity Gap** — candidate, opened 2026-05-10. *"Locally valid operations can compose into a globally false system."* Sibling axis to admissibility, in the admissibility-decay-family's composition/scope row. Not Lean-built. Second forcing case + composition-theorem needed for ratification.
- **Prosecutorial Decomposition** — the inverse direction; same axis. Candidate, not promoted.
- **Axis-2 composition** material — the merge specimens (`BudgetMerge`, `StaleEvidenceMerge`, conflict slice) operationalize composition-axis refusals at the substrate level; `ParameterizedMerge`'s `MergeAdmissible` is the not-yet-defined positive object that the bad-case family forces.

So the corpus has the gap, *named*, with substrate specimens demonstrating it, and is *deliberately not filling it* until the bad-case family is complete and a composition theorem forces the higher-order construct.

**Relay's framing — sacrifice-floor / empty-discharge region:** REFUSED as gap-filler.

- Relay's framing collapses the *composition gap* (locally-valid → globally-false) with a *substantive moral claim* (no admissible witness reaches the sacrifice-class floor). These are distinct axes.
- The legitimate composition gap is held open precisely because filling it prematurely would mint a unifying composition operator the federation doctrine forbids.
- The relay's "empty discharge region at top of effect lattice" would be: (a) an effect-lattice claim (already refused in attack-05 as LAUNDERING), (b) layered onto a sacrifice-class burden claim (closer to [[project-negative-inclusivity]] territory, which is its own primitive with its own ratification gate).

**Verdict:** GAP CONFIRMED + relay-framing REFUSED. The composition gap exists and is filed correctly (LGVG candidate, prosecutorial-decomposition candidate, axis-2 substrate specimens). The relay's framing offers no new content and would launder the gap-shape by collapsing it with sacrifice-class burden machinery that already lives elsewhere.

**Recommended action:** leave LGVG, prosecutorial-decomposition, and axis-2 material undisturbed. Do NOT use the relay's sacrifice-floor framing to motivate building anything. The gap awaits its own second forcing case + composition theorem.

**No survivor.** Attack #6 was passed the gap-detection bar (it didn't try to repair doctrine); the gap is real, the relay's filling is wrong, the appropriate action is patience.

---

## Patch queue (consolidated)

All items below are **patch-queue only**, not live changes. None is authorized without user signal.

1. **Receipt / witness disambiguation glossary** — sibling to `working/vocabulary/standing-three-senses.md`. Three senses each, mapped to corpus locations. ~30 min draft.
2. **Custody disambiguation glossary** — five senses of custody. Same pattern. ~30 min draft. Could extend the standing-three-senses file into a multi-term glossary OR live as `working/vocabulary/custody-five-senses.md`.
3. **Custody-classes ↔ witness-carrier-model cross-ref patch** — bidirectional, ~5 min. Same shape as attack-02's loop-capture × witness-carrier-model patch.
4. **Custody-classes ↔ loop-capture cross-ref patch** — bidirectional, ~5 min. Independent-channel sense of custody as the connecting tissue.
5. (Carried forward, not new) **Separation-of-custody on exception discharge** as vocabulary candidate for when `NoSilentException.lean` earns Lean staging. Already on the queue from attack-05.

Estimated total patch-queue cost if all applied: ~90 min. Each item is mechanical or glossary-shaped — no theorem, no atom, no doctrine.

---

## Next high-risk targets

For future batches, the highest-yield attacks (most likely to produce non-DUPLICATE classifications) cluster around:

1. **Composition-axis substrate × LGVG candidate** — does the corpus's axis-2 specimen family (BudgetMerge / StaleEvidenceMerge / ConflictMerge / ParameterizedMerge) collectively force the LGVG ratification gate, or does it stop short? Gap-detection mode; could surface a real composition theorem.
2. **Heterogeneous-turtles × independent-custody** — [[project-heterogeneous-turtles-not-witnesses]] (2026-06-06) + loop-capture's witness necessity + same-custody refusal (mandamus). Three altitudes on the *receipt-type axis*; possible MISSING-PRECONDITION on the heterogeneity-doesn't-change-receipt-type theorem.
3. **Negative inclusivity × sacrifice-class** — [[project-negative-inclusivity]] vs the relay's sacrifice-floor framing. Separate question from attack #6: does NI's resolution-selective admissibility primitive cover what the relay was reaching for via sacrifice-floor, or are they different axes? Gap-detection mode.
4. **Witness Carrier Model × Cedar Analysis differential testing** — the methodological-theft slot in pre-authorization-layer is named but not built. Could surface a real BRIDGE-CANDIDATE between the carrier model and a tested-correspondence harness.

Avoid for next batch:
- Anything paper-altitude (P22/P25/P27 ×anything). These are well-mapped; high DUPLICATE risk.
- Anything that touches the calculus-retirement boundary or no-unifier doctrine. The federation discipline is settled; vector-mining against it just produces LAUNDERING verdicts.
- Anything that names a new primitive in the question itself. The relay-shape attacks come pre-collapsed; safer to attack at established kernel boundaries.

---

## Method validation (cumulative, 9 pilots)

- **Three solo pilots** (attacks #5, #2, #4): all DUPLICATE or ALIAS-RISK; gate held; cross-altitude scanning emerged as primitive.
- **Six batch pilots** (#1, #2 [batch], #3, #4 [batch], #5 [batch], #6): four DUPLICATEs, two ALIAS-RISK, one GAP-CONFIRMED-with-relay-framing-refused. No promotion-eligible findings.
- **Zero new Lean modules** across all nine. Zero doctrine edits. One glossary file shipped (standing-three-senses), three cross-ref patches shipped, three more on the patch queue.
- **Workflow-hygiene rule confirmed:** *Relay claims must be audited across Lean substrate, substrate-discipline doctrine, paper-candidate synthesis, watchlist, AND lexical-collision altitudes before being treated as novel. Single-altitude novelty is inadmissible for promotion.*
- **Five distinct failure modes characterized:** vocabulary re-skin (#5); multi-altitude bundle (#2); lexical fracture (#4, #3, #4-batch); preventive gate (#5-batch); gap-shape laundering (#6-batch).

---

## Closing

**PROMOTE NOTHING.**

**PATCH QUEUE ONLY.** Five items, all mechanical or glossary-shaped, ~90 min total cost if all applied. No item is authorized without explicit user signal.

**NEXT HIGH-RISK TARGETS.** Four candidates for a future batch, all gap-detection-mode or substrate-completeness-mode; three avoid-zones named.

The instrument continues to behave. Nine pilots, zero false positives, zero unauthorized doctrine motion. Corpus's own architecture does the rejection work; vector mining makes the rejection legible.
