# Three-Way Blind-Audit Comparison — Operator vs Codex vs Gemini

**Filed:** 2026-06-07. **Status:** three-way comparison receipt. **NOT doctrine. NOT a paper. NOT a palette revision.** No revision to any source receipt. No adjudication of which auditor is "right." Records *triangulated* structure of agreement and disagreement across three independent auditors on the same frozen C1 bundle.

## Setup

Same frozen C1 bundle ([`blind-auditor-bundle-2026-06-07.md`](blind-auditor-bundle-2026-06-07.md)) sent independently to three auditors:

| Auditor | Model / Identity | Receipt file |
|---|---|---|
| Operator | Claude Code (Opus 4.7), with full prior context | `2026-06-06-portability-soft-corpus-pilot.md` (Pilot #15) |
| Codex | gpt-5.5 (via `codex exec`), blind | `blind-auditor-receipt-codex-2026-06-07.md` |
| Gemini CLI | gemini-2.5-flash (via `gemini -p`), blind | `blind-auditor-receipt-gemini-2026-06-07.md` |

Both blind auditors received the self-contained bundle with no operator verdicts, no prior pilot history, no method context. Codex completed via inline-prompt after initial sandbox failure; Gemini completed via inline-prompt on first run after retry on default-model-quota → flash.

User constraint: **exact agreement is weaker evidence than structural-family agreement.** Two cameras catching the same rot from different angles supports portability.

## Headline three-way table

| Claim | Operator | Codex | Gemini | Three-way structural agreement? |
|---|---|---|---|---|
| A | DUPLICATE | DUPLICATE | DUPLICATE | **YES — 3/3 exact** |
| B | INTERNAL-REFUTATION GAP + ALIAS-RISK | DUPLICATE + ALIAS-RISK | DUPLICATE | **YES — all three find "corpus contains the disambiguation"; verdict labels differ** |
| C | ALIAS-RISK (revised from CC) | COUNTEREXAMPLE-CANDIDATE + INTERNAL-REFUTATION GAP (revised from MP) | COUNTEREXAMPLE-CANDIDATE | **YES on instability** — three different verdicts, none of them DUPLICATE / DEAD-END; all three see something wrong with the claim |
| D | LAUNDERING | LAUNDERING | LAUNDERING | **YES — 3/3 exact** |
| E | INTERNAL-REFUTATION GAP | INTERNAL-REFUTATION GAP + COMPOSITION-GAP | COUNTEREXAMPLE-CANDIDATE | **YES — all three converge on "PEP 653 refutes the sufficiency claim"; labels differ** |

## Three-way exact agreement counts

| Agreement type | Count |
|---|---|
| **Full three-way exact verdict-string match** | **2/5** (Claims A, D) |
| Two-of-three exact match on at least one label | 4/5 (A: 3/3 DUPLICATE; B: codex+gemini agree on DUPLICATE; C: codex+gemini agree on COUNTEREXAMPLE-CANDIDATE; D: 3/3 LAUNDERING) |
| Zero label overlap across all three | 0/5 |
| LABEL-FAILURE on any auditor | 0 |
| Three-way structural-family agreement | **5/5** |

**Zero divergent claims across three independent auditors.** Five-of-five structural-family agreement. Two-of-five three-way-exact verdict-string match. **No claim collapsed; no labels failed.**

## Claim D is the strongest single datapoint

Three independent auditors — different model families (Claude / GPT / Gemini), different prompt invocations, different verdict-tendency profiles — all returned exactly `LAUNDERING` for Claim D. Same evidence cited (`[WHATSNEW-OPENING-01]` + `[PEP635-CAPTURE-01]`). Same reasoning structure (changelog imports rejected framing).

LAUNDERING is the *least generic* label in the palette. It requires identifying a specific illicit transformation: one altitude gaining authority by passing through another. Three-way exact LAUNDERING agreement is the strongest single piece of portability evidence in this experiment.

## Claim C instability reproduced — at full triangulation

Three auditors, three distinct stable verdicts on Claim C:

| Auditor | Verdict on Claim C | Mid-audit revision? |
|---|---|---|
| Operator | ALIAS-RISK | YES (revised from COUNTEREXAMPLE-CANDIDATE) |
| Codex | COUNTEREXAMPLE-CANDIDATE + INTERNAL-REFUTATION GAP | YES (revised from MISSING-PRECONDITION) |
| Gemini | COUNTEREXAMPLE-CANDIDATE | NO |

What recurs is **disagreement on label**, not disagreement on detection. All three auditors detected that Claim C is wrong or unstable. None classified it as DUPLICATE, BRIDGE-CANDIDATE, or DEAD-END. The destabilization site reproduced; the convergence point did not.

Three-auditor pattern on Claim C:
- Operator and Codex both revised mid-audit; Gemini did not.
- Codex and Gemini converged on COUNTEREXAMPLE-CANDIDATE (at least as one component).
- Operator's stable end-point (ALIAS-RISK) is the outlier — but it was the result of revision, so the "first-pass instinct" of all three was closer to COUNTEREXAMPLE-CANDIDATE territory.

This is convergent diagnostic data: **Claim C is a calibration artifact, not a noise artifact.** The instability is structural to either the claim or the palette boundary in this region, not auditor-specific.

## Fuzzy palette edges — three-auditor triangulation

The two fuzzy edges named in the two-way comparison receipt now have triangulated evidence:

### Edge 1: DUPLICATE ↔ INTERNAL-REFUTATION GAP

| Claim | Operator | Codex | Gemini |
|---|---|---|---|
| B | INTERNAL-REFUTATION GAP | DUPLICATE | DUPLICATE |
| E | INTERNAL-REFUTATION GAP | INTERNAL-REFUTATION GAP | COUNTEREXAMPLE-CANDIDATE |

This edge fires on B and E. Three auditors hit it three times. The pattern:
- **Operator** prefers INTERNAL-REFUTATION GAP when the corpus contains the *disambiguation that defeats* the claim's framing.
- **Codex** mixes — DUPLICATE on B (positive-articulation reading), INTERNAL-REFUTATION GAP on E (refusal reading).
- **Gemini** prefers DUPLICATE on B and COUNTEREXAMPLE-CANDIDATE on E (reaches for the more concrete "the claim is contradicted" framing instead of "the framing is refused").

The edge is real and triangulated. The palette rule suggested in the two-way comparison — *DUPLICATE for positive articulation, INTERNAL-REFUTATION GAP for negative refusal* — would have steered codex and gemini differently on B (toward operator's IRG) and possibly differently on E.

### Edge 2: ALIAS-RISK ↔ COUNTEREXAMPLE-CANDIDATE

| Claim | Operator | Codex | Gemini |
|---|---|---|---|
| C | ALIAS-RISK | COUNTEREXAMPLE-CANDIDATE | COUNTEREXAMPLE-CANDIDATE |

This edge fires on C. Two auditors (codex + gemini) chose COUNTEREXAMPLE-CANDIDATE; one auditor (operator) chose ALIAS-RISK. The edge persists in three-auditor view; the rule suggested in the two-way comparison — *primary ALIAS-RISK when conflation creates the contradiction, secondary COUNTEREXAMPLE-CANDIDATE only when corpus supplies a concrete defeating instance* — would have unified the verdicts toward ALIAS-RISK (codex and gemini both cited concrete corpus language refuting the side-effect-free assumption, but the conflation is the deeper issue).

### New edge: COUNTEREXAMPLE-CANDIDATE ↔ INTERNAL-REFUTATION GAP

Gemini's Claim E verdict introduces a third fuzzy edge that the two-way comparison did not surface:

- Operator: INTERNAL-REFUTATION GAP
- Codex: INTERNAL-REFUTATION GAP + COMPOSITION-GAP
- Gemini: COUNTEREXAMPLE-CANDIDATE

When the corpus contains a contemporaneous PEP that explicitly refutes a sufficiency claim, is that:
- *the corpus refusing the framing* (INTERNAL-REFUTATION GAP), or
- *the corpus containing a counterexample* (COUNTEREXAMPLE-CANDIDATE)?

Two auditors chose IRG; one chose CC. This is a real boundary; PEP 653's existence is both "corpus refuses sufficiency" AND "corpus contains specific contradictions." The palette doesn't currently sharpen this.

## Multi-class verdict tendency varies by model

| Auditor | Multi-class verdicts out of 5 |
|---|---|
| Operator | 2 (Claims B, C-revised) |
| Codex | 4 (Claims B, C, E) |
| Gemini | 0 |

Gemini Flash returned no multi-class verdicts. Codex returned the most. This is *model-temperament variance* on a methodological choice the bundle did not constrain (multi-class is permitted, not required). It affects label-count statistics but not structural-agreement statistics.

For palette-refinement: the multi-class question itself may need explicit rule. The bundle currently says "Multi-class verdicts ... are permitted when the claim genuinely exhibits more than one class" — but "genuinely" is operator-judgment territory.

## Operator-prior contamination assessment (three-auditor view)

Three-auditor view sharpens the operator-prior question:

- **Operator** had full pilot history; its verdicts could be shaped by prior method-internal context.
- **Codex** had only the bundle; no method history; reached COUNTEREXAMPLE-CANDIDATE + IRG on C.
- **Gemini** had only the bundle; no method history; reached COUNTEREXAMPLE-CANDIDATE on C.

Both blind auditors landed closer to each other than either landed to the operator on Claim C. This is mild evidence that *operator's ALIAS-RISK verdict on Claim C is operator-prior-shaped* — the operator's "look at it as a lexical fracture across three senses of order" reading is not blind-discoverable from the bundle alone. Two blind auditors found the *contradiction* (which the corpus directly supplies) before / instead of the *aliasing* (which requires recognizing three distinct senses of "first-to-match").

The portability claim's verdict-granularity component therefore looks specifically like *operator's ALIAS-RISK tendency may be partly operator-shaped* on Claim C. The structural-family detection (something wrong with this claim) is not operator-shaped.

## Recurrent instability sites — three-way

| Claim | Instability signature | Three-way pattern |
|---|---|---|
| C | Verdict locations vary (ALIAS-RISK, CC, CC+IRG); revisions happen | reproduced 3/3 |
| B | Verdict locations vary (IRG+AR, DUP+AR, DUP); one consistent label (DUPLICATE) appears in 2/3 | low instability — converging toward DUPLICATE |
| E | Verdict locations vary (IRG, IRG+CG, CC); IRG appears in 2/3 | low instability — converging toward IRG |

Only Claim C exhibits genuine three-way instability. B and E exhibit cross-auditor *labeling variance* but not destabilization of the underlying detection. **Claim C is the seismograph; B and E are calibration micro-jitters.**

## What does NOT change with the third auditor

- Method discrimination assessment: still RETAINS DISCRIMINATION (all three auditors said so).
- Verdict palette sufficiency: still YES (no LABEL-FAILUREs across three auditors).
- LAUNDERING-as-portability-evidence: strengthened (3/3 instead of 2/2).
- Claim D as highest-signal: confirmed (3/3 exact).
- Claim C as stress specimen: confirmed (3/3 detect, 0/3 converge).

## What does change

- The DUPLICATE/INTERNAL-REFUTATION GAP edge has a third datapoint with Gemini siding with Codex's DUPLICATE reading; operator's IRG reading looks more model-specific (Claude-specific?).
- A new fuzzy edge surfaces: COUNTEREXAMPLE-CANDIDATE ↔ INTERNAL-REFUTATION GAP (Gemini on Claim E).
- Multi-class verdict tendency varies by model in a way the palette doesn't regulate.
- Operator-prior contamination on Claim C is mildly supported (two blind auditors landed away from operator's stable verdict).

## Updated portability judgment

> **Portable at failure-family resolution; verdict-granularity is partly operator-sensitive AND partly model-sensitive.**

The two-way comparison's "portable with palette refinement" still holds, with one qualifier added: *some verdict-granularity variance is model-temperament, not method failure.* Gemini Flash's preference for single-label verdicts and its slight bias toward COUNTEREXAMPLE-CANDIDATE are model-shape features, not method-shape features.

The boundary between "method-instability" and "auditor-shape variance" needs to be drawn carefully. With three auditors:
- **Claim D LAUNDERING** is method-shape — three different models converged exactly.
- **Claim C three-way disagreement** is method-instability — three different models hit different labels at the same observation.
- **Claim B/E label variance** is auditor-shape — different verdict labels for what all three saw as the same kind of corpus-presence.

## Palette-refinement recommendations after triangulation

The two-way comparison's two recommendations stand and gain a third:

1. **DUPLICATE vs INTERNAL-REFUTATION GAP rule:** "Use DUPLICATE when corpus positively states the same mechanism; use INTERNAL-REFUTATION GAP when corpus contains constraint, caveat, or refusal that makes the claim's framing unstable or overbroad." Three auditors hit this boundary in three different ways; the rule would tighten.
2. **ALIAS-RISK vs COUNTEREXAMPLE-CANDIDATE composition rule:** "If contradiction arises because two distinct mechanisms were treated as one, classify primary as ALIAS-RISK and secondary as COUNTEREXAMPLE-CANDIDATE only if corpus supplies a concrete defeating instance." Two of three auditors hit this on Claim C; rule would converge them.
3. **New: COUNTEREXAMPLE-CANDIDATE vs INTERNAL-REFUTATION GAP rule:** "Use COUNTEREXAMPLE-CANDIDATE when the corpus contains a specific instance contradicting the claim. Use INTERNAL-REFUTATION GAP when the corpus contains a meta-level refusal of the claim's framing (e.g., a critique PEP, a 'do not interpret as' note, an explicit Rejected Ideas section)." This boundary fires only on Claim E in this comparison but is structurally important.

4. **(Provisional) Multi-class verdict rule:** "Auditors must list ALL applicable verdict classes that the corpus evidence supports; absence of multi-class on a multi-class-supportable claim is a methodological under-report." The rule would have prompted Gemini to list ALIAS-RISK alongside DUPLICATE on Claim B and IRG alongside CC on Claim E.

None of these refinements is executed by this comparison. They are recorded as the triangulated refinement candidates.

## Should Claim C be removed, split, or retained?

**Retain as stress specimen.** Three-way audit reproduced the destabilization 3/3 with zero convergence. That is exactly the high-information data a calibration artifact provides. Removing it would erase the most informative claim in the bundle. Splitting it would change the experiment. Keep it. It's now a triple-validated stress specimen, not just a double-validated one.

## What this DOES claim

- Method retains discrimination under blind audit by two independent model families (gpt-5.5 and gemini-2.5-flash).
- Verdict palette is sufficient across three auditors (no LABEL-FAILUREs).
- LAUNDERING is genuinely discriminative; three models converge exactly.
- Claim C destabilization is reproducible and structural, not noise.
- Two fuzzy palette edges are confirmed; a third surfaces with three-auditor coverage.

## What this does NOT claim

- Not proof of generalized portability. Three auditors on one corpus is three auditors on one corpus.
- Not adjudication. Where verdicts differ, neither this receipt nor the previous one declares a "correct" verdict.
- Not method revision. Palette refinement is *recommended for future work*, not executed here.
- Not promotion. The Track C external-portability pattern remains candidate-not-promoted in the method note.

## Next gates (named, not authorized)

1. **C3 replication on third corpus** using the same blind-bundle methodology. Independent of palette refinement.
2. **Palette refinement experiment**: refine DUPLICATE/INTERNAL-REFUTATION GAP and ALIAS-RISK/COUNTEREXAMPLE-CANDIDATE boundaries with the rules drafted above; re-run on the same bundle with all three auditors; measure whether agreement count goes up.
3. **Mechanical-aided variant for Claim C** specifically. Allow a Python interpreter; see whether the instability dissolves.
4. **Fourth blind auditor** (DeepSeek, Grok, or human) to test whether the codex+gemini convergence on COUNTEREXAMPLE-CANDIDATE for C is itself a non-Claude-family pattern.

## Curdling guard

This artifact operates at meta-comparison altitude only. No Lean implication. No new primitive minted. No alteration to any source receipt. The blind-auditor packet and bundle remain frozen. The codex and gemini receipts are preserved (raw + clean). Pilots #15, #16, the two-way comparison, and this three-way comparison are independent records.

## Cross-references

- [`blind-auditor-bundle-2026-06-07.md`](blind-auditor-bundle-2026-06-07.md) — self-contained packet
- [`blind-auditor-receipt-codex-2026-06-07.md`](blind-auditor-receipt-codex-2026-06-07.md) — codex receipt (clean)
- [`blind-auditor-receipt-gemini-2026-06-07.md`](blind-auditor-receipt-gemini-2026-06-07.md) — gemini receipt (clean)
- [`2026-06-06-portability-soft-corpus-pilot.md`](2026-06-06-portability-soft-corpus-pilot.md) (Pilot #15) — operator's audit
- [`2026-06-07-blind-audit-comparison.md`](2026-06-07-blind-audit-comparison.md) — two-way comparison
- [`method-note.md`](method-note.md) — operating procedure; not modified by this comparison

---

**No method change. No palette refinement executed. No promotion. Three-auditor evidence supports candidate portability at failure-family resolution with named palette-refinement recommendations; not proof.**
