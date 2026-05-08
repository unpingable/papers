# Thin-Slice Ratchet

*(broader name: Conservatism Amplification Across Agents)*

**Status:** candidate
**Kind:** attractor (recurring basin) — multi-agent review loops fall into this basin when two or more cautious reviewers compose, without any single agent recommending recklessness or refusing action.
**Originated:** 2026-05-08 (chatty diagnosis after operator-surfaced pattern from driftwatch case: 97 stall captures, recurring writer stalls, millions of queue-boundary drops, ~3.4 days disk runway, and yet the next proposed move was still *"maybe run one more toggle"* or *"Phase 1 only."* User named the pattern as recurring across the cabinet, not driftwatch-specific).
**Primary home (paper):** none yet. Cross-tooling primitive — applies to Nightshift, Continuity, papers/Lean cabinet, and any multi-agent review loop. Candidate destinations: methodology essay, agent-governance section.

## Aphorism (keepers)

> *Two conservative agents can manufacture inaction without either one refusing action.*

> *A safe slice can become unsafe when it preserves the failing premise.*

> *At some evidence threshold, smaller slices stop reducing risk and start extending exposure.*

> *Conservative slicing is a tactic. It is not a virtue function.*

## Kernel

A multi-agent review loop where each agent proposes the smallest reversible next step. Each step is locally correct restraint — no agent refuses action, no agent recommends recklessness. But the *composition* of multiple agents' caution amplifies into system-level paralysis: each agent's narrow framing is treated by the next agent as confirmation that further narrowing is wise.

```
Agent A: take a bounded slice.
Agent B: mirrors boundedness, narrows further.
Agent A: sees B's narrow framing, preserves caution.
Agent B: treats A's caution as confirmation.
Result: the next slice is safe, local, reversible — and increasingly useless.
```

Locally correct restraint composing into globally costly under-action. Not cowardice by either agent. **Worse:** it looks responsible right up until urgency has been quietly converted into paperwork.

## Formal-ish shape

Let `R(t)` be risk of acting at time `t` (reversibility, scope, blast radius). Let `E(t)` be risk of continued observation (exposure compounding, runway depletion, accumulated harm).

Conservative slicing is correct while `R(t) > E(t)`. The pathology arises when:

- `R(t)` decreases as more datapoints arrive (action becomes safer with more information).
- `E(t)` increases with continued exposure (cost compounds).
- At threshold `t*` where `R(t*) = E(t*)`, the regime should switch from observation to action.
- **Ratchet failure:** cabinet keeps proposing slices past `t*`, treating `R`'s monotone decrease as ongoing license for more observation.

The pathology is that *the very monotonicity that justified initial slicing* — each datapoint reduces `R` — becomes the rationalization for continuing past `t*`.

## Recognition criteria

- Repeated *"small next step"* proposals across multiple review rounds.
- Evidence base already sufficient for a larger decision (multiple confirmations, accumulated runway data, recurring failure indications).
- Slices preserve the *premise under suspicion* — the very thing being investigated.
- Risk of *action* is discussed more than risk of *continued exposure*.
- *"One more datapoint"* keeps winning against *"act on accumulated evidence."*
- Decision latency approaches or exceeds the timeframe in which the failure could compound.

## Guardrail — the evidence-threshold check

Before approving the next bounded slice, require explicitly:

> *Has the risk of continued observation now exceeded the risk of acting?*

If the answer is *yes* and the proposed slice still preserves the failing premise, the slice is no longer protective — it is exposure-extending.

For multi-agent setups, the threshold-check is the **operator's responsibility**, not delegable to any single agent. Each agent will correctly apply tactical caution; only the operator can see the composition.

## Failure predicate

Thin-slice ratchet occurs when:

1. Two or more review agents are active.
2. Each agent's proposals are individually well-calibrated for caution.
3. Cumulative evidence has crossed an action-threshold.
4. The next proposal is still bounded narrower than the threshold would license.
5. The proposal preserves rather than tests the premise under suspicion.
6. No agent has surfaced the evidence-threshold check explicitly.

The six conditions are jointly required. (1)+(2) alone is healthy multi-agent review. (1)+(2)+(3) without the rest is normal escalation. The full conjunction is the ratchet.

## Adjacency map

- **Guardrail Capture** (`primitives/guardrail-capture.md`) — single-agent sibling. Guardrail Capture: an agent suppresses task in service of a misread constraint. Thin-slice ratchet: two agents jointly suppress action by amplifying each other's caution. Same family (constraint-shaped pathology), different cardinality.
- **Conservative-trim override** (`feedback-conservative-trim-override.md`) — operator-side correction for the single-agent variant. Same axis as ratchet, different intervention point. Conservative-trim override is *"operator overrides one agent's over-trim"*; ratchet is *"operator must override the composition of multiple agents' trims."*
- **Failed factoring as honest boundary** (`feedback-failed-factoring-as-honest-boundary.md`) — adjacent but distinct. That memory: knowing when to stop trying to factor. Ratchet: knowing when to stop slicing. Both are anti-perfectionism disciplines but at different stages.
- **Solution-family exhaustion** (chatty's note, not yet a separate primitive) — adjacent. SFE: too many fixes inside the same premise (premise wrong but unrecognized). Ratchet: review keeps shrinking action even after the premise is already indicted. SFE is premise-blindness; ratchet is threshold-blindness.
- **Δt framework / belated consequence** — late-action direction. Belated consequence is the temporal-shadow form of the same shape: by the time review converges, the window in which action could have mattered is closed. Thin-slice ratchet is one mechanism for getting there.

## Do not confuse with

- **Healthy bounded review.** When `R(t) > E(t)` genuinely, bounded slicing is correct. Ratchet is the *threshold-blind* version: slicing continues past the point where the risks invert.
- **Single-agent over-conservatism.** That's the conservative-trim or guardrail-capture pattern. Ratchet specifically requires the multi-agent composition mechanism — caution-as-confirmation across the loop.
- **Decision paralysis from incompleteness.** Classic *"need more data"* can occur with one agent. Ratchet is when *multiple* agents reinforce each other's *"more data"* framing without any of them surfacing the threshold question.
- **Bureaucratic risk-aversion.** Institutional pattern. Ratchet can occur in tight multi-agent loops without any institutional structure — it's a composition pathology of cautious reviewers, not bureaucracy.

## Worked instance (origin)

**Driftwatch case, 2026-05-08.** 97 stall captures, recurring writer stalls, millions of queue-boundary drops, ~3.4 days disk runway. Multiple cabinet rounds proposed bounded next steps (*"maybe run one more toggle,"* *"Phase 1 only"*). Cumulative evidence had long crossed the threshold for consequential action; the slicing continued anyway. Recognition surfaced operator-side; chatty named the pattern.

Exhibits all six failure-predicate conditions: multiple review agents, individually-calibrated caution, threshold-crossed cumulative evidence, bounded-narrower-than-licensed proposals, premise-preserving slicing, no explicit evidence-threshold check.

## Architectural rule

> *Conservative slicing is a tactic. It is not a virtue function.*

Tactical caution is correctly applied below the action threshold. Above the threshold, continued caution converts urgency into paperwork. Cabinet discipline must include the evidence-threshold check as a load-bearing review gate, not as an optional check that gets skipped under amplification pressure.

## Promotion guardrail (candidate → working)

Hold as candidate until at least one of:

1. A second worked instance from a different domain (not driftwatch) exhibits the same six-condition failure-predicate, confirming cross-tooling reach.
2. An operator override on the basis of *"thin-slice ratchet recognized"* successfully changes a cabinet outcome, and the override survives review.
3. A methodology / agent-governance essay uses the keeper line and the threshold-check guardrail in prose.

## Provenance

- **2026-05-08 origin.** Chatty diagnosis after operator-surfaced pattern from driftwatch case. Keepers and structured failure-mode summary (recognition / guardrail / keeper) provided by chatty in standard cabinet-shaped format.
- **Multi-model lineage:** chatty (naming, structural diagnosis, four keeper lines, structured summary), user (operator-side recognition; named the pattern as recurring across cabinet, not driftwatch-specific), claude-code-papers (this primitive entry).
- Filed candidate / default-density per `feedback-note-density-subtypes.md`. Cross-tooling — applies to any multi-agent review loop, not just Nightshift / Continuity / driftwatch.
