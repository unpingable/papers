# Cybernetic Failure Taxonomy: Role Map

**Status:** Compressed reference. Derived from structured pass (2026-03-31). Updated with meta-layer distinction.
**Structure:** 14 primitive domains + 1 demoted composite. Four role classes: root, amplifier/transmission, sink, constraint. One identified substrate condition (scale geometry) underneath.
**Key finding:** The taxonomy has actors, not just entries. Domains are control mechanisms that flip valence depending on regime and context — not a catalog of bad things.

---

## Role Map

| Domain | Name | Primitive? | Role | Upstream | Downstream | Therapeutic Inversion |
|---|---|---|---|---|---|---|
| **Δn** | Namespace failure | Yes | **Root** | (independent — deepest) | → Δb, Δo, Δm, Δh | Constructive ambiguity; restraint from premature naming |
| **Δo** | Observability failure | Yes | **Root** | (independent) or ← Δb | → Δm, Δg, Δw | Deliberate opacity / privacy / information scoping |
| **Δs** | Signal corruption | Yes | **Root** | (independent) | → Δm → Δg | Signal shaping (failure is deception, not modification) |
| **Δw** | Write-authority drift | Yes | **Root** (governance) | (independent) or ← Δr | → Δc → Δh | Delegated authority with sunset clauses |
| **Δp** | Polarity inversion | Yes | **Root/Amplifier** | (independent) or ← Δr, Δs | → Δr, Δg, Δs | Deliberate contrarian inversion (hack, not stable) |
| **Δm** | Model drift | Yes (weak) | **Transmission** | ← Δs, Δo, Δn, Δb | → Δg, Δa | Deliberate model simplification |
| **Δk** | Coupling mismatch | Yes | **Operational + Amplifier** | (independent) | → Δx | Tight = coordination; loose = modularity |
| **Δx** | Scale inversion | Yes | **Cross-scale transmission** | ← any cross-scale intervention; ← Δk | inverts sign across scale boundaries | Multi-scale coherent design (Paper 1) |
| **Δr** | Recursion capture | Yes | **Context-dependent** | ← Δp, Δs; or (independent) | → Δw, Δm | Recursion as learning / practice / skill acquisition |
| **Δb** | Boundary error | Yes | **Junction** | ← Δn; ↔ Δn | → Δc, Δo, Δm | Appropriate scoping (when outside controller exists) |
| **Δg** | Gain mismatch | Yes | **Terminal** | ← Δm, Δp | (end-state) | Gain tuning (the point of control theory) |
| **Δa** | Actuation mismatch | Yes | **Terminal** | ← Δm | (end-state) | No |
| **Δc** | Consequence detachment | Yes | **Downstream** | ← Δb, Δw | → Δh; ↔ Δh | Deliberate consequence buffering (liability, insurance) |
| **Δe** | Energy deficit | Yes | **Constraint** | (orthogonal — external) | → Δh (prevents recovery) | No |
| **Δh** | Hysteresis failure | Yes | **Sink** | ← everything uncorrected | ↔ Δn, ↔ Δc (lateral) | Anti-flap / damping / regime stabilization |
| *Δi* | *Identity failure* | **No — composite** | *Syndrome* | *Δn + Δr + Δw* | *N/A* | *Demoted: decomposes without residue* |

---

## Key Pipelines

| Pipeline | Path | Description |
|---|---|---|
| **Framing cascade** | Δn → Δb → Δc → Δh | Can't name it → wrong boundary → consequences detach → normalizes permanently |
| **Perception-to-control** | Δs → Δm → Δg | Corrupted signal → model drifts → gain miscalibrated (Goodhart path) |
| **Authority capture** | Δr → Δw → Δc → Δh | Recursion captures authority → authority drifts → consequences detach → locks in |
| **Exhaustion lock-in** | Δe → Δh | No surplus to correct → failure persists → normalizes (maintenance trap loop) |

## Key Reinforcing Loops

| Loop | Description |
|---|---|
| **Δh ↔ Δn** | Normalization erases vocabulary for baseline; lost vocabulary makes non-return invisible. The epistemic trap: persist → normalize → lose the word for "before" → can't even name return. |
| **Δh ↔ Δc** | Consequence detachment normalizes; normalization prevents reconnection. Institutional sclerosis loop. |
| **Δn ↔ Δb** | Can't name it → can't draw the boundary; wrong boundary → excludes the thing → never gets named. |

---

## Substrate vs. Domain: Scale Geometry

The taxonomy presupposes at least one background condition that is not itself a failure domain:

**Scale geometry** — the fact that behavior does not preserve sign, meaning, or controllability automatically across levels. This is a property of multi-scale systems, not something that breaks. It's the substrate Δx operates within.

- **Scale geometry** = the condition. Multi-scale systems exist; crossing scale boundaries changes things.
- **Δx (scale inversion)** = the failure. A specific intervention or optimization that is correct at one scale inverts at another.

Scale is substrate. Δx is the wound. You design around the substrate; you diagnose and fix the failure.

**Temporal geometry** (the Δt framework's home territory) is likely a second substrate condition — the fact that processes unfold at different rates and synchronization is not free. This is already implicit across the entire paper series.

**Boundary geometry** is tempting as a third substrate condition but risky: Δb is one of the strongest concrete domains in the taxonomy. Elevating "boundary geometry" too aggressively could dissolve Δb from a diagnosable failure into mere background ontology. Leave this one alone unless the substrate/domain distinction can be stated as cleanly as it is for scale.

---

## Caution: Δh Scope

Not every durable failure is Δh in the strong sense. Distinction:

- **Persistent failure:** The failure continues because nobody fixed it. Unresolved, not self-stabilizing. Remove the neglect and the failure is correctable.
- **Hysteretic failure (Δh proper):** The failure has become self-stabilizing — the state of being in the failure actively maintains the failure. Reversal attempts are resisted or structurally prevented.

Δh as "universal sink" means it's the *destination* of uncorrected failures, not that every old failure is hysteretic. The discrimination criterion (from the Δh spike): **pathological when the persistence mechanism is self-referential rather than environment-referential.**

---

## What This Map Says

1. **Four roots** (Δn, Δo, Δs, Δw) plus one hybrid (Δp). These distort framing, perception, or authority. They originate cascades.
2. **One junction** (Δb) that sits between framing and governance. High connectivity, key intervention point.
3. **One cross-scale transmission domain** (Δx) that inverts sign across scale boundaries. Operates within scale geometry as substrate condition.
4. **Two terminals** (Δg, Δa) that mostly receive and don't propagate. Engineering problems.
5. **One sink** (Δh) that receives from everything and locks failures in. Has the strongest therapeutic inversion.
6. **One constraint** (Δe) that's orthogonal to the causal graph — determines recoverability, doesn't cause failures.
7. **One confirmed composite** (Δi) that decomposes cleanly. Demote, don't promote.
8. **At least two substrate conditions** (scale geometry, temporal geometry) underneath the taxonomy that are not failures themselves but conditions under which failures propagate.
9. **11 of 14 primitives have therapeutic inversions** — same mechanism, different sign. The taxonomy describes control mechanisms, not a morality catalog.
