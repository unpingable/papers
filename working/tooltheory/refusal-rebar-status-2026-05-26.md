# RefusalRebar status — 2026-05-26

**Status:** State receipt for the day's Lean spike work in `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean`. Not a memo, not a doctrine update — just a pin for where the file landed and what the next pressure points are.

**Posture:** Receipt only. No public surface change. No `CalculusOne.lean` change. No `[1.0]` tags. No 2.0 promotion. Pinned at end-of-day 2026-05-26 with `lake build` green at 8298 jobs.

---

## What changed

Four moves landed in `RefusalPropagation.lean` during the day:

1. **Labelwatch adapter** (`Admissibility.RefusalPropagation.Annex.Labelwatch` namespace) — third substrate-level instantiation of `Composition.refusal_composes_two_hop`. Models the feature → finding → claim ladder. Same Lean structure as `NQDependency` / `NQOnNQ`; substrate-domain distinct (social telemetry vs hardware vs cross-instance NQ).

2. **Transitive closure** in `Composition` namespace:
   - `DependsTrans` inductive (`base` + `step` constructors) — a minimal path relation over `requiredFor`, without edge metadata.
   - `refusal_propagates_transitively` theorem — refusal at any ancestor propagates along the chain to any transitive descendant, by induction on chain length.

3. **NQ fan-out** (`Admissibility.RefusalPropagation.Annex.NQFanOut` namespace) — first structurally-distinct shape: m-to-1 fan-in instead of linear chain. `fleet_cannot_bind_when_any_ancestor_refused` parameterized over the ancestor; all-must-pass via cascade applied per-ancestor independently. No quorum, no weights, no probabilistic verdicts, no `Multiset`.

4. **Runtime conformance** (`publish.rs` masking-cascade) — cost-check **failed honestly**. Modeling the function would need warning_state, MASKING_RULES with string-prefix matching, absent_gens counter, recovery_window, self-loop prevention, and generation/upsert interaction. ~150–250 lines, well over the <100-line bounded-cost guidance. Parked with specific scoping note: the masking cascade is too entangled with NQ's state machine for honest annex modeling.

---

## What this proves

1. **The same generic law carries multiple substrate domains.** `Composition.refusal_composes_two_hop` reproduces the local contract over (hardware basis chain) AND (cross-instance NQ aggregate) AND (social-telemetry feature→claim ladder). Portability is the find; the abstraction is doing work, not decorating.

2. **Refusal propagation extends to finite chains of any length.** `DependsTrans` + `refusal_propagates_transitively` generalize `refusal_composes` and `refusal_composes_two_hop`. Ready as the formal shape for TESTIMONY_DEPENDENCY V2 when NQ ships multi-level.

3. **Fan-in refusal is expressible without quorum semantics.** All-must-pass is the cascade applied per-ancestor; no aggregation algebra needed. The fan-out direction's brakes held during implementation, not just in the gate.

---

## What this does not prove

1. **No runtime conformance.** The masking-cascade function is not modeled. Gap docs and tests suggest a candidate mapping to `CascadeSound`, but this note supplies neither a complete mapping nor a runtime evidence/refinement package.

2. **No public 2.0.** `CalculusOne.lean` is untouched. The 1.0 compatibility claim is unchanged. Nothing in `RefusalPropagation.lean` has a `[1.0]` tag.

3. **No cross-kernel composition.** All composition machinery in `Composition` namespace operates over a single generic `requiredFor` relation; it does not compose between distinct refusal-kernel families (`SurfaceAuthorization`, `FiatAdmissibility`, etc.).

4. **No claim graph.** `DependsTrans` is a minimal path relation — base + step constructors, nothing more. No edge metadata, no scope, no time, no use-kind, no provenance.

5. **No production-side conformance.** The instantiations are formal-side only; consumers have not been mapped and wired through, and no runtime evidence or refinement argument establishes that their behavior satisfies these theorems. Citation, if added, would identify the intended contract but would not by itself close this gap.

---

## Public Phase D promotion status (2026-05-26 wording)

The previous "unmet" framing on Criterion 1 was too coarse. This table governs public Phase D promotion, not permission to continue theorem development. Current policy also requires an explicit mapping plus runtime evidence or refinement for any conformance claim; a production fixture's citation alone is insufficient.

| Criterion | Status |
|---|---|
| 1. Composition between kernels | **Partially satisfied at the generic dependency-relation level** (`refusal_composes` / `_two_hop` / `_propagates_transitively` form a small calculus over a single `requiredFor` relation); **not yet satisfied at the cross-kernel / public-calculus level** (no composition between distinct refusal-kernel families). |
| 2. New abstraction count | Within budget. `DependsTrans` is one new inductive (2 constructors); adapters per consumer are duplicated, not generalized. |
| 3. Promotion evidence | **Multiple candidate consumers with Lean instantiations** (NQ-on-NQ, Labelwatch); **no production fixture with an explicit mapping and behavioral evidence** yet. The dated framing moved from "candidate identified" to "candidates with Lean-side anchors, awaiting consumer-side evidence." |
| 4. Slogan-blast-radius | Unchanged. Keepers stay honest. |
| 5. PL/UC stays as working notes | Unchanged. Lean reserves still not built. |

Public Phase D **remains closed** under this receipt's criteria. Criterion 1's strict reading still requires composition between distinct kernels, and criterion 3 still requires production-side promotion evidence. Neither condition blocks further formal work.

---

## Next pressure points

Three pressure points the next audit should evaluate, in order of likely fire:

1. **Shared adapter extraction audit.** Three chain-shaped adapters now duplicate the same seven-element machinery (`State` / `Refused` / `CascadeSound` / `BindingAdmissible` / `RequiredFor` / `WitnessesInSnapshot` / `cascade_implies_basis_inheriting`). "Rule of three = after three, inspect" is the standard reading. The duplication did evidentiary work; that work is now collected. The extraction decision turns on whether the repeated adapter is genuinely generic and whether the refactor preserves the brakes—not on a runtime forcing case.

2. **Production mapping and evidence.** A real NQ test or labelwatch integration that maps behavior to `refusal_composes_two_hop` / `refusal_propagates_transitively` and supplies behavioral evidence would strengthen the public-promotion case. An external Lean importer supplies formal reuse, not runtime conformance; citation alone closes neither mapping nor evidence. None exists yet. The next consumer-side step (likely NQ TESTIMONY_DEPENDENCY V2's design conversation) is a natural correspondence target.

3. **Bounded cascade helper extraction from NQ.** Runtime conformance failed at the function level because `publish.rs:1294-1382` is monolithic. If NQ ever extracts a smaller helper — e.g., a pure `should_suppress : (Host, Kind, MaskingRules, ObservedParents) → Bool` separated from generation/upsert state — runtime conformance becomes re-evaluable. Currently the function is too entangled; this is an NQ-side refactor pressure, not a Lean-side gate.

---

## File state

`RefusalPropagation.lean` now carries seven namespaces:

| Namespace | Role |
|---|---|
| `Narrowing` | C.1 — refusal narrowing (case analysis over existing tables) |
| `Composition` | C.2 — `refusal_composes` + `refusal_composes_two_hop` + `DependsTrans` + `refusal_propagates_transitively` |
| `NQDependency` | C.3/C.4/C.5 — hardware basis chain (device → smart → disk) |
| `NQOnNQ` | aggregate cross-instance NQ chain (nq_a → nq_b about nq_a → fleet); includes `no_self_requiredFor` guard |
| `Labelwatch` | social-telemetry feature → finding → claim ladder |
| `NQFanOut` | m-to-1 fan-in (a1, a2 → fleet) |
| (Composition extensions) | three composition theorems live here, not in a separate namespace |

`lake build` green at 8298 jobs. `CalculusOne.lean` untouched. No public surface change.

---

## Cross-references

- `~/git/lean/LeanProofs/Admissibility/RefusalPropagation.lean` — the file this receipt summarizes.
- `~/.claude/plans/i-want-a-plan-groovy-stardust.md` — Phase C/D versioning plan.
- [[refusal-kernel-to-refusal-receipt-seam]] — parent operator-family seam.
- [[nq-testimony-dependency-contract.md]] — contract receipt for NQDependency adapter; references the C.4/C.5 dual proof.
- [[nq-forcing-case-audit.md]] — original B classification (potential consumer, no production blocker).
- [[nq-on-nq-forcing-case.md]] — candidate forcing case for aggregate cross-instance refusal.
- [[labelwatch-driftwatch-admissibility.md]] — substrate doc that informed the labelwatch adapter.
- [[uncertainty-custody]] / [[projection-laundering]] — sibling working notes (gate-side, projection-side); Lean reserves still not built.
- [[compression-becomes-authority-vocabulary]] — essay-vocabulary parent for projection-laundering.

---

## Keepers

> **The formal layer is now leading.**

> **DependsTrans is path-shaped without path metadata.**

> **Three chain adapters is audit-worthy duplication.**

> **The annex's deletion clause is the safety mechanism; the bounded-cost-plus-substrate gate is the discipline.**

---

## Provenance

- **2026-05-26.** Day's work produced labelwatch adapter, transitive closure, fan-out, and runtime conformance cost-check. Other-claude's mid-day correction reframed the annex gate from shipping-discipline ("wait for forcing case") to construction-discipline ("substrate exists + bounded cost + brakes survive"). ChatGPT's end-of-day review accepted the corrections and pinned two real points: DependsTrans is path-shaped (no metadata is the surviving brake), and shared-adapter extraction is now audit-worthy rather than held.
- **Filed:** claude-code, 2026-05-26, after operator routed ChatGPT's review.

> **Receipt is filed. The hose remains visible.**
