# Safety-bridge family — kernel-overlap audit (2026-05-29)

**Filed:** 2026-05-29
**Status:** Audit document. Closes the kernel-overlap gate named in
`README.md` §Safety-bridge family, `LeanProofs/Admissibility/README.md` §Roadmap
(*"minting still gates on the kernel-overlap audit and an exit-criteria update"*),
`WHAT-THE-LEAN-STACK-PROVES.md` §Infrastructure: Safety bridge, and
`working/calculus-2-exit-criteria.md` §Track split (*"ratifiable now as the
safety-axis publication path, gated on the kernel-overlap audit and this
reconciliation pass"*). The reconciliation pass landed 2026-05-29; this is the
companion gate.

**Lean modules under audit (8):**
- `LeanProofs/Admissibility/AuthorizedNotSafe.lean`
- `LeanProofs/Admissibility/AuthorizedNotSafeWitness.lean`
- `LeanProofs/Admissibility/SafetyBridge.lean`
- `LeanProofs/Admissibility/SafetyBridgeWitness.lean`
- `LeanProofs/Admissibility/AuthorizedStepNotSafe.lean`
- `LeanProofs/Admissibility/AuthorizedStepNotSafeWitness.lean`
- `LeanProofs/Admissibility/SafetyTrajectory.lean`
- `LeanProofs/Admissibility/AttestationLedger.lean`

## What this audit is

The standard kernel-overlap audit per [[feedback-kernel-overlap-audit]]: before
the safety-bridge family promotes from "annex, candidate" to "named anchor of a
formal-methods preprint," check whether the existing kernel already does this
work under different vocabulary, and name the structural delta that justifies
the family as new content. This is the substrate-contact gate; without it the
preprint risks publishing a re-derivation of `Corrective` / `Execution` /
`WitnessInvariance` under safety-axis vocabulary.

The companion outside-aperture work — Frontier 1 of `FRONTIERS.md` (named the
wound 2026-05-10), the multi-model tier-map (`calculus-2-tier-map-2026-05-28.md`),
the ρ-drop decision (`safety-bridge-rho-drop-decision-2026-05-28.md`), and
today's exit-criteria reconciliation (`calculus-2-exit-criteria.md` §Track
split) — already settled *what* the family claims and *which label* it earns.
This audit settles *whether the family duplicates an existing kernel.*

## Proof patterns: reused, novel, hybrid

### Reused (honest credit, not duplication)

| Pattern | Existing precedent | Safety-bridge instance |
|---|---|---|
| Existential countermodel for `Surface ⇏ Substance` | `RecoveryMargin`, `ClosureEligibility`, `ConsolidationDenial` | `AuthorizedNotSafe`: `∃ s a, StepAllowed s a ∧ ¬ value-preserving` |
| Parallel-miniature consistency discharge | `CorrectiveBoundary` (identity-store + witness model) | `AuthorizedNotSafeWitness`: `List Receipt` miniature discharging the axiomatic wound |
| Bundled-obligation env (function + spec) | `Corrective.CorrectiveMonotone` / `RecoveryEnv`, `Derivation.DerivationEnv` | `SafetyBridge.SafetyEnv`: `bridge` field + `preserves` proof obligation |
| Verdict-layer transfer via bundled construction | `Execution.AuthorizedStep` (stepAllowed + claim verdict by construction) | `AuthorizedStepNotSafe(Witness)` + `SafeAuthorizedStepC` (stepAllowed + claim verdict + bridge witness) |
| Env-supplies-the-strategy parametricity | `Derivation.DerivationEnv` carries `BasisDerivation` etc. | `SafetyEnv (σ α ρ : Type)` parametric over state/action/actor |

This pattern reuse is *the kernel discipline doing its job.* Each safety-bridge
brick uses the same proof shape the surrounding kernel established — that is
how the family stays cite-able from the rest of the calculus rather than
forking off into its own idiom.

### Novel

| Pattern | Why it isn't already in the kernel |
|---|---|
| **State-threaded inductive trajectory family with per-hop witness** (`AuthorizedTraj`, `BridgedTraj`) | `Corrective.corrective_sequence_monotone` composes flat `List Step` because `IsCorrective` is state-independent. Authorization-AND-bridging is state-*dependent*: the next hop's authorization holds at the state the previous hop produced. A flat-list lift would collapse to "a list of independently-authorizable actions" — the exact substitution `AuthorizedStep` was built to refuse. |
| **Forgetful map between trajectory families** (`BridgedTraj.toAuthorizedTraj`) | Turns *"an authorized trajectory that does not lift to a bridged one"* from rhetoric into a *typed function*. The Loop-Capture doctrinal slogan becomes a definition the kernel can quantify over. No existing kernel module has a forgetful-map shape between richer and poorer witness types — `Execution.AuthorizedStep` projects to `StepAllowed` via field access, not as a typed map between inductive families. |
| **Trajectory triple as composition shape** (positive / negative / no-lift) | The existing kernel has *single-step* refusal shapes (`RecoveryMargin` etc.) and *bundled-construction* shapes (`AuthorizedStep`); it does not have a *trajectory-level* shape where a negative result is *composable* (no extension recovers the bridge). `no_bridgedTraj_to_poison_end` is the composition shape that distinguishes a single-step wound from a trajectory-level admissibility failure. |
| **Two-witness ρ-drop confirmation** | The ρ-drop decision (actor-inert base `bridge : σ → α → Prop`, actor stays in `Allowed`) needed evidence on non-degenerate witnesses. The receipt model has `Actor := Unit` — the actor-inert constraint is vacuous there. `AttestationLedger` instantiates with two asymmetric actors (`writer` / `auditor`); authorization genuinely reads the actor, bridge genuinely ignores it. The post-hoc evidence that ρ-drop was the right call lives in this second instantiation; no other kernel module supplies it. |

### Hybrid (pattern reuse with novel axis content)

The `preserves` obligation has the same shape as `Corrective.CorrectiveMonotone`
but its *content* is a separate axis:

- `CorrectiveMonotone env` asserts: *if `classify s = corrective` then the
  resulting derivation is weakly-less-permissive than before.* Axis:
  authorized-action-set.
- `SafetyEnv.preserves` asserts: *if `bridge s a` holds and `a` is allowed at
  `s` then `value s ≤ value (run s a)`.* Axis: externally-defined defended
  value.

Same bundled-obligation pattern, orthogonal axis. The novelty is the axis (and
the trajectory machinery that lifts it), not the obligation discipline.

## Demoted / deferred candidates

Recorded so the audit trail shows what was *not* built:

- ~~`ActorSensitiveBridgeEnv` as base primitive~~ → **named-but-not-implemented
  Open block in `SafetyBridge.lean`.** ρ-drop decision: if actor identity
  affects transition semantics, the transition relation itself must become
  actor-indexed (`run : σ → ρ → α → σ`), not smuggled through `bridge`.
  Smuggling actor-dependence through `bridge` is authorization wearing a safety
  mustache; the audit refuses it.
- ~~Trajectory-global actor (`AuthorizedTraj (a : Actor)`)~~ → **per-hop actor
  in `AttestationLedger.LedgerAuthStep`.** Refactor at the generic
  `SafetyTrajectory.lean` layer is deferred to a separate brick (touches
  brick 1's downstream). The ledger demonstrates the shape; the generic
  generalization waits for a precise reuse theorem and compatibility review outside the ledger; a runtime consumer is not required.
- ~~Tier 2A budget-margin model (value-axis generalization)~~ → **deferred per
  `calculus-2-tier-map-2026-05-28.md`.** Theorem rewrite (`bridgedTraj_preserves`
  → "trajectory stays above floor") + `Preorder V` generalization. Held until
  a concrete, discriminating value-decrease model is specified (budget spend,
  retry-token consumption). That model may be formal and may lead runtime code.
- ~~Tier 2B quorum model (authorization-axis generalization)~~ → **deferred.**
  Role → certificate; intersection-invariant inside `preserves`; bridge stops
  being constructor-inspection. Held until a concrete collective-authorization
  model arrives.
- ~~Maximal safety policy (`bridge := preserves-restated`)~~ → **structurally
  refused.** A maximal bridge collapses bridge into "value-preserving";
  `SafetyBridgeWitness` and `AttestationLedger` both ship deliberately
  *conservative* structural bridges that reject every wound but also some
  value-preserving actions. The audit accepts this as the correct trade for
  *checkable-without-running-the-action.*
- ~~Substantive-grounding claim ("real institutional legitimacy fails to entail
  safety")~~ → **out of scope by design.** The bricks use kernel-legible
  all-green via degenerate `fun _ _ => …` derivation env — sufficient to
  settle the type-level structural question. The Loop-Capture / `L_t` reading
  is a doctrinal mapping that the *interpretive paper (paper 28)* discharges,
  not the formal preprint. This fence is the same fence that lives inside the
  kernel; the audit confirms the family inherits it correctly.

## Cross-family overlap check

Per the audit discipline, check that the safety-bridge family does not
re-derive content from sibling families under different vocabulary.

| Sibling | Does it overlap? | Why not |
|---|---|---|
| `Corrective` | No | Different axis (authorized-action-set, not defended value). Same obligation *shape*, different *content*. |
| `WitnessInvariance` | No | Different axis (cognitive boundary syntax/semantics, not value preservation across transitions). Both supply "bridge"-ish predicates but the witness-invariance bridge is about *encapsulated computation under perturbation*, not *value-preserving transition under authorization*. |
| `SurfaceAuthorization` | No | Refuses *cause-specific actions under collapsed surface*, parameterized refusal rule. Does not address value-preservation; cannot exhibit the safety-bridge wound. |
| `RecoveryMargin` / `ClosureEligibility` / `ConsolidationDenial` | No | Existential countermodel refusal kernels for different surface→substance inferences (visible-green → capacity, survival → closure, fluency → settlement). Same proof-pattern *shape*; different inferences blocked. `AuthorizedNotSafe` is the same shape applied to *authorization → safety*. Honest precedent reuse, not coverage duplication. |
| `CrossBoundary*` family | No | Exposure-mint discipline (forbidden-artifact-unconstructible under sealed boundary). Different artifact (cross-boundary exposure, not defended value). Different theorem family (containment under sealed boundary, not trajectory triple). |
| P27 obligation skeleton (`Admissibility.lean`) | No | Post-transition obligation accounting; safety-bridge is pre/in-transition value preservation. Complementary, not overlapping. |

No reparenting required. The family lives in `Admissibility/` as annex
modules — the same home as `Corrective`, `WitnessInvariance`, and the other
refusal kernels.

## The keeper residues

Audit residues — what specifically the family contributes that the kernel
otherwise lacks:

1. **The forgetful map turns Loop Capture into a definition.**
   `BridgedTraj.toAuthorizedTraj` makes *"an authorized trajectory that does
   not lift to a bridged one"* a typed predicate over trajectory families. The
   slogan is no longer rhetorical; it has a type.

2. **The trajectory triple is the composition shape.** Single-step wound +
   bridge would be a one-shot result like the existential refusal kernels.
   `bridgedTraj_preserves` (positive) + `authorized_trajectory_loses_value`
   (negative) + `no_bridgedTraj_to_poison_end` (no-lift) is what makes the
   negative result *survive composition*. The no-lift is the distinctive
   theorem; without it, an authorized trajectory might still be salvageable
   by retrofit-bridging, which would defeat the wound.

3. **Two-witness ρ-drop evidence.** Receipt model (`Actor := Unit`) +
   ledger model (`writer` / `auditor`) jointly confirm: authorization reads
   the actor; bridge ignores it. The asymmetry is genuine, not artifact.
   This is the load-bearing decision for what `SafetyEnv` will mean in
   downstream extensions.

4. **Verdict-layer canonical gate (`SafeAuthorizedStepC` + `.toSafeStep`).**
   The wound transfers from `StepAllowed` to the full `AuthorizedStep`
   verdict object; the canonical gate bundles authorization + bridge witness
   without consuming `Allowed` in the safety projection. Same bundled-
   construction pattern as `Execution.AuthorizedStep` extended with a new
   dimension.

5. **The `Authorized ≠ Safe` axis as a first-class kernel claim.** The 1.0
   surface (`CalculusOne`) refuses laundering across surface / freshness /
   witness / authority axes; the safety-bridge family adds *value
   preservation* as an orthogonal refusal axis. The annex now has a fifth
   axis with its own bridge primitive and its own trajectory theorem.

## What this audit does NOT do

- Does not mint "Calculus 2.0." The full-label gate has three axes
  (safety / composition / self-amendment); only safety is met (see
  `working/calculus-2-exit-criteria.md` §Track split). The audit closes the
  safety-axis publication-path gate, not the rename.
- Does not promote the family from annex to `CalculusOne`. The 1.0 surface is
  unchanged; the safety-bridge family stays in the annex per
  `LeanProofs/Admissibility/README.md` §Annex.
- Does not schedule tier-2 work. Tier 2A (budget-margin) and tier 2B (quorum)
  retain their model/theorem-shape gates, but neither waits for a runtime forcing case.
- Does not foreclose the trajectory-global → per-hop actor refactor at the
  generic layer. The ledger ships per-hop; the generic refactor is a separate
  brick when formal reuse and compatibility justify it.
- Does not discharge substantive-grounding. The Loop-Capture institutional
  reading remains a doctrinal mapping for paper 28, not a Lean claim here.

## Gate status

| Gate | Status |
|---|---|
| Safety-axis exit criteria (`working/calculus-2-exit-criteria.md` §Track split) | **CLOSED** 2026-05-29 (reconciliation pass) |
| Kernel-overlap audit (this document) | **CLOSED** 2026-05-29 |
| Safety-axis preprint path ratifiable | **YES** — scoped as standalone formal-methods preprint, *not* as "Calculus 2.0" |
| Preprint scaffold | **PENDING** — title decided (`admissibility-suite-spine-2026-05-28.md`); abstract / claim list / theorem-target table / repo pointer not yet drafted |
| Full "Calculus 2.0" label | **NOT RATIFIABLE** — composition axis (necessity) and self-amendment axis (Frontier 3) remain open |

## Related records

- `working/admissibility-suite-spine-2026-05-28.md` — Fork B topology (preprint
  sibling to paper 28, NOT in Δt Zenodo numbering)
- `working/calculus-2-exit-criteria.md` — six-condition map + 2026-05-29
  track-split reconciliation
- `working/tooltheory/calculus-2-tier-map-2026-05-28.md` — four-tier map
  (tier 2A/2B deferred)
- `working/tooltheory/safety-bridge-rho-drop-decision-2026-05-28.md` —
  actor-inert base bridge decision
- `working/cross-boundary-artifact-specimens.md` — audit-shape precedent
- `LeanProofs/Admissibility/README.md` §Annex — safety-bridge family entries
- `LeanProofs/PAPER-MAP.md` §`LeanProofs/Admissibility/` safety-bridge family
  — module-by-module crosswalk + preprint cashout
- `LeanProofs/FRONTIERS.md` Frontier 1 — load-bearing, structurally addressed
  2026-05-28

## Provenance

Inside-aperture audit run by the operator + Claude Code main thread against
the current state of `~/git/lean/LeanProofs/Admissibility/` and adjacent
working notes. The outside-aperture work (Frontier 1 spike, multi-model
tier-map, ρ-drop decision, exit-criteria reconciliation) was completed
earlier; this document is the inside-aperture counterpart that the
publication-path language explicitly gates on.

No demotions, no reparenting, no module renames. The family earns its
annex slot; the safety-axis preprint is licensed.
