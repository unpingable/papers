# Consolidation-denial — formal sketch

**Status (updated 2026-07-14):** Source note for the checked Scratch module `~/git/lean/LeanProofs/Scratch/ConsolidationController.lean`. The extracted module compiles under Lean 4.29 and closes the mode-specific buffer invariant without `sorry`. It is not imported by `LeanProofs.lean`, not a public kernel, not a paper figure, and not evidence that any runtime implements the controller.

**Companion to:** [`consolidation-denial.md`](consolidation-denial.md) — the working note with the wedge, keepers, specimens, and anti-overreach framing. This file holds the equations and the Lean draft that fell out of multi-model iteration.

**Scope fence:** the model below is a *minimal viable controller sketch* for the failure mode named in the companion note. It is not a new public kernel predicate. Formalization is allowed to lead later implementation; the Scratch file fixes only controller state, transition, and conditional boundedness. Promotion, runtime mapping, and conformance remain separate.

---

## Three clocks

Three rates govern the dynamics. Discrete-time, non-negative reals.

| Clock | Symbol | Meaning |
|---|---|---|
| Interaction | λ_ext | external arrival rate (exogenous) |
| Admission | a(t) | controller-gated rate at which arrivals enter the active context stream; 0 ≤ a(t) ≤ λ_ext |
| Settlement | μ | per-unit-buffer audit rate during consolidation; 0 ≤ μ |
| Decay | δ | per-step fractional decay of unsettled buffer; 0 ≤ δ ≤ 1 |
| Focus | f(t) | foreground capacity allocation; 0 ≤ f(t) ≤ 1 |

The interrupt forces `f = 0, a = 0`. Arrivals keep arriving externally; they do not become context.

## Four stocks

| Stock | Meaning |
|---|---|
| B(t) | unsettled buffer mass |
| K(t) | durable consolidated structure |
| X(t) | audited demotion (receipt-bearing discard) |
| R(t) | epistemic rot (unrecoverable loss from decay) |

Settlement quality `η ∈ [0,1]`: fraction of audited buffer that becomes K. Remainder `(1-η)` becomes X — **not R.**

### Operating phase (consolidation-denied; f ≈ 1, a > 0)

```
Ḃ = a(t)       − δ B
Ṙ = δ B
Ḳ = 0
Ẋ = 0
```

Buffer grows from admission and shrinks by decay. Decay produces rot. No durable knowledge accumulates while f ≈ 1.

### Operating phase with slack (0 < f < 1, a > 0)

Background settlement runs at fractional rate `(1 - f) μ`:

```
Ḃ = a(t)       − (1-f) μ B  − δ B
Ṙ = δ B
Ḳ = η (1-f) μ B
Ẋ = (1-η)(1-f) μ B
```

**Note on the rot term in the slack model:** the (1-η) fraction of the *background-audited* buffer is *audited demotion*, not rot. It belongs in X, not R. Rot accrues only from the `δ B` decay term. The displayed equations now encode that correction directly.

### Consolidation phase (interrupt active; f = 0, a = 0)

```
Ḃ = − μ B  − δ B
Ḳ = η μ B
Ẋ = (1-η) μ B
Ṙ = δ B
```

Buffer drains through two sinks: the *good* sink (K) and the *audited* sink (X). Decay continues — even during consolidation, unsettled material still decays at rate δ while waiting for the audit pass.

## Supervisor — Schmitt trigger on a composite health index

The supervisor maintains a discrete mode `q ∈ {Op, Con}` and gates on a composite trigger:

```
H_trigger(t) = B(t) + α · r_window(t) + β · A(t)
```

- r_window(t) = recent rot rate (non-monotone; rolling window).
- A(t) = age / authority risk of unsettled claims.
- α, β > 0.

Transitions:
- `Op → Con` when `H_trigger ≥ H_high`.
- `Con → Op` when `H_trigger ≤ H_low`, where `H_low < H_high` (hysteresis).

**Why r_window and not R_cum:** R_cum monotonically increases. If release depended on R_cum, the controller could eventually become permanently ineligible for release. A rolling pressure measure removes that monotone obstruction, but does **not** by itself prove release or liveness; those require additional hypotheses about decay of the window, admissions, and supervisor evolution.

## Mode-specific safety invariant

The naive invariant `B ≤ B_high + λ_int` is **false** as a global bound (counterexample: δ = 0, B at the bound, another admission overshoots). The correct invariant is mode-specific:

```
mode_safe(s) ≜
  if s.mode = Op  then s.B ≤ B_high
  if s.mode = Con then s.B ≤ B_high + λ_max
```

Where `λ_max` is the per-step admission bound. The Schmitt trigger ensures:
- In Op, buffer is bounded by `B_high` *before* each step; one step can overshoot by at most `λ_max`; if it crosses `B_high`, mode flips to Con, where the Con invariant trivially holds.
- In Con, buffer only decreases (settlement + decay both drain it). Mode flips back to Op only when `B ≤ B_low`, restoring the Op invariant since `B_low < B_high`.

## Lean extraction status

The original 2026-05-25 inline draft ended in `sorry` and used proof arguments
whose semantic domains were not carried by their types. It is retained in git
history; the authoritative formal artifact is now:

```text
~/git/lean/LeanProofs/Scratch/ConsolidationController.lean
```

The extracted file:

- replaces the loose clock/admission arguments with `ControllerConfig` and a
  proof-bearing `Admission` structure;
- makes the real-valued transition explicitly noncomputable;
- closes `step_preserves_mode_safe` by mode and Schmitt-guard case analysis;
- retains a nonnegative buffer clamp and the one-admission-cap overshoot bound;
- states no liveness, eventual-release, or runtime-conformance theorem.

Remaining scope, not proof debt:

- K, X, and R are not modeled; the checked invariant is on B alone.
- Focus `f` and the composite health index are not in the checked slice.
- The theorem is conditional invariant preservation from an already-safe state,
  not a claim that every run reaches, remains in, or exits consolidation.

## Cybernetic commentary (compressed, pruned of the lab coat)

Useful framing without overclaim:

- **Negative feedback:** the interrupt closes a feedback loop that stabilizes an otherwise runaway positive-feedback process (prompts begetting unresolvable context).
- **Requisite variety (Ashby):** the supervisor's variety — at minimum, "halt admission" — matches the variety of the adversary's interaction stream. The interrupt is a variety attenuator: collapses infinite prompt sequences into a forced pause.
- **Algedonic signal (Beer):** the interrupt is a pain signal forcing re-synchronization between the operational unit and its consolidation metasystem. The composite trigger H is the algedonic threshold.
- **Technique (Ellul):** that a forced *technological* interrupt is needed to carve out a non-functional contemplative phase is the signature failure mode of always-on interfaces. We build a circuit-breaker to defend the slack the interface eliminated.

These are *framings*, not derivations. Useful for design-rationale prose; not load-bearing for any theorem.

## Provenance

- Three-clock framing (interaction / settlement / decay), Schmitt-trigger architecture, first Lean draft: **DeepSeek**, 2026-05-25, after operator prewarm with cyberneticist framing.
- Corrections (decay does not pay debt → split stocks; audited demotion ≠ rot; r_window vs R_cum; ghost-Lean fix for missing `mode` field; mode-specific invariant; λ_ext vs a(t) admission control; slack as middle term): **ChatGPT**, same session.
- Anti-overreach framing + relocation to `tooltheory/` + this file's scratch posture: **ChatGPT**, same session.
- Filing: **claude-code**, same session, with the working note + formal sketch separated to keep the load-bearing handle clear of the elaborated mechanism.

## What survives if any of this gets pulled forward

Most likely paths to actual use:

1. **Design rationale for Nightshift / agent_gov / NQ / Continuity** — name the Schmitt-trigger architecture in spec language so the existing tools' refusal-during-uncertain-state behavior reads as a known shape. Lightweight; high value.
2. **A test harness for agent sessions** — the Session A vs Session B comparison in the companion note. Cheap and falsifiable.
3. **A receipt-format extension** — X (audited demotion) deserves a receipt distinct from K (durable structure). Continuity might already do this; if not, the X/K distinction is a candidate spec gap.
4. **A talk / Substack piece** — *not yet.* No serial public surface here until the specimen catalog grows past one.

What does NOT follow from the checked Scratch module:
- promotion into the imported `Admissibility/` surface;
- a new public admissibility predicate;
- a runtime implementation or conformance claim;
- a paper.
