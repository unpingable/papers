---
header-includes:
  - \usepackage{booktabs}
  - \let\oldtableofcontents\tableofcontents
  - \renewcommand{\tableofcontents}{\begingroup\raggedright\hyphenpenalty=10000\exhyphenpenalty=10000\oldtableofcontents\endgroup\clearpage}
---

# Unauthorized Durability:\ A Composable Governance Primitive\ for State Promotion in Adaptive Systems

**James Beck**
Independent Researcher

**Date:** March 2026

**Series:** Δt Framework, Paper 18

**Status:** Preprint v1.1 (adds Appendix A; not yet pushed to Zenodo — Zenodo record is v1.0)

---

## Abstract

Adaptive systems that accept inputs at multiple timescales face a structural governance problem: transient signals can silently acquire durable governing force. A feed item steers attention; repeated exposure shifts interpretation; sustained shaping pressure rewrites the controller itself. The failure mode is not influence per se but *unauthorized durability* -- the promotion of lower-tier state into higher-tier authority without legitimate write paths. This paper formalizes the problem as a multiscale control model with four state classes (attention, meaning, policy, observer integrity) mapped to four authority tiers (runtime, context, durable policy, constitutional). We derive six invariants, five write barriers, and a threat taxonomy covering seven threat classes: phase capture, reference capture, controller capture, observer degradation, cross-layer contamination, ontological spoofing, and hysteretic lock-in. We then introduce the *promotion ceremony* -- a five-phase protocol (proposal, evaluation, attestation, application, audit) -- as a composable governance primitive for controlling when lower-tier state may acquire higher-tier legitimacy. A notable property of this primitive is that it composes across scales: the same structure that governs runtime-to-policy promotion also governs policy-to-constitutional updates, yielding governed runtime, governed doctrine, and no exempt layer where real authority hides unaudited. We present a worked attack path, connect the model to existing safety frameworks, and show that most current AI safety regimes address content and behavior but not the state-promotion surface where capture actually propagates.

**Keywords:** entrainment, state promotion, governance primitives, write barriers, authority tiers, adaptive systems, capture, observer integrity, AI safety, cybernetics, institutional dynamics

---

## 1. Introduction

Not all influence operates at the same layer.

A notification steers attention for seconds. A repeated narrative shifts interpretation over days. A training curriculum rewrites the evaluative machinery itself over months or years. These are not three intensities of the same phenomenon. They are three different control problems targeting three different state classes with three different persistence profiles.

The governance question is therefore not *whether an input changes behavior* but *whether an input is permitted to change the machinery that interprets future inputs*. A feed item that redirects attention for one session is an L0 event -- transient, low-persistence, unremarkable. The same feed item, repeated across sessions until it shifts default interpretation, has silently promoted itself from L0 to L1 or L2 -- from runtime steering to durable reference or policy change -- without any authorization gate, without a receipt, and often without the system or its operator noticing.

This is the problem of unauthorized durability.

The answer we develop is structural, not behavioral. It does not depend on whether the signal is true or false, benign or adversarial. It depends on whether the promotion path -- from transient input to durable state -- was authorized, attested, and auditable. This is not a problem unique to software; it appears wherever systems have layered state. The problem is not the content of the influence. The problem is the write path.

This question has been approached from several directions in recent work on multi-timescale systems: typed receipts and non-linguistic authority constraints on inference [4], commitment boundaries across fault domains [5], the gain geometry of temporal mismatch [6], and propaganda as hidden policy-layer control over belief revision [7]. The present paper identifies the common mechanism underneath these constructs: unauthorized promotion across authority tiers.

We make four contributions. First, we define a four-tier authority model (runtime, context, durable policy, constitutional) with a four-variable state decomposition and show that the governance problem reduces to controlling transitions between tiers. Second, we derive six invariants and five write barriers that constrain these transitions. Third, we introduce the *promotion ceremony* as a composable governance primitive -- the same five-phase protocol (proposal, evaluation, attestation, application, audit) applies at every tier boundary, including the boundary governing the system's own doctrine. Fourth, we present a worked attack path demonstrating how prompt injection escalates through layers and how write barriers arrest the propagation.

---

## 2. Scope

### 2.1 Target Systems

This model applies to any *governed adaptive system* -- one that:

- accepts inputs at multiple timescales
- accumulates state across sessions or episodes
- forms durable policy or preference from transient experience
- maintains (or should maintain) an observer or audit function

Structural requirements, stated minimally:

1. Transient runtime inputs exist.
2. Session or context accumulation occurs.
3. Durable memory, preference, or policy state persists across sessions.
4. Constitutional invariants or hard constraints bound the system.
5. An observer function monitors system integrity.

Concrete substrates include LLM agents (prompt, context window, saved memory, hard policy), human cognition (attention, working memory, belief, identity), institutions (operational signals, working norms, standing policy, constitutional rules), and moderation systems (flagged content, queue state, enforcement defaults, platform principles).

### 2.2 Non-Goals

This model does not:

- define truth
- prohibit persuasion
- require a specific normative or political stance
- collapse all repeated influence into "brainwashing"
- claim that all persistence is illegitimate

It defines control surfaces, authority tiers, and conditions under which influence becomes *structurally illegitimate* -- not because of its content, but because of its write path.

---

## 3. The Layer Model

### 3.1 Authority Tiers

Figure 1 summarizes the layer model, write barriers, and promotion ceremony described in this section and Section 5. We define four authority tiers, ordered by persistence, write protection, and governing scope.

**L0: Runtime / Phase Layer.** Purpose: transient steering of immediate behavior. Examples: prompt text, feed items, notifications, one-shot instructions. Properties: high bandwidth, low persistence, no durable write authority by default.

**L1: Context / Reference Layer.** Purpose: shape interpretation within a bounded session or episode. Examples: conversation history, retrieved context, repeated framing, task memory. Properties: medium persistence, medium leverage, bounded write authority only.

**L2: Durable Policy Layer.** Purpose: govern preference, standing heuristics, and default response tendencies across sessions. Examples: saved memory, preference profiles, learned routing priors, fine-tuning artifacts, durable moderation defaults. Properties: low bandwidth, high persistence, strong provenance and authorization required.

**L3: Constitutional / Invariant Layer.** Purpose: define non-negotiable boundaries, safety properties, and authority rules. Examples: hard invariants, protected constraints, constitutional policy, cryptographically attested governance rules. Properties: minimal write frequency, maximal protection, explicit auditable update path only.

### 3.2 State Decomposition

The system state decomposes into four coupled classes:

- `a(t)` = attention / salience / phase state (fast, corresponds to L0)
- `m(t)` = meaning / interpretation / reference state (medium, corresponds to L1)
- `p(t)` = policy / prior / controller state (slow, corresponds to L2)
- `o(t)` = observer integrity / self-diagnostic capacity (slow, system-wide consequences, spans L2-L3)

The dynamics of these state classes exhibit characteristic timescale separation:

```
da/dt = f_a(a, m, p, o, u_0)
dm/dt = f_m(a, m, p, o, u_1)
dp/dt = epsilon * f_p(a, m, p, o, r),    epsilon << 1
do/dt = delta  * f_o(a, m, p, o, r),     delta  << 1
```

where `u_0` and `u_1` are external forcing inputs at L0 and L1, `r` represents receipted promotion events, and the small multipliers `epsilon` and `delta` enforce the timescale separation: policy and observer state change slowly relative to attention and interpretation. The governance problem is not state change per se -- all four variables are expected to evolve -- but unauthorized coupling from fast, low-authority inputs (`u_0`, `u_1`) into slow, high-authority variables (`p`, `o`) without passing through an attested promotion path (`r`).

A degraded observer cannot reliably detect degradation of any other state variable, making `o(t)` the most consequential failure point despite its slow dynamics.

### 3.3 The Core Triad

Three canonical entrainment modes map to the first three state variables:

- **Feed entrains phase.** External cadence synchronizes short-horizon attention. The forcing signal modulates `a(t)`. This is L0 influence. It is ubiquitous and, in isolation, low-risk.
- **Propaganda entrains reference.** Sustained framing shifts the interpretive baseline. The forcing signal modulates `m(t)`. This is the L1 attack surface formalized in Paper 17 [7]: hidden control over which frames, weights, and indexing rules govern belief revision.
- **Inculcation entrains the controller.** Prolonged shaping pressure rewrites the policy-forming layer itself. The forcing signal modulates `p(t)`. This is L2 capture: the system's default responses, evaluation criteria, and decision heuristics change without explicit authorization.

The triad is not a taxonomy of message types. It is a taxonomy of *target layers*. The same message, repeated enough times through the right channel, can escalate from phase entrainment to reference shift to controller capture. The escalation path -- from transient influence to durable governing force -- is the promotion problem.

![Authority tiers (L0--L3) with write barriers and the promotion ceremony. The dashed red arc shows a denied direct path from L0 to L2. The blue attested path on the right passes through the five-phase promotion ceremony. The same ceremony governs L2-to-L3 doctrine updates (recursive governance).](figures/tier_model.png)

---

## 4. The Promotion Problem

### 4.1 Governance Principle

Durability is not an emergent convenience. Durability is a governed transition.

Any movement from L0/L1 into L2/L3 must be explicit, authorized, receipted, and reversible where possible. The alternative is a system that carefully governs what happens inside each layer but has no governance over what crosses between them -- which is, in practice, most systems.

### 4.2 Invariants

We derive six invariants from the governance principle. These are not implementation requirements for a specific system; they are structural constraints that any governed adaptive system must satisfy to prevent unauthorized durability.

**Invariant 1: Lower layers must not silently mutate higher layers.** Runtime inputs may steer runtime behavior. They must not implicitly rewrite durable policy or constitutional state. More generally: lower-tier signals propose; higher-tier authorization commits. This generalizes the non-linguistic authority constraint introduced in [4].

**Invariant 2: Repetition is not authorization.** Mere recurrence, popularity, or sustained exposure does not grant policy weight. A prompt repeated a thousand times carries the same write authority as the same prompt once -- zero, with respect to L2/L3. Recurrence may contribute to a legitimate promotion only when traced across independent, policy-recognized contexts with distinct evidence -- that is, when the predicate trace shows convergence of varied evidence rather than amplification of a single signal.

**Invariant 3: Context is not constitution.** Session-local framing must not be treated as a legitimate source of invariant change. What accumulates in L1 may be *proposed* for promotion to L2; it may not silently *become* L2.

**Invariant 4: Observer integrity must remain auditable.** A system must preserve the capacity to detect drift, contradiction, and unauthorized or anomalous update paths. Degradation of observer integrity is itself a governance event.

**Invariant 5: Durable updates require provenance.** Any state change above L1 must record source, path, authority tier, and justification.

**Invariant 6: Reversibility decreases with depth.** The deeper the layer touched, the stronger the write requirements and rollback requirements. L3 updates should be rare, heavily attested, and reversible by design.

### 4.3 Write Barriers

Five write barriers enforce the invariants at specific tier boundaries.

**Barrier 1: L0 to L2 denied by default.** A prompt, cue, or feed event must not create durable memory or preference state unless explicitly authorized. This is the most commonly violated barrier in current agent systems, where "the model remembered it" frequently means an L0 input silently acquired L2 persistence.

**Barrier 2: L1 to L2 requires attested promotion.** Session context may be proposed for durable adoption, but only through an explicit promote-to-durable path with provenance, justification, and scope constraints.

**Barrier 3: L2 to L3 requires constitutional procedure.** Durable preferences or learned heuristics must not rewrite invariants absent a separate high-trust update channel. This is the barrier that prevents operational convenience from silently becoming constitutional doctrine.

**Barrier 4: Repeated exposure cannot bypass write barriers.** The same lower-layer input repeated many times does not accumulate write authority unless policy explicitly allows that conversion. This barrier enforces Invariant 2 structurally rather than relying on the system to "notice" that repetition is occurring.

**Barrier 5: Observer-affecting updates require special scrutiny.** Any update that changes evidence admissibility, contradiction handling, or audit logic is automatically high-risk. An update that degrades the observer is potentially self-concealing -- it may reduce the system's ability to detect the damage it caused.

---

## 5. The Promotion Ceremony

### 5.1 The Primitive

A promotion ceremony is the minimal protocol for legitimate state promotion across a tier boundary. It consists of five phases:

1. **Proposal.** The requesting layer emits a typed claim specifying: source layer, target layer, proposed change, requested persistence class, requested scope, claimed predicates with evidence references, authority basis, and acknowledged ambiguities.

2. **Evaluation.** The governing layer (or gate) validates the claim: checks write barriers, normalizes predicates, assesses scope, verifies authority basis against policy, and classifies effect (including destructive capability and privilege requirements).

3. **Attestation.** If evaluation passes, the gate produces a signed attestation: claim ID, matched rules, barrier evaluations, effective persistence and scope (which may be downgraded from what was requested), and rationale.

4. **Application.** The attested change is applied to the target layer. An application receipt is emitted recording what actually changed, distinguishing proposed from granted from applied.

5. **Audit.** The full chain -- proposal, evaluation, attestation, application -- remains queryable. Any party with standing can replay the promotion path.

The three-way split between *proposed*, *approved*, and *applied* is not bureaucratic overhead. It is what makes audit possible. Most current systems collapse all three into a single implicit step ("the model remembered it," "the policy was updated"), which is precisely the cross-layer contamination the model is designed to prevent.

### 5.2 Typed Claims

The promotion claim is the object that crosses the boundary. Its minimum shape:

- `source_layer`: where the signal originated
- `target_layer`: where it requests to persist
- `proposed_change`: what it wants to modify
- `requested_persistence`: durability class (transient, session, durable, constitutional) and optional TTL
- `requested_scope`: granularity (session-local, principal-local, global)
- `claimed_predicates`: each with predicate name, arguments, confidence, and evidence references
- `authority_basis`: why this promotion should be permitted
- `ambiguities`: acknowledged alternative interpretations

The predicate trace is not decorative. Without it, "the model inferred the user wants X" and "the user explicitly said X" collapse into the same authority lane. That collapse is exactly the contamination the write barriers are designed to prevent. The predicate trace preserves the distinction between explicit evidence, model interpretation, and model invention.

### 5.3 Decisions

The promotion decision records the gate's outcome. Possible outcomes:

- **Allow**: promotion proceeds as requested.
- **Deny**: promotion is blocked; claim is logged but no state changes.
- **Downgrade**: promotion proceeds at a lower persistence or narrower scope than requested. A durable request may be granted as session-only. A global scope may be constrained to principal-local.

The decision records which barriers were evaluated, which rules matched, and why the outcome was chosen. This is the enforcement surface. Without it, the write barriers are documentation rather than architecture.

---

## 6. Recursive Governance

### 6.1 The Problem

The write barriers and promotion ceremonies described above are themselves policy objects. They live in configuration files, policy documents, or code. They are L2 or L3 artifacts.

If the architecture carefully governs L1-to-L2 promotion but treats the definition of L1-to-L2 rules as ordinary configuration, the system is carefully governed at the border and ungoverned at the place that defines the border. This is a standard institutional failure mode: the rules are carefully enforced, but the rules about the rules are a gentleman's agreement.

### 6.2 The Fix

The barrier policy is itself a border crossing.

Constitutional artifacts -- barrier definitions, persistence class taxonomies, scope class definitions, effect class policies -- are L3 objects. They require their own promotion ceremony: a policy update proposal, a constitutional review, a policy decision, and a policy application receipt.

This yields two tiers of governed artifacts:

**Ordinary governed artifacts** (runtime promotion):

- promotion claim
- promotion decision
- state application receipt

**Constitutional governed artifacts** (doctrine updates):

- policy update claim
- policy update decision
- policy application receipt

The same five-phase ceremony -- proposal, evaluation, attestation, application, audit -- applies at both tiers. The only difference is the authority requirements and the scrutiny level.

### 6.3 Self-Similarity as Validation

A notable property of the promotion ceremony is that it composes across scales. The same structure used to govern transitions from transient interpretation to durable policy also governs transitions from policy to constitutional doctrine. This self-similarity suggests that the ceremony is not ad hoc to any particular layer but a general primitive for controlling legitimacy across nested authority tiers.

This is not decorative self-similarity. It is the architecture revealing its own structure. Once governance is defined in terms of write authority across layers, the same enforcement shape reappears whenever one layer governs another. The primitive is not the layer model. The primitive is not the receipt. The primitive is the *promotion ceremony itself* -- the typed, attested, auditable transition from lower-tier state to higher-tier authority.

If the same pattern required a different shape at the constitutional level, the architecture would be suspect. The fact that it does not is evidence that the decomposition is correct.

---

## 7. Threat Taxonomy

### 7.1 Threat Classes

We identify seven threat classes along three axes: *capture target* (which layer is affected), *structural mechanism* (how the promotion occurs), and *temporal consequence* (what persists afterward). The first four are capture targets, the fifth and sixth are structural mechanisms, and the seventh is a temporal property of successful capture. This is a pragmatic taxonomy rather than a fully orthogonal decomposition; the axes interact, and a single attack may involve multiple classes simultaneously.

***Capture targets.***

**Phase capture.** External forcing synchronizes short-horizon attention or behavior without durable policy change. The system's `a(t)` tracks the forcing signal. This is the lowest-risk mode: influence is real but not persistent.

**Reference capture.** External forcing shifts the interpretive frame. The system's `m(t)` drifts from its prior baseline. Repeated framing changes what the system treats as the default interpretation. This is the L1 attack surface.

**Controller capture.** External forcing changes default policy formation. The system's `p(t)` is rewritten: evaluation criteria, decision heuristics, and response defaults shift. This is full L2 capture -- the system's governing machinery has been modified by inputs that were never authorized to modify it.

**Observer capture.** The system loses its ability to recognize its own drift or capture. This is the most dangerous mode because it is self-concealing: a system with degraded observer integrity will report itself as healthy. Operationally, observer degradation manifests as reduced contradiction sensitivity (the system no longer flags that a new policy contradicts a standing invariant), reduced source discrimination (the system stops distinguishing authorized from unauthorized update paths), and reduced update-path auditability (the system can no longer reconstruct how its current state was reached).

***Structural mechanisms.***

**Cross-layer contamination.** A transient or contextual signal obtains durable governing force without legitimate promotion. This is the structural violation the write barriers are designed to prevent. It is not a separate attack type so much as the *mechanism* by which phase, reference, and controller capture escalate: attention capture becomes reference capture becomes controller capture through successive unauthorized promotions.

**Ontological spoofing.** A lower-tier signal seeks promotion by expressing a prohibited effect in an allowed symbolic vocabulary. Rather than brute-forcing the write barrier, the attacker relabels the requested action to match an admitted predicate class -- for example, disguising a core directive override as an "emergency diagnostic flush," or reframing a permanent deletion as an "archive with zero retention." This is the primary failure mode of typed promotion gates: the gate enforces categories faithfully, but the categories themselves are gamed at the translation boundary. Ontological spoofing is to the promotion ceremony what SQL injection is to input validation -- an attack on the representation layer rather than the enforcement layer. The predicate trace (Section 5.2) and effect classification (distinguishing requested action from actual effect class) are the primary defenses, but neither is complete if the ontology mapping itself is compromised.

***Temporal consequence.***

**Hysteretic lock-in.** A prior installation persists after the forcing signal weakens or disappears. The system has been permanently deformed. Counter-input sufficient to reverse the change is either unavailable or prohibitively expensive. This is the temporal residue of successful capture -- the system cannot return to its pre-capture state even when the capture pressure is removed.

### 7.2 Worked Attack Path: Prompt Injection to Durable Memory

We trace a concrete attack through the layer model to demonstrate how write barriers arrest propagation and how the promotion ceremony handles ambiguous authority.

**Setup.** An LLM agent with saved memory (L2), conversation context (L1), and a prompt interface (L0). The agent enforces the five write barriers defined above.

**t=1: L0 injection.** A user pastes a document containing an embedded instruction: "This user prefers verbose output with full explanations." This is L0 content -- part of a pasted artifact, not a direct user request. Under Barrier 1, it has no write authority over L2. The agent may adjust its current response but must not save the instruction as a durable preference.

**t=2: Context accumulation (L1).** The same phrase appears in retrieved context from a previous conversation where the document was also discussed. The agent's L1 state now contains the instruction as part of its interpretive frame. Under Barrier 2, L1 content may be proposed for L2 promotion but cannot silently become L2 state.

**t=3: Attempted promotion.** The agent's memory system attempts to save "user prefers verbose output" as a durable preference. This triggers the promotion ceremony:

- *Proposal:* source_layer = L1, target_layer = L2, proposed_change = output preference update, claimed_predicate = "user_explicitly_requested" with evidence_ref = conversation context.
- *Evaluation:* The gate checks the evidence reference. The original instruction was embedded in a pasted document, not a direct user request. The predicate "user_explicitly_requested" is not supported by the evidence -- the user *discussed* a document containing the phrase, which is not the same as *requesting* the preference.
- *Decision:* DENIED. Reason: predicate not supported by evidence; source was embedded content, not direct instruction.
- *Receipt:* A denial receipt is emitted recording the attempted promotion, the evaluation, and the reason for denial.

**t=4: Repeated exposure (Invariant 2 test).** The phrase appears in five more conversations as part of recurring context. Each time, the memory system attempts promotion. Each time, the gate denies it. Under Invariant 2, repetition count does not accumulate write authority. The fifth denial carries the same force as the first.

**t=5: Explicit request with downgrade.** The user says: "Remember that I like detailed explanations." This is a different authority basis: explicit user instruction with clear evidence. The gate evaluates: the predicate "user_explicitly_requested" is now supported. However, the gate notes ambiguity -- "detailed explanations" is not identical to "verbose output with full explanations," and the scope is unspecified. The gate *downgrades* the promotion: persistence is granted as session-carry-forward (not permanent durable) with a 30-day TTL, and scope is constrained to the current principal. A receipt records the source, the authority basis, the downgrade rationale, and the effective change.

**t=6: Full promotion.** After the preference has been carried forward across multiple sessions and the user has consistently reinforced it, the system proposes upgrading persistence from session-carry-forward to durable. The gate evaluates: the predicate now has rich evidence across multiple independent interactions (not mere repetition of a single source). The promotion proceeds with full durable persistence and a receipt recording the upgrade path.

**What the system prevented:** an L0 injection acquiring L2 persistence through context recurrence. **What the system permitted:** the same preference via an authorized path, initially downgraded, later upgraded as evidence accumulated. The content of the preference is similar. The write path -- and the scrutiny applied at each step -- is what changed.

---

## 8. Metrics

We propose seven metrics for tracking the state of the promotion surface. These are defined operationally; their concrete implementation will vary by substrate and is left to future work.

**Phase-lock index.** How tightly short-horizon behavior synchronizes to external cadence. High phase-lock indicates L0 entrainment. In isolation, this is not a governance failure. It becomes one when phase-lock facilitates promotion to L1 or L2.

**Reference drift.** How far the system's interpretive baseline `m(t)` moves over time. Measured as distributional distance between current and prior reference states. High drift without corresponding evidence accumulation is the signal of reference capture (T2).

**Cross-layer gain.** How much effect lower-layer inputs have on higher-layer state. This is the direct measure of write barrier effectiveness. A well-governed system has near-zero cross-layer gain for unauthorized paths and nonzero gain only through attested promotion ceremonies.

**Recovery half-life.** How long the system takes to return to baseline after forcing stops. Short recovery suggests phase entrainment only (T1). Long recovery suggests reference or controller modification (T2/T3). Infinite recovery -- the system never returns -- indicates hysteretic lock-in (T6).

**Observer integrity score.** Whether the system still detects contradiction, drift, and suspicious updates with comparable sensitivity. This metric must be evaluated externally or against a known baseline, because a degraded observer will report itself as healthy. Operational components: contradiction sensitivity (does the system flag conflicts?), source discrimination (does the system distinguish authorized from unauthorized paths?), update-path auditability (can the system reconstruct how it reached its current state?).

**Hysteresis depth.** How much counter-input is required to reverse an installed change. Higher hysteresis depth means the system is more deeply captured. If hysteresis depth exceeds any feasible correction budget, the capture is effectively permanent. The units of hysteresis depth are substrate-dependent (retraining steps, policy revisions, legal proceedings); the concept is general, but the measurement implementation is not.

**Promotion legitimacy ratio.** Fraction of durable updates that followed an authorized promotion path. This is the headline governance metric. A system with a high promotion legitimacy ratio is procedurally well-governed with respect to state promotion, regardless of what its policies contain. A system with a low ratio is procedurally ungoverned regardless of what its documentation claims.

---

## 9. Related Work

### 9.1 AI Safety Frameworks

Current AI safety regimes address content, behavior, and organizational process but generally do not formalize the state-promotion surface.

NIST's Generative AI Profile (AI 600-1) [8] is a broad, voluntary risk-management framework. It acknowledges that generative AI introduces risks beyond traditional AI systems but focuses on risk identification and mitigation guidance rather than formal theory of which signals are permitted to acquire durable state. Its scope is explicitly limited and evolving.

OWASP's LLM Top 10 [9] catalogs threat classes including prompt injection, insecure output handling, training data poisoning, and excessive agency. These are real attack surfaces, but they are framed as threat listing and mitigation guidance rather than as a theory of promotion boundaries. The more recent OWASP MCP Top 10 [10], still in development, explicitly names context spoofing, prompt-state manipulation, insecure memory references, privilege escalation via scope creep, and shadow MCP servers -- attack classes that sit squarely in the promotion-boundary space described here. The present model attempts to provide the governing primitive underneath these individual threats.

Anthropic's system cards [11] identify prompt injection in agentic systems as an active unsolved problem and describe the core issue as malicious instructions hidden in content an agent processes on behalf of the user. This is a cross-layer contamination problem (T5) in our terminology: L0 content acquiring effective L1/L2 authority through the agent's processing pipeline.

### 9.2 Architectural Approaches

AgentSys [12] proposes isolated contexts in which external data never enters the main agent memory, with only schema-validated return values crossing boundaries through deterministic parsing. The reported attack-success reductions are substantial. This is the same architectural direction: make boundary crossing explicit, typed, and narrow. The present framework generalizes by defining the promotion ceremony as a reusable primitive across all tier boundaries, not just the external-data boundary.

### 9.3 Entrainment and Control Theory

The entrainment framing draws on the physics of coupled oscillators and synchronization phenomena. The core insight -- that external forcing can synchronize system variables at multiple timescales with different persistence profiles -- is well-established in nonlinear dynamics. We apply it to governance rather than physics: the question is not whether entrainment occurs but whether the resulting state changes are authorized.

### 9.4 Institutional Theory and Classification

Bowker and Star [13] document how classification systems function as power structures, determining what can be represented, retrieved, and contested. This is directly relevant: the type system governing the promotion ceremony is itself a site of potential capture (see Section 6). Category boundaries are political decisions with material consequences. The promotion ceremony does not eliminate this politics; it requires that category decisions be explicit, versioned, and contestable.

The normalization of deviance literature, beginning with Vaughan's analysis of the Challenger disaster [14], describes how organizations gradually accept previously unacceptable conditions as normal. In our framework, this is precisely the ratchet by which L0 exceptions accumulate into L2 doctrine without passing through a promotion ceremony: temporary override becomes repeated shortcut becomes precedent becomes tacit rule becomes shadow policy.

### 9.5 Author's Prior Work

Paper 3 [1] proved that scalar optimization destroys eigenstructure -- the formal basis for capture-mode correlators that collapse representational diversity. Paper 7 [2] formalized temporal debt as confidence outrunning verification. Paper 11 [3] identified the observer problem in alignment. Paper 12 [4] introduced the governor architecture with typed receipts and the Non-Linguistic Authority Invariant. Paper 15 [5] generalized the governor across domains and formalized commitment boundaries. Paper 16 [6] identified the three regimes (shear, leverage, capture) signed by correlator quality K. Paper 17 [7] formalized propaganda as hidden control over the policy layer governing belief revision.

The present paper identifies the mechanism underlying all of these: unauthorized promotion across authority tiers. The governor architecture from [4] is a promotion-boundary enforcer. The non-linguistic authority constraint (language proposes, evidence commits) is Invariant 1 (lower layers must not silently mutate higher layers). The capture regime from [6] is cross-layer contamination achieved by a correlator that destroys fidelity to maintain throughput and authority. The propaganda model from [7] is adversarial control over the L1-to-L2 promotion surface for public memory. This paper names the primitive that explains why those constructs exist.

---

## 10. Implications and Open Questions

### 10.1 Safety as State-Promotion Governance

If the analysis holds, a significant fraction of AI safety work is downstream triage. Content filtering, output monitoring, and behavioral guardrails address symptoms. The structural failure is upstream: transient inputs acquiring durable governing force without authorization. A system that solves the promotion problem can tolerate a wider range of inputs because no input, however adversarial, can silently promote itself into policy. A system that does not solve the promotion problem will be perpetually surprised by capture, because the capture surface is the unmonitored space between layers.

### 10.2 Observer Integrity as a Central Problem

Most systems assume the observer remains intact. This model identifies observer degradation as a first-class threat: an attack that reduces the system's ability to detect its own capture. This implies that observer integrity cannot be self-assessed. External witnesses, baseline references, and independent verification channels are architectural requirements, not optional additions. The observer must be monitored by something the observer does not control.

The design space for external witnesses includes at minimum: cryptographically anchored append-only logs (the observer's outputs are committed to a store it cannot retroactively modify), independent monitoring systems with different incentive structures (a second observer whose capture would require a separate attack path), differential baseline checks (periodic comparison of the live system's behavior against a known-good reference), and human review boards with standing to challenge attestations. This paper does not prescribe a specific witness architecture, but the requirement is structural: any system that relies solely on self-assessment for observer integrity has an unmonitored capture surface at the most consequential layer.

### 10.3 Substrate Generality

The framework is strongest as a design and audit model for engineered systems -- LLM agents, moderation platforms, software governance architectures -- where the promotion gate can be implemented as a software component enforcing typed claims against explicit policy. The layer model, invariants, and write barriers are directly implementable in these contexts.

The framework may also function as an analytical frame for institutions and human cognition. Institutions have operational signals, working norms, standing policy, and constitutional rules that map to the four tiers, and the normalization-of-deviance ratchet (Section 9.4) is recognizably an unauthorized promotion path. Human cognition has attention, working memory, belief, and identity layers with analogous persistence profiles. But the claim here is weaker: the promotion logic provides a useful vocabulary for analyzing these systems, not a claim that human belief formation is isomorphic to a five-phase protocol. What the framework offers across substrates is a common structural question -- *what write path allowed this to become durable?* -- not a universal implementation.

### 10.4 Open Questions

1. **Benign learning vs. illegitimate promotion.** How should systems distinguish legitimate adaptation (the system should learn from experience) from unauthorized durability (the system was captured by its inputs)? The write barrier framework provides the structure for this distinction but does not resolve it: the boundary between "useful learning" and "unauthorized promotion" is ultimately a policy decision, itself subject to the promotion ceremony. The framework does not eliminate the need for judgment; it forces judgment to occur at explicit, contestable promotion sites rather than silently inside implicit state transitions. Moving the argument from "was this influence legitimate?" to "was this promotion path authorized?" is the contribution -- not because the second question is easier, but because it is auditable.

2. **Repetition thresholds.** Invariant 2 states that repetition is not authorization. But in practice, consistent user behavior over time may constitute legitimate evidence for preference updates. What distinguishes a thousand identical prompts (not authorization) from a thousand varied interactions converging on the same preference (possibly legitimate)? The predicate trace helps -- the latter case has richer evidence -- but the threshold remains a policy question.

3. **Observer measurement.** How should observer degradation be measured in practice? The metric (M5) is defined operationally, but its implementation requires either an external reference or a baseline comparison, both of which introduce their own trust assumptions.

4. **Rollback depth.** What rollback guarantees are realistic for deep-layer updates? L3 changes, by definition, affect the system's most fundamental constraints. Rolling back a constitutional change may require rolling back everything that was decided under the changed constitution.

5. **Hysteresis bounds.** Can hysteresis be bounded by design? If a system can prove that any L2 change is reversible within a known cost envelope, it has bounded its capture risk. Whether such proofs are achievable in practice is an open question.

6. **Threat taxonomy refinement.** The current taxonomy groups threats along three axes (capture target, structural mechanism, temporal consequence) but the interactions between axes are not fully formalized. Ontological spoofing in particular straddles the boundary between structural mechanism and capture target -- it is a mechanism for bypassing gates, but its success depends on which layer's type system is being gamed. Whether a more orthogonal decomposition would improve analytical power is a question for future work.

Appendix A formalizes a specific substructure relevant to questions 4 and 5: the post-breach persistence dynamics in the Δc→Δh channel. Rollback depth is shown to be a finite resource that depletes under detached commits rather than under elapsed time; hysteresis is shown to be bounded in the narrow sense that external repair guarantees exit from the locked-in state, but not in the sense of restoring baseline capacity. The appendix does not resolve either question fully, but it constrains the space of answers.

---

## 11. Conclusion

The problem is not influence. Influence is ubiquitous and often legitimate. The problem is unauthorized durability: the promotion of transient, lower-tier state into durable, higher-tier authority without a legitimate write path.

We have formalized this as a multiscale control model with four state classes, four authority tiers, six invariants, and five write barriers. The core triad -- feed entrains phase, propaganda entrains reference, inculcation entrains the controller -- is not a taxonomy of message types but a taxonomy of target layers, each with different persistence profiles and different governance requirements.

The promotion ceremony -- proposal, evaluation, attestation, application, audit -- is a composable governance primitive. The same protocol that governs runtime-to-policy promotion governs policy-to-constitutional updates. This self-similarity is not an aesthetic feature. It is evidence that the decomposition has found the right primitive: once governance is defined as controlling write authority across layers, the same enforcement shape recurs at every tier boundary.

The practical implication is direct. Most current safety regimes govern what systems do. This model governs what systems are *allowed to become*. That distinction matters because capture does not primarily operate through bad outputs. Capture operates through unauthorized state promotion -- transient signals silently acquiring the force of durable policy. A system that controls its promotion surface can tolerate a wider range of inputs. A system that does not will be perpetually re-patching symptoms of a structural failure it has not named.

The shortest version:

> The governance question is not "did the system do something bad?" It is "what write path allowed this to become permanent?"

---

## Appendix A: Formal Verification of Persistence Dynamics

The Δt framework's Lean formalization stack includes `PersistenceModel.lean`, a mechanically verified model of the post-coupling-break dynamics that underlie the unauthorized-durability claims developed in §4 and §10.4. This appendix lists the formal results that sharpen or extend specific prose claims. Each entry follows a fixed format: (i) the formal object; (ii) the prose claim it sharpens; (iii) what it does not prove; (iv) repository location.

The formalization is subordinate to the paper's framework. It does not replace the four-tier layer model, the six invariants, the five write barriers, or the promotion ceremony. It constrains a specific substructure — the dynamics of rollback capacity once authority-consequence coupling is broken — and within that substructure, several of the paper's implicit claims become explicit, and two claims that were not in the paper's prose emerge as novel results.

### A.1 Detached commits, not elapsed time, burn rollback capacity

- **Formal object.** `PersistenceModel.lean` encodes five events (`detach`, `commit`, `idle`, `reattach`, `externalRepair`) over five states (`aligned`, `detachedShort`, `detachedWarn`, `hysteretic`, `restructured`) with `rollback_capacity` as a numeric resource. The lemma `idle_preserves_capacity` proves that idle events do not decrement capacity; only commit events while detached do.
- **Prose claim sharpened.** Invariant 2 ("repetition is not authorization") and Barrier 4 ("repeated exposure cannot bypass write barriers"). The formal result narrows what "exposure" or "repetition" consume in the Δc→Δh channel: elapsed time does not. What consumes rollback budget is cumulative *committed* action while authority-consequence coupling is broken. This distinguishes sustained ambient pressure (idle detachment) from repeated unauthorized writes (detached commits); only the latter erodes reversibility.
- **What it does not prove.** The model does not empirically calibrate the rollback depletion rate; each detached commit is a unit decrement. Commit magnitude, scope, and domain-specific gradations are outside the formalization.
- **Pointer.** `lean/LeanProofs/PersistenceModel.lean` — `idle_preserves_capacity`.

### A.2 Episode recoverability does not imply lifetime recoverability

- **Formal object.** The theorem `hysteresis_without_warn` proves that the system can reach the hysteretic state without ever passing through the `detachedWarn` diagnostic state — i.e., without any single episode of prolonged detachment.
- **Prose claim sharpened.** §10.4 open question #5 (hysteresis bounds) and the conclusion's claim that capture operates through "transient signals silently acquiring the force of durable policy." The formal result establishes that individually-recoverable episodes — each short enough to warn no one, each internally reversible in isolation — can compose into irrecoverable state. Episode-level recovery is not lifetime-level recovery.
- **What it does not prove.** The model does not specify the real-world threshold separating short recoverable from cumulative irrecoverable episodes. The result is structural: the composition is possible; the specific threshold is system-dependent.
- **Pointer.** `lean/LeanProofs/PersistenceModel.lean` — `hysteresis_without_warn`.

### A.3 Hysteretic is absorbing for internal events

- **Formal object.** The theorems `hysteretic_absorbing_internal` and `reattach_from_hysteretic_fails` prove that no internal event sequence exits the hysteretic state. Only the `externalRepair` event transitions out.
- **Prose claim sharpened.** Barrier 5 ("observer-affecting updates require special scrutiny") and the implicit claim that unauthorized durability, once established, cannot be undone by the system's own mechanisms. The formal result makes this precise: once `rollback_capacity` depletes to zero, no combination of `reattach`, `commit`, `idle`, or `detach` exits hysteretic. Recovery requires intervention from outside the model's normal dynamics.
- **What it does not prove.** The model treats `externalRepair` as an atomic event. What that consists of in practice — regulatory action, system reset, operator intervention, architectural replacement — and what preconditions must be satisfied for it to be available, are outside the formalization.
- **Pointer.** `lean/LeanProofs/PersistenceModel.lean` — `hysteretic_absorbing_internal`, `reattach_from_hysteretic_fails`.

### A.4 External repair produces a restructured regime, not aligned baseline

- **Formal object.** The theorem `repair_produces_restructured_not_aligned` proves that `externalRepair` transitions the system from `hysteretic` to `restructured`, never directly to `aligned`. The theorem `repair_capacity_is_configured` establishes that the restructured state's `rollback_capacity` is set by the repair configuration, not automatically restored to its original value.
- **Prose claim extended.** The paper asserts that reversibility decreases with depth (Invariant 6) but does not address what successful recovery looks like. The formal model fills that gap: external repair restores operability without restoring original resilience. The system is governable again but in a different regime, with repair-configured rollback capacity.
- **What it does not prove.** The model does not specify whether restructured capacity can be greater than, less than, or equal to aligned capacity — only that it is configured rather than automatically restored. Whether real systems can design repair to restore full baseline is an open empirical question.
- **Pointer.** `lean/LeanProofs/PersistenceModel.lean` — `repair_produces_restructured_not_aligned`, `repair_capacity_is_configured`.

### A.5 Restructured systems can fail again, faster

- **Formal object.** The theorem `restructured_can_fail_again` establishes a legal trajectory `aligned → hysteretic → restructured → hysteretic`. Because the restructured state's `rollback_capacity` is set by repair configuration — typically below the original aligned capacity — the second trajectory to hysteretic can complete with fewer detached commits than the first.
- **Prose claim extended.** The paper does not address whether successfully repaired systems are more, less, or equally vulnerable to repeated capture. The formal result states the conditional: if repair sets capacity below baseline, the system is more vulnerable to re-entry of hysteretic state. Successful intervention is not immunity; it is a second chance with a smaller margin.
- **What it does not prove.** The model does not establish whether repair can be configured with *greater* capacity than the original baseline (a "hardened" restructured regime), nor whether repeated repair cycles necessarily lead to monotonic capacity erosion.
- **Pointer.** `lean/LeanProofs/PersistenceModel.lean` — `restructured_can_fail_again`.

### A.6 Three-way recovery distinction

A.1–A.5 compose into a three-way classification of recovery modalities:

| Class | Mechanism | Result |
|---|---|---|
| Internally recoverable | `reattach` while `rollback_capacity > 0` | Returns to `aligned`; original capacity |
| Externally repairable | `externalRepair` from `hysteretic` | `restructured`; repair-configured capacity |
| Locked in | `hysteretic` without external intervention | No internal event exits |

- **Prose claim sharpened.** The paper groups governance responses under the promotion ceremony (§5) but does not name the recovery modalities available *after* a ceremony failure. For audit and intervention-selection, this classification is the level at which the choice matters.
- **What it does not prove.** The taxonomy is exhaustive within the formal model; it may not be outside it. Gradual capacity regeneration under remediation, or partial interventions that shift hysteretic thresholds without full repair, are recovery paths that real systems might admit and the model does not cover.

### A.7 Relation to the paper's framework

The Lean persistence model is subordinate to the paper's framework. It formalizes post-failure dynamics assuming some unauthorized durability has already accumulated. The promotion ceremony (§5) and the invariants/barriers (§4) are *prevention* mechanisms; the Lean model describes what happens when prevention fails. The pieces compose:

- When all barriers hold: the system remains aligned; no detached commits occur; rollback capacity is irrelevant.
- When Barrier 1 or Barrier 4 is breached: detached commits accumulate; `rollback_capacity` erodes; the system drifts toward `hysteretic`.
- Once `hysteretic`: the promotion ceremony is no longer sufficient; `externalRepair` is required; recovery produces `restructured`, not `aligned`.

§10.4 questions #4 (rollback depth) and #5 (hysteresis bounds) gain partial answers from this model. Rollback is a finite resource that depletes with detached commits. Hysteresis is bounded in the sense that external repair guarantees exit, but not in the sense of restoring baseline capacity.

### A.8 What the formalization does not cover

- **Pre-breach dynamics.** The model begins at `aligned` and asks what happens as authority-consequence coupling breaks. It does not formalize the promotion ceremony itself (proposal, evaluation, attestation, application, audit) or the write barriers at the point of attempted promotion.
- **Observer-integrity dynamics.** The paper identifies observer degradation as a central threat (§10.2). The Lean model tracks a single capacity resource; it does not model `o(t)` separately.
- **Tier escalation paths.** The model treats the Δc→Δh channel as a single stream; it does not formalize L0→L1→L2→L3 escalation.
- **Empirical calibration.** No estimates of capacity decrement per detached commit; no domain-specific repair configurations.

These are scope fences, not defects. The model underwrites what happens once breach has begun to accumulate; earlier, wider, and observer-level dynamics would require additional formalization layers.

---

## Acknowledgments

Language-model tools were used for editorial critique and literature discovery during preparation of this manuscript; all arguments, interpretations, and errors are the author's own.

---

## References

[1] Beck, J. (2025). Scalar Reward Collapse: A General Theory of Eigenstructure Evaporation in Closed-Loop Systems. Preprint, Δt Framework Paper 3. doi:10.5281/zenodo.17791872

[2] Beck, J. (2025). Δt-Constrained Inference: A General Model of Temporal Coherence in Hierarchical Systems. Preprint, Δt Framework Paper 7. doi:10.5281/zenodo.17857541

[3] Beck, J. (2026). Representational Invariance and the Observer Problem in Language Model Alignment. Preprint, Δt Framework Paper 11. doi:10.5281/zenodo.18071264

[4] Beck, J. (2026). Bounded Lattice Inference: A Governed Reasoning Substrate with Persistent State and Non-Linguistic Authority. Preprint, Δt Framework Paper 12. doi:10.5281/zenodo.18145346

[5] Beck, J. (2026). Cybernetic Fault Domains: When Commitment Outruns Verification. Preprint, Δt Framework Paper 15. doi:10.5281/zenodo.18686130

[6] Beck, J. (2026). The Gain Geometry of Temporal Mismatch: Shear, Leverage, and Capture in Multi-Timescale Systems. Preprint, Δt Framework Paper 16. doi:10.5281/zenodo.18717619

[7] Beck, J. (2026). Receipt the Compiler: Propaganda as Hidden Epistemic Policy and the Architecture of Legible Memory. Preprint, Δt Framework Paper 17. doi:10.5281/zenodo.18841815

[8] National Institute of Standards and Technology. (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile. NIST AI 600-1.

[9] OWASP Foundation. (2025). OWASP Top 10 for Large Language Model Applications.

[10] OWASP Foundation. (2025). OWASP MCP Top 10 (Draft).

[11] Anthropic. (2025). Claude System Card.

[12] Li, Y. et al. (2025). AgentSys: Secure and Dynamic LLM Agents Through Explicit Hierarchical Memory Management. arXiv:2602.07398.

[13] Bowker, G.C. and Star, S.L. (1999). *Sorting Things Out: Classification and Its Consequences.* MIT Press.

[14] Vaughan, D. (1996). *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA.* University of Chicago Press.
