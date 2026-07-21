# Plain-language summary

**Companion to:** *No Universal Plant Clock: Temporal Failure Geometry in Distributed Control Systems* (Δt Paper 22)

**Version/status:** v1.1, published on Zenodo

**Reading status:** This is an explanatory companion to the paper, not the canonical published artifact. It does not silently amend the version of record and introduces no new paper claims.

Distributed systems often behave as if every component shares one present, local clocks are interchangeable, observations describe the current state, and control actions arrive immediately. None of those assumptions is guaranteed. A controller always learns about remote events after they occurred and acts on a plant that continues changing while the command travels.

Failures caused by these timing gaps are often mislabeled as communication, policy, or decision failures.

The paper separates four timing failures that are often collapsed into “latency.” **Gauge mismatch** is disagreement about the reference for now. **Clock divergence** is disagreement about elapsed time. **Retarded-state estimation** means deciding from an old observation. **Delayed actuation** means a command reaches a plant that has already changed. Each consumes a different temporal resource and calls for a different correction.

The proposed diagnostic compares observation, actuation, round-trip, and synchronization uncertainty with the characteristic timescale of the controlled system. It also compares contract duration with the horizon over which clocks remain acceptably aligned. This turns timing assumptions into explicit design obligations: record event, observation, decision, and effect times separately; track estimate age; maintain coherence budgets; and define what happens when disagreement exceeds them. The paper gives distributed-system designers a vocabulary for locating which temporal resource fails first.

## Claim boundary

The four component literatures are established; the contribution is their shared diagnostic grammar. Critical ratio thresholds depend on plant dynamics, controller gain, damping, contracts, and application tolerances, so “ratio near one” is a heuristic rather than a universal boundary. Institutional examples are structural analogies, not calibrated causal diagnoses. Nearby Lean results enforce scope discipline but do not prove this paper’s clocks, ratios, or dynamics. The linked v1.1 manuscript retains a frozen pre-deposit parenthetical saying the Zenodo push is pending; v1.1 was in fact published at the record linked below, and the stale sentence is preserved until a future version rather than silently rewritten.

## Read the paper

- [Manuscript source](no_universal_plant_clock.md)
- [PDF](no_universal_plant_clock.pdf)
- [Directory guide](README.md)
- [Concept DOI](https://doi.org/10.5281/zenodo.19119617)
- [Zenodo v1.1 record](https://zenodo.org/records/19671885)
