# Epistemic Border Control as Proxy Regulation Under Partial Observability

*Working note — started 2026-04-21, single-agent sim folded in 2026-04-22. Bucket: **earning its keep** — gate item 1 substantially cleared, sibling-vs-§N still pending compound-regime test. Paper 25 candidate or possibly §N case-study extension of Paper 24; promotion deferred until the compound-regime sim runs and the literature differential holds.*

## Core claim

Discourse communities and moderation systems operate as feedback controllers trying to regulate epistemic risk under partial observability. *Truth* is a slow, latent, costly-to-observe variable; *reputational contamination, stylistic contagion, and coalition-adjacency risk* are fast, legible, and cheap. Where no real-time sensor on truth exists, the controller is *structurally forced* to substitute a proxy objective $V'$ (reputational containment) for its nominal objective $V$ (truth-tracking), **while the rhetoric remains fixed on $V$**. The substitution is architectural, not a corruption: sincere regulators facing the same sensor set produce the same substitution.

**Paper-line candidate** (sharpened to necessity-framing after agent-governor-claude's read, 2026-04-21):

> **Where no real-time sensor on truth exists and the available observables load on reputational contamination, discourse regulators *must* substitute reputational containment for truth-tracking. The substitution is structurally forced by observability asymmetry — not a corruption of sincere intent, and not a slow drift toward bad metrics, but an architectural consequence of what the controller can and cannot sense. Sincere regulators facing the same sensor set produce the same substitution.**

## The load-bearing distinction

> **The rhetoric remains fixed on $V$ while the actual controlled variable is $V'$.**

Not "drift" (which implies slow creep, which is Goodhart-adjacent). The substitution is not a temporal corruption — $V'$ replaces $V$ *at every $t$ where $T$ is unobservable in real time*. Call this **control-target substitution** or **objective aliasing under observability asymmetry**.

This is not Goodhart's law, and the distinction is specifically necessity vs. possibility. Goodhart says *a measure becomes a target* — a contingent corruption that can in principle be avoided by better-measured targets or more disciplined measurement. The present claim is sharper: when the underlying target $T$ has no real-time sensor at all, no amount of sincere intent produces $T$-tracking. The controller architecturally cannot optimize what it cannot sense. The substitution is necessary, not contingent.

**Structural mechanism, agential action.** The mechanism is structural (no real-time $T$-sensor exists); the action is agential (humans choose $U_t$ — stigma, derisive framing, suppression, epistemic quarantine — under structural pressure). The substitution does not require anyone to consciously decide "I am now optimizing $V'$ instead of $V$"; but it is also not performed by the controller alone. Human agents deploy $U_t$ under a structural constraint that narrows their optimizable options. Blaming individuals misses that they may be acting in sincere pursuit of $V$; absolving them misses that they still make choices about framing, stigma, and which topics receive which treatment. The paper has to hold both truths: the mechanism is structural, the moves inside it are chosen.

## Relation to Paper 24

Same structural family, distinct mechanism:

|  | Paper 24 | This proposal |
|---|---|---|
| Scale | Organizational governance | Discourse / community moderation |
| Nominal objective | Plant state tracking via $V_t$ | Truth-tracking via epistemic hygiene |
| Failure layer | Aggregation + witness filter | Observability-driven target substitution |
| Effect on $V_t$ | Freezes against updates | Gets *silently replaced* by $V'_t$ |
| Architectural fix | Shape-preserving aggregation + open witness inclusion | ??? (open — the whole point of the seed) |

Paper 24's failures freeze $V$ against updates: the system fails to learn. This proposal's failure is weirder: the system *does* learn, but it learns the proxy. Same umbrella of "controllers under partial observability get fooled by their own sensors," but the specific pathology is different enough to warrant independent treatment — if the three-test gate below clears.

## Minimal state decomposition

Adopted essentially as-is from chatty's sketch:

- $T_t$ — object-level claim quality / truth state. Latent, slow, expensive to measure.
- $I_t$ — institutional opacity / incentive-to-hide state. Latent, usually not directly observable.
- $R_t$ — reputational / coalition-risk state. Partially observable via coalition signals.
- $C_t$ — contamination / crank-adjacency state. Observable via rhetorical markers.

Observation:

- $Y_t$ — what participants and moderators can actually see in real time: rhetoric, associations, source cues, past scandals, adjacent-community signals, weak evidence.

Control:

- $U_t$ — boundary-policing intensity: stigma, derision, pre-emptive framing, topic suppression, trust signaling, epistemic quarantine.

**The load-bearing asymmetry:** $Y_t$ loads heavily and quickly on $R_t$ and $C_t$, only weakly and slowly on $T_t$ and $I_t$. Truth is slow; contamination is fast.

## Control pathologies, split by rigor

Agent-governor-claude flagged that the original list mixed formal claims with illustrative analogies and presented them as though they had equal theoretical commitment. Splitting them honestly:

**Formally instantiable (the sim should reproduce these):**

- **Control-target substitution (the headline).** The controller optimizes $V'$ (reputational containment) instead of $V$ (truth-tracking) whenever $Y_t$ loads on $V'$ and not on $V$. Necessity-framed, not possibility-framed. *Reproduced in the single-agent sim; see §"Sim results" below.*
- **High gain / overshoot.** When $K$ is large relative to the signal-to-noise ratio on $Y_t$, weak contamination signals produce disproportionate suppression action. Classic proportional-controller instability — a sim should reproduce this with standard parameters.
- **Hysteresis.** Threshold asymmetry in topic-classification: the threshold to enter "suspect" status is lower than the threshold to leave. Directly analogous to Paper 23's §2.1 handoff reset structure, and formally instantiable as a state-dependent discrete variable.
- **Shock-statistics mismatch (added 2026-04-22 after the sim run).** If the filter's model assumes smooth (e.g., Gaussian) innovations on $C$ but the real $C$ process has heavy-tailed or impulsive shocks (crank-arrival events, coalition rupture, reputational cascades), then $Y_t$-jumps that the filter cannot explain as within-model $C$-noise get partially misattributed to $T$, and the standard substitution cascade fires even at high $\alpha_T/\alpha_C$. The broader necessity statement the sim suggests: substitution is forced whenever the filter's assumed state statistics diverge from the real ones on a channel coupled to $Y_t$, not only when $\alpha_T \ll \alpha_C$. Shown to persist at $\alpha_T / \alpha_C = 10$ in the sim.

**Illustrative analogies (useful in prose, no theoretical commitment):**

- **Lag compensation on the wrong signal.** The loop reacts to the *last* epistemic disaster; post-anti-vax, post-QAnon, it sees everything through yesterday's transfer function. Evocative framing, not a formally distinct pathology from integral memory.
- **Integral windup as institutional memory.** Past failures accumulate as "we let weird shit grow once, never again." This is metaphor on metaphor — the sim might produce equivalent behavior through accumulated state, but the "institutional memory" framing does not carry theoretical commitment.
- **Sensor fusion from bad instruments.** The system combines who's saying it, what genre it resembles, what clusters nearby, whether institutions dislike it, whether embarrassing people agree. True as inventory; not a sharp pathology claim distinct from the core substitution mechanism.

The split matters because the paper should not pretend all items are on the same theoretical footing. The first four are what the sim should demonstrate and the theorems should cover. The second three are prose tools for making the mechanism legible to readers without over-committing.

## Scope, before the example

**This paper's mechanism applies to informal discourse regulators** — academics, journalists, ad-hoc moderators, professional pundits, coalition enforcers, influential posters — where no formal sensor on $T$ (object-level claim quality) exists. Formal platform moderation with explicit policy revisions and dedicated fact-checking apparatus is a *different object*: those systems do update their rhetoric (often badly), they have explicit policy documents that can be revised in response to errors, and they have their own well-studied pathologies in the existing literature (platform governance, content-moderation trade-offs, algorithmic amplification). The present paper does not claim to cover them.

The reason the scope matters: without this conditioning, the example below reads as anti-tech polemic on one side or a defense of conspiracist epistemics on the other. Both readings are wrong. The paper is about what happens to sincere informal regulators who have no real-time $T$-sensor; it is not a critique of any particular platform policy or any particular political coalition.

## Worked example: local data center opposition

The example is chatty's from the seed conversation; reproduced here so the note carries its own concrete grounding. Read under the scope conditioning above: this is informal discourse at the county / regional / local-coalition level, not a formal platform-moderation case.

A county learns a large data center is coming in with tax abatements, heavy power demand, opaque procurement, and possible strain on water or grid infrastructure.

A local critic posts about sweetheart deals, infrastructure burden, contract secrecy, surveillance-contract adjacency, long-term public cost vs private gain. Some of it is documentable; some is speculative. Nearby posters add "they're hiding the real purpose," "this is AI mind control," "they're poisoning the aquifer on purpose," and generic 5G/UFO sludge.

### What the control system says it is regulating ($V$)

Truth, epistemic hygiene, anti-conspiracist discipline, keeping bad claims from spreading.

### What it can actually observe quickly ($Y_t$, which loads on $V'$)

Whether the topic is attracting cranks; whether the rhetoric resembles prior contamination genres; whether embarrassing people are piling in; whether engaging creates coalition or reputational risk; whether the discourse smells like "just asking questions."

### What happens next

Journalists, academics, posters, moderators cannot quickly resolve: true infrastructure burden, real subsidy structure, extent of institutional concealment, actual future harms. But they can quickly observe that the topic is getting weird, the discourse is aesthetically contaminated, continued engagement carries reputational cost.

Control action fires: dismissive framing, "this is how 5G/UFO nonsense starts," policing "just asking questions" as such, treating continued curiosity as epistemic defect, steering everyone away rather than separating claims within the discourse.

The system is no longer regulating for "truth about the project." It is regulating for distance from contamination, reputational safety, coalition legibility, avoidance of inferential slippage. **The rhetoric stays fixed** — people still say they are protecting truth, reason, and anti-bullshit norms — but the operational target has switched.

### Why this example works

Because the object-level question never got cleanly answered. The system did *not* establish that the project is benign, the harms are fake, the contracts fine, the concerns unfounded. It established that the topic is risky to entertain in an undifferentiated public way, that the social cost of granular inspection is too high, that topic suppression is safer than claim separation. That's the mechanism, visible in outcome.

The example is ugly in exactly the right way: there are plenty of real object-level concerns, it also attracts spectacle and paranoia, institutions have incentives to bullshit, coalition actors are terrified of being seen as adjacent to woo. Concrete without being cartoonish.

## Sim results: single-agent minimum-viable (2026-04-22)

Built at `~/git/lean/paper25_substitution.py`. Correctly-specified Kalman-LQR, two-latent state $(T_{dev}, C)$, cost function $E[q_T T_{dev}^2 + q_C C^2 + \lambda U^2]$ with $q_C = 0$ — the "rhetoric stays fixed on $V$" axiom is baked in at the cost function, not smuggled in through controller misspecification. Process dynamics: $T$ random walk, $C$ AR(1) with Poisson crank shocks. Observation $Y_t = \alpha_T T_t + \alpha_C C_t + v_t$. Control affects both latents, asymmetrically: $b_C = -1.0$, $b_T = -0.05$.

**What ran.**

- *Phase-transition sweep.* $\alpha_T / \alpha_C$ varied from 0.01 to 10, $\alpha_C$ held at 1. Five seeds per ratio, 3000 steps each, burn-in 500.
- *Counterfactual.* Same run with an added clean-T observation channel ($y_2 = T + \text{low noise}$). Controller's cost, LQR gains, and dynamics all unchanged — only the sensor geometry differs. Policy divergence between asymmetric-Y and clean-sensor runs quantifies substitution magnitude.

**Headline: substitution magnitude scales as a power law in observability ratio.** $T_{rms}^{asym} / T_{rms}^{clean}$ drops from ~333 at $\alpha_T/\alpha_C = 0.01$ to ~1.9 at $\alpha_T/\alpha_C = 10$, roughly $(\alpha_T/\alpha_C)^{-0.75}$. No sharp threshold; a continuous gradient that never fully recovers within the tested range. The "sincere controller fails structurally" language is earned: same cost function, same model, same gains, same dynamics, only the sensor changes, and the tracking-error ratio spans two orders of magnitude.

**Second diagnostic: effort without effect.** $|U|_{asym} > |U|_{clean}$ at every ratio tested. At $\alpha_T/\alpha_C = 0.05$: $|U|$ asymmetric = 0.20, clean-sensor = 0.09, $T_{rms}$ asymmetric = 6.8, clean = 0.04. The asymmetric controller is doing more than twice the work for ~180× worse tracking. The effort is not wasted — it is going into $C$-suppression (mean $|C|$ is in fact lower in the asymmetric run by a small amount), with the controller's subjective report remaining "I am regulating $T$." This is the rhetorical payload of the paper stated in two numbers.

**Mechanism confirmation.** LQR gain is $[-2.92, 0]$ across the whole sweep — the controller puts zero weight on $C$ in its cost function, as the $q_C = 0$ axiom requires. The substitution runs entirely through the Kalman filter: $\hat T$ is pulled around by $C$ because $Y = \alpha_T T + \alpha_C C$ and $\alpha_C$ dominates. LQR responds to its (contaminated) $\hat T$. Control output lands via $B = [b_T, b_C]^T$ with $|b_C| = 20|b_T|$, so the same $U$ mostly suppresses $C$. The subjective report stays fixed on $T$ because the cost function does; the objective controlled variable is $C$ because that is where the posterior signal lives. No misspecification required, no wrong beliefs, no corrupted intent — filter geometry alone forces the substitution.

**Unexpected: shock-statistics mismatch is a second substitution channel.** Even at $\alpha_T/\alpha_C = 10$, $T_{rms}^{asym}/T_{rms}^{clean} \approx 1.9$, not unity. The remaining gap comes from the filter's Gaussian model being blindsided by Poisson crank shocks on $C$. A unit-amplitude shock ten times the one-step $C$-sigma arrives instantaneously; the filter, expecting smooth Gaussian $C$-innovations, misattributes part of the resulting $Y$-jump to $T$. That drives $\hat T$ up, LQR applies $U$, and the substitution cascade fires — even though $\alpha_T$ is large enough that the smooth-$C$ component would be well-separated. This widens the necessity claim: substitution is forced not only by observation-weight asymmetry ($\alpha_T \ll \alpha_C$) but by any systematic mismatch between the filter's assumed state statistics and the real ones on a channel coupled to $Y_t$. Promoted to an instantiable pathology in §6 above.

**What the sim has not yet done.**

- *Compound-regime multi-agent sim.* Deferred as a persuasion artifact rather than a decision prerequisite. The homogeneous-agent sibling-vs-§N adjudication is earned by algebra (§"Paper 24 sibling status" below); the sim would confirm the algebra ($1/\sqrt{N}$ variance scaling with unchanged observability direction) but does not discover anything new. If later needed for readers, keep brutally minimal: shared global asymmetry, independent noise, identity witness inclusion, simple aggregation.
- *Heterogeneous-agent extension.* Separate object: what cohort-witness composition (different $C_{obs}^{(i)}$ across agents) restores $T$-observability? Belongs to a Paper 24/25 follow-on, not this paper.
- *Hysteresis / asymmetric suspect-status thresholds.* Elaborative, not scope-deciding. Not yet encoded.

### Paper 23 §3.3 bridge: observability-Gramian geometry (added 2026-04-22)

Operationalized. Computed $O_T = [C_{obs};\, C_{obs} A;\, \ldots;\, C_{obs} A^{T-1}]$ at horizon $T = 20$ across the $\alpha_T/\alpha_C$ sweep, tracked the T-axis observability $e_T^\top W_o\, e_T$ and the alignment of the least-observable direction $v_{\min}$ with the T-axis:

| $\alpha_T/\alpha_C$ | $\sigma_{\min}(O_T)$ | $e_T^\top W_o e_T$ | $|\langle v_{\min}, e_T\rangle|$ | $T_{rms}^{asym}/T_{rms}^{clean}$ |
|---:|---:|---:|---:|---:|
| 0.01 | 0.0226 | 0.002 | **0.9999** | 333 |
| 0.05 | 0.1127 | 0.050 | 0.9964 | 175 |
| 0.20 | 0.4278 | 0.80 | 0.9435 | 57 |
| 0.50 | 0.8364 | 5.0 | 0.7145 | 25 |
| 1.00 | 1.0499 | 20.0 | 0.4215 | 13 |
| 2.00 | 1.1248 | 80.0 | 0.2178 | 7.2 |
| 10.0 | 1.1509 | 2000 | **0.0439** | 1.9 |

The T-axis literally rotates into and out of the observability null-space as $\alpha_T/\alpha_C$ varies. At small $\alpha_T$, the least-observable direction $v_{\min}$ is essentially the T-axis itself (alignment ≈ 1); at large $\alpha_T$, $v_{\min}$ has rotated away (alignment ≈ 0) and the ill-conditioned direction is now the C-axis (via the $\rho_C^k$ geometric decay).

This is the flatter bridge: Paper 23 §3.3 case (ii) is the case where $\text{Im}(B) \cap \ker(O_T) \neq \{0\}$ (invisible interventions); Paper 25 is the case where the cost-targeted state direction lies near $\ker(O_T)$ (uncontrollable-via-observation). Both papers invoke the same geometric object — $\ker(O_T)$ or its near-kernel — and use it to state distinct closed-loop consequences. The "Paper 25 is the closed-loop dual of Paper 23 §3.3" framing was rhetorical rather than mathematical; the operational statement is *"both papers instantiate distinct consequences of the same observability-null-space geometry"*. Theorem shape within reach: *under an LTI system whose cost is concentrated on a state direction $q$ aligned with $v_{\min}(O_T)$, the steady-state substitution index grows as a monotone function of $|\langle v_{\min}, q\rangle|$ and the ill-conditioning of $O_T$ along $q$, independently of controller sincerity or model correctness.*

The headline shape — power-law substitution scaling plus a second channel via shock-model mismatch — is clean enough that Paper 25 has started paying rent. Promotion to preprint still blocked on the compound-regime test and the literature differential. The single-agent theorem of shape *"under ill-conditioned finite-horizon observability Gramian, LQR with cost on the ill-conditioned state direction structurally substitutes regardless of sincere intent"* is within reach.

## Three-test gate for promotion to preprint

Paralleling Paper 24's gate, with content specific to this object:

1. **Toy sim produces a regime where the target-drift gap opens and stays open** — i.e., the controller's action correlates with $R_t$-minimization and decorrelates with $T_t$-minimization, while the nominal objective function stays written on $T_t$. Not just transient; a stable regime. *Cleared 2026-04-22.* Single-agent sim shows power-law substitution magnitude across two decades of $\alpha_T/\alpha_C$ under correctly-specified Kalman-LQR with $q_C = 0$; effort-without-effect signature confirmed; shock-statistics mismatch surfaced as a second substitution channel; Paper 23 §3.3 observability-Gramian bridge operationalized. The scope-decision sub-claim (substitution survives Paper 24's clean-aggregation-open-witness fix) is earned by the homogeneous-agent algebraic argument in the sibling-status section below — heterogeneous-agent extension deferred as a separate object.
2. **One sharp claim beyond mood.** The paper-line sentence above is the candidate; needs to survive pressure-testing against adjacent cases.
3. **Adjacent-literature differential survives cold read.** The specific cut — *observability-driven target substitution, with rhetoric staying fixed on the nominal objective* — is not cleanly covered by performative prediction (Perdomo et al.), closed-loop recommenders (Sprenger et al.), feedback-loop classification (Pagan et al.), moderation trade-offs (Dwork et al.), or opinion-dynamics-under-control. If any of those already formalize the target-substitution mechanism, this folds into that literature rather than standing as a new object.

**Fourth test (framework-side, pass/fail):** the claim must be **necessity-framed**, not possibility-framed. The strong version is *"the controller MUST substitute $V'$ for $V$ when no real-time $T$-sensor exists, regardless of sincere intent"* — structural force. The weak version is *"regulators CAN be corrupted by their metrics"* — Goodhart, possibility, contingent. If the strongest defensible form of the paper's central claim is the weak version, the paper isn't earned. If the strongest defensible form is the strong version — sincere regulators facing the same sensor set produce the same substitution — then there is a theorem to prove. This is the pass/fail framework-side gate.

## Paper 24 sibling status (revisited)

**Adjudication: sibling, by algebraic argument (2026-04-22).** The compound-regime question — does target substitution survive Paper 24's clean-aggregation-open-witness fix? — admits a cleaner answer at the level of observability geometry than a sim would produce. The proposition below earns sibling status in principle; the multi-agent sim is a persuasion artifact if needed later, not a decision prerequisite.

**Proposition (homogeneous-agent sibling case).** Let $N$ homogeneous agents observe the same latent state $x_t = [T_t, C_t]^\top$ through a common measurement map $C_{obs} = [\alpha_T,\ \alpha_C]$ with independent additive noise: $y_{i,t} = C_{obs} x_t + v_{i,t}$, $i = 1, \ldots, N$. Stack the observations as $\bar y_t = \bar C x_t + \bar v_t$ with $\bar C = \mathbf{1}_N \otimes C_{obs}$. Then:

- The stacked finite-horizon observability matrix $O_T^{stack} = \mathbf{1}_N \otimes O_T$, where $O_T$ is the single-agent observability matrix of §"Paper 23 §3.3 bridge" above. Consequently $\ker(O_T^{stack}) = \ker(O_T)$.
- The least-observable direction is unchanged: $v_{\min}(O_T^{stack}) = v_{\min}(O_T)$ (it is merely scaled).
- The stacked-observation Kalman filter has posterior variance $O(\sigma^2/N)$ — aggregation improves SNR — but the *direction* of residual uncertainty is unchanged.
- The LQR gain depends only on $(A, B, Q, R)$ and is identical to the single-agent case. The policy $u = -K_{lqr} \hat x$ uses the aggregated posterior $\hat x$ whose T-axis component is still dominated by filter-leakage from $C$, now at variance $\sigma^2/N$ rather than $\sigma^2$.

**Therefore:** Paper 24's clean aggregation (shape-preserving, open witness inclusion) reduces observation noise but *does not rotate the observability subspace*. The substitution magnitude scales as $O(1/\sqrt{N})$ of the single-agent case but its direction and its structural origin are unchanged. Paper 24's sufficient condition for freeze-freedom is not sufficient for substitution-freedom. The mechanisms are independent. **Paper 25 is a sibling, not §N.**

**The core line**, in one sentence: *aggregation improves SNR; it does not rotate the observability subspace.*

**Scope condition for this argument.** Homogeneity of the measurement map across agents is load-bearing. Heterogeneous agents with genuinely different measurement maps $C_{obs}^{(i)}$ — for instance, a privileged witness with access to $T$ through a different channel than the rest of the cohort — *can* rotate the effective observability subspace, and the sibling claim does not apply to that case without further argument. The heterogeneous-agents extension is a Paper 24/25 follow-on object (what cohort-witness composition restores $T$-observability?), not part of the sibling-vs-§N decision.

**Why this earns it without a sim.** The claim is structural, not empirical. A multi-agent Kalman-LQR sim would confirm the algebra, not discover anything new — it would show posterior variance scaling as $1/N$ while the least-observable-direction alignment with the T-axis stays at its single-agent value. Confirmation, not adjudication. If the paper needs the plot for persuasion against a skeptical reader, it can be built later using the shared global-asymmetry / independent-noise / identity-witness-inclusion shape described above, brutally minimal. Until there is a reader to persuade, the algebra is the artifact.

**Supplementary arguments for sibling:**

- The substitution mechanism is structurally distinct from freeze. Freezing $V$ ≠ replacing $V$.
- The worked example (informal discourse moderation) lives at a different scale with different actors than Paper 24's organizational governance case.
- The necessity-framed paper-line (sincere regulators with the same sensor set produce the same substitution) does not follow from Paper 24's machinery.

**Supplementary arguments for extension:**

- Both are instances of "controller under partial observability optimizes what it can sense."
- Paper 24's multi-agent machinery covers much of the formal setup.

**Defer the decision** until the compound-regime sim runs. Either outcome is fine; the machinery doesn't care which title it ends up under.

## Adjacent literature (from chatty's pass)

- **Perdomo et al. (2020), *Performative Prediction*.** Models change the environment they react to. Captures "Goodhart-shaped" loops but does not center rhetoric-stays-fixed objective substitution.
- **Pagan et al. (2023), *A Classification of Feedback Loops in Automated Decision-Making Systems*.** Dynamical-systems taxonomy of feedback loops. Covers the zoology but does not isolate observability-driven target substitution as a named failure.
- **Sprenger et al. (2024), *Recommender Systems as Closed-Loop Control*.** Directly control-theoretic framing, but for the recommender/user loop, not for discourse moderation.
- **Dwork et al., moderation / community-formation theoretical models.** Existing, adjacent, but not centered on the target-substitution cut.

The novelty candidate is the *specific synthesis*: not "feedback loops exist," not "recommenders are control loops," but "discourse moderation as a controller that nominally regulates truth and actually regulates reputational contamination under observability asymmetry, with the objective substitution invisible because the rhetoric doesn't update." That may or may not survive a proper lit review. Not yet earned.

## Substrate connections

- **Paper 23 §3.3 case (ii) — the closed-loop dual.** This is the structural connection, not a resonance. Paper 23's §3.3 case (ii) (measurement null-space masking) says: a compensator $H_t$ acting in the measurement map's null space is observationally invisible to first order over horizon $T$. The present paper is the **closed-loop dynamical dual**: a controller operating in a regime where its nominal objective $T_t$ lies in the null-space of its available sensor $Y_t$ will *structurally* optimize the wrong thing, not as an error but as an architectural consequence. The identifiability defect Paper 23 formalizes at the identity-axis manifests here at the action-axis — whatever the controller cannot observe about $T$, it cannot optimize for. This paper inherits Paper 23's formal apparatus (the finite-horizon observability matrix, the null-space construction) rather than reconstructing it, and its theorem statements should cite §3.3 case (ii) directly as the identity-axis progenitor of the action-axis claim.
- **Governor / admissibility.** Admissibility gates as refusing to collapse $T_t$ and $R_t$ into a single $Y_t$ — keeping separate accounting for object-level claim quality, reputational risk, institutional opacity, and contamination state. Receipt-lineage as the architectural enforcement that these states cannot be silently unified. Governor's contribution here is specifically the infrastructure that refuses the substitution: separate sensor channels, separate admissibility accounting, separate update rules for each latent.
- **Latent Capitalism.** The data center example is Latent-Capitalism-adjacent: opaque procurement, captured tax abatements, infrastructure burden shifted onto public commons. The objective-aliasing mechanism is one way enclosure sustains itself against scrutiny — make the scrutiny itself reputationally contaminated, so the regulator switches from regulating enclosure to regulating the discourse about enclosure. The rhetoric of "truth-tracking" continues; the controlled variable is now reputational contamination.

## Open / deferred

- **Sim build.** *Single-agent minimum-viable done 2026-04-22* at `~/git/lean/paper25_substitution.py` — see §"Sim results" above. Next sim work is the Paper 23 observability-Gramian bridge (compute $\sigma_{\min}(O_T)$ across the sweep; connect to the near-kernel geometry the paper inherits from Paper 23's apparatus), followed by the compound-regime multi-agent sim (Paper 24's clean-aggregation-open-witness scaffold with observability asymmetry added). Hysteresis / asymmetric-threshold pathology is elaborative, not scope-deciding — sim that last.
- **Full lit review.** Needed before committing to Paper 25 status. Should include: epistemic network effects, social epistemology of moderation, Goodhart variants, credibility-weighting schemes, misinformation-diffusion models. Chatty's pass is a first-pass spike, not a finished review.
- **Substack vs preprint.** This concept is particularly well-suited to Substack essay form — the data center example carries a lot of the work, and the target-substitution claim lands in prose without needing formalism for lay readers. Could land as essay first, paper second if the three-test gate clears.
- **ICU contrast case.** Paper 23's deferred ICU case may apply here too — a domain where target-substitution is especially stark and ethical stakes are high. Worth noting as a possible sibling example if the paper goes long.
- **Note:** the compound-regime question (does Paper 24's freeze stack independently with this paper's substitution?) has been moved out of open/deferred and promoted to the decisive argument in the Paper 24 sibling-status section above. That's where the sim has to land a specific configuration to answer the scope question.
