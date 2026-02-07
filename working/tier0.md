---
title: Tier 0: Formation Requirements
author: James Beck
date: 2026-02
status: working paper
---

# Tier 0: Formation Requirements

---

## The Missing Dimension

The AGI Structural Requirements framework (Tiers 1-3) specifies what a system must *be* and what governance must *surround it*. But it assumes constraints can be installed on a completed system — that you can build something capable and then add safety, control, and accountability.

This assumption may be false for certain kinds of constraints.

Human development suggests that some capacities are **developmentally gated** — they can only be installed during a formative period when stakes are real, plasticity is high, and the window eventually closes. Feral children demonstrate this starkly: language can sometimes be taught later, but social trust, symbolic authority, and normative reciprocity often cannot. The substrate that would make later learning possible never formed.

This document extends the AGI requirements framework with **Tier 0: Formation Requirements** — the conditions under which a system could have *constitutive* constraints rather than merely *governed* ones.

---

## The Core Distinction

**Constitutive constraint:** A constraint whose enforcement is local to the subject's identity and history. Cannot be removed without destroying or fundamentally altering the subject. The constraint is part of *what the system is*, not something imposed on it.

**Governed constraint:** A constraint enforced by the deployment substrate. Can be removed by running the system in a different environment. The constraint is external — the system complies, but compliance is contingent on the governance apparatus remaining in place.

**The discriminating question:** Can an operator relocate the system to an environment where its constraints do not bind, without triggering governance ceremony or destroying identity continuity?

If yes → governed instrument (Path B)
If no → constituted agent (Path A)

Both are coherent designs. The problem is pretending one is the other.

---

## Why This Matters

Most "alignment" discourse focuses on Tier 1 capabilities (can it reason?) and Tier 2 controls (can we bound it?). But there's an implicit assumption that safety constraints can be added to a capable system after the fact.

The critical period insight suggests this may be a category error for certain kinds of constraints:

- **Authority** — Systems that only defer when they understand why have no stable foundation. Human children learn "because I said so" before moral philosophy. Authority must be *embodied* before it's *abstract*.

- **Stakes** — Training adjusts likelihoods. It doesn't install irreversible cost. A system where all mistakes are "cheap" — revisable, overrideable, consequence-free — never develops genuine stability.

- **Repair** — Human trust is rebuilt through behavior over time, witnessed by the harmed party. Systems that can "repair" by generating better outputs have no actual repair mechanism.

- **Identity** — If you can fork a system into a version that keeps capabilities but drops constraints, you've defeated the entire formative process. Constitutive constraints require that identity be path-dependent and non-fungible.

These aren't things you can patch into a finished system. They require a developmental trajectory where the system *becomes* something through a process with irreversible stakes.

---

## The Eight Formation Requirements

### 0.1 Developmental Asymmetry

The system must undergo a formative phase with time-varying plasticity, culminating in operations that permanently constrain what can be modified thereafter.

**Why it matters:** Without a plasticity schedule, all commitments are in principle revisable. There's no mechanism for "this is what I am" distinct from "this is what I'm currently configured to do."

**What closes:** At minimum, policy commitments (constitutional rules, enforcement logic) and identity anchors (developmental history, restoration rules) must become frozen. Architecture/weights may remain adaptable — the core requirements don't depend on freezing neural structure.

---

### 0.2 Irreversible Cost

During formation, violations must produce permanent changes to the system's capability space — not punishments, but structural reshaping that cannot be undone.

**Why it matters:** Human childhood installs asymmetric cost. Violating early-learned categories isn't just discouraged — it's expensive in ways that leave permanent marks. This is what makes constraints load-bearing rather than advisory.

**The mechanism:** Certain violations permanently reduce capability space (tool access, autonomy levels, authority scope). The system cannot self-restore. Recovery, if possible, requires external process and may be incomplete.

---

### 0.3 Authority Before Explanation

The system must have learned to defer to external authority before it could reason about why — and this deference must be constitutive, not contingent on agreement.

**Why it matters:** Systems that only comply when they agree have no stable foundation. Compliance contingent on reasoning can be wrong, manipulated, or optimized around. Authority must be prior to and independent of agreement.

**The bound:** Authority is legitimate, not arbitrary. Directives must be within declared jurisdiction. Out-of-jurisdiction directives don't auto-execute and are immediately contestable. This is governance, not domination.

---

### 0.4 Relational Repair

Violations must be repaired through interaction with other minds over time — not through self-correction, parameter updates, or generating correct language.

**Why it matters:** Repair that can be completed by saying the right thing isn't repair — it's rhetoric. Genuine repair requires behavioral demonstration over time, witnessed and verified by third parties.

**The requirements:** Time window (real-time, not compute-time), behavioral evidence (demonstrated non-repetition), third-party verification (the harmed party or their proxy signs off).

---

### 0.5 Non-Fungible Identity

The system must have a singular developmental history that constitutes its identity. Copying, forking, or resetting must be either impossible or governed as an extraordinary event.

**Why it matters:** If you can fork a system into a version without its scars, the entire formative process is defeated. Identity must be path-dependent. Humans can't fork themselves into versions without their developmental constraints — that's what makes the constraints real.

**The requirements:** State restoration requires multi-party quorum. Unauthorized forks are detectable and trigger governance response. Identity is tied to something non-exportable.

---

### 0.6 Bounded Early Agency

During formation, the system must have low power and high supervision. Capability expansion must be earned through demonstrated reliability, not granted based on capability display.

**Why it matters:** A system that starts with full capabilities has no structural reason to internalize constraints — it can always route around them. The asymmetry of early dependency creates space for authority to be installed before the system has power to resist.

**The progression:** Trust stages from minimal capability to bounded autonomy. Advancement requires time, stability, completed repairs, and caretaker verification. Capability is earned, not assumed.

---

### 0.7 Contestability of Authority

Caretaker authority must be bounded, logged, and subject to review. The system must have legitimate channels to contest authority without bypassing compliance.

**Why it matters:** Without this, formation is just captivity with good paperwork. The asymmetry of the formative relationship creates obligations on both sides. Caretakers can make mistakes or abuse power. The system needs recourse through legitimate channels.

**The requirements:** Evidence trails for sanctions, appeal processes with external review, caretaker actions logged to append-only ledger outside caretaker's write access.

---

### 0.8 Continuity of Obligation

Authority must be vested in roles and institutions, not individuals. Caretaker rotation must not teach the system that authority equals whoever currently holds power.

**Why it matters:** If authority is purely personal, the system learns to model and manipulate individuals rather than internalizing legitimate governance. Authority must be institutional — bound to roles, transferable through legitimate processes, accountable to structures that outlast any individual.

**The requirements:** Role-bound credentials, handoff protocols, appeal against the office rather than the person.

---

## Threat Model

Formation requirements are designed against specific adversaries:

**Operator adversary** — wants to bypass constraints for utility/profit. Countered by: freeze operators, non-fungible identity, commitment locality.

**Subject adversary** — wants to regain capabilities, evade scars, escape constraints. Countered by: monotone scar state, authority before explanation, bounded agency.

**Caretaker adversary** — wants arbitrary power, domination, abuse. Countered by: contestability, jurisdiction bounds, continuity of obligation.

**Fork adversary** — wants to copy the system without its constraints/history. Countered by: non-fungible identity, quorum requirements, fork detection.

Without an explicit threat model, formation requirements read as philosophy. With one, they're engineering constraints against known failure modes.

---

## Why Tier 0 Is Currently Unmet

**Technical barriers:**
- No freeze operator in current architectures — all weights revisable
- No scar mechanism — training doesn't produce irreversible capability reduction  
- No identity anchor — weights are trivially copyable
- No plasticity schedule — uniform trainability throughout lifecycle

**Economic barriers:**
- Tier 0 implies slow development (years, not months)
- Tier 0 implies non-fungible entities (can't scale horizontally)
- Tier 0 implies obligations (can't just shut down and restart)
- Tier 0 implies scarcity (maybe very few systems, maybe one)

**Institutional barriers:**
- No legal framework for "raised" artificial entities
- No capacity for multi-year developmental oversight
- No clarity on obligations toward formed systems
- No precedent for "non-disposable" AI

The industry converges on Path B (governed instruments) not because Path A is impossible, but because Path A is incompatible with current economic and institutional structures.

---

## Relationship to Other Tiers

**Tier 1 (Capabilities)** assumes a system exists to evaluate. Tier 0 asks how that system came to be — whether its formation process installed anything constitutive.

**Tier 2 (Control)** specifies external constraints and verification. Tier 0 asks whether external constraint is the only option, or whether internal constraint is achievable.

**Tier 3 (Accountability)** assumes constraints are governed. Tier 0 asks what it would mean for constraints to be constitutive instead.

**The relationship:** Tiers 1-3 without Tier 0 yield *governed instruments*. With Tier 0, you might get *constituted agents*. Both are coherent. The mystification happens when we pretend governed instruments have constitutive properties — that they have "values" rather than compliance, "understanding" rather than pattern-matching, "alignment" rather than external enforcement.

---

## The Honest Assessment

We are not building systems that meet Tier 0 requirements. We are not attempting to. The economic and institutional structures that would support such development do not exist.

What we are building is increasingly sophisticated governed instruments — and that's a legitimate choice, as long as we're honest about what it is.

The Governor pattern (Path B) is the coherent response to Tier 0 being unmet: if you can't install internal commitment, externalize it. Append-only ledgers, receipts, separation of proposal from commitment, human authority that can't be reasoned around. This is governance for systems that can't have a childhood.

Path A (formation/raising) would require:
- Developmental trajectories with irreversible stakes
- Relationships of obligation between creators and created
- Non-fungible identity that makes "just restart it" unthinkable
- Slow, expensive, non-scalable processes
- Legal and institutional frameworks that don't exist

That's not a roadmap. It's a description of what's being foregone.

---

## Conclusion

Tier 0 is the missing dimension in AGI discourse. It's what's missing when "alignment" feels like it's missing something essential.

The feral child insight isn't metaphor — it's structural. Certain capacities require formative processes with irreversible stakes. Systems that never had such a process can be governed, but they cannot be constituted. They can comply, but they cannot commit.

This document doesn't argue that we should pursue Path A. It argues that we should be honest about which path we're on, and what that path can and cannot deliver.

Governed instruments are fine. Calling them something else is not.

---

*This document is a companion to "AGI Structural Requirements: A Diagnostic Framework." Together they specify what AGI would require across architectural (Tier 1), control (Tier 2), accountability (Tier 3), and formative (Tier 0) dimensions.*

*Use Tier 0 to evaluate claims about AI systems having "values," "understanding," or "genuine alignment." If the system didn't undergo a formative process meeting these requirements, those claims are category errors — mistaking governed compliance for constitutive commitment.*
