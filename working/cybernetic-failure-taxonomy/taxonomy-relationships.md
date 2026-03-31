# Taxonomy Relationships: First-Pass Sketch

**Status:** Rough sketch. Testing whether the 15 domains have internal structure or are actually flat.
**Finding:** They're not flat. There are root failures, pipelines, and at least one composite that should probably be demoted.

---

## Candidate Root Failures

Three domains that sit upstream of others and don't have obvious parents:

| Domain | Why it's upstream |
|---|---|
| **Δn (namespace)** | If you can't name the failure, you can't draw boundaries around it (→ Δb), can't observe it as a category (→ Δo), can't detect model drift against it (→ Δm). Δn is the meta-failure. |
| **Δp (polarity inversion)** | If the reward sign is flipped, every downstream control decision is wrong in a way that *looks correct* to the controller. Corrupts gain (→ Δg), recursion (→ Δr), and signal (→ Δs) simultaneously. |
| **Δe (energy deficit)** | Knows what to do, can't do it. This isn't caused by other failures — it's a constraint that *prevents correction* of other failures. Turns recoverable failures into permanent ones (→ Δh). |

These three are different *kinds* of root:
- **Δn** = can't frame the problem
- **Δp** = the frame is inverted
- **Δe** = can frame it fine, lack the surplus to act

---

## Pipelines

Arrows mean "commonly causes or enables."

### The Framing Pipeline
```
Δn (can't name it) → Δb (wrong boundary) → Δc (consequences detach)
```
Can't name the thing → draw the perimeter wrong → consequences route outside the perimeter → authority and consequence separate. This is the pipeline that makes institutional failures feel "mysterious" — each step is invisible from inside.

### The Perception-to-Model Pipeline
```
Δs (signal corruption) → Δm (model drift) → Δg (gain mismatch)
```
Distorted signal → internal model diverges → controller is too hot or too cold for reality. Classic Goodhart path: the metric is gamed (Δs), the model trusts the metric (Δm), the response is calibrated to the fake signal (Δg).

### The Observation Pipeline
```
Δb (wrong boundary) → Δo (observability failure)
```
If the boundary excludes the causal substrate, your observability is pointed at the wrong thing. You *can* see — you're just looking in the wrong place. This is different from Δo alone (sensor is broken) — it's Δo *induced by* Δb.

### The Authority Pipeline
```
Δw (write-authority drift) → Δc (consequence detachment) → Δh (hysteresis)
```
Temporary exception gains permanent authority → authority and consequence separate → the separation normalizes and can't be reversed. This is the Paper 18 → Paper 19 pipeline, basically.

### The Recursion Pipeline
```
Δp (polarity inversion) → Δr (recursion capture)
```
Inverted reward → feedback loop feeds on its own outputs because the signal saying "stop" now says "more." This is why Δr is so hard to break: the loop is self-reinforcing *and* the reward signal confirms the reinforcement.

### The Exhaustion Pipeline
```
Δe (energy deficit) → Δh (hysteresis)
```
System knows what to do but lacks surplus → can't return to baseline even after trigger is removed → stuck. This is the maintenance trap loop: the failure consumes the resources needed to correct the failure.

---

## Cross-Cutting Relationships (Not Pipelines)

### Δb ↔ Δn (entangled, not directional)
Sometimes Δn → Δb (can't name it, so can't draw the boundary). Sometimes Δb → Δn (wrong boundary excludes the thing, so it never gets named). They can cause each other. This is the entanglement you noticed.

### Δx (scale inversion) as amplifier
Δx isn't caused by a single upstream failure — it's what happens when *any* control intervention crosses a scale boundary. Stabilize one scale, destabilize another. It amplifies whatever failure it touches. More of a property of multi-scale systems than a standalone failure mode.

### Δk (coupling mismatch) as independent
Δk doesn't have strong parents or children in this map. It's genuinely about the engineering of coupling strength, not about framing or perception. This supports the "Δk is an engineering problem, Δb is a framing problem" distinction from the Δb spike.

### Δa (actuation mismatch) as independent
Similar to Δk — it's about having the wrong tools, not about upstream framing failures. You diagnosed correctly, you just can't intervene at the right layer. Genuinely operational.

---

## Candidates for Demotion or Merger

### Δm (model drift) — possible demotion to symptom
Model drift is almost always *caused by* something upstream: signal corruption (Δs), namespace failure (Δn), observability failure (Δo), or boundary error (Δb). It's rare for a model to drift in isolation. It might be better treated as a **symptom** of perception/framing failures than as a peer domain.

Counter-argument: the model can drift through pure time pressure (Paper 7's Δt-constrained inference) even when signals and naming are fine. So it has at least one independent cause. Keep it, but note its dependency.

### Δi (Grok's identity failure) — confirmed composite
Δi = Δn (can't name what you are) + Δr (recursive self-modification) + Δw (authority over self mutates). No independent residue once those three are accounted for. Don't promote.

---

## Tentative Layer Map

Not strict tiers — more like "how far upstream."

```
ROOTS (upstream of most things)
  Δn — namespace failure (can't name it)
  Δp — polarity inversion (reward sign flipped)
  Δe — energy deficit (can't act on knowledge)

FRAMING / PERCEPTION (downstream of roots, upstream of control)
  Δb — boundary error (wrong perimeter)
  Δo — observability failure (can't see state)
  Δs — signal corruption (distorted channel)
  Δm — model drift (internal model diverges) [often downstream of Δs, Δo, Δn]

CONTROL (operational layer)
  Δg — gain mismatch (too hot / too cold)
  Δa — actuation mismatch (wrong tool / wrong layer)
  Δk — coupling mismatch (too tight / too loose)

GOVERNANCE (authority layer)
  Δw — write-authority drift (temporary → permanent)
  Δc — consequence detachment (authority ≠ consequence)

EMERGENT / SCALE
  Δx — scale inversion (cross-scale destabilization)
  Δr — recursion capture (self-feeding loops)

PERSISTENCE
  Δh — hysteresis (can't return after trigger removed)
```

Δh sits at the bottom because it's where *any* uncorrected failure ends up. It's the default destination: if you don't fix it, it normalizes.

---

## What This Suggests

1. **The taxonomy has real structure**, not just 15 peers. Roots, pipelines, and a persistence sink.
2. **Δn, Δp, and Δe** are the deepest roots — framing, polarity, and energy. Everything else is downstream or operational.
3. **Δh** is the universal sink — any failure that persists long enough becomes hysteresis.
4. **Δm** is the weakest independent domain — it's usually a symptom.
5. **Δi** is confirmed composite — don't add it.
6. **Δk and Δa** are genuinely independent operational failures — they don't need framing fixes, they need engineering fixes.
7. **The three thin domains (Δn, Δb, Δh) aren't thin by accident** — Δn is a root, Δb is a key junction, and Δh is the sink. They're thin because they're structural, not operational, and structural things are harder to write about directly.
