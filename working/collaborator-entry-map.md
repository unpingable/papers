# Collaborator Entry Map

**Status:** working seed for the eventual unpingable front page. Not the front page itself.
**Audience:** capable, technically literate readers approaching this corpus from outside the operator's private vocabulary. People who could review specs, test adapters, critique formalizations, supply prior art, or use fixture corpora — not "users" in the product sense, and not casual readers.
**Purpose:** make the corpus enterable without requiring the operator personally as docent.

---

## Start Here

This is a research-and-software corpus about **admissibility**: the question of whether a claim, witness, evaluation, or attestation has standing to authorize a consequence. It runs across formal models (Lean), software kernels (Wicket / agent-governor / NQ), published preprints (the Δt framework series), essays, and working notes.

If you've never seen this work before, the shortest possible orientation:

> **Monitoring asks what happened. Admissibility asks whether what happened may be used.**

Most institutional and technical systems collapse those two questions together. The work here keeps them apart.

The corpus is large and visibly heterogeneous — papers, kernels, working notes, Lean modules, gaps, Substack archives. It is **not** a junk drawer; it is several artifacts of one investigation, recorded in different registers. This page is the map.

---

## What This Work Is About

The core question, stated carefully:

> **May this claim be used to authorize this consequence?**

Underneath that are several related sub-questions the corpus has names for:

- *Standing* — does the claim have the position to bind?
- *Basis* — what evidence does it rest on?
- *Scope* — what is it qualified to authorize?
- *Precedence* — which claim wins under conflict?
- *Witness invariance* — is the witness actually independent of what it claims to be independent of?
- *Receipt* — what is the immutable record of the verdict, including refusals and gaps?

The work argues — across papers, kernels, and formal proofs — that conflating these is the central failure mode of agentic and operational systems: governance gets smuggled in under engineering vocabulary, evidence gets laundered into authorization, and aggregate testimony gets treated as corroborated when its components share a contamination basis.

The frame is **not** AI safety in the policy sense, **not** observability tooling, **not** compliance automation, **not** formal-methods hobbyism, and **not** an agent runtime. It overlaps with all of those and replaces none of them. See [where-admissibility-fits.md](where-admissibility-fits.md) for the explicit applicability map.

---

## Current Research Threads

The live work clusters into four threads:

- **Δt framework series (P22–P27).** Foundational failure geometry; epistemic border control; obligation-unsound reconciliation. The published preprints (P01–P24) live at the Zenodo concept DOI; P25/P26/P27 are scaffolds in motion.
- **Admissibility family.** Six non-collapsible boundaries between signal and action, with a candidate seventh. Both a theoretical structure and a target for Lean formalization.
- **Witness invariance.** When can dirty witnesses compose into clean aggregate testimony? Single-witness form (encapsulation under declared excluded perturbations) and multi-witness composition (two-route discipline: corroborative vs aggregate-invariance).
- **Controller continuity.** Non-self-identical controller; ops as hybrid control; handoff/escalation/hidden-compensation/fatigue as failure families.

If you're interested in a specific thread, the [primitives field notebook](primitives/README.md) is the densest entry point — each primitive note explains a recurrent shape, its formal scope, and its connection to the rest of the corpus.

---

## Software Kernels

Three sibling implementations, each at a different layer:

- **Wicket** — admissibility kernel. Small, deterministic, spec-led. Rules on whether a requested operation has sufficient basis, precedence, and standing to proceed. Verdict space is mean and underfed: *authorized / denied / gap / unaccounted*. Lives in a separate repo.
- **agent-governor** — deployment substrate around Wicket. Daemon, JSON-RPC, receipt format, elaborator that turns dirty real-world claims into structured admissibility queries.
- **NQ** — witness-standing broker. Asks *can this witness actually testify about the thing the consumer wants to know?* Distinct from monitoring; sits beside it. Currently has Prom adapter discipline; eval and supply-chain adapters are candidates.

These are not all in the same repo; not all are public. Pointers exist in the candidate-shapes inventory.

---

## Formal Work

Lean repository at `~/git/lean/LeanProofs/Admissibility/` (separate repo). Currently holds five sibling modules — Authority, StateTransition, Derivation, Execution, Corrective — plus a WitnessInvariance module with three layered forms (relational, typed perturbation-relation, regime-bounded). `lake build` green; no `sorry`.

The proof gate is intentionally narrow. Per repo doctrine:

> **The Lean repo proves; the papers repo publishes.**

CI is proof-gate-only. Documentation backfill happens in the papers repo, not in Lean.

---

## Writing / Essays

Three publication surfaces, each with a different register:

- **Preprints (Δt framework series).** Twenty-seven preprint directories under `papers/preprint/`; P01–P24 published at Zenodo v1.0. Concept DOIs cluster under the *delta-t-framework* series. These are the formal work.
- **Substack (Neutral Ambassador).** Essays in a more public-facing register; archive at `~/git/neutral.zone/archive`. Naming interventions, Δn case law, and applied analysis.
- **Working notes (this directory).** Field notebook for shapes that aren't yet ready for either the formal or the public surface. Treat anything here as **probe**, not doctrine, unless the file explicitly says otherwise.

---

## How to Engage

Norms first; concrete shapes in the next section.

This corpus is **spec-led and boundary-sensitive**. That means three things in practice:

1. **Stable vs experimental is labeled.** Published preprints are stable. A green Lean check establishes proof-check status only; custody headers distinguish public imported modules, annexes, checked Scratch, and other experimental surfaces. Working notes are explicitly probes — many will not survive contact with the next round of explanation. Don't treat working/ or checked Scratch as doctrine.
2. **The kernel stays narrow on purpose.** The discipline of refusal is load-bearing. Proposals to expand Wicket into a policy DSL, generalize the admissibility verdict space, or add orchestration concerns will be declined regardless of how reasonable they sound in isolation.
3. **Doctrine is named, not implicit.** When a piece of work is doctrine (the seven-part admissibility decomposition; the two-route composition discipline; the *adapters may sprawl, kernel must not* invariant), it is named as such. When it is not, it is candidate. Confusing the two is the most expensive mistake an outside contributor can make.

The single overall posture:

> *Use the map to locate judgment. Do not let the map perform judgment.*

---

## Useful Contribution Shapes

Concrete kinds of contribution that *fit* this corpus:

- **Review specs.** SPEC.md (Wicket-side) and the published preprints are the spec layer. Catching tightenings or contradictions is high-leverage.
- **Bring prior art.** This corpus self-references heavily; outside prior art is undersampled. Especially welcome: distributed-systems failure literature, control theory, evidence law, capability-system formalisms, sensor fusion / Kalman-filter discipline.
- **Test fixtures.** Fixture corpora are sovereign — they are how multiple implementations stay in agreement. New fixtures that exercise edge cases (especially structured-refusal cases: gap, unaccounted, openFinding) are direct contributions.
- **Adapter implementations.** WIF-composition vocabulary lifted into a new substrate (CI gate, eval framework, supply-chain attestation, observability stack) is exactly the integration shape the corpus is asking for.
- **Critique formalizations.** Lean modules are open to challenge on whether the formalization actually says what the prose claims. Counterexamples that break a proof are gold.
- **Cite papers.** The Δt framework series is small and academic citation is genuinely useful for finding adjacent work.
- **Implementation audits.** Reading Wicket / NQ / agent-governor for places where the doctrine has drifted from the spec.
- **Counterexamples to keepers.** Every keeper line in the corpus is asking to be falsified. *Self-consistency is not corroboration*; *agreement is not corroboration unless the witnesses fail independently*; *passed aggregate proves the aggregate, does not promote its components*. Counterexamples — clean ones, with declared assumptions — are direct contributions.

---

## What Not To Do

Some contribution shapes will be declined regardless of intent. Stating them up front so contributors don't burn cycles:

- **No platform expansion.** This is not a platform. Proposals to grow the kernel into an orchestration system, an agent runtime, or a general-purpose policy engine will be declined.
- **No policy DSL.** OPA/Rego gravity is real. The kernel's verdict space stays small and structured. Conditionals belong in the elaborator, not the kernel.
- **No "what if this were Kubernetes but moral."** This is a specific failure mode of well-meaning contributors who arrive with a recent platform in heart and want to graft its ergonomics on. The kernel is not a controller; it is an admissibility ruling. The shapes are different.
- **No general AI safety positioning.** The work has things to say about LLM ensembles, eval competence, and agentic authorization, but it is not a contribution to AI safety policy in the framework sense and should not be reframed as one.
- **No compliance-platform retrofit.** Adapters to specific frameworks (SOC2, HIPAA, FedRAMP) are welcome; the kernel encoding any specific compliance framework is not.
- **No MCP server transport coupling.** An MCP shim may exist; the kernel turning into a transport-coupled service is the wrong shape.
- **No premature productization of the deployment shapes.** Several adapter shapes (WASM, LSP, conformance suite as standard) are named as candidates in the [candidate-shapes inventory](where-admissibility-fits-candidates.md). They are not yet earned. Proposals to ship them before the conformance story stabilizes will be declined.

The general shape: **expressiveness lives in the adapters; the kernel stays mean and underfed**. Contributions that respect that asymmetry are tractable; contributions that ignore it are not.

---

## Open Questions

What is genuinely unresolved, listed honestly so contributors know where the seams are:

- **Audit operationalization.** The witness-invariance composition probe requires *audited* failure-surface orthogonality. What does the audit step reduce to in practice? Multiple candidate forms; none is generic.
- **Aggregator contamination ($D_A$).** Named as a hazard but not formally treated. The aggregator-as-witness shape collapses into the kernel form, but audit composition across components and aggregator simultaneously is open.
- **Heterogeneous-target composition.** Witnesses on overlapping but distinct targets need a declared target-alignment map. Whether the composition lemmas extend cleanly through such a map is open.
- **Conformance-suite framing.** The kernel is small enough to support multiple implementations, but the standards-body conformance discipline (SPEC + fixtures + multiple conforming implementations) is not yet established.
- **Δm as predicted seventh boundary.** The admissibility family currently has six non-collapsible boundaries. A candidate seventh is named but not formalized.
- **The audit's own Standing.** The audit step requires the auditor to be without stake in the verdict. That's a Standing claim, and Standing has its own load-bearing role in the corpus. The recursive structure (audit-of-aggregate requires Standing, which may require its own audit) is noted but not unpacked.

If you're looking for a contribution shape and one of these matches your background, that's likely the highest-leverage place to engage.

---

## Pointers

- **Application map (companion):** [where-admissibility-fits.md](where-admissibility-fits.md)
- **Primitives field notebook:** [primitives/README.md](primitives/README.md)
- **Witness invariance (single-witness):** [primitives/witness-invariance-failure.md](primitives/witness-invariance-failure.md)
- **Witness invariance composition:** [primitives/witness-invariance-composition.md](primitives/witness-invariance-composition.md)
- **Published preprints:** `papers/preprint/01-*` through `papers/preprint/24-*` (P25/P26/P27 are scaffolds)
- **Lean repository:** `~/git/lean/LeanProofs/Admissibility/` (separate repo, proof-gate CI only)
- **Substack archive:** `~/git/neutral.zone/archive`

---

## Status

This document is itself a working note, not the front page. It is the seed of what the unpingable front page will eventually compress to. Until then it lives in `working/` alongside the other research material it maps over, with the same epistemic status: probe, not doctrine.

If you are reading this and the unpingable front page exists in a polished form, prefer that. If not, this is the closest thing.
