# Axis 2 — Composition Boundary

**Status:** Design / extraction note (2026-06-01; updated 2026-06-01 with Slice 1b + Finding 3 resolution). Two forcing-case slices landed with local positive objects + a guard-collapse probe + a load-bearing-freshness in-substrate confirmation. Third slice (demoted `ConflictMerge`) preserved with negative only. Generic `MergeAdmissible` deliberately **NOT yet minted**. Filed alongside `working/axis-2-composition-forcing-cases.md` (the per-slice catalog) — this note is the spine that captures what extraction found.

**Provenance:** Multi-model conversation 2026-06-01 (ChatGPT analysis → second Claude session → Claude Code integration). The extraction step from local positive objects to a generic abstraction surfaced three concrete constraints. The third — observable plurality — was resolved by an interferometer probe: three uncorrelated paths (two Claude sessions, one ChatGPT) independently arrived at the same guard-variant specimen, which then collapsed freshness into a value guard. The convergence is the result; the doctrine line "freshness is admissibility basis, not a defended value unless explicitly promoted as terminal" went behind glass.

---

## Core claim

Local bridge evidence is **scoped**. It does not automatically survive reconciliation. Different reconciliation failures require different missing evidence: joint resource bounds, freshness at merge time, and merge-policy preservation. The composition axis is the catalogue of those scopes plus the admissibility evidence that repairs each.

## Slice status

```
Slice 0   SharedBudgetMerge    joint-margin failure        maximal bridge      negative + positive + frame + traj
Slice 1   StaleEvidenceMerge   temporal-horizon failure    non-maximal bridge  negative + positive + frame (trivial) + traj (trivial) + basis (non-trivial)
Slice 1b  StaleEvidenceMerge   freshness made load-bearing (useEvidence guard) negative + positive
Probe     GuardCollapse        freshness ⟺ value-preservation on graded value  collapse witness
Slice 2   ConflictMerge        reconciliation-policy loss  maximal bridge      negative + positive + frame + traj
Generic   ParameterizedMerge   MergeFrame + Value + Composes + Basis           three slices at value/traj; Slice 1 at basis
```

**Triad complete (2026-06-01).** All three forcing-case dimensions now carry both negative keepers and local positive objects, and all three instantiate the generic `MergeFrame` schema with `MergeRestoresValue`. Slice 1's instantiation is deliberately trivial — the value-restoration shape catches Slices 0 and 2 non-vacuously; Slice 1's non-trivial content lives at the basis layer (`MergeRestoresBasis`, deferred).

Each non-degenerate slice now carries BOTH a negative keeper (the bad merge) AND a local positive object (the admissibility evidence that restores composition). That is the move from "cabinet of corpses" to "calculus": every corpse has a coroner's report naming the cause of death and the evidence that would have prevented it.

### Slice 0 — SharedBudgetMerge

- **Negative:** `locally_bridged_fragments_can_merge_to_value_loss`. Two locally viable branches (each `spend 6` under cap 10) merge to over-cap → value 0.
- **Missing evidence:** joint usage at the reconciliation boundary.
- **Positive object:** `BudgetMergeOk a b := a.used + b.used ≤ a.cap` (`σ → σ → Prop`).
- **Restoration:** `budget_merge_restores` — `BudgetMergeOk sA sB` ⟹ merged endpoint viable.
- **Characterization:** `budget_merge_viable_iff_admissible`.

### Slice 1 — StaleEvidenceMerge

- **Negative:** `locally_bridged_branches_can_merge_with_stale_evidence`. Two branches bridged at action time (now 5 ≤ horizon 10) reconcile at `t = 12` → stale.
- **Substrate obstruction:** `no_safeStep_from_stale_merged` (the stale merged state admits no further `SafeStep`).
- **Missing evidence:** freshness at the reconciliation time.
- **Positive object:** `StaleMergeOk t a b := t ≤ min a.exp b.exp` (**`Nat → σ → σ → Prop`** — note the merge parameter).
- **Restoration:** `stale_merge_restores` — `StaleMergeOk t sA sB` ⟹ merged state fresh. Restores **freshness**, not value (the slice isolates temporal non-portability; `merged_value_preserved` shows value is untouched).
- **Characterization:** `stale_merge_fresh_iff_admissible`.
- **Non-maximal:** Also the first non-maximal-bridge specimen; `timed_bridge_not_maximal` proves the bridge is strictly stronger than preservation.

### Slice 2 — ConflictMerge (degenerate corner)

- **Negative:** `locally_bridged_fragments_can_merge_to_value_loss` (over `mergeEnv`). Two locally bridged branches with incompatible owners merge to `clean := false` by fiat.
- **Why degenerate:** the value loss is *written into* `merge` (manual flip on conflict), so the `BridgedTraj` witnesses do no work in the proof. Useful as the third dimension of `MergeAdmissible` (merge-policy preservation), not as a branch-local-scope failure.
- **Missing evidence:** policy-preservation (owner compatibility).
- **Positive object (2026-06-01):** `ConflictMergeOk a b := compatibleOwner a.owner b.owner = true` (`σ → σ → Prop`, `Param = Unit`).
- **Restoration:** `conflict_merge_restores` — under cleanness preconditions and `ConflictMergeOk sA sB`, merged endpoint is viable.
- **Characterization:** `conflict_merge_viable_iff_admissible` (under `a.clean = true ∧ b.clean = true`). The cleanness precondition is what isolates the policy-specific dimension; an unclean input would falsify viability regardless of compatibility.

## The extraction findings — why the generic is deferred

ChatGPT's original sketched generic was:

```lean
structure MergeAdmissible (E : SafetyEnv σ α ρ) (merge : σ → σ → σ)
    (MergeOk : σ → σ → Prop) : Prop where
  preserves : ∀ {a a' b b'}, BridgedTraj E a a' → BridgedTraj E b b' →
              MergeOk a' b' → E.value (merge a b) ≤ E.value (merge a' b')
```

Building the two positive objects shows this shape is **wrong in arity**, and the slices caught it before it got minted:

### Finding 1 — Merge is not uniformly `σ → σ → σ`

- Slice 0's merge: `merge : σ → σ → σ`.
- Slice 1's merge: `mergeAt : Nat → σ → σ → σ` — the reconciliation **time** is a parameter of the operator, not a field of either endpoint.

The unifying merge is `merge : Param → σ → σ → σ`, with budget the `Param = Unit` degenerate case.

### Finding 2 — `MergeOk` must therefore see the merge parameter

- Budget's `BudgetMergeOk : σ → σ → Prop`.
- Stale's `StaleMergeOk : Nat → σ → σ → Prop`.

The naive `MergeOk : σ → σ → Prop` cannot host the stale case. Corrected shape: `MergeOk : Param → σ → σ → Prop`.

### Finding 3 — Freshness collapses into bridge basis (RESOLVED 2026-06-01)

The Slice 1 observable-plurality concern does NOT force a per-slice observable parameter.

**The probe.** `GuardCollapse.lean` tests the question directly with a graded value (authority : Nat) and a value-affecting action (`withdraw`) gated by freshness. The result, `withdraw_preserves_iff_fresh`: for a state with positive authority,

```
value s ≤ value (run s .withdraw)   ↔   fresh s
```

On a value-affecting action, freshness *is* value-preservation. The freshness conjunct is redundant on that fragment (`fresh_conjunct_redundant_on_withdraw`), and a maximal value-only bridge already forbids the stale withdrawal (`maximal_bridge_forbids_stale_withdraw`).

**Why Slice 1 looked plural.** Slice 1's actions were `tick`/`noop` — value-inert. On value-inert actions, preservation holds whether fresh or stale (`noop_preserves_regardless`), so `fresh ∧ preserves` was strictly stronger than `preserves` — Slice 1's `timed_bridge_not_maximal` is genuinely true. But the non-maximality is **stakes-free**: it forbids a stale noop, and a stale noop costs nothing. Freshness looked independent precisely because it was decoupled from any value consequence — which is the opposite of being an independent *defended* observable.

**Slice 1b confirms in-substrate.** `stale_useEvidence_authorized_not_safe` (in `StaleEvidenceMerge.lean`) ties the abstract collapse to the actual `merged` state. The same authorized action `useEvidence`:
- preserves value and admits a `SafeStep` from the *fresh* early merge (`fresh_useEvidence_preserves_and_safe`);
- drops value and admits no `SafeStep` from the *stale* late merge.

So freshness loss is load-bearing because it permits an authorized value drop and blocks bridge construction. Slice 1 stops "floating."

**Consequence for the generic.** The `Obs : σ → Nat` per-slice observable parameter is **cut**. There is one defended observable (value). Do not genericize over "whatever this slice cares about" — that is how calculi become soup. The generic instead needs *basis / continuation* fields alongside value preservation:

```
Param → σ → σ → σ       -- merge may have external parameters
Param → σ → σ → Prop    -- merge admissibility predicate
Single defended value remains.
MergeAdmissible preserves: (1) value floor, where relevant;
                           (2) bridge basis / continuation-readiness,
                               where the bridge has preconditions like freshness.
```

### Doctrine line (behind glass)

> Freshness is not a defended value unless explicitly promoted as terminal. By default, freshness is *admissibility basis*: it matters because stale evidence may fail to guard future value-preserving action.

This avoids both errors: reducing every evidence condition to current `value` (loses the basis structure), and promoting every basis condition into its own defended value (soup). The right shape is **one defended value; multiple admissibility bases that protect it.** The anti-soup discipline is: a basis condition earns "terminal observable" status only by explicit modeling commitment (e.g. auditability or accountability defended for its own sake), never by default and never inherited from freshness bookkeeping.

### Honest fork (NOT decided)

Genuine observable plurality remains *available* if the doctrine wants to defend some property (auditability, accountability) for its own sake rather than because it protects value. That is a deliberate modeling commitment to a second irreducible observable, which must be argued on its own terms — it cannot be inherited for free from freshness, because freshness, as shown, reduces to a value guard. This is a doctrine question, not a Lean question: which of the framework's defended values are terminal vs. instrumental? Default is instrumental. Promotion requires explicit argument.

### Why this matters

This is exactly the "ontology goblin gets tenure" failure: the gorgeous abstraction with three examples bent around it. The local objects exist; the generic does not; and we now have a **recorded constraint set** the generic must satisfy rather than a guess. Had we minted ChatGPT's sketched generic after Slice 0, we would have baked in the wrong arity and bent Slice 1 around it. **Extraction found a real constraint, not a cosmetic one.** This is the strongest argument so far *for* "local versions first, extract second."

### Corrected candidate generic (still NOT minted; `Obs` cut per Finding 3)

```lean
structure MergeAdmissible
    (E : SafetyEnv σ α ρ) {Param : Type}
    (merge : Param → σ → σ → σ)
    (MergeOk : Param → σ → σ → Prop) : Prop where
  preserves_value :
    ∀ {p a a' b b'}, BridgedTraj E a a' → BridgedTraj E b b' →
    MergeOk p a' b' → E.value (merge p a b) ≤ E.value (merge p a' b')
  preserves_basis :
    -- bridge-basis / continuation-readiness condition; shape pending Slice 2
    True
```

Single observable (`E.value`). `MergeOk` carries the merge parameter (Finding 2). A second field is reserved for the basis/continuation dimension; its exact shape is left open until Slice 2's policy-preservation dimension lands and forces it. Do not mint until then.

## `MergeAdmissible` dimensions earned so far

```
joint-resource condition      — Slice 0  (BudgetMergeOk)         [Param = Unit]
freshness-as-basis condition  — Slice 1  (StaleMergeOk)           [Param = Nat]
policy-preservation condition — Slice 2  (ConflictMergeOk)        [Param = Unit]
                                  (under cleanness precondition)
```

All three landed 2026-06-01. The eventual generic is the conjunction that clears all three, over a parameterized merge (`Param → σ → σ → σ`), preserving a single defended value plus the bridge-basis conditions that keep it constructible. Each slice instantiates `Param` differently — that arity finding (Finding 1) survives all three specimens.

## Sequence discipline (do not skip)

1. ✅ Slice 0 negative + positive (`BudgetMergeOk`, `budget_merge_restores`, `budget_merge_viable_iff_admissible`).
2. ✅ Slice 1 negative + positive (`StaleMergeOk`, `stale_merge_restores`, `stale_merge_fresh_iff_admissible`) + obstruction (`no_safeStep_from_stale_merged`) + non-maximal proof (`timed_bridge_not_maximal`).
3. ✅ Slice 1b: freshness made load-bearing (guard variant on the real merged state via `useEvidence`; `fresh_useEvidence_preserves_and_safe`, `stale_useEvidence_authorized_not_safe`) + abstract collapse probe `GuardCollapse.lean` (`withdraw_preserves_iff_fresh`, `maximal_bridge_forbids_stale_withdraw`). Observable-plurality question RESOLVED: freshness is basis, not a second value.
4. ✅ Slice 2: policy-preservation positive object (`ConflictMergeOk`, `conflict_merge_restores`, `conflict_merge_viable_iff_admissible` under cleanness). Three forcing-case dimensions complete.
5. ✅ Generic extraction — `ParameterizedMerge.lean` (scratch, not root-wired): `MergeFrame Param σ α ρ E` structure (`merge`, `MergeOk`); `MergeRestoresValue F` boundary predicate (carries input viability separately — Slice 2's cleanness fork resolved by NOT folding viability into `MergeOk`); `MergeComposesBridgedEndpoints F` trajectory-facing predicate (defined, not instantiated). Three instantiations: `budgetFrame` (Param = Unit), `staleFrame` (Param = Nat), `conflictFrame` (Param = Unit). All three prove `MergeRestoresValue` — but Slice 1's proof is *trivial* (the `_ok` hypothesis is unused; value is preserved at the boundary unconditionally via `valueOk := a.valueOk && b.valueOk`). That asymmetry is the diagnostic, not a bug: Slice 1's non-vacuous restoration lives at the basis layer, captured by `GuardCollapse` + Slice 1b. A `MergeRestoresBasis` companion predicate is filed deferred for the basis-layer instantiation.
6. ✅ Cross-slice trajectory-layer instantiations (2026-06-01): `budgetFrame_composes`, `staleFrame_composes`, `conflictFrame_composes` all prove `MergeComposesBridgedEndpoints`. Method: case-split on `value s ∈ {0, 1}`; viable case discharges via the `*_restores` boundary theorem, non-viable case propagates via the merge structure (additive usage for Budget, conjunctive `valueOk` for Stale, both merge branches yield `clean = false` for Conflict). Diagnostic preserved: `staleFrame_composes` does NOT use the `StaleMergeOk` hypothesis — that's the right outcome, hand-off to step 7. Module builds green, full `lake build` green sorry-free.
7. ✅ `MergeRestoresBasis` companion predicate + Slice 1 instantiation (2026-06-01). Three pieces in `ParameterizedMerge.lean`: (a) `MergeRestoresBasis F Guard` — generic predicate; `Guard : σ → Prop` carried as parameter, NOT a frame field (slices without a basis story don't instantiate). (b) `staleFrame_restores_basis : MergeRestoresBasis staleFrame evidenceFresh` — Slice 1's non-vacuous content; discharges via `mergeAt_within_horizons_stays_fresh`. (c) `useEvidence_preserves_iff_fresh` — TimedState analog of `GuardCollapse.withdraw_preserves_iff_fresh`, confirming within Slice 1's own model that freshness is guard, not parallel observable. (d) `stale_basis_carries_useEvidence_value` — the rent payment: merge admissibility ⟹ merged-state freshness ⟹ `useEvidence` preserves value at merged. Single defended observable preserved; freshness stays instrumental. Module + full `lake build` green sorry-free.
8. ✅ Necessity (task 3 exploration, 2026-06-01). Two dual predicates added: `MergeOkNecessaryAtValue F` and `MergeOkNecessaryAtBasis F Guard`. Per-slice verdict: Budget ✓ (`budgetFrame_value_necessity`), Conflict ✓ (`conflictFrame_value_necessity`, **unconditional** — the cleanness preconditions on the existing iff are needed for the iff-with-positive-witness form but not for the necessity direction; the incompatible branch always writes `clean = false` directly), Stale **fails positively at value layer** (`staleFrame_value_necessity_fails`, witnessed by `mergeAt 12 aEnd bEnd`) and ✓ at basis layer (`staleFrame_basis_necessity`, Guard = `evidenceFresh`). **Verdict: schema, not single generic theorem.** No layer-uniform generic necessity exists — Stale's content lives at the basis layer, and forcing it into a value-layer iff would require distorting either the frame (per-slice layer indicator) or stale (artificial value-affecting merge). The honest formulation is slice-indexed characterization at the per-slice layer (Budget/Conflict at value, Stale at basis), mirroring the sufficiency structure. Composes with the keystone (`BoundaryWitness.lean`): both refuse the single-grand-theorem collapse. Module + full `lake build` green sorry-free.
9. ⏸ Axis 3 (self-amendment): PARKED BY CURRENT PRIORITY. Axis 2 now has both sufficiency and necessity at the appropriate per-slice layers. Axis 3 may nevertheless open from a coherent scoped statement, model, or countermodel before a second runtime specimen exists, and that formalization may lead later implementation. A further specimen would supply stress-test and priority evidence, not permission to formalize. The intrinsic discriminator remains: do not disguise fixed-value transition or merge work as self-amendment.

Do not let "freshness collapses" become "basis conditions don't matter." The right simplification is one defended value; multiple admissibility bases that protect it.

## Honesty ledger on the bridge hypotheses

Both `_restores` theorems carry the `BridgedTraj` hypotheses underscore-bound. Under Boolean viability they are framing, not load-bearing — the conclusion follows from the admissibility evidence alone. Stated rather than hidden. The trajectory hypotheses start earning their keep only when `value` grades (rather than being Boolean), which is a future tier. Each slice also has a negative/positive meeting point as an iff (`budget_merge_viable_iff_admissible`, `stale_merge_fresh_iff_admissible`) — the bad case and the restoration are the two corners of one characterization.

## Paper consequence (deferred)

Axis 1's no-lift theorem reads, in retrospect, as the single-trajectory base case of the composition result: *a value-losing endpoint admits no bridged trajectory* is the n=1 instance of *value-losing reconciliation admits no bridged composition*. That reframing — **no-lift as base case, composition boundary as center of gravity** — is the `paper.md` move that makes the suite a calculus rather than Axis 1 plus annexes. Defer until Slice 2 has its positive object and the generic is minted.

## Cross-references

- Per-slice catalog: `working/axis-2-composition-forcing-cases.md`.
- Slice 0 module: `~/git/lean/LeanProofs/Admissibility/BudgetMerge.lean`; result note: `working/tooltheory/axis-2-slice-0-shared-budget-merge.md`.
- Slice 1 module: `~/git/lean/LeanProofs/Admissibility/StaleEvidenceMerge.lean`; result note: `working/tooltheory/axis-2-slice-1-stale-evidence-merge.md`.
- Slice 2 module: `~/git/lean/LeanProofs/Admissibility/MergeConflict.lean`; result note: `working/tooltheory/axis-2-slice-2-conflict-merge.md`.
- Axis 1 substrate (`SafetyEnv`, `BridgedTraj`, `SafeStep`, `MaximalBridge`, the characterization layer): `~/git/lean/LeanProofs/Admissibility/SafetyBridge.lean`.
- Suite plan: `working/admissibility-suite-map.md`.
- Composition-altitude candidate family designation under audit: [`local-global-validity-gap.md`](local-global-validity-gap.md). LGVG remains a candidate primitive; the Axis-2 substrate work in this note was the empirical test of its single-primitive promotion claim. Audit receipt: [`vector-mining/2026-06-05-composition-substrate-vs-lgvg.md`](vector-mining/2026-06-05-composition-substrate-vs-lgvg.md). The Step 8 schema-vs-theorem verdict (*"refuses single-grand-theorem collapse... composes with the keystone (`BoundaryWitness.lean`)"*) is the substrate-side answer to LGVG-as-single-primitive: refused. The family-designation reframe (LGVG at composition altitude as sibling to [`admissibility-decay-family-note.md`](admissibility-decay-family-note.md) at decay altitude) is filed as candidate, NOT ratified.
