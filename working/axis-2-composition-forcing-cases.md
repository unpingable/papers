# Axis 2 — composition / merge admissibility forcing cases

**Status:** Forcing-case note (2026-05-31; renumbered 2026-06-01 after the triad completed). Filed per `working/admissibility-suite-map.md` Axis 2 plan. **All three specimens landed.** `MergeAdmissible` is now eligible for definition — the bad-case family is complete enough that the positive object can earn its existence without proving itself.

**Renumbering note.**
- 2026-05-31 a.m.: original filing listed Case A (shared global budget), Case B (conflicting reconciliation), Case C (stale evidence). Slice 0 was ConflictMerge.
- 2026-05-31 p.m.: SharedBudget promoted to Slice 0 (more honest base forcing case); ConflictMerge demoted to Case B; Case A dissolved into Slice 0.
- 2026-06-01: StaleEvidenceMerge landed as Slice 1 (temporal scope failure, orthogonal to budget); ConflictMerge renumbered to Slice 2 (reconciliation-policy degenerate corner). All three Lean specimens are now green.

**Provenance:** Multi-model conversation 2026-05-31 (ChatGPT). Triggered by the suite reframing of the safety-axis preprint as Axis 1, which made Axis 2 the next natural pain point.

---

Axis 1 proves that authorization evidence does not imply value-preservation evidence.

Axis 2 asks a different question:

> When do locally bridged transitions fail to compose into a globally bridged transition?

## Candidate theorem shape

There exist two locally bridged fragments whose merge is not bridged.

Informal form:

- `BridgedTraj E a a'`
- `BridgedTraj E b b'`
- but `¬ BridgedTraj E (merge a b) (merge a' b')`

The missing object is `MergeAdmissible`: extra evidence that local preservation survives merge.

## Slice 0 — shared-budget merge *(LANDED 2026-05-31)*

**Failure mode:** branch-local scope cannot see joint resource usage. Each fragment preserves its local viability. Their merge sums usage against a shared cap; joint usage exceeds the cap and the merged state is non-viable.

Pattern:
- each branch is locally bridged (spend stays within cap on its own);
- merge is honest additive reconciliation (no policy detonator);
- joint usage exceeds shared cap;
- local bridged does not imply globally bridged.

**Bridge:** maximal (value preservation).
**Lean module:** `~/git/lean/LeanProofs/Admissibility/BudgetMerge.lean`.
**Result note:** `working/tooltheory/axis-2-slice-0-shared-budget-merge.md`.
**Keeper:** `locally_bridged_fragments_can_merge_to_value_loss`. Contrast theorems (`merge_value_ok_iff_combined_usage_within_cap`, `merge_within_margin_preserves`) block the "merge is just lossy" objection.

## Slice 1 — stale-evidence merge *(LANDED 2026-06-01)*

**Failure mode:** branch-local scope cannot see future time. Each fragment is bridged at action time under a validity horizon. Reconciliation occurs after the inherited (min) horizon; the merged evidence is stale even though no branch was locally degraded.

Pattern:
- each branch is locally bridged AND locally fresh (action-time freshness within horizon);
- merge stamps the actual reconciliation time as `now` and inherits min horizon (no failure flag);
- reconciliation time exceeds inherited horizon;
- merged evidence is computed stale; no further `SafeStep` can be packaged.

**Bridge:** NON-MAXIMAL (`evidenceFresh s ∧ value s ≤ value (run s a)`) — strictly stronger than preservation. First specimen to exercise the substrate's non-maximal-bridge path; `timed_bridge_not_maximal` proves it.
**Lean module:** `~/git/lean/LeanProofs/Admissibility/StaleEvidenceMerge.lean`.
**Result note:** `working/tooltheory/axis-2-slice-1-stale-evidence-merge.md`.
**Keeper:** `locally_bridged_branches_can_merge_with_stale_evidence`. Contrast theorem (`mergeAt_fresh_iff_within_inherited_horizon`, `mergeAt_early_stays_fresh`) and substrate obstruction (`no_safeStep_from_stale_merged`) carry the rest. Value is *not* dropped — orthogonal to Slice 0's value-aggregation failure.

## Slice 2 — conflict merge *(LANDED 2026-05-31, positive object 2026-06-01; demoted from Slice 0 → Case B → Slice 2)*

**Failure mode:** the merge operator's *own policy* destroys value. Branch states are individually preserving; reconciliation collapses incompatible branches into a non-viable state by manual flag flip.

Pattern:
- branch A bridged;
- branch B bridged;
- merge policy itself flips `clean := false` on conflict;
- composition fails at the merge policy, not at either branch.

**Why Slice 2 and not 0/1:** This is the *degenerate corner*, not a branch-local-scope failure. Slices 0 and 1 expose distinct branch-local-scope limits. Slice 2 exposes a merge-policy limit — useful as the third dimension of `MergeAdmissible` (merge-policy preservation), not as where the branch-local-scope dimensions earn their existence.

**Bridge:** maximal.
**Lean module:** `~/git/lean/LeanProofs/Admissibility/MergeConflict.lean`.
**Result note:** `working/tooltheory/axis-2-slice-2-conflict-merge.md`.
**Positive object (2026-06-01):** `ConflictMergeOk a b := compatibleOwner a.owner b.owner = true`. Restoration `conflict_merge_restores` and characterization `conflict_merge_viable_iff_admissible` both require cleanness preconditions (`a.clean = true ∧ b.clean = true`) because the merge's `clean` field on the compatible branch is `a.clean && b.clean` — an unclean input falsifies viability regardless of compatibility. The cleanness assumption isolates the policy-specific dimension.

## Candidate positive object

`MergeAdmissible` should witness that a merge operation preserves the defended value under the relevant branch assumptions.

Possible form:

```
MergeAdmissible E merge :=
  ∀ {a a' b b'},
    BridgedTraj E a a' →
    BridgedTraj E b b' →
    compatible a b →
    compatible a' b' →
    E.value (merge a b) ≤ E.value (merge a' b')
```

But this may be too strong. The first pass should find the bad cases before fixing the positive type.

## Merge model — chosen for Slice 0

Three candidates were considered: Nat budget, set/log, time-scoped evidence. **Slice 0 landed on Nat budget** (against the original recommendation of set/log) because the viability-vs-remaining-budget distinction turned out to be the load-bearing modeling move, and the Nat-budget model exposes it directly: value = `1` iff `used ≤ cap`, not `cap - used`. The merge is honest addition; the bust is `6 + 6 > 10`. Set/log and time-scoped remain candidates for later slices (set/log would naturally model Case C's stale evidence horizon if extended with timestamps).

## Candidate keeper line

> Local preservation is not compositional unless the composition operator carries admissibility evidence.

That's the pain. Neatly packaged, possibly cursed.

## Promotion rule — triad complete

All three specimens AND all three local positive objects landed 2026-06-01:
- `BudgetMergeOk` + `budget_merge_restores` + `budget_merge_viable_iff_admissible`
- `StaleMergeOk` + `stale_merge_restores` + `stale_merge_fresh_iff_admissible` (plus Slice 1b's `useEvidence` guard + the `GuardCollapse` probe resolving Finding 3)
- `ConflictMergeOk` + `conflict_merge_restores` + `conflict_merge_viable_iff_admissible` (under cleanness)

**Generic extraction is now unblocked.** Per the post-triad guidance the local versions came first; the constraint set is now closed, not speculative. See `working/axis-2-composition-boundary.md` for the corrected generic candidate (no `Obs` parameter — Finding 3 cut it; `Param → σ → σ → σ` merge with single defended value).

When the universal positive form is reached, it will quantify over arbitrary bridged trajectories to the branch tips and route through `bridgedTraj_preserves` rather than `decide` on concrete endpoints — that universal companion is the natural shape at promotion time.

## Three dimensions of MergeAdmissible

The three slices begin to force the shape:

```
MergeAdmissible  ⊇  joint-resource condition      (Slice 0)
                 ∧  evidence-freshness condition   (Slice 1)
                 ∧  reconciliation-policy condition (Slice 2)
```

## Open design fork (surfaced by Slice 1)

Freshness in Slice 1 is checked against a reconciliation time stamped into the merged state. A full `MergeAdmissible` must decide whether freshness is evaluated against a **global wall-clock** or against **per-witness horizons threaded through the trajectory**. This is the first real design decision the positive object faces; the choice is deliberately left open until the local predicates are drafted and the choice is forced by one of them.

## What not to do

Do not start with `MergeAdmissible` as a beautiful abstraction. That's how you get another clean definition accused of proving itself. Start with the bad merge. Make the calculus earn the predicate.

## Cross-references

- Suite plan: `admissibility-suite-map.md`.
- Axis 1 kernel note: `preprint/admissibility-kernels/` (titled "Safety-Bridge Kernel: Authorization and Value Preservation"; "Axis 1 of the Admissibility Suite").
- Original Calculus 2.0 exit-criteria composition-axis bullets: `calculus-2-exit-criteria.md` (criteria 3 — `merge_admissible_necessary` — and 4 — ≥3 bad-merge cases formalized; both NOT MET).
- LocalBoundary substrate (the sufficiency-only proof that already exists): `~/git/lean/LeanProofs/Admissibility/LocalBoundary.lean`.
