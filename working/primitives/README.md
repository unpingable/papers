# Primitives — Field Notebook

This directory records reusable theoretical shapes that surface across multiple papers in the Δt-framework series without belonging wholly to any one of them. **It is a field notebook, not a ratified registry.** Inclusion here does not mean ratification, doctrinal status, or commitment to a future paper.

> **Use the map to locate judgment. Do not let the map perform judgment.**

Entries here are not all the same kind of object. They may be primitives, candidate primitives, motifs, coordinates, transitions, attractors, or boundary conditions (see *Kinds of objects* below). The purpose of the directory is **diagnostic orientation** — to help identify what kind of failure is being observed, what axes are involved, what role conversions are occurring, where admissibility or authority may break.

It is **not a state-space machine**. The machinery is used to *explain* candidates, not *manufacture* them. *The state space is diagnostic, not generative.*

## Why this exists

Theory work needs earlier naming than code does. By the time five papers have each localized the same shape under different vocabulary ("cache invalidation," "stale aggregate," "proxy drift," "belated invalidation," "authority decay"), the consolidation cost is higher than naming-it-early-as-candidate ever was. The point of the notebook is to **prevent conceptual drift before it hardens into five near-duplicates that later need reconciliation.**

## Kinds of objects

Entries may belong to any of the following kinds, with different metabolic loads. Naming the kind is part of writing the entry:

| Kind | What it names | Example |
|---|---|---|
| **Axis** | A dimension along which failures vary | observability, controllability, authority, time, scope, evidence-role, corpus-role |
| **Transition** | A role/state conversion | detector → generator; receipt → decision; proxy → target; certificate → authority |
| **Attractor** | A recurring basin systems fall into | metric displacement, compliance theater, taxonomy autocatalysis |
| **Boundary condition** | Where a claim stops being valid | stale binding, design-basis erasure, scope bleed |
| **Coordinate / motif / instance** | Local expression — real but not canon-worthy | a specific failure case located on existing axes; lives as a note under the relevant parent rather than minting its own primitive |

The "Active primitive notes" table below predates this distinction. Existing entries are **not retroactively reclassified** — the new ontology gets voting rights forward, not emergency powers over the archive. Future entries should declare their kind.

## What counts as a primitive

A primitive earns canonization only if it satisfies all of the following:

1. Appears in at least three papers/projects (or has clear potential to).
2. Has a small formal object (definition, predicate, or relation).
3. Has a recognizable **failure predicate**.
4. Has a clear **non-case** — a situation that resembles it but isn't.
5. Has a **distinctness test** against neighboring primitives ("Do not confuse with X because…").
6. Has at least two domains where it **changes diagnosis or admissible intervention**.
7. Names an **axis, transition, attractor, or boundary condition** — not merely a coordinate produced by existing machinery.
8. Prevents duplicate terminology across papers.
9. Does not merely rename a paper's central thesis.
10. Can be cited without dragging the whole paper with it.

If a candidate fails the kind test (item 7) — i.e., it is a coordinate, not a generator — keep it as a motif, instance, or note under its parent. Most coordinates do not need names; naming has metabolic consequences.

**Do not promote ceremoniously.** The question to ask is *"does this note prevent duplication or confusion right now?"* — not *"should we ratify this primitive?"*

## Statuses

| Status | Meaning | Promotion requires |
|---|---|---|
| **candidate** | Named shape with failure predicate, examples, and "do not confuse with." | (initial — written when the shape is noticed) |
| **working** | Reused across multiple papers/projects without semantic drift. | Reuse — observed cross-use, not formal stress |
| **ratified** | Formal object survives math / proof sketch / counterexample pressure; becomes normative apparatus vocabulary in `specifications/`. | Formal stress — survives contact with a hostile whiteboard |

> **Working requires reuse. Ratified requires formal stress.**

Promotion is lazy and earned, not voted on:

- **candidate** is language-first — written when the shape is noticed
- **working** is usage-first — earned by being cited across papers without drift
- **ratified** is formal-first — earned by surviving math or counterexample pressure

Don't ratify from vibes. Even very handsome vibes wearing a little theorem hat.

## Active primitive notes

| Primitive | Status | Primary home | Notes |
|---|---|---|---|
| [Stale Binding](stale-binding.md) | candidate | P26 (empty-window theorem; headline exhibit) | Touches P23/P24/P25/P26/P27; corrected from DeepSeek's "unbounded" to base-rate-decay theorem shape |
| [Design-Basis Erasure](design-basis-erasure.md) | candidate | no current paper home (cross-cutting) | Controller transferred without its hazard model; surfaces in P24 Agile case + SRE-as-shock-absorption + Governor→prose leakage. Diagnostic: *if removed in the imported domain, what specific failure would re-emerge?* Self-applies to this field-notebook |
| [Trajectory-Actuator Gap](trajectory-actuator-gap.md) | candidate | no current paper home (likely Latent Capitalism / Chronopolitics; adjacencies to P22/P25/P26) | Observed historical trajectory mistaken for an available control surface. Sibling to Design-Basis Erasure (both "import without preserving load-bearing context"). Diagnostic: *which parts of the historical transition do we actually have standing/access/capacity to affect now?* Naming note: *Causal Standing Gap* rejected on collision with Governor-native *Standing* |
| [Role Accretion](role-accretion.md) | candidate | no current paper home (closest adjacency P19 Shadow Governance) | A system's effective role expands via accumulated context without explicit re-contracting. Mechanism: *continuity → implied obligation → assumed standing → unauthorized intervention.* Diagnostic: *was this action authorized by the original task contract, or by accumulated context?* The disease against which Standing is the discipline |
| [Control-Set Laundering](control-set-laundering.md) | candidate | no current paper home (controllability-side sibling of P25's observability result; Latent Capitalism / civic systems adjacent) | **Kind:** likely coordinate/sub-region on the controllability axis (not a freestanding primitive — flagged for ratification re-check). A governance/policy/budget choice is embedded into the admissible actuator set, then later presented as a hard plant constraint. Three-layer guardrail (benign / sediment / laundered) prevents universal-acid use. Sovereign-asymmetry signature distinguishes from sediment |
| [Finder-Generator Inversion](finder-generator-inversion.md) | candidate | no current paper home — meta-discipline / ontology layer | **Kind:** transition. A detector / recognition system crosses into production when detection increases the supply, salience, or legitimacy of the thing detected. Descends from misplaced-concreteness / map–territory; sibling to Goodhart (attractor) and Scott (legibility). Diagnostic: *if removing the detector would decrease the rate of the phenomenon, not just measurement of it, the inversion has occurred.* This directory is itself an instance |

## Candidates (observed but not yet pulled out)

These are recurring shapes that have been noticed but do not yet have their own files. Listed to prevent duplicate naming, not to commit to writing them up.

- **Projection.** $\alpha:$ system state → controller-visible state, with $\alpha(b_1) = \alpha(b_2)$ collapsing distinct substrate states. Central to P25 and P27. Probably ratification-grade once written up.
- **Binding.** Object/decision/state attached to authority, evidence, causality, or consequence. Load-bearing noun under half the apparatus. Needs its own formal note; risk of being too general to be useful.
- **Horizon.** How long a claim, receipt, obligation, or authorization remains valid. P26/P27/Night Shift. Probably ratification-grade.
- **Receipt.** Durable record that a transition, degradation, discharge, or authorization occurred. P27 + Governor lineage. Probably ratification-grade.
- **Standing.** Who/what is allowed to testify, decide, or act. Governor-native. Probably ratification-grade.
- **Substitution.** System regulates on $V'$ while claiming to regulate on $V$. P25's central animal. Probably ratification-grade once P25 is drafted.
- **Versioned Semantics.** Same bytes, different interpreter (schema migrations, feature flags, model/prompt drift). Strong candidate; not just stale binding — *truth didn't move; the interpreter moved.*
- **External Irreversibility.** System transition is reversible internally, but consequence outside the system is not (payments, emails, moderation actions, public labels). Strong candidate; sleeper primitive.
- **Masked Transition.** Higher-level transition reports recovery while lower-level accusation remains open. P27-specific but reusable beyond Kubernetes. Candidate.
- **Orphaned Causality.** Evidence survives but loses the binding needed to accuse. P27 + observability + forensic readiness. Candidate.
- **Authority Decay.** Authorization technically valid after basis for authority expired (old tokens, stale sessions, cached permissions). May be composite (Standing + Stale Binding); hold as candidate.

## Anti-patterns

- **Promotion ceremonies.** "Should we ratify X?" is a status meeting in disguise. Don't.
- **Soup with bylaws.** A registry with elaborate templates but no actual cross-paper use. The directory exists to *prevent duplication*, not to model governance.
- **Primitive-shaped papers.** A primitive should be citable without dragging a paper with it. If a primitive starts wanting its own §1–§8, it's a paper, not a primitive.
- **Renaming.** Don't import a paper's central thesis as a primitive. P27's *obligation-unsound reconciliation* is not a primitive; *Receipt* and *Masked Transition* might be.
- **Coordinate combinatorics (anti-generator rule).** Do not generate new entries by mechanically combining axes. A proposed primitive must introduce a new generator — a new axis, transition, attractor, or boundary condition. If it is merely a coordinate produced by existing machinery, keep it as a motif or instance under the relevant parent. *The state space is diagnostic, not generative.* Running the ontology to enumerate candidate primitives is the Finder-Generator failure mode wearing a more sophisticated hat.

## Note template

Each primitive note follows the same brutal template:

```
Name:
Status: candidate | working | ratified
Originated:
Formal object:
Failure predicate:
Typical symptoms:
Primary home (paper):
Used by:
Do not confuse with:
Minimal example:
Architectural rules:
Keeper aphorisms:
```

The most important field is **Do not confuse with**. Half the danger is primitives blob-collapsing into each other.
