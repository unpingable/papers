# Heterogeneous witness cohorts

**Slogan:** Witness diversity is not count diversity; it is observability diversity under preserved standing.

**Source:** P25 §8 collective-observability paragraph; grok reviewer Q1 + chatty lane-mapping 2026-05-12.

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

## Promotion gate

Heterogeneous-agent simulation is the natural promotion target if a forcing case shows up — e.g., a downstream tool finds itself wanting to aggregate testimony across heterogeneous witnesses and needs the formal condition. Sim spec lives in `lean-candidates.md`. Currently the P25 §8 paragraph is sufficient and this note is enough.

If sim earns its keep, the bridge artifact between P24 (witness inclusion) and P25 (target substitution) becomes paper-shaped — but only on forcing case, not just on curiosity.
