# Two generic RTC encodings — dedup debt (CANDIDATE)

**Status:** CANDIDATE / non-binding. A handle for review, NOT authorization to
build. No forcing case yet; resolve when reachability consumers stabilize.

**Filed:** 2026-06-30 (operator-requested, post reachability-consolidation slice).

## The debt

After codex's reachability/closed-lane consolidation slice landed (`~/git/lean`,
2026-06-29), the tree now carries **two generic reflexive-transitive-closure
encodings** of the same shape:

- `LeanProofs/TaxonomyGraph.lean` — `Reachable` (:232) and the robustness
  twin `ReachableBy {α} (E)`, with `reachableBy_stays_in_closed` /
  `no_reach_of_closed_lane` (axiom-free).
- `LeanProofs/Admissibility/ReachabilityClosure.lean` — `Reach`, with
  `ClosedUnder` / `reach_stays_in_closed` / `no_reach_of_closed_lane` /
  `ClosedLaneRefusal`.

Same RTC shape, same closed-lane obstruction theorem, two homes.

## Why it exists (deliberate, not sloppy)

The duplication is an **axiom-isolation decision**, not autocomplete. Historically
`TaxonomyGraph` carried the `persistence_normalizes` axiom; `ReachabilityClosure`
was built import-free precisely so a static reachability claim there could not
inherit a dynamic/documentary axiom. The `#print axioms` check confirms the
payoff: the pure `ReachabilityClosure`/adapter theorems are zero-axiom. So the
two-encoding state is currently *justified* and *honest* — codex flagged it in
`docs/WITNESSED-FRONTIER-REGISTER.md` direction #4 ("retire/adapter-localize
duplicate RTC shapes as those consumers stabilize"). Note: `TaxonomyGraph`'s
`persistence_normalizes` was since removed (A′ step 2, demotion shim), which
*weakens* the original isolation rationale — worth re-checking whether the two
encodings still need to be separate, or whether one can now adapter-localize to
the other without re-importing a forbidden axiom.

## Why it's debt (the smell to watch)

Two RTC encodings is exactly the **re-derive-under-new-vocabulary** shape the
kernel-overlap-audit doctrine warns about (`[[feedback-kernel-overlap-audit]]`).
It is honest *only while flagged*. Left to fossilize, a future reader can't tell
the duplication was deliberate axiom-hygiene vs. an orphan re-derivation, and the
closed-lane theorem now has two maintenance sites that can drift.

## Resolution trigger (forcing case, not now)

Resolve when reachability consumers stabilize — concretely, when the Nightshift
forcing case fires and `ConversionRouter.lean` gets built (the 2-theorem delta
over `TaxonomyGraph`, see `conversion-router-candidate.md` and
`[[project-tooltheory-lean-incubation]]`). At that point decide ONE of:

1. Pick `TaxonomyGraph.ReachableBy` (edge-parameterized) as the single generic
   RTC and adapter-localize `ReachabilityClosure.Reach` onto it — IFF the
   post-demotion axiom footprint stays clean (re-run `#print axioms`).
2. Keep both but make one provably an adapter of the other (one `iff` theorem),
   so there is a single source of truth even if two names survive.

Do NOT mint a third encoding. Do NOT build either resolution speculatively —
this note is the handle, the forcing case is the authorization.

## Receipts

- Consolidation slice reviewed green 2026-06-30: full `lake build` EXIT 0,
  sorry/axiom-free, `check-custody-classes.sh` OK (55 files), adapters zero-axiom
  / embedding lemmas `propext`-only (no new axiom).
- Codex's own flag: `docs/WITNESSED-FRONTIER-REGISTER.md` direction #4.
