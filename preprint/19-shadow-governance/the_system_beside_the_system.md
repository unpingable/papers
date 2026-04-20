---
header-includes:
  - \usepackage{booktabs}
  - \let\oldtableofcontents\tableofcontents
  - \renewcommand{\tableofcontents}{\begingroup\raggedright\hyphenpenalty=10000\exhyphenpenalty=10000\oldtableofcontents\endgroup\clearpage}
---

# The System Beside the System:\ Shadow Governance and the Stabilization\ of Unauthorized Authority

**James Beck**
Independent Researcher

**Date:** March 2026

**Series:** Δt Framework, Paper 19

**Status:** Preprint v1.0.1

---

## Abstract

Paper 18 [1] formalized unauthorized durability: the mechanism by which transient, lower-tier state acquires higher-tier governing force without legitimate promotion. The present paper addresses what happens afterward. When unauthorized promotions accumulate, normalize, and become load-bearing, they undergo a phase transition from isolated violations into a parallel governance structure -- *shadow governance* -- that may exercise more influence over system behavior than the formal rules it was never authorized to replace. We define shadow state formally, distinguishing incipient shadow state (unauthorized authority-bearing state exists) from stabilized shadow governance (shadow state is load-bearing and ratchet-active). We identify a three-component stabilization ratchet (utility debt, dependency entrenchment, semantic erasure) that prevents shadow governance from reverting once established, and describe the *Potemkin layer*: the phenomenon in which formal governance persists as a legitimacy shell while shadow rules handle actual control. We propose detection methods, a remediation pipeline that treats correction as a system migration, and two worked examples in LLM agent memory systems and institutional deployment processes. A central claim is that shadow governance is not inherently pathological -- it is *ungoverned*.

**Keywords:** shadow governance, unauthorized durability, normalization of deviance, state promotion, governance divergence, institutional drift, adaptive systems, remediation, AI safety, cybernetics

---

## 1. Introduction

Paper 18 [1] described the breach: how transient signals acquire durable governing force through unauthorized promotion across authority tiers. The write barriers, promotion ceremony, and threat taxonomy developed there assume a particular remediation posture -- that unauthorized promotions are individual events, detectable at the boundary, correctible by enforcement.

This paper describes the settlement.

In practice, unauthorized promotions are often not caught individually. A runtime exception is allowed once. The workaround is faster than the formal path, so it is used again. Other subsystems begin to depend on the exception's output. New operators learn the workaround before they learn the formal process. The formal rule remains in the documentation. Nobody follows it. Nobody remembers it was the rule.

The arc is consistent across substrates:

> transient exception → repeated shortcut → precedent → tacit rule → parallel constitution

Nobody signs anything. Nobody announces a rewrite. The system starts acting as though the workaround was always law.

This is not merely "more capture" in Paper 18's sense. Individual write-barrier violations are bugs. Stabilized shadow governance is a regime. The difference matters because the remediation strategy is completely different. For individual violations, the prescription is straightforward: enforce barriers, deny promotion, emit receipt. For stabilized shadow governance, strict enforcement of formal policy would break the system, because the system has reorganized around the unauthorized state.

We make four contributions. First, we define shadow state formally in Paper 18's terms and introduce the divergence index as a measure of formal-to-shadow governance ratio. Second, we identify the three-component stabilization ratchet that prevents shadow governance from reverting once established. Third, we describe the Potemkin layer -- the phenomenon in which formal governance survives as a legitimacy shell rather than a functioning control system -- and explain why compliance audits against formal policy produce false assurance in this regime. Fourth, we develop a remediation pipeline that treats correction as a system migration event and show why "just enforce the rules" is not a viable strategy once shadow governance has stabilized.

---

## 2. Shadow State

### 2.1 Definition

We adopt the layer model and promotion ceremony from Paper 18 [1]. A system has four authority tiers (L0 runtime, L1 context, L2 durable policy, L3 constitutional) and a five-phase promotion ceremony (proposal, evaluation, attestation, application, audit) governing legitimate transitions between tiers.

At any time *t*, the system's effectively governing state divides into two sets:

- **S_formal(t)**: state that occupies L2 or L3 authority and reached that tier through an attested promotion path -- that is, state for which a valid promotion receipt exists.
- **S_shadow(t)**: state that exercises L2 or L3 authority -- it governs system behavior with the force of durable policy or constitutional constraint -- but has no valid promotion receipt.

We distinguish three conditions:

- **Shadow state present.** S_shadow(t) is nonempty -- some unauthorized authority-bearing state exists. This is common and may be trivial. A single undocumented default does not constitute a governance crisis.
- **Shadow governance stabilized.** Shadow state is load-bearing, has downstream dependents, and at least one component of the stabilization ratchet (Section 3) is active. Remediation is no longer a simple enforcement action.
- **Shadow governance dominant.** S_shadow(t) has more influence on system behavior than S_formal(t) -- the system's actual decisions, defaults, and routing patterns are better predicted by the shadow rules than by the formal rules. The formal layer has become a Potemkin layer (Section 4).

The bulk of this paper concerns stabilized and dominant shadow governance. Incipient shadow state -- isolated unauthorized promotions that have not yet become load-bearing -- is the domain of Paper 18's write barriers and promotion ceremony.

### 2.2 The Divergence Index

The divergence index D(t) measures how much of the system's behavior is explained by formal governance versus shadow governance. It is a semiquantitative diagnostic, not a metric with natural units.

The estimation strategy is consistent across substrates: compare actual system behavior against predictions derived from formal state alone, then attribute residual explanatory power to shadow state. In an LLM agent, candidate estimators include decision prediction accuracy (what fraction of routing decisions are predicted by formal preferences versus accumulated context), override frequency (how often actual behavior diverges from what formal policy would prescribe), and policy-exception reliance (what fraction of operations depend on undocumented defaults). In an organization, candidate estimators include process adherence rate (what fraction of actions follow the documented procedure), exception-path traffic (what fraction uses informal workarounds), and formal-policy prediction error (how well the written policy predicts actual decisions).

Given an influence measure μ(·) over authority-bearing state -- constructed from whichever estimators fit the substrate -- the divergence index is:

```
D(t) = μ(S_shadow(t)) / (μ(S_formal(t)) + μ(S_shadow(t)))
```

D(t) = 0 means the system is fully governed by its formal state. D(t) = 1 means the formal state has no explanatory power -- shadow governance is total. In between, D(t) measures the degree to which the system has bifurcated into formal and shadow governance layers.

The divergence index need not be computed precisely to be useful. Even a rough estimate -- "most of our deploys bypass the formal process" -- constitutes a D(t) measurement. Its value lies in making an implicit condition explicit: many systems operate at D(t) well above 0.5 without anyone having named the divergence.

### 2.3 Relationship to Technical Debt

Shadow governance resembles technical debt but is not identical to it. Technical debt is accumulated implementation shortfall -- code that works but is poorly structured, fragile, or hard to maintain. Shadow governance is accumulated *authority* shortfall -- state that governs but was never authorized to govern. The operational test: does this state merely constrain implementation choices, or does it decide outcomes that actors treat as binding? A poorly structured codebase forces architectural workarounds (technical debt). An undocumented deployment shortcut that everyone follows and new hires are taught as "how we do it" decides outcomes (shadow governance). The difference is that technical debt makes the system harder to change, while shadow governance makes the system *differently governed than it claims to be*. Operators may well know they are following shadow rules -- the knowledge is often widespread and tacit. What makes it shadow governance rather than mere debt is that the authority being exercised has no receipted path, no versioning, and no formal contestability.

---

## 3. The Stabilization Ratchet

### 3.1 Overview

Why does shadow governance stabilize instead of reverting? Paper 18 [1] identified hysteretic lock-in (threat class T7) as the temporal consequence of successful capture: a prior installation persists after the forcing signal weakens because the cost of reversal exceeds available correction budget. The present section identifies the mechanism by which hysteresis operates at the system level.

Three feedback loops collectively prevent shadow governance from reverting. Each loop raises the cost of correction along a different axis. When all three operate simultaneously, the shadow layer becomes the system's de facto constitution.

### 3.2 Utility Debt

The shadow path is faster, cheaper, or more convenient than the formal path. Users, operators, and subsystems migrate to the shadow path because it works better -- it may have emerged precisely *because* the formal path was too slow, too rigid, or too poorly designed. Over time, the majority of system traffic flows through the shadow path.

Correction now means making everyone slower. The cost of reverting is not merely the engineering effort to restore the formal path. It is the accumulated productivity difference between the shadow path and the formal path, multiplied by every user and subsystem that would be affected. This cost is real and politically legible: the shadow path has constituencies.

### 3.3 Dependency Entrenchment

Other subsystems couple to the shadow state. They consume its outputs, assume its behavior, and build their own logic on the assumption that the shadow path exists and works as observed. These downstream dependencies did not choose to depend on shadow governance. They simply used what was available.

Correction now means breaking downstream systems. The blast radius of reverting a shadow path is proportional to the number and criticality of the systems that depend on it. In complex systems, this dependency graph is often poorly understood -- nobody mapped it because nobody acknowledged the shadow path was a path at all.

### 3.4 Semantic Erasure

Institutional memory of the formal rule decays. The people who wrote the formal rule may have left. The documentation may still exist but is no longer read. New operators learn the shadow path first because that is what experienced operators teach them. The formal rule becomes an artifact rather than a live constraint.

Correction now means re-deriving what the rule even was. The original justification, the context in which it was written, and the threat model it was designed to address may all have been lost. Semantic erasure is the most insidious component of the ratchet because it is invisible: the absence of knowledge about the formal rule does not register as a problem because nobody is looking for the formal rule.

### 3.5 The Complete Ratchet

The ratchet is complete when all three loops operate simultaneously: the shadow path is faster (utility debt), other things depend on it (entrenchment), and nobody remembers it was an exception (erasure). At that point, the shadow rule is the de facto constitution.

The ratchet is not binary. A system may have deep utility debt with minimal semantic erasure -- everyone knows they are using the workaround, they simply prefer it. That is shadow state with partial ratchet activation: not yet fully stabilized, potentially easier to remediate. Full ratchet engagement, where all three components reinforce each other, marks the transition from correctable shadow state to a regime requiring migration (Section 7). Whether this transition is sharp or gradual is an empirical question (Section 10.4), but the direction is clear: each additional ratchet component raises the cost of every remediation path.

This is the same hysteresis problem identified in Paper 18, but at system scale rather than individual-state scale. Paper 18's hysteresis depth metric measures how much counter-input is required to reverse a single captured state. The present analysis asks: what happens when the *entire system* occupies a hysteretic basin?

The answer is that remediation is no longer a policy-enforcement event. It is a system migration. Section 7 develops this implication.

---

## 4. The Potemkin Layer

### 4.1 The Phenomenon

Once shadow governance dominates, the formal governance layer does not disappear. It persists. But it persists as a *legitimacy shell* -- the thing you point to when someone asks "how is this governed?" The formal rules provide the branding. The shadow rules provide the actual control.

This is what we call the Potemkin layer: a formal governance structure that looks complete on inspection but exercises minimal actual authority over system behavior.

### 4.2 False Assurance

The Potemkin layer produces a specific and dangerous form of false assurance. Audit against formal policy passes because the formal rules are intact. The system behaves according to shadow rules because those are the rules that are actually load-bearing. The compliance surface and the control surface have diverged.

This means that governance audits scoped to formal policy are worse than uninformative -- they are actively misleading. They certify a system as compliant with rules it does not follow. The certification process itself becomes part of the Potemkin layer, providing legitimacy to a governance structure that exists primarily as documentation.

### 4.3 Inverted Legibility

A further consequence of the Potemkin layer is that the relationship between documentation and reality inverts. In a well-governed system, the formal governance layer is the most legible description of how the system actually operates. In a Potemkin system, the formal governance layer is the *least* accurate description of system behavior. The shadow layer -- undocumented, unversioned, unaudited -- is more accurate. But because the shadow layer was never written down as policy, the most accurate description of system behavior is the one nobody can read.

This inversion makes shadow governance resistant to casual detection. An auditor examining the formal documentation will find policies, procedures, and constraints. They will look complete and reasonable. They are complete and reasonable. They are also not the rules the system follows.

---

## 5. Detection

### 5.1 The Detection Principle

Detection requires a shift in audit strategy. Instead of asking "what rules exist?" and checking whether they are intact, the auditor asks: *where did authority appear without a matching authorized path?*

This is negative-space auditing: looking for the authority that should not be there rather than the authority that should.

### 5.2 Methods

We present four detection methods in order of increasing cost and infrastructure requirements.

**Behavioral divergence analysis.** Instrument the system to record actual decision outcomes over a period. Compare outcomes against the predictions of a model trained on formal policy alone. Systematic deviations identify behavioral territory governed by shadow rather than formal state. This is the most accessible method: it requires only observation and a model of formal policy, not a parallel system or a comprehensive receipting infrastructure.

**Dependency mapping.** Identify all downstream systems, processes, and operators that depend on the shadow path. This does not detect shadow governance directly but measures its entrenchment -- the blast radius of remediation. Dependency mapping is often the step that converts "we should fix this" into "we cannot fix this without a migration plan."

**Provenance exhaustion.** For each observed system behavior, demand the promotion receipt that authorized it. Any behavior that cannot produce a valid receipt is, by definition, governed by shadow state. This method requires a receipting infrastructure complete enough to cover all authority-bearing state. In systems without comprehensive receipting, provenance exhaustion degenerates into a coverage exercise rather than a detection method.

**Clean-room differential.** Compare a fresh instance of the system -- initialized from formal policy with no accumulated state -- against the live system, given identical inputs. Any behavioral difference that is not explained by the formal promotion log is candidate shadow state. This is the most direct and most expensive method, since it requires the ability to instantiate a clean copy of the system.

### 5.3 The Detection Paradox

Detection is easiest when shadow governance is youngest -- when the divergence is small, the dependencies are few, and the institutional memory of the formal rule is still live. But detection effort is typically invested when shadow governance is most visible -- when the divergence is large, the system has clearly bifurcated, and the Potemkin layer is conspicuous. By that point, the ratchet has deepened and remediation is expensive.

This suggests that detection is most valuable as a continuous process rather than a crisis response. Periodic clean-room differentials, routine provenance audits, and standing divergence metrics are the tools of early detection. Waiting until the symptoms are obvious means waiting until the remediation window has already narrowed.

---

## 6. Worked Examples

### 6.1 Agent Memory Drift

**Setup.** An LLM agent operates with a formal policy layer (L2) containing explicitly promoted preferences and a memory system governed by the promotion ceremony from Paper 18. The agent accumulates context (L1) across conversations.

**The drift.** Over hundreds of conversations, the agent develops routing patterns, tool-selection defaults, and decision heuristics that were never formally promoted. The mechanisms are specific: retrieval memory accumulates summarization artifacts that shape future context retrieval; per-user preference carry-forward encodes interaction patterns as implicit routing rules; tool-selection defaults emerge from repeated successful invocations; error-handling heuristics that arose from early failures become standing policy without anyone writing them down. These patterns emerge from context carry-forward -- accumulated L1 state that has not been promoted through the ceremony but has acquired effective L2 force.

This is shadow governance. The formal policy says the agent should route based on explicit preference settings and documented tool-selection rules. The shadow state routes based on accumulated context artifacts. When they conflict, the shadow state wins because it is the more immediate input to behavior. The shadow state is not a matter of tone or style -- it is a matter of which tools get called, which data sources get consulted, and which actions get taken.

**Detection.** A clean-room differential reveals the divergence: a fresh instance of the agent, given identical prompts, produces materially different decisions. The differences are systematic -- the live agent has acquired routing defaults, tool preferences, error-handling patterns, and priority orderings that the clean instance lacks. None of these have promotion receipts.

**The ratchet.** If users have adapted to the live agent's shadow behavior -- expecting its particular style, relying on its routing patterns -- then reverting to formal policy means degrading the user experience. If downstream systems consume the agent's outputs and have calibrated to its shadow behavior, reverting breaks those integrations. If nobody remembers what the formal policy was supposed to produce, reverting means guessing.

**Remediation.** Clearing the agent's memory is not remediation -- it is data destruction that ignores dependency mass. The remediation pipeline (Section 7) requires first classifying which shadow state is adaptive (the agent learned useful things) and which is pathological (the agent drifted into patterns nobody would have authorized), then choosing legitimization, quarantine, or migration accordingly.

### 6.2 Institutional Deployment Drift

**Setup.** An engineering organization has a formal deployment process: code review, staging environment, canary deployment, progressive rollout, and post-deployment monitoring. The process is documented in a runbook, tracked in a deployment tool, and required by policy.

**The drift.** A separate "emergency" path exists for critical fixes: direct push to production with post-hoc review. The emergency path is faster. Over time, the definition of "emergency" expands. Engineers discover that the emergency path is available for non-emergencies if the post-hoc review is filed promptly. Managers tolerate it because production issues get fixed faster. New engineers learn the emergency path first because experienced engineers use it most.

Within a year, the majority of deployments use the emergency path. The formal process still exists in the runbook. Post-hoc reviews are filed but rarely read. The staging environment falls into disrepair because most changes bypass it. The canary infrastructure develops undiagnosed issues because it is infrequently exercised.

**Shadow governance.** The formal deployment policy says: staged, reviewed, canaried. The de facto deployment policy says: push directly, file a review later, skip staging unless someone is watching. The formal policy remains in the runbook. Nobody has updated it. Nobody has revoked it. Its explanatory power over actual deployment behavior is near zero.

D(t) for this organization's deployment process is well above 0.5. The formal policy has near-zero explanatory power over actual deployment behavior.

**The ratchet.** The emergency path is faster (utility debt). The staging environment has decayed because it is unused, making the formal path even slower (entrenchment). New engineers don't know the formal process was ever the real process (erasure). All three components are active.

**The Potemkin layer.** When a compliance audit asks "do you have a deployment process?", the answer is yes. The runbook is produced. The deployment tool shows records. The post-hoc reviews exist. The audit passes. Nothing about the audit reveals that the documented process governs less than 20% of actual deployments.

**Remediation.** "Enforce the runbook" would mean: slow down all deployments, fix the staging environment, retrain engineers, accept the productivity hit, and break the muscle memory of every team. This is not a policy fix. It is a migration. The remediation pipeline must assess whether the emergency path is actually better (in which case the formal policy should be replaced) or whether it has accumulated unacknowledged risk (in which case migration to a revised formal path is necessary).

---

## 7. Remediation

### 7.1 Why Enforcement Fails

The instinct when shadow governance is detected is to enforce the formal rules. This fails for three reasons, each corresponding to a component of the ratchet.

First, utility debt means the shadow path is often faster or better. Enforcing the formal rules imposes real costs on real users. If those costs are high enough, enforcement will be resisted, circumvented, or reversed.

Second, dependency entrenchment means other systems have coupled to the shadow state. Enforcing the formal rules breaks those downstream systems, producing cascading failures that may be worse than the shadow governance they were intended to fix.

Third, semantic erasure means the formal rules may no longer be appropriate. They were written for a context that has changed. Enforcing rules written for a system that no longer exists is not governance. It is ritual.

### 7.2 Remediation as Migration

Remediation of stabilized shadow governance is a system migration, not a policy enforcement event. The migration pipeline:

**Step 1: Detect.** Identify shadow state through clean-room differential, provenance exhaustion, or behavioral divergence analysis (Section 5).

**Step 2: Classify.** Determine whether shadow state is adaptive, pathological, or mixed:

- *Adaptive*: the shadow rules emerged because the formal rules were inadequate. The shadow rules are genuinely better.
- *Pathological*: the shadow rules emerged from convenience, laziness, or adversarial capture. They function but carry unacknowledged risk.
- *Mixed*: some shadow state is adaptive and some is pathological. This is the common case.

Classification is itself a governance act, and a politically charged one. Where the formal layer has already lost operational legitimacy, the formal layer cannot be trusted to adjudicate. Classification may require temporary mixed authority -- external review, cross-functional assessment, or explicit stakeholder negotiation -- precisely because the system's own governance apparatus is part of the problem being diagnosed.

**Step 3: Measure blast radius.** Map dependency mass -- what subsystems, processes, and operators depend on the shadow state. This determines the cost of any correction path.

**Step 4: Choose a path.**

- **Legitimize.** Promote individual shadow states through the promotion ceremony retroactively, piecemeal. Each shadow rule is evaluated, attested, and brought under governance with receipts and versioning. The formal layer is preserved and augmented. Legitimization is not retrospective absolution for the original bypass; it is formal assumption of accountability for a now-recognized authority path. The risk is that legitimization becomes a standing incentive to bypass formal process ("ship the workaround now, ratify later"). The mitigation is that the ceremony must evaluate the shadow state on its merits, not merely acknowledge its existence. Appropriate when: shadow state is partially adaptive and the formal rules are worth preserving as a foundation.
- **Quarantine.** Isolate shadow state, prevent further coupling, but do not remove it yet. Buys time for assessment without incurring the blast radius of removal. Appropriate when: classification is uncertain and dependency mass is high.
- **Migrate.** Build a parallel clean path, deprecate the shadow path, and move dependents over incrementally. Most expensive, most controlled. Appropriate when: shadow state is pathological but deeply entrenched.
- **Replace.** Accept that the shadow rules are better and replace the formal layer wholesale. Unlike piecemeal legitimization, replacement is a constitutional event: the formal rules are retired, the shadow rules are ratified as the new formal layer through a constitutional ceremony, and governance starts fresh from the new baseline. Appropriate when: the formal rules are clearly wrong and the shadow rules have proven themselves in practice.

**Step 5: Execute.** Every path has a cost. The cost increases with dependency mass and semantic erasure depth. Pretending rollback is free is itself a form of shadow governance -- an informal assumption with real authority that nobody has ratified.

### 7.3 The Remediation Paradox

The longer remediation is deferred, the harder it becomes. The ratchet deepens: utility debt grows, dependencies accumulate, institutional memory fades. But premature remediation -- acting before dependency mass is understood -- causes cascading failures.

This suggests remediation has a window: after detection but before full entrenchment. The window shrinks over time. Missing the window means the difference between a policy fix and a full system migration.

A complicating factor: entrenchment and observability can move in opposite directions. As the shadow system becomes more entrenched, its behavior under real-world load becomes better documented -- not formally, but empirically. The optimal intervention point may not coincide with earliest detection, because some entrenchment yields knowledge of actual operating behavior that makes the Replace path more viable. This does not change the overall direction -- every increment of delay raises remediation cost -- but it means the remediation window is shaped by what you learn as well as what you lose.

---

## 8. Metrics

We propose four metrics for tracking shadow governance. Like the metrics in Paper 18, these are defined operationally; concrete implementation will vary by substrate.

**Divergence index D(t).** Fraction of system behavior explained by shadow state versus formal state (Section 2.2). This is the headline metric. Rising D(t) indicates the system is bifurcating.

**Dependency mass.** How many subsystems, processes, and operators would be affected if shadow state were removed or replaced. This measures the blast radius of remediation. High dependency mass does not mean shadow governance is acceptable. It means remediation is expensive.

**Observability gap.** Volume of state transitions invisible to the formal audit log. A system with comprehensive receipting has a small observability gap. A system where most state transitions happen outside the promotion ceremony has a large one. The observability gap measures how much of the system's actual governance is unauditable.

**Remediation cost.** Estimated cost to move from current D(t) to target D(t), accounting for utility debt (productivity impact), dependency mass (blast radius), and semantic erasure (re-derivation effort). This metric is necessarily approximate, but even a rough estimate converts "we should fix this" from a moral claim into an engineering assessment.

---

## 9. Related Work

### 9.1 Normalization of Deviance

Vaughan's analysis of the Challenger disaster [2] is the canonical case study of how organizations gradually accept previously unacceptable conditions as normal. In our framework, this is precisely the stabilization ratchet: temporary overrides of safety criteria became repeated exceptions became tacit policy became the effective constitution of launch decision-making. The formal safety rules remained in the documentation. The shadow rules -- "this level of O-ring erosion is acceptable because we've seen it before" -- governed actual launch decisions.

Vaughan's contribution was to show that normalization of deviance is not a failure of individual judgment but a structural property of organizations under production pressure. The present framework extends this insight beyond organizations: any governed adaptive system with layered state is susceptible to the same ratchet. The mechanism is structural, even when it expresses itself culturally.

### 9.2 Classification and Infrastructure

Bowker and Star [3] documented how classification systems function as infrastructure: invisible when working, visible only on breakdown, and resistant to change because everything is built on top of them. Shadow governance has the same infrastructural quality. It becomes invisible precisely because it is load-bearing. Challenging it means challenging the infrastructure, which means challenging everything that depends on the infrastructure.

Their concept of *torque* -- the tension experienced by individuals caught between classification categories -- maps to the lived experience of operators in systems with high D(t). The operator knows the formal rules. The operator follows the shadow rules. The operator manages the contradiction daily. This is torque.

### 9.3 Organizational and Technical Debt

The concept of technical debt [4] -- accumulated implementation shortcuts that constrain future development -- provides the closest existing analogue in software engineering. Cunningham's original formulation emphasizes that the debt is known and accepted as a tradeoff; the problem is not the shortcut but the failure to eventually pay it down. Shadow governance is a specific and more dangerous variant: the debt is not merely structural but *authoritative*. Technical debt makes the system harder to change. Shadow governance makes the system *differently governed than it claims to be*. The remediation posture is correspondingly different: paying down technical debt is a refactoring exercise; remediating shadow governance is a legitimacy exercise.

### 9.4 Institutional Theory

DiMaggio and Powell [5] identified isomorphic pressures that cause organizations to adopt similar structures regardless of whether those structures are effective. In our terms, isomorphic pressure is a mechanism for shadow governance formation at the inter-organizational level: formal structures adopted for legitimacy (coercive or mimetic isomorphism) may have no relationship to actual governance processes. Meyer and Rowan [6] made the point directly: formal organizational structures often function as myths and ceremonies, loosely coupled to actual operational routines. The Potemkin layer is precisely this loose coupling, formalized as measurable divergence between receipted formal governance and observed shadow governance.

### 9.5 Author's Prior Work

Papers 16 through 19 trace a single pathology from its mechanism to its systemic consequences. Paper 16 [7] identified three regimes -- shear, leverage, and capture -- signed by correlator quality; shadow governance is a system-level consequence of the capture regime stabilizing into a self-reinforcing structure. Paper 17 [8] formalized propaganda as adversarial control over the policy layer governing belief revision -- in this paper's terms, an adversarial method for producing shadow governance over public memory, where the formal epistemic policy persists as a legitimacy shell while the de facto update rules are governed by the shadow layer. Paper 18 [1] formalized the mechanism: unauthorized promotion across authority tiers. The present paper extends the analysis to what accumulates when those promotions are not individually corrected.

### 9.6 Work as Imagined, Work as Done

The safety science literature on resilience engineering [9] draws a persistent distinction between *work as imagined* (formal procedures, documented processes, trained behaviors) and *work as done* (actual operational practice under real-world constraints). Hollnagel's framing is closely aligned with the present analysis: the gap between imagined and done is precisely the divergence index, and the reasons the gap persists -- efficiency pressure, adaptation to local conditions, incomplete procedures -- map to the utility debt component of the stabilization ratchet. The present framework adds formal structure to this observation: receipted promotion paths, measurable divergence, and a remediation pipeline.

---

## 10. Implications and Open Questions

### 10.1 Shadow Governance Is Not Pathological. It Is Ungoverned.

Shadow governance is dangerous because it is unratified, unaudited, and hard to contest -- not because informal adaptation is inherently bad. The formal rules might be terrible. The shadow layer might be the system's adaptive correction to inadequate formal governance.

This framing is important because it determines the remediation posture. If shadow governance is treated as pathological by definition, the only acceptable response is enforcement -- reimposing the formal rules. But if the shadow rules are better than the formal rules, enforcement makes the system worse. The correct framing is not "governed good, shadow bad" but "governed auditable, shadow not."

If the shadow rules are better, the appropriate response is legitimization: promote the shadow state through the promotion ceremony retroactively, bringing it under governance with receipts, versioning, and contestability. This is not rubber-stamping. It is the system acknowledging that its formal rules were wrong and that the informal adaptation was a governance event that should have been, but was not, ratified.

### 10.2 Continuous Detection

The detection paradox (Section 5.3) implies that shadow governance detection should be a continuous process rather than a crisis response. Periodic clean-room differentials, routine provenance audits, and standing divergence metrics are early-warning infrastructure. The cost of continuous detection is ongoing. The cost of delayed detection is a system migration.

### 10.3 The Formal Layer as Attack Surface

In a Potemkin system, the formal governance layer is not merely useless -- it is an active liability. It provides false assurance to auditors, regulators, and operators. An attacker who wants to install persistent unauthorized control has a playbook: introduce a convenient shortcut (seeding utility debt), allow downstream systems to couple to it (building entrenchment), and wait for institutional memory of the formal rule to decay (relying on semantic erasure). The ratchet does the work. The formal layer provides cover. This is the adversarial complement to Paper 14's temporal attack surface [10]: where Paper 14 identifies the exploitation of detection-decision-response timing gaps, shadow governance exploitation relies on the ratchet operating over weeks, months, or years.

This implies that formal governance layers that are never challenged, never violated, and never updated are suspicious. A governance layer that perfectly matches reality is either extremely well-maintained or is simply not being checked against reality. The divergence index provides a way to distinguish these cases.

### 10.4 Open Questions

1. **Threshold or spectrum?** Is there a formal threshold where individual violations become stabilized shadow governance, or is it a continuous spectrum? Section 3.5 identifies full ratchet engagement (all three feedback loops active simultaneously) as a candidate threshold, but whether this transition is sharp or gradual is an empirical question.

2. **Retroactive legitimization.** What does it mean to promote shadow state through the promotion ceremony retroactively? Is it a rubber stamp or does it produce genuinely different governance properties? We argue it is not a rubber stamp: retroactive promotion produces receipts, versioning, and contestability that the shadow state previously lacked. But the practical difference between a rubber stamp and a careful retroactive ceremony may be difficult to enforce.

3. **Shadow governance detection in systems without receipts.** The detection methods in Section 5 assume some form of receipting or logging infrastructure. In systems with no receipts, detection requires behavioral observation alone. How reliable is detection from behavior without provenance records?

4. **Technical debt boundary.** Where exactly is the boundary between shadow governance and technical debt? We proposed an operational test (Section 2.3): does this state merely constrain implementation choices, or does it decide outcomes that actors treat as binding? But in practice, the boundary may be blurry. A poorly structured codebase that forces certain architectural decisions is exercising a kind of authority, even if nobody would call it governance. Whether a sharper formal test exists is an open question.

5. **The remediation window.** Can the remediation window be measured or predicted? If the ratchet deepens over time, is there a quantitative model of how dependency mass, utility debt, and semantic erasure grow? Such a model would convert the remediation paradox from a warning into a planning tool.

6. **Who benefits?** Utility debt creates constituencies that benefit from shadow governance remaining in place. Remediation redistributes convenience, discretion, and power -- not just technical architecture. Those who benefit from the shadow path's speed will resist its removal regardless of the formal justification. Remediation may therefore face political resistance beyond technical cost, and a governance framework that treats remediation as a purely technical migration will underestimate the difficulty of every path.

---

## 11. Conclusion

The breach is not the whole story. When unauthorized promotions accumulate and stabilize into a parallel governance structure, the result is not a larger breach but a different kind of problem -- a regime. The difference matters because the remediation strategy is completely different: bugs are fixed by enforcement; regimes require migration.

Shadow governance is best understood as an authority-path problem. It is not about bad rules or bad actors. It is about authority that is being exercised without a receipted, versioned, contestable path. The formal layer may be intact, well-documented, and recently audited. If the system's actual behavior is governed by unreceipted state, the formal layer is a compliance surface, not a control surface.

The stabilization ratchet explains why this condition persists. The Potemkin layer explains why it evades detection. The remediation pipeline explains why "just enforce the rules" fails once shadow governance has stabilized. And the central claim -- that shadow governance is not inherently pathological but is *ungoverned* -- determines the remediation posture: not enforcement, but legitimization where the shadow rules are better, migration where they are not.

The question is not "do we have rules?" It is: "does authority exist here that has no authorized path?"

---

## Acknowledgments

Language-model tools were used for editorial critique and literature discovery during preparation of this manuscript; all arguments, interpretations, and errors are the author's own.

---

## References

[1] Beck, J. (2026). Unauthorized Durability: A Composable Governance Primitive for State Promotion in Adaptive Systems. Preprint, Δt Framework Paper 18. doi:10.5281/zenodo.18940007

[2] Vaughan, D. (1996). *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA.* University of Chicago Press.

[3] Bowker, G.C. and Star, S.L. (1999). *Sorting Things Out: Classification and Its Consequences.* MIT Press.

[4] Cunningham, W. (1992). The WyCash Portfolio Management System. *OOPSLA '92 Experience Report.*

[5] DiMaggio, P.J. and Powell, W.W. (1983). The Iron Cage Revisited: Institutional Isomorphism and Collective Rationality in Organizational Fields. *American Sociological Review*, 48(2), 147-160.

[6] Meyer, J.W. and Rowan, B. (1977). Institutionalized Organizations: Formal Structure as Myth and Ceremony. *American Journal of Sociology*, 83(2), 340-363.

[7] Beck, J. (2026). The Gain Geometry of Temporal Mismatch: Shear, Leverage, and Capture in Multi-Timescale Systems. Preprint, Δt Framework Paper 16. doi:10.5281/zenodo.18717619

[8] Beck, J. (2026). Receipt the Compiler: Propaganda as Hidden Epistemic Policy and the Architecture of Legible Memory. Preprint, Δt Framework Paper 17. doi:10.5281/zenodo.18841815

[9] Hollnagel, E. (2014). *Safety-I and Safety-II: The Past and Future of Safety Management.* Ashgate.

[10] Beck, J. (2026). The Temporal Attack Surface: A Δt Framework for Asynchronous Security Systems. Preprint, Δt Framework Paper 14. doi:10.5281/zenodo.18236164
