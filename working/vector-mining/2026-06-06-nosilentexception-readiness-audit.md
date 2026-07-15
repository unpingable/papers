# Pilot #14 — NoSilentException readiness audit (Track A)

**Filed:** 2026-06-06. **Status:** vector-mining receipt; a dated priority/readiness assessment, not a prohibition on formalization. **NOT doctrine. NOT a paper. NOT a primitive. NOT a Lean module.** **NOT a proof sketch.** Operating under [`method-note.md`](method-note.md) discipline. **Verdict palette restricted by user instruction** to: NOT_READY / DUPLICATE / ALIAS-RISK / FORCING_CASE_CANDIDATE / MISSING_PRECONDITION / COUNTEREXAMPLE_CANDIDATE.

**Policy correction (2026-07-14):** the consumer, prose-insufficiency, and forcing-case criteria below are preserved as the rubric this 2026-06 audit used to assess priority and promotion pressure. They are not permission to state or build a theorem. A coherent NoSilentException claim, countermodel, or specification may be formalized in Scratch before a consumer exists and may lead later code. Scratch cannot testify for or pin production; public promotion remains separate, and runtime conformance requires an explicit mapping plus runtime evidence or a refinement proof.

## Setup

The audit question (user-supplied, verbatim shape):

> *Is there a concrete specimen where an exception tries to become precedent or escalation without independent discharge custody, such that existing doctrine requires a tiny Lean spike? Or is the current material still only prose-altitude positioning?*

Hard constraints (user-supplied):

- No Lean.
- No module.
- No proof sketch unless forcing case is explicit.
- No new primitive.
- No doctrine motion.
- No promotion.
- Patch queue only.

These constraints governed this audit pass only. They are not continuing prerequisites for later Scratch formalization.

Inputs read:

- [`../bridge-obligation-lattice.md`](../bridge-obligation-lattice.md) — Exception obligation set `{temporal-bounding, anti-precedent}`; NoSilentException listed as future Lean candidate at line 16 and line 148 ("named, not built. No candidate files yet; the lattice file IS their doctrinal home")
- [`2026-06-05-attack-05-effect-vs-obligation.md`](2026-06-05-attack-05-effect-vs-obligation.md) Survivor 2 (separation-of-custody candidate, lines 60–61)
- [`2026-06-05-batch-six-attacks.md`](2026-06-05-batch-six-attacks.md) Attack #2 (Exception × anti-precedent) and Patch #5 (separation-of-custody held)
- [`../admissibility-as-pre-authorization-layer.md`](../admissibility-as-pre-authorization-layer.md) Cedar 7-row table (line 59: "Did this exception become precedent?" → Exception/anti-precedent atom; line 68 unanswered-questions list)
- [`../tooltheory/documentation-keepers.md`](../tooltheory/documentation-keepers.md) Cedar keeper (line 71) explicitly maps "emergency exit became the main entrance" to *exception ≠ precedent*
- [`../admissibility-vs-arms-control.md`](../admissibility-vs-arms-control.md) Override discipline (Override(actor, time, predicate_bypassed, reason, evidence_considered))
- [`../heterogeneous-turtles-not-witnesses.md`](../heterogeneous-turtles-not-witnesses.md) Override discipline (carries from parent)
- [`../primitives/attractor-admissibility-gap.md`](../primitives/attractor-admissibility-gap.md) cluster clause #4 (*escape ≠ recovery; sacrificial-survival laundering*)
- [`../negative-inclusivity.md`](../negative-inclusivity.md) MAX-pattern contractual specimen (Southwest $1M/plane penalty for requiring simulator training)
- `~/git/lean/LeanProofs/Admissibility/Mandamus.lean` — typed deferral receipt for Frontier 3 (rule-change-as-effect) via [[project-refusals-need-receipts]]

## Readiness criteria

For the 2026-06 audit to assign NoSilentException.lean active-work priority under its then-current YAGNI rubric, **all five** of the following had to hold (composing [`method-note.md`](method-note.md) § "When a result may become a forcing case" with the substrate-doctrine checks). This was a prioritization test, not a formal-development gate:

1. **Concrete specimen present.** A worked instance in the corpus where an exception tries to become precedent or escalation, with the discharge custody question load-bearing in the failure.
2. **Prose treatment insufficient.** The specimen requires composition, type discipline, or formal-impossibility-proof altitude that prose alone cannot supply.
3. **Downstream consumer present.** A paper section, a Lean theorem dependency, or a public claim concretely needs the formalization.
4. **Bridge tax payable.** The five obligation atoms from [[project-no-unifier-without-laundering]] can be honestly discharged: source surface, target surface, witness, licensed claim, residual scope.
5. **Discriminator between anti-precedent (alone) and anti-precedent + separation-of-custody is forced.** The [Attack #5 solo Survivor 2 question](2026-06-05-attack-05-effect-vs-obligation.md) (anti-precedent ± separation-of-custody as one atom with two faces vs. two atoms) is resolved by the specimen rather than left as an open vocabulary choice.

## Evidence FOR readiness

The corpus's recent material does touch the territory:

- **Mandamus typed deferral receipt** (Frontier 3, rule-change-as-effect) is a built-out specimen of *the discharge-system refusing to be the certifier of its own bypass*. The typed receipt enforces separation-of-custody at the Lean type level — Mandamus does NOT discharge rule-change; it emits a typed pointer to the entity that must.
- **Override discipline** (arms-control + heterogeneous-turtles) names the mechanism: `Override(actor, time, predicate_bypassed, reason, evidence_considered)`; *"the bypass is admissible against the bypasser."* Two doctrine notes carry the same shape across distinct refusal kernels.
- **Cedar 7-row map** (line 59) puts "Did this exception become precedent?" inside the upstream-question column that Cedar trusts the application to supply; the corpus's positioning carries that obligation but does not currently formalize it.
- **Cedar keeper** (documentation-keepers line 71) explicitly names *exception ≠ precedent (emergency exit)* as one of the four most load-bearing dynamic refusal families. Prose elevation is high.
- **NI MAX-pattern** is a worked specimen of exception-becomes-contractual-precedent: no-simulator-training was a program design objective; Southwest's $1M/plane contractual penalty made simulator training itself the priced exception, structurally inverting the rule.
- **AAG cluster clause #4** (*escape ≠ recovery; sacrificial-survival laundering*) carries a structurally adjacent refusal pattern at the recovery-audit altitude.
- **Standing vocabulary candidate** for separation-of-custody has been carried across at least three pilots (attack-05 solo Survivor 2; batch attack #2; batch patch #5 held); the linguistic infrastructure is on file.

This is non-trivial corpus pressure on the territory.

## Evidence AGAINST readiness

- **Criterion 1 (specimen):** Each of the worked instances above is already *housed* by an existing primitive or kernel:
  - Mandamus deferral receipt is *built into Mandamus.lean's discharge type* (sprint #1 closed; the separation-of-custody enforcement is already mechanized for rule-change-as-effect at type level).
  - Override discipline is *prose doctrine in two refusal-kernel notes*, deliberately fenced from Lean per curdling timer through 2026-06-07.
  - NI MAX-pattern is *housed by NI* (primitive-naming gate passed 2026-06-03; working note canonical surface).
  - AAG clause #4 is *housed by the AAG cluster* in `primitives/attractor-admissibility-gap.md`.
  - None of these is a "specimen the existing kernels cannot address" — they are all addressed *adequately at the altitude they live*.
- **Criterion 2 (prose-insufficient):** No current specimen demonstrates a *failure of prose treatment*. Prose handles each named case at the altitude it occupies; no composition or formal-verification need has surfaced that requires Lean.
- **Criterion 3 (downstream consumer):** No paper section, Lean theorem dependency, or public claim currently requires `NoSilentException.lean` to function. The bridge-obligation-lattice line 148 explicitly states *"the lattice file IS their doctrinal home until a forcing case earns the build."* No forcing case earned.
- **Criterion 4 (bridge tax):** A NoSilentException kernel would have to carry obligation atoms from multiple existing surfaces (Mandamus deferral discipline, override-discipline override-as-typed-receipt, NI MAX-pattern contractual-as-precedent, AAG escape ≠ recovery). The federation-doctrine bridge tax is non-trivial; without a forcing case, paying it is speculative.
- **Criterion 5 (discriminator):** The attack-05 solo Survivor 2 question — *anti-precedent + separation-of-custody as one atom with two faces vs. two atoms* — remains explicitly open. The audit text reads: *"Filed here as a question for a future kernel-overlap audit when an Exception specimen forces the distinction."* No specimen since has forced it.

Five criteria. Five fails (or, more honestly, five "not-yet"s).

Those failures support the dated **low-priority** verdict. They do not block a bounded Scratch formalization led by a coherent statement; the unresolved discriminator and bridge tax must simply remain explicit rather than being laundered into a stronger claim.

## Verdict

> **NOT_READY.**

Secondary: **NAMED LACUNA persists** — the anti-precedent + separation-of-custody distinction surfaced by attack-05 solo Survivor 2 remains a candidate sharpening, not a separately-named atom. This is the same status as 2026-06-05; the lacuna is named-but-deferred, *not silently assumed*. Therefore not MISSING_PRECONDITION (the gap is explicit), not DUPLICATE (the gap is real), not ALIAS-RISK (the vocabulary is consistent across the references), not FORCING_CASE_CANDIDATE (no specimen forces the distinction), not COUNTEREXAMPLE_CANDIDATE (no contradiction surfaced).

NOT_READY is the cleanest classification of 2026-06 priority: the territory is named, the doctrinal home is the lattice, and prose-altitude treatment was sufficient for every consumer the corpus then had. It is not a “no Lean until a consumer arrives” rule.

## What would tip the historical priority verdict to FORCING_CASE_CANDIDATE

Recording the predicate so a future audit can re-check cleanly:

> *NoSilentException.lean earns its forcing case when a single specimen exhibits all of: (a) a temporally-bounded bypass of a stated rule; (b) the bypass attempting to become precedent OR escalating to a different surface/actor/scope; (c) self-discharge of the anti-precedent obligation by the bypassing actor (no independent custody); (d) the specimen is consequential enough that a downstream consumer — paper section, Lean theorem dependency, or public claim — needs the impossibility-proof altitude; (e) prose treatment by NI / Mandamus / arms-control override-discipline / Cedar emergency-exit keeper / AAG clause #4 collectively fails to address the specimen.*

The conjunction of (a)–(e) was the forcing-case/priority predicate used by this audit. At filing time none of (a)–(e) held in isolation, let alone in conjunction. It is useful for deciding urgency and later promotion pressure, not for granting permission to formalize.

## What this pilot did NOT find

Per containment mode, explicit negative findings:

- **No FORCING_CASE_CANDIDATE.** No specimen in the corpus forces the distinction the Lean spike would mechanize. The closest candidates (Mandamus deferral, NI MAX-pattern, AAG clause #4) are all already housed adequately by existing primitives.
- **No MISSING_PRECONDITION.** The anti-precedent + separation-of-custody status is *explicitly named* as a deferred candidate in three places (attack-05 solo, batch attack #2, batch patch #5); not silently assumed.
- **No COUNTEREXAMPLE_CANDIDATE.** No specimen contradicts the lattice's anti-precedent treatment of Exception.
- **No DUPLICATE.** The territory is not duplicated by another Lean module; Mandamus handles a *different* facet (deferral-as-typed-receipt for rule-change-as-effect) — distinct from "exception-as-precedent" at the obligation-set level.
- **No ALIAS-RISK.** "Exception" is used consistently across the lattice, Mandamus, NI MAX-pattern, override-discipline, and Cedar keeper as *bounded bypass that leaves the rule intact*. The CS-tradition "exception (throw/catch)" sense is not in active use anywhere this audit could find.

## Patch queue (refusal-biased; user authorization required)

One candidate surfaced; small, mechanical, navigability-only. **None landed.**

1. **(Optional) Bridge-obligation-lattice line 148 → forward pointers.** The line then read: *"Future candidates NoSilentDelegation, NoSilentException, NoSilentProjection — named, not built. No candidate files yet; the lattice file IS their doctrinal home until a forcing case earns the build."* The “earns the build” clause is superseded by the 2026-07-14 policy correction above. A forward pointer could still help the next reader find the dated priority assessment without re-deriving it. **Recommend: hold by default.** The lattice is currently clean; adding a pointer per future-candidate creates maintenance burden without paying down current pain. Revisit only if a Pilot #15+ re-audit needs the same trail-following work.

## Method-side observations

Track A's value is *negative confirmation*: the instrument can approach a named-not-built future Lean spike with a structured readiness check and come back with "still not ready, here's the predicate that would tip it." That is:

- More legible than an unstructured priority decision.
- More legible than "we still haven't built it because it remained low priority."
- Reusable: the readiness predicate above can be re-checked by any future audit without re-deriving the criteria.

If this becomes a standing audit pattern, the method-note could grow a *Readiness audit* sibling section to the existing pilot patterns. NOT authorized in this pilot — flagging for future user consideration.

## Common-mode check

Per [[feedback-claude-common-mode-synthesis]]: the audit question was user-supplied with explicit allowed verdicts including NOT_READY (giving the instrument an honest negative-result classifier). The corpus checks drew on mixed-authorship material:

- Mandamus is a multi-session build with codex review and operator-authored corrections (recursive scar preserved per [[project-refusals-need-receipts]]).
- Override discipline is ChatGPT-supplied (arms-control note provenance).
- NI MAX-pattern is operator-named + ChatGPT-extended.
- AAG clause #4 is ChatGPT-extended.
- Cedar 7-row map was codex-corrected after Claude common-mode drift in the original draft.

The "no forcing case" verdict is therefore not Claude-on-Claude common-mode; the non-emergence of a forcing case is supported by mixed-authorship material that collectively addresses the territory at prose altitude. Common-mode immunity holds.

## Failure-mode notes

This pilot does not surface a new failure mode. The readiness-audit pattern is *complementary* to the relay-attack patterns the method-note enumerates: it is a planned probe of a named-not-built artifact, not a defense against a relay-shape claim. If the readiness-audit pattern proves useful across Pilots #15+, it will earn its own method-note section.

## Cumulative-pilots update

To be appended to [`method-note.md`](method-note.md) § Cumulative pilots table when user authorizes:

| # | Pilot | Verdict | Survivors |
|---|---|---|---|
| 14 | NoSilentException readiness audit (Track A) | NOT_READY (named lacuna persists; no specimen forces the discriminator) | 1 candidate patch held by recommendation (lattice line 148 forward pointer); readiness predicate recorded for future re-check |

Failure-mode list unchanged.

## Curdling guard

This pilot operates at vector-mining + readiness-check altitude only. No Lean implication. No new primitive minted. No alteration to bridge-obligation-lattice; no alteration to Mandamus; no alteration to NI or AAG. The arms-control / heterogeneous-turtles 2026-06-07 timer is not touched by this pilot.

## Cross-references

- [`method-note.md`](method-note.md) — operating procedure
- [`2026-06-05-attack-05-effect-vs-obligation.md`](2026-06-05-attack-05-effect-vs-obligation.md) Survivor 2 — the original separation-of-custody candidate
- [`2026-06-05-batch-six-attacks.md`](2026-06-05-batch-six-attacks.md) Attack #2 + Patch #5 — the carry-forward
- [`2026-06-06-witness-carrier-vs-cedar.md`](2026-06-06-witness-carrier-vs-cedar.md) (Pilot #12) — Cedar layer-separation context
- [`2026-06-06-negative-inclusivity-vs-sacrifice-class.md`](2026-06-06-negative-inclusivity-vs-sacrifice-class.md) (Pilot #13) — NI ↔ AAG containment context
- [`../bridge-obligation-lattice.md`](../bridge-obligation-lattice.md) line 148 — doctrinal home for NoSilentException
- `~/git/lean/LeanProofs/Admissibility/Mandamus.lean` — typed deferral receipt mechanism
- [[project-no-unifier-without-laundering]] — federation discipline
- [[project-refusals-need-receipts]] — Mandamus context
- [[feedback-claude-common-mode-synthesis]] — methodology check
- [[feedback-forcing-case]] — name-early discipline (post-2026-06-01 calibration note)

---

**PROMOTE NOTHING. PATCH QUEUE ONLY. NEXT HIGH-RISK TARGETS NAMED.**

Next high-risk targets (named, not authorized):

- **Track B — paper-shape reauthorization** for *no-lift as base case, composition boundary as center of gravity* — user-staged; not vector-mining altitude. Higher-gravity decision than Track A; appropriate after a checkpoint.
- **Track C — portability stress test** against a soft external corpus with no Lean — methodology probe; tests whether Cross-Altitude Novelty Audit retains discrimination outside this cave.
- **LGVG family-designation reframe** — user-held.
- **Labelwatch testimony-vs-enforcement × consequence-partition overlap** — NI gates-remaining item; flagged in pilots #13 footer.
- **Re-audit predicate refresh** — re-check whether prose-altitude treatment is *still* sufficient for current priorities OR whether ambient pressure from cumulative pilots has tipped one of the historical readiness criteria. This affects urgency, not permission to formalize.
