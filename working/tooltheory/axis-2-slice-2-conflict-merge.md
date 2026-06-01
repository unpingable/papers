# Axis 2, Slice 2 — Conflict Merge (reconciliation-policy failure)

**Status:** Result note (2026-05-31; renumbered 2026-06-01; positive object added 2026-06-01). Specimen landed; not promoted. Filed per the Axis 2 forcing-case discipline in `working/axis-2-composition-forcing-cases.md`.

**Reclassification history.**
- 2026-05-31 a.m.: filed as Slice 0
- 2026-05-31 p.m.: demoted to "Case B" when `SharedBudgetMerge` landed as the honest Slice 0
- 2026-06-01: renumbered as **Slice 2** after `StaleEvidenceMerge` (temporal scope failure) landed as the orthogonal Slice 1

**Why Slice 2 and not 0 or 1.** Slices 0 and 1 capture two distinct *branch-local-scope* failures (joint usage unseen; temporal horizon unseen). This module's failure mode is different in kind: the merge operator's *own policy* manually flips `clean := false` on incompatible owners. That makes it real but degenerate — useful as the sibling specimen for the third dimension of `MergeAdmissible` (merge-policy preservation), not as a branch-local-scope failure where the bridge witness's limits are the diagnostic.

**Provenance:** Multi-model conversation 2026-05-31 → 2026-06-01 (ChatGPT then user). The ChatGPT analysis flagged that the conflict-merge model conflates "incompatibility" with "value loss" by construction — when the merge sees conflict, it manually drops `clean` to `false`. That's honest as a *kind* of merge failure but it's not the branch-local-scope failure the suite needs; the loss is in the merge policy. Slices 0 (shared-budget) and 1 (stale-evidence) cover the branch-local-scope failures.

---

## Result

Two locally bridged trajectories can merge into a globally value-losing state.

## Meaning

The merge operator's reconciliation policy can itself destroy value when branch states are incompatible. This is a real but degenerate composition failure — the loss is in the merge function, not in the bridge evidence per se.

## Missing object

Reconciliation-policy preservation: branches must have compatible owners so the merge does not invoke its conflict branch. Local now (2026-06-01) — see "Positive object" below.

## Lean module

`~/git/lean/LeanProofs/Admissibility/MergeConflict.lean` (~155 lines; scratch annex; not root-wired; build with `lake build LeanProofs.Admissibility.MergeConflict`; green).

### Model

- **State.** `MergeState` = `(owner : Owner, clean : Bool)`; `Owner` = `none | alice | bob`.
- **Actions.** `Act` = `setOwner Owner | noop`.
- **Run.** `setOwner` rewrites `owner`; `clean` is preserved by every local action.
- **Value.** `1` if `clean`, else `0`.
- **Bridge.** Maximal (`bridge s a := value s ≤ value (run s a)`). Slice-0-style corner — under this bridge, Axis 1's `MaximalBridge` holds.
- **Authorization.** Trivial.
- **Merge.** Compatible owners (any of: one `none`, equal) merge fields; incompatible owners drop to `{ owner := none, clean := false }` — *this manual flip is what makes the case degenerate*.

### Keeper theorem

```
locally_bridged_fragments_can_merge_to_value_loss :
  ∃ a a' b b' (_ : BridgedTraj mergeEnv a a') (_ : BridgedTraj mergeEnv b b'),
    value (merge a' b') < value (merge a b)
```

Witness:
- `a = b = s0 = { owner := none, clean := true }` (value 1)
- `a' = aliceEnd = { owner := alice, clean := true }` (alice branch bridged)
- `b' = bobEnd = { owner := bob, clean := true }` (bob branch bridged)
- `merge s0 s0` is clean — value 1.
- `merge aliceEnd bobEnd` is conflict (incompatible alice/bob) — manually set to value 0.
- Strict drop: `0 < 1`.

## Why this is Slice 2 and not Slice 0 or 1

The merge policy's conflict-handling branch directly produces the value loss. Without the manual `clean := false` flip on incompatibility, no loss would occur. By contrast:

- **Slice 0 (`BudgetMerge.lean`)** gets the loss purely from joint usage exceeding cap (`6 + 6 > 10`) — branch-local scope cannot see joint resource usage. No policy detonator.
- **Slice 1 (`StaleEvidenceMerge.lean`)** gets the loss from reconciliation occurring outside the inherited evidence horizon (`12 > min(10, 10) = 10`) — branch-local scope cannot see future time. No policy detonator. (Also the first specimen to exercise the substrate's non-maximal-bridge path; see `timed_bridge_not_maximal`.)

Slices 0 and 1 are the *base* forcing cases because they expose distinct branch-local-scope failures. Slice 2's missing evidence is "merge-policy admissibility" — useful as the third dimension of the eventual `MergeAdmissible` predicate, but it is not where the branch-local-scope dimensions earn their existence.

## Positive object (added 2026-06-01)

```
@[reducible] def ConflictMergeOk (a b : MergeState) : Prop :=
  compatibleOwner a.owner b.owner = true

conflict_merge_viable_iff_admissible
  {a b : MergeState} (ha : a.clean = true) (hb : b.clean = true) :
  value (merge a b) = 1 ↔ ConflictMergeOk a b

conflict_merge_restores
  {s sA sB : MergeState}
  (_tA : BridgedTraj mergeEnv s sA) (_tB : BridgedTraj mergeEnv s sB)
  (haClean : sA.clean = true) (hbClean : sB.clean = true)
  (ok : ConflictMergeOk sA sB) :
  value (merge sA sB) = 1
```

Three honesty notes:

1. **`BridgedTraj` hypotheses are framing, not load-bearing.** The conclusion follows from `conflict_merge_viable_iff_admissible` alone. More pronounced here than in Slices 0/1 because Slice 2's failure is policy-induced rather than emergent — even the cleanness preconditions, not the trajectories, do the substantive work. Underscore-bound to mark this.
2. **The iff requires cleanness preconditions.** The merge's `clean` field on the compatible branch is `a.clean && b.clean`; an unclean input would falsify viability regardless of compatibility. Stating the iff *under cleanness* isolates the policy-specific dimension. The cleanness preconditions are what a non-vacuous BridgedTraj would deliver.
3. **Slice 2 is degenerate but real.** Its job is to force the policy-preservation dimension of the eventual generic `MergeAdmissible`; it is NOT equal-depth to BudgetMerge or StaleEvidenceMerge, which exhibit *emergent* composition failure under honest merges.

## Triad complete

With Slice 2 sealed, the three forcing-case dimensions of the eventual `MergeAdmissible` are all named:

```
joint-resource condition       — Slice 0  (BudgetMergeOk)
freshness-as-basis condition   — Slice 1  (StaleMergeOk, collapse-confirmed via GuardCollapse)
policy-preservation condition  — Slice 2  (ConflictMergeOk)
```

Three corpses, three coroner's reports. Generic extraction is no longer speculative — see `working/axis-2-composition-boundary.md`.

## Cross-references

- Forcing-case spec: `working/axis-2-composition-forcing-cases.md`.
- Slice 0 (the honest base forcing case): `working/tooltheory/axis-2-slice-0-shared-budget-merge.md`.
- Suite plan: `working/calculus-suite-map.md`.
- Axis 1 substrate: `~/git/lean/LeanProofs/Admissibility/SafetyBridge.lean`.
