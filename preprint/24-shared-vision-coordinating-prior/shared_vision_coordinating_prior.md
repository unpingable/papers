---
header-includes:
  - \usepackage{booktabs}
---

# Shared Vision as Coordinating Prior: Aggregation-Layer Masking and the Witness-Filter Pathology

**James Beck**
Independent Researcher

**Date:** April 2026

**Series:** Δt Framework, Paper 24

**Status:** Preprint v1.0 (released 2026-04-28; Zenodo)

---

## Abstract

Shared visions, strategic priors, and operating theses coordinate multi-agent systems by reducing policy divergence around a common token. We identify three structural failure modes by which such coordination produces persistently wrong steady states even when the system has working feedback, solicits dissent, and updates on reported error. First, any first-moment aggregator (mean, balanced weighted mean, rank-symmetric median) maps balanced bias-split witness populations to zero; the shared prior is therefore frozen by the arithmetic of the aggregation rule, not by any procedural refusal to update. Second, public alignment to a shared prior is alias-compatible with arbitrary internal compositional divergence under stationary conditions, with the divergence surfacing only under strategic shift. Third, witness inclusion correlated with prior-alignment defeats every aggregator — including shape-preserving receipt-lineage architectures — by removing signal upstream of aggregation; a single such filtering event produces persistent non-vanishing error with no internal mechanism for self-correction. The constructive consequence is that corrective governance architectures must preserve per-witness structure and maintain witness inclusion independent of prior-alignment; collapsing witness reports to scalar summaries or curating the witness population by alignment reintroduces the pathology.

**Keywords:** multi-agent coordination, shared prior, aggregation theory, observational masking, witness inclusion, cohort witness, receipt-lineage governance, federated learning, organizational epistemology, cybernetic regulation

## 1. Thesis and scaffold

Organizations routinely align on shared visions, strategic priors, or operating theses that turn out to be wrong. The standard accounts of this phenomenon are ideological ("leadership refused to listen"), sociological ("groupthink"), or procedural ("the feedback loops were broken"). Each names a real failure mode and each is sometimes correct. This paper argues that an important subset of coordinated-wrongness failures is *structural* in a sharper sense: they occur in organizations that have working feedback loops, that solicit dissent, and that update their shared prior in response to reported error. The failure does not happen in the reporting layer. It happens inside the aggregation layer, and it is invisible to the governance apparatus by construction.

We identify a three-layer pathology and prove four results:

- **Aggregation-layer masking.** Any first-moment aggregator maps balanced bias-split witness populations to zero, freezing the shared prior in the arithmetic of the rule itself. No procedural gate (unanimity, decay-thaw, dissent-override) acting downstream of the aggregator can rescue this. **(Theorem 1.)** A companion conjecture, supported by a four-aggregator probe, asserts that no scalar aggregator achieves both freeze-freedom and stability across the relevant population class. **(Conjecture 1.)**

- **Organizational alias-compatibility.** Public alignment to a shared prior is observationally alias-compatible between cohesive and hiddenly-divergent populations under stationary conditions; the divergence surfaces only under strategic shift. **(Proposition 2.)**

- **Witness-filter pathology.** Witness-inclusion correlated with prior-alignment — stack ranking, performance management correlated with compliance, "culture fit" hiring, attrition of disaffected members — defeats every aggregator, including shape-preserving receipt-lineage architectures, by removing signal upstream of aggregation. **(Theorem 3.)** A single such filtering event produces a persistent non-vanishing error between the shared prior and reality, bounded below by the surviving population's residual bias, with no internal mechanism for self-correction. **(Theorem 4.)**

The constructive corollary, established in §6, is that corrective architectures must preserve per-witness structure (no scalar aggregation) *and* maintain witness inclusion independent of prior-alignment (no alignment-correlated curation). Either condition alone is insufficient: receipt-lineage without open witnesses is defeated by curation; open witnesses without receipt-lineage are defeated by aggregation.

The paper sits structurally parallel to Paper 23 of this series ([1]), which proves a corresponding observational-masking result at the controller-composition layer. The present paper lifts the masking phenomenon one scale up — from the single-controller layer to the multi-agent / organizational layer — and supplies the specific aggregation-layer mechanism by which organizations fail to notice the alias-compatibility even when they nominally have feedback loops. The two papers cross-cite naturally; familiarity with Paper 23 is not required.

### 1.1 Scope boundary

The framework applies to multi-agent systems in which (a) agents share a common coordinating prior $V_t$ that influences their actions, (b) the prior is updated via some aggregation of distributed error signals, and (c) the witness-inclusion rule is a designable choice rather than fixed by physics. Examples include managerial governance over OKRs, KPI-driven performance regimes, federated learning systems, multi-arm bandit ensembles with shared posteriors, and consensus protocols deployed for value-correction (rather than purely for value-selection).

The framework does not apply where the aggregator is replaced by a richer object that already preserves distributional shape (per-witness receipts with downstream interpretation, full probability distributions over witness reports), or where witness inclusion is structurally fixed (every observation must be processed, e.g., physical-sensor systems with no operator). In these regimes the pathologies named below are designed out by the architecture. As with Paper 23, the places where the framework does not apply are often exactly the places where engineering effort has already been spent to restore the missing structural property.

## 2. Model

Discrete-time system, $n$ agents, scalar plant state $x_t \in \mathbb{R}$, scalar shared prior $V_t \in \mathbb{R}$.

**Plant.** $x_{t+1} = f(x_t, a^1_t, \dots, a^n_t, w_t)$, with $f$ linear-stable in the closed loop and $w_t$ a zero-mean disturbance. We retain the scalar plant for simplicity; vector $V_t$ extensions are discussed in §8.

**Observation.** $y^i_t = x_t + b_i + v^i_t$, with bias $b_i \in \mathbb{R}$ fixed per agent and $v^i_t$ zero-mean noise. The bias $b_i$ encodes systematic divergence between agent $i$'s observation and the true plant state — instrument calibration, role-induced perspective, departmental incentive distortion.

**Control.** $a^i_t = -k_i(y^i_t - V_t)$, with gain $k_i > 0$. Each agent acts to drive their observed state toward the shared prior.

**Witness inclusion.** $F : \{1, \dots, n\} \times \mathbb{R} \to \{0, 1\}$ is a filter function. Agent $i$'s error contributes to the prior update at time $t$ iff $F(i, V_t) = 1$. The unfiltered (open-witness) case is $F \equiv 1$.

**Prior update.** $V_{t+1} = V_t + \eta\, \Phi(E_t^F)$, where $E_t = (e^1_t, \dots, e^n_t)$ is the vector of per-agent error signals $e^i_t = y^i_t - V_t$, $E_t^F$ is the restriction of $E_t$ to $\{i : F(i, V_t) = 1\}$, and $\Phi$ is a scalar aggregator: a function $\Phi : \mathbb{R}^* \to \mathbb{R}$ defined on the space of finite-length error vectors.

**Internal interpretation (used in §3.4).** When alias-compatibility is at issue, each agent has a private *local-gradient* interpretation parameter $\varphi_i \in \mathbb{R}$ governing how the agent reads movement of the shared prior. Concretely, agent $i$ implements a public action map $A_i$ such that, around the stationary value $V_0$,
$$A_i(V_0) = A(V_0), \qquad A_i'(V_0) = A'(V_0) + \varphi_i,$$
so to first order in $\Delta V$,
$$A_i(V_0 + \Delta V) = A(V_0) + [A'(V_0) + \varphi_i]\Delta V + O(\Delta V^2).$$
Agents agree on the public level at $V_0$ and disagree only on the local continuation rule — what the token *means* under movement. The control law becomes $a^i_t = -k_i(y^i_t - A_i(V_t))$. The public alignment layer observes only action signatures, not the $\varphi_i$. The earlier additive form $V_t + \varphi_i$ corresponds to private level displacement, not local-gradient divergence; because it produces nonzero baseline action divergence under stationary $V$, it is not the alias-compatibility model used here.

**Aggregator class.** A scalar aggregator $\Phi$ is **first-moment** if $\Phi(E) = 0$ whenever the first moment of the components of $E$ vanishes. Mean, balanced weighted mean, and median under rank-symmetric splits are first-moment. Max-absolute-value and variance-gated aggregators are not. A scalar aggregator is **sup-norm bounded** if $|\Phi(E)| \leq \|E\|_\infty := \max_i |e_i|$ for all $E$, which is satisfied by mean, balanced weighted mean, median, max-absolute-value, and variance-gated. (Note: sup-norm boundedness is the property used in Theorem 3; coordinate-wise Lipschitz with constant $1$ is strictly weaker and would not give the sup-norm bound on $|\Phi(E)|$.)

This is the minimal model of a multi-agent system that shares a coordinating prior and updates it via feedback. It is also, structurally, what most managerial-governance regimes look like once the ritual surface is peeled off: shared target, distributed observations, feedback update rule, aggregation at the top.

## 3. Theorems

### 3.1 Setting (shared across §3)

All four results below operate on the model of §2. We denote the surviving (filtered-in) sub-population at time $t$ by $S(V_t) := \{i : F(i, V_t) = 1\}$. When $F \equiv 1$, $S(V_t) = \{1, \dots, n\}$ and is dropped from notation.

### 3.2 Theorem 1: Mean-Aggregation Masking

**Theorem 1 (Mean-Aggregation Masking).** *Suppose:*

- *(A1, balanced bias-split) $\sum_i b_i = 0$, with both signs nontrivially represented.*
- *(A2, aggregator condition) $\Phi$ satisfies either (i) $\Phi(E) = \tfrac{1}{n}\sum_i e_i$ (the arithmetic mean, or any permutation-symmetric linear aggregator with equal weights), or (ii) $\Phi$ is odd-symmetric ($\Phi(-E) = -\Phi(E)$) and the error distribution is symmetric about its mean.*
- *(A3, open witnesses) $F \equiv 1$.*
- *(A4, equilibrium regime) $V_t = V_*$ is held constant and the plant has reached its closed-loop equilibrium, so that $\mathbb{E}[x_t \mid V_t = V_*] = V_* - \bar{b} = V_*$ (with equal gains $k_i \equiv k$, $\bar{b} = 0$ by (A1)).*
- *(A5, zero-mean noise) $\mathbb{E}[w_t] = \mathbb{E}[v^i_t] = 0$; under case (A2.ii), the $v^i_t$ distributions are symmetric about zero.*

*Then $\mathbb{E}[\Phi(E_t) \mid V_t = V_*] = 0$, hence $\mathbb{E}[V_{t+1} \mid V_t = V_*] = V_*$.*

*Proof.* By (A4) and (A5), $\mathbb{E}[e^i_t \mid V_t = V_*] = \mathbb{E}[y^i_t - V_* \mid V_t = V_*] = \mathbb{E}[x_t] + b_i - V_* = b_i$. Under case (A2.i): $\mathbb{E}[\Phi(E_t)] = \tfrac{1}{n}\sum_i \mathbb{E}[e^i_t] = \tfrac{1}{n}\sum_i b_i = 0$ by (A1). Under case (A2.ii): (A1) with (A5) gives that the vector $E_t$ has distribution symmetric about its mean, which is zero; combined with odd-symmetry of $\Phi$, $\mathbb{E}[\Phi(E_t)] = -\mathbb{E}[\Phi(E_t)]$, so $\mathbb{E}[\Phi(E_t)] = 0$. Either way, $\mathbb{E}[V_{t+1} \mid V_t = V_*] = V_* + \eta \cdot 0 = V_*$. ∎

*Remark on scope.* (A2.i) covers the arithmetic mean and is the cleanest setting. (A2.ii) is the weakest extension that covers the median under balanced bias-split with symmetric noise, at the cost of the additional noise-symmetry assumption. Without one of these structural conditions on $\Phi$, the step from $\Phi(\mathbb{E}[E_t]) = 0$ to $\mathbb{E}[\Phi(E_t)] = 0$ does not go through in general. (A4) can be replaced by a deterministic $v^i_t \equiv 0$ version, which is the setting of the §4.1 probe.

**Consequence.** If $V_t$ differs from the latent target by any fixed gap $\Delta \neq 0$, the gap is not closed by internal dynamics. Procedural gates downstream of $\Phi$ (unanimity thresholds, decay-thaw mechanisms, dissent-override provisions) cannot rescue this, since the gate's input is already approximately zero. **Dissent is not refused; it is arithmetically annihilated.**

### 3.3 Conjecture 1: No-Scalar-Free-Lunch

The natural escape from Theorem 1 is to abandon the first-moment property of $\Phi$. Shape-sensitive scalar aggregators — max-absolute-value, variance-gated, and similar — escape the freeze on balanced bias-split populations, but the empirical evidence (§4.1) suggests they introduce a different failure mode under asymmetric populations. This motivates:

**Conjecture 1 (No-Scalar-Free-Lunch).** *There exists no scalar aggregator $\Phi : \mathbb{R}^* \to \mathbb{R}$ that is simultaneously:*

- *(P1) freeze-free on every balanced bias-split population satisfying (A1) of Theorem 1, and*
- *(P2) $L^\infty$-stable in $V$ on every asymmetric population (one whose bias vector has nonzero first moment).*

The present support is the empirical aggregation-boundary probe of §4.1 across four canonical aggregator classes (mean, median, max-absolute-value, variance-gated), not a class-wide impossibility proof. The probe shows that within the four-class sample, no tested aggregator satisfies both freeze-freedom and stability: first-moment aggregators freeze on balanced bias-split populations, while the tested shape-sensitive aggregators escape freeze but destabilize on asymmetric populations. A formal proof would need to characterize the scalar-aggregator class precisely (continuous? Lipschitz? permutation-invariant?) and show the trade-off is structural rather than a property of the probed sample. We expect the conjecture to hold in a precise form once the class is fixed; this is flagged as an open problem in §8.

If Conjecture 1 holds, the constructive consequence is that the only escape from both failure modes is to abandon scalar aggregation entirely — preserving per-witness reports for downstream interpretation rather than collapsing to a summary. This is developed in §6.

### 3.4 Proposition 2: Shared-Level / Divergent-Gradient Alias-Compatibility

Augment the model with per-agent local-gradient interpretation $\varphi_i$ as in §2, so each agent's public action map satisfies $A_i(V_0) = A(V_0)$ and $A_i'(V_0) = A'(V_0) + \varphi_i$. The control law is $a^i_t = -k_i(y^i_t - A_i(V_t))$. Let the public-alignment observable be the action-divergence metric $D(a^1_t, \dots, a^n_t)$.

**Proposition 2 (Shared-Level / Divergent-Gradient Alias-Compatibility, scope-conditional).** *Suppose (B1) $b \equiv 0$, (B2) equal gains $k_i \equiv k$, and (B3) the closed loop is at equilibrium with $V_t = V_0$ stationary. Then:*

*(2.a, observational aliasing at baseline) Action observations alone cannot distinguish a compositionally-aligned cohort ($\varphi_i \equiv 0$) from a compositionally-divergent cohort ($\varphi_i \not\equiv 0$): the equilibrium action vector satisfies $a^i_* = a^j_*$ for all $i, j$ regardless of the spread of $\varphi$. The two populations are observationally alias-compatible at baseline.*

*(2.b, alias-break under finite shift) Under a finite strategic shift $V_0 \to V_0 + \Delta V$ holding $\varphi$ fixed, the post-shift action vector inherits the local-gradient dispersion: to leading order in $\Delta V$, $(a^i_*)' - (a^j_*)' = k(\varphi_i - \varphi_j)\Delta V + O(\Delta V^2)$, so post-shift action divergence $D$ scales with $\Delta V$ and the dispersion of $\varphi_i$.*

*Proof sketch.* Under (B1)–(B3) with equal gains and $b \equiv 0$, closed-loop balance $\sum_i a^i_* = 0$ at stationary $V_0$ gives $x_* = \tfrac{1}{n}\sum_i A_i(V_0) = A(V_0)$. Substituting: $a^i_* = -k(x_* - A_i(V_0)) = -k(A(V_0) - A(V_0)) = 0$, identical across all $i$ regardless of $\varphi_i$. Under shift $V_0 \to V_0 + \Delta V$, the new equilibrium plant state is $x_*' = \tfrac{1}{n}\sum_i A_i(V_0 + \Delta V) = A(V_0) + [A'(V_0) + \bar\varphi]\Delta V + O(\Delta V^2)$ with $\bar\varphi = \tfrac{1}{n}\sum_i \varphi_i$. The post-shift action becomes $(a^i_*)' = -k(x_*' - A_i(V_0 + \Delta V)) = -k(\bar\varphi - \varphi_i)\Delta V + O(\Delta V^2)$, and pairwise differences inherit the $\varphi$-dispersion at first order. ∎

*Metric distinction.* If $D$ is variance, $D_{\text{post}} \approx k^2 (\Delta V)^2 \mathrm{Var}(\varphi)$ to leading order — quadratic in $|\Delta V|$. If $D$ is standard deviation or mean pairwise absolute divergence, $D_{\text{post}}$ scales linearly in $|\Delta V|$. Either way, detection requires $|\Delta V|$ large enough that the induced divergence clears the measurement and noise floors.

*Falsifiability hook.* The magnitude of $|\Delta V|$ needed to surface divergence is itself a theory-predicted observable: for the linear-metric case, the smallest detectable shift scales as $|\Delta V|_{\min} \sim \sigma_{\text{noise}} / (k\, \sigma_\varphi)$, where $\sigma_\varphi$ is the dispersion scale of $\varphi$ and $\sigma_{\text{noise}}$ is the action-level noise floor. The proposition is therefore falsifiable: a strategic shift of predicted magnitude that produces no measurable divergence implies either $\sigma_\varphi$ is smaller than assumed or the local-gradient model is wrong.

*Scope flag.* The proposition holds in the clean case (B1)–(B3) and is supported by the §4.2 probe in the $b \equiv 0$ two-team setting. Heterogeneous gains, non-zero $b$, nonlinear closed-loop dynamics, and full vector $V$ are deferred to §8; the earlier $(\varphi - b)$-aliasing claim of the v0.1 draft conflated a separate result with the present one and is no longer carried. **We mark this as a proposition rather than a theorem because the linearization-based scaling and the falsifiability hook are stated in a specific dynamical regime; lifting to a closed-form result over a broader dynamical class would convert the proposition.**

**Consequence.** Public alignment to $V$ is observationally alias-compatible at baseline: any nonzero $\varphi$-dispersion is indistinguishable from $\varphi \equiv 0$ from baseline action data alone under stationary $V_0$. Distinguishing them requires either independent identification of internal interpretations or a strategic shift large enough to surface the divergence. This is structurally parallel to the controller-layer observational-masking result of [1, §3.3 case (i)], lifted one scale up; the present proposition supplies the formal statement and dynamical-shift falsification path.

### 3.5 Theorem 3: Witness-Filter

**Theorem 3 (Witness-Filter).** *Suppose:*

- *(C1, alignment-correlated filter) There exists $\tau > 0$ such that $F(i, V_t) = 0$ whenever $|e^i_t| \geq \tau$.*
- *(C2, non-vanishing gap) The plant-to-prior gap $\Delta := \mathbb{E}[x_t] - V_t$ satisfies $|\Delta| > \tau$.*
- *(C3, sup-norm bounded aggregator) $\Phi$ satisfies $|\Phi(E)| \leq \|E\|_\infty := \max_i |e_i|$ for every error vector $E$. (Equivalently: $\Phi$ is sup-norm nonexpansive at the origin and $\Phi(0) = 0$. Mean, balanced weighted mean, median, and max-absolute-value all satisfy this.)*

*Then for all $t$ after the filter activates:*

$$\big| \Phi(E_t^F) \big| \leq \tau, \qquad \big| V_{t+1} - V_t \big| \leq \eta\, \tau.$$

*Proof.* By (C1), every $e^i_t$ in $E_t^F$ satisfies $|e^i_t| < \tau$, so $\|E_t^F\|_\infty < \tau$. By (C3), $|\Phi(E_t^F)| \leq \|E_t^F\|_\infty < \tau$. The update bound $|V_{t+1} - V_t| = \eta \cdot |\Phi(E_t^F)| \leq \eta\,\tau$ follows immediately. ∎

**Consequence.** The corrective signal available to the prior update is *capped* by the filter: the per-step update magnitude is bounded by $\eta\tau$ regardless of how large the underlying gap $|\Delta|$ is. This makes correction arbitrarily slow (when $\eta\tau$ is small relative to $|\Delta|$) or directionally insufficient (when the surviving cohort's first-moment error is small or zero), but does not by itself prove the gap cannot close — a bounded per-step update can still accumulate. Persistent non-closure requires an additional residual-bias or zero-mean-survivor condition, supplied by Theorem 4 for the surviving-cohort fixed-point case. The cap holds **regardless of the choice of aggregator $\Phi$** within the sup-norm-bounded class. In particular, shape-preserving receipt-lineage architectures (which fall outside the scalar class but satisfy a generalized version of (C3)) inherit the same bound when applied to the filtered population: the corrective signal has been removed before it reaches the aggregation layer.

**Corollary (necessary-but-not-sufficient architecture).** Shape-preserving aggregation (the constructive class identified by Conjecture 1) is *necessary but not sufficient* for reality-tracking governance of a shared prior. Any sufficient condition must include both:

- **(a)** shape-preserving aggregation, AND
- **(b)** witness inclusion independent of $V_t$-alignment.

Violating either permits prior-freeze regardless of the other.

### 3.6 Theorem 4: Persistence of Dissident-Filter Effects

**Theorem 4 (Persistence).** *Suppose the filter $F$ is applied at $t = 0$ only, removing all agents with $|b_i| \geq \tau$; thereafter $F \equiv 1$ on the surviving sub-population $S$. Suppose further:*

- *(D1, residual bias) The surviving-population mean bias $\bar{b}_S := \frac{1}{|S|}\sum_{i \in S} b_i$ is non-zero.*
- *(D2, first-moment aggregator) $\Phi$ is first-moment over $S$ (as in §3.2).*
- *(D3, no exogenous $V$ perturbation) $V_t$ evolves only via the aggregator update.*
- *(D4, plant-controller equilibration) The closed-loop dynamics drive the plant state toward $x_* = V_* - \bar{b}_S$ at any fixed $V_*$.*

*Then the system has a fixed point $(V_*, x_*)$ satisfying $V_* - x_* = \bar{b}_S$. At this fixed point, the surviving cohort reports zero net first-moment error — individual surviving agents report $e^i_* = b_i - \bar{b}_S$, which is generally non-zero and identifies the agent's bias relative to the cohort mean, but the aggregate $\Phi(E^F) = 0$ in expectation under (D2). $V$ therefore stops updating, and the plant-to-prior error $|V_* - x_*| = |\bar{b}_S|$ persists. Under the fixed cohort $S$ and fixed update rule $\Phi$ specified by (D1)–(D4), this fixed point is stable to the system's internal dynamics: the error cannot be reduced by any further evolution of $V$ alone. Escape requires exogenous intervention — any of: changing the witness cohort (e.g., adding witnesses whose biases shift $\bar{b}_S$ toward zero), changing the update rule, or perturbing $V$ directly.*

*Proof.* By (D4), at any $V_*$ the closed loop drives $x_t \to V_* - \bar{b}_S$. At this $x_*$, agent $i \in S$ observes $y^i_* = x_* + b_i = V_* + (b_i - \bar{b}_S)$, so reports error $e^i_* = y^i_* - V_* = b_i - \bar{b}_S$. The vector of errors over $S$ has mean zero by construction, so by (D2), $\Phi(E^F) = 0$ in expectation. By (D3), $V$ stops updating. The plant-to-prior error $|V_* - x_*| = |\bar{b}_S|$ is positive by (D1). Stability of the fixed point under internal dynamics: any small perturbation of $V$ away from $V_*$ moves the equilibrium $x_*$ correspondingly, leaving the surviving population's mean error at zero (still in expectation), so the aggregator produces no net update; the perturbation is not amplified. Internal escape would require either modifying $\Phi$ (excluded by the fixed-rule assumption) or modifying $S$ (excluded by the fixed-cohort assumption); both are exogenous interventions in the present model. ∎

**Prose-level corollaries (presented as predictions, not theorems).**

The fixed-point structure of Theorem 4 has four implications for institutional analysis:

- **Ghost-filter pathology.** The filter need not remain active for the error to persist. The drifted equilibrium is self-sustaining and looks filter-free from inside. Statements of the form "we don't stack-rank anymore" are not a defense; the filter could have operated at any prior time (founding cohort selection, methodology rollout, post-merger consolidation, leadership transition), and the population has been running on its output ever since.
- **Efficiency illusion.** From inside the filtered equilibrium, the drift phase is experienced as operational improvement: meetings are faster, consensus is easier, execution feels smoother. The "improvement" is the absence of the reality-correction friction that the filtered dissenters would have provided.
- **Active reintroduction required.** Cessation of filtering is insufficient for remediation. A filter-free regime starting from a filtered population continues to drift in the filtered direction; corrective signal requires deliberate incorporation of outside witnesses (hiring against the current $V$, adversarial external review, explicit dissent mandates).
- **Temporal-capture asymmetry.** A single filtering event produces durable governance drift without continued intervention. This is strictly cheaper than continuous capture and does not require ongoing infrastructure to maintain. One purge at the right moment installs a long-lasting governance defect.

## 4. Empirical demonstrations

The four results above are supported by three numerical probes implementing the model of §2. The probes are intended as existence demonstrations and parameter-class sketches, not as empirical calibration; the simulation source is available as a companion artifact (`shared_vision.py`).

### 4.1 Aggregation-boundary probe (Conjecture 1)

Four aggregators (MEAN, MEDIAN, MAX_ABS, VARIANCE_GATED) crossed with four 4-agent bias configurations (balanced bias-split, asymmetric three-vs-one, asymmetric one-vs-three, uniform). Outcome metric: long-horizon $V$ trajectory under each pairing.

| Aggregator | Balanced bias-split | Asymmetric population |
|---|---|---|
| MEAN | locked (V-freeze) | locked |
| MEDIAN | locked (V-freeze) | runaway |
| MAX_ABS | unlocked, unstable | runaway |
| VARIANCE_GATED | unlocked, unstable | runaway |

The probe shows that within the four-class sample, no tested aggregator satisfies both freeze-freedom and stability: first-moment aggregators freeze on balanced bias-split populations, while the tested shape-sensitive aggregators escape freeze but destabilize on asymmetric populations.

### 4.2 Alias-compatibility probe (Proposition 2)

Two-team population ($n = 2$) with $b \equiv 0$ and hidden internal interpretation spread $\varphi$. Pre-shock: $V_t \approx 0$, action divergence measured. Post-shock: $V_t$ stepped to $\Delta V$, action divergence re-measured.

The probe produces action divergence of algebraically zero pre-shock regardless of $\varphi$ (within numerical precision), and divergence scaling with $\varphi$ and $\Delta V$ post-shock — quadratic in $|\Delta V|$ for variance and linear for standard-deviation / mean-pairwise-absolute-divergence reporting, matching the metric distinction in §3.4. The hidden compositional spread is structurally invisible to action-level alignment metrics under stationary $V$ and surfaces under strategic shift, exactly as Proposition 2 predicts in its clean (B1)–(B3) regime.

### 4.3 Filter probe (Theorems 3 and 4)

Four-agent population (three aligned, one dissenter) with permanent stack-rank-style filter: any agent whose $|e_t|$ exceeds a threshold at any step is removed permanently from the witness pool.

| Aggregation | Filter | $V_{\text{final}}$ | $\|x - V\|$ | Inclusion fraction |
|---|---|---|---|---|
| MEAN | open | 0.05 | 0.80 | 1.00 |
| MEAN | $\|e\| > 0.8$ removed | $-5.96$ | **5.16** | 0.75 |
| MAX_ABS | open | 6.00 | 7.00 | 1.00 |
| MAX_ABS | $\|e\| > 0.8$ removed | $-5.96$ | **5.16** | 0.75 |

Three observations land:

1. **Witness inclusion is the bigger lever than aggregation rule.** Filter activation increases plant error ~6× (0.80 → 5.16), dwarfing the aggregator-choice effect.
2. **Once the filter is active, MEAN and MAX_ABS produce identical $V$ trajectories.** The surviving population is homogeneous, so the aggregation rule collapses to a distinction without a difference. This is the empirical face of Theorem 3's "regardless of aggregator" clause.
3. **One-shot filtering produces persistent drift.** The dissenter was removed at $t = 0$ and the drift ran for the subsequent 100 steps without continued filtering, terminating at a stable fixed point with $|x - V| = |\bar{b}_S|$ as Theorem 4 predicts.

## 5. Worked case study: Agile/Scrum

Agile/Scrum is presented here as one worked example of the three-layer pathology, chosen for the unusual legibility of the gap between its stated mechanism and its enacted aggregation layer. The framework's claim class is broader (federated learning systems with non-IID clients, KPI-driven managerial regimes, sabermetrics, hiring analytics, dashboard-driven public health, criminal-justice risk assessment, military AI doctrine); we develop one case here in depth and treat the others as future work.

The structural argument has three parts.

**The stated mechanism.** Agile/Scrum's stated mechanism is feedback-driven and adaptive. Sprint retrospectives explicitly solicit team-level disagreement. Daily standups create surface area for in-flight blockers. Sprint reviews are designed to catch product-direction errors before they compound across iterations. By the framework's nominal description, Agile is a methodology that ritualizes exactly the kind of dissent-surfacing activity that the witness-filter pathology relies on suppressing.

**The enacted aggregation layer.** The artifacts that propagate from team rituals to organizational governance are velocity, burndown charts, OKR attainment scores, roadmap-confidence aggregates, and similar mean-like summaries. Leadership consumes these artifacts, not the raw retrospective output. Disagreement generated at the team layer is collected, aggregated into a scalar summary, and then governs the prior at the organizational layer through that summary. The aggregation step from team-level rituals to leadership-consumed metrics is where Theorem 1's pathology lives: a team in which half the members report behind-schedule and half report on-track will have a velocity score that averages out, consistent with Theorem 1's first-moment-aggregator hypothesis.

**The witness-curation layer.** Performance management correlated with on-narrative contribution, "culture fit" hiring, attrition of disaffected members, and stack-ranking systems all act as witness-inclusion filters in the sense of Theorem 3. The cumulative effect is that the surviving population over time is selected for $V$-alignment, so that even if the aggregation layer were repaired, the witness population available to it would be pre-curated to produce zero corrective signal. Theorem 4's persistence result then applies: a single curation event (a founding hiring profile, a methodology-rollout culling, a leadership transition) suffices to lock in drift that requires deliberate outside-witness reintroduction to remediate.

The result that survives critique, scoped:

> *Managerial systems that rely on mean-like aggregation over shared coordinating priors and on alignment-correlated witness inclusion are structurally vulnerable to the bias-cancellation and witness-filter pathologies of §3, regardless of how participatory or data-driven the methodology appears at the ritual layer.*

This claim class is broader than Agile and is independent of the merits of Agile as a software-development methodology. The case is sharp because Agile's stated mechanism makes the gap between intended and enacted governance unusually visible; it is not sharp because Agile is a uniquely vulnerable methodology. The same structural analysis applies to any methodology whose feedback rituals are aggregated into mean-like summaries before reaching the governance layer.

## 6. Architectural implication

Theorem 1 and Theorem 3 jointly identify what a corrective architecture must do, and Theorem 4 identifies what it cannot afford to neglect. Conjecture 1 strengthens the aggregation-side claim *conditionally* on its probe-backed form becoming a theorem; until then, the design claim below is read as a design conjecture for the scalar-aggregator class observed in §4.1 rather than as a universal impossibility.

**The aggregation requirement.** Theorem 1 rules out first-moment scalar aggregators on balanced bias-split populations. Conditional on Conjecture 1 in its conjectured form (or restricting attention to the four canonical aggregator classes probed in §4.1), the shape-sensitive scalar aggregators are also ruled out — they escape freeze but destabilize under asymmetric populations. The constructive complement, within the class of candidates eliminated so far, is an architecture that *does not collapse witness reports to a scalar at all*: per-witness receipt preservation, with each witness's error report and basis fields propagated to the governance layer separately for downstream interpretation. If Conjecture 1 promotes to theorem, this becomes a universal necessity claim over the scalar-aggregator class; in its current probe-backed form, it is a specific design recommendation against the aggregator classes probed, with the broader universal claim flagged as conjectural.

The cohort-witness principle from receipt-based agent-governance architectures admits a sharper reading in light of this: cohort witnessing works not because of redundancy but because it preserves distributional shape across witnesses. The pattern of disagreement across cohort members is itself evidence about whether $V_t$ is serving as a coordinating prior for the cohort population. Any aggregation rule that collapses the cohort to a summary statistic destroys this evidence.

**The witness-inclusion requirement.** Theorem 3 establishes that even the strongest receipt-preserving aggregator is defeated by alignment-correlated witness curation. The corrective architecture must therefore additionally maintain witness inclusion that is *independent* of $V_t$-alignment. This rules out stack-ranking semantics, performance management correlated with on-narrative contribution, "culture fit" filters indexed on behavioral proxies for compliance, and attrition mechanisms that select against disaffected members. It rules in: explicit dissent mandates, adversarial external review, hiring policies that require diversity on the dimensions that constitute the prior's domain, and rotation or sortition among witness participants.

**Joint necessity (conditional sufficiency).** Theorem 3's corollary shows that both conditions — shape-preserving aggregation AND open witness inclusion — are jointly necessary. Joint *sufficiency* is plausible on the strength of the analysis but not proved here: it would require showing that any architecture satisfying both conditions avoids the pathologies of §3 under all admissible closed-loop dynamics, which is an open problem flagged in §8. The shipping claim is therefore: neither condition alone suffices; both are required.

**Temporal correction.** Theorem 4 adds that even an architecture satisfying both conditions, applied to a population that has previously been filtered, requires exogenous cohort modification to escape the inherited drift. Architectural correctness is not retroactive: turning on receipt-lineage and opening witness inclusion does not undo prior curation, because the surviving cohort's internal dynamics are stable at the drifted fixed point. The remediation problem is separate from the prevention problem.

**Closing.** The failure mode is not that organizations lack feedback. It is that they destroy the structure of feedback before governance sees it. Scalar aggregation erases disagreement (Theorem 1); alignment-correlated inclusion removes disagreeing witnesses (Theorem 3); prior curation persists after the filter is gone (Theorem 4). Public alignment around the shared prior cannot distinguish concord from divergence at baseline; only strategic shift surfaces what the aggregation layer has been hiding (Proposition 2). Corrective governance therefore requires both receipt-preserving witness structure *and* witness inclusion independent of prior alignment. One without the other is theater.

## 7. Related work

The paper's nearest neighbors span several disjoint literatures. We name each, state what is shared, and state what is structurally different, with the goal of preempting the "isn't this just X with new branding?" response for each adjacent literature.

### 7.1 Distributed consensus and social choice

The distributed-systems consensus literature — Paxos [3], Raft [4], and the Byzantine fault-tolerance family — treats "how does a distributed system agree on a value under failures" as its central question. The shared structural move is the presence of an aggregation or voting mechanism that reduces distributed observations to a common decision. The structural difference is that consensus protocols *assume* correct or boundedly-Byzantine inputs; the pathology identified here is about correct procedure running on inputs whose distribution defeats the procedure's expressiveness. No Paxos-style protocol fails on balanced bias-split witnesses in the sense of Theorem 1, because Paxos is about value-selection, not value-correction. The aggregation-masking result is not a safety failure or a liveness failure in the consensus sense; it is an *observability* failure in a setting that uses consensus machinery as part of its governance stack.

Social-choice theory — Arrow's impossibility theorem [5], Gibbard-Satterthwaite [6, 7], Condorcet paradoxes — is closer in flavor. Arrow proves that no aggregation rule over preference orderings satisfies a small axiom set; Conjecture 1 has a structurally similar form (impossibility across a family of aggregators) but operates on a different object. Arrow aggregates preferences (strategic, ordinal, action-shaping); Conjecture 1 aggregates error signals (descriptive, cardinal, feedback-shaping). The social-choice results address the *design* of one-shot aggregation rules under voter-behavior axioms; Conjecture 1 (if it holds in the conjectured form) addresses the *closed-loop dynamic consequence* of repeatedly applying a defective aggregator over time.

The epistemic-democracy literature — Condorcet jury theorem and its modern extensions [25] — is the closest social-choice cousin to the present work, since it explicitly aggregates *judgments* (truth-tracking error signals) rather than preferences. Theorem 3 can be read as a dynamic violation of two of the standard epistemic-democracy axioms: independence (the witness-inclusion filter induces correlation across surviving witnesses), and competence (the alignment-correlated filter selects against agents whose judgments are most informative about the prior-to-reality gap). The present results extend the epistemic-democracy framework into a closed-loop dynamic setting in which the prior $V_t$ being aggregated also influences the witness population aggregating it. A related observation: $V$-alignment hiding asymmetric private information ($b_i, \varphi_i$) is structurally reminiscent of Aumann's agreement theorem [26] read in reverse — agents share the prior precisely because their private signals have been compressed into an alignment summary that cannot distinguish "concordant beliefs" from "differently-biased agents projecting onto a common token."

### 7.2 Federated learning, distributed estimation, and multi-agent bandits

Federated learning with shared priors or regularization [8] is the nearest technical cousin. A central server aggregates gradient updates from distributed clients with heterogeneous data; the shared prior is the global model, the aggregator is FedAvg or a robust variant. Bias-split is a real open concern in this literature under "heterogeneous clients" or "non-IID data." The structural difference is that federated learning frames this as an *optimization* problem to be solved by a better aggregator, regularizer, or client-reweighting scheme; Conjecture 1 conjectures the problem has no solution within the scalar-aggregator class. Proposed fixes (FedProx, FedNova, personalized FL, clustered FL) are consistent with this conclusion: each escapes mean-aggregation masking only by abandoning the scalar-summary form or the assumption of a single shared prior.

Multi-armed bandits with shared priors [9] and distributed estimation [10, 11] treat related structural objects, with agents updating a common parameter on the basis of local observations. The structural difference is that both literatures model agents as *epistemic* units attempting to learn a true parameter, rather than as *governed* units aligning on a prior whose authority and update rules are institutionally determined. The witness-filter theorem (Theorem 3) has no analogue in these literatures because witness inclusion is assumed.

The performative-prediction literature [27] is the closest contemporary analogue of Theorem 3 in the machine-learning setting. Performative prediction studies the case where a deployed model's predictions induce distribution shift on the data the model is subsequently trained on; the model's state $\theta_t$ becomes a determinant of its own training distribution. Theorem 3 is the governance-layer counterpart: the shared prior $V_t$ becomes a determinant of which agents are included in the next aggregation step (via the alignment-correlated filter $F$). Both results identify closed-loop pathologies where the system's own state regulates the data feeding back into it; the architectural-implication argument of §6 specializes to performative prediction by saying that no choice of training-time aggregator can correct for deployment-time data filtering correlated with model state.

### 7.3 Cybernetics and control-theoretic observability

Ashby's law of requisite variety [12] is the deepest structural cousin. Ashby's formulation — a regulator must match the variety of the regulated system — implies, in the aggregation setting, that a regulator with scalar output cannot regulate a system whose state has richer structure than a scalar. Conjecture 1 specializes this to a particular class of aggregators: first-moment scalar aggregators lack the variety to distinguish balanced bias-split populations from zero-error populations. Beer's Viable System Model [13] takes the cybernetic insight to organizational design directly; the present aggregation-masking result is compatible with Beer's work and can be read as a sharpening of *why* scalar management summaries fail in variety-rich organizations.

Control-theoretic observability [14] is another direct cousin. Observability asks when the internal state of a system can be reconstructed from its outputs over time; if unobservable, no feedback controller can regulate it. Theorem 3 can be read as a statement about *induced* unobservability: the filter removes precisely the state components carrying the information needed to reconstruct the plant-prior gap. Standard observability analysis treats unobservability as a structural property of the plant; Theorem 3 identifies a class of governance choices that *produce* unobservability as a downstream consequence — a dynamic the control literature does not typically model because it assumes the observer is not adversarial to the measurement.

### 7.4 Organizational epistemology, groupthink, and the metrics critique

The groupthink literature [15, 16] names many of the same empirical phenomena — organizations agreeing on wrong things, failure to surface dissent, after-the-fact recognition that warnings were given and ignored — but in social-psychological terms. The framing here is complementary, not competitive: part of what looks like groupthink is, mechanically, mean-aggregation masking and witness filtering. Self-censorship and illusion-of-unanimity are downstream effects of the aggregation layer producing no signal; the aggregation layer produces no signal because it is structurally blind to bias-split populations. Both explanations coexist.

The metrics-critique literature — Muller's *The Tyranny of Metrics* [17], Goodhart's law [18], Campbell's law [19], and Deming's statistical-process-control critiques [20] — is the practitioner-facing literature closest to the paper's implications. Muller catalogues cases of metrics-driven governance pathology; Goodhart names the strategic-response mechanism. Theorem 1 supplies a specific structural account of *one mechanism* by which this happens: aggregated metrics are blind to bias-split witness populations, so an organization whose members produce genuinely informative but bias-split error signals will see "no disagreement" in the aggregate. Theorem 3 supplies the matching witness-filter mechanism. The metrics-critique literature documents the pathology; the theorems supply a class of mechanisms.

High-reliability-organizations work [21, 22] is an empirical cousin. The HRO literature identifies "deference to expertise" and "preoccupation with failure" as practices that maintain organizational attention on edge signals; in the present framing, these practices are witness-inclusion-preserving interventions resisting the drift toward alignment-correlated witness curation that Theorem 3 names as the upstream pathology. HRO practice and the constructive implication of §6 are structurally aligned, though HRO does not state the formal impossibility motivating them.

### 7.5 Robust statistics, wisdom of crowds, and statistical aggregation

The robust-statistics literature — breakdown-point theory (Huber [28]) and influence-function analysis (Hampel [29]) — is the most direct technical cousin of Theorem 3 and Conjecture 1. The breakdown point of an estimator measures the largest fraction of contaminated observations the estimator can tolerate before its output becomes arbitrarily wrong; the influence function characterizes how a single observation perturbs the estimator's value. Theorem 3 in the present setting can be read as a closed-loop statement about a related quantity: when witness inclusion is correlated with prior-alignment, the *retained* observations have bounded influence by construction, regardless of the estimator's nominal breakdown point. The witness-filter pathology is structurally upstream of the choice of robust estimator, and explains why M-estimators and trimmed means do not by themselves rescue the governance setting: the trimming decision has been made by the alignment filter before the robust estimator sees the data. Conjecture 1's no-scalar-free-lunch claim is a finite-class observation in the same spirit as classical robust-statistics impossibility results, restricted here to the four canonical aggregator classes probed in §4.1; tightening the impossibility to the full class of permutation-symmetric scalar aggregators in the breakdown-point sense is one natural form of the §8 open problem.

Galton's 1907 ox-weight experiment [23] and its modern popularization as "wisdom of crowds" [24], including Page's diversity-prediction theorem [30], establish the canonical case for aggregation: under independent errors with zero mean and sufficient cohort diversity, aggregate error shrinks as $1/\sqrt{n}$. The conditions named in that literature as *requirements* (independence, diversity, decentralization, aggregation form) coincide with the conditions whose failure modes our theorems analyze, so the present contribution is not the first-time identification of these failure conditions but rather a *control-theoretic dynamic formalization* of them: the closed-loop consequences of operating in regions where the wisdom-of-crowds requirements are systematically violated by the governance regime itself, rather than incidentally violated by the underlying population. Balanced bias-split populations violate the diversity-without-systematic-bias requirement (Theorem 1); witness filtering violates the independence requirement endogenously (Theorem 3); the dynamic-persistence result (Theorem 4) describes the regime the system equilibrates to once those requirements are violated. Wisdom-of-crowds is not wrong; the present results describe what happens inside the parameter regions it explicitly excludes when the exclusion is produced by governance choice rather than measurement noise.

### 7.6 Controller-layer observational masking (Paper 23)

Paper 23 of this series [1] proves a structurally parallel result at the controller layer: a non-self-identical controller — one whose internal composition changes across handoffs, fatigue cycles, or role transitions — can be observationally indistinguishable from a self-identical one under normal operation, with divergence surfacing only under stress events that strain the controller's composition. The results here are the multi-agent analogue: a cohort whose members differ in local-gradient interpretation $\varphi_i$ is alias-compatible with a $\varphi \equiv 0$ cohort under stationary conditions, with divergence separating only under strategic shift (Proposition 2). The two papers can be read as a masking trilogy in progress: Paper 23 names identifiability masking (controller composition unrecoverable from outputs), the present paper names observational aliasing (alignment versus divergence indistinguishable at baseline), and a forthcoming companion paper on epistemic border control names substitution forcing (target unsensed, proxy regulated as if sensed).

The single-sentence braid: **organizations mistake compressed public alignment for resolved internal composition.** Paper 23 names the phenomenon at the controller layer; this paper names it at the organizational layer and supplies the specific aggregation-layer mechanism by which organizations fail to notice it even when they nominally have feedback loops. The two papers are distinct objects — the aggregation-layer mechanism is not derivable from Paper 23's controller-layer theorem — but they share a structural move and cross-cite naturally.

### 7.7 Receipt-lineage and agent-governance architectures

The constructive architectural implication of §6 — that escape from the three-layer pathology requires preserving per-witness receipts and maintaining open witness inclusion — connects to ongoing work on governance architectures for AI agent systems where receipt-based authority and per-action lineage are proposed as first-class primitives [2]. The contribution of this paper to that line is to identify the formal problem such architectures solve: receipt-lineage is the architectural answer Theorem 1 and Conjecture 1 jointly motivate (with the strength of "motivate" depending on whether Conjecture 1 is taken in its probe-backed or theorem-strength form). Reciprocally, Theorem 3 identifies what receipt-lineage architectures *cannot* solve on their own: open witness inclusion must also be maintained, or the receipts produce no corrective signal.

## 8. Open / deferred

- **Conjecture 1 as a theorem.** The strongest item on the list. A proof requires fixing the scalar-aggregator class precisely (continuous? Lipschitz? permutation-invariant?) and exhibiting the structural trade-off between (P1) and (P2) within that class. We expect the conjecture to hold in a precise form and treat its theorem-ization as the most valuable single next piece of work.
- **Vector-valued $V_t$.** The scalar prior is the cleanest setting and exhibits all four pathologies. The vector case is where alias-compatibility (Proposition 2) gets richer: agents can align on some components and diverge on others, opening masking modes that the scalar case cannot exhibit. Sketched in working notes; left for a sequel.
- **The binding problem.** This paper treats $V_t$ as updated by the aggregator and does not address how $V_t$ is initially set, by whom, with what authority. The binding problem (who authors $V_t$, under what legitimacy, with what receipt-lineage governing the authoring) is structurally distinct from the dynamics problem (once $V_t$ exists, when does it freeze?). A receipt-based governance treatment of the binding problem is a natural sequel and connects to admissibility-family work elsewhere in the program.
- **Empirical calibration.** The probes of §4 are existence demonstrations, not empirical calibration. Real organizational measurements of bias distribution, witness-filter intensity, and aggregation-layer summary structure would let the theorems be applied as post-hoc diagnostics rather than illustrative theory. This is a case-study companion problem.
- **Non-managerial domains.** Federated learning systems, multi-arm bandit ensembles with shared posteriors, distributed scientific consensus, and consensus-protocol deployments for value-correction (rather than value-selection) are all instances of the framework's claim class. Each merits its own worked development.
- **The remediation problem.** Theorem 4's "active reintroduction required" clause raises a separate question: how does an organization that has been running on a filtered population for some time reintroduce outside witnesses without immediately filtering them again? This is a transition-dynamics problem that the present static-fixed-point analysis does not address.

## References

[1] Beck, J. (2026a). Ops Is Control with a Non-Self-Identical Controller. Δt Framework, Paper 23. Zenodo. https://doi.org/10.5281/zenodo.19055415

[2] Beck, J. (in preparation). Receipt-Lineage Governance and the Admissibility Family. Δt Framework, working note.

[3] Lamport, L. (1998). The part-time parliament. *ACM Transactions on Computer Systems*, 16(2), 133–169.

[4] Ongaro, D., & Ousterhout, J. (2014). In search of an understandable consensus algorithm. *USENIX ATC*.

[5] Arrow, K. J. (1951). *Social Choice and Individual Values.* Wiley.

[6] Gibbard, A. (1973). Manipulation of voting schemes: a general result. *Econometrica*, 41(4), 587–601.

[7] Satterthwaite, M. A. (1975). Strategy-proofness and Arrow's conditions. *Journal of Economic Theory*, 10(2), 187–217.

[8] McMahan, B., Moore, E., Ramage, D., Hampson, S., & y Arcas, B. A. (2017). Communication-efficient learning of deep networks from decentralized data. *AISTATS*.

[9] Russo, D., & Van Roy, B. (2014). Learning to optimize via posterior sampling. *Mathematics of Operations Research*, 39(4), 1221–1243.

[10] Tsitsiklis, J. N. (1984). *Problems in decentralized decision making and computation.* PhD thesis, MIT.

[11] Borkar, V. S. (2008). *Stochastic Approximation: A Dynamical Systems Viewpoint.* Cambridge University Press.

[12] Ashby, W. R. (1956). *An Introduction to Cybernetics.* Chapman & Hall.

[13] Beer, S. (1972). *Brain of the Firm.* Allen Lane.

[14] Kalman, R. E. (1960). On the general theory of control systems. *IFAC Proceedings*, 1(1), 491–502.

[15] Janis, I. L. (1972). *Victims of Groupthink.* Houghton Mifflin.

[16] Esser, J. K. (1998). Alive and well after 25 years: a review of groupthink research. *Organizational Behavior and Human Decision Processes*, 73(2–3), 116–141.

[17] Muller, J. Z. (2018). *The Tyranny of Metrics.* Princeton University Press.

[18] Goodhart, C. (1975). Problems of monetary management: the U.K. experience. In *Papers in Monetary Economics*, Reserve Bank of Australia.

[19] Campbell, D. T. (1979). Assessing the impact of planned social change. *Evaluation and Program Planning*, 2(1), 67–90.

[20] Deming, W. E. (1986). *Out of the Crisis.* MIT Press.

[21] Weick, K. E., & Sutcliffe, K. M. (2007). *Managing the Unexpected.* Jossey-Bass.

[22] Roberts, K. H. (1990). Some characteristics of one type of high reliability organization. *Organization Science*, 1(2), 160–176.

[23] Galton, F. (1907). Vox populi. *Nature*, 75, 450–451.

[24] Surowiecki, J. (2004). *The Wisdom of Crowds.* Doubleday.

[25] List, C., & Goodin, R. E. (2001). Epistemic democracy: generalizing the Condorcet jury theorem. *Journal of Political Philosophy*, 9(3), 277–306.

[26] Aumann, R. J. (1976). Agreeing to disagree. *Annals of Statistics*, 4(6), 1236–1239.

[27] Perdomo, J. C., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative prediction. *ICML*.

[28] Huber, P. J. (1964). Robust estimation of a location parameter. *Annals of Mathematical Statistics*, 35(1), 73–101.

[29] Hampel, F. R. (1971). A general qualitative definition of robustness. *Annals of Mathematical Statistics*, 42(6), 1887–1896.

[30] Page, S. E. (2007). *The Difference: How the Power of Diversity Creates Better Groups, Firms, Schools, and Societies.* Princeton University Press.
