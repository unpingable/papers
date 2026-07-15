# Affective Coupling / Sentiment Invariance

**Status:** Candidate diagnostic pattern; not promoted to primitive. A checked formalization-leading classification slice now lives at `~/git/lean/LeanProofs/Scratch/AffectiveCouplingClassification.lean`; it is unwired and not imported by `LeanProofs.lean`.
**Filed:** 2026-05-20
**Tool relevance:** labelwatch, driftwatch, social-telemetry layer; possible future Nightshift cross-pointer.
**Promotion ladder position:** working fragment / tool doctrine note (per `tooltheory/README.md`).

## Core distinction

> A negative room is not necessarily toxic. A room becomes structurally toxic when response affect becomes invariant to post affect, or when author/cohort explains response better than content.

Sentiment is the *output*. Coupling is the *health signal*. The diagnostic surface measures whether response depends on what was actually said, or whether response has detached from input and is being driven by something else (room memory, author identity, cohort affiliation).

## Keepers

> **Toxicity begins when affect stops being conditional on input.**

> **Sentiment is the output. Coupling is the health signal.**

> **Affective capture: the room responds more to its previous affective state than to the current object.**

The third one is the social-media version of an unstable control loop eating its own telemetry.

## Warning

Do **not** collapse this into sentiment analysis. Sentiment is a measurement channel; coupling is the structural question. A monitor that reports only mean valence and calls a negative room "toxic" has done the dashboard version of the failure it claims to detect.

## Diagnostic surface

Six measurements, runtime-side:

| Measurement | What it answers |
| --- | --- |
| Mean response valence | Is the room negative on net? *(necessary but not sufficient for toxicity)* |
| Response entropy `H(R)` | Is response diverse or collapsing? |
| Conditional response entropy `H(R|S)` | Does response depend on the post? |
| Coupling `I(S;R)` | How much does input determine response? |
| Response invariance across `P(R|S)` | Does response distribution change with post sentiment? |
| Author/cohort residual | Does author explain response better than content does? |
| Affective capture `I(Rₜ₋₁; Rₜ) > I(Sₜ; Rₜ)` | Does prior response predict current response better than input does? |

Useful state labels: *calibrated* / *congruent distress* / *toxic basin* / *pile-on* / *chaotic fragmentation* / *standing collapse* / *affective capture*.

## Two-layer split

The clean separation between what a runtime monitor measures and what the checked formal classification slice says:

### Runtime monitor — Python / Rust / notebook / graph code

- Measures `H(R)`, `H(R|S)`, `I(S;R)`, response invariance via distribution similarity
- Computes author-conditioned residuals
- Detects affective capture via lagged mutual information
- Emits state labels per a windowed observation
- Lives wherever the social-telemetry consumer needs it (labelwatch, driftwatch, custom dashboards)

DeepSeek 2026-05-20 produced a reasonable operational sketch (`AffectiveCouplingMonitor` class with `numpy` + `scipy.stats.entropy`). Useful as starting shape; not preserved here verbatim because it's runtime infrastructure, not doctrine.

### Lean classification slice — checked Scratch

The original `Rat`/exact-zero sketch was useful as a warning but was not the
artifact that survived formal contact. The checked Scratch module:

- treats all numeric fields as externally supplied diagnostic summaries rather
  than pretending Lean calculated entropy or causal influence;
- parameterizes the declared input-coupling threshold instead of equating
  invariance with exact zero;
- names the conjunction `ToxicitySignatureAt`, not `Toxic`, and makes no causal
  claim about a room, cohort, author, or response process;
- proves that negative mean valence alone does not determine the signature,
  with a positive inhabitant and paired equal-valence/opposite-verdict worlds.

The computation remains runtime-side. The formal classification semantics lead
any later implementation, which must map its measurements and thresholds to the
abstract fields and supply its own conformance evidence.

## Constellation lineage

| Neighbor | Relationship |
| --- | --- |
| **WitnessInvariance** (Lean kernel + primitive) | Inverse failure mode. WIF: claimed-encapsulated witness *moves* when it shouldn't. Toxic basin: response *doesn't move* when conditional dependence is the health signal. Same shape (witness output vs declared-relevant variables), opposite direction. |
| **AxisSkew** (Lean kernel + primitive, filed 2026-05-20) | Different shape. AxisSkew classifies *direction* of prior-vs-observed mismatch on an ordered surface. Affective coupling classifies *strength* of input-vs-response dependence with sub-classifications. Composable but distinct. |
| **AWP §3.F vocabulary convergence** | Lexical version of input-decoupled response. The monitor speaks the defendant's language regardless of evidence convergence — that's response affect (lexical register) invariant to input affect (claim content). |
| **labelwatch / driftwatch** | Live wires. The custodial labeling surfaces are exactly where coupling-vs-decoupling becomes operationally measurable in the social-telemetry register. |
| **Signal authority** (candidate primitive) | Adjacent at the null-laundering axis. Signal authority: silence ≠ revocation. Affective coupling: invariant response ≠ legitimate response — the absence of conditional variation is its own signal, not neutrality. |

## Promotion and correspondence

The doctrine remains a tooltheory note. These events can affect doctrine or runtime disposition:

- A live labelwatch / driftwatch integration supplies a concrete measurement mapping (then: runtime spec/correspondence review).
- A second non-social-media domain exhibits the same input-decoupled-response failure cleanly (then: candidate-primitive review with kind=Axis or Attractor).
- A nontrivial bridge theorem composes with `WitnessInvariance` (showing the inverse-direction symmetry formally) — then extend formal work after overlap review.

Until then: candidate doctrine plus checked Scratch classification semantics, not an implementation invariant or public theorem surface.

## Failure mode the note guards against

The original Lean-shaped sketch was **suspiciously formal-looking**. Formal contact paid for itself by replacing its exact-zero and causal-looking labels with the narrower thresholded classification result. Do not expand that checked slice without a distinct theorem delta and overlap audit.

The Python kernel is **suspiciously runnable**. The temptation to ship `AffectiveCouplingMonitor` as a labelwatch dependency before the diagnostic surface has been stress-tested against actual social data is the operational counterpart of the same trap.

The formal and runtime temptations resolve differently: formalize a coherent bounded proposition first; implement only against an explicit measurement mapping and evidence plan. Neither artifact promotes the other automatically.

## Provenance and meta-note

Generated 2026-05-20 from a cross-model session: user prompted "you need affective coupling prolly" to a DeepSeek-tier model, which produced (a) a competent Python operational sketch interpreting "lean" as "minimal Python", then (b) on correction, a fake-Lean sketch with `Rat`-based entropy and threshold predicates standing in for theorems. ChatGPT-side critique surfaced the two-layer split (runtime vs classification semantics) and the keeper lines.

**Meta-recognition the note preserves**, useful as a recognition event but *not* doctrine: the conversation about affective coupling itself exhibited affective-coupling failure. DeepSeek's response affect (interpret "lean" as "minimal") was invariant to the input affect (context: theorem-prover-heavy repo with `LeanProofs/` everywhere). Response was conditioned on lexical prior, not on input.

Affective coupling failure, observed in the wild. Filed without ceremony.
