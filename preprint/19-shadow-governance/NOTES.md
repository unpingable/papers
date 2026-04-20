# Paper 19: The System Beside the System — Working Notes

## Changelog

### 2026-04-20 — v1.0.1 (citation correction)

- Reference [10] corrected: Paper 14 citation had an incorrect DOI and subtitle. Reconciled against `14-temporal-attack-surface/metadata.yaml` via `tools/citation_graph.py`.
- `metadata.yaml`: `version: "1.0"` → `"1.0.1"`. Body status line updated to match.
- PDF rebuilt.

## Status
Not yet drafted. Concept emerged during Paper 18 development. `paper.md` is the raw multi-model conversation that generated both Paper 18 and this follow-on.

## Thesis (one sentence)
Systems are often not captured by direct violation of formal rules, but by the accumulation of shadow rules that gain durability and authority without legitimate promotion.

## Relationship to Paper 18
- **Paper 18** (unauthorized durability) = the breach. How illegitimate promotion works.
- **Paper 19** (shadow governance) = the settlement. What accumulates when illegitimate promotion becomes normalized and starts functioning as parallel governance.

One is about **the crossing**. The other is about **the illegal settlement**.

## Core arc
transient exception → repeated shortcut → precedent → tacit rule → shadow doctrine → parallel constitution

Nobody signs anything. Nobody announces a rewrite. The system just starts acting like the workaround was always law.

## Key concepts

### Ghost permissions
Permissions that don't exist in formal policy but reliably work in practice. "Permissions that have no visible mass but are clearly moving the stars."

### Normalization-of-deviance ratchet
Three feedback loops that prevent informal updates from reverting:
- **Utility debt trap**: shadow path is faster, so users migrate to it; reverting now carries massive opportunity cost
- **Dependency entrenchment**: other systems build on the hack; fixing the exception breaks downstream dependents
- **Semantic erasure**: institutional memory of the formal rule decays; eventually nobody remembers the exception was an exception

### Negative-space auditing
Don't ask "what rules exist?" Ask: "where did authority appear without a matching authorized path?"

### The formal/shadow divergence
- The official system says one thing
- The lived system keeps doing another
- The discrepancy stabilizes
- Eventually the shadow layer becomes the real controller

The formal system often becomes a parasitic layer — providing legitimacy and branding (the L3 skin) while the shadow system handles the actual control loops.

## Audit ideas (from Gemini, stripped of theatrics)
- **Clean room differential**: compare a fresh instance against a live one to detect de facto drift
- **Semantic stress test**: probe for alias-based bypasses (ontology-spoofing test harness)
- **Provenance exhaustion**: force every allowed action to show its authorizing path
- **Divergence index**: delta between formal policy and de facto execution path
- **Dependency mass**: how many sub-systems would break if formal policy were strictly enforced today
- **Observability gap**: volume of state transitions invisible to the formal audit log

## Candidate titles
- The System Beside the System
- Shadow Governance in Adaptive Systems
- How Exceptions Become Doctrine
- Parallel Constitution
- Informal Update Paths and De Facto Rule Formation

"The System Beside the System" has the strongest resonance. Gemini: "It sounds like a ghost story for people who manage production environments."

## Series connections
- Paper 18: the promotion mechanism (unauthorized durability)
- Paper 19: the stabilized aftermath (shadow governance)
- Paper 16: capture regime = the state where shadow governance has already won
- Paper 17: propaganda = adversarial shadow governance over public memory
- Book Ch 6-7: training layer + subtraction-as-legitimization = institutional shadow governance in practice
- Vaughan (Challenger): normalization of deviance as the canonical case study

## What the paper actually needs to argue

### The core claim Paper 18 didn't make
Paper 18 says: unauthorized promotion is the mechanism of capture.
Paper 19 says: **when unauthorized promotions accumulate and become load-bearing, they form a parallel governance structure that is harder to fix than the individual violations that produced it.**

That's not just "more capture." It's a phase transition. Individual write-barrier violations are bugs. Stabilized shadow governance is a regime. The difference matters because the remediation strategy is completely different:
- For individual violations: enforce barriers, deny promotion, emit receipt. Done.
- For stabilized shadow governance: you can't just "turn the barriers on" because the system has reorganized around the unauthorized state. Strict enforcement of formal policy would break the system.

### The formal definition (sketch)
In Paper 18's terms, shadow state is:

**The set of effectively governing state that occupies L2/L3 authority without having passed through a promotion ceremony.**

More precisely, at any time t, the system has:
- `S_formal(t)` = state that reached L2/L3 via attested promotion paths
- `S_shadow(t)` = state that exercises L2/L3 authority but has no valid promotion receipt

Shadow governance exists when `S_shadow(t)` is nonempty. Shadow governance is *dominant* when `S_shadow(t)` has more influence on system behavior than `S_formal(t)`.

The divergence index is then just: how much of the system's actual behavior is explained by `S_formal` vs `S_shadow`?

### The ratchet (why it stabilizes)
The three feedback loops aren't just failure modes — they're a stability mechanism for the shadow layer. Each one raises the cost of correction:

1. **Utility debt**: the shadow path is faster/cheaper, so traffic migrates to it. Correction now means making everyone slower.
2. **Dependency entrenchment**: other subsystems couple to the shadow state. Correction now means breaking downstream systems.
3. **Semantic erasure**: the original formal rule loses institutional memory. Correction now means re-deriving what the rule even was.

The ratchet is complete when all three operate simultaneously: the shadow path is faster (utility), other things depend on it (entrenchment), and nobody remembers it was an exception (erasure). At that point, the formal rule is a legacy artifact and the shadow rule is the de facto constitution.

This is the same hysteresis problem from Paper 18 (T6), but at system scale rather than individual-state scale. Paper 18's hysteresis depth metric (M6) measures how hard it is to reverse a single captured state. Paper 19 asks: what happens when the entire system is in a hysteretic basin?

### The Potemkin layer
The nastiest implication: once shadow governance dominates, the formal governance layer doesn't disappear. It persists as a **legitimacy shell** — the thing you point to when someone asks "how is this governed?" The formal rules provide the branding. The shadow rules provide the actual control.

This means audit against formal policy produces false assurance. The system passes the compliance check because the formal rules are intact. The system behaves according to shadow rules because those are the ones that are actually load-bearing.

Detection requires auditing **behavior against receipted promotion paths**, not **policy documents against stated goals**. That's the negative-space auditing idea: look for authority that has no matching authorized path.

### What makes this a separate paper (not just Paper 18 section 10.5)
Paper 18 is about the promotion mechanism. It assumes violations are individual and correctible.
Paper 19 is about what happens when violations compound into structure. At that point:
- The system has two governance layers (formal + shadow)
- They may conflict
- The shadow layer may be more adaptive, faster, and more tightly coupled to actual operations
- Correcting the shadow layer is a system-migration problem, not a policy-enforcement problem
- The formal layer may actively conceal the shadow layer by providing a compliance surface

That's a different paper because it's a different problem with different solutions.

### Worked examples (candidates, pick 1-2)

**Agent memory drift.** An LLM agent accumulates preferences and routing patterns through context carry-forward that never passed through a promotion gate. Over time, the agent's behavior is governed more by its accumulated context artifacts than by its formal policy. A clean-room comparison (fresh instance vs live instance given identical prompts) reveals the divergence. Remediation requires not just "clearing memory" but understanding which downstream behaviors depend on the shadow state.

**Platform moderation drift.** A content moderation system has formal rules (the published community guidelines) and operational rules (the actual enforcement patterns). Over time, the operational patterns diverge: certain content types are de facto allowed despite being formally prohibited, because enforcement exceptions became precedent. New moderators learn the operational patterns, not the formal rules. The formal rules remain on the website. The shadow rules govern actual decisions. A divergence audit would compare enforcement outcomes against stated policy and find systematic gaps.

**Institutional ops drift.** An engineering team has a formal deployment process (reviewed, staged, canary) and an "emergency" path (direct push with post-hoc review). The emergency path is faster. Over time, most deploys use the emergency path. The formal process still exists in the runbook. Nobody follows it. New hires learn the emergency path first. The formal path becomes the thing you do when someone's watching.

### Structure (tentative)
1. Introduction: the problem after the breach
2. Formal definition of shadow state (in Paper 18's terms)
3. The ratchet: why shadow governance stabilizes
4. The Potemkin layer: how formal governance becomes a legitimacy shell
5. Detection: negative-space auditing, clean-room differential, provenance exhaustion
6. Worked example(s)
7. Metrics: divergence index, dependency mass, observability gap, remediation cost
8. Remediation: why "just enforce the rules" doesn't work, and what does
9. Related work (Vaughan, normalization of deviance, institutional theory, organizational debt)
10. Implications and open questions
11. Conclusion

## The "ungoverned, not pathological" framing
Shadow governance is dangerous because it is **unratified, unaudited, and hard to contest** — not because informal adaptation is always bad. The formal rules might be terrible. The shadow layer might be the system's adaptive correction. The right framing is:
- Shadow governance is not inherently pathological. It is *ungoverned*.
- If the shadow rules are better than the formal rules, the right response is to *legitimize them through the promotion ceremony*, not to delete them.
- But that requires knowing they exist, which requires detection.
- The paper should be neutral on "good vs bad" and focus on "governed vs ungoverned."

This is the distinction that keeps the paper from becoming formalist whining or moral panic literature.

## Remediation (the hard section — needs invention)
"Enforce the rules" is not a fix when the system has reorganized around shadow state. Remediation is a migration event.

### The remediation pipeline
1. **Detect** the shadow layer (clean-room differential, provenance exhaustion, negative-space audit)
2. **Classify** whether shadow state is adaptive, pathological, or mixed
3. **Measure blast radius** — dependency mass, what breaks if shadow state is removed
4. **Choose a path**:
   - **Legitimize**: promote shadow state through the ceremony retroactively. Acknowledges the de facto reality, brings it under governance. Risk: rubber-stamps bad state.
   - **Quarantine**: isolate shadow state, prevent further coupling, but don't remove yet. Buys time for assessment.
   - **Migrate**: build parallel clean state, deprecate shadow path, move dependents over incrementally. Most expensive, most controlled.
   - **Replace**: accept that the shadow rules are better, replace formal rules with shadow rules, ratify through constitutional ceremony, start fresh. Requires the system to admit its formal rules were wrong.
5. **Execute transition** without pretending rollback is free — every path has a cost, and the cost increases with dependency mass and semantic erasure depth

### Why this is hard
- You can't just "turn the barriers on" retroactively — the system has reorganized around the unauthorized state
- Strict enforcement of formal policy would break the system (dependency entrenchment)
- The formal rules may no longer be appropriate (the shadow layer adapted for good reasons)
- The people who understand the shadow state may not know the formal state, and vice versa (semantic erasure)
- Detection itself may be resisted by those who benefit from the shadow layer's speed and convenience (utility debt creates constituencies)

### The remediation paradox
The longer you wait, the harder it gets (ratchet deepens). But premature remediation without understanding dependency mass causes cascading failures. This suggests remediation has a window — after detection but before full entrenchment — that shrinks over time. Missing the window means you're doing a full system migration, not a policy fix.

## Open questions for this paper
1. Is there a formal threshold where individual violations become "shadow governance"? Or is it a spectrum?
2. Can shadow governance be *benign*? (The shadow rules might actually be better than the formal rules. The system may have adapted around bad formal policy.) If so, the paper needs to acknowledge that shadow governance is not inherently pathological — it's *ungoverned*, which is different.
3. How does remediation work? You can't just delete the shadow state if the system depends on it. Do you legitimize it (promote it through the ceremony retroactively)? Migrate away from it? Replace the formal rules with the shadow rules and start fresh?
4. What's the relationship between shadow governance and technical debt? They look similar. The difference might be that shadow governance has *authority* — it's not just accumulated mess, it's accumulated mess that makes decisions.
5. Is there a remediation window? Detection → assessment → migration before full entrenchment. Does the window have a measurable size? Can you predict when it closes?
6. What does "legitimize retroactively" actually look like? Is it just a rubber stamp? Or does retroactive promotion through the ceremony produce genuinely different governance properties than no ceremony at all?
7. Who benefits from shadow governance remaining invisible? The utility debt creates constituencies. Remediation may face political resistance, not just technical difficulty.

## Focus warning
Don't let 19 become a junk drawer for all the dark implications of 18. The center is very specific: **shadow state becomes load-bearing and starts governing behavior more than formal state.** If that stays central, the paper holds. If it turns into "and here are all the ways systems haunt themselves," it'll get baggy fast.

## Papers that are NOT this paper (but are real)
These emerged as candidate 19s but are better as their own future work:
- **Observer witness architectures** — what external witnesses require, what trust assumptions they introduce, whether the regress terminates. (Paper 11 identified the problem; Paper 18 flagged it as hardest open question.)
- **Ontological spoofing / type-system attacks** — the SQL injection of governance. You don't break the gate, you break the language the gate speaks. Tight technical paper, implementation-facing.
- **Composition across trust boundaries** — System A's L2 is System B's L0. How do promotion ceremonies compose when there's no shared L3? The MCP/multi-agent/institutional-interop paper. Most immediate practical pull.

## Next steps (when ready)
1. Define shadow state formally
2. Formalize the ratchet as a stability analysis
3. Pick and develop 1-2 worked examples
4. Draft the paper from the notes, not the conversation
