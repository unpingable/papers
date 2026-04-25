---
header-includes:
  - \usepackage{booktabs}
---

# Ops Is Control with a Non-Self-Identical Controller

**James Beck**
Independent Researcher

**Date:** April 2026

**Series:** Δt Framework, Paper 23

**Status:** Preprint v1.0 (2026-04-24)

---

## Abstract

We study two distinct failure modes of controller continuity in operational systems. **Continuity of action** concerns whether the controller can still intervene in time: handoff distortion, authority-routing delay, and fatigue-induced contraction loss jointly consume a viability budget that can be stated as a single inequality. **Continuity of identity** fails when the controller's real composition differs from the nominal controller in ways the measurement-and-authority map cannot resolve: under three sufficient masking conditions — stated locally, over a finite horizon, under the standing assumptions of §3.3 — latent human compensation becomes structurally unidentifiable from observed outputs. Much of classical control theory treats the controller as self-identical across time; hybrid and switched-systems frameworks admit controller change but typically assume its identity at each instant is specified. Operational systems of the kind considered here begin where those assumptions break.

**Keywords:** controller continuity, hybrid control, operational systems, identifiability, viability theory, switched systems, human supervisory control, resilience engineering, authority routing

## 1. Thesis and scaffold

Much standard analysis assumes controller identity is specified at each instant — even in switched-systems, time-varying, and reconfigurable-control frameworks, which permit the controller to change but typically require the loop to know which controller it currently is. Many high-consequence operational settings — grid control rooms, flight decks, ICUs, SRE on-call rotations — violate that weaker assumption. The controller is handed off, reconstituted, partially authorized, quietly supplemented by undocumented human compensation, and degraded by fatigue or ambiguity, often in ways the loop cannot resolve from observed behavior. The result is not merely plant instability. It is instability produced by controller composition being partially reset, delayed, supplemented, or structurally unrecoverable in time.

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

This scope is also diagnostic. The places where the framework does not apply are often exactly the places where an organization has already spent engineering effort to restore controller self-identity — by automating the loop, engineering the handoff, or pre-delegating emergency authority. Such cases are not awkward exceptions; they are institutional repairs to controller discontinuity. The framework should be considered falsified if applied to a system where (a) controller identity is *not* specified at each instant, (b) no institutional repair of the above kinds is in place, and (c) continuity-budget or identifiability failures of the forms in §2–§3 are nevertheless absent across multiple incidents: the predicted failure geometry would then be missing in a regime where it should appear.

## 2. Continuity of action

Three dynamic sources consume the viability budget.

### 2.1 Handoff as reset map

At handoff, controller state is not transmitted directly. It is serialized under a bandwidth constraint, reconstructed by another operator, and partially cold-started:

$$c_{t^+} = D\!\big(S(c_{t^-}; B), r_t\big), \qquad \hat{x}_{t^+} = \hat{x}_{\mathrm{reinit}}$$

where $S$ is lossy serialization under budget $B$, $D$ is reconstruction, and $r_t$ is whatever residual context survives locally. This is not additive noise. It is a reset map; the outgoing and incoming controllers are not identical even if both are individually competent.

For the first pass it is enough to model the serialization loss coarsely. Let

$$S(c_{t^-}; B) = c_{t^-} + \eta_B,$$

where $\eta_B$ is a distortion term with magnitude bound $\|\eta_B\|$ monotone decreasing in handoff bandwidth $B$. Here $B$ should be read broadly: briefing time, artifact fidelity, ticket completeness, and the outgoing operator's ability to externalize state under load. The reconstruction delay induced by this reset — written $\delta_h$ and later decomposed into bandwidth, operator-state, and scene-ambiguity components in §2.4 — is the time required for the incoming operator to recover an actionable estimate from the distorted handoff and live telemetry. Higher $B$ does not eliminate reset; it shrinks the cold-start problem the incoming controller must solve.

The additive bounded-magnitude model $\|\eta_B\| \leq \epsilon(B)$ is a first-pass simplification; real handoffs are often reported in the human-factors and aviation-incident literature as *structurally* omissive rather than merely noisy. In practice $\eta_B$ is often biased rather than zero-mean — the outgoing operator emphasizes what they believe matters and omits what they do not know to be load-bearing — or structurally omissive, where an entire dimension of $c_{t^-}$ (an undocumented tacit calibration, a pattern-recognition habit) is dropped outright rather than noised. High-consequence handoff failures reported in the safety literature [10, 11, 12, 14] are frequently non-Gaussian in this sense: the failure mode is selection, not symmetric noise. The model above should be read as a reset-magnitude bound, not as a noise process.

In the standard switched-systems form (Hespanha–Morse [3]), if the Lyapunov function contracts with rate $\lambda \in (0,1)$ during flow and jumps by at most factor $\mu \geq 1$ at each reset, then stability of the overall hybrid trajectory requires an average dwell time satisfying

$$\tau_a > \frac{\log \mu}{-\log \lambda}.$$

Two caveats matter in the ops setting. First, $\mu$ is not scalar — handoffs vary in quality. The bound is really $\tau_a > \log \mu_{\sup} / (-\log \lambda)$ worst-case, or an expected form with a tail condition on $\mu$. Second, $\lambda$ depends on $\theta_t$: fatigue shrinks contraction, so the dwell-time requirement tightens as operators tire. Handoff and fatigue are not independent failure modes; they are coupled through one inequality.

### 2.2 Authority jump and the Institutional Ruin Condition

Operational systems separate observation from admissible action. An operator may know what needs to be done before they are permitted to do it. Escalation is therefore a jump in the admissible set:

$$A_{t^+} = A_{t^-} \cup \Delta A$$

triggered only after routing delay $\tau_{\text{auth}}$. The plant evolves during that delay under the constrained action set $A_t$, not the action set needed for rescue.

Let $V(A)$ be the viability kernel of the plant under authority set $A$ [6, 7]: the set of states from which the plant can be kept inside the safe set indefinitely using actions in $A$. Let $\mathrm{Reach}_{A, \tau}(x)$ denote the set of states reachable from $x$ in time $\tau$ under any admissible control sequence drawn from $A$ and any admissible disturbance realization. Define the **Institutional Ruin Condition**:

$$x_t \in V(A_{\text{expanded}}), \quad \text{and} \quad \mathrm{Reach}_{A_t,\ \tau_{\text{auth}}}(x_t) \cap V(A_{\text{expanded}}) \;=\; \emptyset.$$

In words: at time $t$ a rescue trajectory exists in the future authorized set, but *no* admissible control under the current authority $A_t$ — against any admissible disturbance — can keep the state inside the viability kernel of the expanded authority set by the time authority arrives.

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

The decomposition is intended to be diagnostic rather than only elegant: two systems with the same aggregate $\delta_h$ but different dominant components predict different interventions. A system where $\delta_{\text{serial}}$ dominates should respond to handoff-bandwidth investment; a system where $\delta_{\text{reorient}}$ dominates should not, and will instead respond to fatigue/staffing changes. §4.5 works through this distinction on a composed scenario.

To first order within the decomposition above, the four knobs each primarily shrink a different term. Shorter authority delay primarily affects $\tau_{\text{auth}}$. Higher handoff bandwidth primarily shrinks $\delta_{\text{serial}}$. Rested operators or task familiarity primarily shrink $\delta_{\text{reorient}}$. Pre-staged playbooks, simulator-run exposure to the failure class, and scene-legibility interventions primarily shrink $\delta_{\text{ambig}}$. Cross-couplings exist at second order: better handoff artifacts can modestly reduce reorientation time if they prime the incoming operator's mental model, and long authority delays can inflate ambiguity load when the operator spends reorientation time waiting on sign-off rather than acting. The decomposition is therefore diagnostic about *dominant* levers rather than a claim of perfect orthogonality. An organization buying continuity by investing only in handoff tooling is buying predominantly $\delta_{\text{serial}}$ reduction; if the binding term is $\delta_{\text{reorient}}$ (fatigue) or $\tau_{\text{auth}}$ (authorization latency), the investment moves the margin at most weakly.

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

Equivalently, the input channel of $H_t$ lies in the kernel of the finite-horizon observability matrix constructed from the plant and measurement Jacobians along the nominal trajectory (under a local-LTI linearization over horizon $T$; see §3.3 standing assumptions). Under this condition, the intervention changes future recoverability — recovery margin, latent state, timing — without moving any observed output over the horizon $T$. The duration of that observational invisibility is set by how long the observability operator keeps the $H$-driven perturbation out of $y$.

**Controller-family confounding (local gain aliasing).** The intervention is observationally equivalent to a parameter shift within the nominal controller family. In a local linear class, let

$$C_{\theta_t}(\hat{x}_t, c_t) = K(\theta_t)\, \phi(\hat{x}_t, c_t),$$

where $K(\theta)$ is a gain matrix and $\phi$ is the feature map presented to the controller. Then $H_t$ is confounded if there exists $\Delta\theta$ such that

$$\Pi_{A_t}\!\big(K(\theta_t)\,\phi + H_t\big) \approx \Pi_{A_t}\!\big(K(\theta_t + \Delta\theta)\,\phi\big)$$

over the operating region of interest. The observed behavior supports the wrong causal story: not "an undocumented human correction stabilized the system," but "the nominal controller seems to be running with different gain today." The compensator has not disappeared; it has been re-described as ordinary controller variation.

### 3.3 Operational Masking Theorem

**Standing assumptions.** Throughout the theorem, $f$ and $h$ are $C^1$ on a neighborhood of the nominal trajectory, and both the nominal system (running $C$) and the perturbed system (running $C + H$) are assumed to remain within a compact product set $\Omega := \Omega_x \times U \subseteq \mathbb{R}^n \times \mathbb{R}^m$ on which $f$ is jointly Lipschitz in $(x, u)$ with constant $L_f$, and $h$ is Lipschitz in $x$ with constant $L_h$. The compensator $H_s$ is small in the sense that first-order expansions in $\|H\|$ dominate higher-order terms over the horizon $[t, t+T]$. For the stochastic case, we assume *either* (a) sample-path equality of the disturbances $(w, v)$ across the two systems — a single probability space on which both $C$ and $C+H$ are driven by the same noise realization — *or* (b) law-level independence, under which the law of $(w, v)$ does not depend on the choice between $C$ and $C + H$ given the plant and control histories; (a) gives pathwise equality of outputs and (b) gives equality of output laws. Case (ii) additionally restricts to a **local-LTI regime**: the Jacobians $A := \partial f/\partial x$, $B := \partial f/\partial u$, and $C_y := \partial h/\partial x$ (the *measurement* Jacobian, written $C_y$ to avoid clashing with the nominal controller symbol $C$) evaluated along the nominal trajectory are assumed approximately constant over the horizon $[t, t+T]$, so that the standard time-invariant observability matrix $O_T$ is a valid local linearization. The time-varying generalization — replacing $A^k$ by the state-transition operator $\Phi(s+k, s)$ and $O_T$ by a time-indexed observability Gramian — is straightforward in principle and is deferred. The projection $\Pi_{A_s}$ is evaluated at the nominal action in linearized arguments: non-smoothness of $\Pi$ at its boundary does not enter case (ii), unless the nominal action lies on that boundary — that situation is the regime of case (i), handled separately.

Consolidating the above:

> **Theorem (Operational Masking).** Let $C_{\theta_s}$ be a nominal controller with authority projection $\Pi_{A_s}$, measurement map $h$, plant dynamics $f$, and latent compensator sequence $(H_s)_{s \in [t, t+T-1]}$ with $H_s$ not identically zero. Under the standing assumptions above, if any of the following hold *for every* $s \in [t, t+T-1]$:
>
> (i) $\Pi_{A_s}(C_{\theta_s}(\hat{x}_s, c_s) + H_s) = \Pi_{A_s}(C_{\theta_s}(\hat{x}_s, c_s))$ (projection masking);
>
> (ii) under the local-LTI regime above, $B H_s$ lies in the kernel of the stacked finite-horizon observability matrix $O_T := [C_y;\, C_y A;\, \ldots;\, C_y A^{T-1}]$, where $A, B, C_y$ are the nominal-trajectory Jacobians treated as constant over the horizon (measurement null-space masking; finite-horizon, first-order);
>
> (iii) $C_\theta$ lies in a local linear class $K(\theta)\phi$ and there exists $\Delta\theta$ (independent of $s$) such that $\left\| \Pi_{A_s}(K(\theta_s)\phi + H_s) - \Pi_{A_s}(K(\theta_s + \Delta\theta)\phi) \right\|_{L^2(\Omega_x)} \leq \varepsilon$ for each $s \in [t, t+T-1]$, with $\varepsilon$ fixed relative to the observation noise floor, and with the trajectory of the shifted nominal controller $C_{\theta + \Delta\theta}$ also contained in $\Omega$ over $[t, t+T]$ (local gain aliasing);
>
> then $(H_s)$ is observationally masked over horizon $T$ under the primary real-time measurement-and-authority map $(\Pi_{A_t}, h)$: **exactly** under (i), **to first order in $\|H\|$ over horizon $T$** under (ii), and **up to output resolution $K(T, L_f, L_h)\,\varepsilon$** under (iii), where $K(T, L_f, L_h)$ is a horizon-and-Lipschitz-dependent constant derived in the proof.

The three conditions are sufficient and non-exhaustive. They are not mutually exclusive — a given compensator may satisfy more than one simultaneously, and effective compensation plausibly can, though this paper does not establish how often that is the case in the field.

**Proof sketches.**

*Case (i), projection masking.* For each $s \in [t, t+T-1]$, the realized action $u_s = \Pi_{A_s}(C + H_s) = \Pi_{A_s}(C)$ by hypothesis, so $u_s$ is identical under both controllers. Plant dynamics $x_{s+1} = f(x_s, u_s, w_s)$ and observation $y_s = h(x_s, v_s)$ depend on $(x_s, u_s, w_s)$ and $(x_s, v_s)$ respectively. Under noise assumption (a), identical $u$-sequences and identical noise realizations produce pathwise-identical $x_{t:t+T}$ and $y_{t:t+T}$. Under assumption (b), identical $u$-sequences and noise laws that do not depend on the choice of controller produce identical *output laws* $P(y_{t:t+T} \mid C + H) = P(y_{t:t+T} \mid C)$. Either gives output indistinguishability at the appropriate level. $\\blacksquare$

*Case (ii), measurement null-space masking, finite-horizon, local-LTI.* Let $\delta u_s = H_s$ denote the perturbation to the nominal action at each step $s \in [t, t+T-1]$, and assume the local-LTI regime above: Jacobians $A, B, C_y$ along the nominal trajectory are approximately constant over $[t, t+T]$. Expanding the plant dynamics to first order gives, for $k \geq 1$,
>
> $$\delta x_{t+k} = \sum_{s = t}^{t+k-1} A^{\,t+k-s-1} B\, H_s \; + \; O\!\left(\|H\|^2\right),$$
>
> so the first-order output deviation at $t+k$ is
>
> $$\delta y_{t+k} = \sum_{s = t}^{t+k-1} C_y\, A^{\,t+k-s-1}\, B\, H_s \; + \; O\!\left(\|H\|^2\right).$$
>
> Each summand $C_y A^{j} B H_s$ has exponent $j = t+k-s-1 \in [0, k-1] \subseteq [0, T-1]$, and by the hypothesis $B H_s \in \ker(O_T)$ each row $C_y A^{j} B H_s$ vanishes for $j = 0, \ldots, T-1$. The first-order sum therefore vanishes term-by-term, and $\delta y_{t+1:t+T} = O(\|H\|^2)$: output indistinguishability holds to first order *over the full horizon* $T$, not just pointwise at one step. The conclusion is first-order; a fully nonlinear global version requires the weakly-unobservable subspace construction (Isidori, Ch. 6, [9]) and is deferred. $\\blacksquare$

*Case (iii), local gain aliasing.* The $L^2(\Omega_x)$ norm is evaluated per step $s$ by integrating over the spatial operating region $\Omega_x$; the hypothesis requires the same single shift $\Delta\theta$ to achieve the $\varepsilon$-closeness uniformly across $s \in [t, t+T-1]$. Under the standing assumption that $f$ is jointly Lipschitz in $(x, u)$ on $\Omega = \Omega_x \times U$ with constant $L_f$, that $h$ is Lipschitz in $x$ with constant $L_h$, and that both trajectories remain in $\Omega$, a discrete Grönwall-type bound propagates the per-step action difference through the dynamics. Writing $\Delta u_s := \Pi_{A_s}(K(\theta_s)\phi + H_s) - \Pi_{A_s}(K(\theta_s + \Delta\theta)\phi)$, with $\|\Delta u_s\| \leq \varepsilon$ by hypothesis, and letting $e_k := \|x_{t+k}^{C+H} - x_{t+k}^{C_{\theta + \Delta\theta}}\|$ denote the trajectory deviation, the recursion $e_{k+1} \leq L_f(e_k + \|\Delta u_{t+k}\|)$ unrolls to $e_k \leq \varepsilon L_f (1 + L_f)^{k-1}$ (with matched initial conditions at step $t$). The output deviation at step $t+k$ is bounded by $L_h e_k \leq K(T, L_f, L_h)\,\varepsilon$, with $K(T, L_f, L_h) := L_h L_f (1 + L_f)^{T-1}$. An observer with output-level resolution coarser than $K(T, L_f, L_h)\,\varepsilon$ cannot distinguish $(H_s)$ from the parameter shift $\Delta\theta$. Exact indistinguishability holds only at $\varepsilon = 0$; the load-bearing regime is $K(T, L_f, L_h)\,\varepsilon$ small relative to the observation noise floor — which, for fixed $T, L_f, L_h$, is equivalent to $\varepsilon$ being small by a problem-specific factor. $\\blacksquare$

### 3.4 Scope and breaking the mask

The masking result is relative to the system's **primary real-time measurement-and-authority map** — the regime by which the system ordinarily sees and governs itself. The claim is not permanent invisibility but structural under-resolution in that regime.

Secondary channels can recover latent compensation after the fact: operator notebooks, voice-loop recordings, alarm acknowledgment logs, historian replay, PMU data, post-event debriefs, black-box reconstruction. These channels are not reducible to $h$ or $\Pi_{A_t}$, and in high-stakes domains with mature incident-reconstruction practice — aviation investigations under NTSB [18], nuclear-plant event reporting under NRC [19], transmission post-mortems under NERC reliability standards [17] — such channels are routinely mobilized to reconstruct the realized control activity after the fact, with varying success depending on the incident and the richness of the preserved record. The mask can also be broken prospectively: by enriching instrumentation so that interventions no longer lie in the effective observation null space, or by active probing and drills that drive the system toward regions where projection masking no longer holds.

The present paper identifies masking conditions under the primary regime. Recovery of identifiability — whether through enriched instrumentation, active probing, or secondary witness channels — is a separate problem and is deferred.

An immediate theorem-level consequence: organizations do not merely fail to notice stabilizing labor. Under common measurement and authority regimes that happen to satisfy one of conditions (i)–(iii) above, effective stabilizing labor *can be* unidentifiable from the outputs those regimes observe. The masking theorem tells us *when* this happens; it does not tell us *how often* it happens in the field.

A sharper — and more contentious — claim is suggested by the same structure, but is *not* established by the theorem:

> **Conjecture (non-theorem; conjectural systems reading).** *Effectiveness and detectability are frequently anti-correlated by construction: compensation that successfully keeps the plant interior to the safety set tends to act in directions the authority projection or measurement map cannot resolve, because compensation that crossed the authority boundary or triggered instrumentation would typically be flagged and routed to procedure rather than remaining latent.*
>
> This is a conjectural systems reading, not a theorem-level consequence. The masking theorem supplies only sufficient conditions; the conjecture additionally claims that the regime of effective compensation and the regime of masked compensation coincide with nontrivial frequency in the field. Testing that empirically — across grid, flight-deck, ICU, and SRE-oncall domains where the framework is meant to apply — is out of scope here.

## 4. Worked example: tie-line loss at the thermal limit

The following is *illustrative*, not diagnostic. It shows how the framework's four failure families can co-occur on a single timeline and how the continuity-budget inequality would apply. The parameters are plausible — transformer short-time and emergency thermal ratings published by the IEEE and NERC fall within ranges on the order of minutes to tens of minutes [16, 17] — but the specific numeric values are composed, not reconstructed from a named incident, and the escalation-latency figure should be read as a scenario parameter rather than an empirical estimate. A real-case diagnostic application is deferred until published post-mortem data can be mapped onto the $(\tau_{\text{auth}}, \delta_h, T_{\text{exit}})$ triple directly.

Consider a single transformer downstream of a primary transmission tie-line during a heavy storm. The transformer is already near its thermal limit due to earlier redistribution. The control room is staffed by a shift about to turn over.

### 4.1 Pre-event: masking and slow wear

The veteran operator knows that substation voltage telemetry drifts high during heavy rain. They are silently bias-correcting their commands — a nonzero $H_t$ that keeps the system in the strict interior of the safety set and does not move top-level SCADA alarms. This is measurement null-space masking: the intervention acts on state the observation map does not resolve. The organization believes the grid is robust; in reality it is being stabilized by an undocumented $H_t$ that will disappear the moment this operator retires.

The operator is ten hours into an extended shift. Parameter drift has set in: $\theta_t$ is slowly moving toward sluggish response.

The masked compensator does not itself precipitate the collapse; it renders the system dependent on stabilizing labor whose withdrawal appears, to the primary regime, as surprise.

### 4.2 Disturbance: the authority bottleneck

A primary tie-line trips. Flows redistribute; the downstream transformer pushes to 110% of rated thermal capacity. The operator identifies a destructive rescue — shed load on a protected municipal feeder — but this action lies outside current $A_t$. Standing authority covers industrial load, not the municipal core.

The transformer has a 15-minute thermal integration limit ($T_{\text{exit}} = 15\text{ min}$). Escalation to expand $A_t$ requires multi-party sign-off with median latency 20 minutes. The Institutional Ruin Condition holds: $x_t \in V(A_{\text{expanded}})$ but $x_{t + \tau_{\text{auth}}} \notin V(A_{\text{expanded}})$. A rescue exists in principle; authority cannot arrive in time.

### 4.3 Crisis: handoff reset

At minute 8 of the 15-minute countdown, shift change occurs. The outgoing operator serializes $c_t$: redistribution flows, the voltage bias correction, status of the pending escalation. Under storm-time bandwidth constraint $B$, the nuance of the manual bias does not survive. The incoming operator's estimator $\hat{x}$ is cold-started; they spend three minutes reconciling telemetry with the brief. The reset consumes all three components of $\delta_h$: $\delta_{\text{serial}}$ in deserializing the bandwidth-limited brief, $\delta_{\text{reorient}}$ inflated because the incoming operator is also at the end of an extended storm rotation and their own $\theta$ is already degraded (storm staffing has kept both crews in back-to-back extended shifts), and $\delta_{\text{ambig}}$ driven by an unfamiliar post-trip redistribution pattern under storm conditions. The three components are distinct in kind: $\delta_{\text{serial}}$ is what the outgoing operator could not transmit; $\delta_{\text{reorient}}$ is what the incoming operator cannot yet assimilate; $\delta_{\text{ambig}}$ is what the scene has not yet revealed.

### 4.4 Outcome: fracture

As thermal alarms transition from Warning to Critical, the incoming operator hits an ambiguity shock. The controller undergoes a mode switch $\sigma_{\text{nom}} \to \sigma_{\text{degraded}}$: panic switching in place of balancing, rapid breaker cycling inducing sub-synchronous resonance. The substation trips.

On this constructed timeline, the grid's failure is explained by four distinct continuity failures composing: identity loss at shift change, authority insufficient to physical requirements, stability dependent on an uninherited masked compensator, and controller fracture in place of graceful degradation. The scenario is not a causal identification — "bad operator" and "storm too big" are not formally excluded by the setup — but a demonstration that the four failure families *can* compose on a single timeline in exactly the way the continuity-budget and masking theorems predict.

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

**Paper 21** (observer integrity under procedural sociality [1]) establishes the static observer-integrity conditions under which an observer's report can be trusted. §3 of this paper extends that result to controller composition: the observer integrity problem is not only about whether the observer is telling the truth, but about whether the composition of the realized controller is recoverable at all under the current measurement-and-authority map. Continuity of identity is observer integrity made dynamical.

**Paper 22** (no universal plant clock [2]) decomposes the plant/controller stack into four layers (gauge, clock, estimation, actuation) and shows that timing failures distribute across them. §2 of this paper is Paper 22's actuation layer operationalized with authority explicitly in the loop — the delay in actuation is not only physical but institutional, and the composition of that delay with handoff and fatigue produces the continuity-budget inequality.

The paper therefore occupies a specific niche: not a rebrand of prior work, not a standalone island, but the moving-object treatment that connects observer integrity and layer decomposition through controller continuity.

## 6. Adjacency and distinction

This paper sits adjacent to four established literatures: switched and hybrid systems, viability theory, structural identifiability, and human supervisory control / resilience engineering. It borrows machinery from the first two, reframes the third at the controller-composition layer, and gives theorem-level structure to a phenomenon the fourth usually describes qualitatively. Its distinct claim is the joint object: **operational systems in which the controller is not self-identical across time, and in which the system's primary measurement-and-authority map cannot in general resolve that fact.**

From switched and hybrid systems [3, 4, 5], the paper takes the jump/flow scaffold directly. Handoffs are reset maps, fatigue fractures are mode switches, and the continuity-of-action problem inherits the usual dwell-time and stability language. The departure is specific: standard switched-systems treatments generally assume that the active controller at each instant is specified. The present paper starts where that assumption fails. In operational systems, the controller is reconstituted across handoffs, partially gated by authority, and sometimes supplemented by latent compensation that the loop cannot name from observed behavior alone.

From viability theory [6, 7], the paper takes the language of reachable safety under constrained action sets. The Institutional Ruin Condition is stated in that register: rescue exists under an expanded admissible set, but authority-routing delay carries the plant out of the corresponding viability kernel before the set can be enlarged. What is added is that the admissible set is not fixed. It is institutionally routed, delayed, and only partially available to the controller in time. That makes authority not merely a governance detail but part of the control object itself.

From structural identifiability and observability [8, 9], the paper takes the question of recoverability from input-output behavior, but shifts it from plant parameters to **controller composition**. The issue is no longer only whether the plant can be reconstructed from measurements, but whether the realized controller $C + H$ can be distinguished from the nominal controller $C$ under the system's primary measurement-and-authority map. Projection masking, measurement null-space masking, and controller-family confounding are sufficient conditions under which that recovery fails. In that sense, the paper's identity axis is an identifiability result on the controller side of the loop.

From human supervisory control and resilience engineering [10, 11, 12, 13, 14, 15], the paper inherits a familiar empirical observation: operators often stabilize systems through undocumented compensatory labor, tacit calibration, and work that exists in practice more than in procedure. Prior formalizations have engaged parts of this — observability and identifiability of plant parameters [8, 9], switched-controller stability [3, 4, 5], viability under constrained action [6, 7], situation awareness and supervisory handoff [10, 11]. The specific contribution claimed here is narrower: the joint object defined by (a) authority projection $\Pi_{A_t}$ treated as part of the effective measurement map, (b) controller-composition identifiability $(C + H)$ vs $C$ under that joint map, and (c) the continuity-budget inequality that links handoff, authority delay, and operator-state degradation in one falsifiable form. None of the three ingredients is individually novel; the claim is that they compose into a single object under which two orthogonal failure axes become tractable together.

---

## Acknowledgments

Language-model tools were used for editorial critique, proof-soundness review, and literature discovery during preparation of this manuscript; all arguments, interpretations, and errors are the author's own.

---

## References

[1] Beck, J. (2026). Observer Integrity under Procedural Sociality: Measurement When the Instrument Shares the Grammar. Preprint, Δt Framework Paper 21. doi:10.5281/zenodo.19055415

[2] Beck, J. (2026). No Universal Plant Clock: Temporal Failure Geometry in Distributed Control Systems. Preprint, Δt Framework Paper 22. doi:10.5281/zenodo.19119617

[3] Hespanha, J.P., Morse, A.S. (1999). "Stability of switched systems with average dwell-time." In *Proc. 38th IEEE Conference on Decision and Control*, pp. 2655–2660. doi:10.1109/CDC.1999.831330

[4] Liberzon, D. (2003). *Switching in Systems and Control.* Birkhäuser. doi:10.1007/978-1-4612-0017-8

[5] Goebel, R., Sanfelice, R.G., Teel, A.R. (2012). *Hybrid Dynamical Systems: Modeling, Stability, and Robustness.* Princeton University Press. doi:10.1515/9781400842636

[6] Aubin, J.-P. (1991). *Viability Theory.* Birkhäuser. (2nd ed., Springer, 2009.)

[7] Blanchini, F., Miani, S. (2008). *Set-Theoretic Methods in Control.* Birkhäuser.

[8] Hermann, R., Krener, A.J. (1977). "Nonlinear controllability and observability." *IEEE Transactions on Automatic Control* AC-22(5), 728–740.

[9] Isidori, A. (1995). *Nonlinear Control Systems.* 3rd ed. Springer.

[10] Sheridan, T.B. (1992). *Telerobotics, Automation, and Human Supervisory Control.* MIT Press.

[11] Endsley, M.R. (1995). "Toward a theory of situation awareness in dynamic systems." *Human Factors* 37(1), 32–64.

[12] Hollnagel, E., Woods, D.D., Leveson, N., eds. (2006). *Resilience Engineering: Concepts and Precepts.* Ashgate.

[13] Rasmussen, J. (1997). "Risk management in a dynamic society: a modelling problem." *Safety Science* 27(2–3), 183–213. doi:10.1016/S0925-7535(97)00052-0

[14] Dekker, S. (2011). *Drift into Failure: From Hunting Broken Components to Understanding Complex Systems.* Ashgate.

[15] Beyer, B., Jones, C., Petoff, J., Murphy, N.R., eds. (2016). *Site Reliability Engineering: How Google Runs Production Systems.* O'Reilly Media.

[16] IEEE Std C57.91-2011. *Guide for Loading Mineral-Oil-Immersed Transformers and Step-Voltage Regulators.* IEEE (superseded by IEEE Std C57.91-2025; cited here for the historical thermal-rating convention). https://standards.ieee.org/ieee/C57.91/5297/ (accessed 2026-04-24).

[17] North American Electric Reliability Corporation. *Reliability Standards for the Bulk Electric Systems of North America*, including the TOP (Transmission Operations) and IRO (Interconnection Reliability Operations) standard families. NERC. https://www.nerc.com/pa/Stand/ (accessed 2026-04-23).

[18] U.S. Department of Transportation, 49 CFR Part 830 — Notification and Reporting of Aircraft Accidents or Incidents and Overdue Aircraft, and Preservation of Aircraft Wreckage, Mail, Cargo, and Records. Federal Aviation Administration / National Transportation Safety Board (reporting framework under which post-incident reconstruction occurs). https://www.ecfr.gov/current/title-49/part-830 (accessed 2026-04-24).

[19] U.S. Code of Federal Regulations, 10 CFR 50.72 — Immediate notification requirements for operating nuclear power reactors. U.S. Nuclear Regulatory Commission. https://www.ecfr.gov/current/title-10/part-50/section-50.72 (accessed 2026-04-24).
