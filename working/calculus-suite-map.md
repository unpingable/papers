# Admissibility Suite — axis plan

**Status:** Suite-architecture decision record (2026-05-31). Supersedes the implicit framing that one safety-axis preprint = "Calculus 2.0." Per the spine page (`working/calculus-paper-spine-2026-05-28.md`) and the post-DeepSeek scope honesty: the full admissibility calculus is a *suite* of axis kernels, not a single grand starting paper.

**Provenance:** Triggered by DeepSeek's adversarial review of the safety-axis draft (filed under the working title "An Admissibility Calculus") + ChatGPT's triage. DeepSeek's strongest hit — "the results are definitional, not substantial; reads like an internal development log" — forced the hidden scope question: is this *the* paper, or one component of a suite? The current artifact is small because it covers one axis. Trying to dress it as a complete calculus paper is what made the small theorem mass look bad; framing it as Axis 1 of a multi-axis suite turns the same smallness into correct modularity.

---

## The plan

The full admissibility calculus is a suite, not a single starting kernel.

### Axis 1 — Safety / value preservation

**Current artifact:** Safety-Bridge Kernel (`preprint/admissibility-calculus/`).

**Question:** When does authorization evidence fail to carry value-preservation evidence?

**Status:** Drafted as safety-axis note. Not the full calculus.

### Axis 2 — Composition / merge admissibility

**Future artifact.**

**Question:** When do locally admissible transitions fail under composition or merge?

**Status:** Open. Likely home for the `LocalBoundary.MergeAdmissible` necessity work and the bad-merge counterexample family that `working/calculus-2-exit-criteria.md` named as criteria (3) and (4).

### Axis 3 — Self-amendment / frontier mutation

**Future artifact.**

**Question:** When is mutation of admissibility rules itself admissible?

**Status:** Open. Maps to `FRONTIERS.md` Frontier 3.

### Final synthesis — Admissibility Calculus

**Only promote after** the axes exist and cross-axis theorems or counterexamples force unification. Until then, "An Admissibility Calculus" is the name of a publication slot, not an artifact.

---

## Why this is better than parking

The earlier proposal was to *park* the safety-axis kernel as a sealed-but-unpublished formal organ. The suite framing is better because:

- It turns the artifact's smallness from a weakness into correct modularity per axis.
- Each axis can have its own theorem-mass threshold; the unifying paper is not padded, it's synthesis.
- The current draft already says "Not Calculus 2.0" because composition and self-amendment remain open — the suite plan lines up with the document's own scope fence instead of fighting it.
- Each axis-note is independently citable; Paper 28 can cite Axis 1 today without waiting for Axes 2/3.

## Promotion criteria

Each axis-note promotes from candidate → drafted → released when:

- The axis's question has a clean answer in Lean (theorem family or counterexample family).
- The note answers *what does this axis prove that the others do not?* in one sentence.
- A consumer (paper or downstream artifact) needs it.

For each axis, the consumer-forced-promotion rule applies: no consumer, no release.

## Per-axis "what does this axis prove that the others do not?"

- **Axis 1 (Safety):** Authorization does not imply value preservation; bridge evidence cannot be reconstructed from authorization in gap cases.
- **Axis 2 (Composition):** Local admissibility does not imply admissible merge / global composition.
- **Axis 3 (Self-amendment):** Present authorization does not automatically authorize mutation of future admissibility conditions.

## Repository layout — light vs full

The full ChatGPT-recommended layout splits the work into a sibling directory tree:

```
preprint/admissibility-suite/
  00-spine/        (calculus-suite-map.md, terminology.md, promotion-criteria.md)
  01-safety-bridge/
  02-composition/
  03-self-amendment/
  04-unifying-calculus/
```

For now: deferred. Creating empty hallways for axes 02/03/04 before they have content is premature scaffolding. The current safety-axis preprint stays at `preprint/admissibility-calculus/` with its title and framing internally renamed; this suite-map note serves as the spine until Axis 2 or 3 has substance and forces the directory restructure.

## Related records

- Safety-axis preprint: `preprint/admissibility-calculus/` (internally renamed "Safety-Bridge Kernel: Authorization and Value Preservation").
- Spine page: `working/calculus-paper-spine-2026-05-28.md` (preprint sibling to paper 28).
- Exit criteria: `working/calculus-2-exit-criteria.md` (the original 6-criterion framing of "Calculus 2.0"; criteria split across axes 1/2/3 per its track-split annotation).
- Trajectory canonicalization: `working/tooltheory/trajectory-canonicalization-2026-05-30.md`.
- Tier map: `working/tooltheory/calculus-2-tier-map-2026-05-28.md`.
- DeepSeek adversarial review + ChatGPT triage: in conversation history 2026-05-31 (not filed as standalone artifact; the suite plan above is the load-bearing distillation).

## What did NOT change

- Lean source remains at `~/git/lean/LeanProofs/Admissibility/` as one substrate; axes do not split the kernel, only the publication artifacts. Cross-axis theorems (when they exist) will live wherever fits — likely the substrate.
- Paper 28 plan is unchanged: it cites the formal kernel (now Axis 1 specifically) and discharges the institutional antecedent.
- The trajectory canonicalization, characterization predicates (`AuthorizationBridgeGap`, `AuthPreserves`, `MaximalBridge`, `BridgeComplete`, `HasForgetfulSection`), and characterization theorems (`authorizedTraj_preserves_iff_authPreserves`, `no_gap_implies_authorized_steps_bridgeable`, `no_safeStep_for_unbridged_authStep`, `gap_blocks_safeStep_lift`, `maximal_bridge_implies_complete`) all land in `SafetyBridge.lean` and serve Axis 1.
