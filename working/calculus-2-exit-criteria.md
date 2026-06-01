# Calculus 2.0 — exit criteria

> **Status:** internal exit-criteria record. Not a 2.0 commitment.
> Companion to [[kernel-to-body-map]] and [[frontier-proof-obligations]].
>
> **Status update 2026-05-29 — spine page split.** The original framing in this document assumed "Calculus 2.0" was a single artifact whose body the six criteria below define. Per `working/calculus-paper-spine-2026-05-28.md`, the publication track is now split: the **safety-axis** lands as a standalone formal-methods preprint (working slug *"An Admissibility Calculus: Authorization, Safety Bridges, and Value Decay"*) outside the Δt Zenodo numbering; **paper 28** is the interpretation paper that cites the preprint; the **composition-axis** body and Frontier-3 self-amendment work remain on the original (now-renamed) "composition-axis 2.0" trajectory. The six criteria below remain valid as a *map of what 2.0 would need*; what changed is which publication artifact closes each one. The track-split annotation block after the criteria list reclassifies each criterion by publication track and marks current status.

## What "full body" means here

The 1.0 surface is named, versioned, and DOI'd. **Under this map**, Calculus 2.0 (the body) exists iff *all* of:

1. *Authorized ≠ Safe* is mechanically exhibited (`AuthorizedNotSafe.lean`).
2. A minimal safety bridge proves safety **only under explicit extra hypotheses** (`SafetyBridge.lean` with a non-trivial `SafetyEnv` obligation).
3. `LocalBoundary.MergeAdmissible` has **necessity** (for the named exposure-safety property under the current `LocalBoundary` model), not just sufficiency (`merge_admissible_necessary`).
4. At least three bad merge cases are formalized as `MergeAdmissible` violations.
5. Self-amendment is blocked without weakening the 1.0 transition story (wrapper module, no mutation to `StateTransition.lean` until forced).
6. Annex axes either compose (with a theorem that has a consumer) or are explicitly kept outside the surface.

Until all six land, "Calculus 2.0" is not a thing that exists. The map is allowed to point at an unbuilt body. *More modules, more theorems, more vibes* is not progress.

The "Under this map" qualifier is load-bearing: future Frontier 5 (currently reserved) or a downstream forcing case may change the body shape. This document is allowed to be revised. It is not a constitution.

## Track split (2026-05-29, web-Claude verification pass)

The six criteria above are now distributed across three axes / publication tracks per the spine page decision (`working/calculus-paper-spine-2026-05-28.md`) and the per-condition verification web-Claude ran against the actual Lean source on 2026-05-29. Meeting the safety-axis criteria does NOT mint "Calculus 2.0" as this document originally framed it; it mints the **safety-axis publication path** (the planned preprint plus paper 28) as a sibling artifact. The other axes remain separate gates with the original-document bar.

Per-axis status, verified against `~/git/lean/LeanProofs/Admissibility/`:

### Safety axis — MET, over-delivered

Preprint working slug: *"An Admissibility Calculus: Authorization, Safety Bridges, and Value Decay."* Target venue: arXiv cs.LO at minimum.

- **(1) Authorized ≠ Safe mechanically exhibited — MET 2026-05-28.** Broader than the original criterion: `AuthorizedNotSafe(Witness)` exhibits the wound at the `StepAllowed` layer (axiomatic + concrete `List Receipt` discharge); `AuthorizedStepNotSafe(Witness)` transfers the wound to the full verdict-layer `Execution.AuthorizedStep` (axiomatic + concrete `AuthorizedStepC` discharge over real `Authority.authorityVerdict`).
- **(2) Safety bridge with non-trivial obligation — MET 2026-05-28, AND the original bar was a floor.** The original wording asked for "a minimal safety bridge proves safety only under explicit extra hypotheses." What shipped is materially more: the safety-axis criterion *as actually met* is the full brick set, and the original wording undersells it by a wide margin. Effective content:
  - `SafetyBridge.SafetyEnv` with actor-inert `bridge : σ → α → Prop` and `preserves` obligation; `SafeStep` gate; `bridge_implies_safe` projects through `preserves` without consuming `Allowed` (per ρ-drop decision at `working/tooltheory/safety-bridge-rho-drop-decision-2026-05-28.md`).
  - Trajectory triple in `SafetyTrajectory.lean`: `bridgedTraj_preserves` (positive composition), `authorized_trajectory_loses_value` (negative composition), `no_bridgedTraj_to_poison_end` (no-lift).
  - Forgetful map `BridgedTraj.toAuthorizedTraj` makes "an authorized trajectory that does not lift to a bridged one" a *definition*, not rhetoric — the Loop-Capture mapping turned into a typed function.
  - Verdict-layer canonical gate `SafeAuthorizedStepC` + `.toSafeStep` adapter (brick 1b).
  - Second concrete witness `AttestationLedger.lean` (tier-1 per `working/tooltheory/calculus-2-tier-map-2026-05-28.md`): textured `Nat`-valued model with ≥2 asymmetric actors; the wound is an actor-authorized revoke. Confirms the abstract layer is not receipt-specific. Per-hop actor in the trajectory type makes multi-actor paths expressible.

  The trajectory triple is not "additional evidence beyond the criterion" — it is the criterion's substantive form. The original wording is preserved above as historical record of the minimum bar; the criterion *as met* is the full brick set described here. (Revision per web-Claude 2026-05-29: condition 2 marked upward to reflect what shipped.)

**Safety-axis publication status:** *formalized YES; trajectory-design divergence DISCHARGED 2026-05-30 via the substrate canonicalization (per-hop actor as field in `SafeStep` / `AuthorizedStepC` / `SafeAuthorizedStepC`, generic per-hop-actor trajectories at the `SafetyBridge.lean` substrate); preprint scaffold pending.* Lean source is the source of truth; the preprint is exposition. Canonicalization record: `working/tooltheory/trajectory-canonicalization-2026-05-30.md`.

### Composition axis — NOT MET (sufficiency only)

Per the verification pass: `LocalBoundary.lean`'s own "Open obligations" block states that necessity is "not started." Only sufficiency (the aperture) is proven. The composition axis stays on the original (now-renamed "composition-axis 2.0") trajectory; the safety-axis preprint does not close any of these.

- **(3) `LocalBoundary.MergeAdmissible` necessity — NOT MET.** `merge_admissible_necessary` theorem not started; sufficiency only.
- **(4) At least three bad merge cases formalized — NOT MET.** Per LocalBoundary's own block: "paper-shaped, not Lean-shaped."
- **(6) Annex axes either compose or stay outside the surface — PARTIAL.** "Stay outside" honored via current `[annex]` labeling in `LeanProofs/Admissibility/README.md`; composition theorems pending. (Note: this is the Roadmap's *composition-axis 2.0* criterion, distinct from the safety-axis content above.)

### Self-amendment axis — NOT MET (Frontier 3, deferred)

- **(5) Self-amendment blocked without weakening the 1.0 transition story — NOT MET.** Frontier 3 in `FRONTIERS.md`, deferred per dependency-order discipline (tractable but not load-bearing for the safety-axis claim; gate stays open for the full 2.0 label).

### "2.0" label — scoped

The naming question is decided as scoped, not as left-open:

- **Safety axis is ratifiable now** as the safety-axis publication path (preprint + paper 28), gated on the kernel-overlap audit and this reconciliation pass. The safety-axis preprint is scoped narrowly as *"An Admissibility Calculus: Authorization, Safety Bridges, and Value Decay"* — it does not claim the "Calculus 2.0" label, so it inherits none of the unmet-condition overclaim. Fork B's sober title bought exactly this scoping.
- **Full "Calculus 2.0" (all axes) is NOT ratifiable** on safety-axis evidence alone. The composition-axis necessity (3) and self-amendment block (5) are open in the source's own words. Minting the full label requires either (a) all six original conditions met across all three axes, or (b) an explicit doctrinal decision to redefine "Calculus 2.0" as scoped to the safety axis — which the spine page does *not* propose and which this document does *not* recommend (the anti-vibes discipline of the original framing applies).
- **In published / README / public-surface language**, use "safety-axis Calculus 2.0 candidate" or just "safety-axis preprint" — not "Calculus 2.0 core" — until either (a) or (b) above.

This document's six criteria stand as the map of what *the original framing of* 2.0 needs. The spine page is where the publication structure that achieves the safety-axis portion is decided. The composition-axis and Frontier-3 portions of 2.0 remain on their original trajectories, unaccelerated by the safety-axis work.

## Phase 1 — verification criteria

Phase 1 of the body work is exactly one file: `LeanProofs/Admissibility/AuthorizedNotSafe.lean`. Verification:

- `lake build` (no args) passes; the new file is wired into root.
- `grep -rn "sorry" LeanProofs/` returns only the docstring-text references already documented in `Admissibility/README.md`.
- `AuthorizedNotSafe.lean` exhibits, in Lean, a state pair `s₀, s₁` and a `Step` such that `AuthorizedStep` holds on the transition and a `DefendedValue` (inline-defined, minimal) strictly decreases.
- The file's docstring states what 1.0 does not imply, names the wound, and points at `FRONTIERS.md` Frontier 1.
- The docstring includes the scope clause: *this proves `AuthorizedStep` does not imply preservation of arbitrary defended value; it does not prove that no safety bridge exists.*
- `WHAT-THE-LEAN-STACK-PROVES.md` gains one sentence: *authorization does not imply preservation of defended value; see `AuthorizedNotSafe.lean`.*

Root-wired means build-covered; it does not mean public-surface-promised. The 1.0 surface (named in `CalculusOne.lean`) is unchanged by Phase 1.

For each later slice (if and when it lands): the same five-step proof pattern from [[frontier-proof-obligations]], the same ledger update, the same non-claim disclosure.

## What this document is not

- Not a project plan. Slice ordering is in [[kernel-to-body-map]].
- Not a proof ledger. Per-frontier obligations are in [[frontier-proof-obligations]].
- Not a release schedule. None of the six conditions has a date.
- Not a sufficiency claim. Meeting all six lands the body *as currently mapped*. Frontier 5 reserved precisely because the map is allowed to learn.
