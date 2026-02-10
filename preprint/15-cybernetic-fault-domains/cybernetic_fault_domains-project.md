# Cybernetic Fault Domains: When Commitment Outruns Verification

**James Beck**  
Independent Researcher

---

## Abstract

Disparate failure modes across organizational, computational, security, and socio-technical domains share a common structural invariant: temporal decoupling between fast commitment layers and slow verification layers. Building on fifteen domain-specific case studies (2023-2025), we formalize **cybernetic fault domains**—regions where system layers operating at mismatched temporal scales accumulate coherence stress until coupling breaks. Institutional decay, language model hallucinations, and security system bypasses are analyzable as instances of this mechanism. The Δt framework provides formal failure conditions (Δt > 0 ∧ σ > threshold), measurable parameters, and architectural solutions (governors enforcing temporal coupling). We provide fifteen instantiations (parameter mappings) and one ordering-only intervention consistent with causal reduction (BLI governor implementation).

**Keywords:** cybernetics, temporal dynamics, failure modes, Δt framework, system invariants, epistemic governance, control theory

---

## 1. Introduction

### 1.1 The Pattern Across Fifteen Papers

Between 2023 and 2025, we published fifteen papers analyzing failure modes across domains: organizational entropy [1], language model hallucinations [2-4], institutional resilience [5], scalar reward collapse [6], platform dynamics [7], representational coherence [8], temporal closure [9-11], AI-constrained inference [12], governed reasoning substrates [13], censorship circumvention [14], and asynchronous security systems [15].

Each paper was presented as a domain-specific contribution. Each used variations of the Δt (delta-time) framework to formalize temporal dynamics. Each identified measurable parameters and failure conditions. Each was released as a standalone contribution (archival publication or preprint) with domain-specific framing.

**The pattern that emerged:** They are not fifteen different findings. They are fifteen demonstrations of the same structural invariant.

**This paper formalizes that invariant as cybernetic fault domains.**

### 1.2 What Is A Cybernetic Fault Domain?

The concept builds on established cybernetics and dependable systems literature, synthesizing:

**From Ashby [16]:** Variety management—systems fail when requisite variety is exceeded. We extend this temporally: systems fail when variety **propagates faster than it can be attenuated**.

**From Laprie et al. [21]:** Fault containment regions in dependable systems—boundaries that prevent failure propagation. We generalize this across non-physical systems where "faults" are coherence violations. (We use "domain" in the containment-region sense, not root-cause taxonomy.)

**From Leveson [22]:** STAMP/STPA framework showing failures emerge from inadequate control structure. We formalize the temporal dimension: control fails when observation lags action.

**Our synthesis:** A **cybernetic fault domain** is a temporally defined containment failure: commitments become irreversible before verification can complete. More precisely, it is a regime of system operation in which fast-layer commitments outrun slow-layer verification, causing coherence stress to accumulate until coupling fails.

### Definition 1 (Cybernetic Fault Domain; boundary-relative)

Fix a commitment boundary C_k (Definition 2). A system S is in a **cybernetic fault domain** (a temporal regime) over an interval [t_0, t_1] if there exists a nonzero-measure subset of triggering events i such that:

1. **Ordering violation exists:** Δt_i ≡ max{0, T_commit,i - (W_i + A_i)} > 0 at boundary C_k, i.e., irreversible commitment can occur before verification-and-response could complete.

2. **Boundary load accumulates:** the count of **unverified crossings** of C_k over the interval exceeds a calibrated threshold:

$$\sigma_{[t_0,t_1]} \equiv \sum_{i \in [t_0,t_1]} \mathbf{1}[\text{cross}(C_k)_i \land \neg \text{verified\_and\_applied}_i] > \sigma_{\text{threshold}}$$

This definition is *boundary-relative*: disputes about "does Δt apply?" usually reduce to disagreement about where C_k is placed, not the mechanism.

**Terminology:** We use "fault domain" to mean a *temporal regime* (interval during which the system operates with Δt > 0 and accumulating σ). We reserve "region" for spatial/containment metaphors only.

### Entry, Load, Failure (separated)

- **Domain entry condition:** Δt > 0 (a race window exists; failure is structurally *possible*)
- **Load condition:** σ is increasing (unverified crossings accumulating)
- **Failure onset:** σ crosses σ_threshold **AND** domain-specific harm becomes irrecoverable within the correction horizon (rollback fails, breach completes, institutional commitment locks, etc.)

This separation prevents conflating "a system has a race window" with "a system has already failed."

Cybernetic fault domains do not exhaust all causes of failure; they identify a **recurring structural invariant** across otherwise heterogeneous failures.

More formally, a fault domain exists where:

1. **Multiple layers** operate at different temporal scales
2. **Variety propagates faster** than attenuation mechanisms can handle
3. **Control structure degrades** when observation cannot keep pace with dynamics
4. **Coherence stress accumulates** at the temporal boundary
5. **Coupling breaks** when stress exceeds containment threshold
6. **System fails** in characteristic, predictable ways

**Key insight:** Fault domains are not just spatial (where failures exist) but **temporal** (when fast layers outrun slow layers). The Δt boundary is a **fault domain in time**—a region where variety propagates unconstrained because verification cannot keep pace.

**Analogy to physical fault containment:**
- Bulkheads in ships prevent water propagation (spatial containment)
- Firewalls prevent network intrusion propagation (topological containment)
- **Governors prevent commitment propagation** (temporal containment)

**Cybernetic fault domains extend containment to temporal boundaries** where fast/slow layer decoupling allows failures to propagate before attenuation mechanisms engage.

### 1.3 Why This Matters

**Theoretical contribution:** Unifies disparate failure modes under single framework

**Practical contribution:** Provides instrumentation for detecting/mitigating temporal faults

**Methodological contribution:** Demonstrates how cross-domain analysis reveals structural invariants

### 1.4 Scope and Claims

**We claim:**
1. Temporal decoupling is a **structurally recurrent failure mechanism within cybernetic systems exhibiting fast/slow layer separation**
2. The Δt framework provides **formal conditions** for when failures occur
3. **Measurable parameters** (W_j, T_commit, A_j, C_j, κ_j) can be defined in all domains studied, and measured or bounded given minimal instrumentation
4. **Architectural solutions** (governors enforcing temporal coupling) generalize across these domains

**We do not claim:**
1. This explains all failures (some failures have other causes)
2. All systems are cybernetic (some lack feedback/control structure)
3. Temporal coupling is always optimal (some systems benefit from decoupling)

This framework applies specifically to **cybernetic systems with hierarchical temporal structure and delayed feedback**, where commitments can become irreversible prior to verification. It does not apply to tightly coupled physical control systems, single-timescale processes, or systems lacking feedback-mediated control loops.

**Necessary conditions for framework applicability:**
1. Separable fast/slow loops with different characteristic timescales
2. A commitment boundary that can harden state (irreversibility exists)
3. Delayed or limited observability between layers

**We demonstrate:**
- Fifteen empirical validations across domains
- Working implementation (Bounded Lattice Inference governor)
- Predictions tested across our case studies

**Note:** Appendix B (paradox reframings) is illustrative and not required for the core theoretical claims or empirical validations. It is omitted from evaluation claims.

**Validation terminology:** We distinguish **instantiation** (mapping the same measurable parameters onto a domain with documented failures) from **causal validation** (ordering-only intervention that reduces downstream failure). This paper provides fifteen instantiations and one causal validation via BLI.

**Critical non-circularity condition:** Δt is defined as a **leading indicator** (measured before failure), not a descriptive label (applied after failure). The framework is falsifiable: if enforcing temporal coupling does not reduce failure rates, Δt is not causal. Our BLI implementation demonstrates that it is (§2.4.1, §4.2).

---

## 2. Theoretical Foundation: The Δt Framework

### 2.1 Core Concepts

**Δt (Commitment Lead):** The nonnegative lead time by which an irreversible commitment occurs before verification-and-response could have completed.

**Fast Layer:** System component that generates proposals rapidly; may attempt commitment at boundary
- Examples: Token generation (proposal stream), packet transmission (commit at send), decision deliberation (proposal), policy execution (commit)

**Slow Layer:** System component that verifies, grounds, or validates the fast layer's outputs
- Examples: Fact-checking, evidence accumulation, feedback collection

**Temporal Coupling:** The degree to which fast and slow layers remain synchronized

**Coherence Stress:** Accumulated inconsistency when fast layer outruns slow layer. "Coherence" here means **non-contradictory committed state relative to the chosen boundary contract C_k** (domain-specific).

### 2.1.1 Notation Summary

| Symbol | Definition | Units |
|--------|------------|-------|
| T_commit | Time at which fast layer output becomes irreversible | time |
| W_j | Observation window for verification evidence | time |
| A_j | Action latency after verification completes | time |
| Δt | Commitment lead: max\{0, T_commit - (W_j + A_j)\} | time |
| m_proxy | Rate-space mismatch proxy (non-causal): \|r_F - r_G\| · (1 - c) | events/time |
| C_j | Commitment polarity (fail-open or fail-closed) | categorical |
| κ_j | Political budget / false positive tolerance | ratio |
| σ(t) | Accumulated unattenuated variety at commitment/verification boundary | variety |

### 2.2 Formal Definition

Let a system S have:
- **Fast layer F** with commitment rate r_F (commits per unit time)
- **Slow layer G** with verification rate r_G (verifications per unit time)
- **Coupling strength c** ∈ [0,1] (0 = decoupled, 1 = perfectly coupled)
- **Variety V_F** generated by fast layer (possible states/outputs)
- **Attenuation capacity K_G** of slow layer (variety it can verify/constrain)

### Proxy Metric (non-causal; use only when timestamps unavailable)

When event timing is unobservable, we use a **rate mismatch proxy**:

$$m_{\text{proxy}} \equiv |r_F - r_G| \cdot (1-c)$$

where c is coupling strength, defined operationally as the measured fraction of commitments that are reversibly bounded within correction horizon H AND whose reversal actually restores pre-commit state.

**m_proxy is NOT an estimator of Δt** and must not be used for causal claims. It is a coarse risk signal: sustained mismatch and weak coupling predict rising boundary load (σ), but Δt remains the causal quantity for ordering-only interventions. **If timestamps exist, report Δt distributions and do not use m_proxy.**

In event-timed systems we measure the **commitment lead over verification capacity**:

$$\Delta t \equiv \max\{0,\; T_{\text{commit}} - (W_j + A_j)\}$$

Where (all times measured from the same triggering event—proposal issuance or request arrival):
- T_commit = time at which fast layer output becomes irreversible
- W_j = observation window (time slow layer needs for evidence to arrive)
- A_j = action latency (time for slow layer to respond after verification)

**Convention:** Δt ≥ 0 always. When Δt > 0, the fast layer commits *before* the slow layer could complete verification-and-response—an open race window exists. When Δt = 0, verification keeps pace with commitment.

**Latency vs ordering (critical distinction):** Latency is ubiquitous; Δt is not. Δt is positive only when an **irreversible transition** can occur before the earliest possible verified corrective action. Systems with high latency but no irreversibility (C0 only) have Δt = 0 at relevant boundaries.

Δt remains the primary quantity for causal tests and interventions; m_proxy is a coarse fallback when timestamps are unavailable.

**Variety propagation rate.** Let V_F and K_G be dimensionless "variety-per-event" multipliers that map events into effective variety units (domain-specific; typically normalized). Then:

$$\frac{dV}{dt} = V_F \cdot r_F - K_G \cdot r_G$$

so dV/dt has units of variety/time.

**Operational "variety" definition:** In this paper, "variety" is operational: the count or entropy of distinct unverified proposals competing for commitment under finite verification capacity. It is a domain-native boundary-crossing counter. "Variety units" are optional normalization for cross-domain comparison; the mechanistic claim does not require cross-domain unit commensurability.

**Coherence stress.** Define accumulated unattenuated variety:

$$\sigma(t) = \int_{0}^{t} \max\left(0,\; \frac{dV}{d\tau}\right) d\tau$$

**Discrete-event form:** Let x_i = 1 if event i crosses the commitment boundary without verification complete; else x_i = 0. Then:

$$\sigma_N = \sum_{i=1}^{N} x_i \quad \text{or windowed:} \quad \sigma_{[t, t+\Delta]} = \sum_{i \in \text{window}} x_i$$

The integral form is a conceptual continuous approximation; the discrete count is what you actually measure. Both have units of variety (accumulated unattenuated crossings).

**σ units clarification:** σ is operationally an integer counter (boundary crossings). The "variety integral" is an interpretive continuous approximation. We report σ as counts; variety normalization is optional and not required for any causal claim. It is not generic backlog; it is the portion of variety that remains unattenuated **at the commitment/verification boundary**—proposals that cross into irreversible state while verification is incomplete.

**Queueing distinction (critical):** Standard queueing models typically describe backlog growth when arrivals exceed service. **A backlog is not failure.** A cybernetic fault domain arises when **irreversible state transitions occur while verification is incomplete**—i.e., when unverified items cross an irreversibility boundary. σ(t) formalizes accumulation at that boundary: it is backlog *with consequences*, not backlog as such. **The differentiator is not backlog; it's unverified backlog that crosses an irreversibility boundary.**

**Lemma (boundary crossing is the differentiator):** Queue length L(t) can grow without harm if items remain reversible. Harm correlates with B(t), the count of items that cross C_k unverified. B(t) is not determined by L(t) alone unless irreversibility and deadlines are modeled. Queue length is not predictive without modeling irreversibility; **σ counts deadline misses at the irreversibility boundary**.

In queueing terms, σ is most like a deadline-miss or commitment-before-service-completion counter, not queue length.

**Irreversibility in different domains:**
- *Organizations:* Resource allocation, public announcement, personnel decisions
- *LLMs:* User-visible closure (final answer, tool invocation, externally logged claim)—not raw token sampling
- *Security:* Privilege grant, data exfiltration, lateral movement
- *Networks:* Packet transmission, connection establishment

**Commitment taxonomy:** To reduce ambiguity, we distinguish commitment levels:
- **C0 (ephemeral):** Internal tokens, scratch state, proposals—fully reversible
- **C1 (communicative):** User-visible asserted claims, answer closure
- **C2 (actuated):** Tool calls, state changes, side effects
- **C3 (institutional):** Public commitments, policy, resource allocation, announcements

### Definition 2 (Commitment boundary C_k)

A **commitment boundary** C_k is a domain-chosen threshold at which a state transition becomes *irreversible within a correction horizon H* (Definition 3). All Δt claims in this paper are evaluated **relative to C_k**. For LLMs, Δt analysis targets **C1+** (closure) and **C2+** (actuation), not raw token emission (C0).

### Definition 3 (Correction horizon H and irreversibility)

A commitment is **irreversible** if restoring the pre-commit state is infeasible **within the domain's correction horizon H** (time, cost, legal, or physical constraints). Irreversibility is time-bounded and substrate-relative: "reversible in principle" is not operationally relevant when H is exceeded.

### Boundary Selection Principle

C_k must satisfy three constraints:
1. **Externally observable:** The crossing can be detected by an independent observer
2. **Operationally irreversible:** Restoration exceeds H or is infeasible
3. **Decision-relevant:** Crossing changes downstream state/behavior

Boundaries chosen post hoc to fit outcomes are invalid. In empirical work, C_k should be fixed before measurement.

**Irreversibility definition:** A commitment is irreversible if restoring pre-commit state is impossible or exceeds the domain's correction horizon. "Everything is reversible if you wait long enough" is not a counterargument; irreversibility is substrate-level and time-bounded.

This paper's Δt analysis applies to commitment levels where irreversibility exists in the substrate (C1+ for LLMs, C2+ for tool-using agents, C3 for organizations). Raw token sampling (C0) is not a commitment event.

**Boundary choice note:** All claims in this paper are relative to a chosen commitment boundary C_k. Disagreements about applicability typically reduce to boundary choice, not the Δt mechanism itself.

### Definition 4 (Verification)

**Verification** is a process whose output is authorized to block or rollback commitments at C_k within correction horizon H. Verification may be automated, human, statistical, or procedural; what matters is *authority* (can it prevent commitment?) and *timing* (can it complete before T_commit?).

**Operationalization:** In engineered systems, σ(t) can be measured directly via counts of unverified proposals, unreviewed changes, untriaged alerts, or uninspected flows that have crossed into committed state. In LLMs specifically: count of asserted factual claims without citations per output window. In less instrumented systems, proxy via leading precursors (drift metrics, reversal rates, alert saturation).

---

**Operational Δt Measurement Protocol:**

> 1. Choose a commitment boundary C_k appropriate to the domain
> 2. Measure T_commit as the timestamp of the first irreversible transition across C_k
> 3. Measure W_j + A_j as the earliest time a verifier could have produced and applied a corrective action
> 4. Compute Δt = max\{0, T_commit - (W_j + A_j)\}
> 5. Measure σ as count of unverified crossings per observation window

**Note on Δt estimation:** The above computes Δt_min (best-case). For operational robustness, also compute Δt_p95 using p95 verification+action latency. Report Δt distribution, not a single cherry-picked scalar.

---

**Loaded-domain condition (active risk boundary):** 

$$(\Delta t > 0) \land (\sigma(t) > \sigma_{\text{threshold}})$$

Note: This is the **loaded** condition, not mere entry. Entry is Δt > 0 alone (race window exists). The conjunction indicates the domain is *actively loaded* with accumulated unverified crossings.

Δt > 0 identifies an ordering violation (commitment can outrun verification). σ(t) > threshold identifies accumulated consequence: boundary accumulation has exceeded containment capacity.

This defines the regime in which failure becomes structurally likely absent additional hidden coupling mechanisms. A single ordering violation may be absorbed if irreversibility is low or if verification catches up quickly. Sustained ordering violations accumulate boundary stress until containment fails: unverified variety propagates into committed state, and the system enters a characteristic failure mode.

**Hidden coupling mechanisms:** Systems can tolerate Δt > 0 if they have latent couplers:
- Strong reversibility (easy rollback even after "commitment")
- Bounded blast radius (damage doesn't propagate)
- Redundancy (multiple verification paths)
- Low propagation gain (errors don't amplify)
- Pre-commit sandboxing (testing before real commitment)

These keep σ from converting into harm even when ordering violations occur. The framework predicts: remove hidden couplers → system becomes fragile to Δt > 0.

**Δt vs σ relationship:** Δt > 0 is necessary for *possibility* of failure; σ growth is necessary for *realization*. A sparse system (low event rate) or one where verification keeps up in expectation may have Δt > 0 but σ stays subcritical. We do not claim Δt alone implies failure.

**σ_threshold calibration:** Two concrete methods:
- *Damage-onset calibration:* Smallest σ over a window that correlates with irreversible harm or rollback failure rate spikes
- *Budget calibration:* σ_threshold derived from κ_j (political budget)—maximum tolerated false-positive gating cost before operators route around the governor
- *ROC calibration:* Choose σ_threshold to maximize AUC for a harm label (rollback failure, incident severity class, etc.)

**Sensitivity reporting:** We report sensitivity to σ_threshold via threshold sweeps; conclusions rely on monotone regions, not a single tuned value. σ is a random process; report rate (λ̂) and distribution (p95), not a single scalar.

**Interpretation:** 
When fast layer commits before slow layer can verify (Δt > 0) AND unverified variety has accumulated beyond threshold (σ(t) > σ_threshold), the system lacks requisite variety to maintain control—coupling breaks and system enters failure mode.

**This formalizes Ashby's Law of Requisite Variety in temporal terms:** A system cannot attenuate variety that arrives faster than its attenuation mechanisms can process. The temporal gap (Δt) determines whether variety propagates unconstrained or remains bounded.

### 2.3 Observable Parameters

**Measurement doctrine:** Measurability is tiered:
- **Instrumented systems:** Measure T_commit, W_j, A_j directly from timestamps
- **Partially instrumented:** Use proxy bounds (upper/lower estimates)
- **Uninstrumented:** Treat as qualitative *ordering* evidence only, not numeric Δt claims

Across all domains studied, the following parameters are measurable (or boundable):

**W_j (Observation Window):** Maximum time the slow layer will wait for evidence before defaulting
- SIEM: Mean Time to Detect (MTTD)
- DPI: Buffer depth / inspection window
- Organizations: Analysis cycle time
- LLMs: Context window / inference budget

**T_commit:** When fast layer's output becomes irreversible (at chosen C_k)
- LLMs: First C1/C2 crossing (answer-finalization, tool invocation)—NOT token generation (C0)
- Networks: Packet transmission
- Organizations: Decision implementation
- Security: Privilege granted

**A_j (Action Latency):** Time required for slow layer to respond after verification
- SIEM: Mean Time to Respond (MTTR)
- DPI: RST injection latency
- Organizations: Policy implementation delay
- Security: Enforcement latency

**C_j (Commitment Polarity):** Default behavior under uncertainty
- Fail-open: Proceed when evidence insufficient
- Fail-closed: Block when evidence insufficient

**κ_j (Political Budget):** Maximum tolerable disruption from slow layer enforcement
- False positive tolerance
- Operational overhead limit
- User friction threshold

### Operational κ Definition

Let FP_cost denote expected cost of false-positive gating over a window and H_cost denote expected harm cost of unverified commitments over the same window. Define:

$$\kappa \equiv \frac{\text{max FP\_cost operators will tolerate before bypassing governor}}{H\_cost}$$

Empirically, κ is observed at the **bypass point**: when enforcement is disabled, routed around, or softened due to operator friction.

### 2.4 General Failure Condition

**A system enters a cybernetic fault domain when:**

$$(\Delta t > 0) \land (\sigma(t) > \sigma_{\text{threshold}})$$

That is:
- Fast layer commits before slow layer can verify (Δt > 0)
- **AND** coherence stress has accumulated beyond threshold

**We operationalize this condition across all fifteen domains analyzed.**

#### 2.4.1 Δt as a Leading Indicator (Non-Circularity Condition)

Δt is not defined post hoc as system failure, but as a **leading indicator of coherence stress accumulation**. The framework is non-circular if and only if increasing temporal coupling (reducing Δt) *prior to failure onset* reduces downstream error propagation without modifying system objectives or alignment criteria.

This distinguishes Δt from descriptive labels: if temporal coupling is enforced and failure signatures persist unchanged, Δt was not causal. If failure attenuates or localizes under enforced coupling, Δt is mechanistic.

**Empirical test:** Our BLI governor implementation [13] demonstrates this: enforcing temporal coupling (language proposes, evidence commits) reduces hallucination rates in LLMs without changing model objectives. This validates Δt as causal mechanism, not post-hoc classification.

**BLI intervention summary:**
- *Baseline (C1 closure, no gate):* Claims commit at generation; hallucination rate H₀
- *With governor (evidence-gated C1):* Claims require citation/verification before commit; hallucination rate H₁ < H₀
- *Held fixed:* Model, prompts/tasks, verifier capacity
- *Changed:* Commit boundary gating (ordering only)

This is a minimal demonstration; full quantitative analysis is in [13].

**Strengthened non-circularity test:** The intervention must change temporal ordering (prevent irreversible commitment prior to verification) without increasing verifier capacity or narrowing the task. Hold r_G and task distribution fixed; modify only T_commit (or gating) such that Δt → 0. If failures persist at unchanged rates, the Δt mechanism is falsified for that system. If error propagation decreases under ordering-only enforcement, Δt is mechanistic.

**Potential confounders (and controls):**
- *Better verifier capacity:* Hold r_G constant
- *Task narrowing:* Hold task distribution constant
- *Different objective/reward:* Hold objectives constant
- *Post-hoc relabeling:* Measure Δt before outcomes
- *Selection bias:* Report Δt distribution, not cherry-picked cases

### 2.5 Minimal Worked Example (Two-Layer Discrete-Event System)

Consider a two-layer system where a fast layer produces commitments and a slow layer verifies them.

Let the trigger event occur at t=0. Define:
- T_commit = 2 s (commitment becomes irreversible at 2 seconds)
- W_j = 4 s (evidence arrival window)
- A_j = 1 s (action latency after verification)

Then:

$$\Delta t = \max\{0,\; 2 - (4 + 1)\} = 0$$

The system is temporally coupled: verification-and-response can complete before commitment.

Now introduce a race window:
- T_commit = 2 s
- W_j = 1.5 s
- A_j = 0.25 s

$$\Delta t = \max\{0,\; 2 - (1.5 + 0.25)\} = 0.25 \text{ s}$$

A positive commitment lead exists: the system commits irreversibly 0.25 seconds before verification-and-response could complete.

Define unattenuated variety inflow during that window as q commitments per second. Then over n events, accumulated unverified variety is approximately:

$$\sigma_n \approx \sum_{i=1}^{n} q \cdot \Delta t_i$$

If q = 10 and Δt = 0.25 s, then each event adds ≈ 2.5 units of unverified variety. With σ_threshold = 50, the system crosses threshold after ≈ 20 events, at which point failure becomes likely: downstream state reflects committed outputs that could not have been verified in time.

**Governor intervention:** A governor that enforces the ordering constraint "no irreversible commitment before verification completes" modifies T_commit to occur no earlier than W_j + A_j, forcing Δt → 0 and preventing σ from accumulating through irreversible commitments. The fast layer can still propose at full speed; only irreversible transitions are delayed.

---

## 3. Domain Demonstrations

We briefly summarize how the cybernetic fault framework manifests in each previously studied domain. Full details are in the cited papers; here we extract the common structure.

### Canonical Instantiation Template

Each domain mapping follows this protocol:

| Element | Definition |
|---------|------------|
| **C_k** | Commitment boundary chosen (C1/C2/C3) |
| **H** | Correction horizon for this domain |
| **T_commit** | How commitment time is measured/bounded |
| **W_j** | How observation window is measured/bounded |
| **A_j** | How action latency is measured/bounded |
| **σ method** | How boundary crossings are counted |
| **κ estimate** | How political budget is estimated |
| **Failure label** | Observable failure signature |

All fifteen instantiations follow this template. We provide abbreviated mappings below; full measurement protocols are domain-specific.

### 3.1 Organizational Systems [1,5]

**Fast layer:** Leadership decision-making  
**Slow layer:** Evidence gathering, feedback from implementation  
**Δt manifestation:** Decisions outpace information → institutional entropy  
**Observable:** Second Law of Organizations—temporal lag drives irreversible decay  
**Parameters:** 
- W_j = Analysis cycle time
- T_commit = Resource allocation/policy implementation
- C_j = Fail-open (proceed despite uncertainty)
- κ_j = Tolerance for wrong decisions

**Failure signature:** Organizations make decisions faster than feedback can inform corrections, leading to drift from reality and eventual collapse.

### 3.2 Language Model Hallucinations [2-4,12]

**Fast layer:** Proposal production (token stream, hypothesized claims)  
**Commitment boundary:** C1/C2 closure (final answer, tool invocation)  
**Slow layer:** Fact verification, evidence assembly, grounding  
**Δt manifestation:** Closure outruns verification → plausible nonsense  
**Observable:** Temporal debt detection—hallucinations as temporal coherence violations  
**Parameters:**
- W_j = Inference budget / context window
- T_commit = First irreversible boundary crossing at C1 (answer-finalization) or C2 (tool invocation / external write). Token generation (C0) is explicitly NOT T_commit.
- C_j = Fail-open (generate without verification)
- κ_j = User tolerance for errors

**Failure signature:** LLMs produce fluent outputs without grounding, generating claims faster than verification can keep pace.

**Training implications:** LLM training primarily reduces error rate within the fast layer; Δt failures persist unless training objectives explicitly internalize delayed commitment (e.g., two-phase decoding, process supervision penalizing premature closure) or the system architecture externalizes commitment behind a verifier-governed boundary.

### 3.3 Deep Packet Inspection Bypass [14]

**Fast layer:** Packet transmission (transport clock)  
**Slow layer:** Content inspection (inspection clock)  
**Δt manifestation:** Evidence arrives after inspection window → bypass  
**Observable:** Bypass Inequality—formal conditions for circumvention  
**Parameters:**
- W_j = Buffer depth / inspection window
- T_commit = Handshake completion
- C_j = Fail-open vs fail-closed policy
- κ_j = False positive tolerance (collateral damage)

**Failure signature:** DPI systems cannot accumulate evidence before connections complete, enabling circumvention via temporal manipulation.

### 3.4 Asynchronous Security Systems [15]

**Fast layer:** Attacker objectives (data exfiltration, privilege escalation)  
**Slow layer:** Detection and response (SIEM, alerts, manual intervention)  
**Δt manifestation:** Objectives complete before response → security bypass  
**Observable:** Temporal Attack Surface—race windows in async systems  
**Parameters:**
- W_j = MTTD (Mean Time to Detect)
- T_commit = Objective completion
- A_j = MTTR (Mean Time to Respond)
- C_j = Alert-only vs auto-isolate
- κ_j = Operational disruption tolerance

**Failure signature:** Security controls operate on slower timescale than threats, creating race windows where adversaries succeed before detection/response.

### 3.5 AI Safety Tuning [Observed, not yet published]

**Fast layer:** Safety classifier (keyword pattern matching)  
**Slow layer:** Intent analysis (context evaluation)  
**Δt manifestation:** Classification outruns understanding → false positives  
**Observable:** Meta-epistemic work blocked despite legitimate intent  
**Parameters:**
- W_j = Pattern matching speed (instant)
- T_commit = Refusal decision
- Context accumulation = slow (multi-turn)
- C_j = Fail-closed (refuse on suspicion)
- κ_j = Zero (no tolerance for PR risk)

**Failure signature:** Safety systems refuse legitimate sophisticated work because pattern matching operates faster than context evaluation.

### 3.6 Platform Dynamics [7]

**Fast layer:** User engagement (viral content, network effects)  
**Slow layer:** Moderation (content review, policy enforcement)  
**Δt manifestation:** Harmful content spreads before moderation → platform capture  
**Observable:** Eigenstructure collapse—engagement optimization dominates governance  
**Parameters:**
- W_j = Moderation queue depth / review time
- T_commit = Content virality threshold
- C_j = Fail-open (allow pending review)
- κ_j = User growth vs safety trade-off

**Failure signature:** Content moderation cannot keep pace with viral spread, leading to platform capture by engagement-optimized harmful content.

### 3.7 Representational Coherence [8]

**Fast layer:** Representational transformation (compression, translation, formalization)  
**Slow layer:** Commitment preservation verification  
**Δt manifestation:** Transformation outruns verification → commitment shear  
**Observable:** ΔR (representational coherence) violations  
**Parameters:**
- W_j = Verification against original commitments
- T_commit = Transformed representation adoption
- Shear = Lost commitments / total commitments

**Failure signature:** Transformations change representations faster than commitment preservation can be verified, causing selective loss of constraints, edge cases, and enforcement mechanisms.

### 3.8 Scalar Reward Collapse [6]

**Fast layer:** Optimization pressure (gradient descent, selection pressure)  
**Slow layer:** Multi-objective balance (competing values, constraints)  
**Δt manifestation:** Single metric optimization outruns holistic evaluation → Goodhart's Law  
**Observable:** Reward function collapses to single dimension  
**Parameters:**
- W_j = Policy evaluation cycle
- T_commit = Optimization step
- C_j = Fail-forward (continue optimizing)

**Failure signature:** Systems optimize faster than multi-objective balance can be maintained, collapsing to single scalar and producing unintended side effects.

### 3.9 Temporal Closure [9]

**Fast layer:** Synthetic system dynamics  
**Slow layer:** Reality feedback  
**Δt manifestation:** Simulation outruns reality check → simulator gap  
**Observable:** Coherence requirements for synthetic systems  
**Parameters:**
- W_j = Reality check frequency
- T_commit = Synthetic decision propagation
- Gap = Simulation divergence from reality

**Failure signature:** Synthetic systems evolve faster than reality can constrain them, leading to divergence and loss of correspondence.

### 3.10 Summary of Domain Unification

**Common structure across all domains:**

| Domain | Fast Layer | Slow Layer | Failure Mode |
|--------|-----------|-----------|--------------|
| Organizations | Decisions | Evidence | Institutional decay |
| LLMs | Generation | Verification | Hallucination |
| DPI | Packets | Inspection | Bypass |
| Security | Attacks | Detection | Breach |
| Safety Tuning | Classification | Intent analysis | False positives |
| Platforms | Virality | Moderation | Capture |
| Representations | Transform | Preservation | Shear |
| Optimization | Gradient | Multi-objective | Collapse |
| Synthesis | Simulation | Reality check | Divergence |

*Same pattern, different nouns, same failure mechanism.*

---

## 4. Architectural Solutions: Epistemic Governors

### 4.1 The Governor Pattern

If temporal decoupling is the failure mechanism, the solution is **enforcing temporal coupling architecturally** through fault containment at temporal boundaries.

**Governor architecture as fault containment:**

1. **Separate proposal from commitment** (containment boundary)
   - Fast layer generates proposals (variety production)
   - Slow layer commits after verification (variety attenuation)
   - **Boundary prevents unverified variety from propagating into committed state**

2. **Enforce temporal ordering** (variety flow control)
   - No commitment without evidence
   - No closure without verification
   - **Controls rate at which variety can cross temporal boundary**

3. **Make decoupling visible** (fault detection)
   - Track uncommitted proposals (accumulated variety)
   - Measure Δt in real-time (propagation rate)
   - Alert when threshold approached (imminent containment failure)

4. **Maintain invariants** (containment verification)
   - Temporal coherence (no contradictions across time)
   - Contradiction-free state (variety remains bounded)
   - Evidence > speculation (attenuation > production)

**In Ashby's terms:** The governor ensures the slow layer has **requisite variety** to attenuate the fast layer's output. When fast layer produces variety faster than slow layer can verify, governor **buffers** proposals until verification catches up.

**In Laprie's terms:** The governor is a **fault containment region** where failures (unverified commitments) are quarantined until they can be verified or rejected.

**In Leveson's terms:** The governor provides **control structure** ensuring that actions (commitments) cannot outrun observations (verifications)—preventing the loss of control that leads to accidents.

**Control-law corollary:** In tool-using agents and other actuator-bearing systems, Δt dynamics imply a runtime stability bound: allowable actuation power must scale inversely with verification delay and proportionally with evidence integrity. We formalize this as a dimensionless risk index and derive a binding inequality for dynamic capability shaping (Appendix C).

#### 4.1.1 Developmental Tradeoff

Temporal decoupling is not inherently pathological. In early-stage systems, exploratory regimes, or low-cost error environments, decoupling increases search efficiency and innovation rate. Δt enforcement becomes necessary only when system actions acquire irreversible externalities, scale-dependent amplification, or political insulation from correction.

Failure arises not from decoupling per se, but from **failure to reintroduce coupling after crossing the irreversibility threshold**. A startup can iterate rapidly with high Δt (move fast, break things) because failures are local and reversible. The same organization at scale requires lower Δt (governance, verification) because failures propagate widely and persist.

Governors should be introduced **phase-appropriately**, not universally. The framework predicts when coupling enforcement becomes necessary, not that it's always optimal.

**Coupling costs:** Forcing Δt → 0 is not free:
- *Throughput/latency tradeoff:* Verification gating reduces commit rate
- *Brittleness risk:* Over-coupling can shift risk to verifier availability
- κ_j (political budget) is the binding constraint on enforcement strength

**Selective coupling for real-time domains:** The governor forces Δt → 0 only at C2/C3 (actuated/institutional commitments), not at proposal generation. In real-time domains where latency is critical, the constraint is not Δt = 0 everywhere but *bounded risk as a function of action power* (see Appendix C):

$$R_t = \frac{P_t \cdot D_t}{E_t} \le \tau$$

If you must act fast (high D), you either (a) reduce P (lower-power action), (b) increase E (more evidence), or (c) accept higher τ with explicit governance approval. This preserves throughput for exploration while preventing unverified state from hardening at high-consequence boundaries.

### 4.2 Bounded Lattice Inference (BLI)

Our working implementation [13] demonstrates multiple fault containment boundaries:

**Temporal fault domain (Δt boundary):**
- **Linguistic layer** (fast): Generates claims, proposals, hypotheses
- **Evidence layer** (slow): Accumulates citations, verification, grounding
- **Governor**: Enforces that claims don't close without evidence
- **Containment:** Unverified variety (proposals) cannot propagate into committed state

**Authority fault domain (NLAI boundary):**
- **Language** (proposals): Can suggest, hypothesize, generate
- **Evidence** (authority): Makes final commitment decisions
- **Governor**: Non-linguistic signals have authority over linguistic fluency
- **Containment:** Linguistic variety cannot override evidential constraints

**Contradiction fault domain:**
- **Proposals** can be mutually inconsistent (exploration)
- **Committed state** must be contradiction-free (coherence)
- **Governor**: Prevents contradictory commitments from coexisting
- **Containment:** Logical inconsistency cannot propagate across commitment boundary

**Result:** Multiple nested fault domains where different varieties are contained at different boundaries. System can propose freely (high variety) but cannot commit without verification (variety attenuated).

**In terms of variety propagation:**
- Fast layer: High variety generation (many possible claims)
- Slow layer: Variety attenuation (only verified claims pass)
- Governor: Boundary ensuring attenuation capacity > generation rate
- **Requisite variety maintained architecturally, not procedurally**

### 4.3 Generalization to Other Domains

**The governor pattern applies wherever Δt failures occur:**

**Organizations:**
- Fast: Executive decisions
- Slow: Evidence-based analysis
- Governor: Policy requiring impact assessments before major decisions

**Security systems:**
- Fast: Attack execution
- Slow: Detection + response
- Governor: Inline enforcement (detection → immediate response, no gap)

**AI Safety:**
- Fast: Pattern matching
- Slow: Intent verification
- Governor: Context accumulation before refusal (proposed but not implemented)

**Platforms:**
- Fast: Content virality
- Slow: Moderation review
- Governor: Require manual review before algorithmic amplification past threshold

**Key insight:** Governors don't prevent fast layer operation. They prevent **commitment without verification**.

**Governor as interface contract:** The governor is the only path from proposal to committed state. No proposal can harden into irreversible state except through the governor's verification gate.

**Governor vs process:** A governor is enforcement at the *only path* from proposal → commitment; process is advisory and bypassable. This distinction is critical: adding "more review process" doesn't help if commitments can route around it. Governors are architectural, not procedural.

### 4.1.2 Governor Failure Modes (Threat Model)

Governors shift the control problem to the boundary; typical failure modes include:

- **Bypass channels:** Commitments cross C_k outside the governor path
- **Evidence laundering:** Low-integrity "receipts" that satisfy the schema but not reality
- **Verifier capture / rubber-stamping:** Verification becomes performative under throughput pressure
- **Backlog-induced starvation:** Verification delay D rises, forcing either unsafe power P or halting
- **Availability collapse:** Over-coupling makes the verifier a single point of failure
- **Adversarial timing:** Attacks target the governor's observation window to force fail-open/closed behavior

These are not exceptions to the framework: each creates a new Δt window or inflates D, raising risk per Appendix C. Governors create secondary Δt windows (verification pipeline latency, evidence laundering). These are modeled identically by choosing C_k at the governor boundary and re-measuring Δt and σ there.

**Mitigation:** High-availability verification, graceful degradation (power demotion rather than halt), and defense-in-depth at commitment boundaries.

Language still proposes. Attacks still attempt. Content still spreads. **But outcomes don't commit until slow layer verifies.**

---

## 5. Falsifiability and Predictions

### 5.1 Falsifiable Claims

**Claim 1:** Systems with Δt > 0 and σ(t) > threshold will exhibit characteristic failure modes
- **Falsification:** Find system with high Δt and accumulated stress that doesn't exhibit characteristic failure modes
- **Status:** Consistent with all fifteen case studies in our corpus; we observed no counterexample within this set. This is not evidence of universality; it is evidence of consistency within the surveyed corpus.

**Claim 2:** Measurable parameters (W_j, T_commit, A_j, C_j, κ_j) can be defined for cybernetic systems with separable fast/slow loops, and measured or bounded given minimal instrumentation
- **Falsification:** Find such a system where these parameters cannot be defined or bounded
- **Status:** Measured or bounded in every domain analyzed

**Claim 3:** Architectural governors enforcing temporal coupling prevent failures
- **Falsification:** Implement governor, show it doesn't prevent Δt failures
- **Status:** BLI implementation validates; tested on LLM hallucinations

**Claim 4:** Several classical paradoxes become tractable to reframe under explicit temporal ordering
- **Falsification:** Find paradox that remains paradoxical after Δt analysis
- **Status:** Addressed six major paradoxes; invites scrutiny on others

### 5.2 Testable Predictions

**Prediction 1:** Any system where we can measure W_j, T_commit, and Δt can predict failure onset. Use Δt_p95 (not Δt_min) and windowed σ for operational prediction.

**Prediction 2:** Systems with architectural coupling enforcement will show lower failure rates than those relying on procedural compliance

**Prediction 3:** Safety-tuned AI systems will show higher false positive rates on sophisticated queries than base models (temporal mismatch between pattern matching and intent analysis)

**Prediction 4:** Organizations with faster decision cycles than feedback loops will show higher rates of institutional drift

### 5.3 How To Falsify This Framework

**Strongest adversarial target:** A high-Δt system with persistent unverified commitments (σ > threshold sustained) that remains stable without hidden coupling mechanisms. If such a system exists and maintains coherence indefinitely, the framework's core claim is falsified.

**Method 1:** Find high-Δt system that doesn't fail
- Measure Δt > 0 persistently
- Show system maintains coherence
- Demonstrate coupling remains intact
- **Would invalidate:** Core failure mechanism claim

**Method 2:** Find failure that isn't Δt-related
- System fails catastrophically
- Measure Δt = 0
- Show no temporal decoupling
- **Would invalidate:** Generality across system class claim

**Method 3:** Implement governor, show it doesn't work
- Build architectural coupling enforcement
- Deploy in high-Δt system
- Failures continue at same rate
- **Would invalidate:** Solution mechanism claim

**We invite adversarial evaluation and replication.** The framework is strongest when subjected to critical testing.

**External validation opportunities:** The Δt mechanism can be tested independently in domains with existing instrumentation:
- *Incident response datasets:* MTTD/MTTR logs vs breach severity correlation
- *CI/CD pipelines:* Review lag + rollback rates vs deployment failure rates  
- *Content moderation:* Queue depth + virality curves vs harm propagation

Replication would involve: (1) measuring Δt and σ in a new domain, (2) implementing ordering-only intervention, (3) demonstrating failure attenuation without changing verifier capacity.

---

## 6. Discussion

### 6.1 Why This Took So Long To Discover

**Required confluence:**

1. **Cybernetics foundation** (Ashby, Beer, Wiener provided concepts)
2. **Control theory formalism** (observers, plants, feedback loops)
3. **Computational systems** (LLMs, distributed systems provide test cases)
4. **Cross-domain analysis** (willingness to look everywhere)
5. **Mathematical framework** (formalize Δt, measure parameters)
6. **Working implementation** (BLI proves it's not just theory)

**Ashby had 1-2.** Couldn't formalize temporal coupling precisely.

**Modern control theory has 1-2.** Focuses on narrow engineering domains.

**AI safety has 2-3.** Treats each failure as domain-specific problem.

**This synthesis required 1-6.** The invariant becomes visible only when all elements converge.

### 6.2 Relationship to Existing Work

**Related work spine:**
- *Dependability (Laprie):* Fault containment regions → C_k, σ
- *Safety/STAMP (Leveson):* Control structure + delayed feedback → Δt
- *Supervisory control (Ramadge/Wonham):* Event gating → governor pattern
- *OODA (Boyd):* Cycle-time advantage → Δt as ordering weapon
- *Resilience engineering (Hollnagel):* Drift + normalization of deviance → σ growth
- *Queueing/deadlines:* Deadline-miss models → σ as miss counter

**Cybernetics (Ashby, Beer, Wiener):**
- We formalize what they gestured at
- "Requisite variety" → temporal coupling requirements
- VSM → governor architectures
- Feedback → verification loops

**Control Theory:**
- Observer bandwidth vs plant dynamics → Δt
- Stability conditions → coherence thresholds
- Supervisory control → governor pattern

**Systems Theory:**
- Emergence → coherence from coupling
- Feedback loops → verification layers
- Resilience → governor enforcement

**AI Safety:**
- Alignment → temporal coupling between values and optimization
- Robustness → governor preventing Δt failures
- Interpretability → making Δt visible

**We're not replacing these fields. We're showing they share underlying structure.**

### 6.3 External Corroborations and Adjacent Results

While this synthesis draws primarily on our fifteen-paper corpus, closely related timing/verification asymmetries appear independently in multiple literatures:

**Decision cycles and latency:**
- Boyd's OODA loop [25]: Decision-making advantage from faster observe-orient-decide-act cycles. *We import:* timing asymmetry determines outcome. *We do not claim:* OODA is a special case of Δt. (Note: Boyd's work is commonly circulated via unpublished lecture notes; see Osinga [2007] for scholarly treatment.)
- Distributed systems CAP theorem [26]: Consistency vs latency trade-offs as temporal coupling constraints
- Incident response MTTD/MTTR [27]: Mean Time to Detect vs Mean Time to Respond as explicit Δt parameters

**Metric collapse under optimization:**
- Goodhart's Law [28]: "When a measure becomes a target, it ceases to be a good measure"
- Strathern's variant [29]: Optimization pressure outruns multi-objective verification
- Observable as scalar reward collapse (our §3.8) — same Δt structure

**Safety engineering and drift:**
- Vaughan's normalization of deviance [30]: Organizations drift from standards when feedback lags decisions
- Dekker's drift into failure [31]: Systems degrade when local adaptations outpace systemic understanding
- Both analyzable as institutional Δt accumulation (our §3.1)

**Queueing theory and backlogs:**
- Standard queueing models describe backlog accumulation when arrival rate exceeds service rate
- **Distinction:** Queueing theory models **backlog**; σ(t) formalizes backlog specifically at the commitment/verification boundary where irreversibility converts backlog into coherent-state damage
- The cybernetic fault domain emerges when queued items **commit** before verification, not merely when queues grow

**Important note:** These works do not claim "cybernetic fault domains"; we claim that their observed asymmetries are instances of the same structural condition formalized here. The contribution is the unified framework, not the discovery of timing asymmetries *per se*.

### 6.4 Limitations

**This framework does not explain:**
- Failures unrelated to temporal dynamics (resource exhaustion, corruption, external shocks)
- Systems without clear fast/slow layer separation
- Non-cybernetic systems (no feedback, no control)

**Explicit "doesn't apply" examples:**
- *Tightly coupled control loops* where actuation is continuously corrected (Δt ≈ 0 by design, e.g., PID controllers)
- *Pure scratch simulation* with no meaningful irreversibility (all state is proposal-grade)
- *Adversarial incentive failures* where timing is irrelevant (e.g., pure corruption, bribery)
- *Resource exhaustion* failures (capacity, not ordering)

**Scope clarification:** Δt is a **necessary structural condition** for a class of failures, not a complete causal story. Domain-specific mechanisms still matter; Δt explains *why control fails*, not *every symptom*. The framework identifies when verification cannot keep pace with commitment—it does not claim to explain all failure modes.

**Mechanistic claim boundary:** We claim a shared loss-of-control mechanism (unverified irreversible transitions), not shared symptoms. Domain-specific dynamics determine what happens after coupling breaks.

**It does explain:**
- Failures where timing matters
- Systems with hierarchical temporal structure
- Cybernetic systems with feedback loops

**Scope:** Applicable to cybernetic systems with hierarchical temporal structure—not universal across all possible failures.

**Note on paradoxes:** Several classical philosophical paradoxes (Sorites, Ship of Theseus, Zeno, Liar's, etc.) appear analyzable as temporal framing errors under Δt analysis. Full treatments of these appear in Appendix B; here we claim only that the framework **provides a lens** for reframing them, not that all paradoxes reduce to temporal issues.

### 6.5 Why This Matters

**Theoretical:**
- Unifies disparate failure modes under common framework
- Extends established fault containment theory temporally
- Provides falsifiable predictions

**Practical:**
- Instrumentation for detecting temporal faults
- Architectural solutions (governors)
- Predictive failure analysis

**Methodological:**
- Demonstrates value of cross-domain analysis
- Shows how structural invariants can be found across domains
- Validates incremental publication strategy

---

## 7. Conclusion

We have demonstrated that **temporal decoupling between fast and slow layers is a common structural failure pattern in cybernetic systems**, manifesting as:

- Organizational decay when decisions outpace evidence
- LLM hallucinations when generation outruns verification
- DPI bypass when inspection lags transmission
- Security breaches when attacks outpace detection
- Safety tuning false positives when classification outruns intent analysis
- Platform capture when virality outruns moderation
- Optimization pathology when gradient descent outruns multi-objective balance

**This pattern recurs across domains we have studied.** Whether it represents a universal principle or a common but bounded phenomenon requires further investigation across additional domains.

**Cybernetic fault domains**, as we have formalized them, are regions where system layers decouple temporally, accumulating coherence stress until coupling breaks and the system fails in characteristic ways. Building on Ashby's variety management [16], Laprie's fault containment [21], and Leveson's control structure theory [22], the Δt framework provides:

- **Formal conditions** for failure (Δt > 0 and σ(t) > threshold)
- **Measurable parameters** (W_j, T_commit, A_j, C_j, κ_j) demonstrated across studied domains
- **Architectural solutions** (governors enforcing temporal coupling via fault containment boundaries)
- **Falsifiable predictions** (invites adversarial testing and replication across new domains)

This work extends existing cybernetic fault containment theory to explicitly model temporal boundaries where variety propagates faster than attenuation mechanisms can process. The contribution: showing that temporal decoupling can be measured, predicted, and mitigated through architectural enforcement of coupling constraints.

We conclude by noting that the framework's scope is necessarily limited to cybernetic systems with hierarchical temporal structure and feedback loops. Whether the pattern extends beyond this domain requires empirical validation. The fifteen case studies presented demonstrate viability across the tested systems; further work should explore boundary conditions where the framework no longer applies.

**The practical value:** instrumentation for detecting temporal fault domains before failure occurs, and architectural patterns (governors) for maintaining requisite variety at temporal boundaries. **The theoretical value:** synthesis of temporal dynamics with established fault containment theory. **The open question:** how broadly does this pattern generalize beyond the domains studied?

---

## References

[1] Beck, J. "The Second Law of Organizations: How Temporal Lag Drives Irreversible Institutional Entropy." Zenodo, 2024. DOI: 10.5281/zenodo.14412133

[2] Beck, J. "Detecting Temporal Debt in Language Models and Software Systems." Zenodo, 2024. DOI: 10.5281/zenodo.14537066

[3] Beck, J. "You Need More Than Just Attention: Invariant Requirements for Temporal Coherence in AI Systems." Preprint, 2025.

[4] Beck, J. "AI-Constrained Inference: A General Model of Temporal Coherence in Hierarchical Inference Systems." Zenodo, 2024.

[5] Beck, J. "Capacity-Constrained Stability: A Control-Theoretic Framework for Institutional Resilience." Zenodo, 2024. DOI: 10.5281/zenodo.14412099

[6] Beck, J. "Scalar Reward Collapse: A General Theory of Eigenstructure Evaporation in Closed-Loop Systems." Zenodo, 2024.

[7] Beck, J. "Eigenstructure Collapse in Social Media Platforms: An Application of Scalar Reward Dynamics in Closed-Loop Systems." Zenodo, 2024.

[8] Beck, J. "Representational Invariance and the Observer Problem in Language Model Alignment." Zenodo, 2024.

[9] Beck, J. "Temporal Closure Requirements for Synthetic Coherence: Architectural Foundations and the Simulator Gap." Zenodo, 2024.

[10] Beck, J. "The Coherence Criterion: A Unified Framework for Stability in Hierarchical Systems." Zenodo, 2024.

[11] Beck, J. "Control Laws for Hierarchical Kinetics: Design Principles and Intervention Strategies for Multi-Timescale Systems." Zenodo, 2024.

[12] Beck, J. "Detecting Temporal Debt in Language Models and Software Systems: Applications of AI-Constrained Inference." Zenodo, 2024.

[13] Beck, J. "Bounded Lattice Inference: A Governed Reasoning Substrate with Persistent State and Non-Linguistic Authority." Zenodo, 2025.

[14] Beck, J. "From Timing Attacks to Evidence Denial: A Control-Theoretic Model of Censorship Circumvention." Preprint, 2025.

[15] Beck, J. "The Temporal Attack Surface: A Δt Framework for Asynchronous Security Systems." Preprint, 2025.

[16] Ashby, W.R. "An Introduction to Cybernetics." Chapman & Hall, 1956.

[17] Beer, S. "Brain of the Firm." Wiley, 1981.

[18] Wiener, N. "Cybernetics: Or Control and Communication in the Animal and the Machine." MIT Press, 1948.

[19] Ramadge, P.J. & Wonham, W.M. "Supervisory Control of a Class of Discrete Event Processes." SIAM Journal on Control and Optimization, 1987.

[20] Åström, K.J. & Murray, R.M. "Feedback Systems: An Introduction for Scientists and Engineers." Princeton University Press, 2008.

[21] Laprie, J.C. "Dependable Computing: Concepts, Limits, Challenges." Proceedings of the 25th IEEE International Symposium on Fault-Tolerant Computing, 1995.

[22] Leveson, N. "Engineering a Safer World: Systems Thinking Applied to Safety." MIT Press, 2011.

[23] Conant, R.C. & Ashby, W.R. "Every Good Regulator of a System Must Be a Model of That System." International Journal of Systems Science, 1970.

[24] Hollnagel, E., Woods, D.D., & Leveson, N. "Resilience Engineering: Concepts and Precepts." Ashgate, 2006.

[25] Boyd, J. "The Essence of Winning and Losing." Unpublished lecture notes, 1996.

[26] Brewer, E. "CAP Twelve Years Later: How the 'Rules' Have Changed." IEEE Computer, Vol. 45, No. 2, 2012.

[27] NIST. "Computer Security Incident Handling Guide." NIST Special Publication 800-61 Revision 2, August 2012.

[28] Goodhart, C. "Problems of Monetary Management: The UK Experience." Papers in Monetary Economics, Reserve Bank of Australia, 1975.

[29] Strathern, M. "'Improving ratings': audit in the British University system." European Review, Vol. 5, No. 3, 1997.

[30] Vaughan, D. "The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA." University of Chicago Press, 1996.

[31] Dekker, S. "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems." Ashgate, 2011.

---

## Appendix A: Parameter Measurement Guide

For practitioners seeking to instrument their systems for Δt analysis:

**Step 1: Identify Layers**
- What generates outputs/decisions quickly? (fast layer)
- What verifies/validates those outputs? (slow layer)
- Are they temporally decoupled?

**Step 2: Measure Temporal Parameters**
- **W_j:** How long does verification wait before defaulting?
- **T_commit:** When do fast layer outputs become irreversible?
- **A_j:** How long to act after verification completes?
- **Δt:** max\{0, T_commit - (W_j + A_j)\}

**Step 3: Determine Commitment Polarity**
- **C_j:** What happens under uncertainty?
  - Fail-open: Proceed without verification
  - Fail-closed: Block without verification
- Is this explicit policy or implicit default?

**Step 4: Assess Political Budget**
- **κ_j:** At what false positive rate do operators disable/circumvent the control?
- What's the operational overhead tolerance?
- Where does usability override security/accuracy?

**Step 5: Calculate Coherence Stress**
- σ(t) = accumulated unverified commitments over observation period
- Is stress accumulating?
- How close to threshold?

**Step 6: Intervene**
- If Δt > 0: Implement governor
- If C_j = fail-open and risk high: Consider fail-closed
- If κ_j exceeded: Improve signal quality or automate
- If A_j dominates: Reduce response latency

---

## Appendix B: Classical Paradoxes as Temporal Framing Reframings

*This appendix is illustrative and not required for the core theoretical claims or empirical validations. It is omitted from evaluation claims. These sketches demonstrate how temporal ordering may clarify certain apparent contradictions; they are not presented as definitive resolutions of longstanding philosophical disputes.*

### B.1 Sorites Paradox (Heap Problem)

**Classical formulation:** Removing one grain can't change a heap to non-heap, yet eventually it's not a heap.

**Δt analysis:**
- **Fast layer:** Physical grain removal (discrete events)
- **Slow layer:** Category recognition system (continuous perception with update latency)
- **Problem:** Classification operates on slower update rate than physical changes

**Reframing:** The paradox arises from forcing a vague boundary into instantaneous binary commitment; temporal update lag makes the boundary-crossing moment ill-posed. Not a logical paradox—a temporal framing problem where classification granularity doesn't match change granularity.

### B.2 Ship of Theseus

**Classical formulation:** If every plank is replaced, is it the same ship?

**Δt analysis:**
- **Fast layer:** Physical component replacement events
- **Slow layer:** Identity governance (legal, functional, narrative, or material criteria)
- **Problem:** "Same ship" is a commitment output of a chosen identity governor, but the paradox demands a single binary answer without specifying C_k

**Reframing:** The paradox is under-specified commitment boundary. Different governance contracts produce different stable outputs:
- *Legal contract:* Registry continuity → same ship
- *Functional contract:* Seaworthiness/mission capability → same ship if capable
- *Material contract:* Atom-level continuity → different ship
- *Narrative contract:* Crew/culture continuity → depends on crew

The apparent contradiction arises when we demand instantaneous binary commitment ("same/not") without specifying the governing contract. Once C_k is fixed, the paradox reduces to a governance-choice dispute: identity becomes the stable output of a chosen governor, not a property that must remain invariant under arbitrary boundary changes. All claims about "sameness" are relative to a chosen commitment boundary.

### B.3 Zeno's Paradox (Achilles and Tortoise)

**Classical formulation:** Achilles must first reach where tortoise was...infinite steps, never catches up.

**Δt analysis:**
- **Fast layer:** Physical motion (continuous in reality)
- **Slow layer:** Conceptual division (discrete sampling)
- **Problem:** Infinite conceptual steps mapped onto finite physical time

**Reframing:** Paradox exists in conceptual time (infinite discrete observations) not physical time (continuous dynamics). Physical Δt (time to catch up) is finite. Conceptual Δt (infinite measurement points) is unbounded. Not a motion paradox—a frame rate mismatch.

### B.4 Liar's Paradox

**Classical formulation:** "This statement is false" — if true then false, if false then true.

**Δt analysis:**
- **Fast layer:** Truth evaluation attempt (instant)
- **Slow layer:** Self-reference requires temporal delay (T>0)
- **Problem:** Statement refers to itself at T=0, but reference requires T>0

**Reframing:** Avoiding contradiction typically requires stratifying evaluation across steps (temporal or semantic), rather than collapsing self-reference into a single instant. Truth value cannot be determined at T=0 because the reference chain needs processing time. Not a logical paradox—a temporal ordering violation where evaluation requires staged semantics.

### B.5 Grandfather Paradox

**Classical formulation:** Go back, kill grandfather, prevent own birth. Contradiction.

**Δt analysis:**
- **Fast layer:** Causal intervention
- **Slow layer:** Identity persistence
- **Problem:** System tries to commit contradictory states across temporal boundary

**Reframing:** Temporal coherence is an invariant—system cannot maintain contradictory commitments across temporal loop. Same reason epistemic governors prevent contradictions: temporal closure must be maintained. Not "time travel impossible" but "contradictory temporal commitments impossible."

**Summary:** These paradoxes share a pattern: attempting to collapse temporal processes into instantaneous logic. When proper timescales are respected, the apparent contradictions dissolve. This doesn't "solve" the philosophical debates, but suggests many arise from incorrect temporal framing rather than logical impossibility.

---

## Appendix C: Dimensionless Risk Index for Actuator-Bearing Agents

In tool-using agents and other actuator-bearing systems, the Δt framework implies a runtime stability bound expressible as a dimensionless ratio. This ratio is analogous to the Reynolds number in fluid dynamics, which determines whether flow is laminar or turbulent.

### C.1 Variables

**Tool Power (P_t):** For action a_t using tool k:

$$P_t \equiv P(a_t) = \pi_k \cdot b_k \cdot \iota_k$$

where π_k is privilege scope, b_k is blast radius, and ι_k is irreversibility/undo cost, each normalized to [0,1]. P_t is dimensionless.

**Normalized Feedback Delay (D_t):** Let Δt(a_t) be the effective delay from action to trustworthy verification, and let D_{\text{ref}} > 0 be a system-specific reference delay (e.g., median verification delay under normal operation). Define:

$$D_t \equiv \frac{\max(D^{\text{tool}}_t, D^{\text{telemetry}}_t, D^{\text{human}}_t)}{D_{\text{ref}}}$$

so D_t is dimensionless.

**Evidence Integrity (E_t):** Bounded score E_t ∈ (0,1]. Evidence is fundamentally a vector; the scalar is a policy projection:

$$\mathbf{E}_t = (Q_t, PV_t, Rep_t, I_t)$$
$$E_t = g(\mathbf{E}_t) \text{ where } g \text{ is a monotone policy function}$$

Constraints on g:
- Monotone in each component (more receipts/provenance/replayability/independence → higher E)
- Normalized so E = 1.0 means fully instrumented, replayable, and independently verified

A weighted sum is one simple default choice:

$$E_t = w_q Q_t + w_p PV_t + w_r Rep_t + w_i I_t$$

**Concrete operationalizations:**
- Q_t: Receipts present? Tool logs? Hashes? (binary + coverage ratio, e.g., 0.8 = 80% of claims have receipts)
- PV_t: Number of custody links / depth to trusted root (normalized)
- Rep_t: Replay success rate / determinism class (0-1)
- I_t: Independent checks count / cross-model agreement rate

Weights sum to 1. Clamp E_t ≥ ε for numeric stability. Results are robust to monotone transforms of g. **We report components alongside E_t so policy choices are auditable.**

### C.2 The Agent Risk Index

Per-step risk (dimensionless):

$$R_t = \frac{P_t \cdot D_t}{E_t}$$

This ratio is **formally similar to a dimensionless regime separator** (like the Reynolds number in fluid dynamics). The analogy clarifies the role: R_t separates controlled from chaotic operation regimes. This is a *design heuristic*, not a physical isomorphism.

**Interpretation:**
- High power × long delay ÷ weak evidence = HIGH RISK
- Low power × short delay ÷ strong evidence = LOW RISK

This is analogous to the Reynolds number: Re = (inertial forces)/(viscous forces) determines laminar vs turbulent flow. R_t = (action momentum)/(verification friction) determines controlled vs chaotic operation.

### C.3 Regime Classification

Define thresholds 0 < τ₁ < τ₂ < τ₃:

$$\text{Regime}(\bar{R}_t) = \begin{cases} \text{SAFE} & \bar{R}_t < \tau_1 \\ \text{ELASTIC} & \tau_1 \le \bar{R}_t < \tau_2 \\ \text{DANGEROUS} & \tau_2 \le \bar{R}_t < \tau_3 \\ \text{RUNAWAY} & \bar{R}_t \ge \tau_3 \end{cases}$$

Where $\bar{R}_t$ is windowed/rolling risk (EMA or worst-case over window).

**Threshold calibration:** Thresholds are *policy parameters*, not derived constants. Choose σ_threshold based on observed "reversal cost" or "damage onset" point in the domain. Choose τ(tool) via historical incident tolerance. If domain-specific data is unavailable, treat thresholds as tunable and report sensitivity. **The form of the inequality is the contribution, not the numeric thresholds.**

### C.4 The Binding Policy

To enforce R_t ≤ τ, the allowed power is:

$$P_t \le P^{max}_t = \frac{\tau \cdot E_t}{D_t}$$

**"Your allowed power is proportional to your evidence and inversely proportional to your feedback delay."**

This is the entire governor expressed as a single inequality.

### C.5 Evidence Minimums (Fail-Closed Gates)

Tool class k has minimum evidence requirement E_min(k):

$$E_t < E_{min}(k) \Rightarrow \text{DENY tool } k$$

### C.6 Open-Loop Detection

Define actuation rate u_t and verification rate V_t:

$$\Gamma_t = \frac{u_t}{V_t}$$

Open-loop boundary: Γ_t > 1 implies verification lag is growing.

Fold backlog into delay: D_t := D_t + λ · backlog_t

This creates self-regulating feedback: verification backlog increases D_t, which decreases P^max, forcing the system to slow down.

### C.7 Receipts as Currency

Let required "evidence spend" be:

$$Cost_t = \eta \cdot P_t \cdot D_t$$

Let available credit be:

$$Credit_t = \alpha \cdot E_t$$

Permission rule:

$$Credit_t \ge Cost_t \Rightarrow \text{ALLOW}$$
$$Credit_t < Cost_t \Rightarrow \text{DENY}$$

This is algebraically equivalent to bounding R_t. If Credit_t ≥ Cost_t, then:

$$\alpha E_t \ge \eta P_t D_t \;\Rightarrow\; \frac{P_t D_t}{E_t} \le \frac{\alpha}{\eta}$$

So the credit rule enforces R_t ≤ τ with τ = α/η.

**Intuition:** You pay for powerful actions with evidence. No receipts, no capability.

### C.8 The Governor Loop

```
Given: (D_t, E_t) observed, P_req requested

1. If E_t < E_min(tool): DENY (insufficient evidence)
2. Compute R_t = (P_req · D_t) / E_t
3. If R_t > τ(tool): 
   - Compute P_max = (τ · E_t) / D_t
   - DEMOTE to highest tier ≤ P_max, or DENY if none
4. Update R̄_t, check regime
5. If RUNAWAY: HALT
6. Otherwise: ALLOW
```

### C.9 Why Evidence is the Denominator

Evidence is the **stabilizing force**. As E_t increases:
- R_t decreases (safer)
- P^max increases (more capability)

This creates correct incentives: want more power? Provide more evidence.

### C.10 Why Delay is in the Numerator

Delay is the **destabilizing force**. As D_t increases:
- R_t increases (riskier)
- P^max decreases (less capability)

This captures the Δt insight: slow feedback → more uncertainty → more risk.

### C.11 Glass Cannon Sensitivity

When P is large, small changes in D or E produce large changes in R:

$$\frac{\partial R}{\partial D} = \frac{P}{E}, \quad \frac{\partial R}{\partial E} = -\frac{R}{E}$$

If E → E/10 and D → 10D: R' = 100R

A 10x evidence degradation + 10x delay spike = **100x risk increase**.

This is why systems that "look safe" can become catastrophic instantly.

---

**Acknowledgments:**

Portions of this manuscript were developed with assistance from multiple large language models used as drafting and formalization aids. All claims, errors, and interpretive choices remain the author's responsibility.

**Ethical Statement:**

This work analyzes failure modes to enable their detection and mitigation. We deliberately avoid operational exploitation details. The goal is defensive instrumentation, not offensive capability development.

**Conflict of Interest:**

The author has no financial interests in cybernetics, control theory, AI safety, or related domains.
