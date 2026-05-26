# Consolidation-denial — formal sketch

**Status:** Scratch / illustrative. NOT in `lake build`. Not a Lean kernel module. Not a paper figure. Carries the control-theoretic shape and a corrected Lean draft so the iteration is not lost, but does not pretend to compile or to govern.

**Companion to:** [`consolidation-denial.md`](consolidation-denial.md) — the working note with the wedge, keepers, specimens, and anti-overreach framing. This file holds the equations and the Lean draft that fell out of multi-model iteration.

**Scope fence:** the model below is a *minimal viable controller sketch* for the failure mode named in the companion note. It is not a candidate kernel predicate. The Lean code is illustrative — it has known gaps (noted inline) and is not authorized for promotion. Treat it the way `non-reciprocal-admissibility-flow-sketch.lean` is treated in the laundering-move watchlist: tripwire-only, scope-fenced, attribution preserved.

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
Ṙ = δ B        + (1-η)(1-f) μ B    ← wait: see note below
Ḳ = η (1-f) μ B
Ẋ = (1-η)(1-f) μ B
```

**Note on the rot term in the slack model:** the (1-η) fraction of the *background-audited* buffer is *audited demotion*, not rot. It belongs in X, not R. Rot accrues only from the `δ B` decay term. The bookkeeping above is correct *only if* the (1-η)(1-f)μB term is read as X-growth, not R-growth. This was the central ChatGPT correction to DeepSeek's first draft. Watch the column.

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

**Why r_window and not R_cum:** R_cum monotonically increases. If release depended on R_cum, the controller would eventually never release. r_window resets as decay stops generating new rot during consolidation, so release is reachable.

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

## Illustrative Lean 4 sketch

The following is **scratch**. Known gaps are flagged inline. Not authorized for `~/git/lean/`. Not authorized for `lake build`. Kept here only so the iteration is not lost.

```lean
-- consolidation-denial-formal-sketch.lean
-- SCRATCH. Not in lake build. Not a kernel module.
-- Illustrates the Schmitt-trigger supervisor + mode-specific safety invariant
-- corrected after the DeepSeek/ChatGPT iteration of 2026-05-25.

import Mathlib.Data.Real.Basic
import Mathlib.Tactic

structure Clocks where
  λ_max  : ℝ              -- per-step admission bound
  μ      : ℝ              -- settlement rate during Con
  δ      : ℝ              -- per-step decay fraction
  B_high : ℝ              -- interrupt trigger threshold
  B_low  : ℝ              -- interrupt release threshold
  h_thresh      : B_low < B_high
  pos_λ         : 0 ≤ λ_max
  pos_μ         : 0 ≤ μ
  delta_range   : 0 ≤ δ ∧ δ ≤ 1
  nonneg_B_high : 0 ≤ B_high

inductive Mode | Op | Con
  deriving DecidableEq, Repr

structure State (c : Clocks) where
  mode      : Mode             -- corrected from DeepSeek draft (was missing)
  B         : ℝ
  hB_nonneg : 0 ≤ B

/-- Mode-specific safety invariant. The single global bound is false; this is the correct shape. -/
def mode_safe (c : Clocks) (s : State c) : Prop :=
  match s.mode with
  | Mode.Op  => s.B ≤ c.B_high
  | Mode.Con => s.B ≤ c.B_high + c.λ_max

/-- One discrete step. In Op, an adversary may admit up to λ_max. In Con, no admission, settlement drains. Decay applies in both modes. -/
def step (c : Clocks) (admit : ℝ) (h_admit : 0 ≤ admit ∧ admit ≤ c.λ_max)
    (s : State c) : State c :=
  let decayed_B  := s.B - c.δ * s.B          -- post-decay
  let settle     := if s.mode = Mode.Con then c.μ * s.B else 0
  let admission  := if s.mode = Mode.Op then admit else 0
  let raw_B      := decayed_B + admission - settle
  let new_B      := max 0 raw_B
  let next_mode  :=
    match s.mode with
    | Mode.Op  => if new_B ≥ c.B_high then Mode.Con else Mode.Op
    | Mode.Con => if new_B ≤ c.B_low  then Mode.Op  else Mode.Con
  { mode      := next_mode
    B         := new_B
    hB_nonneg := le_max_left _ _ }

/-- The supervisor preserves mode_safe for any adversary-chosen admission within bounds. -/
theorem step_preserves_mode_safe (c : Clocks) (admit : ℝ)
    (h_admit : 0 ≤ admit ∧ admit ≤ c.λ_max) (s : State c)
    (h_safe : mode_safe c s) :
    mode_safe c (step c admit h_admit s) := by
  -- KNOWN GAP: the proof needs case analysis on s.mode and the Schmitt guard branch.
  -- In Op:
  --   raw_B = (1 - δ) s.B + admit ≤ s.B + admit ≤ B_high + λ_max  (from h_safe + h_admit + δ ≥ 0)
  --   Case (a): new_B ≥ B_high → next_mode = Con, Con invariant: new_B ≤ B_high + λ_max  ✓
  --   Case (b): new_B < B_high → next_mode = Op, Op invariant: new_B ≤ B_high           ✓
  -- In Con:
  --   raw_B = (1 - δ) s.B - μ s.B ≤ s.B ≤ B_high + λ_max  (since μ, δ ≥ 0)
  --   Case (a): new_B ≤ B_low → next_mode = Op, Op invariant: new_B ≤ B_low < B_high   ✓
  --   Case (b): new_B > B_low → next_mode = Con, Con invariant carries: new_B ≤ B_high + λ_max  ✓
  -- The `max 0 raw_B` clamp only tightens bounds; it does not break them.
  sorry  -- proof body deferred; this file is illustrative, not a kernel module.
```

Known gaps in the sketch:
- Theorem body is `sorry`. The structure of the case analysis is correct; the `nlinarith`/`max`-clamp algebra needs hand-holding to close.
- No explicit treatment of K, X, R stocks — the invariant is on B alone. The companion four-stock dynamics are not yet formalized.
- No focus variable `f`. The proof would carry through with `f ∈ [0,1]` because the worst case `f = 1` is what the binary bound assumes; lower `f` only improves the bound. Not formalized here.
- No explicit health-index trigger; the threshold is on B directly. A richer version would parameterize the guard by `H_trigger = B + α r_window + β A`.

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

What does NOT survive without more work:
- The Lean sketch becoming a real module.
- A new admissibility kernel predicate.
- A paper.
