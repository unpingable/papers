---
title: "Safety-Bridge Kernel: Authorization and Value Preservation"
subtitle: "Axis 1 of the Admissibility Suite"
author: "James Beck"
affiliation: "Independent Researcher"
date: "[TBD — release-candidate date]"
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
  parameterizing structures. The formal contribution is a minimal
  mechanized separation result rather than a complex proof artifact:
  authorization evidence and preservation evidence inhabit different path
  families, and the weaker family admits value-losing trajectories. The
  institutional interpretation of this cost asymmetry is left to a
  separate companion paper.
keywords: [admissibility, authorization, safety bridge, value preservation, Lean 4, formal methods, trajectory triple, no-lift theorem, actor-inert bridge, attestation ledger]
---

> **Scope: Axis 1 of the admissibility suite.** The admissibility work is a set of small axis kernels, not a unified calculus. Axis 1 (this note) covers safety / value preservation. Axis 2 (composition / merge admissibility) and Axis 3 (self-amendment / frontier mutation) remain open as separate kernel notes. A 2026-06-03 cross-axis synthesis pass closed *against* a single unifying calculus paper: what survives is the **disciplined premise production** umbrella with two named species (source/temporal — this axis; multiplicity/resource — ContractionHinge sibling) plus a per-species architecture-gap audit, not a unifying formal system. See `working/admissibility-suite-map.md` for the suite plan and `working/source-basis-discipline-synthesis.md` for the synthesis closure.
>
> The contribution of *this* note is bounded by the axis: authorization evidence and value-preservation evidence are distinct, the trajectory triple makes the gap visible at sequence level, and the characterization theorems (collapse iff, gap obstruction, maximal-bridge corner case) name the boundary. The note does not claim a unified calculus, and the rest of the admissibility work does not claim one either.

---

## Claim list (irreducible)

The preprint stakes the following claims. Each is a Lean theorem against the safety-bridge family modules. Together they form the contribution; no claim is decorative.

1. **Single-step wound (StepAllowed layer).** There exist `s, a, p` such that `StepAllowed s a p` holds and the defended value strictly decreases across the step.
   *(Module: `AuthorizedNotSafe.lean`. Theorem: `authorized_not_safe`.)*

2. **Wound is witnessed-consistent.** The same wound holds in a concrete parallel miniature where the underlying state distinctions are themselves constructive, ruling out vacuity.
   *(Module: `AuthorizedNotSafeWitness.lean`. Theorem: `authorized_not_safe_witnessed`; joint witness: `scenario_joint_witness`.)*

3. **Verdict-layer wound transfer.** The wound transfers from the `StepAllowed` superset to the full `Execution.AuthorizedStep` (mutation standing plus kernel-legible all-green claim verdict by construction).
   *(Modules: `AuthorizedStepNotSafe.lean`, `AuthorizedStepNotSafeWitness.lean`. Theorems: `authorized_step_not_safe`, `authorizedStep_admits_unsafe_witness`, `authorizedStepC_not_safe`.)*

4. **Actor-inert safety bridge primitive with per-hop-actor substrate.** A `SafetyEnv (σ α ρ : Type)` carries an actor-inert `bridge : σ → α → Prop` field and a `preserves` proof obligation. The substrate per-hop types `AuthStep E st` and `SafeStep E st` carry actor as a *field*, not a type parameter, so trajectories are multi-actor by default; single-actor is a property over the substrate, not a primitive constraint. The generic `bridge_implies_safe` theorem projects safety through `preserves` without consuming `Allowed`.
   *(Module: `SafetyBridge.lean`. Definitions: `SafetyEnv`, `AuthStep`, `SafeStep`. Theorem: `bridge_implies_safe`.)*

5. **Bridge dischargeability.** The `preserves` obligation is dischargeable structurally, by a candidate bridge that inspects step constructors rather than re-running the action.
   *(Module: `SafetyBridgeWitness.lean`. Specimen: receipt non-contamination bridge.)*

6. **Trajectory triple (positive / negative / no-lift).** The *generic* substrate carries the per-hop-actor inductive trajectory families `AuthorizedTraj E` and `BridgedTraj E` over any `SafetyEnv`, plus the generic positive theorem `bridgedTraj_preserves`. The *verdict-layer specialization* carries `AuthorizedTrajC` and `BridgedTrajC` (richer hops, holding the actual `AuthorizedStepC` rather than the existential-erased `SafeStep authEnv`) and proves the triple over the concrete receipt-poison miniature.
   - *Positive composition (generic + verdict-layer):* a bridged trajectory does not decrease the defended-value floor, end to end.
     *(Theorems: `bridgedTraj_preserves` in `SafetyBridge.lean`; `bridgedTrajC_preserves` in `SafetyTrajectory.lean`.)*
   - *Negative composition:* an authorized trajectory exists in which the end-state defended value is strictly below the start.
     *(Theorem: `authorized_trajectory_loses_value` in `SafetyTrajectory.lean`.)*
   - *No lift:* the value-losing endpoint admits no bridged trajectory.
     *(Theorem: `no_bridgedTrajC_to_poison_end` in `SafetyTrajectory.lean`.)*

   *(Together with the forgetful map below, this triple is the irreducible theorem family the preprint exists to publish.)*

7. **Forgetful map between trajectory families.** Typed functions `BridgedTraj.toAuthorizedTraj : BridgedTraj E s s' → AuthorizedTraj E s s'` (generic, in `SafetyBridge.lean`) and `BridgedTrajC.toAuthorizedTrajC` (verdict-layer specialization, in `SafetyTrajectory.lean`) make "an authorized trajectory that does not lift to a bridged one" a definition over inductive families, not rhetoric.

   *Scope of "forgetful map" in this preprint.* The forgetful map here has the narrow formal meaning above: it erases the bridge witness at each hop while preserving the trajectory's step-by-step structure (same state-thread, same per-hop actor and action). It is **not** the broader `AttestedTrajectory → SafetyPath` projection sketched in working notes (Phase 2–7 of `working/tooltheory/trajectory-canonicalization-2026-05-30.md`), which would additionally erase hop custody, witness standing, freshness, scope justifications, and non-contamination evidence. That architecture is name-early candidate, not part of this preprint.

8. **Second concrete witness (ρ-drop confirmation; multi-actor acid test).** The abstract `SafetyEnv` instantiates over a textured `Nat`-valued, two-actor protocol with asymmetric powers (writer / auditor). Authorization reads the actor; bridge ignores it. The wound is an *actor-authorized* revoke. The model consumes the generic per-hop-actor trajectory inductives directly (no bespoke `Ledger*Traj` types): `protocolHappyPath` (writer.post → auditor.attest) is a single `BridgedTraj ledgerEnv` carrying two different per-hop actors, which is the acid test for the per-hop-actor substrate.
   *(Module: `AttestationLedger.lean`. Models, theorems, and a multi-actor trajectory example.)*

## Theorem-target table

| Claim | Lean module | Lean identifier | Theorem shape |
|---|---|---|---|
| 1 | `AuthorizedNotSafe.lean` | `authorized_not_safe` | `∃ s a p, StepAllowed s a p ∧ value (run s a) < value s` |
| 2 | `AuthorizedNotSafeWitness.lean` | `authorized_not_safe_witnessed`, `scenario_joint_witness` | Same shape, with constructive underlying distinctions |
| 3a | `AuthorizedStepNotSafe.lean` | `authorized_step_not_safe`, `authorizedStep_admits_unsafe_witness` | `∃ as : AuthorizedStep …, value (run s as.step) < value s` |
| 3b | `AuthorizedStepNotSafeWitness.lean` | `authorizedStepC_not_safe`, `no_safeAuthorizedStepC_for_poison`, `bridge_separates_authorized_steps_at_verdict_layer` | Same shape, against canonical `AuthorizedStepC` |
| 4 | `SafetyBridge.lean` | `AuthStep`, `SafeStep`, `bridge_implies_safe`, `safeStep_is_safe`, `bridge_two_step_preserves` | `SafeStep e s` is `{ actor : ρ, act : α, allowed, bridged }`; `∀ (e) (s) (x : SafeStep e s), value s ≤ value (run s x.act)` |
| 5 | `SafetyBridgeWitness.lean` | `nonContamination_preserves`, `bridge_separates_authorized_steps`, `no_safeStep_for_poison` | Discharges `preserves` for the non-contamination candidate |
| 6.+ (generic) | `SafetyBridge.lean` | `AuthorizedTraj`, `BridgedTraj`, `BridgedTraj.toAuthorizedTraj`, `bridgedTraj_preserves` | `BridgedTraj E s s' → E.value s ≤ E.value s'`, generic over `SafetyEnv` |
| 6.+ (verdict) | `SafetyTrajectory.lean` | `bridgedTrajC_preserves` | `BridgedTrajC s s' → defendedValue s ≤ defendedValue s'` over the verdict-layer specialization |
| 6.− | `SafetyTrajectory.lean` | `authorized_trajectory_loses_value` (with `poisonTraj_loses_value` as concrete witness) | `∃ s' (_ : AuthorizedTrajC cleanState s'), defendedValue s' < defendedValue cleanState` |
| 6.0 | `SafetyTrajectory.lean` | `no_bridgedTrajC_to_poison_end` | `¬ Nonempty (BridgedTrajC cleanState (applyStep cleanState poisonAuthorizedStep.step))` |
| 7 | `SafetyBridge.lean`, `SafetyTrajectory.lean` | `BridgedTraj.toAuthorizedTraj` (generic), `BridgedTrajC.toAuthorizedTrajC` (verdict) | Forgetful map at both layers |
| 8 | `AttestationLedger.lean` | `ledgerEnv` (the `SafetyEnv` instance); `revoke_loses_value`, `revoke_not_bridged`, `no_safeStep_for_revoke`, `bridge_separates_steps` (single-step); the trajectory work consumes the generic substrate: `revokeTraj`, `protocolHappyPath` (multi-actor, single trajectory), `protocolHappyPath_preserves`, `authorized_trajectory_loses_value` (namespaced), `no_bridgedTraj_to_revoke_end` | `SafetyEnv` instantiation + brick-1/2 results over Nat-textured two-actor model; no bespoke trajectory types |

Identifier verification status (2026-05-30): names refreshed against the Lean source after the trajectory canonicalization pass. `tools/formalization_crosswalk.py` automation pass deferred until the body prose stabilizes.

---

## 1. Introduction

Systems frequently treat operational permission as a proxy for structural integrity. This conflation masks a structural vulnerability. In formal transition systems, authorization constraints specify which transitions an actor has the standing to initiate, an approach often encapsulated in bundled-construction objects like `Execution.AuthorizedStep`. But authorization says nothing about whether a transition preserves an externally defined metric of systemic value.

This preprint demonstrates the consequences of that gap using a small Lean 4 admissibility kernel. The primary finding is immediate: an action can be fully authorized by a system's operational rules while strictly reducing its defended value. In the kernel specimens, authorization evidence can be constructed without carrying a preservation witness. Proving that an action preserves value requires a distinct structural witness — a safety bridge.

We position this work against three adjacent registers in formal methods:

- **Refinement and Simulation:** Unlike classical simulation frameworks (e.g., Abadi-Lamport, Lynch), the forgetful map defined here between path families is an explicit witness-degradation function, not a proof of behavioral compliance or implementation refinement.
- **Information Flow and Noninterference:** This kernel differs from multi-level security paradigms (e.g., Goguen-Meseguer); we do not partition or classify the state space into security lattices, but floor a single, globally visible observable value.
- **Resource Semantics:** While sharing a conceptual lineage with separation logics where obligations gate transitions, the safety bridge enforces an invariant floor rather than accounting for consumable or partitionable resources.

The thesis of this preprint is structural: when authorization evidence is not separated from value-preservation evidence, the authorized trajectory family may contain paths whose endpoints fall outside the bridged trajectory family. This paper proves that conditional claim inside a small Lean 4 kernel. It does not argue that any specific institution or deployed system instantiates the antecedent. That interpretive argument belongs to the sibling paper, *The Lie Is Cheaper Than the Proof*.

## 2. Formal apparatus

The kernel separates three things that are often collapsed in informal accounts of admissibility: a transition, an authorization for taking that transition, and an independent bridge witness that the transition preserves a defended value. The separation is small enough to state directly. A system supplies a state type `σ`, an action type `α`, and an actor type `ρ`. It also supplies a transition function, a defended-value observable, an authorization predicate, and a bridge predicate. Authorization answers whether an actor may take an action from a state. The bridge answers a different question: whether the action is structurally admissible with respect to the defended value.

The parameterizing object is `SafetyEnv (σ α ρ : Type)`. In the present kernel, defended value is Nat-valued. The environment carries:

- a transition function `run : σ → α → σ`;
- a value function `value : σ → Nat`;
- an authorization predicate over state, actor, and action;
- an actor-inert bridge predicate `bridge : σ → α → Prop`;
- and a preservation obligation proving that bridged actions do not lower the defended-value floor.

The important asymmetry is that authorization may inspect the actor, while the bridge does not. This is intentional. The actor decides whether the transition is permitted; the bridge decides whether the transition preserves the defended observable. If actor identity must change the transition semantics, the appropriate generalization is to make the transition function actor-sensitive. Smuggling actor identity into the bridge would collapse the distinction this kernel exists to preserve.

An authorized step is represented by `AuthStep E s`. It packages an actor, an action, and a proof that the actor is authorized to take that action from state `s`. Actor is a field of the step, not a parameter of the trajectory. This makes multi-actor trajectories first-class. A single-actor path is therefore not the primitive case; it is a property one may prove of a path.

A bridged step is represented by `SafeStep E s`. It extends the authorized-step shape with a bridge witness for the same state and action. In other words, a `SafeStep` does not replace authorization with safety. It carries both: authorization for taking the transition, and a separate witness that the transition satisfies the bridge predicate. The theorem `bridge_implies_safe` then projects the preservation result: given a `SafeStep E s`, the defended value at `s` is less than or equal to the defended value after applying the step.

This is the first cost asymmetry in the kernel. Authorization can be cheap to construct in a permissive or degenerate environment. Preservation is not obtained from authorization. It must be carried by the bridge witness and discharged through the environment's preservation obligation.

The single-step apparatus lifts to trajectories by state-threaded inductive families. `AuthorizedTraj E s s'` represents a finite path from `s` to `s'` whose hops are authorized. `BridgedTraj E s s'` represents the corresponding stronger path whose hops are both authorized and bridged. The trajectory itself binds no global actor. Each hop carries its own actor field, so a path may move through different authorized actors without changing the trajectory type.

This design choice is load-bearing. It prevents the formal layer from treating "one actor controls the whole path" as a hidden default. In the attestation-ledger witness, a writer post followed by an auditor attestation type-checks as one bridged trajectory over the same generic substrate. That example is not an ornament; it is the acid test that actor is correctly placed at the hop level.

The relationship between the two trajectory families is given by a forgetful map. `BridgedTraj.toAuthorizedTraj` erases the bridge witness at each hop while preserving the state thread, actor, and action structure. It does not reinterpret the trajectory. It does not prove refinement. It simply states that every bridged trajectory is, by witness erasure, also an authorized trajectory.

The kernel therefore has three layers:

1. authorized steps, which witness permission to act;
2. bridged steps, which witness permission plus defended-value preservation;
3. trajectories, which compose those witnesses across state transitions.

The v0 kernel deliberately keeps several dimensions narrow. Defended value is Nat-valued rather than abstracted over an arbitrary preorder. Preservation is a floor condition, not equality. Sequence composition is represented by inductive trajectories rather than by list encodings or trace predicates. These choices are restrictions, but they are not evasions. They keep the first result focused on the separation between authorization and value-preservation evidence.

## 3. The irreducible theorem family

The formal contribution is not a single counterexample. A single authorized-but-unsafe step would show only that authorization and value preservation can diverge locally. The kernel's main result is stronger: the divergence composes across trajectories, and a value-losing authorized trajectory cannot be retrofitted into a bridged one.

The theorem family has four moving parts:

1. a single-step wound;
2. a positive composition theorem for bridged trajectories;
3. a negative composition theorem for authorized trajectories;
4. a no-lift theorem connecting the two through the forgetful map.

Together these state the central result: authorization alone does not preserve defended value, bridged authorization does, and the gap between the two is visible at the trajectory level.

### 3.1 Single-step wound

The first result establishes that authorization is not safety. At the `StepAllowed` layer, there exist a state, an action, and a proof of authorization such that running the action strictly decreases defended value.

The theorem shape is:

`∃ s a p, StepAllowed s a p ∧ value (run s a) < value s`

This is the minimal wound. It does not rely on a long trajectory, a hidden scheduler, or a complicated adversarial environment. The authorized step itself lowers the defended observable.

The point of this theorem is not that every authorization predicate permits value loss. The point is that authorization, as a type of evidence, does not by itself contain a preservation witness. A system may define an authorization relation that happens to imply preservation, but that implication is then an additional property of the system. It is not supplied by authorization as such.

The witness-consistency theorem repeats the wound in a concrete miniature. This rules out a vacuity objection: the negative result is not merely an artifact of an underspecified abstract predicate. The underlying distinctions can be constructed, and the authorized decrease remains.

### 3.2 Verdict-layer wound transfer

The next step transfers the wound from the broad `StepAllowed` layer to the fuller verdict layer. The kernel already has an `AuthorizedStep`-style object that bundles mutation standing with a kernel-legible all-green claim verdict. The safety-bridge family extends that object rather than replacing it.

The verdict-layer theorem says that even this richer authorized-step object can carry a value-losing transition. The important phrase is "kernel-legible." The object is all-green with respect to the verdict machinery it inhabits. That does not make the step value-preserving. A green verdict over authorization evidence is still not a bridge witness.

This is where the scope fence first matters. The theorem does not claim that the verdict is substantively legitimate in any institutional sense. It claims that, inside the kernel, the authorized object can be constructed while the defended value decreases. That is enough for the formal result. The institutional interpretation belongs elsewhere.

### 3.3 Bridge dischargeability

The bridge primitive is not merely a negation of the wound. It is a separate structural witness. In the receipt-poison miniature, the candidate bridge inspects the step shape and rules out contamination. The preservation proof is then discharged from that structural condition.

This matters because an unstructured bridge would be cheap theater. A maximal bridge that simply restates preservation would prove little: it would make the bridge predicate a disguised copy of the theorem conclusion. The useful bridge is conservative and inspectable. It may reject some value-preserving actions, but every admitted action carries a reason preservation follows.

The theorem `bridge_implies_safe` captures the general projection. Given an environment whose bridge predicate has a preservation obligation, every `SafeStep` preserves the defended-value floor. The proof does not consume authorization as preservation. Authorization remains permission to act; the bridge supplies the preservation evidence.

### 3.4 Positive composition

The positive trajectory theorem lifts single-step bridge preservation to finite paths. If every hop in a trajectory is bridged, then defended value at the endpoint is at least the defended value at the start.

The generic theorem shape is:

`BridgedTraj E s s' → E.value s ≤ E.value s'`

At the proof level, the result is intentionally unsurprising: preservation composes by transitivity of `≤`. That simplicity is a virtue. The theorem says that once preservation is carried hop-by-hop, the trajectory-level result does not require a second global magic trick.

The honest formulation is floor preservation, not strict increase and not equality. In the Boolean receipt-poison model, a safe hop may preserve the value without increasing it. Requiring strict increase would be false. Requiring equality would overstate the intended discipline. The kernel proves the floor because the floor is the invariant the bridge promises.

### 3.5 Negative composition

The negative trajectory theorem gives the authorized counterpart. There exists an authorized trajectory whose endpoint has strictly lower defended value than its start.

The shape is:

`∃ s' (_ : AuthorizedTrajC cleanState s'), defendedValue s' < defendedValue cleanState`

This is not merely the single-step wound with more notation around it. It places the wound inside the trajectory family, so the failure is expressed in the same compositional language as the positive theorem. That is what makes the comparison sharp. There is a family of authorized paths and a family of bridged paths; the negative result inhabits the former but not the latter.

The concrete witness is the poison trajectory. Its role is not to simulate a realistic institution. It is to force the type distinction to become visible. The authorized trajectory exists. Its endpoint loses value. Therefore authorization alone cannot be the trajectory invariant.

### 3.6 No lift

The no-lift theorem is the hinge. It states that the value-losing authorized endpoint admits no bridged trajectory from the same start.

The theorem shape is:

`¬ Nonempty (BridgedTrajC cleanState poisonEnd)`

The proof idea is by contradiction. Suppose a bridged trajectory to the poisoned endpoint existed. Positive composition would imply that defended value at the endpoint is at least the defended value at the clean start. But the explicit authorized trajectory establishes that the endpoint has lower defended value. The two facts cannot both hold.

This is the result that blocks retroactive bridge certification. Without no-lift, the negative theorem would show only that one authorized path lost value. A later bridge witness might still be invented to bless the same endpoint. The no-lift theorem blocks that move for the modeled endpoint: if the endpoint is value-losing, then there is no bridged trajectory to it.

That is the trajectory-level contribution. The system does not merely distinguish good and bad individual steps. It distinguishes two path families and proves that the weaker family contains paths the stronger family cannot recover.

### 3.7 Forgetful map and witness degradation

The forgetful map gives the comparison its formal direction. A bridged trajectory can always be viewed as an authorized trajectory by erasing the bridge witnesses. The reverse is not available in general.

This is witness degradation, not refinement. A `BridgedTraj` is not an implementation of an `AuthorizedTraj`; it is a stronger witness over the same state-threaded path shape. The forgetful map preserves the path skeleton while discarding the evidence that made the path safe with respect to defended value.

The no-lift theorem then says there are authorized trajectories outside the image of this forgetful map. That is the clean formal statement behind the slogan. Some authorized histories cannot be made bridged histories by later relabeling.

### 3.8 Doctrinal mapping fence

The theorem family makes available an institutional reading: a system may preserve authorization continuity while defended value decays, and the resulting history may not be recoverable by retroactive bridge claims. The doctrinal frame for this reading is laundering-shaped — the sibling paper develops it under the heading *authorization laundering*. This paper does not argue that any real institution has that shape. It proves the conditional kernel.

The interpretive sibling paper takes up the antecedent. This preprint stays at the formal boundary: authorization can compose without preserving value; bridged authorization preserves value; and the value-losing authorized trajectory does not lift.

## 4. Two witnesses

To confirm that the abstract environment is non-vacuous and not an artifact of an underspecified predicate, the kernel is instantiated over two concrete models.

### 4.1 The receipt-poison miniature

This is a low-dimensional Boolean model designed to verify baseline consistency. The state tracks operational objects alongside a Boolean `poisoned` flag. The defended value function maps a clean state to 1 and a poisoned state to 0. The candidate bridge performs a direct non-contamination check by inspecting the step constructor rather than evaluating the post-transition state, structurally rejecting any operation carrying the poison vector. Authorization is purposefully permissive, granting any receipt holder the standing to execute a step. Consequently, an authorized step can inject the poison vector, dropping the defended value from 1 to 0 while returning a kernel-legible, all-green authorization verdict.

### 4.2 The Nat-valued attestation ledger

The second witness serves as the multi-actor acid test, moving beyond the Boolean miniature to a textured, Nat-valued state space. The system models a ledger state acted on by two actors with asymmetric powers: a writer and an auditor. The defended value is a Nat-valued observable over that modeled state. The safety bridge is strictly actor-inert: it ignores the actor field and evaluates only whether the transition mechanics preserve the value floor. Authorization, by contrast, reads the actor field to determine whether the step is permitted.

The wound is delivered via an authorized `revoke` action. The auditor possesses the legitimate authority to execute a revocation, making the step fully actor-authorized within the system's permission model. However, executing the revoke drops the ledger's defended value. Because the bridge is actor-inert, it rejects the step despite the auditor's administrative standing, proving that authorization and safety diverge even under permitted administrative action.

Crucially, this model consumes the generic per-hop-actor trajectory substrate directly, without inventing bespoke ledger trajectory types. We demonstrate this via `protocolHappyPath`, a single trajectory where the first hop is executed by the writer (creating a post) and the second hop is executed by the auditor (attesting to it). This confirms that multi-actor execution paths type-check natively on the substrate, validating the design choice to place the actor field at the individual hop level rather than binding a single actor globally to the path type.

## 5. Scope and non-claims

To prevent misinterpretation by reviewers or downstream implementers, we explicitly define what this kernel does not warrant:

- **Not a complete safety policy.** Structural bridges are conservative by design. They enforce a strict floor and will actively reject valid, value-preserving actions if those actions lack structural evidence of preservation.
- **Not a claim of institutional legitimacy.** The "all-green" verdicts generated within this kernel are machine-legible artifacts computed under a degenerate `fun _ _ => ...` derivation environment. They do not certify, imply, or substitute for substantive, ground-level legitimacy within an actual institution.
- **Not a process calculus.** This framework provides sequence composition only, modeled via state-threaded inductive trajectory families. It contains no primitives for parallel composition, process monitors, bisimulation, trace equivalence, or operational rates.
- **Not refinement.** The forgetful map is strictly a tool for witness degradation, demonstrating that a bridged trajectory can be mapped to an authorized trajectory by discarding its safety evidence. It does not prove that an implementation satisfies an abstract specification.
- **Not a unified calculus.** This preprint covers only the safety axis of the broader admissibility problem. The composition axis (requiring `MergeAdmissible` necessity proofs and bad-merge counterexample families) and the self-amendment axis remain entirely open as separate kernels. Post-2026-06-03 synthesis closure (see `working/source-basis-discipline-synthesis.md`), no unifying calculus is the target object across these axes — surviving structure is the "disciplined premise production" umbrella over separate species, not a single rename.
- **Not real-world certification.** The kernel type-checks proofs over abstract specimens and miniatures. It does not certify any specific real-world system, financial ledger, deployment configuration, or software implementation as safe.

The institutional fence is a feature, not an apology.

## 6. Related work

We position the safety-bridge architecture within four established formal-methods registers:

- **Authority and capability discipline.** Our approach builds on bundled-construction styles found in object capability systems (e.g., Miller's *Object Capabilities and Subjective Aggregation*, Lampson, Levy's authority logics), where operational mutation standing and claim verdicts are packaged together. We diverge by refusing to partition or classify the state space by capability level; the bridge is instead a value-preservation discipline over a single externally defined observable.
- **Refinement and simulation.** In contrast to classical simulation frameworks (e.g., Abadi-Lamport's *Composing Specifications*, Lynch's I/O-automata framework), our forgetful map is not a behavioral refinement relation. It operates as a witness-degradation function between inductive families that share an identical step-by-step structure, rather than an implementation-to-specification mapping over infinite behaviors.
- **Information flow under transition.** The closest conceptual kin is the declassification literature extending Goguen-Meseguer (1982) and surveyed by Sabelfeld-Myers and Sabelfeld-Sands. Bridge dischargeability behaves similarly to structural declassification filters. However, we enforce a floor under a single external observable rather than classifying states into security lattices. The bridge does not "declassify" data; it blocks the mutation unless value preservation is independently verifiable.
- **Resource and obligation semantics.** Our framework shares structural patterns with separation logic (O'Hearn, Reynolds, Yang) and obligation logics, where obligations flow through state transitions. We diverge because the safety bridge does not function as a resource-accounting predicate; the defended value is a globally visible observable rather than a consumable or partitionable asset.

Δt-series cross-references (P22, P25, P27) appear in this preprint as background context only, not as load-bearing dependencies.

## 7. Discussion

The kernel yields three observations.

First, it exposes a type-level cost asymmetry. In the specimens developed here, authorization evidence can be constructed without carrying any proof that the defended value is preserved. Preservation requires a separate bridge witness and a `preserves` discharge. The distinction is structural: permission to perform a transition is not evidence that the transition preserves the defended observable.

Second, the negative result is trajectory-level, not merely local. The positive theorem shows that bridged trajectories preserve the defended-value floor. The negative theorem gives an authorized trajectory whose endpoint loses value. The no-lift theorem connects the two: the value-losing endpoint cannot be reached by a bridged trajectory in the modeled system. This is what prevents the result from collapsing into a one-step counterexample.

Third, the separation creates a clean handoff to the interpretive sibling paper. This preprint proves the formal conditional: if a system has this authorization/bridge shape, authorized paths can diverge from value-preserving paths. The empirical and institutional claim that real systems instantiate the antecedent is outside this paper's proof boundary.

## 8. Conclusion

The Lean 4 kernel isolates authorization permission from structural value-preservation evidence. Through an irreducible theorem family and two distinct witnesses, we demonstrate that authorized steps can decrease a system's defended value, that such decreases can be represented at trajectory level, and that value-losing endpoints cannot be retroactively lifted into bridged paths. The publishable observation remains the type-level cost asymmetry: authorization is an assertion; preservation requires a witness.

## Appendix A. Module map

The following table maps the claims argued in this paper directly to their corresponding formal modules and theorem identifiers within the canonical Lean 4 source repository.

| Claim | Lean module | Lean identifier | Theorem shape / description |
| --- | --- | --- | --- |
| **1** | `AuthorizedNotSafe.lean` | `authorized_not_safe` | `∃ s a p, StepAllowed s a p ∧ value (run s a) < value s` |
| **2** | `AuthorizedNotSafeWitness.lean` | `authorized_not_safe_witnessed`, `scenario_joint_witness` | Same shape, instantiated over concrete, non-vacuous state distinctions. |
| **3a** | `AuthorizedStepNotSafe.lean` | `authorized_step_not_safe`, `authorizedStep_admits_unsafe_witness` | `∃ as : AuthorizedStep …, value (run s as.step) < value s` |
| **3b** | `AuthorizedStepNotSafeWitness.lean` | `authorizedStepC_not_safe`, `no_safeAuthorizedStepC_for_poison`, `bridge_separates_authorized_steps_at_verdict_layer` | Verdict-layer wound transfer mapping to the canonical `AuthorizedStepC` gate. |
| **4** | `SafetyBridge.lean` | `AuthStep`, `SafeStep`, `bridge_implies_safe`, `safeStep_is_safe`, `bridge_two_step_preserves` | Projects safety through the `preserves` obligation without consuming authorization. |
| **5** | `SafetyBridgeWitness.lean` | `nonContamination_preserves`, `bridge_separates_authorized_steps`, `no_safeStep_for_poison` | Discharges the `preserves` obligation for the non-contamination candidate bridge. |
| **6 (generic)** | `SafetyBridge.lean` | `AuthorizedTraj`, `BridgedTraj`, `BridgedTraj.toAuthorizedTraj`, `bridgedTraj_preserves` | Generic trajectory composition and preservation proofs over an arbitrary `SafetyEnv`. |
| **6 (verdict)** | `SafetyTrajectory.lean` | `bridgedTrajC_preserves` | Specializes positive trajectory composition over the verdict-layer miniature. |
| **6.−** | `SafetyTrajectory.lean` | `authorized_trajectory_loses_value` | Proves the existence of a value-losing authorized trajectory family. |
| **6.0** | `SafetyTrajectory.lean` | `no_bridgedTrajC_to_poison_end` | The no-lift theorem: `¬ Nonempty (BridgedTrajC cleanState poisonEnd)`. |
| **7 (generic)** | `SafetyBridge.lean` | `BridgedTraj.toAuthorizedTraj` | Witness-degradation forgetful map at the substrate layer. |
| **7 (verdict)** | `SafetyTrajectory.lean` | `BridgedTrajC.toAuthorizedTrajC` | Witness-degradation forgetful map at the verdict-layer specialization. |
| **8** | `AttestationLedger.lean` | `ledgerEnv`, `revoke_loses_value`, `revoke_not_bridged`, `protocolHappyPath` | Instantiates the multi-actor, Nat-valued acid test directly over the generic substrate. |

## Appendix B. Build and reproducibility

The canonical formal source is the Lean repository at `~/git/lean`, with public mirror at `https://github.com/unpingable/lean`. The safety-bridge family is part of the repository build and is checked with Lake:

```bash
lake build
```

As of the 2026-05-30 source-verification pass, the cited safety-bridge modules build with no `sorry` placeholders and no additional axioms beyond the parameterizing structures used by the kernel.

Identifier drift between this exposition and the Lean source should be audited before release candidates using `tools/formalization_crosswalk.py` in the papers repository. The 2026-05-30 report-only drift check verified all 36 cited identifiers at their claimed module locations.

## References

*Scaffold direction.* Bibliography is venue-dependent; defer formatting until target venue is locked. Anchor citations:

- Δt P22 (*No Universal Plant Clock*) — background motivation, not load-bearing.
- Δt P25 (*Epistemic Border Control*) — closest doctrinal sibling for the forgetful map shape.
- Δt P27 (*Obligation-Unsound Reconciliation*) — obligation-accounting layer downstream of this kernel's verdict gate.
- Paper 28 (*The Lie Is Cheaper Than the Proof*) — interpretive sibling, cited as forthcoming.
- Standard formal-methods literature per §6 clusters.
