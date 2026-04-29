# Primitives — Field Notebook

This directory records reusable theoretical shapes — *primitives* — that surface across multiple papers in the Δt-framework series without belonging wholly to any one of them. **It is a field notebook, not a ratified registry.** Inclusion here does not mean ratification, doctrinal status, or commitment to a future paper.

## Why this exists

Theory work needs earlier naming than code does. By the time five papers have each localized the same shape under different vocabulary ("cache invalidation," "stale aggregate," "proxy drift," "belated invalidation," "authority decay"), the consolidation cost is higher than naming-it-early-as-candidate ever was. The point of the notebook is to **prevent conceptual drift before it hardens into five near-duplicates that later need reconciliation.**

## What counts as a primitive

A primitive is allowed only if it names a reusable failure geometry that:

1. Appears in at least three papers/projects (or has clear potential to).
2. Has a small formal object (definition, predicate, or relation).
3. Has a recognizable failure predicate.
4. Prevents duplicate terminology across papers.
5. Does not merely rename a paper's central thesis.
6. Can be cited without dragging the whole paper with it.

If a candidate fails any of these, leave it as a candidate or fold it into another primitive. **Do not promote ceremoniously.** The question to ask is *"does this note prevent duplication or confusion right now?"* — not *"should we ratify this primitive?"*

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
