# Composition-axis substrate × Local-Global Validity Gap

**Filed:** 2026-06-05. **Status:** vector-mining pilot output. **Mode:** gap detection only. **Cumulative pilot #10.** **Confidence:** high (substrate work has already done much of the audit internally; the question reduces to interpreting the schema-vs-theorem verdict against LGVG's promotion claim).

## Verdict

> **GAP CONFIRMED BUT NOT FORCED — and the substrate work generates positive evidence *against* LGVG-as-single-primitive, not merely "doesn't force ratification."**

The Axis-2 specimen family (Slice 0 / Slice 1 / Slice 1b / GuardCollapse probe / Slice 2 / `ParameterizedMerge` schema) establishes a complete per-axis schema for *merge* admissibility, deliberately refuses the single-grand-theorem collapse, and composes with the BoundaryWitness keystone in that refusal. That is the federation doctrine ([[project-no-unifier-without-laundering]]) being instantiated at the composition axis — exactly the same shape attack #5 found at the discharge axis. Under that posture, LGVG-as-primitive is not unforced; it is *refused as a single primitive*. LGVG may survive as a descriptive family designation at the composition altitude (sibling to [[project-admissibility-decay-family]]) or as a paper-shape reframe ("no-lift as base case, composition boundary as center of gravity"), but not as a unified composition theorem.

## Corpus artifacts consulted

- `working/local-global-validity-gap.md` (2026-05-10): the candidate primitive itself; four axes (drift / coupling / saturation / mimicry) as test cases; anti-laundering target; explicit anti-promotion rules.
- `working/axis-2-composition-boundary.md` (2026-06-01 — extraction spine note): Finding 1 (merge takes Param), Finding 2 (`MergeOk` carries Param), Finding 3 (`Obs` cut — freshness is basis, not parallel observable), Step 8's necessity verdict.
- `working/axis-2-composition-forcing-cases.md` (2026-06-01 — per-slice catalog): three slices' negative/positive shapes; "do not start with `MergeAdmissible` as a beautiful abstraction."
- `LeanProofs/Admissibility/StaleEvidenceMerge.lean` (UNRATIFIED-CANDIDATE, in context): Slice 1 + 1b material; `no_safeStep_from_stale_merged`; `MergeAdmissible` open design question.
- `LeanProofs/Admissibility/BudgetMerge.lean` (referenced by doctrine note; not loaded — gap-detection mode does not require full Lean text when the doctrine note carries the keepers); `MergeConflict.lean`; `GuardCollapse.lean`; `ParameterizedMerge.lean`; `LocalBoundary.lean` (sufficiency-only proof that already exists per axis-2 cross-references).
- `working/bridge-obligation-lattice.md` (in context): five obligation atoms; relevant for the *which atom* per slice.
- `working/no-unifier-without-laundering.md` (in context): the federation discipline the substrate work composes with.
- [[project-admissibility-decay-family]] (in context): five-axis family; LGVG is the composition/scope row as a *candidate primitive*, not the family designation.

## Specimen-by-specimen table

| Slice | Module | Local validity preserved | Global validity broken | Bridge | Already covered by existing theorem? | Obligation atom (per bridge-obligation-lattice) |
|---|---|---|---|---|---|---|
| 0 | `BudgetMerge` | each branch's spend within local cap (`spend 6 ≤ 10`) | joint usage exceeds shared cap (`6 + 6 > 10`); merged endpoint non-viable | maximal | `locally_bridged_fragments_can_merge_to_value_loss` + `budget_merge_restores` + `budget_merge_viable_iff_admissible` | resource accounting (not a named atom in the lattice; closest sibling: coverage/preservation at workflow altitude) |
| 1 | `StaleEvidenceMerge` | each branch bridged at action time within horizon | reconciliation at `t > inherited horizon`; merged evidence stale | NON-MAXIMAL (`evidenceFresh ∧ value preserves`) | `locally_bridged_branches_can_merge_with_stale_evidence` + `stale_merge_restores` + `no_safeStep_from_stale_merged` + `timed_bridge_not_maximal` | **freshness** (atom 4 in the lattice) |
| 1b | `StaleEvidenceMerge` (useEvidence guard) | same as Slice 1 plus action-time guard | stale merged state admits authorized `useEvidence` that drops value, no `SafeStep` | non-maximal | `stale_useEvidence_authorized_not_safe` + `GuardCollapse.withdraw_preserves_iff_fresh` | **freshness made load-bearing** (Finding 3 collapsed to basis) |
| 2 | `MergeConflict` | each branch individually viable (`clean = true`) | merge policy flips `clean := false` on incompatible owners | maximal | `locally_bridged_fragments_can_merge_to_value_loss` (over `mergeEnv`) + `conflict_merge_restores` + `conflict_merge_viable_iff_admissible` (under cleanness) | **type-fidelity** at the policy-preservation altitude; closest: anti-precedent + type-fidelity per lattice composition |
| Schema | `ParameterizedMerge` | — (generic) | — (generic) | both maximal and non-maximal | `MergeRestoresValue` + `MergeComposesBridgedEndpoints` + `MergeRestoresBasis` + `MergeOkNecessaryAt{Value,Basis}` | spans atoms by Param indexing |

The common shape is established: `Param → σ → σ → σ` operator, branch-local-scope-bridge that does NOT imply globally-bridged composition, plus per-slice admissibility evidence that *restores* the failure mode each slice isolates.

The shape that is NOT established: a single composition theorem across all slices. Per Step 8 of axis-2-composition-boundary (necessity exploration, 2026-06-01):

> **Verdict: schema, not single generic theorem.** No layer-uniform generic necessity exists — Stale's content lives at the basis layer, and forcing it into a value-layer iff would require distorting either the frame (per-slice layer indicator) or stale (artificial value-affecting merge). The honest formulation is slice-indexed characterization at the per-slice layer (Budget/Conflict at value, Stale at basis), mirroring the sufficiency structure. **Composes with the keystone (`BoundaryWitness.lean`): both refuse the single-grand-theorem collapse.**

## What LGVG would add (beyond the specimens)

LGVG, as filed in 2026-05-10, claims:

1. **Cross-axis recurrence.** Four axes (drift / coupling / saturation / mimicry) instantiate the same gap shape. The substrate covers ONE axis (merge composition, closest to *coupling* under shared substrate but not cleanly any single axis).
2. **A single unifying primitive.** Some object — "missing proof obligation between local validity and global continuity" — that the four axes are surfaces of. Sheaf vocabulary available as probe; explicit "kernel vocabulary unstable."
3. **A field-shaped contribution.** "Field-shaped because the same structural failure recurs across substrates with different local costumes."

Each of these is *additional* to what the substrate specimens prove. The specimens give a worked schema at one axis with three forcing cases; they do not (and cannot, without other substrates) establish the four-axis recurrence or the unifying primitive.

## What the specimens already prove

1. **A common operator shape:** `Param → σ → σ → σ`. Finding 1; survives all three specimens.
2. **A common local/global distinction:** `BridgedTraj E a a' ∧ BridgedTraj E b b' ⇏ BridgedTraj E (merge a b) (merge a' b')`. Three concrete witnesses.
3. **Per-slice characterizations** (`*_iff_admissible`): the bad case and the restoration as two corners of one characterization, for each slice independently.
4. **Sufficiency schema across three slices:** `MergeRestoresValue` (Budget + Conflict at value layer; Stale trivially at value, non-vacuously at basis); `MergeRestoresBasis F Guard` (Stale at basis with `Guard = evidenceFresh`); `MergeComposesBridgedEndpoints` (trajectory-layer for all three).
5. **Necessity as schema, not theorem:** `MergeOkNecessaryAtValue F` holds for Budget + Conflict; *fails positively* for Stale at value (`staleFrame_value_necessity_fails`); holds for Stale at basis (`staleFrame_basis_necessity` with `Guard = evidenceFresh`).
6. **The federation-doctrine composition pattern:** the explicit sentence *"both refuse the single-grand-theorem collapse"* binding `ParameterizedMerge` and `BoundaryWitness` in shared discipline.

That last item is the substrate work *answering* the question LGVG-as-primitive asks. The composition axis already arrived at "schema with per-slice instantiations" rather than "single composition theorem." LGVG-as-primitive would have to overturn that finding to be ratified.

## What remains unforced

1. **The four-axis recurrence claim.** The substrate covers one axis. The other three (drift / saturation / mimicry) have no substrate specimens of their own. *Drift* could potentially be approached via a temporal-evolution specimen (closest existing material: Freshness.lean + the stale-evidence slice); *coupling* is closest to what merge composition is; *saturation* and *mimicry* have no substrate footprint yet.
2. **The unifying primitive itself.** Even if a second axis's specimens landed, the substrate's federation-doctrine compose move would likely repeat: per-axis schemas, refusal of single-grand-theorem collapse. That is the prior the substrate has established.
3. **The field-shaped claim.** "Same structural failure recurs across substrates" — undemonstrated without cross-substrate evidence. The merge family is one substrate (the value/basis-preservation substrate).
4. **The promotion gate from [[project-admissibility-decay-family]]:** *"Composition test: does at least one cross-primitive theorem in Lean force the higher-order construct?"* The MergeAdmissible-shaped schema is one composition theorem, but it is internal to the merge axis. It does not force the higher-order LGVG primitive.

## Minimal next forcing case, if any

The honest minimal next forcing case for LGVG-as-primitive promotion would be:

- A substrate specimen family from a *different* composition axis (drift / saturation / mimicry — pick one), with its own negative keepers and per-slice positive objects.
- A demonstration that the *same scaffolding* (`Param → σ → σ → σ` operator, schema-shaped necessity, federation-doctrine composition pattern) recurs.
- A cross-axis comparison showing the scaffolding stabilizes at higher altitude than per-axis schema.

That is a major undertaking. The merge specimen family took multiple slices, a GuardCollapse probe, three Findings, and a deliberate "do not pre-mint" discipline. A second-axis specimen family would be a similar arc. **Estimated cost:** sprint-scale, not session-scale. **Estimated yield:** likely the same federation-doctrine outcome (per-axis schema + cross-axis refusal of single-primitive collapse) — meaning LGVG promotion would still be refused even with the second forcing case.

**Honest alternative:** LGVG could be promoted as a **descriptive family designation** at the composition altitude, sibling to admissibility-decay-family at the decay altitude. The merge axis is one row; future axes would be future rows; the family is the *line through the points*, not a single primitive. This matches the explicit non-promotion of admissibility-decay-family itself: *"Not a primitive in its own right."* That promotion path would be small (rewrite the LGVG note's "field-shaped primitive" framing as "family designation"), low-blast-radius, and consistent with the federation doctrine. **It is also not authorized by this audit** — the user's instruction is gap-detection only, not LGVG-reframe-authorization.

## Patch queue (if any)

Two candidate cross-ref patches, mechanical and low-cost. Neither is authorized without explicit user signal.

1. **LGVG note ↔ axis-2-composition-boundary cross-ref.** `working/local-global-validity-gap.md` does not currently reference the axis-2 specimen work that empirically tested its claim. `working/axis-2-composition-boundary.md` does not currently reference LGVG as the named candidate the specimens were testing against. Bidirectional ~5 min patch. Adds navigability; does not promote LGVG.
2. **LGVG note ↔ admissibility-decay-family cross-ref.** LGVG appears in the decay-family table (composition/scope axis row) but the LGVG note itself does not cross-reference the family. Adding the cross-ref makes the "family designation candidate" reframing legible without performing it. ~5 min.

Both patches are pure connective tissue. Same shape as the cross-ref patches from attack-02 and attack-04. **Both deferred unless explicitly authorized.**

## Promotion status

**PROMOTE NOTHING.**

- LGVG: candidate status preserved. The audit *does* generate evidence the substrate refuses single-primitive promotion; that evidence is recorded here, not propagated into the LGVG note.
- `ParameterizedMerge`: already built green; no promotion change needed.
- Necessity-as-schema verdict: already in the corpus (axis-2-composition-boundary Step 8); no promotion change needed.
- "No-lift as base case, composition boundary as center of gravity" paper-shape reframe: explicitly **deferred** per the axis-2 note ("until Slice 2 has its positive object and the generic is minted"). Slice 2 now has its positive object and the generic is minted. The reframe could be promoted to paper-shape, but that is a paper-authorization decision, not a vector-mining-pilot decision. **Out of scope.**

## Method note

Attack #6 (sacrifice floor × Mist/composition) confirmed the LGVG gap from outside; this pilot tested it from inside (substrate-completeness mode). Both arrived at the same federation-doctrine answer: the gap exists, the corpus deliberately holds it open, and the substrate evidence weighs *against* single-primitive promotion rather than for it. That is two independent altitudes (paper-candidate + Lean substrate) producing the same refusal verdict on the LGVG-as-primitive promotion question.

**Pattern recognized:** vector mining at the substrate altitude can produce *evidence against promotion* even when the gap is real. This is a sharper outcome than attack #6's "gap confirmed + relay-framing refused" — here the substrate work has actively done the refutation internally, and the audit only needs to interpret it. Add to the failure-modes catalogue:

6. **Internal-refutation gap:** real gap exists; substrate work has done the federation-doctrine refusal internally; audit verdict is *promotion is refused by the corpus's own work*, not merely *not forced*.

## Cross-references

- `working/local-global-validity-gap.md` — the candidate primitive under audit.
- `working/axis-2-composition-boundary.md` — the substrate doctrine spine; carries Step 8's schema-vs-theorem verdict.
- `working/axis-2-composition-forcing-cases.md` — the per-slice forcing-case catalog.
- `LeanProofs/Admissibility/StaleEvidenceMerge.lean`, `BudgetMerge.lean`, `MergeConflict.lean`, `ParameterizedMerge.lean`, `GuardCollapse.lean` — the specimen family.
- `LeanProofs/Admissibility/BoundaryWitness.lean` — the keystone whose refusal of single-grand-theorem the substrate composes with.
- [[project-no-unifier-without-laundering]] — the federation discipline both the keystone and the composition substrate instantiate.
- [[project-admissibility-decay-family]] — the family-designation pattern LGVG could survive under.
- `working/vector-mining/2026-06-05-batch-six-attacks.md` § Attack #6 — outside-substrate sibling pilot that confirmed the gap from the paper-candidate altitude.

## Provenance

Single-target pilot 2026-06-05 of the vector-mining method, gap-detection mode, hard-constrained per user spec. Result: substrate generates positive evidence against LGVG-as-single-primitive promotion via the schema-vs-theorem verdict and explicit compose-with-keystone refusal. Cumulative pilot count 10; cumulative failure-modes characterized 6 (newly: internal-refutation gap).
