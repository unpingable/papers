# Baby River — Admissibility Residue

**Status:** small note, not a project. Negative residue from a kernel-overlap audit (2026-05-24).

## Frame

A fresh-context model proposed inserting an admissibility "promotion gate" between environmental traces and policy action in Baby River — `agent.authorized_bias(trace, need_state)` replacing direct `score += env.trail[y][x]`. The proposal was triangulated against the actual simulator and against a second model with opposite review bias. Both reads converged: no code seam, the mediation layer already exists.

The useful keeper is negative, at two scales:

> **Genus:** *Interpretive analogy is not architectural license.*
>
> **Species (Baby River):** Don't patch a mediation layer into an architecture that already has one.

Filed here so future-me/Claude doesn't try to "kernel" some other simulator under the same vocabulary skid without checking whether the mediation is already cooked in.

## Why no code change

Baby River's actual architecture (`preprint/06-temporal-closure-requirements/baby_river_v2.py`):

- No trails. No accumulating residue. Heat spikes are transient (100-step expiry); food regenerates; shade is static. Largely Markovian + bounded transients.
- Agents are PPO-trained policy networks, not hand-coded reflexes. There is no `score += env.trail[y][x]` to refactor.
- The promotion-equivalent already exists as `MetabolicAgent.get_temperature(energy, heat)` — exploration temperature scales with metabolic urgency. The whole Paper 06 contrast (`MetabolicAgent` vs `BaselineAgent`) is precisely the test of urgency-modulated vs scheduled exploration bandwidth.

Bolting a symbolic admissibility gate onto a PPO architecture either (a) fights the learner upstream as a hand-coded mask, or (b) censors logits downstream as a worse temperature schedule. Both are kernel-cosplay.

## Interpretive sentence (for Paper 06 / SI-B if next touched)

> In Baby River, metabolic urgency already functions as a promotion gate by modulating exploration bandwidth; the admissibility analogy is interpretive, not architectural.

Not a paper edit today. Note for next pass.

## Cousin experiment (default-future-work, not forcing case)

A stigmergic/residue world where persistent environmental traces influence action would actually exhibit the failure mode Baby River does not have. Narrower causal claim than "admissibility works":

> **Persistent traces become maladaptive when they steer action without current internal-state mediation; need-gated promotion reduces that failure.**

Sketch:

- Environment with residue/trails/marks left by past behavior.
- Agent variants: trace-blind baseline / trace-following reflex / trace-following learned policy / need-gated trace promotion / metabolic-mediated.
- Stressors: substrate change, old trails become misleading, resource needs invert, danger zones shift.
- Measures: survival, recovery after substrate change, perseveration on stale trails, action entropy, dependence on trace age, failure to abandon formerly useful paths.

Not Baby River. Cousin. Filed as default-future-work; promotion to forcing case requires a current need.

## Composes with

- [[feedback-kernel-overlap-audit]] — 2026-05-24 case (cognitive memory promotion + this) where felt-sense register echo caught the import before substrate audit needed to fire
- [[feedback-multi-model-routing]] — triangulation across opposite-bias models confirmed no-patch
- Paper 06 (Temporal Closure Requirements) — interpretive sentence above belongs in SI-B if/when next touched
