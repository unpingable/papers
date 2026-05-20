# Affective Coupling / Sentiment Invariance

**Status:** Candidate diagnostic pattern; not promoted to primitive; not Lean-staged.
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

The clean separation between what the runtime monitors and what a (future) formal kernel would say:

### Runtime monitor — Python / Rust / notebook / graph code

- Measures `H(R)`, `H(R|S)`, `I(S;R)`, response invariance via distribution similarity
- Computes author-conditioned residuals
- Detects affective capture via lagged mutual information
- Emits state labels per a windowed observation
- Lives wherever the social-telemetry consumer needs it (labelwatch, driftwatch, custom dashboards)

DeepSeek 2026-05-20 produced a reasonable operational sketch (`AffectiveCouplingMonitor` class with `numpy` + `scipy.stats.entropy`). Useful as starting shape; not preserved here verbatim because it's runtime infrastructure, not doctrine.

### Lean kernel — NOT staged

If a Lean kernel eventually lands, it should:

- **Abstract over** the measures, not formalize entropy in `Rat` (logarithms don't live comfortably there; would force mathlib real-analysis tax forms).
- **Prove structural facts about classification semantics**, not certify social pathology from thresholds.
- **Stay small.** Shape sketch only, not authorized to build:

```lean
structure CouplingSurface where
  inputCoupling      : Rat  -- abstract; I(S;R)
  roomMemoryCoupling : Rat  -- abstract; I(R_prev;R)
  authorCoupling     : Rat  -- abstract; I(A;R)
  meanResponseValence : Rat

def responseInvariant (c : CouplingSurface) : Prop := c.inputCoupling = 0
def negativeBasin    (c : CouplingSurface) : Prop := c.meanResponseValence < 0
def toxicBasin       (c : CouplingSurface) : Prop := responseInvariant c ∧ negativeBasin c
def affectiveCapture (c : CouplingSurface) : Prop := c.roomMemoryCoupling > c.inputCoupling
def standingCollapse (c : CouplingSurface) : Prop := c.authorCoupling > c.inputCoupling
```

Theorems would be small structural unfoldings (e.g., `toxic_basin_invariant : toxicBasin c → responseInvariant c`). The computation lives outside; Lean would guard only the classification semantics.

**Do not stage yet.** No live tool consumer; no recurrent specimen base; the abstraction would be premature scaffolding. Per the kernel-overlap-audit discipline, this is exactly the kind of "looks formal, isn't earning rent" candidate that the AWP-audit precedent rejected.

## Constellation lineage

| Neighbor | Relationship |
| --- | --- |
| **WitnessInvariance** (Lean kernel + primitive) | Inverse failure mode. WIF: claimed-encapsulated witness *moves* when it shouldn't. Toxic basin: response *doesn't move* when conditional dependence is the health signal. Same shape (witness output vs declared-relevant variables), opposite direction. |
| **AxisSkew** (Lean kernel + primitive, filed 2026-05-20) | Different shape. AxisSkew classifies *direction* of prior-vs-observed mismatch on an ordered surface. Affective coupling classifies *strength* of input-vs-response dependence with sub-classifications. Composable but distinct. |
| **AWP §3.F vocabulary convergence** | Lexical version of input-decoupled response. The monitor speaks the defendant's language regardless of evidence convergence — that's response affect (lexical register) invariant to input affect (claim content). |
| **labelwatch / driftwatch** | Live wires. The custodial labeling surfaces are exactly where coupling-vs-decoupling becomes operationally measurable in the social-telemetry register. |
| **Signal authority** (candidate primitive) | Adjacent at the null-laundering axis. Signal authority: silence ≠ revocation. Affective coupling: invariant response ≠ legitimate response — the absence of conditional variation is its own signal, not neutrality. |

## Promotion gates

This stays as a tooltheory note until at least one of:

- A live labelwatch / driftwatch consumer needs the diagnostic surface and forces a concrete schema (then: promote to spec).
- A second non-social-media domain exhibits the same input-decoupled-response failure cleanly (then: candidate primitive with kind=Axis or Attractor).
- A bridge theorem composes with `WitnessInvariance` (showing the inverse-direction symmetry formally) — would justify Lean kernel staging.

Until then: tool doctrine, not implementation invariant.

## Failure mode the note guards against

The Lean kernel sketch above is **suspiciously formal-looking**. The temptation to immediately implement `AffectiveCoupling.lean` is the second-most-recent instance of the failure pattern memory `feedback-kernel-overlap-audit` names: *appearance of formality without earned residue*. Don't.

The Python kernel is **suspiciously runnable**. The temptation to ship `AffectiveCouplingMonitor` as a labelwatch dependency before the diagnostic surface has been stress-tested against actual social data is the operational counterpart of the same trap.

Both temptations resolve the same way: hold at note, wait for the consumer to surface a forcing case.

## Provenance and meta-note

Generated 2026-05-20 from a cross-model session: user prompted "you need affective coupling prolly" to a DeepSeek-tier model, which produced (a) a competent Python operational sketch interpreting "lean" as "minimal Python", then (b) on correction, a fake-Lean sketch with `Rat`-based entropy and threshold predicates standing in for theorems. ChatGPT-side critique surfaced the two-layer split (runtime vs classification semantics) and the keeper lines.

**Meta-recognition the note preserves**, useful as a recognition event but *not* doctrine: the conversation about affective coupling itself exhibited affective-coupling failure. DeepSeek's response affect (interpret "lean" as "minimal") was invariant to the input affect (context: theorem-prover-heavy repo with `LeanProofs/` everywhere). Response was conditioned on lexical prior, not on input.

Affective coupling failure, observed in the wild. Filed without ceremony.
