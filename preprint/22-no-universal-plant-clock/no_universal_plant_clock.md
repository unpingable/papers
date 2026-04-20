---
header-includes:
  - \usepackage{booktabs}
  - \usepackage{tikz}
  - \usetikzlibrary{arrows.meta,positioning,fit,backgrounds,calc}
  - \let\oldtableofcontents\tableofcontents
  - \renewcommand{\tableofcontents}{\begingroup\raggedright\hyphenpenalty=10000\exhyphenpenalty=10000\oldtableofcontents\endgroup\clearpage}
---

# No Universal Plant Clock:\ Temporal Failure Geometry\ in Distributed Control Systems

**James Beck**
Independent Researcher

**Date:** March 2026

**Series:** Δt Framework, Paper 22

**Status:** Preprint v1.1 (adds §6.4 Lean-formalization paragraph; not yet pushed to Zenodo — Zenodo record is v1.0)

**DOI:** [10.5281/zenodo.19119617](https://doi.org/10.5281/zenodo.19119617)

---

## Abstract

Modern distributed systems routinely behave as though they possess a shared present, interchangeable clocks, fresh state observations, and timely control channels. In practice, none of these assumptions is guaranteed. This paper introduces a four-layer model of temporal failure in distributed control systems: (1) gauge mismatch in the construction of shared temporal reference frames, (2) clock divergence in the accumulation of local elapsed time, (3) retarded-state estimation under delayed observation, and (4) delayed actuation in closed-loop control. The framework treats temporal coherence not as a metaphysical property but as an operational constraint and, in many systems, a scarce control resource. Relativistic systems make these constraints explicit, but the same failure geometry appears at ordinary engineering scales in asynchronous networks, multi-agent control, remote operation, and institutional decision systems. We argue that many coordination failures are best understood as temporal failures wearing other labels. We introduce characteristic timescale ratios -- observation lag to plant dynamics, actuation lag to plant dynamics, synchronization uncertainty to plant dynamics, and contract duration to clock divergence horizon -- and show that the dominant failure mode in a given system is determined by which ratio exceeds its critical threshold first. The result is a diagnostic vocabulary for identifying which temporal layer dominates, what assumptions are being smuggled in by design, and how coherence budgets can be measured, allocated, and governed.

**Keywords:** temporal coherence, distributed control, clock synchronization, state estimation, control delay, timescale analysis, systems governance, cyber-physical systems, coordination failure

---

## 1. Introduction

Every control system assumes a clock. Most distributed systems assume several clocks agree.

A GPS receiver computes its position from signals whose transit time encodes distance. A drone swarm coordinates formation based on shared position estimates, each derived from sensors with different latencies. A moderation system reviews content that was posted hours ago, applying policy that was drafted months ago, targeting a conversation that has already moved on. A central bank adjusts interest rates based on economic indicators measured last quarter, targeting an economy that has already responded to the expectation of the adjustment.

These systems share a structural feature: they act on a model of the present constructed from observations of the past, through control channels that deliver their effects into the future. None of them has direct access to the current state of the thing they are trying to control. All of them assume, at some level of their design, that this indirection is small enough not to matter.

When the assumption holds, the system works. When it fails, the system does not merely degrade -- it fails in ways that are routinely misdiagnosed as logic errors, communication failures, or policy mistakes. A drone that oscillates is not confused about where to go. It is acting on stale state. A moderation system that over-corrects is not applying bad policy. It is applying yesterday's policy to a conversation that no longer exists. A central bank that induces the volatility it was trying to suppress is not incompetent. It is controlling a plant whose dynamics are faster than its observation-actuation loop.

This paper does not attempt to resolve metaphysical disputes about the ontology of time. It treats time operationally: as a set of constraints on synchronization, state estimation, and control in distributed systems. The question is not "what is time?" but *which temporal assumption breaks first in a given system, and what fails when it does*.

We formalize this as a four-layer model of temporal failure. The layers are not a hierarchy of importance but a decomposition of the distinct ways temporal coherence can break:

1. **Gauge mismatch.** Shared temporal reference is constructed, not discovered. Systems that assume a universal "now" are relying on a synchronization convention that may not hold.

2. **Clock divergence.** Local elapsed time is not interchangeable across nodes. Clocks drift, skew, and -- in relativistic systems -- accumulate genuinely different proper times along different worldlines.

3. **Retarded-state estimation.** All remote observation is delayed. "Current state" is always an inference from past measurements, never a direct reading.

4. **Delayed actuation.** Control signals propagate with finite speed and arrive at a plant that has already evolved past the state they were computed to address.

Relativistic systems make all four constraints non-negotiable: the speed of light bounds synchronization, proper time diverges along different paths, observations arrive retarded, and control signals cannot outrun light. GPS is the canonical example [10]: without relativistic corrections for gravitational and kinematic time dilation (a net +38 microseconds per day), position errors would accumulate at approximately 10 kilometers per day. The factory clock offset — setting satellite oscillator frequency to 10.22999999543 MHz instead of 10.23 MHz — is a permanent rate pre-compensation for clock divergence: the satellite oscillator is deliberately detuned so that its elapsed time, as experienced along its orbital worldline, matches ground-clock elapsed time. But the same four failure modes appear at ordinary engineering scales wherever observation latency, actuation delay, clock drift, or synchronization uncertainty is non-negligible relative to plant dynamics. The structure is the same. The scale is different.

Prior work in this series has established the consequences of temporal mismatch: architectural requirements for temporal coherence [1], inference failure when confidence outruns verification [2], adversarial exploitation of temporal attack surfaces [3], and the gain geometry by which temporal mismatch produces shear, leverage, and capture regimes [4]. The present paper proposes the underlying failure geometry that these prior papers have characterized in domain-specific form: temporal incoherence arising from mismatches among gauge, clock, estimation, and actuation layers in systems without a universal plant clock. It identifies the common structure underneath these results: four distinct temporal failure modes with characteristic timescales whose ratios determine which mode dominates and what breaks first.

We make three contributions. First, we decompose temporal failure into four operationally distinct layers and show that each corresponds to a different engineering constraint with different detection, different consequences, and different mitigations. Second, we introduce timescale ratio analysis as a diagnostic: the ratios of observation latency, actuation latency, and synchronization uncertainty to plant dynamics — and of contract duration to clock divergence horizon — determine the dominant failure mode. Third, we argue that temporal coherence is a scarce control resource -- not a single property but a bounded compatibility condition across timing conventions, local clocks, state estimates, and control windows -- that can be budgeted, allocated, and governed. The contribution is not discovering these layers individually — each is well-studied in its home literature — but providing a single diagnostic grammar for identifying which temporal resource is scarce, how the layers interact, and where failure will appear first when assumptions are relaxed. The framework is diagnostic rather than monocausal: in some domains temporal mismatch is the primary failure mechanism, while in others it amplifies or exposes failures rooted elsewhere.

---

## 2. No Universal Plant Clock

### 2.1 The Four Assumptions

Distributed control systems inherit four temporal assumptions, usually without stating them. Each assumption is false in general. Each produces a specific failure mode when violated.

**Assumption 1: A universal plant clock exists.** There is a single, objective "now" that all nodes share. Events can be globally ordered. Simultaneity is unambiguous. The system can refer to "the current state" without specifying whose clock or what synchronization convention.

This assumption is false in relativistic systems, where simultaneity is frame-dependent and no observer-independent global ordering of spacelike-separated events exists. It is also false in practice in any asynchronous distributed system where nodes cannot instantaneously agree on a common time. The engineering shadow of relativity's deeper constraint is the mundane reality that timestamp assignment is a convention, not a discovery.

**Assumption 2: Local clocks are interchangeable.** One second on node A is equivalent to one second on node B. Elapsed times can be compared, differenced, and aggregated across nodes without correction.

This assumption is false in relativistic systems, where proper time along different worldlines diverges (gravitational and kinematic time dilation). It is false in ordinary distributed systems whenever clock drift, skew, or resolution differences exist. Deadlines, leases, validity windows, and timeout contracts all silently assume clock interchangeability. When the assumption fails, temporal contracts rot: a lease that expires "in 30 seconds" means different things on different nodes.

**Assumption 3: Remote current state is directly accessible.** A controller can observe the current state of a remote plant. Measurements are instantaneous or negligibly delayed. The system can read "what is happening now" at a distance.

This assumption is false everywhere. All remote observation is retarded: the signal encoding the measurement travels at finite speed, the sensor has finite processing time, the communication channel has finite latency. "Current state" at a distance is always an inference from past observations plus a model of the plant's dynamics in the interval since measurement. The inference may be good or bad, but it is always an inference. No system has direct access to the present state of a remote plant.

**Assumption 4: Control is instantaneous.** A control signal computed now arrives at the plant now. Actuation lag is negligible. The state the controller computed its action against is still the state when the action arrives.

This assumption is false in any system with non-negligible actuation latency. In interplanetary telerobotics, the assumption is absurd: a command sent to a Mars rover addresses a state that existed 4-24 minutes ago. In a content moderation system, a policy enforcement action addresses a conversation that has evolved for hours since the content was flagged. In a central bank, an interest rate change addresses an economy that has already priced in the expectation of the change. The plant moves. The control signal arrives late. The gap between the two is the delayed-actuation failure mode.

### 2.2 The Four Negations

The paper's foundation is the negation of all four assumptions, stated as design constraints rather than unfortunate limitations:

1. **No universal plant clock.** Shared temporal reference is constructed through synchronization protocols, not discovered as a property of the world. The construction has finite precision, finite scope, and finite validity.

2. **No interchangeable local clocks.** Elapsed time is path-dependent, node-dependent, or otherwise non-fungible. Temporal contracts (deadlines, leases, validity windows) must specify which clock, what precision, and what divergence budget.

3. **No direct access to remote current state.** All remote state estimates are retarded. Measurement age is a first-class property of every observation. Uncertainty grows with delay and plant volatility.

4. **No instantaneous control.** Actuation lag is structural. Control actions target anticipated future state, not measured current state. The controller must model the plant's evolution during the actuation interval or accept that its actions address a state that no longer exists.

These are not exotic constraints. They are the default condition. Systems that work well are systems where these constraints happen to be satisfied within operational tolerances -- where the ratios of lag, drift, and uncertainty to plant dynamics are small enough to ignore. The failures come when the ratios are not small enough and the design does not account for them.

```{=latex}
\begin{figure}[ht]
\centering
\begin{tikzpicture}[
    >=Stealth,
    node distance=1.8cm and 3.2cm,
    block/.style={draw, rounded corners, minimum width=2.8cm, minimum height=1cm, align=center, font=\small},
    layer/.style={draw, dashed, rounded corners, inner sep=10pt, fill opacity=0.05},
    label/.style={font=\scriptsize\itshape, text=black!60},
    delay/.style={font=\scriptsize, midway, fill=white, inner sep=1pt},
]

% Plant
\node[block, fill=black!8] (plant) {Plant\\[-2pt]{\scriptsize dynamics at $T_p$}};

% Sensor
\node[block, fill=blue!8, right=of plant] (sensor) {Sensor /\\[-2pt]Observer};

% Controller
\node[block, fill=blue!8, right=of sensor] (controller) {Controller /\\[-2pt]Decision-maker};

% Actuator
\node[block, fill=blue!8, below=2.2cm of controller] (actuator) {Actuator /\\[-2pt]Enforcer};

% Arrows with delay labels
\draw[->, thick, blue!70] (plant.east) -- node[delay, above] {$T_o$ (observation lag)} (sensor.west);
\draw[->, thick, blue!70] (sensor.east) -- node[delay, above] {processing} (controller.west);
\draw[->, thick, red!70] (controller.south) -- node[delay, right, font=\scriptsize, fill=white, inner sep=1pt] {$T_u$ (actuation lag)} (actuator.north);
\draw[->, thick, red!70] (actuator.west) -| node[delay, below left, pos=0.25] {effect arrives late} (plant.south);

% Loop delay annotation
\draw[<->, thick, black!50, dashed] ([yshift=-6pt]plant.south east) -- node[delay, below, font=\scriptsize] {round-trip: $T_o + T_u$} ([yshift=-6pt]actuator.south west);

% Layer 1 & 2: constraint layers spanning everything
\begin{scope}[on background layer]
    \node[layer, fill=orange!10, fit=(plant)(sensor)(controller)(actuator), inner sep=18pt, label={[label, anchor=south west]south west:{Layer 1: Gauge --- shared ``now'' convention ($T_s$)}}] (gauge) {};
    \node[layer, fill=yellow!10, fit=(plant)(sensor)(controller)(actuator), inner sep=12pt, label={[label, anchor=north west]north west:{Layer 2: Clocks --- local elapsed time ($T_c$ divergence horizon)}}] (clocks) {};
\end{scope}

% Layer labels on right
\node[label, anchor=west] at ([xshift=8pt]sensor.east |- {$(sensor.north)+(0,0.5)$}) {Layer 3: Retarded-state estimation};
\node[label, anchor=west] at ([xshift=8pt]actuator.east) {Layer 4: Delayed actuation};

\end{tikzpicture}
\caption{Four-layer model of temporal failure in distributed control. Layers 1 and 2 (gauge convention, clock divergence) are constraint layers that bound the precision of Layers 3 and 4. Layers 3 and 4 (observation delay, actuation delay) compose into the closed-loop delay $(T_o + T_u)$ that determines control stability. The plant evolves at timescale $T_p$; failure occurs when a temporal ratio exceeds its critical threshold.}
\label{fig:four-layer}
\end{figure}
```

---

## 3. Four-Layer Model of Temporal Failure

The four layers are not a hierarchy of severity or a sequence of occurrence. They are four distinct ways that temporal coherence can break, each with its own detection signature, its own engineering consequences, and its own mitigations. A system may suffer from one layer, several, or all four simultaneously. The diagnostic value of the decomposition is precisely that it separates failure modes that are routinely conflated.

### 3.1 Layer 1: Gauge Mismatch

**What it is.** Gauge mismatch is disagreement about what "now" means. Not clock error — a deeper problem: the absence of a shared temporal reference frame within which clocks could even be compared.

In general relativity, this is rigorous: simultaneity is frame-dependent. Two events that are simultaneous in one reference frame are not simultaneous in another. There is no observer-independent global ordering of spacelike-separated events. In distributed computing, the absence of a free global temporal substrate appears in two distinct results. Lamport's logical clocks [5] address the ordering problem: they construct a partial ordering of events that does not require a shared physical clock, demonstrating that useful coordination is possible without a global "now." Fischer, Lynch, and Paterson [20] address a different limit: deterministic consensus is impossible in an asynchronous system with even one faulty process. Both results point to the same underlying constraint — shared temporal reference is not given, it must be constructed — but they formalize different consequences of that constraint.

But the practical manifestation of gauge mismatch is more mundane than either relativity or consensus impossibility. It is the silent assumption, embedded in system design, that timestamps assigned by different nodes refer to the same temporal reality. A log entry timestamped 14:03:22.451 on server A and another timestamped 14:03:22.451 on server B are assumed to record simultaneous events. They may not. The gap between the timestamps is not measurement noise — it is a convention mismatch. The nodes have constructed different "nows."

**How it manifests.** Gauge mismatch produces ordering ambiguity. Events that are causally unrelated but temporally close (relative to the synchronization precision) cannot be reliably ordered across nodes. Systems that assume total ordering — distributed databases with timestamp-based concurrency, event-sourced architectures that rely on monotonic sequence numbers, audit trails that assume a single timeline — produce incorrect results silently.

Google's Spanner [6] addresses gauge mismatch directly through TrueTime, an API that provides a bounded uncertainty interval rather than a point timestamp. Instead of claiming "the time is t," TrueTime says "the time is between t ± ε." Operations wait out the uncertainty interval before committing, ensuring that causally related events are properly ordered despite gauge mismatch. The engineering cost is real: Spanner commits are bounded below by the TrueTime uncertainty, typically 1-7 milliseconds. This is the price of taking gauge mismatch seriously rather than assuming it away.

**What it breaks.** Gauge mismatch undermines any operation that depends on a shared ordering of events across nodes: causal reasoning about distributed state, before/after relationships in audit trails, exactly-once semantics, and temporal fencing (locks, leases, and barriers that assume a common clock). When the gauge mismatch exceeds the temporal resolution required by the application, these operations do not fail loudly. They produce results that are internally consistent within each node but inconsistent across nodes.

**Interaction with other layers.** Gauge mismatch is the foundation layer. It does not cause clock divergence, retarded-state estimation, or delayed actuation — but it determines the precision floor for all of them. A system that cannot agree on "now" to within T_s cannot meaningfully compare clocks to precision better than T_s, cannot timestamp observations more precisely than T_s, and cannot coordinate control actions to finer granularity than T_s. Gauge mismatch sets the noise floor for temporal coherence.

### 3.2 Layer 2: Clock Divergence

**What it is.** Clock divergence is the accumulation of elapsed-time disagreement between nodes. Even after establishing a shared "now" (resolving gauge mismatch to some precision), local clocks drift apart. One second on node A is not the same duration as one second on node B.

In relativistic systems, this divergence is physical and irreducible. Gravitational time dilation causes clocks at different altitudes to run at different rates; kinematic time dilation causes moving clocks to run slower. GPS satellite clocks, orbiting at 20,200 km altitude and traveling at ~3.9 km/s, gain approximately 45 microseconds per day from reduced gravity and lose approximately 7 microseconds per day from their velocity, for a net gain of ~38 microseconds per day [10]. Without correction, this would produce position errors growing at ~10 km/day.

In ordinary distributed systems, clock divergence is an engineering imperfection rather than a physical law — but the operational consequence is the same. Crystal oscillators drift. Temperature changes shift oscillator frequency. Different hardware has different drift characteristics. Network Time Protocol (NTP) resynchronizes periodically, but between synchronization events, clocks wander. The divergence is typically parts per million — roughly 1 millisecond per 15 minutes for a commodity oscillator — but it accumulates.

**How it manifests.** Clock divergence rots temporal contracts. Any agreement that depends on elapsed time — "this lease expires in 30 seconds," "this cache entry is valid for 5 minutes," "this timeout fires after 200 milliseconds" — means different things on different nodes when their clocks run at different rates. A 30-second lease issued by node A and enforced by node B expires at a different real-world instant depending on whose clock is authoritative. The discrepancy is usually small. But "usually small" is not a guarantee, and systems that treat it as one discover the exception through failure: split-brain from asymmetric lease expiry, double-spending from timeout disagreement, or stale-data serving from cache invalidation that fires too late on one node.

**What it breaks.** Clock divergence undermines temporal contracts: leases, timeouts, TTLs, validity windows, deadline scheduling, and any protocol that compares elapsed times across nodes. It also undermines rate-based reasoning: "events per second" means different things when the seconds are different lengths. Drift-sensitive systems include distributed locks (where lease duration must exceed clock divergence plus message delay), certificate expiry (where validity windows must account for clock disagreement between issuer and validator), and real-time control (where sample-rate assumptions fail when the sampling clock and the plant clock diverge).

**Interaction with other layers.** Clock divergence is bounded by gauge mismatch from below (you cannot detect clock divergence smaller than the synchronization uncertainty) and bounds the useful precision of Layers 3 and 4 from above. A state estimate timestamped to microsecond precision is meaningless if the clocks involved diverge by milliseconds. An actuation deadline specified to millisecond precision is unenforceable if the deadline clock and the actuation clock disagree by more than the deadline itself.

### 3.3 Layer 3: Retarded-State Estimation

**What it is.** Retarded-state estimation is the fundamental condition of all remote observation: by the time a measurement arrives at the controller, the plant has moved. The controller never sees the current state. It sees what the state *was*, at a time determined by sensor processing delay, signal propagation, communication latency, and any queuing or batching in the observation pipeline.

The term "retarded" is used in its technical sense from physics and control theory: a retarded potential, a retarded field, a retarded state estimate — one that refers to an earlier time than the present. The observation is not delayed by accident. Delay is structural. Light moves at finite speed. Sensors take time to process. Networks have latency. There is no observation channel with zero delay.

The Age of Information (AoI) literature [9] has formalized this as a first-class metric: AoI is the time elapsed since the generation of the most recently received update. Crucially, AoI is not monotonically decreasing with update rate. Sending updates more frequently can increase queuing delay, causing the *freshest available* observation to be older than it would be under a sparser update schedule. Freshness is a resource with non-obvious dynamics.

**How it manifests.** Retarded-state estimation produces model-reality divergence. The controller's internal model of the plant state becomes a prediction rather than a reading, and the prediction degrades with the age of the last observation. In stable, slowly-evolving plants, the degradation is gradual and the controller can compensate with simple extrapolation. In volatile, fast-evolving plants, the degradation is rapid and the controller's model diverges from reality within a fraction of a plant timescale.

The classic engineering response is the state estimator (Kalman filter, particle filter, or their variants): a mathematical model that combines the last measurement with a dynamics model to predict the current state. The estimator's accuracy depends on the fidelity of the dynamics model and the freshness of the last measurement. When the dynamics model is poor or the measurement is stale, the estimator produces confident predictions of states that may not exist. This is temporal debt [2] at the estimation layer: the estimate carries more confidence than the evidence supports, and the gap is invisible until the plant deviates from the model.

**What it breaks.** Retarded-state estimation undermines any decision that depends on knowing the current state of a remote system: collision avoidance (the other vehicle is not where you think it is), inventory management (the warehouse does not contain what the database says), content moderation (the conversation has moved past the comment being reviewed), medical telemetry (the patient's vitals have changed since the last reading). In each case, the system acts on a state that is real but past, and the action's correctness depends on how much the plant has changed in the interval.

**Interaction with other layers.** Layer 3 is bounded by Layer 1 from below (the observation cannot be timestamped more precisely than the gauge convention allows) and bounds Layer 4 from above (a control action computed from a stale state estimate inherits the staleness). The round-trip — observe, estimate, compute, actuate — means that Layers 3 and 4 compose: the total delay between plant state and control effect is at least T_o + T_u, and the control action targets a state that is at least T_o + T_u old by the time it arrives. This is the closed-loop delay that determines whether the control system is stable.

### 3.4 Layer 4: Delayed Actuation

**What it is.** Delayed actuation is the other half of the closed-loop delay: the control signal takes time to reach the plant, and the plant evolves during transit. The controller computes an action for state x(t - T_o). The action arrives at the plant at time t + T_u. The plant is now in state x(t + T_u), which may be far from x(t - T_o). The control action was correct for a state that existed T_o + T_u ago.

Smith's predictor [8], introduced in 1957, remains the canonical engineering response: the controller contains an internal model of the plant and the delay, allowing it to predict the plant's future state at the time the control action will arrive and compute actions for that predicted state rather than the measured state. The technique works well when the plant model is accurate and the delay is known and constant. It degrades when the model is poor, the delay is variable, or the plant is subject to unmeasured disturbances.

**How it manifests.** Delayed actuation produces control instability. The pathology is familiar from classical control theory: a system with a feedback delay exhibits oscillation, overshoot, and potentially sustained instability. The controller corrects for a state that has already changed, the correction arrives and pushes the plant past the target in the opposite direction, and the next correction compounds the error. The system oscillates around the target rather than converging to it.

In engineered control systems, this manifests as phase margin erosion: the actuation delay eats into the phase margin of the feedback loop, reducing the range of controller gains that produce stable behavior. High-gain controllers — which respond aggressively to errors — are most vulnerable. A controller that is stable with zero delay becomes oscillatory as delay increases, and becomes unstable when the delay exceeds a critical fraction of the plant's characteristic timescale.

In institutional systems, the manifestation is policy overshoot. A central bank that observes economic indicators with a one-quarter lag and implements rate changes that take effect over months is controlling a plant with a round-trip delay measured in quarters. If the economic dynamics operate on a similar timescale, the bank's corrections can induce the volatility they were designed to suppress. Content moderation systems exhibit the same structure: enforcement actions that arrive after the conversation has moved on do not moderate the conversation — they punish participation in a context that no longer exists, which is a different intervention with different effects.

**What it breaks.** Delayed actuation undermines any closed-loop control system whose plant dynamics are fast relative to the actuation delay. The specific failure mode depends on the controller's design: conservative controllers become sluggish (they cannot respond faster than the round-trip delay allows), aggressive controllers become oscillatory (they overcorrect for states that have already passed), and both become ineffective when the delay exceeds the plant's characteristic timescale (the control action addresses a state that bears no useful relationship to the current state).

**Interaction with other layers.** Layer 4 composes with Layer 3 to form the closed-loop delay. It interacts with Layer 2 when control deadlines are specified in terms of elapsed time that may differ between controller and plant. It interacts with Layer 1 when multiple controllers must coordinate their actions and their "nows" disagree.

### 3.5 The Layers Are Not Independent

The four layers interact. Gauge mismatch sets the precision floor for all timing. Clock divergence degrades temporal contracts that coordinate the other layers. Retarded-state estimation and delayed actuation compose into the closed-loop delay that determines control stability.

A complete temporal failure analysis requires identifying which layer dominates, but it also requires checking for cross-layer interactions. A system with excellent synchronization (small gauge mismatch) but stale observations (large retarded-state estimation) has a different failure profile from a system with poor synchronization but fresh observations. The timescale ratio analysis in Section 4 provides the diagnostic framework for this assessment.

---

## 4. Timescale Analysis: What Breaks First

### 4.1 Characteristic Timescales

The four temporal failure modes are not abstract categories. Each has a characteristic timescale that determines when it becomes operationally relevant. The diagnostic question is not whether a failure mode exists -- all four exist in every distributed system -- but whether it matters, given the dynamics of the plant being controlled.

We define five characteristic timescales:

- **T_p** — plant timescale: the characteristic rate at which the controlled system evolves. In a drone swarm, T_p is the timescale of position and velocity changes. In a financial market, T_p is the timescale of price movements. In a moderation system, T_p is the timescale of conversation evolution. Many plants have dynamics at multiple timescales — a drone has millisecond attitude dynamics and second-scale position dynamics; an economy has daily price movements and quarterly structural shifts. Singular perturbation theory [11] formalizes this decomposition for systems with well-separated timescales; the present framework generalizes the question to cases where the separation may not be clean. In such cases, T_p should be matched to the timescale the controller is targeting. A position controller that ignores attitude dynamics is not temporally incoherent — it is operating at a different layer. The relevant T_p is the one whose violation would degrade the specific control objective under analysis. In practice, T_p can often be estimated from the system's step response time, the dominant mode period, or — in institutional settings — the characteristic timescale over which the quantity being controlled changes enough to invalidate a decision based on its prior value.

- **T_s** — synchronization uncertainty: the precision of the shared temporal reference frame. How well do the nodes agree on "now"? In GPS, T_s is bounded by the synchronization protocol (tens of nanoseconds). In an institutional decision system, T_s may be days or weeks -- different departments may be operating on different reporting cycles with different definitions of "current."

- **T_c** — clock divergence horizon: how long before local clocks diverge enough to invalidate temporal contracts. In systems with high-quality oscillators and periodic resynchronization, T_c may be months. In systems with cheap clocks and no resync protocol, T_c may be minutes. T_c is the shelf life of the assumption that one second here equals one second there.

- **T_o** — observation latency: the delay between an event occurring at the plant and the controller receiving a measurement of that event. This includes sensor processing time, signal propagation, communication latency, and any queuing or batching. T_o is the age of the freshest observation available to the controller. The Age of Information (AoI) literature [9] formalizes this as a first-class metric and shows that the relationship between update rate and information freshness is non-monotonic: updating too frequently can increase queuing delay and degrade freshness. AoI provides the mathematical machinery for the coherence budget concept developed in Section 4.4.

- **T_u** — actuation latency: the delay between the controller emitting a command and the plant experiencing its effect. This includes communication latency, actuator processing, and any queuing. T_u is the age of the controller's intent by the time it arrives.

### 4.2 Ratio Analysis

The temporal health of a distributed system is not determined by the absolute magnitude of any single timescale. It is determined by the *ratios* of the temporal failure timescales to the plant timescale. A 100-millisecond observation delay is negligible for a system whose plant evolves over hours. The same delay is catastrophic for a system whose plant evolves in microseconds.

The diagnostic ratios:

**Observation ratio: T_o / T_p.** When this ratio is small, the controller's state estimate is a reasonable approximation of the plant's current state. When this ratio approaches or exceeds 1, the controller is operating on a state estimate that is at least one plant-evolution timescale old. The plant has moved. The estimate is fiction.

The observation ratio determines estimator quality. As T_o / T_p grows:

- State uncertainty increases (the plant has had time to evolve away from the last measurement)
- Model dependence increases (the estimator must predict more of the plant's trajectory from its dynamics model rather than from fresh data)
- Estimation errors compound (small model errors are amplified over longer prediction horizons)

**Actuation ratio: T_u / T_p.** When this ratio is small, control commands arrive while the plant is still approximately in the state they were computed for. When this ratio approaches or exceeds 1, the control action addresses a plant state that no longer exists. The action is not wrong in itself -- it was correct for the state the controller observed. It is wrong for the state the plant is in when the action arrives. The critical threshold is not fixed at 1. In high-gain control loops, instability can onset at T_u / T_p well below 1, because the controller's aggressive corrections amplify the phase lag introduced by the delay. The ratio-equals-1 heuristic identifies where the problem is *likely to become significant*; the actual stability boundary depends on the controller's gain and the plant's damping.

The actuation ratio determines control viability. As T_u / T_p grows:

- Effective control bandwidth shrinks (the controller cannot respond to disturbances faster than the round-trip delay)
- Oscillation risk increases (the controller corrects for states that have already been corrected or have evolved past the correction)
- Stability margins degrade (the phase margin of the control loop is eaten by the actuation delay)

**Loop delay ratio: (T_o + T_u) / T_p.** In any closed-loop system, Layers 3 and 4 compose. The controller observes the plant with delay T_o, computes a response, and actuates with delay T_u. The plant state at the moment of actuation is at least (T_o + T_u) older than the state the controller computed its action against. Many real failures are not observation-dominant or actuation-dominant in isolation — they are loop-delay failures where the round-trip time exceeds the plant's tolerance. The loop delay ratio is the primary stability diagnostic for any closed-loop system: when (T_o + T_u) / T_p approaches or exceeds 1, the controller is correcting for states that have already been superseded, and oscillation or instability is likely. The MATI (Maximum Allowable Transfer Interval) literature formalizes specific bounds on this ratio for classes of networked control systems [7].

**Synchronization ratio: T_s / T_p.** When this ratio is small, nodes can meaningfully coordinate on the basis of shared timestamps. When this ratio approaches or exceeds 1, timestamp-based coordination becomes ambiguous. Two nodes that disagree about "now" by an amount comparable to the plant timescale cannot usefully coordinate on the basis of temporal ordering alone.

The synchronization ratio determines coordination viability. As T_s / T_p grows:

- Causal ordering becomes ambiguous (events that are temporally close relative to the plant may be ordered differently by different nodes)
- Coordination protocols that assume shared ordering break silently (distributed consensus, leader election, optimistic concurrency)
- Temporal fencing fails (a lock that expires "in T seconds" may expire at different real times on different nodes)

**Divergence ratio: T_contract / T_c.** This ratio compares the duration of temporal contracts to the clock divergence horizon — the time before local clocks diverge enough to invalidate those contracts. When T_contract / T_c is small, contracts expire well before clocks diverge significantly, and clock interchangeability holds within operational tolerances. When T_contract / T_c approaches or exceeds 1, the contract spans a period in which clocks have diverged enough to change its meaning: a deadline that means one thing to the issuer means a different thing to the recipient. Leases expire prematurely or late. Validity windows drift. Freshness guarantees become unreliable.

### 4.3 Dominance and Triage

In any given system, one ratio will dominate. That ratio determines the system's primary temporal failure mode.

| Dominant ratio | Primary failure mode | Symptom class |
|---|---|---|
| T_o / T_p | Estimator collapse | Acting on stale state; model-reality divergence; systematic overshoot |
| T_u / T_p | Control instability | Oscillation; overcorrection; induced volatility; the system causes the disturbance it was trying to suppress |
| (T_o + T_u) / T_p | Closed-loop instability | Round-trip delay exceeds plant tolerance; neither observation nor actuation is dominant alone, but their sum is |
| T_s / T_p | Coordination breakdown | Ordering ambiguity; split-brain; conflicting decisions from nodes that disagree about sequence |
| T_contract / T_c | Contract rot | Leases and deadlines that mean different things to different parties; freshness guarantees that silently expire |

The loop-delay ratio is a composite diagnostic derived from Layers 3 and 4 rather than a separate layer. It appears in the table because many real failures are round-trip failures where neither the observation ratio nor the actuation ratio alone exceeds its threshold, but their sum does. A system with T_o / T_p = 0.4 and T_u / T_p = 0.4 looks healthy on each individual ratio but has a loop delay ratio of 0.8 — close to the stability boundary.

The triage principle: **start with the ratio that has the least remaining margin to its critical threshold.** A system with T_o / T_p >> 1 does not have a coordination problem or a control-design problem. It has a state estimation problem. Improving the control algorithm or the synchronization protocol will not help. Only reducing observation latency (or accepting the degraded estimate and designing for it) addresses the actual failure. When multiple ratios are near their thresholds simultaneously, the system is temporally fragile across layers, and the interaction between layers (Section 3.5) must be considered.

This is why many coordination failures are temporal failures wearing other labels. The system is diagnosed as having a "communication problem" (T_s / T_p is high), a "decision-making problem" (T_o / T_p is high), or a "responsiveness problem" (T_u / T_p is high). The ratio analysis strips the label and reveals the structural constraint.

### 4.4 Temporal Coherence as a Control Resource

Temporal coherence is not a single property. It is the bounded compatibility of four distinct operational conditions:

- **Coherence as convention** (gauge layer): the degree to which nodes share a temporal reference frame. Measured by synchronization precision T_s. Consumed by any operation that relies on shared timestamps or global ordering.

- **Coherence as bounded mismatch** (clock layer): the degree to which local elapsed times remain interchangeable. Measured by divergence rate and resynchronization interval. Consumed by any temporal contract (deadline, lease, validity window) that spans nodes.

- **Coherence as estimation quality** (inference layer): the degree to which state estimates approximate current reality. Measured by observation latency T_o relative to plant dynamics T_p. Consumed by any decision based on remote state.

- **Coherence as phase margin** (control layer): the degree to which control actions arrive in time to address the state they were computed for. Measured by actuation latency T_u relative to plant dynamics T_p. Consumed by any closed-loop control action.

Each form of coherence is a resource with a budget. Synchronization precision requires energy, bandwidth, and protocol overhead to maintain. State estimation quality requires measurement frequency, sensor fidelity, and model accuracy. Control viability requires low-latency actuation channels. Clock interchangeability requires periodic resynchronization or high-quality local oscillators.

When the budget is exhausted -- when a ratio exceeds its critical threshold -- the system does not fail uniformly. It fails at the specific layer whose budget ran out first. The failure geometry is determined by which resource was scarce, not by the system's overall complexity.

This is why temporal coherence should be treated as a governed resource rather than an assumed property. Governed, in the sense that:

- temporal assumptions should be explicit design parameters, not silent defaults
- coherence budgets should be measured and allocated, not hoped for
- violations should be detected and handled, not misdiagnosed as other kinds of failure
- the cost of maintaining each form of coherence should be weighed against the cost of designing for its absence

A system that explicitly budgets its temporal coherence -- that knows its observation ratio, its actuation ratio, its synchronization precision, and its clock divergence horizon -- can make informed tradeoffs. A system that assumes temporal coherence without measuring it will discover its budget limitations through failure.

---

## 5. Case Studies

The four-layer model is not an abstract taxonomy. It is a diagnostic framework that should make systems legible. Three exemplars demonstrate the framework operating at different scales, in different domains, with different dominant failure modes.

### 5.1 GPS: All Four Layers, Non-Negotiable

GPS is the cleanest exemplar because relativistic effects make all four temporal failure modes simultaneously non-negotiable, precisely quantified, and well-documented [10].

**Layer 1 (gauge mismatch).** GPS satellites and ground receivers occupy different gravitational potentials and move at different velocities. There is no observer-independent "now" shared between a satellite at 20,200 km altitude and a receiver on the ground. The GPS system constructs a shared temporal reference frame — GPS Time — through a network of ground stations and atomic clocks. This is gauge construction: a synchronization convention, not a discovered simultaneity.

**Layer 2 (clock divergence).** Satellite clocks run faster than ground clocks by approximately 38 microseconds per day (45 μs/day from gravitational time dilation minus 7 μs/day from kinematic time dilation). The factory clock offset — setting the satellite oscillator to 10.22999999543 MHz instead of the nominal 10.23 MHz — is a permanent compensation for this divergence. Without it, position errors would accumulate at approximately 10 km/day. This is not a bug fix. It is an explicit acknowledgment that one second in orbit is not the same duration as one second on the ground.

**Layer 3 (retarded-state estimation).** A GPS receiver computes its position from signals that left the satellite approximately 67 milliseconds ago (at the speed of light over ~20,200 km). The position computed from these signals is the receiver's position 67 milliseconds in the past — or more precisely, a weighted estimate based on signals from multiple satellites, each with different propagation delays. For a stationary receiver, 67 milliseconds of staleness is irrelevant. For a vehicle moving at highway speed (~30 m/s), the receiver has moved approximately 2 meters since the signals departed. For a fighter jet at Mach 2 (~680 m/s), the receiver has moved approximately 45 meters. The observation is never current. The question is whether the staleness matters given the plant dynamics.

**Layer 4 (delayed actuation).** GPS itself does not close a control loop — it provides position estimates that other systems use for control. But the systems that depend on GPS inherit the actuation delay problem. A drone using GPS for position hold receives a position estimate that is 67+ milliseconds old (plus processing time), computes a correction, and sends that correction to its motors. The correction addresses a position the drone occupied some time ago. The plant (the drone's position) has evolved. The control action arrives late. This is why high-performance drone control uses inertial measurement for inner-loop stabilization (millisecond-scale T_o) and GPS only for outer-loop position correction (where 100ms staleness is acceptable relative to position-change timescales).

**Diagnostic.** In GPS, the dominant ratio depends on the application. For surveying (stationary plant, T_p → ∞), all ratios are negligible. For automotive navigation (T_p ~ seconds), the observation ratio T_o/T_p ~ 0.01 is comfortable. For precision drone control (T_p ~ 10ms for attitude), the observation ratio T_o/T_p ~ 10 — ten times the plant timescale — which is why GPS cannot be the primary control input for attitude stabilization. The same measurement system serves all three applications, but the dominant failure mode changes because the plant timescale changes.

### 5.2 Networked Control Systems: Prior Art and Extension

Networked control systems (NCS) — where sensors, controllers, and actuators communicate over a shared network rather than dedicated wiring — are the domain where Layers 3 and 4 have been most rigorously studied [7]. The NCS literature provides the formal machinery for much of the ratio analysis in Section 4, and it is worth situating the present framework against it.

Hespanha, Naghshtabrizi, and Xu's survey [7] identifies the core NCS challenges: variable sampling intervals, network-induced delays in both the sensor-to-controller and controller-to-actuator channels, and packet dropout. Their four-component model (plant, sensor, controller, actuator) with two delay channels maps directly onto Layers 3 and 4 of the present framework. The Maximum Allowable Transfer Interval (MATI) — the longest interval between sensor updates that still guarantees stability — is a specific instance of the critical threshold for T_o / T_p: the observation ratio beyond which the estimator cannot maintain the stability guarantee.

What the NCS literature does not do, and what the present framework adds, is unify the delay analysis with Layers 1 and 2. NCS assumes a shared time base (gauge mismatch resolved) and interchangeable clocks (no clock divergence). These assumptions hold within a single factory floor or vehicle, where all nodes share a time source. They do not hold in wide-area networked control (multi-site industrial systems, inter-vehicle coordination, cloud-edge control), in institutional decision systems (where "nodes" are departments with different reporting cycles), or in any system where the temporal reference frame is itself uncertain. The four-layer framework generalizes NCS by asking what breaks when the NCS assumptions about Layers 1 and 2 are relaxed.

### 5.3 Institutional Governance: Temporal Failure at Human Timescales

Institutional governance systems — regulatory enforcement, content moderation, organizational decision-making — exhibit the same four-layer failure structure at timescales of hours, days, and quarters rather than milliseconds.

**Layer 1 (gauge mismatch).** Different departments, agencies, or decision-makers operate on different temporal reference frames. The finance team reports quarterly. The engineering team reports in sprints. The legal team reports in case cycles. There is no institutional "now" — the organization's state is a composite of measurements taken at different times, on different cycles, with different definitions of "current." This is gauge mismatch: not clock error, but the absence of a shared temporal convention.

**Layer 2 (clock divergence).** In institutional systems, "clock divergence" is organizationally instantiated rather than physically oscillator-based — but the structural consequence is the same: elapsed time as measured by one subsystem is not interchangeable with elapsed time as measured by another. Institutional clocks diverge through policy lag, reporting delay, and bureaucratic processing time. A regulation drafted in response to conditions observed two years ago, reviewed for eighteen months, and enforced starting next quarter is a temporal contract whose clock has drifted far from the system it governs. The regulation addresses a past state. The regulated system has evolved. Carpenter's analysis of bureaucratic delay [18] formalizes one mechanism: regulatory agencies delay action as an optimal response to uncertainty, but the delay itself changes the system being regulated.

**Layer 3 (retarded-state estimation).** All institutional state estimates are retarded. A CEO's understanding of organizational culture is based on surveys taken last quarter, reports filtered through middle management, and anecdotes from hallway conversations months ago. A regulator's understanding of market conditions is based on filings from last quarter, investigations that began years ago, and economic indicators that lag the phenomena they measure by weeks to months. The observation is never current. The institutional "state estimate" is always an inference from past measurements plus a model of how the institution has evolved since. When the model is wrong — when conditions have changed faster than the reporting cycle — the estimate is fiction.

Content moderation provides a particularly clean example. A post is published. It is flagged, by algorithm or user report, after some delay. It enters a review queue. A moderator reviews it hours or days later. The enforcement action — removal, labeling, or restriction — arrives at a conversation that has already moved on. Trujillo et al. [14] document that delayed takedown makes moderation ineffective: by the time content is removed, the audience has already been exposed and the conversation has already incorporated the content's effects. The moderation system is controlling a plant (the conversation) whose dynamics (minutes to hours) are faster than the observation-actuation loop (hours to days). The actuation ratio T_u / T_p >> 1. The control action arrives after the plant has left the state it was computed to address.

**Layer 4 (delayed actuation).** Institutional control actions — policy changes, enforcement actions, resource allocation — propagate with delay. A central bank adjusts interest rates based on indicators measured last quarter, through a decision process that takes weeks, implementing changes that take months to propagate through the economy. The round-trip delay (T_o + T_u) may be measured in quarters. If the economic dynamics being targeted operate on a similar timescale, the bank's corrections can induce the volatility they were designed to suppress. The bank is not incompetent. It is a delayed controller operating on a plant whose dynamics are comparable to its loop delay.

**Diagnostic.** Institutional governance failures are routinely attributed to bad policy, poor communication, or institutional incompetence. The four-layer framework offers a different diagnosis: the institution may have the right policy, executed by competent people, with adequate communication — and still fail because the temporal ratios are wrong. The observation is too old. The control action arrives too late. The temporal reference frames are misaligned. The clocks have diverged. In institutional settings, temporal mismatch is not always the sole cause of failure; it can act as a primary driver, an amplifier of incentive misalignment or capacity shortage, or an overlay that converts ordinary administrative limits into visible control failure. The diagnostic contribution is not a claim that all institutional failures are temporal. It is a claim that the temporal component is under-modeled, and in some cases temporality is the dominant control variable.

### 5.4 Cross-Domain Pattern

The three exemplars — GPS, networked control systems, institutional governance — span temporal scales from nanoseconds to quarters. The four-layer structure is invariant across these scales. What changes is:

- Which layer dominates (GPS: Layers 1-2 are non-negotiable; NCS: Layers 3-4 dominate; institutions: all four are large)
- What mitigations are available (GPS: factory clock offsets and mathematical corrections; NCS: estimators and predictors; institutions: faster reporting cycles, shorter decision processes, standing authority for rapid response)
- How visible the temporal failure is (GPS: precisely quantified; NCS: measurable in simulation and experiment; institutions: typically misdiagnosed as something else)

The diagnostic contribution of the framework is greatest in the last case: institutional systems where temporal failures are routinely attributed to other causes. The timescale ratio analysis does not solve the institutional problem, but it names the structural constraint that the institution must satisfy to avoid the failure. Whether the institution can satisfy it — whether it can observe faster, act faster, synchronize better, or redesign its temporal contracts — is a separate question. The framework says what must be true, not how to make it true.

---

## 6. Temporal Coherence as a Governed Resource

Section 4.4 introduced the claim that temporal coherence is a scarce control resource with a budget. This section develops the operational consequences.

### 6.1 Coherence Budgets

A coherence budget is an explicit accounting of how much temporal imprecision a system can tolerate before a specific function degrades. The budget is not a single number. It decomposes across the four layers:

- **Synchronization budget:** How much gauge mismatch can the system tolerate before ordering-dependent operations produce incorrect results? For a distributed database with timestamp-based concurrency, this is the uncertainty interval that commits must wait out (Spanner's TrueTime). For an institutional reporting system, this is the maximum acceptable difference in reporting periods across departments before aggregate figures become misleading.

- **Divergence budget:** How much clock drift can the system tolerate before temporal contracts rot? Measured as the ratio of accumulated divergence to the shortest temporal contract in the system. When accumulated drift exceeds the shortest lease, timeout, or validity window, the first contract failure occurs.

- **Freshness budget:** How stale can the most recent observation be before decisions based on it become unreliable? This is the observation ratio T_o / T_p restated as a constraint: for a given plant volatility, there is a maximum acceptable observation age beyond which the state estimate's expected error exceeds the decision's tolerance.

- **Actuation budget:** How much delay can the control channel tolerate before the control action addresses a state that has changed beyond the action's useful range? This is the actuation ratio T_u / T_p restated as a stability constraint.

**Worked example: content moderation coherence budget.** Consider a platform where harmful content has a measurable impact window — the period during which a post is actively being viewed and shared. Suppose the median impact window (the plant timescale T_p) is 4 hours for viral content and 48 hours for slow-burn policy violations.

The platform's temporal budget:

- *Freshness budget:* Automated flagging takes ~10 minutes (T_o = 0.17 hours). For viral content, T_o / T_p = 0.04 — comfortable. For a human review queue with an average wait of 18 hours, T_o / T_p = 4.5 for viral content and 0.38 for slow-burn content. The queue is within budget for slow-burn violations but far over budget for viral harm: the observation is 4.5 plant-timescales old by the time a human sees it.
- *Actuation budget:* After review, the enforcement action (removal, labeling) is effectively instantaneous — T_u ≈ 0. But if the enforcement is an appeal process or policy change, T_u may be days to weeks.
- *Loop delay:* For automated flagging + immediate removal: (T_o + T_u) / T_p ≈ 0.04 — well within budget. For human review + removal: (18 + 0) / 4 = 4.5 — the loop delay is 4.5 times the plant timescale for viral content. The moderation system is controlling a plant that has already moved.
- *Divergence budget:* Different moderation teams may be operating on different policy versions (updated weekly, monthly, or ad hoc). If policy updates arrive monthly and harmful content evolves weekly, T_contract / T_c > 1 — the policy contract rots before the divergence cycle completes.

The budget analysis reveals why automated moderation works for fast-evolving harm (the observation ratio stays small) and why human review fails for the same content (the observation ratio exceeds the plant timescale). This is not a staffing problem — it is a temporal architecture mismatch. Adding more moderators reduces the queue wait (T_o), which helps. But if the queue wait cannot be reduced below T_p, the system is structurally incapable of timely intervention regardless of headcount.

Each budget is consumed by operations and replenished by maintenance: synchronization protocols replenish the synchronization budget, clock resynchronization replenishes the divergence budget, fresh measurements replenish the freshness budget, and faster actuation channels replenish the actuation budget. When replenishment stops — the synchronization protocol fails, the resync schedule slips, measurements stop arriving, the actuation channel congests — the budget depletes toward zero and the system drifts toward the failure mode corresponding to the exhausted layer.

### 6.2 Temporal Contracts

A temporal contract is any agreement whose terms include elapsed time, deadlines, or validity windows. Temporal contracts are pervasive:

- Leases ("this lock is valid for 30 seconds")
- TTLs ("this cache entry expires in 5 minutes")
- Deadlines ("this request must complete by 14:00 UTC")
- Validity windows ("this certificate is valid from March 1 to March 31")
- Reporting periods ("this metric reflects data from Q4 2025")
- Freshness guarantees ("this state estimate is no more than 100ms old")

Every temporal contract implicitly assumes that the clocks involved agree on the duration, that the reference frame is shared, and that the contract's validity horizon is shorter than the divergence horizon. The four-layer framework makes these assumptions explicit and auditable:

- Does the contract specify *which clock*?
- What is the maximum divergence between the issuer's clock and the enforcer's clock over the contract's lifetime?
- Does the contract's validity horizon exceed the divergence budget?
- Does the contract account for observation delay (the contract may have expired by the time the enforcer learns of the event it governs)?

Temporal contracts that do not answer these questions are temporally incoherent by default. They may work — most do, most of the time, because the divergences are small relative to the contract terms. But when divergences grow — under load, at scale, across geographic distance, across institutional boundaries — the contracts rot silently.

### 6.3 Revalidation Triggers

A revalidation trigger fires when a coherence budget is approaching exhaustion. The trigger does not fix the temporal failure. It flags that the system is operating on assumptions that may no longer hold and that decisions made under those assumptions should be treated as provisional.

For state estimates: revalidate when the observation age exceeds a threshold fraction of the plant timescale. The threshold depends on the plant's volatility and the decision's sensitivity — a collision avoidance system needs a lower threshold than an inventory system.

For temporal contracts: revalidate when accumulated clock divergence exceeds a threshold fraction of the shortest active contract. The threshold depends on the contract's tolerance — a distributed lock needs a tighter threshold than a cache TTL.

For control actions: revalidate when the actuation delay exceeds a threshold fraction of the control loop's stability margin. The threshold depends on the controller's gain and the plant's damping.

The key insight is that revalidation is itself a temporal operation with its own costs and delays. A system that revalidates too frequently wastes resources. A system that revalidates too rarely operates on stale assumptions. The optimal revalidation frequency is itself a function of the coherence budget — a temporal resource allocation problem.

### 6.4 Connection to Prior Series Work

The temporal coherence resource framework unifies several constructs from earlier papers in this series:

- **Δt-constrained inference** [2] established that confidence growth must not exceed evidence accumulation rate. The freshness budget is the observation-layer instantiation of this constraint: state-estimate confidence must not exceed the evidence quality implied by the observation's age.

- **The temporal attack surface** [3] identified adversarial exploitation of temporal gaps. Coherence budget depletion is the vulnerability; the attacker's strategy is to act in the interval between budget exhaustion and revalidation — the window where the system operates on assumptions that no longer hold.

- **The gain geometry of temporal mismatch** [4] characterized the signed effect of Δt separation. The coherence budget determines which regime the system operates in: when all budgets are healthy, the system is in the coherent regime; as budgets deplete, the system transitions through the shear, leverage, and capture regimes identified in that paper.

- **Cybernetic fault domains** (Paper 15) formalized commitment-verification lag. The actuation budget provides the temporal grounding: commitments outrun verification precisely when the actuation ratio exceeds the system's ability to verify state before acting on it.

A parallel formalization of the Δt framework in Lean applies the same scope discipline at finer grain. The formalization separates static claims (closure classification and reachability in the cybernetic failure taxonomy) from dynamic claims (rollback depletion, recovery taxonomy, Δc→Δh persistence), with a boundary axiom explicitly marking where static commitments end. The four-layer temporal decomposition presented here occupies the temporal-claim side of that boundary: its content is operational control theory, and its critical quantities are timescale ratios rather than reachability classes. A cross-layer formalization index is maintained in the papers repository (`docs/formalization-index.md`).

The four-layer framework does not replace these prior results. It identifies the common substrate — four distinct temporal resources whose depletion produces the specific failure modes each prior paper characterized in domain-specific form.

---

## 7. Design Implications

The four-layer framework implies several design principles. These are not novel in isolation — many are well-known in specific domains (distributed systems, control engineering, real-time computing). The contribution is collecting them under a single temporal-failure model and stating them as layer-specific constraints rather than general best practices.

### 7.1 Make Temporal Assumptions Explicit

Every distributed system embeds temporal assumptions. Most embed them silently. The first design implication is to surface them:

- What synchronization convention does the system use? What is its precision?
- What clock sources does the system depend on? What is their drift rate? When are they resynchronized?
- What is the maximum observation latency for each input? What is the freshness guarantee?
- What is the actuation latency for each output? What state changes can occur during transit?

A system that cannot answer these questions does not know its coherence budget. It is operating on temporal assumptions that it has never audited. The four-layer decomposition provides the audit checklist.

### 7.2 Separate Four Timestamps

Every event in a distributed system has at least four temporal coordinates:

- **Event time (t_event):** when the event occurred at the plant.
- **Observation time (t_obs):** when the controller received the measurement. Always later than t_event by at least T_o.
- **Decision time (t_dec):** when the controller computed the response. Always later than t_obs by at least the computation time.
- **Effect time (t_effect):** when the control action arrived at the plant. Always later than t_dec by at least T_u.

Systems that collapse these into a single timestamp — "time" — lose the ability to diagnose which temporal layer failed. A log entry that says "event at 14:03:22" does not distinguish between "the event occurred at 14:03:22" and "we learned about the event at 14:03:22." When the system fails, this distinction is often the diagnostic.

### 7.3 Track Observation Age as First-Class Metadata

Every state estimate should carry its age: the interval between the measurement it is based on and the current time. This is the AoI concept [9] applied as a design pattern rather than a research metric.

Observation age is not a debugging aid. It is an operational parameter. A state estimate with an age of 50ms is a different input from the same estimate with an age of 500ms, even if the values are identical. A decision-maker that does not know the age of its inputs cannot assess whether its decisions are grounded in current reality or past fiction.

The practical implementation is straightforward: attach a generation timestamp to every measurement, compute age at the point of use, and expose age to decision logic. The engineering cost is minimal. The diagnostic value is substantial: observation age anomalies — sudden spikes, persistent staleness, periodic gaps — are early indicators of Layer 3 degradation.

### 7.4 Audit Temporal Contracts for Clock Non-Interchangeability

Every lease, timeout, TTL, deadline, and validity window in a distributed system should be audited against the divergence budget:

- What clocks does the contract span?
- What is the maximum divergence between those clocks over the contract's lifetime?
- Does the contract's tolerance exceed the maximum divergence? If not, the contract will occasionally fail even when the system is functioning correctly.

In practice, most temporal contracts are specified with margins that implicitly (and unknowingly) account for clock divergence. A 30-second lock with a 5-second safety margin works as long as clock divergence over 30 seconds is less than 5 seconds — which it almost always is for commodity hardware on a local network. The audit reveals which contracts are at risk and under what conditions. It does not require changing contracts that work. It requires knowing *why* they work and what would make them stop.

### 7.5 Distinguish State Records from State Estimates

A state record is a fact about the past: "at time t, the measurement was x." A state estimate is an inference about the present: "given the measurement at time t and the plant model, the current state is approximately x̂." These are different epistemic objects with different reliability properties. A state record is as reliable as the sensor. A state estimate is as reliable as the sensor *and* the model *and* the freshness of the measurement.

Systems that conflate records and estimates — that treat "the last known state" as "the current state" — are smuggling in Layer 3 assumptions without auditing them. The design implication is to distinguish them in data structures, APIs, and decision logic. A state estimate should carry its provenance: which measurement it is based on, what model was used, and what the expected error is given the measurement age.

### 7.6 Design for Bounded Incoherence, Not Ideal Simultaneity

The deepest design implication is a shift in default assumption. Most distributed systems are designed as though temporal coherence is free and unlimited — as though clocks agree, observations are fresh, and control actions are instantaneous — and then patched when failures reveal that the assumption was wrong.

The four-layer framework suggests inverting the default: design for bounded temporal incoherence. Assume that clocks will diverge, observations will be stale, and control actions will be late. Specify the bounds. Design the system to function correctly within those bounds and to degrade gracefully when the bounds are exceeded.

This is not a counsel of pessimism. It is the same engineering discipline that treats bandwidth as finite, memory as bounded, and failure as possible. Temporal coherence is a resource. Treating it as one — measuring it, budgeting it, monitoring it, and designing for its absence — produces systems that fail informatively rather than mysteriously.

---

## 8. Conclusion

Distributed systems fail temporally because they assume temporal resources they do not have: a shared present, interchangeable clocks, fresh observations, and timely control. The four-layer decomposition — gauge mismatch, clock divergence, retarded-state estimation, delayed actuation — separates these assumptions and identifies the distinct failure mode each produces when violated.

The diagnostic contribution is the timescale ratio analysis. The dominant failure mode in a given system is determined by which ratio — observation latency to plant dynamics, actuation latency to plant dynamics, round-trip loop delay to plant dynamics, synchronization uncertainty to plant dynamics, and contract duration to clock divergence horizon — has the least remaining margin to its critical threshold. This is an engineering question with measurable inputs and testable predictions. A system whose observation ratio exceeds 1 does not have a communication problem or a policy problem. It has a state estimation problem. The ratio names the constraint. The constraint determines the failure mode.

The individual layers are well-studied. Gauge construction is the subject of clock synchronization theory from Lamport [5] through Spanner [6]. Clock divergence is the subject of relativistic geodesy and distributed systems timekeeping. Retarded-state estimation is the subject of networked control systems [7] and the Age of Information literature [9]. Delayed actuation is the subject of classical control under delay from Smith [8] through MATI analysis. What is new is the unified diagnostic framework that identifies which of these four resources is scarce in a given system and predicts where failure will occur.

The practical claim is that temporal coherence should be governed — budgeted, measured, and monitored — rather than assumed. Systems that treat temporal coherence as an invisible default discover its limits through failure. Systems that treat it as a scarce resource with measurable budgets and explicit contracts can diagnose failures by layer, triage by ratio, and design for bounded incoherence rather than ideal simultaneity.

Many coordination failures contain a temporal component that is under-modeled, and in some cases temporality is the dominant control variable. The four-layer model and ratio analysis provide the vocabulary to identify that component, assess whether it is primary or secondary, and name the structural constraint.

---

## Acknowledgments

Language-model tools were used for editorial critique and literature discovery during preparation of this manuscript; all arguments, interpretations, and errors are the author's own.

---

## References

[1] Beck, J. (2025). Temporal Closure Requirements for Synthetic Coherence: Architectural Foundations and the Simulator Gap. Preprint, Δt Framework Paper 6. doi:10.5281/zenodo.17849277

[2] Beck, J. (2025). Δt-Constrained Inference: A General Model of Temporal Coherence in Hierarchical Systems. Preprint, Δt Framework Paper 7. doi:10.5281/zenodo.17857541

[3] Beck, J. (2026). The Temporal Attack Surface: A Δt Framework for Asynchronous Security Systems. Preprint, Δt Framework Paper 14. doi:10.5281/zenodo.18236164

[4] Beck, J. (2026). The Gain Geometry of Temporal Mismatch: Shear, Leverage, and Capture in Multi-Timescale Systems. Preprint, Δt Framework Paper 16. doi:10.5281/zenodo.18717619

[5] Lamport, L. (1978). Time, Clocks, and the Ordering of Events in a Distributed System. *Communications of the ACM*, 21(7), 558-565.

[6] Corbett, J.C. et al. (2013). Spanner: Google's Globally-Distributed Database. *ACM Transactions on Computer Systems*, 31(3), Article 8.

[7] Hespanha, J.P., Naghshtabrizi, P., and Xu, Y. (2007). A Survey of Recent Results in Networked Control Systems. *Proceedings of the IEEE*, 95(1), 138-162.

[8] Smith, O.J.M. (1957). Closer Control of Loops with Dead Time. *Chemical Engineering Progress*, 53(5), 217-219.

[9] S. Kaul, R. Yates, and M. Gruteser, "Real-Time Status: How Often Should One Update?" IEEE INFOCOM, 2012.

[10] N. Ashby, "Relativity in the Global Positioning System," *Living Reviews in Relativity*, 6(1), 2003.

[11] P. Kokotovic, H. Khalil, and J. O'Reilly, *Singular Perturbation Methods in Control: Analysis and Design*, SIAM Classics, 1986.

[12] F. Cristian and C. Fetzer, "The Timed Asynchronous Distributed System Model," *IEEE Transactions on Parallel and Distributed Systems*, 10(6), 642-657, 1999.

[13] J. Cipar, "Trading Freshness for Performance in Distributed Systems," PhD Thesis, Carnegie Mellon University, CMU-CS-14-144, 2014.

[14] L. Trujillo et al., "Delayed Takedown of Illegal Content on Social Media Makes Moderation Ineffective," arXiv:2502.08841, 2025.

[15] J. Muller et al., "The Effectiveness of Moderating Harmful Online Content," *PNAS*, 120(34), 2023.

[16] H. Kopetz, "Time-Triggered Real-Time Computing," *Annual Reviews in Control*, 27(1), 3-13, 2003.

[17] T. Nauta et al., "Stealthy Computational Delay Attacks on Control Systems," ACM/IEEE ICCPS, 2025.

[18] D. Carpenter, "Why Do Bureaucrats Delay? Lessons from a Stochastic Optimal Stopping Model," in *Politics, Policy, and Organizations*, U Michigan Press, 2002.

[19] R.D. Yates, Y. Sun, D.R. Brown, S.K. Kaul, E. Modiano, and S. Ulukus, "Age of Information: An Introduction and Survey," *IEEE Journal on Selected Areas in Communications*, 39(5), 1183-1210, 2021.

[20] M.J. Fischer, N.A. Lynch, and M.S. Paterson, "Impossibility of Distributed Consensus with One Faulty Process," *Journal of the ACM*, 32(2), 374-382, 1985.

[21] H. Kopetz and W. Steiner, "Temporal Consistency of Data and Information in Cyber-Physical Systems," arXiv:2409.19309, 2024.

[22] S. Bulusu et al., "SoK: Resilience and Fault Tolerance in Cyber-Physical Systems," arXiv:2512.20873, 2025.
