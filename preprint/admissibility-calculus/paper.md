---
title: "An Admissibility Calculus: Authorization, Safety Bridges, and Value Decay"
author: "James Beck"
affiliation: "Independent Researcher"
date: "[TBD — first arXiv submission date]"
abstract: |
  We present a small Lean 4 admissibility kernel that separates two kinds of
  evidence a transition system can carry: authorization that a step may be
  taken, and a bridge witness that the step preserves an externally-defined
  defended value. The kernel exhibits, as a constructive countermodel, an
  authorized step that strictly decreases defended value; supplies an
  actor-inert bridge primitive whose preserves-obligation must be discharged
  at construction; and lifts the single-step result to state-threaded
  inductive trajectory families. The main contribution is the trajectory
  triple — positive composition, negative composition, and a no-lift
  theorem — together with a forgetful map between the two families that
  turns "an authorized trajectory that does not lift to a bridged one" into
  a typed function rather than a slogan. The pattern is instantiated over
  two distinct witnesses: a Boolean receipt-poison miniature and a
  Nat-valued two-actor attestation ledger. The kernel is type-checked
  under Lean 4 with no `sorry` and no axiom additions beyond the
  parameterizing structures. The institutional reading of the kernel — that
  systems exhibit authorization laundering when unchecked assertion is
  structurally cheaper than verified assertion — is the subject of a
  separate interpretive paper that cites this one.
keywords: [admissibility, authorization, safety bridge, value preservation, Lean 4, formal methods, trajectory triple, no-lift theorem, actor-inert bridge, attestation ledger]
---

> **Scaffold status (2026-05-29).** This file is a section-level scaffold: title page, abstract, claim list, theorem-target table, section headers, and per-section direction notes. Body prose is not yet drafted. Source-of-truth pointers are stable; theorem names are verified against the Lean source as of 2026-05-29.

---

## Claim list (irreducible)

The preprint stakes the following claims. Each is a Lean theorem against the safety-bridge family modules. Together they form the contribution; no claim is decorative.

1. **Single-step wound (StepAllowed layer).** There exist `s, a, p` such that `StepAllowed s a p` holds and the defended value strictly decreases across the step.
   *(Module: `AuthorizedNotSafe.lean`. Theorem: `authorized_not_safe`.)*

2. **Wound is witnessed-consistent.** The same wound holds in a concrete parallel miniature where the underlying state distinctions are themselves constructive, ruling out vacuity.
   *(Module: `AuthorizedNotSafeWitness.lean`. Theorem: `authorized_not_safe_witnessed`; joint witness: `scenario_joint_witness`.)*

3. **Verdict-layer wound transfer.** The wound transfers from the `StepAllowed` superset to the full `Execution.AuthorizedStep` (mutation standing plus kernel-legible all-green claim verdict by construction).
   *(Modules: `AuthorizedStepNotSafe.lean`, `AuthorizedStepNotSafeWitness.lean`. Theorems: `authorized_step_not_safe`, `authorizedStep_admits_unsafe_witness`, `authorizedStepC_not_safe`.)*

4. **Actor-inert safety bridge primitive.** A `SafetyEnv (σ α ρ : Type)` carries an actor-inert `bridge : σ → α → Prop` field and a `preserves` proof obligation; the generic `bridge_implies_safe` theorem projects safety through `preserves` without consuming `Allowed`.
   *(Module: `SafetyBridge.lean`. Definitions: `SafetyEnv`, `SafeStep`. Theorem: `bridge_implies_safe`.)*

5. **Bridge dischargeability.** The `preserves` obligation is dischargeable structurally, by a candidate bridge that inspects step constructors rather than re-running the action.
   *(Module: `SafetyBridgeWitness.lean`. Specimen: receipt non-contamination bridge.)*

6. **Trajectory triple (positive / negative / no-lift).**
   - *Positive composition:* a bridged trajectory does not decrease the defended-value floor, end to end.
     *(Theorem: `bridgedTraj_preserves`.)*
   - *Negative composition:* an authorized trajectory exists in which the end-state defended value is strictly below the start.
     *(Theorem: `authorized_trajectory_loses_value`.)*
   - *No lift:* the value-losing endpoint admits no bridged trajectory.
     *(Theorem: `no_bridgedTraj_to_poison_end`.)*

   *(Module: `SafetyTrajectory.lean`. Together with the forgetful map `BridgedTraj.toAuthorizedTraj`, this triple is the irreducible theorem family the preprint exists to publish.)*

7. **Forgetful map between trajectory families.** A typed function `BridgedTraj.toAuthorizedTraj : BridgedTraj env … → AuthorizedTraj …` makes "an authorized trajectory that does not lift to a bridged one" a definition over inductive families, not rhetoric.
   *(Module: `SafetyTrajectory.lean`. Definition: `BridgedTraj.toAuthorizedTraj`.)*

8. **Second concrete witness (ρ-drop confirmation).** The abstract `SafetyEnv` instantiates over a textured `Nat`-valued, two-actor protocol with asymmetric powers (writer / auditor). Authorization reads the actor; bridge ignores it. The wound is an *actor-authorized* revoke.
   *(Module: `AttestationLedger.lean`. Models, theorems, and a multi-actor trajectory example.)*

## Theorem-target table

| Claim | Lean module | Lean identifier | Theorem shape |
|---|---|---|---|
| 1 | `AuthorizedNotSafe.lean` | `authorized_not_safe` | `∃ s a p, StepAllowed s a p ∧ value (run s a) < value s` |
| 2 | `AuthorizedNotSafeWitness.lean` | `authorized_not_safe_witnessed`, `scenario_joint_witness` | Same shape, with constructive underlying distinctions |
| 3a | `AuthorizedStepNotSafe.lean` | `authorized_step_not_safe`, `authorizedStep_admits_unsafe_witness` | `∃ as : AuthorizedStep …, value (run s as.step) < value s` |
| 3b | `AuthorizedStepNotSafeWitness.lean` | `authorizedStepC_not_safe`, `no_safeAuthorizedStepC_for_poison`, `bridge_separates_authorized_steps_at_verdict_layer` | Same shape, against canonical `AuthorizedStepC` |
| 4 | `SafetyBridge.lean` | `bridge_implies_safe`, `safeStep_is_safe`, `bridge_two_step_preserves` | `∀ (e : SafetyEnv …) (s a), SafeStep e s a → value s ≤ value (run s a)` |
| 5 | `SafetyBridgeWitness.lean` | `nonContamination_preserves`, `bridge_separates_authorized_steps`, `no_safeStep_for_poison` | Discharges `preserves` for the non-contamination candidate |
| 6.+ | `SafetyTrajectory.lean` | `bridgedTraj_preserves` | `BridgedTraj e s as → value s ≤ value e (last as)` |
| 6.− | `SafetyTrajectory.lean` | `authorized_trajectory_loses_value` (with `poisonTraj_loses_value` as concrete witness) | `∃ s as, AuthorizedTraj … s as ∧ value (last as) < value s` |
| 6.0 | `SafetyTrajectory.lean` | `no_bridgedTraj_to_poison_end` | `¬ ∃ as, BridgedTraj … cleanState as ∧ last as = poisonState` |
| 7 | `SafetyTrajectory.lean` | `BridgedTraj.toAuthorizedTraj` | `BridgedTraj e s as → AuthorizedTraj … s as` |
| 8 | `AttestationLedger.lean` | `ledgerEnv` (the `SafetyEnv` instance); `revoke_loses_value`, `revoke_not_bridged`, `no_safeStep_for_revoke`, `bridge_separates_steps` (single-step); `ledgerBridgedTraj_preserves`, `authorized_trajectory_loses_value` (trajectory, namespaced), `no_bridgedTraj_to_revoke_end`, `protocolHappyPath_preserves` (trajectory) | `SafetyEnv` instantiation + brick-1/2 results over Nat-textured two-actor model |

Identifier verification status (2026-05-29): names checked against the Lean source manually; `tools/formalization_crosswalk.py` automation pass deferred until the abstract section names stabilize.

---

## 1. Introduction

*Scaffold direction.* Open with the gap: what `Allowed` says and what it does not say. Cite the Lean kernel's existing `Execution.AuthorizedStep` as the bundled-construction object the safety-bridge family extends. Name the negative result (authorized step can strictly decrease defended value) early — within the first page — to signal the paper is a kernel + theorem family, not a survey.

Position the contribution against three nearby formal-methods registers, briefly:

- *Refinement / simulation* (Abadi-Lamport, Lynch): we are *not* doing simulation refinement; the forgetful map between `BridgedTraj` and `AuthorizedTraj` is a witness-degradation function, not a refinement relation.
- *Information flow / noninterference* (Goguen-Meseguer; subsequent work): defended value is observable-by-construction; we are not classifying state by security level but by value floor.
- *Resource semantics / separation logic*: closer kin in spirit (resources change at transitions, obligations gate transitions), but our bridge is value-preservation discipline, not resource accounting.

The thesis goes here in two sentences: a system that does not separate authorization from value-preservation evidence admits authorized trajectories whose endpoints have lower defended value than their starts, and the gap is composable rather than one-shot. Declaration is cheap; demonstration must be witnessed.

Sign-post the institutional fence early: this preprint proves the conditional. The interpretive sibling (paper 28) discharges the antecedent.

## 2. Formal apparatus

*Scaffold direction.* Define the parameterizing structures with minimal Lean detail in-text; defer module-level code to an appendix. The abstract layer needs five definitions clearly in the body:

- `SafetyEnv (σ α ρ : Type)` — value codomain `Nat`, value function, bridge predicate, preserves obligation, run.
- `SafeStep e s a` — bundled object of `Allowed e s a` and `bridge e s a`.
- `bridge_implies_safe` — projection through `preserves`.
- `AuthorizedTraj` and `BridgedTraj` — state-threaded inductive trajectory families with per-hop witnesses.
- `BridgedTraj.toAuthorizedTraj` — forgetful map.

State the actor-inertness decision in this section, not in a footnote. The ρ-drop is load-bearing for the abstract layer's portability across witnesses; readers should encounter it before they see the two witnesses, so the asymmetry between authorization (actor-aware) and bridge (actor-inert) is the operative shape they carry forward.

State the v0 simplifications honestly:

- Value codomain is `Nat`; `Preorder V` generalization is mechanical and deferred.
- Preservation is a floor (`≤`); strengthening to conservation (`=`) is a doctrinal choice a stricter env may make.
- Sequence composition beyond two steps lives in `SafetyTrajectory` via inductive lifting; not as a list-and-quantifier construction.

## 3. The irreducible theorem family

*Scaffold direction.* This is the longest section. Each theorem gets:

1. The shape it has in Lean (typeset, not raw Lean source).
2. Why the formulation is the honest one — i.e. what looser formulation would be a lie. Value monotonicity honesty (per-hop strict decrease would be false in the Bool model) is the canonical example; surface it here.
3. The proof idea in two paragraphs maximum (positive: floor composition via `Nat.le_trans` per hop; negative: explicit poison trajectory; no-lift: contradiction via positive).

End the section with the forgetful map and the Loop-Capture mapping reading, fenced as a *doctrinal mapping, not a Lean claim* — the same fence the Lean source carries verbatim. Be careful here: the institutional reading is paper 28's contribution. This preprint can name the mapping as a doctrinal frame the no-lift theorem makes available; it must not argue that real institutions exhibit it.

## 4. Two witnesses

*Scaffold direction.* Receipt-poison miniature first (one short subsection). Attestation ledger second (longer subsection). For each:

- Model — state, actions, value function.
- Bridge — what the candidate bridge inspects and what it admits.
- Wound — the authorized step that loses value.
- Verification — what the brick-0 / brick-1 / brick-2 results look like in the model.

The attestation ledger is the load-bearing witness for ρ-drop confirmation; spend the most space here. Surface:

- Per-hop actor in the trajectory type is the response to brick 2's trajectory-global-actor limitation.
- The wound is *authorized* — auditor legitimately holds revoke power; the value-destroying step is fully actor-authorized.
- Bridge stays actor-inert; the asymmetry between authorization (reads actor) and bridge (ignores actor) is what makes ρ-drop non-vacuous on this model.

## 5. Scope and non-claims

*Scaffold direction.* This section earns its weight by being specific about what the kernel does not prove. Six bullets, each with one example:

1. Not a complete safety policy — the structural bridges are conservative and reject some value-preserving actions.
2. Not a claim about institutional legitimacy — all-green verdicts use degenerate `fun _ _ => …` derivation environments; substantively-grounded legitimacy is paper 28's argument.
3. Not a process calculus — no parallel composition, no monitors, no bisimulation, no trace equivalence, no rates. Sequence composition only, via inductive trajectories.
4. Not refinement — the forgetful map is witness-degradation, not implementation refinement.
5. Not Calculus 2.0 (the full label) — only the safety axis is met; the composition axis (`MergeAdmissible` necessity, ≥3 bad-merge cases) and the self-amendment axis (Frontier 3) remain open per the exit-criteria reconciliation. This preprint is the safety-axis publication path, scoped narrowly.
6. Not certification — the kernel does not certify any institution, system, or implementation. Specimens are kernels, not contents.

The institutional fence is a feature, not an apology.

## 6. Related work

*Scaffold direction.* Brief, formal-methods-register. Four clusters:

- Authority / capability discipline (object capabilities; Miller; Levy's authority logic; Lampson).
- Refinement and simulation (Abadi-Lamport; Lynch; Liskov substitution as a degenerate special case).
- Information flow under transition (Goguen-Meseguer; Sabelfeld-Myers survey; subsequent work on declassification — closest in spirit to bridge dischargeability).
- Resource and obligation semantics (separation logic; Hoare-CSP; obligation logics).

For each cluster: where the kernel reuses the surrounding discipline (e.g., bundled-construction is Capability-style; structural bridges are declassification-flavored), and where it diverges (e.g., we do not classify state by level; we floor a single externally-defined observable).

Δt-series cross-references (P22, P25, P27) are background context, not load-bearing dependencies. Mention briefly; do not over-cite.

## 7. Discussion

*Scaffold direction.* Three short paragraphs:

- *Type-level cost asymmetry.* Authorization-by-declaration is `= rfl`; preservation-by-witness is a `preserves` discharge. The asymmetry is structural, not contingent.
- *Composability of the negative result.* The no-lift theorem is what distinguishes a trajectory-level admissibility failure from a single-step accident. Without it, the negative result is reparable by retrofit-bridging.
- *Doctrinal handoff.* The institutional reading — that systems with this cost asymmetry exhibit authorization laundering — is the subject of the interpretive sibling paper. Pointing at that paper is honest division of labor; collapsing the two would compromise both.

## 8. Conclusion

*Scaffold direction.* One paragraph. Restate the kernel's separation, the irreducible theorem family, the two-witness confirmation, and the institutional fence. End on the type-level cost asymmetry as the publishable observation.

## Appendix A. Module map

*Scaffold direction.* One-page table mapping section claims to Lean files and identifiers, mirroring the theorem-target table above. The body keeps Lean notation light; this appendix is for the reader who wants to chase a theorem to source.

## Appendix B. Build and reproducibility

*Scaffold direction.* Two paragraphs.

- The Lean repository at `~/git/lean` (public: <https://github.com/unpingable/lean>) builds under `elan` + Lean 4 with `lake build`. As of 2026-05-29 the safety-bridge family is part of the green build with no `sorry` and no axiom additions beyond the parameterizing structures.
- Identifier-drift between this preprint and the Lean source is checked by `tools/formalization_crosswalk.py` in the papers repository.

## References

*Scaffold direction.* Bibliography is venue-dependent; defer formatting until target venue is locked. Anchor citations:

- Δt P22 (*No Universal Plant Clock*) — background motivation, not load-bearing.
- Δt P25 (*Epistemic Border Control*) — closest doctrinal sibling for the forgetful map shape.
- Δt P27 (*Obligation-Unsound Reconciliation*) — obligation-accounting layer downstream of this kernel's verdict gate.
- Paper 28 (*The Lie Is Cheaper Than the Proof*) — interpretive sibling, cited as forthcoming.
- Standard formal-methods literature per §6 clusters.
