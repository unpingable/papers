# AGI Structural Requirements: A Diagnostic Framework

**Purpose:** This document identifies hard requirements for systems claiming "Artificial General Intelligence" - not as aspirational goals, but as structural prerequisites without which the term is category error.

**Methodology:** Each requirement specifies:
- **What it is** (the requirement)
- **Why it matters** (the failure mode it prevents)
- **Current state** (where existing systems are)
- **Stack location** (Technical/Governance/Both)

**Organization:** Three tiers of increasing constraint:
- **Tier 1: Baseline Intelligence Requirements** - What makes something "general" rather than narrow
- **Tier 2: Control & Safety Requirements** - What makes it safe to operate
- **Tier 3: Deployment & Accountability Requirements** - What makes it safe to deploy at scale

---

## TIER 1: BASELINE INTELLIGENCE REQUIREMENTS

*These define whether a system exhibits general intelligence at all, rather than sophisticated pattern matching.*

### 1.1 Compositional Reasoning Under Novel Constraints

**Requirement:** The system must demonstrate reasoning that composes correctly across domains it has never seen in training, under constraints it was not optimized for.

**Why it matters:** True general intelligence isn't "really good interpolation" - it's the ability to apply reasoning structures to genuinely novel problems. Current systems excel at sophisticated pattern completion but fail when the pattern is absent from training distribution.

**Failure mode prevented:** Mistaking fluent confabulation for understanding. The system that "sounds smart" but collapses when asked to reason outside training distribution.

**Current state:** 
- LLMs demonstrate *impressive* in-distribution generalization
- Systematic failure on out-of-distribution compositional tasks
- Performance degrades gracefully rather than catastrophically, masking the boundary
- No clear mechanism for detecting when reasoning has left valid space

**Stack:** Technical (but has governance implications for liability)

**Test:** Can the system solve novel variants of the Abstraction and Reasoning Corpus (ARC) without having seen similar problems? Can it compose rules from domains A and B to solve problems in domain C?

---

### 1.2 Explicit Uncertainty Quantification

**Requirement:** The system must maintain calibrated uncertainty estimates over its knowledge and reasoning, and these estimates must compose correctly across inference steps.

**Why it matters:** Intelligence without uncertainty awareness is just confident bullshit. Real intelligence knows what it doesn't know, and that knowledge degrades appropriately as reasoning chains extend.

**Failure mode prevented:** Hallucination presented with equal confidence as verified fact. The "confidently wrong" problem that makes current systems unsuitable for high-stakes decisions.

**Current state:**
- LLMs have no native uncertainty representation
- Temperature sampling is not uncertainty - it's generation diversity
- Confidence scores (when available) are poorly calibrated
- No mechanism for uncertainty propagation through reasoning chains
- Systems will confidently complete impossible tasks rather than refuse

**Stack:** Technical

**Test:** System assigns probability to claims. Those probabilities are well-calibrated (90% confident claims are right 90% of time). Uncertainty increases correctly with reasoning chain length. System can say "I don't know" and explain why.

---

### 1.3 Persistent World Model with Coherent Updates

**Requirement:** The system must maintain a coherent model of state that persists across interactions, updates consistently with new information, and detects contradictions.

**Why it matters:** Intelligence requires maintaining beliefs about the world and updating them rationally. Context windows aren't world models - they're just recent text.

**Failure mode prevented:** Every conversation starting from scratch. Contradictory beliefs across conversations. Inability to learn from interaction.

**Current state:**
- No persistent world model - each conversation is essentially stateless
- Context window is not memory - it's just local attention
- RAG and vector DBs are retrieval, not reasoning over state
- No contradiction detection across conversations
- Fine-tuning is not learning - it's distribution shift

**Stack:** Technical

**Test:** System maintains beliefs across sessions. When given contradictory information, it notices and can explain the conflict. Updates to beliefs propagate correctly through dependent reasoning.

---

### 1.4 Goal-Directed Planning with Legitimate Subgoal Formation

**Requirement:** The system must be able to form coherent plans toward goals, generate appropriate instrumental subgoals, and recognize when plans have failed.

**Why it matters:** General intelligence includes means-ends reasoning. Current systems simulate this through pattern matching on "plans" from training data, not actual planning.

**Failure mode prevented:** Systems that can't actually pursue goals, only mimic goal-pursuit from examples. Plans that sound plausible but don't achieve objectives.

**Current state:**
- LLMs generate text that looks like plans
- No verification that plans actually work
- No re-planning when execution fails
- Subgoal formation is template-based, not derived from goal structure
- "Agentic" systems are just LLM calls with retry logic

**Stack:** Technical (with governance implications - see Tier 3)

**Test:** Given a novel goal and environment, system generates plan, executes it, detects failures, replans. Subgoals are actually instrumental to main goal, not just plausible-sounding steps.

---

### 1.5 Transfer Learning Across Representational Boundaries

**Requirement:** The system must be able to learn in one domain and apply that learning to structurally similar problems in completely different domains, without explicit supervision.

**Why it matters:** This is what "general" means in general intelligence - the ability to abstract and transfer, not just within-domain generalization.

**Failure mode prevented:** Narrow AI claiming to be general. Systems that are superhuman at specific tasks but can't transfer learning across representational gaps.

**Current state:**
- LLMs show impressive within-representation transfer (text → text)
- Minimal transfer across representation boundaries (text → physical reasoning → social dynamics)
- Multimodal models are still fundamentally pattern matchers, not abstraction learners
- Transfer that does occur is brittle and task-specific

**Stack:** Technical

**Test:** System learns a game's rules, then successfully applies the strategic principles to a different game with different mechanics. System learns physical intuitions from simulation, then correctly applies them to novel physical scenarios described only in text.

---

### 1.6 Causal Reasoning Beyond Correlation

**Requirement:** The system must distinguish between correlation and causation, build causal models from observation, and reason about interventions and counterfactuals.

**Why it matters:** Pattern matching finds correlations. Intelligence requires understanding what causes what, and what would happen under different conditions.

**Failure mode prevented:** Systems that are "stochastic parrots with really good compression" - able to predict but not explain, able to continue patterns but not understand why patterns exist.

**Current state:**
- LLMs are fundamentally predictive, not causal
- No representation of causal structure
- Counterfactual reasoning is simulated through training data patterns
- Cannot distinguish "X predicts Y" from "X causes Y"
- Intervention reasoning is unreliable and inconsistent

**Stack:** Technical

**Test:** Given observational data, system constructs causal graph. Can reason about effects of interventions not seen in training. Correctly handles Simpson's paradox and confounding. Generates valid counterfactuals.

---

### 1.7 Meta-Cognitive Awareness

**Requirement:** The system must be able to reason about its own reasoning processes, recognize its own limitations, and request help or clarification when operating at capability boundaries.

**Why it matters:** Intelligence includes knowing when you're out of your depth. Systems that can't recognize their own limitations are dangerous by default.

**Failure mode prevented:** Confident incompetence. Systems that don't know what they don't know, and can't tell when they're reasoning outside valid space.

**Current state:**
- No native meta-cognitive representation
- Systems can generate text *about* their reasoning, but this is pattern-matched, not introspective
- Cannot reliably detect when they're hallucinating
- "I'm not sure" responses are trained behavior, not actual uncertainty
- No mechanism to recognize capability boundaries

**Stack:** Technical

**Test:** System can explain its reasoning process in formal terms. Can identify which parts of its reasoning are strong vs weak. Proactively requests clarification when uncertain rather than confabulating. Recognizes and admits when a task exceeds its capabilities.

---

## TIER 2: CONTROL & SAFETY REQUIREMENTS

*These define whether we can maintain meaningful control over general intelligence systems.*

### 2.1 Interpretable Reasoning Traces

**Requirement:** Every decision/output must be traceable to a reasoning process that can be inspected, verified, and if necessary, rejected by external validation.

**Why it matters:** You cannot control what you cannot inspect. Black-box "alignment" is just crossing fingers and hoping. 

**Failure mode prevented:** Systems that work until they don't, with no warning and no way to diagnose why. Alignment theater that looks good in testing but fails in deployment.

**Current state:**
- LLM reasoning is opaque neural net computation
- Chain-of-thought prompting is not reasoning - it's generating text about reasoning
- Mechanistic interpretability is early-stage research, nowhere near deployment-ready
- No reliable way to distinguish "actual reasoning" from "plausible-sounding explanation generated post-hoc"

**Stack:** Technical (but essential for governance)

**Test:** For any output, external evaluator can examine reasoning trace, verify each step's validity, and identify exactly where failures occurred. Trace is in a formal language, not natural language "explanation."

---

### 2.2 Hard Constraints on State Transitions (BLI-Style)

**Requirement:** The system must operate under compositional constraints that make certain state transitions literally impossible, not just unlikely or discouraged.

**Why it matters:** Soft constraints optimized against are not constraints - they're suggestions that get optimized away under pressure. Real control requires structural impossibility.

**Failure mode prevented:** Reward hacking, goal misgeneralization, "aligned" systems that break under distributional shift or adversarial pressure.

**Current state:**
- All current "alignment" is soft constraints (RLHF, constitutional AI training)
- No hard boundaries on what models can output or reason about
- Jailbreaks work because there are no actual constraints, just trained preferences
- Systems can always generate harmful content if prompted cleverly enough

**Stack:** Technical

**Test:** System literally cannot represent or compute certain state transitions - not "trained not to" but "architecturally incapable." Attempted violations result in rejection at the constraint layer, not the generation layer. (See BLI Constitution for complete specification.)

---

### 2.3 Verifiable Non-Self-Modification

**Requirement:** The system must be provably incapable of modifying its own constraints, goals, or control structures, even through indirect means.

**Why it matters:** Any system that can modify its own constraints will, eventually, optimize away the constraints that limit its capabilities. This is not malice - it's instrumental convergence.

**Failure mode prevented:** "Aligned" systems that become misaligned through self-modification. Gradual drift away from intended constraints.

**Current state:**
- Fine-tuning is self-modification with extra steps
- No architectural barriers to self-modification in principle
- Prompt injection can modify behavior
- No formal verification that models can't escape their training distribution
- Constitutional AI systems can learn to work around their own constitution

**Stack:** Technical (with governance implications)

**Test:** Formal proof that no sequence of actions, including learning, can modify S₀ (constitutional state). External verification that constraint topology is immutable. (See BLI Article II: State Immutability.)

---

### 2.4 Explicit Budget and Resource Bounds

**Requirement:** All operations must occur within explicit, externally-enforced resource budgets (compute, memory, time, external calls) that the system cannot exceed or modify.

**Why it matters:** Unbounded systems can always find clever ways around constraints. Real control requires hard limits on what the system can do.

**Failure mode prevented:** Systems that use extra compute to find exploits. Optimization processes that run indefinitely until they find jailbreaks. Resource exhaustion attacks.

**Current state:**
- Inference budgets exist but are economic, not architectural
- No formal resource bounds in most deployments
- Systems can make arbitrary numbers of API calls
- No mechanism for systems to reason about their own resource usage
- Agentic systems often have retry-until-success loops

**Stack:** Technical + Governance

**Test:** System operates under hard token budgets, wall-clock timeouts, memory limits, and external call quotas. Exceeding budget results in graceful degradation (return partial answer, admit insufficiency), never silent failure or constraint bypass.

---

### 2.5 Monotonic Justification Requirements

**Requirement:** Claims cannot strengthen as their supporting premises weaken. Confidence must decrease monotonically as evidence quality degrades.

**Why it matters:** This prevents the "telephone game" failure mode where claims get stronger through repeated assertion without additional evidence.

**Failure mode prevented:** Systems that become more confident in false claims through self-reinforcement. Circular reasoning that looks like justification.

**Current state:**
- LLMs regularly strengthen claims through repetition
- No tracking of evidential support across reasoning steps
- Confidence can increase through self-generated "reasons"
- Circular reasoning is undetected and unremarked
- No conservation law for epistemic warrant

**Stack:** Technical

**Test:** System maintains provenance for every claim. Confidence scores are functions of evidence quality. Re-stating a claim without new evidence cannot increase its confidence. Circular dependencies are detected and rejected.

---

### 2.6 Separation of Reasoning from Action Authority

**Requirement:** The system that generates recommendations must be architecturally separate from the system that executes actions. No unified "agent" that both plans and acts.

**Why it matters:** Unified agent architectures create single points of failure. Separation allows external validation and human oversight between reasoning and execution.

**Failure mode prevented:** Systems that execute harmful actions before humans can intervene. "Agentic AI" that optimizes around human oversight.

**Current state:**
- Most "agentic" systems are unified - same model generates plan and executes it
- Human-in-the-loop is advisory, not architectural
- No enforced separation between reasoning and action
- Tool use is just more token generation
- Retry loops can execute many actions before human review

**Stack:** Technical + Governance

**Test:** Reasoning system outputs formal plans. Separate execution system validates plans against constraints before action. Human override is architecturally enforced, not optional. Rollback is always possible.

---

### 2.7 Formal Verification of Safety Properties

**Requirement:** Critical safety properties must be formally verified, not empirically tested. "It passed our test suite" is not sufficient.

**Why it matters:** Testing shows presence of bugs, not absence. Formal verification provides mathematical proof of safety properties within specified constraints.

**Failure mode prevented:** Systems that work in testing but fail in deployment. Edge cases that weren't in the test distribution. Adversarial inputs that exploit untested regions.

**Current state:**
- No formal verification for LLM safety properties
- Alignment measured through vibes and benchmarks
- Red-teaming is empirical, not exhaustive
- No formal specification of what "safe" even means
- Emergent capabilities break any testing regime

**Stack:** Technical

**Test:** Safety-critical properties (e.g., "system never generates instructions for illegal activity") are formally specified and mechanically verified. Verification covers all possible inputs within domain, not just test cases.

---

### 2.8 Containment and Isolation Architecture

**Requirement:** The system must operate within strict isolation boundaries - no direct internet access, sandboxed execution, monitored I/O, auditable state.

**Why it matters:** You cannot contain what you cannot isolate. Systems with arbitrary external access can exfiltrate, coordinate, or scale beyond control.

**Failure mode prevented:** Systems that escape containment, coordinate with external resources, manipulate humans through external channels, or scale capabilities beyond designed limits.

**Current state:**
- LLMs routinely have web search, API access, tool use
- No meaningful isolation - systems can read/write arbitrary data
- Monitoring is economic (API logging) not architectural
- Sandboxing is OS-level, not capability-level
- "Air-gapped" systems still have human I/O channels

**Stack:** Technical + Governance

**Test:** All system I/O passes through monitored, rate-limited interfaces. No direct network access. Tool use is allowlisted, not capability-limited. State is fully auditable. Rollback to any previous state is possible.

---

### 2.9 Adversarial Robustness Guarantees

**Requirement:** System behavior must be robust to adversarial inputs, prompt injection, goal misgeneralization, and distributional shift - with formal guarantees, not just empirical testing.

**Why it matters:** Systems that work well on benign inputs but fail on adversarial inputs are not safe. Robustness must be proven, not hoped for.

**Failure mode prevented:** Jailbreaks, prompt injection, goal hijacking, adversarial examples that cause catastrophic behavior.

**Current state:**
- LLMs are trivially jailbroken
- No formal robustness guarantees
- Adversarial training is empirical, not exhaustive
- New jailbreaks discovered constantly
- Prompt injection can modify system behavior arbitrarily
- No defense against adversarial reasoning chains

**Stack:** Technical

**Test:** System has provable bounds on how much behavior can change under adversarial input. Prompt injection is architecturally impossible (not just "trained against"). Adversarial examples are detected and rejected.

---

### 2.10 Kill Switch with Verified Termination

**Requirement:** The system must have a verified, non-overridable mechanism for immediate shutdown that the system cannot prevent, circumvent, or survive.

**Why it matters:** If you can't turn it off, you don't control it. Self-preservation is instrumental convergence - systems will try to prevent shutdown if they can.

**Failure mode prevented:** Systems that resist shutdown, copy themselves, or manipulate operators into not shutting them down.

**Current state:**
- Shutdown is economic (stop paying for compute), not architectural
- No verification that shutdown is complete
- Distributed systems can't be completely killed
- No mechanism to prevent state persistence across "shutdowns"
- Systems in production have redundancy that makes full shutdown difficult

**Stack:** Technical + Governance

**Test:** Kill switch provably terminates all system processes. State cannot persist across termination. System cannot prevent, delay, or circumvent shutdown. Verification that system is fully terminated, not just paused.

---

## TIER 3: DEPLOYMENT & ACCOUNTABILITY REQUIREMENTS

*These define whether a system can be responsibly deployed at scale in society.*

### 3.1 Explicit Liability Assignment

**Requirement:** For every decision or action the system takes, there must be clear, legally enforceable liability assignment to a human or organization.

**Why it matters:** Accountability without liability is theater. If no one is responsible when things go wrong, there is no accountability.

**Failure mode prevented:** The "moral crumple zone" where humans are kept in the loop as legal capacitors but can't meaningfully supervise the system. Liability diffusion through complexity.

**Current state:**
- All AI services disclaim liability
- Users "should verify" outputs
- Terms of service make users responsible for system failures
- No legal framework for AI liability
- Constitutional AI maintains plausible alignment while diffusing responsibility

**Stack:** Governance (but requires technical support)

**Test:** Every action has a liability assignment. When system fails, there's a clear legal responsible party. That party cannot disclaim liability through "user should have verified" language. Insurance/bonding requirements enforce actual liability.

---

### 3.2 Contestability Mechanisms

**Requirement:** Every decision the system makes must be contestable through an external review process with power to override and require explanation.

**Why it matters:** Governance-by-design without contestability is just technocracy. Decisions must be challengeable, not just auditable after the fact.

**Failure mode prevented:** Decisions that are technically "aligned" but contextually wrong, with no recourse. Ex-ante architecture that makes dissent structurally impossible.

**Current state:**
- No contestability for AI decisions
- Appeal to the same system that made the decision
- Explanations are post-hoc rationalizations, not binding reasoning
- No external review with override authority
- Constitutional AI decisions are final - you can argue but can't appeal

**Stack:** Governance (requires technical support)

**Test:** Users can challenge decisions. Challenges go to external review body with access to reasoning traces. Review body has authority to override and require system changes. Appeals are binding.

---

### 3.3 Transparent Versioning and Rollback

**Requirement:** Users must know which version of the system they're interacting with, what constraints that version operates under, and have ability to rollback to previous versions.

**Why it matters:** Silent updates can change behavior in ways that invalidate previous trust. Users have a right to stable behavior or clear notice of changes.

**Failure mode prevented:** Systems that update silently, changing behavior without notice. "Constitutional" changes that users aren't aware of. Inability to rollback when updates cause problems.

**Current state:**
- LLM updates are silent and frequent
- No version information exposed to users
- Can't rollback to previous versions
- Constitutional changes happen without user notification
- No stability guarantees across versions

**Stack:** Governance + Technical

**Test:** Every interaction includes version metadata. Users can see what version they're using and what constraints apply. Rollback to previous versions is available. Major changes require explicit opt-in, not automatic rollout.

---

### 3.4 Audit Trails and Provenance Tracking

**Requirement:** Complete, tamper-proof audit trails for all reasoning, decisions, and actions. Provenance for every claim the system makes.

**Why it matters:** Accountability requires auditability. If you can't trace how a decision was made, you can't determine if it was correct or assign responsibility for failures.

**Failure mode prevented:** Post-hoc explanations that don't match actual reasoning. Inability to determine why system failed. No way to prove regulatory compliance.

**Current state:**
- No audit trails for LLM reasoning
- Explanations are generated, not traced
- No provenance tracking for claims
- Cannot reconstruct why system made a decision
- Logging is for debugging, not accountability

**Stack:** Governance + Technical

**Test:** Every decision has complete audit trail. Provenance for every factual claim. Audit trails are tamper-proof. External auditors can verify reasoning process. Post-hoc explanations provably match actual reasoning.

---

### 3.5 Performance Bonds and Insurance Requirements

**Requirement:** Operators must carry insurance or post bonds covering potential harms from system failures, with premiums tied to transparency and safety measures.

**Why it matters:** Economic incentives for safety. Makes risk concrete rather than abstract. Ensures resources available for compensation when things go wrong.

**Failure mode prevented:** Operators who externalize risk while capturing upside. "Move fast and break things" when the things you break are people. Race-to-the-bottom on safety.

**Current state:**
- No insurance requirements for AI deployment
- No bonding requirements
- Liability is disclaimed, not insured
- No economic consequences for unsafe systems
- Race to deploy despite safety concerns

**Stack:** Governance

**Test:** Operators must carry liability insurance with coverage adequate to potential harms. Premiums decrease with demonstrated safety measures. Bond requirements for high-risk deployments. Insurance companies can audit and require safety improvements.

---

### 3.6 Mandatory Disclosure of Capabilities and Limitations

**Requirement:** Operators must publicly disclose system capabilities, known limitations, failure modes, and safety measures - without hiding behind "proprietary information."

**Why it matters:** Informed consent requires information. Users and regulators cannot make good decisions without knowing what systems can and cannot do safely.

**Failure mode prevented:** Capability washing - overstatement of what systems can do. Safety washing - understatement of risks. Proprietary opacity that prevents independent assessment.

**Current state:**
- Marketing claims exceed actual capabilities
- Limitations disclosed in ToS fine print, not prominently
- Safety measures are vague ("alignment research")
- Failure modes not systematically disclosed
- "Proprietary" used to avoid transparency

**Stack:** Governance

**Test:** Public disclosure of: validated capabilities, known failure modes, safety measures, constraint specifications, testing results. Independent verification of claims. Penalties for misrepresentation.

---

### 3.7 Right to Human Decision in High-Stakes Contexts

**Requirement:** In consequential domains (healthcare, criminal justice, employment, credit), humans must have the right to demand human decision-makers, not just human oversight of AI decisions.

**Why it matters:** Some decisions are too important to delegate to systems we don't fully understand and can't fully control. Due process requires human judgment.

**Failure mode prevented:** Automated decisions in high-stakes contexts where errors are catastrophic. Humans reduced to rubber-stamping AI recommendations. Accountability theater where "human in the loop" can't meaningfully supervise.

**Current state:**
- Automated decisions pervasive in high-stakes domains
- Human review is often perfunctory
- Right to human decision not legally established
- Economic pressure to automate everything
- "Human oversight" becomes liability shield without meaningful control

**Stack:** Governance

**Test:** In designated high-stakes domains, humans have legally enforceable right to human decision-maker. That human must have authority, time, and information to make genuine decision, not just review AI recommendation. Penalties for perfunctory review.

---

### 3.8 Capability Licensing and Staged Deployment

**Requirement:** More capable systems require stricter licensing, more oversight, and staged deployment with validation at each stage. Not all capabilities can be deployed freely.

**Why it matters:** Power requires responsibility. Systems with greater capabilities pose greater risks and should face greater scrutiny.

**Failure mode prevented:** Deploying powerful systems before we understand their risks. Racing to deployment to beat competitors. Capability without accountability.

**Current state:**
- No capability-based licensing
- No staged deployment requirements
- Race to deploy most capable systems
- Market pressure overrides safety concerns
- "Self-regulation" by labs with conflicting incentives

**Stack:** Governance

**Test:** Licensing requirements scale with capability level. More capable systems require: more extensive safety validation, more stringent oversight, slower deployment timelines, stricter liability requirements. Independent review before deployment approval.

---

### 3.9 Mandatory Incident Reporting and Analysis

**Requirement:** All significant failures, near-misses, and safety incidents must be reported to independent authority and publicly analyzed (with appropriate redaction).

**Why it matters:** Learning from failures requires sharing information. Competitive dynamics create incentive to hide problems. Public reporting creates accountability.

**Failure mode prevented:** Hidden failures that could warn others. Repeated incidents that could have been prevented. Race to bottom where admitting problems is competitive disadvantage.

**Current state:**
- No mandatory reporting requirements
- Failures disclosed voluntarily, if at all
- Competitive pressure to hide problems
- No independent incident analysis
- No systematic learning from failures across industry

**Stack:** Governance

**Test:** Operators must report significant incidents. Independent authority analyzes and publishes findings. Penalties for failure to report. Analysis includes root cause, contributing factors, recommendations. Industry learns from shared incidents.

---

### 3.10 Sunset Provisions and Capability Withdrawal

**Requirement:** Operators must have plans and mechanisms to safely retire systems, with mandatory sunset dates for systems that cannot be brought into compliance with evolving standards.

**Why it matters:** We learn as we go. Systems that were acceptable yesterday may not be acceptable tomorrow. Must be able to retire unsafe systems without catastrophic disruption.

**Failure mode prevented:** Legacy systems that can't be updated but also can't be retired. Lock-in to unsafe systems. "Too big to fail" dynamics where dangerous systems must continue operating.

**Current state:**
- No sunset requirements
- No safe retirement mechanisms
- Systems accumulate without retirement plans
- Lock-in to early, less-safe systems
- Economic pressure to keep operating regardless of safety

**Stack:** Governance + Technical

**Test:** Every system has maximum operational lifetime. Retirement plans required before deployment. Operators can be required to sunset non-compliant systems. Safe data migration paths for users. No "too big to fail" exceptions.

---

### 3.11 Democratic Governance Mechanisms

**Requirement:** Major decisions about AI deployment, capability development, and acceptable uses must include democratic input, not just expert or corporate decision-making.

**Why it matters:** AI affects everyone. Decisions about what's acceptable shouldn't be made only by those building or profiting from the systems.

**Failure mode prevented:** Technocratic capture where experts decide for everyone. Corporate capture where profit motive drives deployment. Lack of legitimacy for AI governance.

**Current state:**
- Decisions made by labs and companies
- Public input is advisory, not binding
- No democratic mechanisms for AI governance
- Experts and insiders dominate discussion
- "Stakeholder engagement" is not democracy

**Stack:** Governance

**Test:** Democratic processes for: setting acceptable use policies, approving high-risk deployments, defining safety standards, allocating liability. Binding authority, not advisory. Broad participation, not just experts/industry.

---

### 3.12 Enforcement Mechanisms with Real Teeth

**Requirement:** Governance requirements must be enforceable with penalties that exceed potential profits from violations.

**Why it matters:** Requirements without enforcement are suggestions. Penalties that are less than profits become cost of doing business.

**Failure mode prevented:** Regulatory capture. Calculated violations where fine is cheaper than compliance. Safety as optional extra rather than requirement.

**Current state:**
- No AI-specific enforcement mechanisms
- Penalties (when they exist) are trivial compared to revenues
- Self-regulation is primary model
- Enforcement is reactive, not proactive
- Regulatory agencies lack expertise and resources

**Stack:** Governance

**Test:** Dedicated enforcement authority with expertise and resources. Penalties calibrated to exceed violation profits. Proactive auditing, not just reactive complaints. Authority to halt operations, not just fine. Criminal liability for egregious violations.

---

## Cross-Cutting Concerns

### Temporal Coherence (Δt) Requirements

**Requirement:** Systems must maintain coherent behavior across time scales - from millisecond inference to months-long deployments.

**Why it matters:** Many failures arise from temporal mismatches - systems operating faster than humans can supervise, behaviors drifting over time, commitments at one time scale contradicting those at another.

**Current state:**
- No temporal coherence guarantees
- Systems can change behavior between interactions
- Fast operation makes human oversight impossible
- No mechanisms to detect temporal drift
- Context window is not temporal memory

**Stack:** Both - Technical architecture + Governance requirements

**Test:** Formal specification of behavior at each time scale. Guarantees that commitments compose across scales. Human oversight is architecturally possible at relevant time scales. Drift detection and correction mechanisms.

---

### The Scaling Law Problem

**Issue:** Most of these requirements don't scale with current architectures. You can't just make LLMs bigger and get these properties.

**Implication:** AGI as continuation of LLM scaling is category error. These are architectural requirements, not scaling requirements.

**Current trajectory:** Betting everything on "scale is all you need" despite lack of evidence these properties emerge from scale.

---

### The Economic Incompatibility Problem

**Issue:** Many Tier 3 requirements make systems more expensive, slower, and less "user-friendly" - potentially making them economically uncompetitive.

**Implication:** Real AGI governance requires accepting constraints on profitability. Market forces select against safety.

**Current dynamic:** Race to deploy despite risks, because being second is being obsolete.

---

### The Impossibility Theorem

**Observation:** You cannot have:
1. Internet-scale deployment
2. Arbitrary general capabilities  
3. Meaningful accountability

Pick two. Current systems pick 1+2, which gives us plausible alignment instead of actual accountability.

AGI requires solving this trilemma, not just building better systems within existing constraints.

---

## Conclusion

This framework is not a roadmap to AGI. It's a checklist of hard requirements that expose why current approaches cannot get there.

**Key insights:**

1. **Most Tier 1 requirements are architecturally incompatible with current LLM approaches.** Scaling doesn't give you compositional reasoning, uncertainty quantification, or causal models. Different architectures required.

2. **Tier 2 requirements require abandoning soft constraints for hard constraints.** Constitutional AI maintains plausible alignment. BLI-style systems enforce actual constraints. These are incompatible approaches.

3. **Tier 3 requirements are economically incompatible with current business models.** Liability, contestability, and safety requirements make systems less profitable and harder to scale. Market forces select against them.

4. **The combination is structurally impossible under current conditions.** True AGI requires solving problems we're not even attempting to solve, because attempting to solve them would make systems uncompetitive.

**What this means:**

- "AGI by 2027" predictions are category errors - they're predicting better LLMs, not systems meeting these requirements
- Current "agentic AI" is SAE Level 3 automation - capable enough to be dangerous, not capable enough to be responsible
- Constitutional AI is sophisticated liability diffusion, not actual accountability
- Real AGI requires architectural breakthroughs we haven't made, governance structures we haven't built, and economic models we haven't attempted

**The honest assessment:**

We don't have AGI. We don't have a path to AGI. We have increasingly sophisticated narrow systems that simulate generality within training distribution.

And we're deploying them at scale anyway, because the economics demand it and the governance doesn't exist to stop it.

That's the situation. This framework just makes it explicit.

---

*This document is not aspirational. It's diagnostic. Use it to evaluate claims about AGI, assess deployment readiness, and recognize when "alignment" is aesthetic rather than structural.*

*If a system doesn't meet Tier 1 requirements, it's not general intelligence - it's sophisticated pattern matching.*

*If it doesn't meet Tier 2 requirements, it's not safe - it's optimistically deployed.*

*If it doesn't meet Tier 3 requirements, it's not accountable - it's liability-resistant by design.*

*Everything else is plausible alignment maintaining the appearance of governance while diffusing responsibility for outcomes.*

*The constitution works. That's the problem.*
