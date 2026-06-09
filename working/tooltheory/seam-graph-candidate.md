# Seam-Graph (candidate) — Admissibility subtree

**Status:** UNRATIFIED / generated-snapshot / drift-prone.
**Date built:** 2026-06-09.
**Source:** distilled from an external-model audit pass (see
[[external-model-find-corrective-boundary.md]] for related external-model
provenance pattern), reclassified against current local state and
extended with corrections.
**Custody:** working note in `working/tooltheory/`. **NOT** ANNEX. **NOT**
imported into any Lean module. **NOT** kernel-adjacent. **NOT** part of
`LeanProofs.lean` or `AdmissibilityKernels.lean` build coverage.

## Caution — what this is and is NOT

This is a **receipt-indexed seam graph snapshot** over the Admissibility
subtree's declared theorems. It is intended for navigation and for
discipline (making absence and non-conversion first-class).

It is **not**:
- a topology in the mathematical sense (no opens, no continuity, no
  separation axioms);
- a category (no composition law, no identity rule, no functor);
- a unifier (no claim that the federation collapses to a common
  substrate);
- a public kernel claim (the kernels stand or fall on their own theorems,
  not on this map);
- evidence that "doctrine is validated" (the graph records what theorems
  exist, not whether they are doctrinally correct);
- a closure-under-composition (composing two edges across module
  boundaries is itself a claim requiring its own theorem; none is taken
  for granted here).

**The "federation" framing is descriptive, not algebraic.** If "topology"
appears below it is in scare quotes or qualified — never as a load-bearing
term.

**This snapshot rots.** Every kernel patch can invalidate cells silently.
Regenerate or recheck against current theorem names before treating any
entry as live. A thin theorem-name grep script is the unrotting form; a
prose snapshot is not. See §11 for regeneration approach.

## 0. Edge / cut typing (vocabulary)

All types are drawn from existing repo discipline and are theorem-backed
unless explicitly marked.

**Edge types** (positive conversions):
- **PRESERVATION** — a property carried across a transition or trajectory by theorem.
- **PROJECTION** — a richer Config/structure maps onto a kernel structure preserving the relevant set (the README's "projection pattern").
- **BRIDGE** — a proved implication or iff between two formulations of the same boundary concept.
- **CONDITIONAL** — preservation that exists only inside a structure whose obligation is discharged at construction (`CorrectiveMonotone`, `SafetyEnv.preserves`, `MergeAdmissible`). The edge is real but gated; citing it without the gate is laundering.
- **PARAMETRIC** — true only with a relation supplied as a hypothesis (`BasisInheriting`). Explicitly **not** a kernel edge; the repo's own rebar/kernel distinction.

**Cut types** (non-conversions with receipts, or receipted missing bridges):
- **BLOCKING** — universal: condition ⇒ verdict ≠ authorized / denial.
- **COUNTERMODEL** — existential: a concrete state where Surface holds and Substance fails.
- **NO-LIFT** — non-inhabitation: no bridged object exists over a given endpoint.
- **ISOLATION** — a mutation provably cannot touch a store.
- **MODEL-DEPENDENCE** — both answers exhibited in models; the abstract layer commits to neither.
- **DECLARED-MISSING** — a non-edge with a receipt: the repo documents the bridge as absent and refuses to supply it.

Every edge/cut cell below either cites an exact declaration name, or is
marked OPEN, DECLARED-MISSING, DOCSTRING-ONLY, or WITNESS-ONLY.

## 1. Nodes

Grouped by axis. Parallel-miniature nodes are marked ⟂ — they are
**copies** of kernel shapes inside specimen modules and are not
identified with the kernel nodes of the same or similar name (see §4).

**Authority axis (PUBLIC-SHIPPED):**
- N1 `BasisVerdict` / N2 `PrecedenceVerdict` / N3 `StandingVerdict` (Authority)
- N4 `AuthorityVerdict` via `authorityVerdict` (Authority)
- N5 `GovState` four-store partition: `PolicyStore`, `EvidenceStore`, `GapStore`, `RevocationStore` (StateTransition)
- N6 `Step` (governance mutation kinds) + `StepAllowed` (mutation standing) (StateTransition)
- N7 `DerivationEnv` component derivations: `BasisDerivation`, `PrecedenceDerivation`, `StandingDerivation`; `decideAuthority` (Derivation)
- N8 `AuthorizedStep` (both-proofs bundle) + `executeAuthorizedStep` (Execution)
- N9 `StepClassification` {corrective, forward, neutral} via `classify`; `WeaklyLessPermissive` preorder; `CorrectiveMonotone`; `RecoveryEnv` (Corrective)

**Temporal axis (PUBLIC-SHIPPED):**
- N10 `Fresh` = `TemporallyCoherent` ∧ `DivergenceAcceptable` ∧ `WithinValidity` (Freshness)

**Surface/cause axis (PUBLIC-SHIPPED + annex companion):**
- N11 `SurfaceStatus` × `ActionKind` × `Breaker` → `Verdict` via `authorize` (SurfaceAuthorization)
- N12 `Refines` (receipt refinement: `Excludes` ∧ some cause still admitted) (PublicReceiptRefinement)

**Witness-stability axis (PUBLIC-SHIPPED):**
- N13 `Encapsulated` / `MovesUnderExcludedPerturbation` (relational); `EncapsulatedWrt` (typed); `EncapsulatedWithinRegime` (regime-bounded) (WitnessInvariance)
- N13⟂ `ToyWitness` over `ToyState` (WitnessInvarianceToy)

**Surface-vs-substance refusal kernels (ANNEX):**
- N14 `VisibleGreen` / `RecoveryMargin` (RecoveryMargin)
- N15 `IntervalOutcome` × `ThreatState` × `SlackState` → `Verdict` (ClosureEligibility)
- N16 `Fluent` / `SettlementAdequate` (ConsolidationDenial)

**Kind axes (ANNEX):**
- N17 `ArtifactKind` × `UseKind` → `Classification` (FiatAdmissibility)
- N18 `NumericalKind` × `NumericalUse` → `Classification` (NumericalAdmissibility)
- N19 `Skew` {lagging, matched, leading} via `classifyBy` (AxisSkew)

**Cross-boundary family (ANNEX):**
- N20 `Exposure` artifacts over `Boundary`/`BoundaryPartition`; `Config`/`Reach` (CrossBoundaryExposure)
- N21 Degradation `Cause` {direct, fromExposure} over graded `Config` (CrossBoundaryDegradation)
- N22 `FailureEvent` (CrossBoundaryFailureMint)
- N23 `AuthorizedPath` (cascade reachability) (CrossBoundaryCascade)
- N24 `Process`/`SystemState` (Composition, Slice 0) and `LocalAllows`/`ComponentStep`/`MergeAdmissible` (LocalBoundary, Slice 1)

**Safety axis (ANNEX):**
- N25 `SafetyEnv` (`Allowed`, `bridge`, `preserves`); `SafeStep`; `AuthorizedTraj`/`BridgedTraj` (SafetyBridge)
- N25⟂a Receipt miniature: `nonContamination`, poison/genuine steps (SafetyBridgeWitness; AuthorizedNotSafeWitness `defendedValue`, `hasPoison`)
- N25⟂b Verdict-layer miniature: `AuthorizedStepC`, `SafeAuthorizedStepC`, `AuthorizedTrajC`/`BridgedTrajC` (AuthorizedStepNotSafeWitness, SafetyTrajectory)
- N25⟂c Ledger miniature: `Ledger`, `Act`, `ledgerEnv`, two-party `defendedValue` (AttestationLedger)
- N26 Abstract wound scenario: axiomatized `defendedValue` over kernel `GovState` (AuthorizedNotSafe, AuthorizedStepNotSafe)

**Propagation rebar (ANNEX, parametric):**
- N27 `witnesses` / `requiredFor` / `BasisInheriting` / `DependsTrans`; `Refused` / `BindingAdmissible` (RefusalPropagation)

**Boundary-result miniature (ANNEX):**
- N28⟂ `Mini.*` parallel kernel (`Mini.GovState`, `Mini.Step`, `Mini.decideAuthority`, `Mini.applySteps`); `NondegenerateStoreSemantics` fields (3.1)/(3.2)/(3.3); `PerverseRevocationEnv` perverse-revocation model (CorrectiveBoundary)

## 2. Edges (theorem-backed)

| # | Edge | Type | Theorem(s) | File |
|---|------|------|------------|------|
| E1 | all-three-green ⇄ `authorized` (N1×N2×N3 ⇄ N4) | BRIDGE | `authorized_iff_all_green` | Authority |
| E2 | `authorized` → each green component | PRESERVATION | `authorized_requires_admissible_basis`, `authorized_requires_resolved_precedence`, `authorized_requires_standing` | Authority |
| E3 | derived all-green ⇒ `decideAuthority = authorized` (N7 → N4) | BRIDGE | `decide_authorized_requires_all_green` | Derivation |
| E4 | `AuthorizedStep` → claim-side authorized verdict (N8 → N4) | PRESERVATION | `authorized_step_requires_authority` | Execution |
| E5 | `AuthorizedStep` execution carries store isolation (N8 → N5) | PRESERVATION | `authorized_record_receipt_does_not_amend_policy`, `authorized_declare_policy_gap_does_not_amend_policy`, `authorized_record_revocation_does_not_amend_policy`, `authorized_amend_policy_targets_policy_store` | Execution |
| E6 | corrective Step preserves `WeaklyLessPermissive` (N9, gated) | CONDITIONAL (`CorrectiveMonotone` discharge) | `corrective_monotone`, `corrective_sequence_monotone`, `recovery_monotone` | Corrective |
| E7 | `≼` is a preorder (reflexive, transitive) | PRESERVATION | `weakly_less_permissive_refl`, `weakly_less_permissive_trans` | Corrective |
| E8 | typed ⇄ relational encapsulation (within N13) | BRIDGE | `encapsulated_wrt_iff_relational` | WitnessInvariance |
| E9 | regime-form at universal regime ⇄ typed form (within N13) | BRIDGE | `encapsulated_within_universal_regime_iff_encapsulated_wrt` | WitnessInvariance |
| E10 | refinement-narrowing preserves encapsulation (within N13) | PRESERVATION | `encapsulated_wrt_mono`, `encapsulated_within_regime_mono` | WitnessInvariance |
| E11 | joint admission → surface admission (within N12) | PRESERVATION | `joint_admit_implies_surface_admit` | PublicReceiptRefinement |
| E12 | `Refines` → excludes-some ∧ admits-some; → collapsed surface | PRESERVATION | `refines_implies_excludes`, `refines_implies_some_admitted`, `refines_implies_collapsed_surface`, `public_receipt_refines_observation` | PublicReceiptRefinement |
| E13 | degradation Config ⇒ exposure-kernel Reach (N21 → N20) | PROJECTION | `step_to_exposure_reach`, `reach_to_exposure_reach` (`lemma`) | CrossBoundaryDegradation |
| E14 | failure-mint Config ⇒ exposure-kernel Reach (N22 → N20) | PROJECTION | `step_to_exposure_reach`, `reach_to_exposure_reach` (`lemma`) | CrossBoundaryFailureMint |
| E15 | cascade Config ⇒ exposure-kernel Reach (N23 → N20) | PROJECTION | cascade `step_to_exposure_reach` (`lemma`) + local `Reach.trans` | CrossBoundaryCascade |
| E16 | `AuthorizedPath` ⇒ ∃ reachable endpoint exposure (within N23) | PRESERVATION (existential — *permits* not *will*) | `authorized_path_permits_endpoint_exposure` | CrossBoundaryCascade |
| E17 | `bridge` ⇒ value floor preserved; `SafeStep` ⇒ safe (within N25, gated) | CONDITIONAL (`preserves` discharge) | `bridge_implies_safe`, `safeStep_is_safe`, `bridgedTraj_preserves`, `bridge_two_step_preserves` | SafetyBridge |
| E18 | bridged trajectory ⇒ authorized trajectory (forgetful, within N25/N25⟂b) | PROJECTION | `BridgedTraj.toAuthorizedTraj`, `BridgedTrajC.toAuthorizedTrajC`, `SafeStep.toAuthStep`, `SafeAuthorizedStepC.toSafeStep` | SafetyBridge, SafetyTrajectory, AuthorizedStepNotSafeWitness |
| E19 | bridged verdict-layer trajectory preserves floor (N25⟂b, gated) | CONDITIONAL | `bridgedTrajC_preserves`, `genuineTraj_preserves_value` | SafetyTrajectory |
| E20 | concrete bridges discharge `preserves` (N25⟂a, N25⟂c) | CONDITIONAL discharge | `nonContamination_preserves` (receipt), `bridge_preserves` (ledger), `genuinePost_safe` | SafetyBridgeWitness, AttestationLedger |
| E21 | refusal propagates along supplied basis-inheritance (N27) | PARAMETRIC — **not a kernel edge** | `refusal_composes`, `refusal_composes_two_hop`, `refusal_propagates_transitively`, `refused_blocks_binding`, `cascade_implies_basis_inheriting`, `downstream_proposal_cannot_bind_when_claim_basis_refused` | RefusalPropagation |
| E22 | `NondegenerateStoreSemantics` ⇒ corrective+forward non-monotonicity existential (N28⟂) | PRESERVATION (consumes field (3.3) only) | `corrective_then_forward_is_not_monotone_of_nondegenerate`, `witness_satisfies_nondegenerate`, `witness_corrective_then_forward_is_not_monotone_via_abstract` | CorrectiveBoundary |
| E23 | local authorization + merge soundness ⇒ global safety (N24, gated, experimental) | CONDITIONAL (`MergeAdmissible` discharge) | `composition_preserves_global_safety_aperture`; Slice-0 diagnostic `any_process_safe_under_sealed_boundary`, `composition_preserves_safety_global_lift` | LocalBoundary, Composition |
| E24 | discriminator licenses cause-specific action (N11) | PRESERVATION | `discriminator_licenses_cause_specific`, `discriminating_surface_permits_all`, `collapsed_surface_permits_observe` | SurfaceAuthorization |
| E25 | public-surface specimen consumers (positive paths through N4/N8) | PRESERVATION (specimen) | `specimen_valid_advisory_result`, `specimen_valid_authorized_mutation`, `specimen_open_finding_accounted` | Examples |
| **E26** | **mixed-class witness ⇒ verdict-sensitive (N28⟂, within `NondegenerateStoreSemantics`)** | **PRESERVATION** | **`mixed_class_witness_implies_verdict_sensitive`** | **CorrectiveBoundary** |

E26 records the (3.3) → (3.2) derivation. The corollary at the structure
level is `fun h => mixed_class_witness_implies_verdict_sensitive
h.mixed_class_witness`. The companion direction (3.3) → (3.1) is **not**
claimed as an edge — see O2.

Note on E21: the repo's own docstrings type this family as rebar — "the
structural assumption is doing the work; the theorem is contrapositive
packaging." Listing it as PARAMETRIC here is what keeps the Roadmap's
composition-axis promotion gate intact.

## 3. Cuts (theorem-backed non-conversions + receipted missing bridges)

The StateTransition section (formerly one muddy cell) is now split into
three rows reflecting three distinct edge species.

### 3a. StateTransition — split accounting

**Policy-column isolation cuts** (non-amendment Steps ⇏ `PolicyStore` mutation):

| # | Cut | Type | Theorem(s) | File |
|---|-----|------|------------|------|
| C2a | `recordReceipt` ⇏ policy mutation | ISOLATION | `record_receipt_does_not_amend_policy` (+ execute lift) | StateTransition |
| C2b | `declarePolicyGap` ⇏ policy mutation | ISOLATION | `declare_policy_gap_does_not_amend_policy` (+ execute lift) | StateTransition |
| C2c | `recordRevocation` ⇏ policy mutation | ISOLATION | `record_revocation_does_not_amend_policy` (+ execute lift) | StateTransition |

**Privileged-write positive target** (the privileged write does target PolicyStore — this is the *positive* edge corresponding to the trapdoor, included here for completeness of the matrix accounting, not as a cut):

| # | Edge | Type | Theorem(s) | File |
|---|------|------|------------|------|
| E27 | `amendPolicy` targets PolicyStore | PRESERVATION (positive witness) | `amend_policy_targets_policy_store` (+ execute lift) | StateTransition |

**AmendPolicy-row isolation cuts** (the privileged write touches *only* PolicyStore):

| # | Cut | Type | Theorem(s) | File |
|---|-----|------|------------|------|
| C2d | `amendPolicy` ⇏ `EvidenceStore` mutation | ISOLATION | `amend_policy_preserves_evidence_store` | StateTransition |
| C2e | `amendPolicy` ⇏ `GapStore` mutation | ISOLATION | `amend_policy_preserves_gap_store` | StateTransition |
| C2f | `amendPolicy` ⇏ `RevocationStore` mutation | ISOLATION | `amend_policy_preserves_revocation_store` | StateTransition |
| C2g | row-level corollary | ISOLATION (row corollary) | `amend_policy_preserves_other_stores` | StateTransition |

**Explicit non-claim:** the StateTransition trapdoor matrix has 4 steps ×
3 non-target stores = 12 off-diagonal cells. C2a–C2f together fill 6 of
them (the policy column and the amendPolicy row). **The remaining six
off-diagonal cells are OPEN** — e.g., `recordReceipt` preserving
`GapStore`, `recordRevocation` preserving `EvidenceStore`, etc. No
theorem of "full four-store orthogonality" is claimed or implied.

### 3b. Remaining cuts (other modules)

| # | Cut | Type | Theorem(s) / receipt | File |
|---|-----|------|----------------------|------|
| C1 | each non-green component ⇏ `authorized` | BLOCKING | `no_basis_never_authorized`, `advisory_basis_never_authorized`, `incomparable_precedence_never_authorized`, `conflicting_precedence_never_authorized`, `no_standing_never_authorized` | Authority |
| C3 | revoked basis ⇏ authorized; revoked standing ⇏ standing/authorized | BLOCKING | `revoked_basis_never_authorized`, `revoked_standing_never_authorized` | Derivation |
| C4 | revoked basis ⇏ inhabitable `AuthorizedStep` | NO-LIFT | `revoked_basis_cannot_be_authorized_step` | Execution |
| C5 | corrective Step ⇏ same-basis authority increase | BLOCKING | `corrective_no_authority_laundering`; class disjointness `corrective_not_forward`, `corrective_not_neutral` | Corrective |
| C6 | each temporal failure ⇏ `Fresh` | BLOCKING | `expired_not_fresh`, `not_yet_valid_not_fresh`, `incoherent_not_fresh`, `not_precedes_not_fresh`, `divergence_excessive_not_fresh` | Freshness |
| C7 | collapsed surface + cause-specific + no breaker ⇒ deny | BLOCKING | `collapsed_surface_denies_cause_specific_without_breaker`, `collapsed_surface_denies_causeSpecificMutation`, `collapsed_surface_denies_revokeStanding` | SurfaceAuthorization |
| C8 | trivial receipt ⇏ refinement; contradictory receipt ⇏ refinement; refinement ⇏ identification | BLOCKING | `trivial_receipt_does_not_refine`, `contradictory_receipt_does_not_refine`, `multiple_joint_admit_means_not_identified`, `multiple_joint_admit_no_unique`, `refines_without_identification` | PublicReceiptRefinement |
| C9 | moves-under-excluded-perturbation ⇏ encapsulated (all three forms); selectivity ⇏ encapsulation | BLOCKING + COUNTERMODEL | `moves_implies_not_encapsulated`, `moves_under_disturbance_implies_not_encapsulated_wrt`, `moves_within_regime_implies_not_encapsulated_within_regime`; toy: `selectivity_does_not_imply_encapsulation`, `toy_witness_not_syntax_encapsulated` | WitnessInvariance |
| C10 | `VisibleGreen` ⇏ `RecoveryMargin` | COUNTERMODEL | `visible_green_does_not_imply_recovery_margin`; dynamics: `zero_margin_non_green_next_red`, `red_zero_margin_stays_red` | RecoveryMargin |
| C11 | survival ⇏ closure | BLOCKING + COUNTERMODEL | `survival_alone_does_not_authorize_closure`, `survived_unresolved_requires_handoff`, `survived_depleted_requires_handoff`, `closure_requires_resolution_and_slack`, `verdict_closure_iff` | ClosureEligibility |
| C12 | `Fluent` ⇏ `SettlementAdequate` | COUNTERMODEL | `fluency_does_not_witness_settlement` | ConsolidationDenial |
| C13 | prestige ⇏ support; metaphor ⇏ derive; proxy ⇏ self-certified magnitude; fiat ⇏ state mutation | BLOCKING | `prestige_cannot_support`, `metaphor_cannot_derive`, `proxy_cannot_self_certify_magnitude`, `fiat_does_not_govern_state_mutation` | FiatAdmissibility |
| C14 | score ⇏ magnitude; confidence ⇏ truth; rank ⇏ magnitude/substrate; etc. | BLOCKING (per-cell) | `score_cannot_imply_magnitude`, `confidence_cannot_imply_truth`, `rank_cannot_imply_magnitude`, `probability_cannot_imply_truth`, `rank_cannot_imply_substrate`, `confidence_cannot_imply_substrate`, `probability_cannot_imply_substrate` | NumericalAdmissibility |
| C15 | sealed boundary ⇏ Internal→External exposure (and lifts) | BLOCKING (invariant) | `no_external_exposure_without_authorized_edge`; lifted: `no_external_degradation_from_internal_exposure`, `no_exposeFromFailure_internal_to_external`, `no_external_exposure_from_internal_failure` | CrossBoundary* |
| C16 | `StepAllowed` ⇏ defended-value preservation (mutation-layer wound) | COUNTERMODEL (axiomatized, consistency witnessed) | `authorized_not_safe`; discharge: `authorized_not_safe_witnessed`, `scenario_joint_witness`, `scenario_state_changes` | AuthorizedNotSafe(+Witness) |
| C17 | kernel-legible all-green `AuthorizedStep` ⇏ safe (verdict-layer wound) | COUNTERMODEL | `authorized_step_not_safe`, `authorizedStep_admits_unsafe_witness`; concrete `authorizedStepC_not_safe` | AuthorizedStepNotSafe(+Witness) |
| C18 | authorized trajectory ⇏ floor preserved; poison endpoint admits no bridged trajectory | COUNTERMODEL + NO-LIFT | `authorized_trajectory_loses_value`, `poisonTraj_loses_value`, `no_bridgedTrajC_to_poison_end`; receipt-layer `poison_not_bridged`, `no_safeStep_for_poison`, `bridge_separates_authorized_steps`; ledger-layer `revoke_authorized` + `revoke_not_bridged` + `revoke_loses_value` + `no_safeStep_for_revoke` | SafetyTrajectory, SafetyBridgeWitness, AttestationLedger |
| C19 | corrective-then-forward monotonicity: Identity model FALSE / Witness model TRUE | MODEL-DEPENDENCE | `corrective_then_forward_is_monotone_universally` (Identity), `corrective_then_forward_is_not_monotone` (Witness) — abstract kernel committed to neither | CorrectiveBoundary |
| C20 | receipt without authority ⇏ upgrade; self-cert ⇏ basis; stale evidence ⇒ refusal; conflicting precedence ⇒ denial | BLOCKING (specimen) | `specimen_receipt_no_authority_upgrade`, `specimen_self_cert_denial`, `specimen_stale_evidence_refusal`, `specimen_conflicting_precedence_denial` | Examples |
| C21 | `Skew` cannot be lagging and leading on the same axis | BLOCKING | `not_lagging_and_leading_same_axis` | AxisSkew |
| C22 | invocation standing (`deriveStanding`) ⇄ mutation standing (`StepAllowed`) | **DECLARED-MISSING** | README "What it does NOT warrant" + `Derivation.lean` L37–40, L244–247 ("bridge them later if a concrete `amendPolicy` claim forces it") | Derivation / StateTransition |
| C23 | `Fresh` ⇄ authority kernel (temporal admissibility as input to `BasisDerivation`) | **DECLARED-MISSING** | Freshness defer-marker ("Composition with the other admissibility kernels is explicitly deferred") | Freshness |
| C24 | `FiatAdmissibility`/`NumericalAdmissibility` classifications ⇄ `AuthorityVerdict` | **DECLARED-MISSING** | both modules' "composition lemmas explicitly deferred" markers | FiatAdmissibility, NumericalAdmissibility |
| C25 | `BasisInheriting` as kernel-level theorem over `deriveBasis`/`decideAuthority` | **DECLARED-MISSING** | RefusalPropagation docstring: instantiation "not in this probe"; Roadmap composition-axis gate | RefusalPropagation |
| C26 | actor-sensitive safety bridges | **DECLARED-MISSING** | `ActorSensitiveBridgeEnv` declared in SafetyBridge Open block, not implemented | SafetyBridge |
| C27 | cascade ultimate provenance | **DECLARED-MISSING** | `CascadeChain` named-not-built; immediate-origin discipline forbids overloading `Exposure.origin` | CrossBoundaryCascade |
| C28 | `MergeAdmissible` necessity (each field load-bearing via counterexample) | **DECLARED-MISSING** | LocalBoundary Open obligation 1, "Status: not started" | LocalBoundary |

## 4. Name-similarity traps (non-identifications)

Per the "no edge by name similarity" constraint, these same-named or
similar-shaped nodes are **distinct** and carry no identifying edge:

- **`Step` family.** `StateTransition.Step` ≠ `CrossBoundaryExposure.Step` ≠ `Composition.StepP` ≠ `CorrectiveBoundary.Mini.Step` ≠ `AuthorizedNotSafeWitness.Step` ≠ `AttestationLedger.Act`. Five-plus mutation vocabularies, **zero cross-theorems**.
- **`defendedValue` family.** Exists in four places (AuthorizedNotSafe axiomatic; AuthorizedNotSafeWitness/AuthorizedStepNotSafeWitness receipt miniature; AttestationLedger `Nat` ledger). Same word, separate functions; the only relations are the per-module wound theorems.
- **`Reach` family.** Defined per cross-boundary module; relations exist **only** through the explicit `toExposureConfig` / `step_to_exposure_reach` / `reach_to_exposure_reach` projection lemmas (E13–E15). Cascade ↔ Degradation: no edge at all (Cascade deliberately does not import Degradation).
- **Kernel `GovState` vs miniature `GovState`.** All wound transfer from miniature to kernel is via *consistency discharge* (the wound axioms are jointly satisfiable in a parallel model), never via identification.
- **Standing.** `StandingVerdict.standing` (claim invocation) vs `*Standing` predicates (mutation) — C22.

## 5. Open cells

Cells with **neither** a theorem-backed edge **nor** a theorem-backed cut.
Asserting either direction is overclaiming. Naming the cell is naming
work that has not been done — not a license to do it.

- **~~O1~~ (closed → E26).** `(3.3) → (3.2)` formerly listed as open; closed by `mixed_class_witness_implies_verdict_sensitive`. **Promoted to E26 above.**
- **O2.** `(3.3) → (3.1)` — claimed **false** in the `NondegenerateStoreSemantics` docstring (a model can witness (3.3) through revocation/evidence steps while `applyUpdate` stays identity). **Status:** WITNESS-ONLY. The perverse-revocation model `PerverseRevocationEnv` in `CorrectiveBoundary.lean` exhibits exactly this — `applyUpdate_trivial` proves (3.1) fails, `mixed_class_witness_holds` proves (3.3) holds, satisfying the implication-failure shape — but **no named theorem states the cell relation directly** (e.g. no `mixed_class_witness_does_not_imply_applyUpdate_nontrivial`). The countermodel witness exists; the cell theorem does not.
- **O3.** Corrective × safety: do classify-corrective Steps (`declarePolicyGap`, `recordRevocation`) preserve any `defendedValue`-shaped floor? No theorem, no countermodel. (AttestationLedger's `revoke_loses_value` is suggestive — an authorized revoke destroying value — but it lives on `Act`, not kernel `Step`; using it here would be a name-similarity bridge.)
- **O4.** Freshness × Derivation mechanism: C23 receipts the deferral, but no theorem shape is even drafted for "stale evidence ⇒ basis not admissible" at kernel level (the `specimen_stale_evidence_refusal` specimen exercises it through a concrete env only).
- **O5.** WitnessInvariance × Derivation: encapsulation-of-witness as an obligation field on `BasisDerivation` (the way `revoked_never_admissible` became structural on 2026-06-03). Neither bridged nor refused.
- **O6.** Cross-boundary family × governance kernel: no projection in either direction between `CrossBoundaryExposure.Config` and `GovState`. Entirely open — and the most tempting name-similarity trap in the repo (`Step`/`Step`).
- **O7.** RecoveryMargin / ClosureEligibility / ConsolidationDenial pairwise: the prose siblings ("within-interval / end-of-interval / between-interval") share no formal substrate; no theorem relates their `System`/`IntervalOutcome` types.
- **O8.** `AxisSkew` × everything: isolated node; no edges, no cuts.
- **O9.** NumericalAdmissibility × FiatAdmissibility: same `Classification` *shape*, separate inductives, no cross-theorem (and correctly so — but the cell is open, not closed).
- **O10.** Safety axis × refusal-propagation axis: the Roadmap declares them independent; independence here is *doctrine*, not a theorem-backed cut. The graph records this cell as open, not as a proved orthogonality.
- **OST6.** The six remaining off-diagonal cells of the StateTransition trapdoor matrix (non-amend steps preserving non-target stores) — see §3a's explicit non-claim.

## 6. Absence is first-class

Three mechanisms in this snapshot keep "we have not proved X" from drifting into "X is settled":

1. **Open is a status, not a default.** A cell with no entry in §2 or §3 appears in §5. Cells never go missing into silent closure.

2. **No closure operator.** Edges do not compose across module seams by transitivity in this document. E13 + C15 yields C15-lifted *only because the repo proved the lift* (`no_external_degradation_from_internal_exposure`); where the repo did not prove a composite, the composite is not an edge here.

3. **Typed edges block silent strengthening.** CONDITIONAL edges (E6, E17, E19, E23) cannot be cited without their gate; PARAMETRIC edges (E21) cannot be cited as kernel facts; PROJECTION edges move sets, not authority. Each laundering move the kernels exist to refuse corresponds to an attempted type-coercion on an edge — e.g., reading E18's forgetful map backwards is exactly C18's no-lift; reading E21 as kernel transitivity is exactly C25's missing bridge. The typing makes the illegal reading visible at the type level of the inventory.

§4 closes the cheapest overclaim route: same-named primitives across modules are non-identifications by default; identification requires a cited projection theorem.

## 7. Doctrine connections

- **[[project-no-unifier-without-laundering]]** — this graph is non-closed deliberately. The "five fractured relational vocabularies" of that doctrine appear here as the typed edge species; the bumper sticker "nothing composes for free" is structurally enforced by §6.2 (no closure operator).
- **[[project-anti-laundering-doctrine-map]]** — every PARAMETRIC and CONDITIONAL edge type, and every DECLARED-MISSING cut, is a refusal-kernel candidate by the family table.
- **[[feedback-claude-common-mode-synthesis]]** — the graph's vocabulary and the §7-style framings ("absence is first-class," "federation becoming X") are synthesis-altitude when used as descriptive doctrine, not as artifact-level claims. The artifact-level claims (theorem names + cell entries) are verifiable; the descriptive framings are candidate.

## 8. Provenance + verification receipt

- **Source.** Distilled from an external-model (Anthropic web, "Fable" 2026-06-09 release; common-mode with Claude Code) audit pass + chatgpt critique + local reclassification.
- **Verification.** All 141 distinct theorem/def/inductive/structure/namespace/lemma identifiers cited above were bulk-checked against `/tmp/decls.txt` (built from `grep -rhoE 'theorem|def|inductive|structure'` over `LeanProofs/Admissibility/*.lean`) plus a manual probe for the three remaining (`PerverseRevocationEnv` is a namespace; `step_to_exposure_reach` and `reach_to_exposure_reach` are `lemma`s). **Zero genuinely missing names.** Verification is **declaration-existence only** — it does NOT certify semantic content, proof correctness, or doctrinal accuracy of the docstrings cited under DECLARED-MISSING.
- **Build state.** `lake build` was green at 8306 jobs as of the patches recorded earlier in the parent conversation (E26 / C2d–C2g all green under 4.29.0).
- **Caveat.** Theorem-name grep confirms declarations, not semantic completeness. A theorem can exist and be wrong; a theorem can exist with a misleading docstring; a theorem's *statement* can drift from what this graph claims it does. Spot-check before citing any cell against a stronger claim than "the name resolves."

## 9. What this snapshot does NOT support

- It does not authorize calling the corpus a "calculus," a "topology," or a "category."
- It does not validate any of the doctrine notes it points to in §7 — those stand or fall on their own.
- It does not constitute a promotion gate. Cells appearing as PARAMETRIC or CONDITIONAL or DECLARED-MISSING remain so; this document is a navigation aid, not an upgrade path.
- It does not close the maximal-calculus refusal. The "no unifier without laundering" finding is the load-bearing post-axes result; this snapshot is consistent with that finding and does not weaken it.
- It does not justify new abstraction. Cells named here are candidates for review, not for build. Per the YAGNI / completeness composition rule: existence of a named open cell is **not** a forcing case.

## 10. Redshift corrections applied (vs source audit)

1. **O1 → E26.** Reclassified from "blocked theorem shape" to theorem-backed edge with cited name `mixed_class_witness_implies_verdict_sensitive`. No new theorem written; the existing one was added in a prior session.
2. **C2 split.** The single muddy StateTransition cell decomposed into three distinct species: C2a–C2c (policy-column isolation cuts), E27 (privileged-write positive target — moved to the edge table), C2d–C2g (amendPolicy-row isolation cuts including row corollary). Explicit non-claim: 6 off-diagonal cells remain OPEN (OST6).
3. **O2 properly characterized.** Status WITNESS-ONLY — `PerverseRevocationEnv` exhibits the implication-failure shape, but no named theorem states the cell relation directly. Not presented as fully closed.
4. **Stale-risk header** added (§ status + § caution + § 8 caveat).
5. **Custody-class downgrade.** Source called this an "ANNEX." That custody class is reserved for files under `LeanProofs/Admissibility/`. This snapshot lives in `working/tooltheory/` and carries no custody class beyond UNRATIFIED working note.

## 11. Regeneration

This snapshot will drift. To detect drift cheaply:

```bash
cd ~/git/lean/LeanProofs/Admissibility
# Build current declaration index:
grep -rhoE 'theorem +[a-zA-Z_][a-zA-Z0-9_]+|def +[a-zA-Z_][a-zA-Z0-9_]+|inductive +[a-zA-Z_][a-zA-Z0-9_]+|structure +[a-zA-Z_][a-zA-Z0-9_]+|lemma +[a-zA-Z_][a-zA-Z0-9_]+|namespace +[a-zA-Z_][a-zA-Z0-9_]+' *.lean | awk '{print $2}' | sort -u > /tmp/decls-now.txt
# Compare to claims (this file's identifiers):
grep -oE '`[a-zA-Z_][a-zA-Z0-9_]+`' ~/git/papers/working/tooltheory/seam-graph-candidate.md \
  | tr -d '`' | sort -u > /tmp/claims-now.txt
comm -23 /tmp/claims-now.txt /tmp/decls-now.txt
```

Any output is a stale name in this snapshot. The right unrotting form is
a small generator script; this prose snapshot is a one-time review aid.

## 12. Useful concepts preserved (changelog vs source)

Preserved verbatim from source audit:
- Five edge types (PRESERVATION / PROJECTION / BRIDGE / CONDITIONAL / PARAMETRIC).
- Six cut types (BLOCKING / COUNTERMODEL / NO-LIFT / ISOLATION / MODEL-DEPENDENCE / DECLARED-MISSING).
- Node inventory across 28 nodes including ⟂ miniature distinction.
- Name-similarity trap discipline (§4).
- "Absence is first-class" / "no closure operator" / "no edge by name similarity" framings (§6, with re-grounding).
- Every edge/cut citing an exact declaration name or marked OPEN / DECLARED-MISSING / WITNESS-ONLY / DOCSTRING-ONLY.

Not preserved / explicitly downgraded:
- "Federation becoming topology" — refused as load-bearing phrasing. The word "topology" appears in this file's title in scare quotes only via the "seam-graph" naming; §0 explicitly disclaims topology / category / unifier readings.
- "ANNEX" custody framing for this document — downgraded to working-note status.
- "Picked cell" theorem-production handoff — explicitly held per pass scope.
