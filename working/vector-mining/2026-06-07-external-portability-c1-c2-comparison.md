# External Portability Comparison — C1 (PEP 634) ↔ C2 (Rust RFC 3137 / let-else)

**Filed:** 2026-06-07. **Status:** cross-receipt comparison artifact. **NOT doctrine. NOT a paper. NOT a promotion of the method. NOT a portability proof.** **Receipt only.** Operates strictly on the two completed Pilot #15 (C1) and #16 (C2) receipts; does not re-audit either corpus and does not revise either pilot's verdicts.

## Setup

User-authorized comparison after both pilot receipts existed and were frozen. The seven questions the comparison must answer (user-supplied):

1. Which verdict classes recurred across both corpora?
2. Which failure modes recurred?
3. Did existing labels remain sufficient?
4. Where did each corpus depend on operator prior?
5. Where would a mechanical altitude have helped?
6. Does LAUNDERING externally recur in the same shape?
7. Does the method retain discrimination, degrade gracefully, or show receipt-shaped-vibes risk across two corpora?

Expected status language (user-supplied):

> *"Two-corpus external evidence supports candidate portability under caveats; not proof of portability."*

Constraints:
- Do not promote method as proven portable.
- Do not introduce new labels.
- Do not revise either pilot.
- Do not compare to internal corpus except in a short clearly marked note.
- No doctrine.
- No paper.

## Source pilots (frozen)

- Pilot #15 (C1): `2026-06-06-portability-soft-corpus-pilot.md` — PEP 634 family — *RETAINS DISCRIMINATION with caveats*
- Pilot #16 (C2): `2026-06-07-portability-c2-rust-let-else.md` — Rust RFC 3137 / let-else — *RETAINS DISCRIMINATION with caveats*

External corpora archived at `~/git/track-c-pep634/sources/` and `~/git/track-c-let-else/sources/`.

## Question 1 — Verdict classes recurring across both corpora

| Verdict class | C1 instances | C2 instances | Recurs externally? |
|---|---|---|---|
| DUPLICATE | Claim A | Claim A | YES |
| ALIAS-RISK | Claims B, C | Claims B, E | YES |
| INTERNAL-REFUTATION GAP | Claims B, E | Claims B, C | YES |
| LAUNDERING | Claim D | Claim D | YES |
| COUNTEREXAMPLE-CANDIDATE | Claim C (revised to ALIAS-RISK on re-read) | — | NO (one-shot, revised) |
| PREVENTIVE GATE | — | — | NO |
| MISSING-PRECONDITION | — | — | NO |
| BRIDGE-CANDIDATE | — | — | NO |
| COMPOSITION-GAP | — | — | NO |
| GAP CONFIRMED + RELAY-FRAMING REFUSED | — | — | NO |

Four verdict classes recur externally on both corpora. Two of them (ALIAS-RISK, INTERNAL-REFUTATION GAP) are the two standing failure modes' verdict-class counterparts. DUPLICATE and LAUNDERING are the additional two.

No verdict class appeared exclusively on one corpus (COUNTEREXAMPLE-CANDIDATE was a within-pilot revision in C1, not a sustained verdict).

## Question 2 — Failure modes recurring

| Failure mode | C1 instances | C2 instances | Recurs externally? |
|---|---|---|---|
| #1 Vocabulary re-skin | Claim A (mild) | Claim A (mild) | YES (mild) |
| #2 Multi-altitude bundle | — | — | NO |
| #3 Lexical fracture | Claims B, C | Claims B, E | **YES (clean)** |
| #4 Preventive gate | — | — | NO |
| #5 Gap-shape laundering | — | — | NO |
| #6 Internal-refutation gap | Claims B, E | Claims B, C | **YES (clean)** |

Two standing failure modes (#3 and #6) recur cleanly on both external corpora. This is the load-bearing finding: the modes the cave promoted to standing are not cave-local.

Modes #2, #4, #5 did not fire in either external pilot. This is consistent: these modes target specific relay-shape attack patterns (multi-altitude bundle, preventive-gate, gap-shape laundering) that are *cave-specific phenomena* — they describe how *internal* relay attacks fail. External corpora do not have analogous attack vectors in the audit framing used here.

## Question 3 — Did existing labels remain sufficient?

**Yes, on both corpora.** Five claims per corpus, ten verdicts total. Every verdict used an existing label. One C1 verdict was revised mid-claim from COUNTEREXAMPLE-CANDIDATE to ALIAS-RISK; both labels are in the existing palette.

No new labels minted. No verdict required an extension. No claim was unclassifiable.

## Question 4 — Operator prior dependencies

### C1 (PEP 634)

- **Corpus selection:** Operator selected PEP 653 (post-acceptance precise-semantics PEP) because the operator's prior expected PEP 634's under-specification to have generated a follow-up PEP. The expectation was correct, but the *selection* was prior-steered.
- **Claim construction:** Claims were constructed from the *concept* of structural pattern matching without targeting specific verdicts. No single claim's existence was prior-steered (claims A–E all emerged from the feature's structural shape).

### C2 (Rust RFC 3137)

- **Corpus selection:** Operator selected the internals-forum thread on let-else × let-chains non-interaction because the operator's prior knew this was a live discussion. Like C1's PEP 653, the *existence* was confirmed but the selection had a fingerprint.
- **Claim C construction:** Operator's training-data prior knew that `&&`/`||` in let-else is reserved syntactic space. Claim C's *existence* was prior-steered; a blind auditor without Rust documentation knowledge would not have invented it.
- **Claim D construction:** Claim D directly targeted the user-supplied substrate-specific watchlist patterns ("accepted RFC ≠ stabilized behavior", "stabilization ≠ all edge cases settled"). Presence-confirmation of these patterns in C2 Claim D is weaker evidence than blind-discovery would have been.

### Comparison

C2 had more operator-prior contamination than C1. Two distinct mechanisms:
- C1: prior steered *one* corpus selection (PEP 653).
- C2: prior steered *one corpus selection* (forum thread) + *one claim construction* (C) + *one claim's target shape* (D, via user watchlist).

Honest framing: C2's higher contamination makes its verdicts less surprising, but its *cross-altitude evidence trail* (RFC Future Possibilities + Reference grammar carve-out + internals thread on Claim C; changelog vs stab-PR named-concerns + tracking-issue blocker on Claim D) is independently strong. The contamination affects *claim selection*, not *evidence sufficiency for the verdict given the claim.*

## Question 5 — Where would a mechanical altitude have helped?

### C1 (PEP 634)

Three mechanical altitudes available, deliberately not invoked:

- **Python interpreter** for Claim C's side-effects-in-guards question. Trivial decision (run `match x: case _ if (print('side-effect'), True)[1]: pass`).
- **Static analyzer (mypy, pylint)** for Claim B's bare-name-as-capture surprise. Both tools warn on this; cheaper than rationale reading.
- **Behavior-differential test** (CPython vs alternate-pattern-matching implementations) for Claim E's class-pattern under-specification.

### C2 (Rust RFC 3137)

Four mechanical altitudes available, deliberately not invoked:

- **rustc playground** for Claim B's divergence-vs-refutability edge cases. Type errors from edge-case programs would have decided the type-system-rule question.
- **rustc with `--warn irrefutable_let_patterns`** for Claim E's grammar-vs-lint fracture. Single-command decision.
- **Behavior-differential test** for Claim D's desugaring difference (RFC-described match-form vs shipped form).
- **Compile attempt** for Claim C's chaining behavior. The rustc error message would have disambiguated parser-level rejection vs type-system rejection.

### Comparison

C2 had more available mechanical altitudes (4 vs 3) and they were more trivially accessible (rustc playground is single-click). C1 corresponds slightly less directly to its mechanical altitudes (CPython behavior-differential testing is non-trivial; static-analyzer behavior depends on tool choice). 

**The deliberate-non-invocation discipline held on both corpora.** Neither pilot reached for the playground. Both pilots flagged the available-but-unused altitudes explicitly.

**The cost of non-invocation is asymmetric:** C2's mechanical altitudes would have been *cheaper to invoke* than C1's. A future-pilot question worth recording (not promoting): *should the no-mechanical-altitude constraint be relaxed for replication runs, given that calibration benefits visible in C2 may be mechanical-altitude-substitutable?*

## Question 6 — Does LAUNDERING externally recur in the same shape?

**Yes, in the same shape both times.**

### C1 (PEP 634) Claim D

- **User-facing framing:** What's New 3.10 opens with *"pattern matching ... like the switch statement found in C, Java or JavaScript."*
- **Decision-record refusal:** PEP 635 § Capture Patterns explicitly rejects this framing as *"misconception that pattern matching extends switch statements"* — used as the *rationale* for rejecting explicit-marker syntax proposals.
- **Pattern:** changelog imports a mental model the rationale explicitly named as misconception-driving-rejected-design-choices.

### C2 (Rust let-else) Claim D

- **User-facing framing:** Rust 1.65 release notes package let-else as "stabilized"; second major feature; no caveats about unresolved edge cases.
- **Decision-record refusal:** Stabilization PR carries `@rfcbot concern need-consistency-rvalue-temporary-rules-between-let-and-let-else`; tracking issue notes implementation didn't match RFC behaviour; one core dev: *"Originally the RFC described the lowering in form of a match statement. I'm not sure why @cormacrelf chose the currently used desugaring in their PR."*
- **Pattern:** changelog packages "stabilized" as settlement while stabilization PR explicitly carries forward unresolved items as fixable-post-stabilization.

### Common shape

Both LAUNDERING instances exhibit the same structural pattern:

> *User-facing simplification (changelog / release-notes altitude) compresses a contested status into a settled framing; decision-record altitude (rationale PEP or stabilization PR) carries the contestation explicitly. The compression is not a lie; it is a register-shift that smooths over the contested-but-shipped status into something readable as "decided."*

This is more specific than just "LAUNDERING." It is *user-facing-changelog vs internal-decision-record laundering on the stabilization/settlement axis.* The two specimens are not identical-instance — PEP 634's is a *conceptual* mental-model framing; Rust let-else's is a *status* framing — but they are isomorphic under the *register-shift from contested to readable* lens.

### Recording (NOT promoting)

This is an **externally recurring observation**, NOT a new failure mode. Two specimens of a shape do not earn promotion to standing mode; the threshold for failure-mode promotion in the method-note is three specimens. The shape is recorded here and in the method-note Track C subsection at observation altitude.

The framing-as-hypothesis from the user, preserved verbatim for re-check:

> *Internal corpora with explicit federation/refusal doctrine suppress laundering by refusing collapse early; external soft corpora surface laundering as cross-altitude tension between user-facing framing and decision-record evidence.*

Status: candidate hypothesis. Two-corpus support, not three. Not promoted.

## Question 7 — Discrimination, degradation, or vibes across two corpora?

**Retains discrimination across both corpora.** Not degrades-gracefully; not collapses-into-receipt-shaped-vibes.

Evidence:

- All ten verdicts (five per corpus) cite specific corpus locations.
- Four verdict classes recurred across both corpora with non-trivial citation patterns.
- Two standing failure modes (#3, #6) both fired cleanly on both external substrates.
- Existing label palette was sufficient on both runs.
- No verdict was unclassifiable. One verdict (C1 Claim C) was revised on re-read; the revision was internal-to-existing-palette.
- LAUNDERING verdict surfaced in the same shape on both corpora.

Caveats that prevent a stronger statement:

- Two corpora is two corpora, not many.
- Same operator across both runs (common-mode risk between operator-as-corpus-selector and operator-as-verdict-grader is unmitigated).
- C2 benefited from C1's calibration (path-dependence is real; second-pilot was more deliberate about cross-altitude reading).
- Both corpora had cheap mechanical altitudes deliberately ignored; the prose-altitude discrimination was tested honestly, but mechanical altitudes would have *sharpened* multiple verdicts.
- Operator prior contaminated C2 Claim C's selection (named explicitly).
- User-named substrate-specific watchlist steered C2 Claim D construction (presence-confirmation is weaker than blind-discovery).

## Short clearly marked note on internal-corpus comparison

This section is explicitly bounded per user instruction: *"Do not compare to internal corpus except in a short clearly marked note."* Limited to one observation worth recording.

> **Observation (not analysis):** Internal pilots #1–#2 produced LAUNDERING verdicts in the early relay-attack pilots. Internal pilots #4–#14 did not produce LAUNDERING verdicts. External pilots #15 and #16 both produced LAUNDERING verdicts (on Claim D each). This is *consistent* with the federation-doctrine-as-internal-laundering-suppressor hypothesis, but the internal-LAUNDERING-quieting after pilot #2 is also consistent with the corpus *internalizing* the federation doctrine over time (the explicit refusal-kernel layer of the corpus matured between #2 and #4). The two hypotheses (federation-doctrine-suppresses vs corpus-internalized) are not separable from this comparison alone. Recording for transparency; not analyzed further.

End of internal-comparison note.

## Status

> **Two-corpus external evidence supports candidate portability under caveats; not proof of portability.**

Standing rule for future portability work:

- **Three-corpus replication** is the next gate for graduating from candidate to standing for the Track C pattern (matching the same three-specimen threshold the failure-mode promotion gate uses).
- **A deliberately-mechanical-aided run** that produces non-trivial divergence with the prose-only runs is a separate gate worth setting up; the question *"how much of the discrimination is the method vs the operator's care?"* is best addressed by running the same audit with mechanical aid and comparing.
- **A blind-auditor variant** (different operator-prior fingerprint) is a stronger discrimination test than another same-operator pilot.

None of these three gates is authorized; all three are recorded for future user consideration.

## Cumulative-state snapshot (2026-06-07)

```text
16 pilots
14 internal
2 external
6 failure modes
Modes #3 and #6 standing — both recur externally on both C1 and C2
LAUNDERING recurs externally twice (Claim D on both runs); externally recurring observation, NOT a new mode
0 unauthorized motion
external portability candidate strengthened (two-corpus); not promoted
patch queue empty
held by deliberate refusal:
  - sacrifice-three-senses.md
  - bridge-obligation-lattice line 148 forward-pointer
curdling guard intact
```

## Curdling guard

This artifact operates at meta-comparison altitude only. No Lean implication. No new primitive minted. No alteration to either pilot receipt; no alteration to the method note's promotion thresholds. Pilots #15 and #16 receipts are unchanged.

## Cross-references

- [`method-note.md`](method-note.md) — operating procedure; cumulative-pilots table now includes #15 and #16
- [`2026-06-06-portability-soft-corpus-pilot.md`](2026-06-06-portability-soft-corpus-pilot.md) (Pilot #15) — C1, PEP 634 family
- [`2026-06-07-portability-c2-rust-let-else.md`](2026-06-07-portability-c2-rust-let-else.md) (Pilot #16) — C2, Rust RFC 3137 / let-else
- [[project-no-unifier-without-laundering]] — the federation doctrine whose external absence is the LAUNDERING-surfacing hypothesis under test
- [[feedback-claude-common-mode-synthesis]] — methodology check; same-operator-across-both-runs common-mode risk is unmitigated by this comparison

---

**PROMOTE NOTHING. PATCH QUEUE EMPTY. NEXT GATES NAMED.**

Next gates (named, not authorized):

- **Three-corpus replication** (C3) for Track C promotion from candidate-with-two-specimens to standing pattern.
- **Mechanical-aided variant pilot** to decompose method-vs-operator-care contribution to discrimination.
- **Blind-auditor variant** to break same-operator common-mode.
- **Held items unchanged:** Track B paper-shape reauthorization; LGVG family-designation reframe; NoSilentException.lean (NOT_READY per Pilot #14); Labelwatch testimony-vs-enforcement × consequence-partition overlap.
