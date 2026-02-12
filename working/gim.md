---
title: "Governor Insertion Method (GIM)"
author: James Beck
date: 2026-02
status: working paper
provenance: "Emerged from a DeepSeek → ChatGPT → Claude cross-model session. DeepSeek asked whether the Δt framework had a generalizable operational methodology; ChatGPT produced the seven-step method; Claude filed and cross-referenced it."
---

# Governor Insertion Method (GIM)

A design methodology for placing temporal governors in layered systems. Think "threat modeling," but for **closure + time + boundary load**.

This is the operational bridge between the theoretical framework (cybernetic fault domains, paper [15]) and the motivation (why governors are needed — *The Jar Brain*). Paper 15 gives you the theory. The Jar Brain gives you the "why." GIM gives you the "how."

---

## Inputs

* A layered system with components, interfaces, and operators (humans/agents/services).
* Observability access: logs, traces, configs, build artifacts, workflows.

## Outputs

* A **closure map** (C_k) across layers
* Measured **Δt** (latency between state change and corrective action)
* Measured **σ** (boundary load) per interface / team / tool
* A **governor placement plan**: what to gate, where, and with what enforcement class

---

## Step 0: Draw the system as a DAG of commitments

Not "architecture diagram." A **commitment graph**:

* Nodes = stateful loci (repo, DB, queue, policy store, human decision, model output cache, deployment config)
* Edges = actions that change state (write, deploy, approve, promote, rotate, reconcile)
* Annotate each edge with:

  * actor (human, agent, service)
  * reversibility cost
  * blast radius
  * existing controls (reviews, authz, CI, rate limits)

If you can't express the system as "who can change what," you can't govern it.

---

## Step 1: Identify closure layers (C_k)

Define C_k as "the layer where this class of error is *detectable and correctable* with bounded cost."

For each failure class (pick 5–15, not infinite):

* drift (spec vs implementation)
* unsafe actuation
* silent bypass
* stale configuration
* bad provenance
* runaway automation
* schema erosion

Find **the earliest layer** where you can reliably:

1. detect it, and
2. prevent it or roll it back cheaply.

That's the candidate closure layer C_k.

Heuristic:

* If detection is only possible after irreversible action, your C_k is too late.
* If prevention requires perfect prediction, your C_k is too early.

---

## Step 2: Measure Δt (control latency)

For each failure class and candidate C_k, measure Δt as:

> Δt = time from *bad state introduced* → *bad state detected* → *corrective action applied*

You don't need perfect instrumentation; use:

* git timestamps (introduce)
* CI / monitoring alerts (detect)
* rollback / revert / config change (correct)

Break Δt into:

* Δt_detect
* Δt_correct
* Δt_total

If Δt_total exceeds the system's tolerance window (i.e., the point where damage becomes large), you need a governor earlier or stronger.

---

## Step 3: Measure σ (boundary load)

σ is the "stress on boundary interfaces" — where ambiguity, throughput, or coordination costs pile up.

Measure σ per interface/tool boundary using proxies:

* change rate × review load
* incident rate attributable to that boundary
* number of handoffs (teams/tools)
* variance in input formats (schema drift / "HTML as API" crimes)
* number of bypass paths available
* cognitive load indicators (frequent "which session am I in?"; repeated mistakes)

High σ boundaries are where governors actually pay rent.

---

## Step 4: Classify governor type by enforcement class

Governors aren't one thing. Pick the lightest that closes the loop.

**G0: Observability governor**

* receipts, audits, provenance
* no blocking
* use when Δt is acceptable but uncertainty is high

**G1: Precondition governor (soft gate)**

* warnings, required attestation, preflight
* use when errors are common but reversibility is high

**G2: Hard gate (physics)**

* hook blocks write/deploy/actuation (exit code 2)
* use when reversibility is low or σ is high

**G3: Capability proxy**

* force all actuation through governed tools (MCP/tool proxy)
* use when bypass paths exist (direct-write, symlink escape)

**G4: Closed-loop controller**

* rate limits, dwell-time, rollback automation, budgeted action selection
* use when the system is dynamic and needs continuous regulation

Placement rule:

* Put the governor at the *lowest* layer that still sees the "intent → actuation" boundary.
* If the actor can bypass that layer, your governor is decor.

---

## Step 5: Placement algorithm (practical)

For each edge in the commitment DAG:

1. Compute **Risk = (blast radius × irreversibility × change rate)**
2. Compute **Control gap = Δt_total − tolerance_window**
3. Compute **Boundary stress = σ**

Then:

* If Risk high AND gap high → **G2/G3**
* If Risk medium AND σ high → **G1/G2**
* If Risk low but uncertainty high → **G0**
* If bypass exists → **upgrade to G3** regardless

---

## Step 6: Prove it with a bypass test suite

Every governor placement needs a "can we route around it?" test.

Examples:

* unapproved write
* bash heredoc/tee
* config stale (settings newer than invocation stamp)
* direct-write path (agent B writes without agent A's tool gate)
* symlink escape (if you're in that league)

If you can't name the bypasses, you don't have a governor, you have a ritual.

This is the fork test from *The Jar Brain*, operationalized: "if the generator can talk its way past the gate, the gate doesn't exist" — except now it's a test suite, not a thought experiment.

---

## Step 7: Deliverables (what you'd actually ship)

* `CLOSURE_MAP.md`: failure classes → C_k layer + rationale
* `CONTROL_METRICS.json`: Δt/σ baselines per boundary
* `GOVERNOR_PLAN.md`: where to insert G0–G4, what it gates, what it logs
* `tests/governance_bypass/`: smoke tests proving enforcement is live
* `preflight --strict`: the "installed ≠ effective" detector

---

## Falsifiability

Two falsifiers:

1. **If you can't quantify Δt and σ with *any* proxies, you can't operationalize the method.**
   (Then you're doing vibes-based governance.)

2. **If your bypass suite can route around your governor, it's not at C_k; it's theater.**

---

## Minimum viable template

* define system DAG
* list failure classes
* for each: pick C_k, measure Δt, estimate σ
* choose governor class G0–G4
* write bypass tests
* require preflight before work starts

That's "control theory meets SRE threat modeling," minus the incense.

---

## Cross-references

| Concept | GIM step | Paper 15 | Jar Brain |
|---------|----------|----------|-----------|
| Commitment graph | Step 0 | C_k taxonomy (C0–C3) | — |
| Closure layers | Step 1 | §2 closure definition | "the fix that works" §5 |
| Δt measurement | Step 2 | §2 Δt = max{0, T_commit − (W+A)} | — |
| σ measurement | Step 3 | §2 boundary load definition | — |
| G0–G4 taxonomy | Step 4 | v0.3 governor architecture (planned) | governor as prosthetic |
| Placement algorithm | Step 5 | v0.4 dimensionless risk index (planned) | — |
| Bypass test suite | Step 6 | — | fork test §6 |
| Three-clock decomposition | Step 2 (Δt_detect/correct) | §3.4 async security | — |
