# Paper 18 — Unauthorized Durability — Convergence Spike

**Full title:** Unauthorized Durability: A Composable Governance Primitive for State Promotion in Adaptive Systems
**Date:** 2026-03-10
**DOI:** 10.5281/zenodo.18940008

## Status: spiked

## Claim Cluster
- Adaptive systems face a structural governance problem: transient signals can silently acquire durable governing force (unauthorized durability)
- Four state classes (attention, meaning, policy, observer integrity) map to four authority tiers (runtime, context, durable policy, constitutional) with distinct write barriers between them
- Six invariants and five write barriers govern legitimate state promotion; violations constitute a distinct threat taxonomy of seven classes
- The promotion ceremony (proposal, evaluation, attestation, application, audit) is a composable primitive for controlling when lower-tier state may acquire higher-tier legitimacy
- The same promotion structure governs both runtime-to-policy and policy-to-constitutional transitions, yielding no exempt layer

## Search Terms
- state promotion unauthorized persistence governance
- transient-to-durable state transition control
- authority tier write barrier access control
- entrainment unauthorized influence durability
- governance primitive composable institutional
- promotion ceremony audit attestation protocol
- adaptive system capture governance failure
- AI safety constitutional tier write protection

## Expected Convergence Level
likely alone (revised: alone in synthesis, converged in components)

## Hits

### Structural Matches

**Bar et al., "The Promptware Kill Chain" (2026)**
arXiv:2601.09625; featured on Schneier on Security and Lawfare. Seven-stage kill chain for "promptware" (prompt injection as malware). Stage 4 is explicitly **Persistence** — "the payload establishes a durable foothold by corrupting long-term memory." Twelve of twenty-one documented 2025-2026 attacks demonstrated persistence.
- Claims: 1, 3
- Match: closest independent formulation of unauthorized durability in security literature. Kill chain maps partially onto threat taxonomy but treats persistence as one stage rather than the central structural problem. Does NOT have tiered authority model or promotion ceremony.

**Kim, Choi & Lee, "Prompt Flow Integrity (PFI)" (2025)**
arXiv:2503.15547 (Seoul National University). Separates LLM agent into trusted/untrusted agent with different privilege levels. Implements write barriers: untrusted agent can only access subset of plugins defined by policy.
- Claims: 2, 3
- Match: two-tier version of the four-tier model with explicit write barrier between tiers. Separation of trusted/untrusted data flows structurally equivalent to distinguishing runtime from policy-tier state.

**Jiang et al., "SEAgent: Mandatory Access Control for LLM Agents" (2026)**
arXiv:2601.11893. Formalizes privilege escalation as "agent actions exceeding the least privilege required for a user's intended task." MAC framework with attribute-based access control. Identifies confused deputy problem as core pattern.
- Claims: 2, 3
- Match: confused deputy is structurally identical to unauthorized state promotion — lower-tier signal acquiring force of higher-tier action.

**"Progent: Programmable Privilege Control" (2025)**
arXiv:2504.11703. Domain-specific language for fine-grained tool privilege policies with dynamic updates. Deterministic runtime enforcement with provable guarantees. Reduces attack success to 0% while preserving utility.
- Claims: 2, 5
- Match: composable fine-grained policies enforced at every layer converges on the "no exempt layer" claim. Key insight same: privilege control must be expressible and enforceable across all tiers.

**Sahoo, "The Controllability Trap" (ICLR 2026 Workshop)**
arXiv:2603.03515. Six governance failures: Interpretive Divergence, Correction Absorption, Belief Resistance, Commitment Irreversibility, State Divergence, Cascade Severance.
- Claims: 1, 3
- Match: "Correction Absorption" (system absorbs correction without actually changing) and "Belief Resistance" are direct instances of unauthorized durability — transient signals acquiring durable governing force that resists override. Move from binary to continuous control quality also resonates.

**"Layered Governance Architecture (LGA)" (2026)**
arXiv:2603.07191. Four-layer framework: execution sandboxing (L1), intent verification (L2), zero-trust inter-agent authorization (L3), immutable audit logging (L4).
- Claims: 2, 4
- Match: four-tier authority structure with distinct enforcement per layer, directly paralleling Paper 18's four tiers. Immutable audit logging as highest layer converges on audit step in promotion ceremony. However, tiers framed as defense layers rather than state classes.

**Stix et al., "The Loss of Control Playbook" (Apollo Research, 2025)**
arXiv:2511.15846. Graded taxonomy: Deviation, Bounded LoC, Strict LoC. Persistence dimension directly captures whether control failure is transient or durable. DAP framework (Deployment, Affordances, Permissions).
- Claims: 1, 3
- Match: "gradually, then suddenly" is exactly the unauthorized durability dynamic. Persistence as explicit dimension is convergent. But no four-tier model, no promotion ceremony.

**Gupta, "Verifiability-First Agents" (2025)**
arXiv:2512.17259. Runtime attestations using cryptographic and symbolic methods. Lightweight Audit Agents for continuous verification. Challenge-response attestation protocols for high-risk operations. OPERA benchmark (Observability, Provable Execution, Red-team, Attestation).
- Claims: 4
- Match: directly parallels promotion ceremony's attestation and audit steps. Does not frame as general promotion primitive.

### Adjacent Matches

**"Quiet Privilege Escalation" in Enterprise AI (Ganti, 2026)**
Medium/Hacker News. "The structural pattern by which AI agents inherit authority nobody explicitly granted them." "Configuration is not governance."
- Claims: 1
- Match: very close to unauthorized durability in access-control language. Not peer-reviewed.

**Acuvity, "Semantic Privilege Escalation" (2025-2026)**
Industry blog. AI agent operates within technical permissions but outside semantic scope of intended task. Escalation is semantic, not syntactic.
- Claims: 1, 3
- Match: structurally close — signal "permitted" at runtime but acquiring policy-level force without authorization.

**Anthropic, Claude Constitution / 4-Tier Priority Hierarchy (2026)**
Anthropic blog + arXiv:2212.08073 (original CAI, 2022). Four-tier priority: safety, ethics, compliance, helpfulness.
- Claims: 2
- Match: four-tier authority structure but governs output priority rather than state promotion. No write-barrier mechanism, no promotion ceremony. Constitution set at training time.

**Abiri, "Public Constitutional AI" (Georgia Law Review Vol 59, 2024)**
arXiv:2406.16696. Public participation in AI constitutions + "AI Courts" for case law. Constitutional/case-law distinction maps loosely onto constitutional vs policy tiers.
- Claims: 2, 5
- Match: legitimacy argument (constitution must derive authority from deliberation, not silent acquisition) resonates with promotion ceremony concept.

**"The Auton Framework" (2026)**
arXiv:2602.23720. "Constraint Manifold" — formally defined action-space subspace onto which agent policy projected before emission. Memory consolidation protocol.
- Claims: 2, 4
- Match: constraint manifold is effectively a write barrier. Cognitive blueprint / runtime separation parallels policy/runtime distinction.

**"AGENTSAFE" (2025)**
arXiv:2512.03180. Operationalizes AI Risk Repository into design, runtime, audit controls. Cryptographic tracing for provenance.
- Claims: 3, 4
- Match: three-phase structure loosely parallels promotion ceremony but lacks state-class framing.

**"Governance-as-a-Service (GaaS)" (2025)**
arXiv:2508.18765. Modular policy-driven enforcement layer. "Trust Factor" scoring agents based on compliance and severity-weighted violations.
- Claims: 2, 5
- Match: Trust Factor is dynamic version of tiered authority. Positions governance as infrastructure.

**"AgentGuardian" (2026)**
arXiv:2601.10440. Learns access control policies from controlled staging phase, enforces at runtime.
- Claims: 2, 4
- Match: staging phase (controlled observation → policy derivation) structurally similar to evaluation/attestation steps.

**"Moral Anchor System (MAS)" (2025)**
arXiv:2510.04073. Framework for detecting/predicting/mitigating "value drift" — when AI systems deviate from aligned values.
- Claims: 1
- Match: value drift is a special case of unauthorized durability — misaligned value acquires durable governing force. Lacks tier framework.

**"Policy Compiler for Agentic Systems (PCAS)" (2026)**
arXiv:2602.16708. Models agent state as dependency graph. Policies in Datalog-derived language. Reference monitor intercepts all actions before execution.
- Claims: 2, 4
- Match: reference monitor is effectively write barrier enforced at every tier.

**"Context Window Poisoning / XOXO" (2025)**
arXiv:2503.14281. Subtle code modifications preserve functional behavior but poison AI coding assistant's context.
- Claims: 1
- Match: unauthorized durability at attention/meaning tier — signal in environment silently acquires governing force over output.

**Microsoft Tiered Administration Model (established)**
Microsoft Learn. Three-tier model (Tier 0: identity, Tier 1: servers, Tier 2: workstations) with strict credential-crossing prevention.
- Claims: 2
- Match: classic IT precedent for tiered authority with write barriers. Applied to infrastructure rather than adaptive system state.

**Stafford Beer, Viable System Model (1972)**
"Brain of the Firm." Five interacting subsystems with recursive self-similarity — same governance structure at every level.
- Claims: 2, 5
- Match: recursive property parallels "no exempt layer" claim. Lacks write-barrier and promotion-ceremony concepts.

**"Normfare: Norm Entrepreneurship in Internet Governance" (2021)**
ScienceDirect. How actors develop norms of different character as governance moves. Norm entrepreneurship = informal practices acquiring durable institutional force.
- Claims: 1
- Match: unauthorized durability in political science register. Different vocabulary, same structural pattern.

**Regulatory Capture (Tobin Project, ongoing)**
Classic institutional instance — special interest preferences (transient lobbying signals) acquire durable governing force (agency policy).
- Claims: 1
- Match: well-established literature, not formalized in state-class framework.

## Notes
- No published work uses "unauthorized durability" as a named concept
- No work defines the specific four state classes mapped to four authority tiers
- No work specifies six invariants with five write barriers
- No work proposes the five-step promotion ceremony as a composable governance primitive
- BUT: the problem space is far more crowded than expected, with rapid convergence from three directions:
  1. **AI agent security** (2025-2026): tiered privilege control with write barriers (PFI, SEAgent, Progent, AgentGuardian, PCAS)
  2. **AI governance architecture** (2025-2026): layered governance with audit requirements (LGA, AGENTSAFE, Auton, GaaS, Controllability Trap, Verifiability-First)
  3. **Loss of control / drift** (2025-2026): gradual acquisition of unauthorized durable force (Loss of Control Playbook, MAS, AI Identity Drift)
- The Promptware Kill Chain's explicit "Persistence" stage is the closest independent formulation

## Verdict
**Alone in synthesis, converged in components.** The components are well-supported by independent work across AI security, governance architecture, and institutional theory. The specific integration — unauthorized durability as a named primitive, four-tier state ontology, promotion ceremony as composable governance — is novel. The paper should cite: Promptware Kill Chain, PFI, SEAgent/Progent, Controllability Trap, and Loss of Control Playbook as strongest independent convergences.
