# Axis 2, Slice 1 — Stale-Evidence Merge

**Status:** Result note (2026-06-01). Specimen landed; not promoted. Filed per the Axis 2 forcing-case discipline in `working/axis-2-composition-forcing-cases.md`.

**Provenance:** Multi-model conversation 2026-06-01 (ChatGPT analysis → file drafted blind to substrate → user pushed to me → substrate-fix pass on the one typeclass annotation + the three strengthening edits ChatGPT's review surfaced). Triggered by Slice 0 (`BudgetMerge`) leaving open the orthogonal failure mode — local bridges that cannot survive *time* rather than cannot see *joint usage*.

---

## Result

Two locally bridged trajectories whose endpoints are locally viable and locally fresh, but whose reconciliation at a later time produces stale merged evidence. The merged state's value does *not* drop; the failure isolated is purely temporal — bridge non-portability across the reconciliation boundary.

## Meaning

Bridge evidence in this model carries a validity horizon. A bridge is taken at action time when the witness is fresh; nothing about that witness extends its scope to a future reconciliation time. The reconciliation operator inherits the minimum (conjunctive) horizon and stamps the actual reconciliation time as `now`; if that time exceeds the inherited horizon, freshness is computed false. *No witness is destroyed; the witness simply does not cover the period its own data is being reused in.*

The point is **scope insufficiency in time**, distinct from Slice 0's scope insufficiency in joint resource usage:

- Slice 0: branch-local bridges cannot see *joint resource usage*. Spatial / aggregative failure.
- Slice 1: branch-local bridges cannot see *future time*. Temporal failure.

Two genuinely orthogonal failures. Together they begin to force the multi-dimensional shape of `MergeAdmissible`.

## Missing object

Evidence-freshness admissibility at the reconciliation boundary — a dimension branch-local bridges cannot supply, since they certify validity only at their own action time. **Deliberately not yet defined.**

## Lean module

`~/git/lean/LeanProofs/Admissibility/StaleEvidenceMerge.lean` (~310 lines; scratch annex; not root-wired; build with `lake build LeanProofs.Admissibility.StaleEvidenceMerge`; green as of 2026-06-01).

### Model

- **State.** `TimedState` = `(valueOk : Bool, evidenceExpiresAt : Nat, now : Nat)`.
- **Actions.** `Act` = `tick | noop`. `tick` advances local clock by 1; neither touches `valueOk` or the evidence horizon.
- **Value.** Viability: `1` if `valueOk`, else `0`.
- **Bridge.** **NON-MAXIMAL** (load-bearing): `evidenceFresh s ∧ value s ≤ value (run s a)`. Strictly stronger than value preservation — demands action-time freshness AND preservation.
- **Authorization.** Trivial.
- **Merge.** `mergeAt t a b := { valueOk := a.valueOk && b.valueOk, evidenceExpiresAt := min a.… b.…, now := t }`. Parametric in reconciliation time `t`; conjunctive validity; inherited (min) horizon. **No failure flag is ever written** — staleness is *computed* by `evidenceFresh` from the interaction of inherited horizon and reconciliation time.

### Theorems

```
mergeAt_fresh_iff_within_inherited_horizon (t a b) :
  evidenceFresh (mergeAt t a b) ↔ t ≤ min a.evidenceExpiresAt b.evidenceExpiresAt

mergeAt_early_stays_fresh : evidenceFresh (mergeAt 8 aEnd bEnd)
```

These block the "you hardcoded staleness" reviewer attack: the merge is stale-iff-late, not stale-always. Same honesty structure as Slice 0's `merge_value_ok_iff_combined_usage_within_cap`.

```
locally_bridged_branches_can_merge_with_stale_evidence : -- keeper
  ∃ s sA sB (_ : BridgedTraj timedEnv s sA) (_ : BridgedTraj timedEnv s sB),
    value sA = value s ∧ value sB = value s ∧
    evidenceFresh sA ∧ evidenceFresh sB ∧
    ¬ evidenceFresh (mergeAt 12 sA sB)

merged_value_preserved : value merged = 1
```

The merged state stays viable (`merged_value_preserved`). This slice isolates freshness non-portability; the value-drop-under-stale-evidence variant is deferred because honest construction requires the bridge to be doing *guard* work this concrete witness does not exercise.

```
no_safeStep_from_stale_merged : ¬ Nonempty (SafeStep timedEnv merged)
```

**Substrate obstruction.** Because the bridge requires freshness at action time, no further `SafeStep` can be packaged from the stale merged state. Freshness non-portability is not just a predicate fact hanging in the air; it blocks safe-step packaging directly. The same shape as Axis 1's `no_safeStep_for_unbridged_authStep` obstruction.

```
timed_bridge_not_maximal : ¬ MaximalBridge timedEnv
```

**Non-maximal bridge.** Slice 1 is the first specimen to use a strictly-stronger-than-preservation bridge. Witness: `staleButViable` (a state where `valueOk = true` but `now = 12 > 10 = evidenceExpiresAt`); the noop preserves value but the bridge fails on the freshness conjunct. Discharges the slice's prose claim that this bridge is genuinely stricter than preservation. This is also the answer to "is the whole substrate just maximal bridges wearing hats" — no, demonstrably.

### Witness

- `s0 = { valueOk := true, evidenceExpiresAt := 10, now := 5 }` (fresh, viable).
- `aEnd = bEnd = { valueOk := true, evidenceExpiresAt := 10, now := 6 }` (one bridged tick).
- `mergeAt 12 aEnd bEnd = { valueOk := true, evidenceExpiresAt := 10, now := 12 }` (stale: 12 > 10).
- `mergeAt 8 aEnd bEnd` would still be fresh — the contrast witness.

## Slice 1 keeper line

> Local preservation evidence is not compositional when its validity horizon expires before reconciliation.

## Honesty checks (preempting reviewer objections)

1. **Is `mergeAt 12` a detonator?** No. The operator is parametric in reconciliation time and stamps the actual time, never writes a `fresh := false` flag. `mergeAt_fresh_iff_within_inherited_horizon` plus `mergeAt_early_stays_fresh` prove staleness is *computed* by interaction with the inherited horizon, not stamped. Same shape as Slice 0's `6 + 6 > 10`.
2. **The branch witnesses certify what, exactly?** Action-time freshness AND value preservation — that is the content of the non-maximal bridge. The concrete endpoints `aEnd`/`bEnd` are also locally fresh in this specimen, but that is a separate closed fact about these particular `now = 6` states, not a consequence of `BridgedTraj` in general. (Corrected from an earlier drift that conflated "fresh when it acted" with "fresh on its own.")
3. **Why no value drop?** Following the spec deliberately — isolating temporal failure orthogonal to Slice 0's value-aggregation failure. A value-drop-under-stale-evidence variant would need the bridge doing guard work this concrete witness does not exercise; deferred with reason rather than punted.

## Open design question this slice surfaces

Freshness is checked against a reconciliation time stamped into the merged state. A full `MergeAdmissible` must decide whether freshness is evaluated against a **global wall-clock** or against **per-witness horizons threaded through the trajectory**. That choice is what `MergeAdmissible` will have to pin down — and it is exactly why the user's original forcing-case note called Case C "scope-explosive." It is the first real design fork the positive object faces.

## What this slice does *not* claim

- Not all late merges are stale. The merge is stale iff the reconciliation time exceeds the inherited horizon. (`mergeAt_early_stays_fresh` exhibits a fresh merge at `t = 8`.)
- Not "merge launders evidence by default." Only when reconciliation time exceeds the inherited horizon.
- Not `MergeAdmissible` minted. The third specimen (Slice 2, ConflictMerge) provides the merge-policy dimension; only after the triad is complete does the positive object earn definition.

## Cross-references

- Forcing-case spec: `working/axis-2-composition-forcing-cases.md`.
- Slice 0 (joint-margin failure): `working/tooltheory/axis-2-slice-0-shared-budget-merge.md`.
- Slice 2 (reconciliation-policy failure, demoted): `working/tooltheory/axis-2-slice-2-conflict-merge.md`.
- Suite plan: `working/calculus-suite-map.md`.
- Axis 1 substrate (`SafetyEnv`, `BridgedTraj`, `SafeStep`, `MaximalBridge`): `~/git/lean/LeanProofs/Admissibility/SafetyBridge.lean`.
