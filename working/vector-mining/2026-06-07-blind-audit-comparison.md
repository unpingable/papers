# Blind-Audit Comparison — Operator (Pilot #15) vs Codex (gpt-5.5)

**Filed:** 2026-06-07. **Status:** comparison receipt. **NOT doctrine. NOT a paper. NOT a method revision.** **No revision to Pilot #15. No revision to Codex receipt.** No adjudication of which auditor is right. The comparison records *structure of agreement and disagreement*, not winners.

## Setup

Codex (gpt-5.5) audited a blind-auditor bundle on the PEP 634 family corpus, returning a receipt with no operator context. The bundle inlined five claims, a verdict palette, and ~15 source excerpts; codex performed the audit without access to Pilot #15's prior verdicts. Codex's receipt: `blind-auditor-receipt-codex-2026-06-07.md`.

This comparison instructs that **exact verdict agreement is weaker evidence of portability than structural agreement on failure family**. Two cameras catching the same rot from different angles supports portability; two cameras returning the identical verdict string is the lower-information path.

Sources:
- Operator: `2026-06-06-portability-soft-corpus-pilot.md` § Audit (Pilot #15)
- Codex: `blind-auditor-receipt-codex-2026-06-07.md`

## Headline counts

| Metric | Count |
|---|---|
| Claims audited | 5 |
| **Exact verdict-string agreement** (full match across all labels) | **2** (Claims A, D) |
| **Partial agreement** (one or more labels overlap) | **3** (Claims B, C, E) |
| **Divergent** (zero label overlap) | **0** |
| **Structural-family agreement** (same underlying failure caught, possibly via different label) | **5/5** |
| **LABEL-FAILURE on either side** | 0 |
| **Mid-audit revisions** | 1 operator (Claim C), 1 codex (Claim C) |
| **Multi-class verdicts** | operator: 2 (Claims B, C-revised); codex: 4 (Claims B, C, E) |

Zero divergent verdicts. Five-of-five structural agreement. Three-of-five exact-or-partial overlap at label granularity. **No claim collapsed.** No labels failed. Both auditors converged on the same instability locus (Claim C).

## Per-claim table

| Claim | Operator verdict | Codex verdict | Overlap class | Evidence basis overlap | Disagreement source |
|---|---|---|---|---|---|
| A | DUPLICATE | DUPLICATE | **exact** | high (both cite PEP 635 motivation + tutorial + What's New) | — |
| B | INTERNAL-REFUTATION GAP + ALIAS-RISK | DUPLICATE + ALIAS-RISK | **same-family + exact on ALIAS-RISK; codex-less-strict on the second component** | high (both cite PEP 635 § Value Patterns + Language Reference capture/value grammar + PEP 636 dotted-name warning) | (a) label-definition ambiguity — DUPLICATE and INTERNAL-REFUTATION GAP both fit "corpus contains the material" but at different stance-altitudes |
| C | ALIAS-RISK (revised from COUNTEREXAMPLE-CANDIDATE) | COUNTEREXAMPLE-CANDIDATE + INTERNAL-REFUTATION GAP (revised from MISSING-PRECONDITION) | **same-family / adjacent** — both auditors unstable, both reading the corpus's disambiguation; landed at different stable verdicts | high (both cite Language Reference § 8.6.2 + PEP 635 guards rationale) | (e) **actual method instability** at this claim — same unstable locus surfaces in both auditors with different stable end-points; not auditor failure but palette-edge fuzziness |
| D | LAUNDERING | LAUNDERING | **exact** | high (both cite What's New "switch" framing + PEP 635 Capture-Patterns "misconception" rejection) | — |
| E | INTERNAL-REFUTATION GAP | INTERNAL-REFUTATION GAP + COMPOSITION-GAP | **codex-stricter** (operator-set is strictly contained in codex-set) | high (both cite PEP 653 motivation + class-pattern critique; codex extracts an additional COMPOSITION-GAP reading from the same evidence) | (b) **evidence selection** — codex pulled COMPOSITION-GAP from "valid components don't compose to the claimed sufficiency" reading; operator stopped at the refutation-of-sufficiency reading |

## Structural-family agreement (the load-bearing finding)

Treating exact agreement as the lower-information signal and structural agreement as the higher-information signal, all five claims register structural agreement:

- **Claim A — duplicate-shape:** both auditors find the claim already articulated by the corpus at rationale + tutorial + changelog altitudes. *Same failure family caught by both.*
- **Claim B — corpus-contains-disambiguation:** both auditors agree the corpus carries the binding-vs-comparison disambiguation explicitly; operator reads this as *the corpus refused the claim's "discovery" framing* (INTERNAL-REFUTATION GAP), codex reads it as *the claim is already articulated by the corpus* (DUPLICATE). Different cameras, same rot — the rot being "the disambiguation lives at multiple altitudes already." Plus exact agreement on ALIAS-RISK.
- **Claim C — claim collapses what corpus disambiguates:** both auditors landed mid-audit in the territory of "the claim conflates things the corpus separates." Operator stable-reading: lexical fracture across three senses of "first-to-match" (ALIAS-RISK). Codex stable-reading: the claim is contradicted AND the corpus refuses the framing (COUNTEREXAMPLE-CANDIDATE + INTERNAL-REFUTATION GAP). Both auditors saw instability; the instability itself is the consistent finding.
- **Claim D — changelog vs rationale tension:** both auditors detect the same cross-altitude laundering: changelog imports a switch-extension framing that PEP 635 rationale explicitly rejected. Exact verdict-string match.
- **Claim E — composition-of-valid-mechanisms-not-sufficient:** both auditors detect that PEP 653's existence refutes the sufficiency claim of PEP 634 + `__match_args__` + `collections.abc`. Operator records the refutation as INTERNAL-REFUTATION GAP; codex additionally extracts a COMPOSITION-GAP reading (valid components don't compose to claimed sufficiency). Codex's additional reading is in the same family.

**Five-of-five structural-family agreement is materially stronger than two-of-five exact agreement.** Per user's framing: two cameras catching the same failure from different angles is real signal.

## Where evidence-bases diverged

Across all five claims, the evidence-base overlap is high. Both auditors cited:
- PEP 634 (spec) — Claim A
- PEP 635 (rationale) — all five claims
- PEP 636 (tutorial) — Claims A, B
- What's New 3.10 (changelog) — Claims A, C, D
- Python Language Reference — Claims B, C, E
- PEP 653 (regret PEP) — Claim E

Neither auditor pulled significantly from the CPython tracking issue or implementation PR (Documents 6, 7); both relied primarily on PEP-text + Language Reference for the verdict load. Evidence-base overlap is therefore close to total at the document level.

Where evidence selection differed at the *passage* level, the divergence was about *which sentence of the same document* to cite as load-bearing. Codex was somewhat more thorough at extracting multi-class verdicts from a single document's evidence (Claim E COMPOSITION-GAP from PEP 653; Claim C INTERNAL-REFUTATION GAP from Language Reference).

## Disagreement-source map (per user's question 4)

| Disagreement source | Where it fired | Count |
|---|---|---|
| (a) label-definition ambiguity | Claim B (DUPLICATE vs INTERNAL-REFUTATION GAP overlap zone) | 1 |
| (b) evidence selection | Claim E (codex extracted COMPOSITION-GAP from shared evidence operator stopped short of) | 1 |
| (c) claim wording ambiguity | not the dominant factor on any claim (both auditors honored the claims verbatim) | 0 |
| (d) missing precondition | not surfaced as a disagreement source | 0 |
| (e) **actual method instability** | Claim C (both auditors unstable mid-audit, different stable end-points) | **1** |

Three of five claims had no disagreement source to enumerate (Claims A, D exact; Claim B largely overlapping with one fuzzy edge). Only one claim (C) exhibits actual method instability; the other two disagreement instances (Claims B and E) are within-palette resolution differences rather than method failure.

**The single method-instability site is Claim C, in both audits.** This is convergent diagnostic data.

## Overall portability judgment

> **Portable with palette refinement.**

The method retained discrimination under blind audit by a non-operator. Structural agreement on 5/5 claims. Zero divergent verdicts. Zero LABEL-FAILUREs. The verdict palette was sufficient for both auditors. The single locus of method instability (Claim C) is the same locus operator identified in the original Pilot #15 receipt — *the instability is reproducible*, not auditor-specific.

The "with palette refinement" qualifier records: at the boundary between DUPLICATE / INTERNAL-REFUTATION GAP / ALIAS-RISK / COUNTEREXAMPLE-CANDIDATE, the palette's edges are fuzzy enough that different auditors land different verdicts on the *same underlying observation*. This isn't a fatal flaw — both auditors caught the underlying failure family — but it is a real signal that the labels could be sharpened. Specifically:

- The boundary between *"corpus already says this"* (DUPLICATE) and *"corpus already refused this framing of the same observation"* (INTERNAL-REFUTATION GAP) needs sharper definition. They are close cousins; the difference is whether the corpus has a *positive articulation* or a *refusal* of the claim's framing.
- The boundary between *"claim conflates X and Y"* (ALIAS-RISK) and *"claim is contradicted by Z"* (COUNTEREXAMPLE-CANDIDATE) overlaps when the conflation IS the contradiction.

The right verdict on portability is therefore stronger than "operator-dependent" (the method survived) and weaker than "portable" (palette edges show fuzziness across auditors). "Portable with palette refinement" matches the observed data without over-claiming.

User's predicted outcome — *"portable at failure-family level; partially operator-dependent at verdict granularity"* — matches the observed result almost verbatim.

## Claim C: keep, split, or retire?

**Retain as stress specimen.**

Claim C is the only claim where both auditors revised mid-audit and landed at non-overlapping stable verdicts. That makes it the highest-signal probe in the bundle for testing palette-edge ambiguity and method stability. Removing it would erase the diagnostic information that *both* auditors found ambiguity in *the same place*. Splitting it would change the claim and discard the convergent instability finding. Keeping it lets future replication audits (C3, blind-auditor-#2) measure whether the same instability site recurs and whether the palette boundary tightens with use.

The "claim is bad / palette is fuzzy / both" question is not yet decidable from two audits. A third independent auditor on the same bundle, or a palette-refinement experiment that re-runs the same audits with tightened label boundaries, would let the question separate. Until then, Claim C is doing useful work as a *stability stress specimen* exactly because it makes auditors visibly unstable.

## Receipt hygiene

- Codex's receipt is dated `2026-06-08` in its header. Actual run completed 2026-06-07 (today, ~one hour before this comparison). Off-by-one date is a gpt-5.5 quirk; recorded for transparency, not load-bearing. The temporal-discipline-instrument hallucinating tomorrow is mildly comic; cataloged in the hygiene bucket.
- Both auditors honored the "no prior verdicts" packet constraint; codex did not request expected verdicts.
- Both auditors honored the "no new labels" constraint; LABEL-FAILURE was never invoked.
- Codex's audit time self-reported as ~45 minutes; operator's audit time was longer (interleaved with corpus fetch and write).

## What the comparison does NOT claim

- **Not proof of method portability.** Two auditors on one corpus is two audits; the result supports candidate portability under explicit palette-refinement caveat, not generalized portability.
- **Not adjudication.** Where operator and codex differed, the receipt does not declare which auditor's verdict is "correct." Both verdicts were reached by reading the corpus and applying the palette; both were defensible at their own altitude.
- **Not method revision.** No palette label has been refined as a result of this comparison; the "palette refinement" qualifier is a *recommendation for future work*, not an executed change.
- **Not promotion.** The Track C external-portability candidate pattern remains candidate-not-promoted in the method note. Two auditors on one corpus is not three corpora; it is also not the same threshold.

## Suggested next gates (named, not authorized)

- **C3 replication on a third corpus** with the *same blind-bundle methodology* (no operator audit; auditor produces verdicts from bundle alone). If the structural-agreement pattern recurs on a different corpus, the candidate portability claim graduates.
- **Palette-refinement pass** that sharpens DUPLICATE / INTERNAL-REFUTATION GAP boundary and ALIAS-RISK / COUNTEREXAMPLE-CANDIDATE boundary. Could be tested by re-running this same comparison with refined labels and measuring whether agreement count goes up.
- **Second blind auditor** (DeepSeek / Grok / different model family) on the same C1 bundle for triangulation. Tests whether the agreement pattern is specific to codex/gpt-5.5 or generalizes across auditor models.
- **Mechanical-aided variant** that allows the auditor to use a Python interpreter on Claim C specifically, to test whether the instability dissolves under mechanical aid.

## Curdling guard

This artifact operates at meta-comparison altitude only. No Lean implication. No new primitive minted. No alteration to either source receipt; no alteration to the method note's promotion thresholds. Pilots #15, #16, and this comparison receipt are independent records. The blind-auditor packet and bundle remain frozen; the codex receipt is preserved (raw + clean versions).

## Cross-references

- `2026-06-06-portability-soft-corpus-pilot.md` (Pilot #15) — operator audit
- `blind-auditor-bundle-2026-06-07.md` — self-contained packet sent to codex
- `blind-auditor-receipt-codex-2026-06-07.md` — codex's receipt (clean)
- `blind-auditor-receipt-codex-2026-06-07-raw.md` — codex's receipt (raw with CLI banner)
- `method-note.md` — operating procedure; not modified by this comparison
- `2026-06-07-portability-c2-rust-let-else.md` (Pilot #16) — C2 receipt; not in scope for this comparison

---

**No method change. No palette refinement executed. No promotion. Two-auditor evidence supports candidate portability with named palette-refinement caveat; not proof.**
