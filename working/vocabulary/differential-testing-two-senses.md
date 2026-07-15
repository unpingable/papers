# "Differential testing" — two instruments sharing a name

**Filed:** 2026-06-06. **Status:** vocabulary disambiguation note. **NOT a primitive.** **NOT doctrine.** **NOT a generalized methodology.** Records the lexical fracture surfaced by Pilot #12 (WCM × Cedar Analysis).

## Why this note exists

Surfaced 2026-06-06 in [`../vector-mining/2026-06-06-witness-carrier-vs-cedar.md`](../vector-mining/2026-06-06-witness-carrier-vs-cedar.md) as the ALIAS-RISK leg of the multi-class verdict. Sibling to [`standing-three-senses.md`](standing-three-senses.md), [`custody-five-senses.md`](custody-five-senses.md), and [`receipt-and-witness-senses.md`](receipt-and-witness-senses.md).

The phrase "differential testing" carries two distinct instruments across the corpus's Cedar-adjacent context. Single-altitude reading can conflate them, importing build obligations or generalization claims from one sense into the other.

## The genus boundary

> *Correctness differential tests two implementations of the same semantics. Coverage differential compares the refusal envelopes of two different tools at different layers.*

Both produce comparison tables; both consume randomized inputs. The semantic content of "agreement" is incommensurable across the two senses. Same name, two instruments.

## Sense (a) — Cedar-internal correctness differential testing

**Where:** AWS Cedar's published methodology; mirrored in [`../tooltheory/admissibility-related-work-map.md`](../tooltheory/admissibility-related-work-map.md) § Adjacent methodological theft; cited in [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) § 7 guardrail #5; flagged in the substrate-gap header of `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` (lines 59–68).

**What it names:** A *correctness check across two implementations of the same semantics*. Generate many randomized inputs (valid and malformed); classify each through the Lean model and through the production substrate; treat divergence as model error, schema error, or implementation error. The two arms agree by construction at the spec level; divergence at the implementation level is a bug.

**What it does:** Tests that the production engine faithfully implements the formal model. The Lean side is the ground truth; the Rust side is the artifact under test. Disagreement is a defect, not a finding.

**What "differential" refers to:** The *difference between Lean output and Rust output* on the same input.

**Status in the corpus:** Named as the methodological template for the future BoundaryTransit witness-substrate bridge. Explicitly fenced: *"the harness is not built. Do not promote."* (WCM § 7 guardrail #5). Level 4 conformance work needs a concrete runtime target, an explicit formal-to-runtime mapping, and generated behavioral evidence. That target-dependence does not gate development of the formal contract, and citation alone would not establish conformance.

## Sense (b) — Vector-mining coverage differential

**Where:** [`../vector-mining/method-note.md`](../vector-mining/method-note.md) operating procedure; the framing under which Pilot #12 was authorized; a candidate verdict-pattern across pilots that compare a corpus artifact against an adjacent external tool.

**What it names:** A *coverage check across two different tools at different layers*. Take a refusal set produced by one tool (e.g., WCM § 6's seven refusal rows); ask whether the second tool (e.g., Cedar Analysis under its policy semantics) can encode each refusal, partly encode it, encode it only via a known gambit, or not encode it at all. Classify the cells; record where each tool's envelope holds and where it does not.

**What it does:** Maps the relationship between two non-identical tools. Disagreement is the *point*: the comparison shows which refusals each tool owns and which it routes elsewhere. The output is a verdict (DUPLICATE, ALIAS-RISK, INTERNAL-REFUTATION GAP, etc.), not a defect report.

**What "differential" refers to:** The *envelope difference between Tool A and Tool B* across their respective semantics.

**Status in the corpus:** A pattern used by vector-mining pilots when the audit target is an adjacent external neighbor; produces classified receipts per [`../vector-mining/method-note.md`](../vector-mining/method-note.md). Not a generalized methodology — the pattern is *the audit shape*, not *the harness*.

## The cross-sense rule

> **These are two instruments sharing a name, not one generalized primitive.**

A claim that "WCM × Cedar differential testing" requires the Cedar-style Lean↔Rust harness imports sense (a) into a sense (b) audit. The two instruments do not generalize to a common parent without losing what makes each useful.

Specifically:

- **Sense (a) requires a shared spec.** No shared spec → no notion of agreement → the instrument has no ground truth axis.
- **Sense (b) requires distinct layers / different semantics.** A shared spec would collapse the audit into either a correctness check or a tautology.

The two are not points on a spectrum; they are different machines that happen to share a name. The corpus uses both, separately.

## What this note is NOT

- **NOT a new instrument.** No new audit pattern minted; the two existing senses are enumerated, not extended.
- **NOT a generalization claim.** The note refuses the framing that the two senses share a common parent.
- **NOT authorization to build the Level 4 harness.** WCM § 7 guardrail #5 still governs sense (a); curdling guard intact.
- **NOT a Lean target.** No formalization implied at either altitude.
- **NOT a paper-candidate.** Glossary entry only.

## Cross-references

- [`standing-three-senses.md`](standing-three-senses.md), [`custody-five-senses.md`](custody-five-senses.md), [`receipt-and-witness-senses.md`](receipt-and-witness-senses.md) — sibling disambiguation notes.
- [`../vector-mining/2026-06-06-witness-carrier-vs-cedar.md`](../vector-mining/2026-06-06-witness-carrier-vs-cedar.md) — Pilot #12; the ALIAS-RISK forcing example.
- [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) § 7 guardrail #5 — sense (a) corpus anchor.
- [`../tooltheory/admissibility-related-work-map.md`](../tooltheory/admissibility-related-work-map.md) § Adjacent methodological theft — sense (a) methodology source.
- [`../vector-mining/method-note.md`](../vector-mining/method-note.md) — sense (b) operating procedure context.
- [`../admissibility-as-pre-authorization-layer.md`](../admissibility-as-pre-authorization-layer.md) § Falsifier — names the *reification gambit* that pilot #12 demonstrated in the sense-(b) row-by-row.
- `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` lines 50–75 — sense (a) substrate-gap header.
