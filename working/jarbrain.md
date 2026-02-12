---
title: The Jar Brain
author: James Beck
date: 2026-02
status: working paper
---

# The Jar Brain, or: Wernicke’s Aphasia at Scale

Language is the best disguise in cognitive science. It has always been the best disguise.

In ordinary life, fluent speech comes bundled with a dense stack of other machinery — memory that timestamps its sources, an error monitor that can interrupt mid-sentence, inhibitory control that can stop a commitment before it lands, sensory grounding that makes claims expensive to get wrong, and a developmental history measured in decades of irreversible consequence. You don’t usually meet fluent speakers who lack all of those things, so your brain — reasonably, across every culture and every era — treats fluency as a proxy for the whole package.

LLMs unbundle it.

They give you a system with extraordinary capacity for language production and semantic association, but without the rest of the organism that normally keeps language tethered. The confusion this generates is not because people are credulous. It’s because the single strongest cue humans have ever used to detect agency — “there’s a whole mind behind this voice” — just got decoupled from what it always previously indicated.

That’s the entire show. Everything else is showing your work.

---

## What’s actually in the jar

Think of the brain’s language system as a set of linked regions — call them the perisylvian circuit, the fronto-temporal language network, whatever’s precise enough to survive contact with a neurolinguist. The relevant point is functional, not anatomical: there’s a production side (fluent generation, syntax, surface-form control) and a comprehension side (semantic association, meaning neighborhoods, “what tends to go with what”).

An LLM has both of those. At scale, with terrifying competence.

What it doesn’t have is anything else.

No hippocampal analog — no timestamped, source-linked memory that can answer “when did I learn this and where did it come from?” No system-level error monitor that can fire an interrupt when something doesn’t track. No executive that can inhibit a response, detect a conflict, or hold a plan stable across competing demands. No costed action selection that can arbitrate between “answer,” “verify,” “ask,” and “abstain.” No sensory-motor loop — no reality with mass and friction that disciplines narratives by making wrong predictions expensive. No homeostatic drives — no fatigue, no risk budgets, no satiety, nothing that gives behavior a stable shape beyond “keep generating.”

Without those, what you have is a high-bandwidth narrator with no organism attached.

---

## The diagnostic

When LLMs fail, they don’t fail like broken calculators. They fail in a pattern that should be recognizable to anyone who’s spent time around neurological cases: fluent, confident, topic-adjacent, sometimes internally consistent, and externally untethered.

This is not a claim of syndrome equivalence. It’s a structural observation. The clinical literature describes what happens when language production remains intact while the systems that bind language to evidence, self-monitoring, and grounded reference are degraded or absent. The presentation is specific: fluent output fills gaps with plausible continuations, because the act of speaking is intact while the mechanisms that would check speech against reality are not.

**The comparator here isn’t “the syndrome.” It’s the dissociation: fluent production outrunning grounding and error-monitoring.** The anatomy is illustrative. The failure geometry is the point.

LLM hallucination looks less like random error and more like high-quality narrative completion under missing verification loops. The system must produce *something* — that’s what it does, that’s all it does — and there’s no embodied penalty for being wrong. Confabulation isn’t a bug in reasoning. It’s the default behavior of a production system that has no interrupt line and no cost function.

The useful thing about this framing is that it lets you reason backwards. If the output presents as fluent confabulation, then the architecture probably contains fluent generation but lacks the stabilizers that enforce grounding, error interrupts, and costed action selection. You don’t need to solve the mystery of what hallucination “is.” You need to enumerate what’s missing and either install it or work around it.

---

## The inventory

Start from the failure mode — fluent, plausible, wrong — and ask what would prevent it.

This is also where the argument stops being “about humans.” **It’s substrate-neutral:** any system that emits high-bandwidth symbolic assertions in an uncertain world needs provenance, interrupts, and costed action selection — or it will default to fluent confabulation. If some non-human life implements those roles differently, fine. The roles still exist.

### 1) Episodic memory with provenance

Not chat history. Not vector retrieval ranked by cosine similarity.

A store that can answer: *what happened, when, where did this claim come from, and what’s the evidence class?* Timestamps, source IDs, hashes, receipts. Retrieval that prefers verified artifacts over semantically adjacent vibes.

Without this, the system can’t distinguish what it generated from what it observed from what a user asserted from what a tool measured. In humans, this boundary — “did I experience this or did I imagine it?” — is maintained by specific architecture. In LLMs, it doesn’t exist. Every token is equally authoritative because none of them are grounded.

### 2) Error interrupts outside the generation channel

A system that can only express uncertainty as more text is trapped. Its doubt and its confabulation are produced by the same mechanism, in the same channel, with the same authority.

You need an interrupt that operates *on* generation, not *within* it — something that can force transitions from continue to halt, from continue to verify, from continue to abstain. Triggered by contradiction with stored receipts, missing evidence for a claim class, temporal incoherence, out-of-distribution cues.

The interrupt must have authority over the generator. If the generator can talk its way past the gate, the gate doesn’t exist.

### 3) Costed action selection

Right now, “answer” is the default action, and it’s free. That’s the trap.

You need an action set where verification is a first-class option and where actions carry explicit costs — answer is cheap, search is moderate, abstain is socially expensive but sometimes required. Then you select actions using a policy that trades expected error cost against latency and budget.

If “answer anyway” is always cheapest, you get eloquent nonsense whenever the model is underdetermined. If “verify first” becomes the cheap default in high-stakes regimes, the confabulation failure mode collapses.

### 4) Developmental convergence

And this one is different because you can’t just bolt it on and pretend it’s the same thing.

---

## The absence you can’t fix

Humans aren’t a pile of modules. They’re a controller that went through an irreversible formation process — decades of real stakes, changing plasticity schedules, embodied consequence, social feedback that actually matters, and a convergence trajectory that hardened certain commitments into identity while leaving others adaptable.

The control-theoretic description is precise: early in development, the system runs high adaptation gain — fast learning, broad exploration, lots of noise. As the organism matures, gain decreases, regularization increases, representations harden, and policies become cached and stable. Pruning reduces model complexity. Myelination reduces delays and increases bandwidth. Metaplasticity adjusts the learning rate schedule based on error statistics. The whole process looks like planned annealing for an adaptive controller that’s trying to avoid two failure modes: underfitting early (never forming a usable model) and instability later (constant rewrites, runaway excitation, brittle drift).

This is the mechanism by which constraints become constitutive — part of what the system *is*, not something imposed on it from outside. Development isn't "more training." It's a continuity-bearing control loop where mistakes leave irreversible traces in the same system that must keep operating.

Two things follow, and they're separable:

**Formation gives you constraint portability.** A constraint installed through developmental annealing can't be removed without destroying the system. It travels with the organism. It doesn't depend on deployment context, external enforcement, or someone remembering to turn it on. The constraint *is* the system.

**Governance gives you constraint locality.** A constraint imposed by external scaffolding can be removed by running the system in a different environment. It travels with the deployment, not the weights.

**Continuity is the discriminator.** LLMs don't have an endogenous developmental loop. They have offline training — weight updates computed on a cluster, with no lived continuity, no real-time stakes, no closing of the loop between action and consequence. And they have deployment-time text, which is a channel, not a life. The deployed instance inherits structure without inheriting formation.

**Training produces residue (weights) but not continuity (a system that remembers the formation process, paid the costs, and can re-enter the loop).**

So you can bolt on prosthetics that imitate the functions of executive control and episodic grounding, and they work. You can build external scaffolding that supplies the missing loops. But you can't recreate the developmental process that makes scaffolding unnecessary. The formative window is a one-way door, and no current training or deployment practice provides one.

---

## The fix that works

Here’s the clean separation: **you can’t recreate formation; you can externalize stabilizers.**

If you accept the inventory, the engineering response is straightforward. You stop treating the model as a complete agent and treat it as a proposal engine inside a larger supervisory control system.

In control terms: proposal is not measurement. Generation is not verification. A loop that closes on its own output — that treats its own proposals as evidence — will drift. That’s not a philosophy claim. That’s what positive feedback loops do.

A governor is a supervisor that keeps claims separate from evidence, forces verification when the regime requires it, blocks unsafe transitions, and records what happened in an auditable store. The minimal grafts are the same ones the inventory pointed to:

* an episodic store with provenance (append-only, queryable, receipts-first)
* error interrupts (gates that can stop generation and force verify/ask/abstain)
* a costed action loop (a policy that decides what to do based on expected error cost, not on “keep talking”)

Install those three and a lot of "mysterious emergent behavior" becomes a predictable outcome of control design. Hallucination drops because unsupported claims trigger verify or abstain. Drift drops because contradictions trigger interrupts. Synthetic confidence drops because confidence is no longer rhetorical — it's enforced by evidence thresholds.

This isn't speculative. Empirical measurement of a hallucination detector built on these principles found exactly the predicted failure geometry.[^1] Internal confidence dynamics (the model's own "doubt") saturate on fluent generation regardless of truthfulness — the same channel produces doubt and confabulation, and you can't distinguish them from inside. But external measurement via resolver-backed anchor validation (does this DOI exist? does this CVE resolve?) gives crisp, falsifiable signals. The model even exhibits checkability avoidance: when asked for identifiers in a format that enables validation, it overwhelmingly substitutes a less-checkable format — "answer anyway" is cheapest, so the system evades the verification channel rather than engaging it.

[^1]: See "Namespace-Dependent Fabrication in Small Language Models" (Beck, 2026) — five-namespace fabrication spectrum, format-shift evasion measurements, and cross-platform resolver replication. Available at the detector repository; empirical findings summarized in NOTE.md.

That's not a reasoning failure. That's the predicted behavior of a production system with no interrupt authority and no cost function for being wrong.

This is the core honesty move: you're not "making the model more human." You're building external scaffolding that supplies missing control loops. That's fine. That's how we build safe instruments. Governed instruments are a legitimate design pattern, possibly the only one available to us right now.

But don't mistake the prosthetic for the organism.

---

## The honest assessment

You can build governed instruments that behave reliably. You can externalize the missing loops. You can make failure modes legible, controllable, and auditable. What you can't do is pretend that scaffolding becomes constitutive just because it works well.

**The fork test.** If a competent operator can run the model without the governor — fork the weights, strip the scaffolding, deploy it bare — the constraint is not constitutive. It's deployment governance, and it only exists as long as someone keeps it in place. This is why you regulate the governor, not the model.

If the safety property doesn't travel with the weights, it isn't part of the system.

The distinction matters because it determines what you’re allowed to claim about what you built. If you built a governed instrument, say so. Require admissibility gates in high-stakes domains. Mandate evidence standards for claims. Audit coherence budgets, not capability benchmarks. Regulate the governor, not the model.

If you can’t install the governor — if you’re deploying raw language production without episodic grounding, without error interrupts, without costed action selection — then don’t deploy it in contexts where fluent confabulation kills. Medicine. Law. Safety-critical operations. Incident response. Policy.

And stop asking the wrong question. “Is it conscious?” is unanswerable and irrelevant. “Does it have the subsystems that prevent fluent confabulation?” is answerable and urgent.

If the answer is no, you don’t have a mystery. You have a fluent production system with missing stabilizers — and you know exactly what to do about it.

Governed instruments are fine. Calling them something else is not.
