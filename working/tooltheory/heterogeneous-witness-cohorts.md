# Heterogeneous witness cohorts

**Slogan:** Witness diversity is not count diversity; it is observability diversity under preserved standing.

**Source:** P25 §8 collective-observability paragraph; grok reviewer Q1 + ChatGPT lane-mapping 2026-05-12.

## What it is

P25 §8 names *collective observability* — at the cohort level, the relevant condition is $q \notin \ker(\bar O_T)$, where $\bar O_T$ is the stacked finite-horizon observability matrix from heterogeneous sensor maps. Necessary, not sufficient: the architecture must preserve the heterogeneous signal through aggregation, estimation, and control allocation.

The doctrine implication: more witnesses helps only if they add observability dimensions *and* the aggregation rule preserves those dimensions. Replicated proxy sensors do not improve target access regardless of count. Aggregation that collapses heterogeneity back into the proxy channel discards exactly the signal that made the cohort case better than the single-agent case.

The diversity that matters is **orthogonality + latency**: orthogonal sensors rotate the subspace; different temporal profiles stop the cohort from collapsing onto the same fast proxy. A slow / expensive $T$-sensor is still useful if the architecture preserves its standing instead of letting the fast $C$-channel dominate every live decision.

## Tool mapping

- **NQ:** witness registry as observability-mapping, not just witness-counting. Distinguish "multiple witnesses to $C$" from "witnesses to $T$ and $C$ together." Each witness has a scope tag.
- **AG:** standing-preservation under aggregation. A slow $T$-sensor only gets to authorize $T$-binding if the architecture refuses to let the fast $C$-channel dominate every live decision.
- **labelwatch / driftwatch:** aggregation rules that preserve heterogeneity vs collapse it — design constraint, not implementation detail.

## Lean candidates

- `homogeneous_replication_preserves_kernel` — already proven in `Paper25EpistemicBorderControl.lean` as `ker_replicateRows_eq_ker`; the predicate-name pattern is the keeper
- `collective_observability_necessary_not_sufficient` — sufficiency part is open

## Simulation and promotion posture

Heterogeneous-agent simulation is a natural validation target once the comparison question and measurement model are sharp enough. A downstream aggregation tool can provide a useful instantiation, but the formal condition may be developed first and lead the simulation or runtime design. The sim spec lives in `lean-candidates.md`. Currently the P25 §8 paragraph and existing kernel theorem cover the selected scope; that is a prioritization judgment, not a consumer gate.

If a simulation produces discriminating evidence, the bridge artifact between P24 (witness inclusion) and P25 (target substitution) may become paper-shaped. Paper promotion remains evidence-gated; Scratch formalization does not wait for that promotion case.
