# Lean custody ledger — 2026-06-06

**Filed:** 2026-06-06 (Fri). **Status:** post-cleanup snapshot. **Source:** the 2026-06-06 custody audit + the post-audit cleanup pass (SurfaceDeformation v3 fix-up; `lean_proofs/` retirement).

This file is the single retrievable answer to *"where is the Lean?"* for the work captured in this corpus as of today. It is NOT doctrine, NOT a candidate ledger; it is the after-action custody snapshot. Update when custody states change; do not re-litigate doctrine here.

## Checked Scratch (compile-clean)

- `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` — direct `lake env lean` check clean (0 errors, exit 0). Status: **scratch-checked**. Not in `LeanProofs.lean` import surface. **Fenced scratch now has internal doctrine-verification pins** (added 2026-06-06 PM): five theorems prove that the type-level choices actually deliver what the comments claim. `witness_implies_all_kernels_passed`, `failure_list_is_accumulation`, `no_witness_for_self_attested`, `no_witness_past_horizon`, `refusal_is_nonempty`. **Still not promoted** — internal verification for fenced scratch only, does not discharge authority possession or close the Lean↔production substrate gap. Two Lean-mechanics corrections applied during build (from operator-provided patch + iteration): (a) `¬ Witness a n` → `Witness a n → False` (Witness is in `Type`, not `Prop`); (b) `not_lt_of_ge` is not in core → use `Nat.lt_irrefl n (Nat.lt_of_le_of_lt w.notExpired h)`; (c) `unfold check_crossing` can't reduce the 8-way match without all three kernel results known → use chained `cases <;>` + full simp set per branch (case-split ALL THREE before simp).
- `~/git/lean/LeanProofs/Scratch/SurfaceDeformationRequiresCoupling.lean` — direct `lake env lean` check clean *after* corrections. **Substantive fix applied 2026-06-06:** the three `CouplingWitness` invariance fields (`antiRetroactive`, `outsideScopeInvariant`, `afterHorizonInvariant`) were re-parenthesized to bind the `Iff` body under the implication (Lean 4 `↔` has lower precedence than `→`; without parens the fields parsed as Iff-of-implication, making every projection unusable). claude-web's v3 was authored without a Lean binary; the bug was masked by the sandbox. Five proof bodies were also rewritten to use Lean 4 core (`by_contra` / `by_cases` unavailable in v4.29.0 without imports). Type design and theorem statements survived intact. Status: **scratch-checked**. Not in `LeanProofs.lean` import surface.
- `~/git/lean/LeanProofs/Scratch/AggregateWitnessRequiresJoin.lean` — direct `lake env lean` check clean on first elaboration 2026-06-06 (133 lines including category-2 prelude). Filed as a bounded compile probe per the *"build when Lean is asked a bounded question"* discipline; prelude records the four questions the probe answers (dependent-indexing prevents unindexed laundering ✓; `Option (JoinWitness b reqs)` preserves index visibility through `match` ✓; `bundleSatisfies := ∃ p, p ∈ b.parts ∧ p.satisfies r` typechecks against arbitrary `Requirement → Prop` ✓; no parens-bug-shaped surprise ✓). Type design holds; `unjoined_bundle_not_admissible_as_unified` theorem is intentionally toy (per *"the theorem is less important than the type you cannot construct"*). Status: **scratch-checked**. Not in `LeanProofs.lean` import surface. Layer tag: `NoSilentJoin`. Field-guide name: Frankenstein Witness.
- `~/git/lean/LeanProofs/Scratch/LogOnlyProvesEmission.lean` — direct `lake env lean` check clean on first elaboration 2026-06-06 (~127 lines including category-2 prelude). Filed as a **tactic / custody probe** (smaller-altitude than Aggregate's type-design probe — explicit framing in prelude). Prelude records four questions: constructor split elaborates ✓; negative cases reduce cleanly via `simp` ✓; many-logs existential proof elaborates without Mathlib-only destructuring ✓; `deriving` clauses for String-backed structures elaborate ✓. **Corrective finding:** the pre-audit predicted `rcases` would need Mathlib substitution (sandbox-style claim about core availability); Lean disagreed — `rcases` and `simpa` are available in the current toolchain (v4.29.0 + the lakefile's mathlib package, even without an explicit `import`). The probe corrected the prediction — exactly the kind of custody-honest fact only Lean can give. Only non-fatal output: linter suggests `simp at hInfer` instead of `simpa using hInfer` as cleaner style; left as written per the "don't modify beyond proof failures" directive. Status: **scratch-checked**. Not in `LeanProofs.lean` import surface. Layer tag: `NoLift`. Doctrine: *"A log proves emission, not truth, authorization, causality, completeness, or fairness."* **Fenced scratch now has internal doctrine-verification pins** (added 2026-06-06 PM; equivalence pin added later same evening): 15 theorems pin the doctrine — `inferable_emitted_iff` and `inferable_emitted_determines_fields` characterize the positive case at the entry level; `emitted_inferable_from_log` / `_from_singleton` / `_from_many` show emission claims compose into singleton and arbitrary lists; **`inferableFromManyLogs_emitted_iff_exists_matching_entry`** is the positive characterization at the existential level — many logs infer an emitted claim *exactly when* the list contains a matching entry, nothing more smuggled through the `∃`; `log_entry_does_not_discharge_{truth, authorization, causality, completeness, fairness}` cover the five False constructors directly; `many_logs_do_not_discharge_{authorization, causality, completeness, fairness}` cover the existential lift. **Still not promoted.** **Doctrine scar preserved in prelude** (DeepSeek's first patch caught itself): *constructor-negative claims (truthOf / authorizationOf / etc.) reduce to False; mismatched emitted claims (`.emitted sys stmt ts` with wrong fields) reduce to unmet equality obligations; do NOT collapse those two cases — different failure species.* The file is about emission-only admissibility, so it must be especially careful not to launder *"not this emitted claim"* into *"all negative claims are definitionally false."* That distinction is the doctrine in miniature. Same gremlin shape as the Mandamus first-draft caught its own author; here DeepSeek's first verification patch caught itself trying to over-collapse the two failure species. **Discipline carry:** future commentary on this file must qualify *"negative cases reduce to False"* with *constructor-negative only* — the wrong-emitted-fields case lives in the unmet-equality-obligations bucket, not the False bucket. The equivalence theorem operationalizes the positive side without widening the claim: *the many-log existential adds list membership; it does not add truth, authorization, causality, completeness, fairness, or institutional standing.*
- `~/git/lean/LeanProofs/Admissibility/Mandamus.lean` — direct `lake env lean` check clean on second elaboration 2026-06-06 (~200 lines including header). Filed as the **liveness-dual minimal-spine kernel** per the 2026-06-06 multi-model exchange. Three sprint-#1 theorems all elaborate: `sufficient_ministerial_before_horizon_implies_owes` ✓; `nondecision_past_horizon_implies_deemed_refusal` ✓; `blocking_predicate_does_not_reset_matter_clock` ✓. **One Lean 4 quirk corrected during build:** `Prop`-valued `structure HasDecided` can't carry a `DecisionRecord` data field; switched to existential form `∃ record, record.decidedAt ≤ now`. Sprint #2 deferred items recorded as inline deferral receipts: well-founded `ReachableCure` theorem, claimant-capability indexed reachability, full BlockingPredicate discipline, appellate-independence via same-custody refusal. Frontier 3 (rule-change-as-effect) explicitly deferred to `working/frontier3-rule-change-deferral.md`. Status: **scratch-checked**. **NOT in `LeanProofs.lean` import surface** (fenced-Admissibility annex per the existing 13-file precedent — `AmendmentFragment`, `BoundaryWitness`, `BudgetMerge`, etc. — same convention). Layer tag: liveness-dual (new — separate axis from the static/dynamic split in [[project-bridge-obligation-lattice]]). Doctrine: *"Refusal is an accountable act"* / *"The kernel that proves the institution owed you an answer."* Companion working notes: `working/refusals-need-receipts.md` + `working/mandamus-liveness-dual.md` + `working/frontier3-rule-change-deferral.md`.

## Retired

- `~/git/lean/lean_proofs/` — abandoned `lake new` init skeleton (`def hello := "world"` in the only non-template file; untouched since template setup). Carried a full mathlib `.lake/` download as dead weight. Removed 2026-06-06.

## Root-level specimens (left as-is)

- `~/git/lean/non-reciprocal-admissibility-flow-sketch.lean` — header explicitly documents the root-level convention as intentional ("lives at the lean repo top level [...] not inside `LeanProofs/Admissibility/`. Promotion to the canonical path requires the gates documented in the companion working note"). Filed 2026-05-15. Status: **specimen**.
- `~/git/lean/taxonomy-lean-sketch.lean` — older sketch (mtime 2026-05-10). Header: *"Status: SKETCH. Needs Lean 4 toolchain to compile."* Companion to the older Δ-taxonomy work, not the post-2026-05 admissibility kernel work. Status: **specimen**.

## Markdown-only candidate Lean (hold per name-early)

- **`LogOnlyProvesEmission`** — **moved 2026-06-06 to Checked Scratch above.** See § Checked Scratch. Initial "too mechanical to pose a real question" classification was revised on operator challenge: the sketch poses smaller-altitude questions (tactic mechanics, core availability of `rcases` / `simpa`) than Aggregate's type-design questions, but they are real questions only Lean can answer. The probe corrected the pre-audit prediction about `rcases` requiring Mathlib substitution.

- **`AggregateWitnessRequiresJoin`** — **moved 2026-06-06 to Checked Scratch above.** See § Checked Scratch.

## Field-guide examples (doctrine, not candidate kernels)

- **`NoObjectionRequiresSolicitation`** — `working/tooltheory/admissibility-field-guide-2026-06-05.md` entry #1 / Lean sketch. Status: **field-guide example only; doctrine, not candidate kernel.** Parent kernel: `project-signal-authority` (Lean deferred). If/when SignalAuthority earns a Lean build, this sketch is candidate shape; until then it's doctrine.
- **`ReportedStatusRequiresConversionWitness`** — same file, entry #2 / Lean sketch. Status: **field-guide example only; doctrine, not candidate kernel.** Parent: master-frame conversion-witness binding rule. Same discipline.

## Frontier / do not promote

- **`BridgeWitness`** (generic shape, lattice file) — `working/bridge-obligation-lattice.md` § The generic shape. Status: **Frontier; do not promote.** Explicit "Receipt 2.0" caution against premature build; promotion requires the Coupling-as-instance Lean spike to compile.
- **`BudgetedCouplingWitness`** (composition sibling, surface-deformation candidate) — `working/tooltheory/surface-deformation-requires-coupling-candidate-2026-06-05.md` § Frontier. Status: **Frontier; do not promote.** Practical blocker: finite-claim-domain instantiation required for honest `spend` count.
- **`NoSilentDelegation`**, **`NoSilentException`**, **`NoSilentProjection`** — `working/bridge-obligation-lattice.md` § Dynamic refusal kernels. Status: **Frontier; named, not built; do not promote.** The lattice file is their doctrinal home until a forcing case earns the build.
- **`NoSilentSurfaceComposition`** (a.k.a. `SurfaceDeformationCompositionRequiresWitness`) — `working/tooltheory/surface-deformation-requires-coupling-candidate-2026-06-05.md` § Frontier. Status: **Frontier; do not promote.** Composition family; held with budget-as-custody-layer discipline.

## Admissibility/ — non-imported `.lean` files (custody-convention inconsistency, NOT misroute)

Thirteen `.lean` files live in `~/git/lean/LeanProofs/Admissibility/` but are NOT imported by `LeanProofs.lean`. Each carries an explicit header fencing it as scratch / annex / specimen / probe / candidate. Status: **fenced-scratch convention**; intentional per per-file headers; convention is inconsistent with the BoundaryTransit / SurfaceDeformation pattern (which uses `Scratch/`), but no action required this round. List for retrieval:

- `AmendmentFragment.lean` (specimen)
- `BoundaryWitness.lean` (expository)
- `BudgetMerge.lean` (Axis 2 Slice 0 specimen)
- `Conductance.lean` (candidate)
- `ConsequencePartition.lean` (candidate)
- `ContractionHinge.lean` (specimen)
- `GuardCollapse.lean` (probe)
- `MergeConflict.lean` (Slice 2 specimen)
- `ParameterizedMerge.lean` (candidate)
- `ProjectionLaundering.lean` (candidate)
- `RetroactiveLegitimation.lean` (specimen)
- `StaleEvidenceMerge.lean` (Slice 1 specimen)

Custody policy decision deferred (per the audit's "Option A / B / C" framing — operator picked C short-term: both allowed, but every file must declare custody class in header).

## Custody-policy rule (working)

Adopted 2026-06-06:

> **Every `.lean` file must declare custody class in its header.**
> **Every markdown Lean block must declare Lean custody on the candidate-file's status line.**

Custody classes:

- `canonical-imported` — wired into `LeanProofs.lean`; subject to `lake build`.
- `scratch-checked` — direct `lake env lean` runs clean; not in import surface.
- `scratch-unchecked` — `.lean` exists but not Lean-checked.
- `specimen` — intentional out-of-convention placement (root-level; per-file header documents discipline).
- `retired` — superseded or abandoned; awaiting removal or kept for historical reference.

Markdown Lean-block custody values:

- `markdown-only` — block exists in markdown; never extracted; never Lean-checked.
- `promoted-to:<path>` — block was extracted; canonical source lives at the given path.
- `superseded-by:<path>` — block was extracted and has since diverged; the path is canonical, the markdown is stale.
- `frontier-do-not-extract` — block is doctrine-shape sketch; promotion is gated on a forcing case.

## Cross-references

- The 2026-06-06 custody audit (in this session's transcript) — original diagnostic that surfaced the three-systems-pretending-to-be-one finding.
- [`anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) § Cross-cutting type-design rules — corpus-wide rules from the SurfaceDeformation review/repair cycle.
- [`surface-deformation-requires-coupling-candidate-2026-06-05.md`](surface-deformation-requires-coupling-candidate-2026-06-05.md) — candidate working note for the SurfaceDeformation kernel; provenance line should note the 2026-06-06 parens fix (see § Checked Scratch above).
- [`../bridge-obligation-lattice.md`](../bridge-obligation-lattice.md) — Frontier-family doctrinal home for the named-not-built dynamic kernels.
- [[documentation-keepers]] — keeper-phrase register; cross-cutting.

## Provenance

Filed 2026-06-06 following:
- The 2026-06-06 custody audit (read-only diagnostic across `working/`, `working/tooltheory/`, `~/git/lean/`) — surfaced 13 markdown-only candidate sketches, 13 non-imported Admissibility/*.lean files, 3 root-level Lean files (including the abandoned `lean_proofs/` skeleton), and the v3 SurfaceDeformation file landed but un-checked.
- The 2026-06-06 fix-up pass — landed v3 to Scratch/, ran direct Lean checks (BoundaryTransit clean; SurfaceDeformation initially broken with 11 errors), diagnosed the `↔` / `→` precedence bug as the actual culprit, fixed 1 struct + 5 proof bodies, re-elaborated clean.
- The 2026-06-06 cleanup pass — operator removed `lean_proofs/` (abandoned skeleton); operator committed SurfaceDeformation; operator opted for custody-policy Option C (both `Scratch/` and fenced-Admissibility/* allowed, with mandatory custody-class header).

This ledger is the closing receipt. Next custody change: update this file.
