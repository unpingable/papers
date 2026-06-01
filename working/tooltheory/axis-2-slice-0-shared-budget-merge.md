# Axis 2, Slice 0 — Shared-Budget Merge

**Status:** Base forcing case (2026-05-31). Specimen landed; not promoted. Replaces the original Slice 0 = ConflictMerge filing (now demoted to Case B per `axis-2-case-b-conflict-merge.md`).

**Provenance:** Multi-model conversation 2026-05-31 (ChatGPT analysis → user → Claude Code). ChatGPT pointed out that the conflict-merge model conflated incompatibility with value loss by construction — the merge operator manually flipped a `clean` flag on conflict. The shared-budget model fixes this: the loss emerges purely from joint usage against a shared cap, with no policy detonator. That is the honest Axis 2 phenomenon.

---

## Result

Two locally bridged trajectories can merge into a globally non-viable state where joint usage exceeds the shared cap.

## Meaning

Bridge evidence is local to a trajectory's view of the budget. It does not automatically survive reconciliation against a shared cap. Value loss that no branch-local witness is *scoped to rule out* — not value loss that could not have been anticipated. A bridge with global allocation context could anticipate it; branch-local bridges cannot. The point is **scope insufficiency**, not epistemic impossibility.

## Missing object

Merge admissibility evidence — specifically, evidence that reads **joint usage against shared resources** at the reconciliation boundary. Branch-local bridges cannot see joint usage by construction. **Deliberately not yet defined as a formal predicate.**

## Lean module

`~/git/lean/LeanProofs/Admissibility/BudgetMerge.lean` (~190 lines; scratch annex; not root-wired; build with `lake build LeanProofs.Admissibility.BudgetMerge`; green).

### Model

- **State.** `BudgetState` = `(used : Nat, cap : Nat)`.
- **Actions.** `Act` = `spend Nat | noop`.
- **Run.** `spend n` adds `n` to `used`.
- **Value.** *Viability*: `1` if `used ≤ cap`, `0` otherwise. **Load-bearing — not remaining budget.** Using remaining budget would make every spend locally value-decreasing and collapse the specimen.
- **Bridge.** Maximal (`bridge s a := value s ≤ value (run s a)`). Slice 0's discriminating power lives in the merge layer, not the per-step layer.
- **Authorization.** Trivial.
- **Merge.** Honest additive reconciliation: `merge a b := { used := a.used + b.used, cap := a.cap }`. The bust comes from `6 + 6 > 10`, not from a policy detonator.

### Contrast theorems (these block the "merge is just lossy" objection)

```
merge_value_ok_iff_combined_usage_within_cap :
  value (merge a b) = 1 ↔ a.used + b.used ≤ a.cap

merge_within_margin_preserves :
  value a = 1 → a.used + b.used ≤ a.cap → value a ≤ value (merge a b)
```

The merge is viability-preserving exactly when joint usage stays within the shared cap. The loss requires cap exceedance specifically.

### Keeper theorem

```
locally_bridged_fragments_can_merge_to_value_loss :
  ∃ a a' b b' (_ : BridgedTraj budgetEnv a a') (_ : BridgedTraj budgetEnv b b'),
    value (merge a' b') < value (merge a b)
```

Witness:
- `a = b = s0 = { used := 0, cap := 10 }` (value 1; viable)
- `a' = aliceEnd = { used := 6, cap := 10 }` (value 1; alice branch bridged, since 0+6 ≤ 10)
- `b' = bobEnd = { used := 6, cap := 10 }` (value 1; bob branch bridged)
- `merge s0 s0 = { used := 0, cap := 10 }` — value 1.
- `merge aliceEnd bobEnd = { used := 12, cap := 10 }` — value 0 (12 > 10).
- Strict drop: `0 < 1`.

## Slice 0 keeper line

> Local preservation is not compositional across merge under shared resource composition. The missing evidence is joint-margin admissibility at the reconciliation boundary.

## Why this is Slice 0 (and ConflictMerge is Case B)

The shared-budget specimen produces value loss from *honest additive reconciliation* against a shared cap. The conflict-merge specimen produces loss from the *merge operator's policy itself* flipping a `clean` flag. Both are real compositional failures, but the shared-budget case is the one where the missing evidence (joint-margin admissibility) is cleanly diagnostic. The conflict case is the degenerate sibling — useful as a *kind* of merge failure but not where `MergeAdmissible` will earn its existence.

## What this slice does *not* claim

- Not all merges drop value. Compatible margins preserve it (`merge_within_margin_preserves`).
- Not "merge launders evidence by default" — only when joint usage exceeds cap.
- Not `MergeAdmissible` minted. The corpse is on the slab. The coroner waits for at least one more specimen (Case C, stale evidence) before earning the predicate.
- Not a claim about real institutional budget systems instantiating this shape. The interpretive antecedent belongs to a future sibling paper, not to this kernel.

## Next slices (candidate; not committed)

- **Case B — Reconciliation policy loss.** Already landed as the demoted Slice 0; see `axis-2-case-b-conflict-merge.md`. Sibling specimen showing merge-policy-induced loss.
- **Case C — Stale bridge evidence.** Time-scoped bridge whose horizon has expired by merge time. Scope-explosive — freshness sneaks in. Not yet drafted.
- **Promotion gate.** Slice 0 + Case B + Case C → draft `MergeAdmissible` against the now-real obstacle set. The general statement will likely need to quantify over arbitrary bridged trajectories to the branch tips, which will force routing through `bridgedTraj_preserves` rather than `decide` on concrete endpoints — but that universal companion is the natural shape of the positive theorem at promotion time, not a Slice 0 fix.

## Cross-references

- Forcing-case spec: `working/axis-2-composition-forcing-cases.md`.
- Demoted Slice 0 (now Case B): `working/tooltheory/axis-2-case-b-conflict-merge.md`.
- Suite plan: `working/calculus-suite-map.md`.
- Axis 1 substrate (`SafetyEnv`, `BridgedTraj`, `bridgedTraj_preserves`): `~/git/lean/LeanProofs/Admissibility/SafetyBridge.lean`.
- Original Calculus 2.0 exit-criteria composition-axis bullet (criterion 4: ≥3 bad-merge cases): `working/calculus-2-exit-criteria.md`. Slice 0 + Case B = two of three; Case C is the open slot.
