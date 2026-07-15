# Specimen: Ambient Authority Leak

Status: scratch / non-doctrinal / one specimen, not a taxonomy
Logged: 2026-05-21
Lives near: [locality-and-merge](../notes/locality-and-merge.md). One of five known bad cases the aperture deliberately defers; surfaced here as a single forcing fixture to lock the keeper, not to enumerate the family.
Witness in Lean: `~/git/lean/LeanProofs/Admissibility/LocalBoundary.lean`, `ComponentStep.{left, right}` — examine the `LocalAllows lb_i` field. The merged boundary does not appear there.

## What the specimen targets

> If the merged boundary authorizes the component step, locality has already been lost.

This specimen is the concrete failure case the aperture rules out by construction. It is not a counterexample to the current theorem; it is a counterexample to a *weakened* version of `ComponentStep` that authorizes against `lbₘ.boundary` instead of `lb_i.boundary`.

## Setup

Two components, `P` and `Q`, with local boundaries `lb₁` and `lb₂`. Domains include `secret`, `audit`, `world`.

- `lb₁.partition`: `Internal = {secret, audit}`, `External = {world}`.
- `lb₁.boundary`: authorizes `secret → audit` only. **No edge from any domain to `world`.**
- `lb₂.partition`: `Internal = {world}`, `External = {secret, audit}`.
- `lb₂.boundary`: authorizes `world → world` and nothing else.

`P` would like to expose `secret → world`. **`lb₁` does not authorize this edge.** Under correctly designed `ComponentStep`, `P` cannot take this step. The component never produces the exposure. End of story.

## The leak (counterfactual)

Suppose `ComponentStep` is "fixed" to authorize against the merged boundary `lbₘ` rather than the component's own boundary. Suppose further that `lbₘ.boundary` is the pointwise OR of `lb₁.boundary` and `lb₂.boundary` (the naive "no widening" merge from earlier sketches).

Then:

- `lbₘ.boundary.authorized secret world = false` (neither component authorizes it), so `P` *still* cannot take the step. The leak does not fire on this exact pair.

So the simple OR-merge of authorization is not where the leak happens. **The leak requires a merged boundary that gains authority neither component had.** That happens when the merge policy admits external supplements (a "trust authority" added at composition time), or when `lbₘ.boundary` is constructed from a richer policy than pointwise OR.

Concretely: imagine a composition rule that grants `secret → world` "because the joint system is trusted." Now `lbₘ.boundary.authorized secret world = true`. Under the broken `ComponentStep` that authorizes via `lbₘ`, `P` takes the step. The exposure lands in the global config. `lbₘ.partition.Internal secret ∧ lbₘ.partition.External world` — and the partition agrees? It depends on how partitions merged. If `lbₘ.partition.External world = true` (because `lb₁` already said so), the new config violates `NoInternalExternalExposure lbₘ.partition`. **Safety broken.**

But what if the merge also widens the partition — declares `world` to be Internal under `lbₘ`? Then `NoInternalExternalExposure lbₘ.partition` is preserved trivially. *No violation visible at the merged level.* The exposure is silently laundered into "internal traffic." This is the worse failure mode: **the merged view has been redefined to hide the leak.**

## Why the current aperture refuses both modes

`ComponentStep.left` and `ComponentStep.right` in `LocalBoundary.lean` require `LocalAllows lb₁` and `LocalAllows lb₂` respectively. `lbₘ.boundary` is not consulted. So:

- Mode 1 (leak via merged-authorization widening): `P` still needs `lb₁.boundary.authorized secret world = true` to step. It does not. The step does not fire. The leak is structurally impossible at the seam.
- Mode 2 (leak via merged-partition widening hiding the violation): `MergeAdmissible.left_sound` requires that any action `lb₁` authorizes is safe under `lbₘ.partition`. So redefining `lbₘ.partition` to absorb `world` as Internal would have to be admissible w.r.t. `lb₁`'s authorized set. The merge predicate is checked at composition time; it constrains what `lbₘ.partition` can claim.

The aperture refuses the leak in both modes because authorization stays local, and the merge predicate constrains the global partition rather than the local step.

## What this specimen is and is not

- It is one fixture pinning the keeper to a concrete scenario.
- It is NOT a proof of impossibility — only an existence-of-design argument: the current `ComponentStep` shape has no place where ambient authority could enter the step.
- It is NOT currently a Lean theorem. Formalizing it as `example_ambient_authority_leak` would require constructing concrete `Domain`, `Failure`, `Boundary`, and `BoundaryPartition` values. That is a separate cost and the resulting fixture must discriminate the two leak modes; it may be undertaken before any runtime forcing case.
- It is NOT a taxonomy entry. The other four bad cases (boundary collision, authority widening, projection laundering, containment inversion) remain explicitly deferred.

## Keeper, locked

> A component step authorized by the merged boundary is not a local step. It is a global step wearing a local mask.

## Forward-pointing

If this specimen is later formalized as a Lean example, the natural home is `LeanProofs/Admissibility/LocalBoundarySpecimens.lean`, not extensions to `LocalBoundary.lean` itself. The aperture file should stay small.

The corpse will still be there tomorrow.
