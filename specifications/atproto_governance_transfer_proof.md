# ATProto Governance Layer: Ontology Transfer Proof

**Date:** 2026-02-20
**Status:** Specification note (not a roadmap)
**Related:** Agent Governor `specs/gaps/3X_BRAIN_DUMP.md` (artifact ontology, failure geometry)

## Purpose

This is a generalization test, not a product plan. The question: does the
governor's 5-artifact ontology transfer to a domain with fundamentally different
runtime characteristics (federated social infrastructure vs LLM coding agents)?

Short answer: yes, and the mapping is cleaner than expected because ATProto
already solved identity and integrity. The governance layer is the only thing
missing.

## Claim

ATProto provides:
- **What was written** (content-addressed CIDs, Merkle tree repos)
- **Who signed it** (DID-based identity, signed repo commits)

ATProto does not provide:
- Why something was delayed or routed
- What regime it entered
- Who overrode a routing decision
- What recovery path was taken after containment

**Provenance is not governance.** Cryptographic integrity proves authorship and
content. It says nothing about the runtime decisions made about that content
after creation. This is the same gap the governor addresses in LLM runtimes:
the model produces output (provenance), but the gate decides what happens to it
(governance).

## Artifact Mapping

The 5-artifact ontology from the governor's 3.x design maps to ATProto at both
the PDS (Personal Data Server) and relay layers:

| Artifact | Governor domain | ATProto PDS | ATProto Relay |
|----------|----------------|-------------|---------------|
| **MeasurementSnapshot** | Signal values at gate time | Account state at submit: rate, age, prior violations, graph metrics, token provenance | Event stream metrics: burst timing, PDS clustering, labeler agreement, fanout velocity |
| **TransitionProposal** | Proposed theta change + evidence | Write request: create post, delete, profile edit, follow burst, repo import | Fanout request: event propagation, indexing, subscription delivery |
| **AuthorityReceipt** | Proof authority was checked | Operator/admin intervention: manual override, policy escalation | Relay admin action: routing override, PDS trust adjustment |
| **RecoveryPlanReceipt** | Planned (not ad-hoc) recovery | Constrained path back from containment: what changes, what timeline, what evidence | Graduated re-entry: restore fanout incrementally, require dwell time at each stage |
| **ResetReceipt** | State reset with provenance | Session/key/tool reset after lock event | Trust score reset, fanout restoration, PDS re-indexing |

## Novel Capability: Containment Without Erasure

Every existing moderation system operates on a binary: **fully live** or
**removed/banned**. A governance layer enables intermediate routing:

At the PDS layer, LOCKED can mean:
- Delayed publish
- Private staging lane
- Reduced fanout
- No mass-follow / no bulk actions
- Text-only / no embeds
- Challenge-required actions

At the relay layer, regime routing on event fanout:
- **NORMAL**: immediate fanout
- **ELEVATED**: fanout with sampling / delayed propagation
- **DWELL**: hold-and-evaluate lane
- **RECOVERING**: reduced capability surface (no high-amplification events)
- **LOCKED**: no public fanout, but receipts + archival path still active

The key: **containment without pretending the event never existed.** The event is
receipted, the routing decision is receipted, the recovery path is receipted.
This produces a legible audit trail instead of "trust us, moderation happened."

## Failure Geometry Mapping

ATProto abuse is not "this post bad." It's patterns — combinations of signals
that produce qualitatively different diagnoses:

| Signal class | Examples |
|-------------|----------|
| Temporal | Burst timing, post velocity, follow/unfollow churn rate |
| Topological | PDS clustering, graph density anomalies, coordinated repo activity |
| Content | Repeated near-identical ops, template-driven posts |
| Epistemic | Labeler disagreement patterns, appeal frequency, flag clustering |

Most moderation systems flatten these into vibes + heuristics + staff escalation.
A governor approach treats them as measured state with typed transitions and
constrained routing. Much harder to launder. Much easier to debug.

This is the same insight as the governor's failure geometry concept: reasoning
about **combinations** of signals, not individual scalar thresholds.

## Political and Deployment Constraints

### Hard problems
- **Latency budget** at relay layer (inserting gates adds propagation delay)
- **False positive optics** ("algorithmic suppression" accusations are instant)
- **Authority distribution** (who gets AuthorityReceipt power: operator, relay admin, labeler, automated break-glass?)
- **Federation politics** (federated systems resist shared governance semantics until catastrophe forces them)

### Deployment wedge: PDS-sidecar first

The practical path avoids "central censorship appliance" framing:

1. PDS-sidecar for self-hosters and managed PDS providers
2. Emit receipts locally (governance is self-applied, not imposed)
3. Optional relay-facing signals added later (opt-in, not mandatory)

This mirrors the governor's own deployment model: enforcement is local to the
runtime, receipts are the coordination substrate, no central authority required.

## Implication for Governor Ontology

This transfer proof provides evidence that:

1. The 5-artifact ontology is **domain-independent** — it describes governance
   relationships, not LLM-specific concepts
2. **Failure geometry** generalizes to any system with multi-signal abuse patterns
3. **"Containment without erasure"** is a capability gap in most runtime systems,
   not just LLM tooling
4. The **LOCKED-as-routing-regime** framing (from `3X_BRAIN_DUMP.md` item #1)
   maps directly: LOCKED means "route through constrained lane," not "stop"

The nouns travel. The verbs (measure, propose, receipt, route, recover) travel.
The invariants (provenance != governance, containment != erasure, recovery
requires external entropy) travel. This is evidence that the ontology is
correctly factored.
