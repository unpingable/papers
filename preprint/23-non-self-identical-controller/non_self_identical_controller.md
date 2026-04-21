---
header-includes:
  - \usepackage{booktabs}
---

# Ops Is Control with a Non-Self-Identical Controller

**James Beck**
Independent Researcher

**Date:** April 2026

**Series:** Δt Framework, Paper 23

**Status:** Preprint v0.1 (initial draft, 2026-04-21; not yet pushed to Zenodo)

---

## Abstract

We study two distinct failure modes of controller continuity in operational systems. **Continuity of action** concerns whether the controller can still intervene in time: handoff distortion, authority-routing delay, and fatigue-induced contraction loss jointly consume a viability budget that can be stated as a single inequality. **Continuity of identity** fails when the controller's real composition differs from the nominal controller in ways the measurement-and-authority map cannot resolve: under three sufficient masking conditions, latent human compensation becomes structurally unidentifiable from observed outputs. Classical control assumes the controller is self-identical across time. Operations begin where that assumption breaks.

**Keywords:** controller continuity, hybrid control, operational systems, identifiability, viability theory, switched systems, human supervisory control, resilience engineering, authority routing

## 1. Thesis and scaffold

Classical control theory usually treats the controller as a stable object. Switched-systems, time-varying, and reconfigurable-control frameworks permit the controller to change, but typically assume its identity at each instant is *specified*: the loop knows which controller it currently is. Real operational systems violate that weaker assumption. The controller is handed off, reconstituted, partially authorized, quietly supplemented by undocumented human compensation, and degraded by fatigue or ambiguity, often in ways the loop cannot resolve from observed behavior. The result is not merely plant instability. It is instability produced by controller composition being partially reset, delayed, supplemented, or structurally unrecoverable in time.

This suggests a hybrid system in which the controller itself evolves through flows and jumps. Let the augmented state be

$$\xi_t = (x_t, \hat{x}_t, c_t, \theta_t, A_t)$$

where $x_t$ is the plant state, $\hat{x}_t$ the estimated plant state, $c_t$ the controller's internal context or working state, $\theta_t$ its operative parameters, and $A_t$ the currently admissible action set or authority state. The realized control action is

$$u_t = \Pi_{A_t}\!\big(C_{\theta_t}(\hat{x}_t, c_t) + H_t(z_t)\big)$$

where $C_{\theta_t}$ is the nominal controller, $H_t$ is a latent human compensator acting on undocumented side information $z_t$, and $\Pi_{A_t}$ projects intended action into the currently authorized region. Here $z_t$ may include genuinely exogenous side information, but it may also include a differently interpreted subset of the ordinary observation stream $y_t$ — tacit calibration, undocumented priors, pattern knowledge not represented in the nominal controller. The plant evolves by

$$x_{t+1} = f(x_t, u_t, w_t), \qquad y_t = h(x_t, v_t)$$

with disturbance $w_t$ and observation noise $v_t$.

Controller continuity fails along two orthogonal axes.

**Continuity of action** asks: can the realized action reach the plant in time, given handoff-induced reset of $(\hat{x}, c)$, authority-routing delay on $A_t$, and fatigue-induced drift or fracture of $\theta_t$? This is a viability question.

**Continuity of identity** — meaning continuity of controller *composition*, not continuity of which person is on shift — asks: can the realized composition $C + H$ be recovered from the outputs the measurement-and-authority map produces? This is an identifiability question.

The four operational failure families in the literature — handoff, escalation, hidden compensation, fatigue — distribute across these two axes rather than forming an unstructured list. Handoff and fatigue are action-side. Masking is identity-side. Authority straddles: its delay is an action-side effect, but the projection $\Pi_{A_t}$ defines the map under which identity is obscured.

**Ops is control with a non-self-identical controller.**

The phrase "non-self-identical controller" is used here in a precise sense. It names the failure to recover the realized controller composition $C + H$ from outputs observed under the system's primary measurement-and-authority map $(\Pi_{A_t}, h)$. The thesis is therefore an identifiability claim on the controller side of the loop — structurally parallel to long-standing identifiability claims on the plant side, with the authority projection $\Pi$ functioning as part of the effective measurement map. It is not a claim about personal, organizational, or machine identity.

### 1.1 Scope boundary

The framework applies to operational systems in which the primary stabilizing controller remains partially or wholly human, and in which continuity of controller state, authority, or operative mode can still bind recovery. In fully automated subsystems — remedial action schemes, special protection systems, under-frequency load shedding, model-predictive emergency controllers — the classical self-identical-controller assumption is often restored by design. In highly engineered handoff environments — overlapping shifts, shared digital state, real-time historian replay — reset severity may be small enough that controller discontinuity is not the dominant constraint. The present object is therefore not "all control," but the hybrid human-operational layer where controller continuity remains a live systems problem.

This scope is also diagnostic. The places where the framework does not apply are often exactly the places where an organization has already spent engineering effort to restore controller self-identity — by automating the loop, engineering the handoff, or pre-delegating emergency authority. Such cases are not awkward exceptions; they are institutional repairs to controller discontinuity. That counterexamples cluster at already-solved cases is consistent with the underlying claim.

## 2. Continuity of action

Three dynamic sources consume the viability budget.

### 2.1 Handoff as reset map

At handoff, controller state is not transmitted directly. It is serialized under a bandwidth constraint, reconstructed by another operator, and partially cold-started:

$$c_{t^+} = D\!\big(S(c_{t^-}; B), r_t\big), \qquad \hat{x}_{t^+} = \hat{x}_{\mathrm{reinit}}$$

where $S$ is lossy serialization under budget $B$, $D$ is reconstruction, and $r_t$ is whatever residual context survives locally. This is not additive noise. It is a reset map; the outgoing and incoming controllers are not identical even if both are individually competent.

For the first pass it is enough to model the serialization loss coarsely. Let

$$S(c_{t^-}; B) = c_{t^-} + \eta_B,$$

where $\eta_B$ is a distortion term with magnitude bound $\|\eta_B\|$ monotone decreasing in handoff bandwidth $B$. Here $B$ should be read broadly: briefing time, artifact fidelity, ticket completeness, and the outgoing operator's ability to externalize state under load. The reconstruction delay induced by this reset — written $\delta_h$ and later decomposed into bandwidth, operator-state, and scene-ambiguity components in §2.4 — is the time required for the incoming operator to recover an actionable estimate from the distorted handoff and live telemetry. Higher $B$ does not eliminate reset; it shrinks the cold-start problem the incoming controller must solve.

The additive bounded-magnitude model $\|\eta_B\| \leq \epsilon(B)$ is a first-pass simplification; real handoffs are often *structurally* omissive rather than merely noisy. In practice $\eta_B$ is often biased rather than zero-mean — the outgoing operator emphasizes what they believe matters and omits what they do not know to be load-bearing — or structurally omissive, where an entire dimension of $c_{t^-}$ (an undocumented tacit calibration, a pattern-recognition habit) is dropped outright rather than noised. The worst handoffs are not Gaussian; they are selective. The model above should be read as a reset-magnitude bound, not as a noise process.

In the standard switched-systems form (Hespanha–Morse), if the Lyapunov function contracts with rate $\lambda \in (0,1)$ during flow and jumps by at most factor $\mu \geq 1$ at each reset, then stability of the overall hybrid trajectory requires an average dwell time satisfying

$$\tau_a > \frac{\log \mu}{-\log \lambda}.$$

Two caveats matter in the ops setting. First, $\mu$ is not scalar — handoffs vary in quality. The bound is really $\tau_a > \log \mu_{\sup} / (-\log \lambda)$ worst-case, or an expected form with a tail condition on $\mu$. Second, $\lambda$ depends on $\theta_t$: fatigue shrinks contraction, so the dwell-time requirement tightens as operators tire. Handoff and fatigue are not independent failure modes; they are coupled through one inequality.

### 2.2 Authority jump and the Institutional Ruin Condition

Operational systems separate observation from admissible action. An operator may know what needs to be done before they are permitted to do it. Escalation is therefore a jump in the admissible set:

$$A_{t^+} = A_{t^-} \cup \Delta A$$

triggered only after routing delay $\tau_{\text{auth}}$. The plant evolves during that delay under the constrained action set $A_t$, not the action set needed for rescue.

Let $V(A)$ be the viability kernel of the plant under authority set $A$: the set of states from which the plant can be kept inside the safe set indefinitely using actions in $A$. Define the **Institutional Ruin Condition**:

$$x_t \in V(A_{\text{expanded}}) \quad \text{and} \quad x_{t + \tau_{\text{auth}}} \notin V(A_{\text{expanded}}).$$

In words: at time $t$ a rescue trajectory exists in the future authorized set, but the plant's open-loop drift under the current set carries the state out of the reachable safe region before the authority jump occurs.

This separates two failure classes. **Technical ruin**: no admissible rescue exists even under expanded authority. **Governance-induced ruin**: rescue existed in principle, but the organization could not authorize it before the state exited the viability kernel. The second is not a metaphor; it is a delayed set-valued control problem.

### 2.3 Fatigue: wear versus fracture

Controller degradation has two regimes. **Wear** is slow parameter drift:

$$\theta_{t+1} = \theta_t + \epsilon \omega_t, \qquad \epsilon \ll 1,$$

which can be treated with ordinary time-scale separation arguments. The operator remains in a nominal mode with slightly degraded gains; stability is maintained via singular perturbation.

**Fracture** is a discrete mode switch. Pager storms, ambiguity shocks, and overload do not merely nudge parameters; they trigger a jump $\sigma: \theta_i \to \theta_j$ into a degraded controller mode:

$$\theta_{t^+} = \Psi(\theta_{t^-}, x_t, L_t) \quad \text{when } L_t > L_{\text{crit}}$$

where $L_t$ is a load or ambiguity measure and $\Psi$ selects the successor mode. Formally this is a switched-controller system (or Markov jump linear system in the stochastic version) in which the post-fracture mode $\sigma_{\text{degraded}}$ exhibits altered stability properties — typically, but not always, degraded. The common failure signatures are familiar: hesitation becomes bang-bang, cautious monitoring becomes oscillatory intervention, confidence collapse becomes freeze-then-overshoot. Less often, trained crisis mode or stress-induced hyper-focus produces a post-fracture mode that is more conservative than nominal. Fracture is not a slow operator; it is a qualitatively different controller, and the relevant question is what margin the new mode actually has.

### 2.4 The continuity budget

The three action-side failures compose into a single viability condition. After a disturbance, let $T_{\text{exit}}$ be the remaining open-loop time before the plant leaves $V(A_{\text{expanded}})$. Let $\delta_h$ be the effective reorientation delay induced by a handoff — the time the incoming operator needs to reach an actionable state estimate. This delay decomposes into three structurally distinct components:

$$\delta_h = \delta_{\text{serial}}(B) + \delta_{\text{reorient}}(\theta) + \delta_{\text{ambig}}(L).$$

$\delta_{\text{serial}}(B)$ is bandwidth-limited: the time to deserialize whatever the outgoing operator managed to externalize under budget $B$. $\delta_{\text{reorient}}(\theta)$ is operator-state-limited: the time for the incoming operator, with parameters $\theta$ (fatigue, tenure, familiarity with the plant), to build an actionable live-state estimate from the brief plus current telemetry. $\delta_{\text{ambig}}(L)$ is scene-limited: the irreducible time to resolve whatever genuine situational uncertainty the scene itself presents, a function of the same load/ambiguity measure $L$ introduced in §2.3. The rescue is reachable only if

$$\tau_{\text{auth}} + \delta_{\text{serial}}(B) + \delta_{\text{reorient}}(\theta) + \delta_{\text{ambig}}(L) < T_{\text{exit}}.$$

This inequality does useful work, and the decomposition makes it diagnostic rather than only elegant.

The four knobs are non-substitutable because each shrinks exactly one term. Shorter authority delay affects only $\tau_{\text{auth}}$. Higher handoff bandwidth shrinks only $\delta_{\text{serial}}$ — it does not reach operator state or scene ambiguity. Rested operators or task familiarity shrink $\delta_{\text{reorient}}$ without touching serialization or authority. Pre-staged playbooks, simulator-run exposure to the failure class, and scene-legibility interventions shrink $\delta_{\text{ambig}}$ alone. An organization buying continuity by investing only in handoff tooling is buying only $\delta_{\text{serial}}$ reduction; if the dominant term is $\delta_{\text{reorient}}$ (fatigue) or $\tau_{\text{auth}}$ (authorization latency), the investment does not move the margin.

Fatigue and handoff are therefore separately auditable in principle — $\theta$ drives $\delta_{\text{reorient}}$, not $\delta_{\text{serial}}$. In practice they become indistinguishable when organizations track only $B$ (brief length, ticket completeness) without tracking operator state or scene ambiguity. The coupling under a single scalar $\delta_h$ is a measurement choice, not a structural identity.

## 3. Continuity of identity

The two axes are orthogonal in definition but coupled in failure. A handoff reset that cold-starts $\hat{x}_t$ and degrades $c_t$, combined with delayed authority expansion and fatigue-shrunk contraction, forces the incoming operator to rely more heavily on latent compensatory action $H_t$ while situational awareness is being rebuilt. Those are also the conditions under which the measurement-and-authority map is least able to resolve the controller's real composition. The same continuity failures that consume the viability budget increase dependence on masked compensation.

The second axis concerns whether the controller's real composition can be recovered from observed behavior. The nominal controller $C$ is supplemented by a latent human compensator $H_t$ acting on side information $z_t$. The official model omits $H$, so the realized loop $C + H$ looks like $C$ alone.

The claim is not that $H$ is always hidden. It is that under specific structural conditions, $H$ cannot be recovered from the outputs the system's measurement-and-authority map produces.

### 3.1 Definition: operational masking

A compensator $H_t$ is **observationally masked** over horizon $T$ if, given the authority projection $\Pi_{A_t}$ and measurement map $h$, the system under $C + H$ cannot be distinguished from the system under $C$ alone through observed outputs.

**Deterministic (exact) case.** Output trajectories coincide on $[0, T]$:

$$y_{0:T}(C + H) = y_{0:T}(C).$$

**Stochastic (exact) case.** Output laws coincide on $[0, T]$:

$$P(y_{0:T} \mid C + H) = P(y_{0:T} \mid C + 0).$$

**Approximate ($\varepsilon$-)case.** Output trajectories coincide up to tolerance in an appropriate norm on $[0, T]$:

$$\|y_{0:T}(C + H) - y_{0:T}(C)\|_{L^2([0,T])} \leq \varepsilon,$$

with $\varepsilon$ fixed relative to the observation noise floor of the primary measurement map. Exact masking is the $\varepsilon = 0$ limit; $\varepsilon$-masking is what the system's real-time detection regime cannot resolve.

The dynamics differ; the outputs cannot resolve the difference.

### 3.2 Sufficient masking conditions

A nonzero $H_t$ is observationally masked if any of the following holds.

**Projection masking (boundary erasure).** The intervention is clipped by the authority gate such that the realized action is identical to the nominal intent:

$$\Pi_{A_t}(C_{\theta_t}(\hat{x}_t, c_t) + H_t) = \Pi_{A_t}(C_{\theta_t}(\hat{x}_t, c_t)).$$

The operator is pushing on a locked door; the policy boundary erases the contribution before it reaches the plant.

**Measurement null-space masking (latent stabilization).** The intervention's first-order propagation to observed output is annihilated by the plant-plus-observation dynamics over horizon $T$:

$$\frac{\partial h}{\partial x}\left(\frac{\partial f}{\partial x}\right)^k\frac{\partial f}{\partial u} H_t = 0, \quad k = 0, 1, \ldots, T-1.$$

Equivalently, the input channel of $H_t$ lies in the kernel of the finite-horizon observability matrix constructed from the plant and measurement Jacobians along the nominal trajectory. The intervention changes future recoverability — recovery margin, latent state, timing — without moving any observed output over the horizon $T$. Quiet heroics are structurally invisible under the measurement map for a finite but potentially long window, set by how long the observability operator keeps the $H$-driven perturbation out of $y$.

**Controller-family confounding (local gain aliasing).** The intervention is observationally equivalent to a parameter shift within the nominal controller family. In a local linear class, let

$$C_{\theta_t}(\hat{x}_t, c_t) = K(\theta_t)\, \phi(\hat{x}_t, c_t),$$

where $K(\theta)$ is a gain matrix and $\phi$ is the feature map presented to the controller. Then $H_t$ is confounded if there exists $\Delta\theta$ such that

$$\Pi_{A_t}\!\big(K(\theta_t)\,\phi + H_t\big) \approx \Pi_{A_t}\!\big(K(\theta_t + \Delta\theta)\,\phi\big)$$

over the operating region of interest. The observed behavior supports the wrong causal story: not "an undocumented human correction stabilized the system," but "the nominal controller seems to be running with different gain today." The compensator has not disappeared; it has been re-described as ordinary controller variation.

### 3.3 Operational Masking Theorem

Consolidating the above:

> **Theorem (Operational Masking).** Let $C_{\theta_t}$ be a nominal controller with authority projection $\Pi_{A_t}$, measurement map $h$, plant dynamics $f$, and latent compensator $H_t \neq 0$. If any of the following hold:
>
> (i) $\Pi_{A_t}(C_{\theta_t}(\hat{x}_t, c_t) + H_t) = \Pi_{A_t}(C_{\theta_t}(\hat{x}_t, c_t))$ (projection masking);
>
> (ii) $\dfrac{\partial h}{\partial x}\left(\dfrac{\partial f}{\partial x}\right)^k\dfrac{\partial f}{\partial u} H_t = 0$ for $k = 0, 1, \ldots, T-1$ (equivalently, $(\partial f/\partial u) H_t$ lies in the kernel of the stacked finite-horizon observability matrix $O_T = [C;\, CA;\, \ldots;\, CA^{T-1}]$ with $A := \partial f/\partial x$, $C := \partial h/\partial x$) (measurement null-space masking; finite-horizon, first-order);
>
> (iii) $C_\theta$ lies in a local linear class $K(\theta)\phi$ and there exists $\Delta\theta$ such that $\left\| \Pi_{A_t}(K(\theta_t)\phi + H_t) - \Pi_{A_t}(K(\theta_t + \Delta\theta)\phi) \right\|_{L^2(\Omega)} \leq \varepsilon$, where $\Omega$ is the operating region and $\varepsilon$ is a tolerance fixed relative to the observation noise floor (local gain aliasing);
>
> then $H_t$ is observationally masked over horizon $T$ under the primary real-time measurement-and-authority map $(\Pi_{A_t}, h)$: **exactly** under (i), **to first order over horizon $T$** under (ii), and **up to resolution $\varepsilon$** under (iii).

The three conditions are sufficient and non-exhaustive. They are not mutually exclusive — a given compensator may satisfy more than one simultaneously, and effective compensation often does.

**Proof sketches.**

*Case (i), projection masking.* By hypothesis $\Pi_{A_t}(C + H_t) = \Pi_{A_t}(C)$, so the realized action $u_t$ is identical under both controllers at every $t$. Plant dynamics $x_{t+1} = f(x_t, u_t, w_t)$ and observation $y_t = h(x_t, v_t)$ depend on $(x_t, u_t)$ only, so identical $u$-sequences produce identical $x_{0:T}$ and $y_{0:T}$ for matched noise realizations. Output indistinguishability follows. ∎

*Case (ii), measurement null-space masking, finite-horizon.* Let $\delta u_t = H_t$ be the perturbation from the nominal action, and let $A := \partial f / \partial x$, $B := \partial f / \partial u$, $C := \partial h / \partial x$ denote the Jacobians along the nominal trajectory. To first order, the perturbation propagates as $\delta x_{t+k} = A^{k-1} B H_t$ for $k \geq 1$, producing observed deviation $\delta y_{t+k} = C A^{k-1} B H_t$. The hypothesis $C A^k B H_t = 0$ for $k = 0, 1, \ldots, T-1$ zeroes the first-order term at every step of the horizon; equivalently, $B H_t$ lies in the kernel of the finite-horizon observability matrix $O_T := [C;\, CA;\, \ldots;\, CA^{T-1}]$. Under this hypothesis, $\delta y_{t+1:t+T} = O(\|H_t\|^2)$: output indistinguishability holds to first order *over the full horizon* $T$, not just pointwise at one step. The statement remains first-order; a fully nonlinear global version requires the weakly-unobservable subspace construction (Isidori, Ch. 6) and is deferred. ∎

*Case (iii), local gain aliasing.* By hypothesis, the realized action under $C + H$ lies within $\varepsilon$ in $L^2(\Omega)$ of the realized action under the shifted nominal controller $C_{\theta + \Delta\theta}$. Assuming $f$ and $h$ are Lipschitz over $\Omega$, trajectory and output differences between the two systems propagate as $O(\varepsilon)$ over $[0, T]$. An observer with resolution coarser than $O(\varepsilon)$ cannot distinguish $H_t$ from the parameter shift $\Delta\theta$. Exact indistinguishability holds only at $\varepsilon = 0$; the interesting regime is $\varepsilon$ small relative to the noise floor. ∎

### 3.4 Scope and breaking the mask

The masking result is relative to the system's **primary real-time measurement-and-authority map** — the regime by which the system ordinarily sees and governs itself. The claim is not permanent invisibility but structural under-resolution in that regime.

Secondary channels routinely recover latent compensation after the fact: operator notebooks, voice-loop recordings, alarm acknowledgment logs, historian replay, PMU data, post-event debriefs, black-box reconstruction. These are not reducible to $h$ or $\Pi_{A_t}$, and in high-stakes domains (FAA, NRC, transmission post-mortems) they routinely do recover what was masked in real time. The mask can also be broken prospectively: by enriching instrumentation so that interventions no longer lie in the effective observation null space, or by active probing and drills that drive the system toward regions where projection masking no longer holds.

The present paper identifies masking conditions under the primary regime. Recovery of identifiability — whether through enriched instrumentation, active probing, or secondary witness channels — is a separate problem and is deferred.

The important consequence: organizations do not merely fail to notice stabilizing labor. Under common measurement and authority regimes, effective stabilizing labor is often not identifiable from the outputs those regimes observe. And this bites hardest where it matters most:

**The most effective compensators are often the hardest to detect, because successful compensation moves the system away from the boundaries where compensation would become observable.**

## 4. Worked example: tie-line loss at the thermal limit

The following is *illustrative*, not diagnostic. It shows how the framework's four failure families can co-occur on a single timeline and how the continuity-budget inequality would apply. The parameters are plausible — NERC emergency ratings run 15–30 minutes, published escalation latencies run 10–30 minutes — but the scenario is composed, not reconstructed from a named incident. A real-case diagnostic application is deferred until published post-mortem data can be mapped onto the $(\tau_{\text{auth}}, \delta_h, T_{\text{exit}})$ triple directly.

Consider a single transformer downstream of a primary transmission tie-line during a heavy storm. The transformer is already near its thermal limit due to earlier redistribution. The control room is staffed by a shift about to turn over.

### 4.1 Pre-event: masking and slow wear

The veteran operator knows that substation voltage telemetry drifts high during heavy rain. They are silently bias-correcting their commands — a nonzero $H_t$ that keeps the system in the strict interior of the safety set and does not move top-level SCADA alarms. This is measurement null-space masking: the intervention acts on state the observation map does not resolve. The organization believes the grid is robust; in reality it is being stabilized by an undocumented $H_t$ that will disappear the moment this operator retires.

The operator is ten hours into an extended shift. Parameter drift has set in: $\theta_t$ is slowly moving toward sluggish response.

### 4.2 Disturbance: the authority bottleneck

A primary tie-line trips. Flows redistribute; the downstream transformer pushes to 110% of rated thermal capacity. The operator identifies a destructive rescue — shed load on a protected municipal feeder — but this action lies outside current $A_t$. Standing authority covers industrial load, not the municipal core.

The transformer has a 15-minute thermal integration limit ($T_{\text{exit}} = 15\text{ min}$). Escalation to expand $A_t$ requires multi-party sign-off with median latency 20 minutes. The Institutional Ruin Condition holds: $x_t \in V(A_{\text{expanded}})$ but $x_{t + \tau_{\text{auth}}} \notin V(A_{\text{expanded}})$. A rescue exists in principle; authority cannot arrive in time.

### 4.3 Crisis: handoff reset

At minute 8 of the 15-minute countdown, shift change occurs. The outgoing operator serializes $c_t$: redistribution flows, the voltage bias correction, status of the pending escalation. Under storm-time bandwidth constraint $B$, the nuance of the manual bias does not survive. The incoming operator's estimator $\hat{x}$ is cold-started; they spend three minutes reconciling telemetry with the brief. The reset consumes all three components of $\delta_h$: $\delta_{\text{serial}}$ in deserializing the bandwidth-limited brief, $\delta_{\text{reorient}}$ inflated because $\theta_t$ is already degraded from the outgoing operator's fatigue and propagates through the handoff, and $\delta_{\text{ambig}}$ driven by an unfamiliar post-trip redistribution pattern under storm conditions.

### 4.4 Outcome: fracture

As thermal alarms transition from Warning to Critical, the incoming operator hits an ambiguity shock. The controller undergoes a mode switch $\sigma_{\text{nom}} \to \sigma_{\text{degraded}}$: panic switching in place of balancing, rapid breaker cycling inducing sub-synchronous resonance. The substation trips.

The grid failed not because the operator was bad or the storm was too big, but because four distinct continuity failures composed on one timeline: identity loss at shift change, authority insufficient to physical requirements, stability dependent on an uninherited masked compensator, controller fracture in place of graceful degradation.

### 4.5 Counterfactual sensitivity

Two knobs govern whether the rescue remains reachable: handoff bandwidth $B$ (which sets reset expansion $\mu(B)$ and the $\delta_{\text{serial}}$ component of $\delta_h$) and authority-routing delay $\tau_{\text{auth}}$. Holding $\delta_{\text{reorient}}$ and $\delta_{\text{ambig}}$ fixed at their scenario values, the feasibility condition is the continuity-budget inequality:

$$\tau_{\text{auth}} + \delta_h < T_{\text{exit}}.$$

Three mini-cases show non-substitutability.

**Case A:** $B \uparrow$, $\tau_{\text{auth}}$ fixed. $\delta_{\text{serial}}$ shrinks; $\delta_{\text{reorient}}$ and $\delta_{\text{ambig}}$ are unchanged, and $\tau_{\text{auth}}$ dominates. Escalation still misses the window. Ruin is governance-induced.

**Case B:** $\tau_{\text{auth}} \downarrow$, $B$ fixed. Authority arrives in time despite imperfect handoff. Masked compensator still unrecovered, but action-side continuity is restored.

**Case C:** both improved. Positive margin; viability preserved. But action-side continuity is restored without recovering identity-side continuity: the masked compensator remains unidentifiable, and the system is saveable without yet being legible to itself. The two axes are separately repaired and separately repairable — restoring one does not recover the other.

Case A is the scenario no amount of better tooling or documentation will save. The bottleneck is authorization latency, not information transfer. Case B is the scenario where governance reform alone suffices. The distinction is checkable.

## 5. Position in the series

This paper is the dynamical hinge between two existing results.

**Paper 21** (observer integrity under procedural sociality) establishes the static observer-integrity conditions under which an observer's report can be trusted. §3 of this paper extends that result to controller composition: the observer integrity problem is not only about whether the observer is telling the truth, but about whether the composition of the realized controller is recoverable at all under the current measurement-and-authority map. Continuity of identity is observer integrity made dynamical.

**Paper 22** (no universal plant clock) decomposes the plant/controller stack into four layers (gauge, clock, estimation, actuation) and shows that timing failures distribute across them. §2 of this paper is Paper 22's actuation layer operationalized with authority explicitly in the loop — the delay in actuation is not only physical but institutional, and the composition of that delay with handoff and fatigue produces the continuity-budget inequality.

The paper therefore occupies a specific niche: not a rebrand of prior work, not a standalone island, but the moving-object treatment that connects observer integrity and layer decomposition through controller continuity.

## 6. Notes for next pass

- **Coherent checkpoint, 2026-04-21.** Landed in this pass: §3.1 case-(iii) honesty patch, projection-masking Lean kernel, bounded adjacency spike, and a §1 operationalization of "non-self-identical" (after independent flags from DeepSeek, chatty, and the Lean signature check that the §3 math is doing identifiability work, not metaphysics). The artifact has spine — named theorem-shaped objects, scoped caveats, a worked example that knows what it is, and one Lean module proving the kernel object is real. Bullets below are next-pass branches, not commitments. Iteration continues; freezing is thesis discipline, which is not the publication context here.

- **Lean target — done (case (i), 2026-04-21).** Projection-masking case (i) is formalized in `LeanProofs/OpsMasking.lean` as `projection_masking`, built on a more general lemma `trajectory_eq_of_projected_eq`: under any plant dynamics $f$ and measurement map $h$, two controllers whose *gated* actions agree pointwise produce identical plant trajectories and observations from any initial state. The paper-form corollary takes actions in an additive type and asserts $\Pi(C+H) = \Pi(C)$ pointwise ⇒ outputs coincide exactly. Deterministic case only. Cases (ii) (measurement null-space, first-order) and (iii) (local gain aliasing, $\varepsilon$-resolution) remain paper-level and are not yet Leaned. One signature note: in the formalization the gate is a fixed function $\text{proj} : U \to U$ rather than the paper's authority-state-indexed $\Pi_{A_t}$; for case (i) this is harmless (the masking hypothesis is already pointwise and absorbs any gate-state dependence), but lifting to $\text{proj} : X \to U \to U$ is required if a future module wants to carry $A_t$ explicitly — e.g., to formalize the §2 continuity-budget inequality, where authority delay is the load-bearing object. The §2 ADT bound itself remains imported scaffolding and is intentionally not Leaned.

- **Adjacency spike (bounded, pre-lit-review) — first pass, 2026-04-21.** Four buckets, "differs from X because Y" for each. To be expanded into a proper §1 novelty paragraph and a §7 related-work pass; not yet committed to the body.

  *Switched and hybrid systems; average dwell time (Hespanha–Morse); Markov jump linear systems; reconfigurable control.* The §2 dwell-time inequality is imported directly from this literature, and §1 names this as scaffolding. The departure is that switched-systems arguments assume the loop *knows* which controller it currently is — the active mode is a specified discrete index, and stability reduces to switching-frequency conditions on a known sequence. Operations begin where that assumption breaks: the active controller is partially reconstituted across handoffs, partially supplemented by latent compensation, and partially under-resolved by the measurement-and-authority map. The hybrid object is the same; controller non-self-identity, in the strong sense of *unspecified composition*, is the new constraint.

  *Viability theory (Aubin; Aubin–Bayen–Saint-Pierre).* Viability kernels under set-valued control supply the geometric language for §2.2's Institutional Ruin Condition — a rescue trajectory exists in $V(A_{\text{expanded}})$ but not in $V(A_t)$. The departure is that the admissible-action set $A_t$ is itself a controlled object, evolving via institutional authority routing with delay $\tau_{\text{auth}}$ rather than as a fixed correspondence. Authority-as-set-valued-control with explicit routing latency, and the Institutional Ruin Condition as a delayed reachability problem, is the operational extension.

  *Structural identifiability (Bellman–Åström, Walter, Pohjanpalo); observer design under partial observability.* Identifiability theory studies whether parameters of a *plant* can be recovered from input-output data; weakly-unobservable subspace constructions handle the dual question for state. §3 reframes this at the controller-composition layer: given fixed plant dynamics, can the realized controller composition $C + H$ be recovered from outputs under the primary measurement-and-authority map $(\Pi_{A_t}, h)$? The three sufficient conditions — projection masking, measurement null-space masking, local gain aliasing — are controller-side analogues of identifiability defects long-known on the plant side. Treating $\Pi$ as part of the effective measurement map is the new move; it is what makes authority a structural identifiability constraint, not just an authorization workflow.

  *Human supervisory control (Sheridan); resilience engineering (Hollnagel); joint cognitive systems (Woods).* The qualitative observation that operators silently stabilize systems through undocumented compensatory action — the "substitution myth," "graceful extensibility," "work-as-imagined vs work-as-done" — is well-developed in this literature. What is added here is the hybrid-systems formal object that says *under what structural conditions* such compensation is not merely undocumented but observationally non-recoverable from the system's primary measurement-and-authority map. The resilience-engineering observation has a name; here it gets a theorem.

  *Synthesis.* The novelty claim is the joint move: a hybrid-systems formalism on the action side (§2, importing dwell-time and viability machinery and extending the latter with authority-as-set-valued-control under delay) plus an identifiability-style theorem on the identity side (§3, reframing recoverability of controller composition under the institutional measurement-and-authority map), unified by the observation that operations is precisely the regime in which the controller is non-self-identical and the system's own measurement-and-authority map is structurally unable to resolve that fact. None of the adjacent literatures separately makes that combined claim. Full citations and §7-style positioning deferred to the lit-review pass.

- **Predicted governance family.** The admissibility family's spatial receipts (authorization, provenance) predict a temporal-axis sibling: handoff receipts, authority-routing receipts, operator-state receipts, continuity witnesses. This is a structural prediction, worth pulling into the family paper when it gets written.

- **ICU contrast case for later.** Once the power-grid example is stable, a medical handover example makes the identity-continuity half viscerally obvious — but ethical static would swallow the formal object on first pass. Grid first; ICU later as "the framework generalizes beyond infrastructure."

- **Second example of Case A is worth collecting.** Published grid timelines (PJM, ERCOT) supply real $\tau_{\text{auth}}$ and $T_{\text{exit}}$ numbers; the inequality becomes a post-hoc diagnostic rather than a hypothetical.
