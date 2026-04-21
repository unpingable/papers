# Epistemic Border Control as Proxy Regulation Under Partial Observability

*Working note — 2026-04-21. Bucket: **model-seed with paper potential.** Paper 25 candidate or possibly §N case-study extension of Paper 24, to be decided after the three-test gate clears. Not promoted until the gate clears.*

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

- **Control-target substitution (the headline).** The controller optimizes $V'$ (reputational containment) instead of $V$ (truth-tracking) whenever $Y_t$ loads on $V'$ and not on $V$. Necessity-framed, not possibility-framed.
- **High gain / overshoot.** When $K$ is large relative to the signal-to-noise ratio on $Y_t$, weak contamination signals produce disproportionate suppression action. Classic proportional-controller instability — a sim should reproduce this with standard parameters.
- **Hysteresis.** Threshold asymmetry in topic-classification: the threshold to enter "suspect" status is lower than the threshold to leave. Directly analogous to Paper 23's §2.1 handoff reset structure, and formally instantiable as a state-dependent discrete variable.

**Illustrative analogies (useful in prose, no theoretical commitment):**

- **Lag compensation on the wrong signal.** The loop reacts to the *last* epistemic disaster; post-anti-vax, post-QAnon, it sees everything through yesterday's transfer function. Evocative framing, not a formally distinct pathology from integral memory.
- **Integral windup as institutional memory.** Past failures accumulate as "we let weird shit grow once, never again." This is metaphor on metaphor — the sim might produce equivalent behavior through accumulated state, but the "institutional memory" framing does not carry theoretical commitment.
- **Sensor fusion from bad instruments.** The system combines who's saying it, what genre it resembles, what clusters nearby, whether institutions dislike it, whether embarrassing people agree. True as inventory; not a sharp pathology claim distinct from the core substitution mechanism.

The split matters because the paper should not pretend all six items are on the same theoretical footing. The first three are what the sim should demonstrate and the theorems should cover. The second three are prose tools for making the mechanism legible to readers without over-committing.

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

## Sim sketch (for when / if the toy gets built)

Not building this tonight. If built in the `shared_vision.py` / `ops_continuity.py` tradition, the shape would be:

- **Latent state.** $T_t$ evolving slowly (e.g., $T_{t+1} = T_t + \text{slow drift}$), with institutional-opacity scalar $I_t$ hiding a fraction from observation.
- **Contamination state.** $C_t$ growing as rhetorical markers accumulate, with crank-adjacency events modeled as discrete shocks that raise $C_t$ instantaneously.
- **Reputational risk.** $R_t$ as a function of $C_t$ and coalition signals (who's in the discourse).
- **Observation.** $Y_t = \alpha_C C_t + \alpha_R R_t + \alpha_T T_t + \text{noise}$, with $\alpha_C, \alpha_R \gg \alpha_T$ and higher noise on the $T_t$ channel.
- **Controller.** $U_t = K \hat{Y}_t + \text{integral memory term}$ — proportional-plus-integral on the observed signal, not on latent truth.
- **Diagnostic: target-drift gap.** Track the divergence between what the controller *thinks* it's regulating (its nominal objective) and what it is *actually* minimizing. Compute this as the difference between the control action's correlation with $T_t$-deviation versus its correlation with $R_t$-deviation over a window. The headline visualization would be a time-series plot showing the two correlations decoupling as $C_t$ rises.
- **Regimes to expect.**
  - *Nominal regime:* low $C_t$, $Y_t$ tracks $T_t$ reasonably, system behaves as advertised.
  - *Substitution regime:* high $C_t$, $Y_t$ decouples from $T_t$, controller optimizes $R_t$ while rhetoric stays fixed on $T$. This is the headline regime, not a "drift" — $V'$ replaces $V$ at every $t$ once the observability condition bites, not slowly over time.
  - *Hysteretic regime:* transient contamination event, system overshoots into $R_t$-regulation and stays there even after $C_t$ decays.
  - *Reputational-equilibrium lock-in:* structurally analogous to the bias-cancellation lock-in in Paper 24 — $R_t$ regulation converges to a stable point that is provably not optimal for $T_t$.

## Three-test gate for promotion to preprint

Paralleling Paper 24's gate, with content specific to this object:

1. **Toy sim produces a regime where the target-drift gap opens and stays open** — i.e., the controller's action correlates with $R_t$-minimization and decorrelates with $T_t$-minimization, while the nominal objective function stays written on $T_t$. Not just transient; a stable regime.
2. **One sharp claim beyond mood.** The paper-line sentence above is the candidate; needs to survive pressure-testing against adjacent cases.
3. **Adjacent-literature differential survives cold read.** The specific cut — *observability-driven target substitution, with rhetoric staying fixed on the nominal objective* — is not cleanly covered by performative prediction (Perdomo et al.), closed-loop recommenders (Sprenger et al.), feedback-loop classification (Pagan et al.), moderation trade-offs (Dwork et al.), or opinion-dynamics-under-control. If any of those already formalize the target-substitution mechanism, this folds into that literature rather than standing as a new object.

**Fourth test (framework-side, pass/fail):** the claim must be **necessity-framed**, not possibility-framed. The strong version is *"the controller MUST substitute $V'$ for $V$ when no real-time $T$-sensor exists, regardless of sincere intent"* — structural force. The weak version is *"regulators CAN be corrupted by their metrics"* — Goodhart, possibility, contingent. If the strongest defensible form of the paper's central claim is the weak version, the paper isn't earned. If the strongest defensible form is the strong version — sincere regulators facing the same sensor set produce the same substitution — then there is a theorem to prove. This is the pass/fail framework-side gate.

## Paper 24 sibling status (revisited)

Open question: is this Paper 25, or is it §N of Paper 24?

**Decisive argument (promoted from "curiosity at the bottom" to lead): the compound-regime case.** If a discourse community exhibits *both* Paper 24's mechanisms (aggregation-masking freeze + witness-filter) *and* this paper's mechanism (objective-aliasing substitution) *simultaneously and independently*, then the two failures stack: $V$ is frozen against updates AND silently replaced by $V'$, at the same time. If the sim shows that you can take a system with clean aggregation + open witness inclusion (Paper 24's sufficient condition) and *still* observe target substitution because $Y_t$ structurally underdetermines $T_t$ regardless of how you aggregate, then the cases are **independent**, and sibling status is correct. Paper 24's fix does not address Paper 25's failure. Conversely, if the substitution always rides on aggregation failure — if shape-preserving aggregation with open witnesses always recovers $T$-tracking — then this is §N of Paper 24.

This is what the sim has to decide. Framed this way, the three-test-gate item 1 becomes specifically: *build Paper 24's clean-aggregation-open-witness sim configuration, then add the observability asymmetry, then show substitution still occurs*. That is a clean experimental design, not just "does the toy produce regimes."

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

- **Sim build.** Deferred. Gate item 1 is "toy produces distinct regimes"; no need to build it tonight.
- **Full lit review.** Needed before committing to Paper 25 status. Should include: epistemic network effects, social epistemology of moderation, Goodhart variants, credibility-weighting schemes, misinformation-diffusion models. Chatty's pass is a first-pass spike, not a finished review.
- **Substack vs preprint.** This concept is particularly well-suited to Substack essay form — the data center example carries a lot of the work, and the target-substitution claim lands in prose without needing formalism for lay readers. Could land as essay first, paper second if the three-test gate clears.
- **ICU contrast case.** Paper 23's deferred ICU case may apply here too — a domain where target-substitution is especially stark and ethical stakes are high. Worth noting as a possible sibling example if the paper goes long.
- **Note:** the compound-regime question (does Paper 24's freeze stack independently with this paper's substitution?) has been moved out of open/deferred and promoted to the decisive argument in the Paper 24 sibling-status section above. That's where the sim has to land a specific configuration to answer the scope question.
