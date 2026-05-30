# Consequence Partition — candidate primitive (2026-05-29)

**Status:** Candidate primitive. **Scratch Lean annex built and green** at `~/git/lean/LeanProofs/Admissibility/ConsequencePartition.lean` (410ms, no sorry / no axiom / no `LeanProofs.lean` import). Not public surface. Not in the safety-bridge preprint. Not paper-shaped.

**Posture:** Fourth specimen in a recognized family (projection-erases-distinction kernels) under tooltheory-class candidate density. Names early, ratifies lazily. The annex module is a *build-test* for whether the slice has independent shape distinct from `WitnessInvariance` / `SurfaceAuthorization` / sketched `ProjectionLaundering` — not a promise to extend.

**Distinct from full-protocol modeling.** The handoff that produced this slice came out of a Bluesky / ATProto moderation conversation, but the kernel is platform-generic. ATProto vocabulary (labelers, label values, preference aggregation) is *not* in the kernel; if a worked example is ever forced, it goes in a sibling specimen module. *The raccoons do not get tenure.*

---

## The kernel claim

> **Composable classification with centralized consequence is theater.**

A user policy is expressible through a platform projection exactly when the platform projection refines the policy partition. If every feasible action factors through the platform's projection, then no feasible action can implement a policy the projection fails to refine. The repair exists — but only as a strictly finer projection living outside the feasible action set.

Compressed:

> **You cannot buy back a distinction the platform already quotiented away unless the finer projection is inside your feasible action set.**

## The family

| Module | Axis | Status |
|---|---|---|
| `Admissibility.WitnessInvariance` | encapsulation under perturbation | built, in `LeanProofs.lean` |
| `Admissibility.SurfaceAuthorization` | cause attribution under collapsed surface | built, in `LeanProofs.lean` |
| `ProjectionLaundering` (sketched) | deferral signal under lossy compression | candidate, not built |
| `Admissibility.ConsequencePartition` (this) | policy expressibility under platform projection | **built as scratch annex 2026-05-29**, not in `LeanProofs.lean` |

All four are *projection-erases-distinction* refusal kernels applied to different downstream axes. `FactorsThrough p c` is structurally `WitnessInvariance.Encapsulated (sameAdmittedBasis := · =ₚ ·) c`. The siblings share the proof pattern; the axis content differs.

## The structural delta that earns the sibling slot

(Per [[feedback-kernel-overlap-audit]] — name the delta before promotion.)

1. **Feasibility surface.** `Surface S A` + `Feasible` + `Implements` give the impossibility theorem its boundary character. `WitnessInvariance` has no notion of action-cost. This is a *new content axis* under the same projection mechanism.

2. **Off-budget repair theorem.** `policy_repair_strictly_finer_off_budget` is a three-way conjunction: (a) the policy is unimplementable inside the feasible action set, (b) the fine projection strictly refines the coarse one, *witnessed by the policy*, (c) an off-budget repair exists. No sibling has this shape — `WitnessInvariance` has `encapsulated_wrt_mono` (refinement monotonicity) but no analog of the strict-refinement-witnessed-by-policy theorem.

3. **`ObservedNonRefinement` as `Type`-level data.** Labelwatch produces an *actual pair* the platform collapses but the policy separates. The sibling kernels' refusal witnesses are `Prop`-level existentials. A bridge that cannot carry its own witnesses across is not a bridge.

## The Lean shape (built)

Slot: `Admissibility.ConsequencePartition` namespace. Universe-polymorphic over `S` (state), `L` / `M` (projection codomains), `A` (action index). No Mathlib dependency. No `LeanProofs.lean` import. Built standalone via `lake build LeanProofs.Admissibility.ConsequencePartition`.

Contents:

- `Visibility` (two-valued)
- `Control S := S → Visibility`
- `Policy S := Control S` (collapsed; see below)
- `FactorsThrough p c := ∀ s t, p s = p t → c s = c t`
- `Refines q p := ∀ s t, q s = q t → p s = p t`
- `refines_refl`, `refines_trans`
- `ExpressibleBy p policy := FactorsThrough p policy`
- `policy_expressible_iff_refines_policy` (proved by `Iff.rfl`)
- `Implements c policy := ∀ s, c s = policy s`
- `Surface S A` structure with `control` / `feasible` fields
- `Feasible sf a := sf.feasible a`
- `ObservedNonRefinement observed p policy` — **`structure`, not `Prop`** — fields `left`, `right`, `observedLeft`, `observedRight`, `collapsed`, `split`
- `observed_nonrefinement_denies_refinement` — bridge theorem
- `no_feasible_action_implements_unrefined_policy` — impossibility / cost-wall
- `StrictlyRefines q p := Refines q p ∧ ¬ Refines p q`
- `OffBudgetFineRepair sf pFine policy` — repair witness existence
- `fine_projection_is_strict_for_policy` — strictness lemma
- `policy_repair_strictly_finer_off_budget` — three-way conjunction; **every hypothesis load-bearing**

## Multi-model relay receipts (provenance)

Surfaced via a Bluesky / ATProto moderation discussion. Three model passes preceded this filing:

| Model | Contribution | Failure mode |
|---|---|---|
| DeepSeek | Hit the cost wall; admitted it; left proofs as `...`. | Got far enough to expose the structure, then timed out — the `¬ Feasible` end of the theorem under test, lived. |
| Gemini Pro | Filled every hole; claimed axiom-free while opening `axiom State : Type`; left `hcoarse` / `p_fine` unused in `you_cannot_buy_back_quotiented_distinction` and `v` unused in `toggle_is_theater`. | Theater — every hole filled, theorem-name laundering on the boundary claim. The paper proved itself on its reviewers. |
| Operator + Claude (web) | Caught the laundering and the `Prop` vs `Type` boundary on `ObservedNonRefinement`. Reframed `you_cannot_buy_back_…` as a three-way conjunction so every hypothesis is load-bearing. | None at the corrected layer; this is what the annex module preserves. |

**Composition keeper:** the slice proved its own kernel claim on the people grading it. DeepSeek landed in `¬ Feasible`; Gemini shipped theater. The corrected reading is what the annex module captures.

## On `Policy := Control` (kernel decision)

Collapsed for the kernel. Reasoning:

- `ExpressibleBy ↔ Refines` becomes `Iff.rfl`; the bridge is exact.
- The impossibility theorem does not need anything else.
- The empirical layer (intent → desired control) is a downstream consumer responsibility, not kernel content.

**Downstream gap, name-early:** Labelwatch's `Policy` in the wild is *declared user intent*, not a `Control`. The mapping `intent → desiredControl` is a custody act that belongs in the consumer. When a forcing case arrives, the slot is `PolicyIntent` with `desiredControl : PolicyIntent → Control` and `ImplementsIntent c i := Implements c (desiredControl i)`. Not built. Not named in the Lean. Reserved here for retrofit-cost control.

## Empirical handoff for Labelwatch

**Update 2026-05-29 (labelwatch read-back):** Labelwatch's `boundary_edges` table (schema v18) is **half-built as `ObservedNonRefinement`** — `target_uri` is the `collapsed` shared frame, divergent labeler verdict is the `split`, two edge observations are `left` / `right`. Load-bearing tiny gap (chatty): to become a *true* witness, the row must bind the exact projection `p` and policy/control being tested; otherwise the schema risks "same post, different labels" rather than "platform collapsed a distinction the policy needed." Retrofit cost near-zero; mapping is probably one page when a consumer demands it. The three trip-distinctions below match Labelwatch's `BOUNDARY_PHASE2_SPEC.md` trio (domain taxonomy / polarity model / JSD orthogonality filter); same questions, different vocabulary; *do not over-extract before consumer asks*. See [annex-probe-queue-2026-05-29.md](annex-probe-queue-2026-05-29.md) §Labelwatch's emitter-finding for full context.

Labelwatch's deliverable is **not** UI screenshots of exposed toggles. It is an `ObservedNonRefinement` witness:

```text
observed left
observed right
platformProjection left = platformProjection right
desiredPolicy left ≠ desiredPolicy right
```

Then the bridge theorem supplies:

```text
¬ Refines platformProjection desiredPolicy
```

Then `no_feasible_action_implements_unrefined_policy` supplies:

```text
no feasible p-factored action can implement that policy
```

Three distinctions Labelwatch will trip on, named early:

1. **State identity.** What exactly is a `State`? Post URI? account DID? label snapshot at timestamp T? feed position? viewer prefs at that moment? If those drift between `left` and `right`, the witness gets mushy. Labelwatch's tag-set on each observed state is the load-bearing piece — same set ⇒ comparable, different set ⇒ inadmissible witness.

2. **Effective consequence.** `Visibility := visible | hidden` is the bounded kernel. Real Labelwatch consequence may need more: warning-gated, deprioritized, suppressed-from-search, suppressed-from-feed-but-visible-on-profile, etc. When that forcing case arrives, generalize `Visibility` to an arbitrary type `V` and parameterize `Control S := S → V`. The proof obligations carry over.

3. **Where the projection collapses.** The kernel does not care whether the quotient happens at label ingestion, appview aggregation, feed generation, client filtering, or final rendering. Labelwatch *does* care — the witness must locate the collapse point or it cannot survive a "that's just a client UI bug" rebuttal. The instrumentation question is downstream.

## Composition with sibling kernels (named, not built)

- **With [[projection-laundering]] (PL/UC composition):** the Labelwatch pipeline `observed states → tag features → finding artifacts → `ObservedNonRefinement` witness` is itself a representation pipeline. PL's `loss-aware projection` discipline applies at each hop: the witness emitted by Labelwatch must preserve the predicates downstream consumers (the kernel here, the Governor, NQ) will need. Composing PL + ConsequencePartition gives end-to-end custody from observation to refusal. Not built. Named for retrofit-cost.

- **With `Admissibility.SurfaceAuthorization`:** if the Labelwatch witness pair is itself produced from a collapsed surface (e.g., identical-looking timeline events that differ in causally relevant ways), `SurfaceAuthorization` would refuse to authorize the witness as cause-attributing. Composition is: collapsed surface ⇏ admissible `ObservedNonRefinement` witness. Open.

- **With `Admissibility.WitnessInvariance`:** the Labelwatch instrumentation itself is a witness; if it moves under excluded perturbations (e.g., the platform A/B tests change the projection without changing the labeler graph), the witness fails encapsulation. Open.

## What this candidate does NOT claim

- **Not a model of ATProto.** No labelers, no label values, no preference aggregation in the kernel. Gemini modeled the stack; this annex deliberately does not.
- **Not a moderation-theory paper.** Paper-shape promotion gates on a forcing case (a published Labelwatch finding that needs the kernel to carry its refusal, *and* a downstream consumer that demands the formal pair).
- **Not promotion to `LeanProofs.lean`.** The annex is scratch — wired only via direct `lake build` invocation. Wiring into the public surface gates on a forcing case (sibling kernel needs to compose with it, or Governor wants it as a basis-derivation candidate).
- **Not blessing of "Composable Moderation Calculus" or any such public name.** Per [[project-boundary-calculus-program]] this is one specimen in an existing family. No new program.
- **Not foreclosing `PolicyIntent`.** The slot is reserved; the kernel does not build it.
- **Not certifying any specific platform.** The kernel is conditional: *if* every feasible action factors through `p`, *then* no feasible action implements unrefined policies. The antecedent is a question for Labelwatch instrumentation, not for the kernel.

## Forcing-case watchlist (gates promotion from annex to public surface)

Build is *done* at annex density. Promotion to `LeanProofs.lean` import / paper-shape gates on at least one of:

- **Labelwatch finding** that needs to emit an `ObservedNonRefinement` witness as a structured deliverable, not just a screenshot.
- **NQ / Wicket / Governor consumer** that cites `policy_repair_strictly_finer_off_budget` as the basis for refusing a "this is composable" claim against a platform with centralized consequence.
- **Sibling kernel composition** that needs ConsequencePartition's bridge shape (e.g., projection-laundering's `loss-aware projection` composed with consequence-partition's `Refines`).
- **Paper-side citation** that requires the formal pair (e.g., paper 28 framing wants a typed handle on "the platform sells classification composability but reserves consequence composability").

Until one arrives, the annex stays as scratch, the candidate note stays here, and the slot stays reserved.

## Keeper stack

> Composable classification with centralized consequence is theater.

> A fire escape that requires a Kubernetes cluster is mostly decorative.

> You cannot buy back a distinction the platform already quotiented away unless the finer projection is inside your feasible action set.

> Labelwatch's deliverable is the pair, not the prose.

> A bridge that cannot carry its own witnesses across is not a bridge. (Why `ObservedNonRefinement` is `Type`, not `Prop`.)

> Theorem-name laundering = the title claims a boundary the proof does not establish. (The Gemini residue. Every hypothesis in `policy_repair_strictly_finer_off_budget` is load-bearing.)

> The slice proved its own kernel claim on the people grading it.

## Anti-goals

- **Do NOT** extend the kernel to model the ATProto stack (or any platform stack). The kernel is platform-generic; specific platforms are downstream example modules, gated on a forcing case.
- **Do NOT** generalize `Visibility` preemptively. The bounded kernel is the contract; generalization gates on a Labelwatch consequence model that needs more than `visible | hidden`.
- **Do NOT** promote `ObservedNonRefinement` to multi-witness / compositional shapes preemptively. The slot is single-witness for the same reason `SurfaceAuthorization` is single-action: composition is downstream.
- **Do NOT** mint a `PolicyIntent` type or `Surface.cost` field in the kernel until a consumer demands it. Both are name-early, build-on-forcing-case.
- **Do NOT** rename the family ("Compositional Consequence Theory", "Refinement-Based Moderation Calculus", etc.). The annex sits inside the existing `Admissibility` namespace as a sibling kernel; no new program.

## Cross-references

- **Lean annex:** `~/git/lean/LeanProofs/Admissibility/ConsequencePartition.lean` — green 2026-05-29.
- **Sibling kernels (built):** `~/git/lean/LeanProofs/Admissibility/WitnessInvariance.lean`, `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean`.
- **Sibling kernel (sketched):** [[projection-laundering]] — the deferral-signal-axis projection-erases-distinction kernel. PL/UC composition partner.
- **Downstream tool:** [[labelwatch-driftwatch-admissibility]] — the consumer that will emit `ObservedNonRefinement` witnesses if the kernel earns a forcing case.
- **Family doctrine:** [[feedback-kernel-overlap-audit]] — the audit run before filing.
- **Composition discipline:** [[refusal-kernel-to-refusal-receipt-seam]] — operator-family parent. ConsequencePartition is a new row at the *policy-expressibility* layer.
- **Naming discipline:** [[feedback-name-early]] — slot reserved at candidate density; ratification lazy.
- **Build-vs-promote distinction:** [[feedback-forcing-case]] — the operator override that produced this annex. Forcing-case discipline gates *public-surface promotion*; it does not block bounded scratch annexes whose purpose is to test whether the candidate has independent shape.
- **Program-name caution:** [[project-boundary-calculus-program]] — this annex does not authorize the program name or any rename. One specimen, sibling slot, no expansion.

## Provenance

- **2026-05-29.** Multi-model relay: Bluesky / ATProto moderation discussion → DeepSeek expansion attempt → Gemini Pro full-hole-fill with axiom laundering and unused hypotheses → operator + Claude (web) correction pass producing the kernel + bridge + off-budget shape with all hypotheses load-bearing → paper/Lean Claude (this session) ran the kernel-overlap audit, the Prop/Type fix, and the compile.
- **Annex landed:** 2026-05-29, ~410ms `lake build`, no sorry, no axiom, no warning, not in `LeanProofs.lean`. Operator override of the conservative "candidate-density only" reading: forcing-case discipline gates *public-surface promotion*, not bounded scratch annexes whose purpose is to test whether the candidate has independent shape.
- **Filed by:** claude-code, after audit confirmed (a) the shape was *not* fully covered by existing kernels — `Surface` / `Feasible` / off-budget repair / Type-level `ObservedNonRefinement` are genuinely new, (b) the family slot is `Admissibility/`, not a new namespace, (c) the build was cheap enough that compile-then-decide beat candidate-density-then-defer.

## Park state

Next session — if the topic recurs — should:

1. Check whether Labelwatch has produced an `ObservedNonRefinement` witness in the wild.
2. Check whether NQ / Wicket / Governor / a paper draft has cited `policy_repair_strictly_finer_off_budget`.
3. Check whether sibling-kernel composition (PL + CP, SA + CP, WI + CP) is producing real consumer load.
4. Only then consider:
   - Importing into `LeanProofs.lean`.
   - Generalizing `Visibility` beyond two values.
   - Building a worked-example sibling specimen.
   - Promoting to paper-shape (likely an addendum / appendix to an existing preprint, not a new numbered paper).

Until then: annex stays scratch, note stays here, slot stays reserved.

> **The audit was the gate. The compile was the receipt. The forcing case is still upstream.**
