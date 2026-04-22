# Shared Vision as Coordinating Prior

*Working note — 2026-04-21. Bucket: **model-seed with paper potential.** Exploratory model first, candidate Paper 24 second. Not promoted to preprint until the three-test gate (below) clears.*

## Core claim

Shared vision is often a cheap, public surrogate for actual composition resolution. It works by reducing policy divergence across agents, but it can stabilize *coordinated wrongness* when the surrogate drifts away from reality. The failure mode is not "people believed a false thing." It is **the coordination gain exceeded the truth-tracking gain.**

## Minimal dynamic toy model

One plant, $n$ agents, one shared vision.

$$x_{t+1} = f(x_t, a^1_t, \dots, a^n_t, w_t)$$
$$y^i_t = h_i(x_t, v^i_t) = x_t + b_i + v^i_t$$
$$a^i_t = \pi_i(y^i_t, V_t; \theta_i) = -k_i (y^i_t - V_t)$$
$$V_{t+1} = V_t + \eta \,\Phi(E_t)$$

Each agent mixes three losses: local cost $L_i$, system cost $L_{\text{sys}}$, and deviation penalty $C_i(a^i_t, V_t)$ from the shared vision, with weights $\alpha_i, \beta_i, \gamma_i$.

Two-team reduction (simplest pressure-chamber instance): $n=2$, scalar $x_t$, biases $b_1 \neq b_2$, shared scalar $V_t$, $V_{t+1} = V_t + \eta(x_t - V_t)$.

## Three proposed regimes

- **Fragmented realism** — low $\gamma_i$, weak shared vision. Agents act on local truth fragments. Coordination is poor. Cold wars, duplicated work, dropped balls.
- **Useful fiction** — moderate $\gamma_i$, moderate $\eta$. Shared vision is not perfectly true but is stable enough to coordinate and plastic enough to update. Sweet spot.
- **Cargo-cult ideology** — high $\gamma_i$, low $\eta$. Tight alignment to the public story, no error correction against reality. The manager's dream and the system's long-term problem.

Cursed result: a coherent wrong map can outperform fragmented local maps on $L_{\text{sys}}$, because the coordination gain exceeds the truth-loss — until it doesn't.

## Distinctive move (vs. well-populated adjacent literature)

The adjacent territory (consensus algorithms, social choice, mechanism design, federated learning with regularization, multi-armed bandits with shared priors) already covers "agents coordinate around a shared signal." The distinctive move for Paper 24 — the one that earns it as a Δt object rather than a restatement — is this:

> **When two agents "align to $V_t$" but their internal representations of $V_t$ differ, the alignment is itself alias-compatible.** Public tokens match, internal compositions diverge, stress event exposes the gap.

This is Paper 23's §3 observational-masking theorem applied one scale up. Without that framing the model is mechanism design with better branding; with it, it's the multi-agent analogue of the controller non-self-identity problem.

## Two-axis carve (hypothesis)

Paper 23's carve (continuity of action, continuity of identity) probably generalizes:

- **Coordination-gain continuity** — can $V_t$ still reduce policy divergence in time? (Action-side analogue.)
- **Truth-tracking continuity** — can $V_t$ still resolve to the real plant state before error accumulates? (Identity-side analogue.)

Failure on axis 1 → fragmented realism. Failure on axis 2 → cargo-cult ideology. Success on both → useful fiction. If this carve holds, the Δt framework has a general two-axis pattern that applies at multiple scales: controller (Paper 23), shared prior (Paper 24), possibly others.

## Governance layer

The toy model treats $V_{t+1} = V_t + \eta \Phi(E_t)$ as an error-driven update. In real institutions, $V_t$ is authored, ratified, propagated, and defended by specific actors with specific standing. The governed form is

$$V_{t+1} = \mathcal{G}(V_t, \hat E_t, \mathcal{A}_t)$$

where $\mathcal{A}_t$ is the admissible authority / witness structure for changing the shared prior. This is where Governor's receipt-lineage and admissibility gates apply to shared-prior authoring — not just what $V_t$ does, but who is allowed to bind it and under what provenance.

Two separable problems, not collapsing them:

- **Binding problem** — who sets $V_t$, under what legitimacy, how updated? Governor / admissibility / receipt-lineage territory.
- **Dynamics problem** — once $V_t$ exists, when does it reduce divergence vs. produce ideology? Toy-model / simulation territory.

## Three-test gate for promotion to Paper 24

**Status: cleared 2026-04-21, with the mechanism turning out sharper than the original hypothesis. See "Mechanism earned" below.**

1. **Sim produces the three regimes as distinct phases** — fragmented / useful / cargo-cult actually show up, not just parameter tuning that labels itself.
2. **One sharp claim beyond mood** — candidate: *a partially false shared vision can outperform fragmented local accuracy until coordination gain is overtaken by reality error.* Or: *public alignment to $V_t$ is alias-compatible with diverged internal representations, and the divergence is observationally masked until a stress event.*
3. **Governance layer integrates cleanly** — not just who binds $V_t$ but the receipt-lineage structure that makes shared-prior updates admissible. Should connect to Governor without being a rebrand.

**Fourth test (framework-side):** the claim must be distinctively about alias-compatibility at the shared-prior level. If the final paper claim is statable in standard consensus / mechanism-design vocabulary without loss, Paper 24 isn't earned — it's consensus theory with new branding.

## Mechanism earned (2026-04-21)

All four gates cleared through the lock-in probe (`ops_continuity.py` companion run via `shared_vision.py`):

1. **Three regimes produced as distinct phases** ✓ (fragmented / useful fiction / cargo-cult, plus a fourth bias-cancellation quadrant now explainable rather than anomalous).
2. **Organizational alias-compatibility demonstrated** ✓. The `alias_compatibility_demo` produces action divergence of *algebraically zero* pre-shock regardless of the hidden interpretation spread $\varphi$, and divergence proportional to $\varphi \cdot \text{shock\_offset}$ post-shock. This is Paper 23's §3 case (i) masking exhibited one scale up: while $V_t \approx 0$ the public alignment layer cannot resolve the compositional divergence; under strategic shift the hidden spread surfaces proportionally.
3. **Governance changes outcomes substantively** ✓. Ungoverned USEFUL_FICTION flipped to CARGO_CULT_IDEOLOGY under naive witness-consensus governance; regime transitions are not subtle.
4. **Unexpected mechanism beats the original hypothesis** ✓ (the most important one).

**The mechanism, named:** **Mean-Aggregation Masking (bias-cancellation lock-in).**

Governance over coordinating priors via mean-error aggregation is *structurally incapable of responding to bias-split witnesses*. $V_t$ freezes not because the update rule refuses to act, but because the mean of sign-opposite errors is $\approx 0$ — the aggregator cannot distinguish "balanced disagreement" from "no error." Safety valves (unanimity, decay-thaw, dissent-override) do not rescue this, because the failure is not at the gate but at the aggregator. Dissent is arithmetically annihilated before it reaches the update rule.

The paper-grade claim, in its final scoped form:

> **Governance over coordinating priors via mean-error aggregation is structurally incapable of responding to bias-split witnesses. Naive governance rules do not just ratify early consensus — they silence post-consensus dissent by making disagreement look like no signal.**

Connection back to Paper 23: this is §3 masking one scale up *and one layer deeper*. Paper 23 names the measurement-and-authority map at the controller layer; Paper 24 names the aggregation map at the organizational layer. Both are primary real-time observation regimes that admit structural under-resolution.

## Sharpening pass — distributional shape (2026-04-21 evening)

One more layer surfaced through the multi-model polish pass: the mean-aggregation masking result is not really about governance *refusing* to act. It is about **aggregation collapsing the shape of disagreement into a summary that cannot distinguish "no signal" from "bimodal signal."** The aggregator treats:

- witnesses agreeing, error ≈ 0 (no update needed — correct), and
- witnesses bias-split, mean error ≈ 0 (needs update — incorrect),

as indistinguishable. The structure of the disagreement — bimodal, correlated, anticorrelated — is visible in the witness-by-witness reports and invisible in any mean-like summary.

Sharper form:

> **Mean aggregation destroys the information carried by disagreement shape.**

### Cohort witness, upgraded

This bridges into the Governor stack's cohort-witness principle. The standard reading of cohort witness ("no continuity-bearing thing should be raised in total private custody; multiple witnesses catch more errors") is a *redundancy* framing. The deeper reading is:

> **Cohort witness works not because of redundancy, but because it preserves distributional shape.**

What makes a cohort valuable is the pattern of disagreement across its members — that pattern is itself evidence about whether $V_t$ is serving as a coordinating prior for the witness population. If downstream governance collapses the cohort to any summary statistic (mean error, aggregate confidence, KPI), the shape information is discarded and the specific property the cohort provided is destroyed.

Governor's per-witness receipt architecture — each witness produces their own receipt with their own basis fields — is structurally compatible with distribution-sensitive aggregation. Dashboards and aggregate KPIs are not.

Specific prediction worth flagging: the more a "data-driven" organization relies on dashboards and aggregate KPIs for governance of $V_t$, the *more* susceptible it becomes to bias-cancellation lock-in, because the aggregators are structurally blind to bias-split witness populations. The pathology is not prevented by having more data; it is *produced* by the form in which the data is reduced.

### Paper-line candidate (save for writing pass)

> **Governance fails not only when it ignores dissent, but when its aggregation rule makes dissent look like no signal.**

### Scope caution

Not "all summaries are evil." The scoped claim: *when governance over coordinating priors relies on mean-like aggregation of witness error, bias-split populations can be rendered invisible at the aggregation layer, and the cohort witness that was supposed to catch this is defeated upstream by its own aggregator.* Strong enough.

## Paper 24 result stack (surface to depth)

1. **Shared vision as coordinating prior** — public token that reduces policy divergence at the multi-agent layer.
2. **Alias-compatible organizational agreement** — public alignment to $V_t$ compatible with diverged internal representations; stress exposes the gap.
3. **Mean-aggregation masking (bias-cancellation lock-in)** — governance via mean-error aggregation is structurally blind to bias-split witness populations.
4. **Cohort witness as distribution-shape preservation** — the epistemic value of cohort witness is not redundancy but preservation of disagreement structure; aggregation regimes that collapse to summaries destroy this value.

## Illustrative case studies (scoping discipline)

The bias-split-aggregation pathology applies across a specific class of governance regimes: those that rely on mean-like aggregation over shared coordinating priors. **Agile/Scrum is the sharpest worked example**, but the claim form that survives critique is scoped, not charged:

> *Managerial systems that rely on mean-like aggregation over shared coordinating priors are structurally vulnerable to bias-split witness pathologies, regardless of how participatory or data-driven they appear.*

Agile is a devastating case for a structural reason, not an ideological one. Its **stated** mechanism — responsive, adaptive, feedback-driven; rituals like retrospectives, standups, and reviews explicitly designed to surface team-level disagreement — is contradicted by its **enacted** aggregation layer: velocity, burndown, OKR attainment, roadmap confidence, all mean-like summaries that leadership consumes instead of the raw ritual output. Disagreement gets generated at the team layer and cancelled at the aggregation layer before reaching any governance process that could update $V_t$. The gap between stated mechanism and enacted mechanism is precisely where cargo-cult-ideology regime hides inside a methodology that explicitly claims to prevent it.

A broader hypothesis worth flagging but not defending in Paper 24: **Agile won not because it was the best coordination methodology but because it was the methodology most compatible with the legibility requirements of modern corporate governance** — it produced the summary statistics the dashboards needed. The relational substrate (team knowledge, divergent product models, actual disagreement about what "done" means) was illegible to that apparatus, so Agile's rituals were co-opted into generating the legible version while the illegible substrate ran underneath.

### Case-study discipline

Agile is *an illustration*, not the target. The paper's contribution is the mathematical framing. That framing applies across domains: SRE (already adjacent to Paper 23), Agile/Scrum, sabermetrics, hiring analytics, education metrics, criminal-justice risk assessment, military AI doctrine, dashboard-driven public health. **Pointing at one or two worked examples makes the abstract machinery legible; charging at any one of them invites dismissal.** The scoped version survives peer review; the "Agile considered harmful" version gets shouted down. First version first.

## The Paper 23 braid point (explicit)

> **Organizations mistake compressed public alignment for resolved internal composition.**

That's the single sentence that connects 23 and 24. Paper 23's §3 masking names the phenomenon at the controller layer; Paper 24 names it at the organizational layer and provides the specific mechanism (mean-aggregation masking) by which orgs fail to notice the aliasing *even when they nominally have feedback loops*. The two papers are distinct objects — the aggregation-layer mechanism is not derivable from Paper 23's controller-layer theorem — but they share a structural move and cross-cite naturally.

## Downstream destination

Paper 24 feeds into the **Latent Capitalism** volume as worked methodology for how enclosure mechanisms operate in specific organizational contexts: shared relational substrate enclosed by a measurement regime, rebranded as efficiency, actual function invisible to its own apparatus. The aggregation critique is the specific technical mechanism that makes enclosure self-stabilizing — the apparatus can't perceive what it's destroying because its own aggregators are structurally blind to the thing being enclosed. Flag this connection but do not develop it in Paper 24 itself; it belongs in the book.

## Publication gating

**The book/Substack hard-claim publication is blocked on Paper 24.** Specifically, the aggregation-layer piece has to land at theorem-level strength before the Latent Capitalism chapter (or any Substack piece that deploys the Agile / managerial-governance critique) can be published. Right now the aggregation-layer claim is a sim-demonstrated phenomenon scoped to mean aggregation — that's strong enough to name a mechanism but not strong enough to anchor a public argument about widely-deployed governance regimes.

**Concrete unblock criteria** (so the gate has named shape rather than being infinite):

1. **Median / variance-weighted aggregation probe runs.** Scopes the claim: either distribution-sensitive aggregators break the pathology (claim is "naive-mean aggregation under bias-split witnesses," with a constructive complement) or they don't (claim generalizes to a broader class, gets correspondingly nastier). Bounded: one extension to `shared_vision.py`, same shape as the unanimity / decay-thaw / dissent-override probe already done.

2. **Mean-aggregation masking at theorem level.** Not necessarily Lean-formalized, but a statable theorem with hypotheses (witness biases, aggregation rule form, update gate) and a conclusion (V-freeze under bias-split witnesses regardless of gate). Analogous to Paper 23 §3.3's Operational Masking Theorem but at the aggregation layer rather than the measurement-and-authority layer.

3. **Organizational alias-compatibility at theorem level.** Sufficient conditions under which public action-level alignment is compatible with internal compositional divergence ($\varphi$ spread in the current sim). Structurally parallel to Paper 23 §3.3 case (i), lifted one scale.

4. **Paper 24 as a preprint artifact.** v0.1 draft with metadata.yaml, README, NOTES, PDF — the same shape as Paper 23's preprint directory. The book can cite a DOI'd artifact; it cannot cite a working note.

Items 1–3 are the mathematical work; item 4 is the hardening. Together they are what "24 stronger" concretely means. Two specific claim fragments the hard-claim publication depends on:

- *disagreement shape collapsed into mean-like planning surfaces* — item 2.
- *public alignment masking internal divergence* — item 3.

Until both land at theorem level, the book/Substack deployment stays held. This is not scope inflation; it is the specific discipline that keeps the hard claim from being shouted down as overreach when it makes contact with the Agile / KPI / managerial-methodology world.

## Aggregation-boundary probe result (2026-04-21, late)

Probe ran. Four aggregation rules (MEAN, MEDIAN, MAX_ABS, VARIANCE_GATED) crossed with four 4-agent bias configurations. The pathology is **broader than mean aggregation**, and "use median" is not a fix.

| Aggregator | Balanced bias-split | Asymmetric population |
|---|---|---|
| MEAN | locked | locked |
| MEDIAN | **locked** | runaway |
| MAX_ABS | unlocked but unstable | runaway |
| VARIANCE_GATED | unlocked but unstable | runaway |

Two classes, both failing differently:

- **First-moment aggregators (MEAN, MEDIAN):** collapse to zero under balanced bias-split → V-freeze. The failure is not specifically mean; it is any aggregator whose value at a bias-split population is zero. Median locks in exactly when the split is symmetric in rank space, which is the typical bias-split case.
- **Shape-sensitive aggregators (MAX_ABS, VARIANCE_GATED):** escape the freeze by picking the loudest voice, but **destabilize** under asymmetric populations (the `three_vs_one` config drove V to ±12 within 100 steps). Fix one pathology, introduce another.

**Generalized theorem (informal, hardened form):**

> Any aggregator $\Phi$ satisfying $\Phi(E_t) = 0$ whenever $E_t$ is a balanced bias-split witness population produces V-freeze under such populations, regardless of procedural gate. This class includes mean, weighted mean (with balanced weights), and median. Shape-sensitive aggregators escape the freeze but introduce runaway under asymmetric populations. **No scalar aggregator is both freeze-free and stable** under the class of bias-split witness populations.

**Constructive conclusion (the architectural punchline):**

> The only aggregation class that is both shape-sensitive and population-stable is one that refuses to aggregate at all — preserving per-witness reports (receipts) for downstream interpretation rather than collapsing to a summary. Governor's receipt-lineage architecture is not one possible remedy among many; it is the specific architectural answer the formal analysis forces.

This tightens the Paper 23 ↔ Paper 24 ↔ Governor braid. Cohort witness as distribution-shape preservation is no longer a suggestive rhyme — it is the *constructive* solution that the aggregation-boundary probe identifies. Any scalar collapse (dashboard, KPI, aggregate confidence score) introduces one of the two failure modes. Only per-witness preservation avoids both.

### Scope boundary, now settled

The claim class is:

- **mean-like first-moment collapse** (mean, weighted mean, median under balanced splits) → V-freeze under bias-split populations
- **shape-sensitive scalar aggregators** (max-abs, variance-gated) → freeze-free but unstable
- **non-aggregating / receipt-preserving architectures** → the only class that is both freeze-free and stable

The remaining probe deferred to Paper 24's writing pass: formalize the theorem statement and the "no stable scalar aggregator" corollary at proof level. That is the item-2 and item-3 gate work named in the publication gating section.

## Witness-filter extension (2026-04-21, very late)

Chris's Amazon example — engineer estimates halved ritually, late delivery blamed on engineer, "naysayer" label and stack-rank exit for anyone who names the cycle — forced a third mechanism layer the model did not capture.

**The three stacked pathology layers, now all named:**

1. **Aggregation-layer masking** (mean-like collapse of bias-split dissent) — this morning's finding.
2. **Shape-sensitivity failure** (non-mean scalar aggregators escape freeze but destabilize under asymmetric populations) — this evening's boundary-probe finding.
3. **Witness-filter failure** (aggregation operating on a pre-curated witness population cannot see what was filtered out) — Chris's contribution.

**Formal extension.** Let $F : (\text{agent}_i, V_t) \to \{0, 1\}$ be a witness-inclusion function that determines whether agent $i$'s error signal $e_i$ enters the aggregation. The current model implicitly assumes $F \equiv 1$ (all agents count). The extension allows $F$ to be correlated with $V_t$-alignment — specifically, $F(a_i, V_t) = 0$ whenever agent $i$'s dissent magnitude exceeds a threshold, or its alignment score falls below a threshold. Real institutional examples: stack ranking, performance-management filtering, "culture fit" selection, promotion-based witness curation, attrition of disaffected employees.

**Witness-filter theorem (informal).** If $F$ is correlated with $V_t$-alignment in the direction of removing dissenters, then the surviving witness population consists of agents whose error signals are small by construction (they survived the filter precisely because their errors were small). The aggregate error $\Phi(E_t^{\text{filtered}}) \approx 0$ regardless of the true plant-versus-$V_t$ divergence. No aggregation rule — including shape-preserving receipt-lineage architectures — can produce $V_t$-correcting updates from a pre-aligned witness population, because the signal required to correct $V_t$ was filtered out before aggregation. V-freeze is enforced *upstream* of the aggregator.

*Proof sketch.* Suppose $V_t$ has drifted from the true optimum by $\Delta$. The witnesses whose error reports would push $V_t$ by $\Delta$ are precisely those with errors of magnitude $\geq \Delta$. If $F$ filters on $|e_i| < \tau$ for some $\tau < \Delta$, those witnesses are excluded by construction. The remaining witnesses have $|e_i| < \tau < \Delta$, so their aggregate error is bounded above by $\tau$, and V updates (if at all) by $O(\eta \tau)$ per step, which is insufficient to close the gap $\Delta$. The gap is structurally unfixable without either (a) reducing $\tau$ (loosening the filter, which defeats its purpose from the governance perspective) or (b) an exogenous change to $V_t$ itself. ∎

**Architectural implication, upgraded.**

> **Receipt-lineage / cohort-witness architecture is necessary but not sufficient. The sufficient condition for escape from V-freeze requires both:**
>
> **(a) the aggregator preserves distributional shape (no first-moment collapse), AND**
>
> **(b) witness inclusion is independent of $V_t$-alignment (no dissent-filtering via stack rank, culture fit, performance management correlated with compliance).**
>
> **Violating either condition permits V-freeze regardless of the other. Receipt-lineage without open witness inclusion is defeated by curation; open witness inclusion without receipt-lineage is defeated by aggregation. Both together are the minimal sufficient governance architecture.**

**Why this matters for the hard claim.** The Agile/KPI critique by itself is vulnerable to the response *"we just need better aggregation."* The witness-filter theorem closes that escape: better aggregation cannot save a governance regime that filters its witness population. Stack ranking, performance management, "culture fit" hiring, and promotion criteria that reward alignment with $V_t$ are not independent organizational practices from the aggregation problem — they are the mechanism that ensures aggregation cannot catch the pathology even if it were improved. Chris's Amazon ritual is the textbook case: the halving ritual produces late delivery, the late delivery is blamed on the engineer, and the stack-rank removes anyone who names the cycle. The witness population is continuously curated to only include agents who will participate in the fiction. *No aggregation rule can rescue this* — the solution has to address witness inclusion upstream.

## Publication gating, updated

Item 5 added to the unblock criteria: **witness-filter extension formalized.** Equivalent to items 2 and 3 in structural weight — this is a new mechanism layer, not a refinement. The hard claim (book/Substack) is blocked on this because the real-world organizational examples readers will bring (Amazon stack rank, dissent-suppressing performance management, "nay-sayer" culture filters) are direct instances of the witness-filter pathology. Without formalizing it, Paper 24's constructive conclusion has an exploitable gap.

### Filter probe result (2026-04-21, closing closing)

Thin-slice probe ran with permanent-filter (stack-rank) semantics: population of 3 aligned witnesses + 1 dissenter; filter removes any agent whose $|e_i|$ exceeds threshold at any step; filtered agents continue acting on the plant but their signal no longer reaches the V-update.

| Aggregation rule | Filter | V_final | \|plant error\| | Inclusion |
|---|---|---|---|---|
| MEAN | open | 0.05 | 0.80 | 1.00 |
| MEAN | \|e\|>0.8 removed | −5.96 | **5.16** | 0.75 |
| MAX_ABS | open | 6.00 | 7.00 | 1.00 |
| MAX_ABS | \|e\|>0.8 removed | −5.96 | **5.16** | 0.75 |

Three things land:

1. **The filter increases plant error ~6× (0.80 → 5.16).** Witness inclusion is the bigger lever than aggregation-rule choice.
2. **With filter on, MEAN and MAX_ABS produce identical V trajectories** ($-5.96$, $5.16$). Once the dissenter is permanently removed, the surviving population is homogeneous and the aggregation rule collapses to meaninglessness — whatever distinguished MEAN from MAX_ABS in the aggregation-boundary probe becomes a distinction without a difference when all the remaining voices are saying the same thing by construction.
3. **This is the algebraic prediction confirmed.** The surviving witness population has $|e_i| < 0.8$ by construction, so any aggregator produces a signal bounded above by $0.8$ per step, which over $T$ steps drives V in the aligned-population's biased direction rather than toward the true target. Chris's Amazon example is this exact dynamic, with *stack rank* playing the role of the filter threshold.

4. **Temporal asymmetry: one purge is enough.** The dissenter was removed *in step 0* and the drift ran for the subsequent 100 steps without any continued filtering. The filter does not need to remain continuously active; a single filtering event at the start produces persistent drift. This is a separate prediction from "filter defeats aggregation" and is structurally distinct — findings 1–3 are static claims about the filter-aggregation relationship, whereas this is a temporal claim about what the filter's effects do over time. Promoted to its own named proto-theorem below.

### Proto-theorem candidate: Persistence of dissident-filter effects

Based on the filter probe result and on the analysis surfacing through the multi-model riff:

> **A single dissident-removal event at $t = 0$ produces persistent non-vanishing error between $V_t$ and reality, bounded by the surviving population's bias magnitude relative to the removed dissenters. The error stabilizes at a finite value rather than growing, but cannot self-correct in the absence of either (a) re-introduction of non-aligned witnesses or (b) exogenous perturbation of $V$.**

(Intentionally narrower than an earlier draft formulation that claimed "unbounded drift" — the sim shows bounded persistent error, and the stable-incorrect-equilibrium framing is sharper than divergence. Divergence would require additional model assumptions, e.g., continuous exogenous plant drift or independently-moving ground truth.)

*Proof sketch.* Let the surviving population have mean bias $\bar{b}$ relative to the removed dissenter(s). Aligned agents produce observations $y_i = x + b_i$ and apply control proportional to $y_i - V$. As V drifts under the aligned signal, the plant equilibrates at $x \approx V - \bar{b}$. At that point each surviving agent's observation matches their target ($y_i = V$), their error signal vanishes, and V stops updating. The system has found a fixed point in which plant error equals $|\bar{b}|$, which is positive by the filter's selection criterion. No internal mechanism can reduce this error further because no witness is reporting it. ∎

### Downstream implications (prose-level, not theorem-level)

The temporal-persistence result has four implications that deserve explicit prose in the paper, because they turn the result from "describes a pathology" into "predicts specific failure signatures that observers can diagnose in the field":

- **Ghost-filter pathology.** Organizations can exhibit reality-tracking failure with no currently-visible filtering mechanism. The filter operated during a founding purge, a merger, a leadership transition, a methodology rollout, an original hiring-criteria choice. After that, the population is self-sustaining: new members are vetted against the already-curated $V$, and anyone who drifts surfaces as a dissenter and gets filtered as they surface their drift. The *maintenance* filtering rate is low (rarely needs to fire), so the filter looks absent. "We don't stack-rank" is not a defense; the filter could have been anything, at any time, and the population has been running on its output ever since.
- **The "we got more efficient" illusion.** Filtered organizations often report operational improvement after a purge because the friction of disagreement is gone. Meetings go faster; consensus is easier; execution feels smoother. What's actually happening: the dissenters who would have forced $V$ to engage with reality are gone, so the remaining population can drift freely. The efficiency gain is the absence of the reality-correction mechanism, which feels like improvement until the accumulated drift produces a catastrophic reality collision. *From inside the filtered equilibrium, the drift phase feels good.*
- **Remediation requires active reintroduction, not mere cessation.** Findings 1–3 suggest "stop filtering" as the intervention. The temporal-persistence theorem says stopping isn't enough — a filter-free regime starting from a filtered population will continue to drift in the filtered direction, because homogeneous witnesses do not carry the signal needed to correct $V$. Remediation requires *deliberate incorporation of outside witnesses* (hiring against the current $V$, adversarial external review, explicit dissent mandates) — not just "we stopped stack-ranking."
- **Chronopolitics temporal-capture connection.** Dissident filtering is a *temporal weapon*. A purge at $t=0$ produces a population that behaves a specific way at $t=100$ without continued intervention. Temporal capture at the governance layer does not require ongoing active capture; it requires *one successful capture event* that locks the evaluation apparatus into a drifted state, after which the apparatus sustains itself. That is cheaper and more durable than continuous capture, which is probably why it is a preferred mechanism of institutional takeover. This ties the Paper 24 machinery directly to the Chronopolitics volume's temporal-capture thesis and to the Latent Capitalism enclosure-via-one-shot-intervention pattern.

These four don't need to be theorems. They are the *practical payoffs* of the temporal-persistence theorem for real institutional analysis — the reason a proof-level statement is worth writing out, rather than the proof itself.

The probe closes the formal loop: Paper 24's constructive conclusion ("receipt-lineage / cohort-witness preservation is the architectural fix") is now *necessary but not sufficient* at proof level, and the "both (a) shape-preserving aggregation AND (b) open witness inclusion" sufficient condition is backed by a minimum-viable demonstration that either half alone fails.

## Theorems (hypothesis / conclusion formalization)

*First-pass consolidation, 2026-04-22. Each theorem restates and tightens a result derived above; the body's proof-sketch passages are the informal justification. Lean formalization is deferred — this is the statable-theorem gate (items 2, 3, 5 from the publication gating section).*

### Setting (shared across theorems)

Discrete-time system with $n$ agents, scalar plant state $x_t \in \mathbb{R}$, shared scalar coordinating prior $V_t \in \mathbb{R}$.

- **Plant:** $x_{t+1} = f(x_t, a^1_t, \dots, a^n_t, w_t)$, with $f$ linear-stable in the closed loop and $w_t$ a zero-mean disturbance.
- **Observation:** $y^i_t = x_t + b_i + v^i_t$, with bias $b_i$ fixed per agent and $v^i_t$ zero-mean noise.
- **Control:** $a^i_t = -k_i(y^i_t - V_t)$, with gain $k_i > 0$.
- **Prior update:** $V_{t+1} = V_t + \eta\,\Phi(E_t^F)$, where $E_t = (e^1_t, \dots, e^n_t)$ is the vector of witness errors $e^i_t = y^i_t - V_t$, $F : \text{Agent} \times \mathbb{R} \to \{0,1\}$ is a witness-inclusion function, $E_t^F$ is the restriction of $E_t$ to $\{i : F(i, V_t) = 1\}$, and $\Phi$ is a scalar aggregator. The unfiltered / open-witness case is $F \equiv 1$.

### Theorem 1 — Mean-Aggregation Masking (aggregation-layer freeze)

*Claim form: any first-moment aggregator is blind to balanced bias-split witness populations, producing V-freeze without any procedural refusal.*

**Hypotheses.**
- **(A1) Bias-split population.** The bias vector $(b_1, \dots, b_n)$ is balanced: $\sum_i b_i = 0$, with both signs represented non-trivially.
- **(A2) First-moment aggregator.** $\Phi$ satisfies $\Phi(E) = 0$ whenever the sign-weighted first moment of $E$ vanishes (includes mean, balanced weighted mean, median under rank-symmetric splits).
- **(A3) Open witnesses.** $F \equiv 1$.
- **(A4) Stationarity.** $w_t$ and $v^i_t$ are zero-mean.

**Conclusion.** $\mathbb{E}[V_{t+1} \mid V_t] = V_t$ for all $t$. In particular, if $V_t$ differs from the plant target by any $\Delta \neq 0$, the gap is not closed by internal dynamics. No procedural gate downstream of $\Phi$ (unanimity, decay-thaw, dissent-override) can rescue this, since the gate's input is $\approx 0$.

**Corollary (no-free-lunch for scalar aggregators).** There is no scalar $\Phi$ that is simultaneously (i) freeze-free on every balanced bias-split population and (ii) stable on every asymmetric population. Shape-sensitive aggregators (max-absolute, variance-gated) violate (A2) but produce unbounded-drift under asymmetric populations (confirmed empirically in the aggregation-boundary probe). The only escape class is non-aggregating — per-witness receipt preservation.

### Theorem 2 — Organizational Alias-Compatibility

*Claim form: public-alignment observables are alias-compatible with internal compositional divergence; the divergence surfaces only under strategic shift.*

Augment the setting with a per-agent internal interpretation $\varphi_i \in \mathbb{R}$, so the agent's effective target is $V_t + \varphi_i$: $a^i_t = -k_i(y^i_t - (V_t + \varphi_i))$. Let $\varphi = (\varphi_1, \dots, \varphi_n)$.

**Hypotheses.**
- **(B1) Stationary $V$.** $V_t$ held constant over the observation window.
- **(B2) Local equilibrium.** Each agent operates near its local steady state.
- **(B3) Public-alignment observable.** The alignment metric is action-level divergence $D(a^1_t, \dots, a^n_t)$ — e.g., variance or pairwise spread of actions.

**Conclusion.** $D$ is independent of $\varphi$ up to $O(\varepsilon)$ noise floor. That is, for any $\varphi, \varphi'$, the stationary distributions of $D$ coincide: $D \perp \varphi$ under (B1)–(B3). Under a strategic shift $V_t \to V_t + \Delta V$, the induced action divergence becomes $D = \Theta(\|\varphi\| \cdot |\Delta V|)$, surfacing the hidden spread proportionally.

**Corollary.** Public alignment to $V_t$ lies in the observational-masking regime of Paper 23 §3.3 case (i): the observable equivalence class $\{(\varphi, V) : D(\varphi, V) \leq \varepsilon\}$ contains both compositionally-aligned and compositionally-divergent members, distinguishable only by stress events.

### Theorem 3 — Witness-Filter (V-freeze upstream of aggregator)

*Claim form: if witness inclusion is correlated with $V_t$-alignment, no aggregator — including shape-preserving receipt-lineage architectures — can produce $V_t$-correcting updates. V-freeze is enforced upstream of $\Phi$.*

**Hypotheses.**
- **(C1) Alignment-correlated filter.** There exists $\tau > 0$ such that $F(i, V_t) = 0$ whenever $|e^i_t| \geq \tau$.
- **(C2) Non-vanishing gap.** The true plant-to-$V_t$ gap $\Delta$ satisfies $|\Delta| > \tau$.
- **(C3) Bounded aggregator.** $\Phi$ is 1-Lipschitz in each argument (standard: mean, median, weighted variants, max-abs, shape-preserving aggregators).

**Conclusion.** $|\Phi(E_t^F)| \leq \tau$ for all $t$ after the filter activates, so $|V_{t+1} - V_t| \leq \eta \tau$ per step. The gap $|\Delta|$ cannot be closed by internal dynamics alone: V-freeze persists upstream of $\Phi$.

**Corollary (necessary-but-not-sufficient architecture).** Shape-preserving aggregation (Theorem 1 Corollary) is *necessary but not sufficient* for reality-tracking governance of $V_t$. The sufficient condition is: **(a)** shape-preserving aggregation AND **(b)** witness inclusion independent of $V_t$-alignment. Violating either permits V-freeze regardless of the other.

### Theorem 4 — Persistence of Dissident-Filter Effects

*Claim form: a single filtering event at $t = 0$ produces persistent non-vanishing error between $V_t$ and reality, bounded below by the surviving population's residual bias, with no internal mechanism for self-correction.*

**Hypotheses.**
- **(D1) One-shot filter.** $F$ is applied at $t = 0$ only, removing all agents with $|b_i| \geq \tau$; thereafter $F \equiv 1$ on the surviving sub-population $S$.
- **(D2) Non-zero residual bias.** The surviving-population mean bias $\bar{b} = \frac{1}{|S|} \sum_{i \in S} b_i$ is non-zero (generic under asymmetric original bias distributions).
- **(D3) First-moment aggregator.** $\Phi$ satisfies $\Phi(E) = 0$ whenever $E$'s first moment over the included population vanishes (Theorem 1's (A2), restricted to $S$).
- **(D4) No exogenous $V$ perturbation.** $V_t$ evolves only via the aggregator update.
- **(D5) Plant-controller equilibration.** Under the surviving agents' control law, the plant state tends to $x_* = V_* - \bar{b}$ at any fixed $V_*$.

**Conclusion.** The system has a fixed point $(V_*, x_*)$ with $V_* - x_* = \bar{b}$. At this fixed point, $e^i = b_i - \bar{b}$, which has mean zero over $S$; hence $\Phi(E^F) = 0$ and $V$ stops updating. The plant-to-$V$ error $|V_* - x_*| = |\bar{b}|$ persists and cannot be reduced without (a) re-introducing agents with $|b_i| \geq \tau$ (exogenous witness addition) or (b) exogenous perturbation of $V$.

**Prose-level corollaries (paper §X, not theorem-grade).**
- **Ghost-filter.** The filter need not remain active; the drifted equilibrium is self-sustaining and looks filter-free from inside.
- **Efficiency illusion.** The drift phase is experienced as operational improvement (reduced dissent friction) until reality collision.
- **Active reintroduction.** Cessation of filtering is insufficient for remediation; deliberate incorporation of outside witnesses is required.
- **Temporal capture.** One filtering event produces durable capture — strictly cheaper than continuous intervention, and a Chronopolitics-grade temporal weapon.

### What "formalized at hypothesis/conclusion level" means here

Each theorem above has: a named setting, explicit hypotheses labeled (A1)–(D5), a single sharp conclusion, and a corollary or prose-level payoff. The informal proof-sketches in the body sections above stand as the justification pending either full Lean formalization or a refereed-paper proof appendix. The four statements are jointly what the book / Substack hard-claim publication can cite — the publication-gating items 2, 3, and 5 are now discharged at this level.

## Paper 24 §1 draft (cold-reader intro)

*Draft intended for readers with no prior exposure to Papers 22 / 23 or the Δt framework. Cross-refs to Paper 23 are marked as related work, not prerequisites.*

### 1. Introduction

Organizations routinely align on shared visions, strategic priors, or operating theses that turn out to be wrong. The standard accounts of this phenomenon are ideological ("leadership refused to listen"), sociological ("groupthink"), or procedural ("the feedback loops were broken"). Each names a real failure mode, and each is sometimes correct. This paper argues, however, that an important subset of coordinated-wrongness failures is *structural* in a sharper sense: they occur in organizations that have working feedback loops, that solicit dissent, and that update their shared prior in response to reported error. The failure does not happen in the reporting layer. It happens inside the aggregation layer, and it is invisible to the governance apparatus by construction.

We call the core pathology **mean-aggregation masking**, and we show that it is only the surface of a three-layer structural failure. The deeper layers are an alias-compatibility result — public alignment on a shared prior is indistinguishable from internally divergent interpretation under stationary conditions — and a *witness-filter* result in which compliance-correlated curation (stack ranking, performance management rewarding alignment, culture-fit hiring, attrition of disaffected members) defeats any aggregation rule, including correctly-designed shape-preserving ones, by removing signal before it reaches the aggregator. A fourth result establishes that these effects are temporally durable: a single filtering event produces persistent plant-to-prior error with no internal mechanism for self-correction.

The practical implication is sharp. Organizations that aggregate error reports via first-moment summaries — dashboards, velocity metrics, OKR attainment scores, roadmap-confidence aggregates, KPI-driven governance surfaces — are structurally vulnerable to coordinated wrongness that their own apparatus cannot detect, *even when those organizations participatorily invite dissent and ritualize feedback.* The aggregation layer, not the willingness-to-listen layer, is where the pathology lives.

### 1.1 The model in one paragraph

A plant $x_t$ is observed by $n$ agents, each with a fixed bias $b_i$ and noisy observation $y^i_t = x_t + b_i + v^i_t$. Agents act on the plant with control $a^i_t = -k_i(y^i_t - V_t)$, where $V_t$ is a shared coordinating prior — the "vision," the strategic thesis, the OKR target, the KPI goal. $V_t$ updates via $V_{t+1} = V_t + \eta\,\Phi(E_t)$, where $E_t$ is the vector of witness error signals $e^i_t = y^i_t - V_t$ and $\Phi$ is a scalar aggregator (mean, weighted mean, median, variance-gated, etc.). This is the minimal model of a multi-agent system that shares a prior and updates it via feedback. It is also, structurally, what most corporate-governance mechanisms look like when the ritual surface is peeled off: shared target, distributed observations, feedback update rule, aggregation at the top.

### 1.2 The four results, informally

**(T1) Mean-aggregation masking.** If the witness-bias distribution is balanced around zero (equal numbers of positively-biased and negatively-biased agents, or any population whose first moment of error vanishes), then every first-moment aggregator — mean, balanced weighted mean, median under rank-symmetric splits — maps the error vector to zero. The update rule consequently produces no motion in $V_t$, regardless of how large the underlying gap between $V_t$ and reality is. Safety valves attached downstream of the aggregator (unanimity thresholds, decay-thaw mechanisms, dissent-override provisions) cannot rescue this; their input is already ≈ 0. Dissent is not refused. It is arithmetically annihilated.

**(T2) Organizational alias-compatibility.** If each agent has an internal interpretation $\varphi_i$ of the shared prior — so that agent $i$'s effective target is $V_t + \varphi_i$ rather than $V_t$ — then action-level agreement across the cohort is independent of the $\varphi_i$ spread under stationary conditions. Public alignment on a shared vision is therefore *observationally indistinguishable* between cohesive and hiddenly-divergent populations. The spread surfaces only under strategic shift: a change of $\Delta V$ produces action divergence proportional to $\|\varphi\| \cdot |\Delta V|$, which is why organizations often discover their "aligned" team is not aligned precisely when a pivot, reorganization, or crisis forces the prior to move.

**(T3) Witness-filter defeats aggregation.** If the witness-inclusion rule is correlated with prior-alignment — i.e., agents whose reported error exceeds a compliance threshold are systematically excluded, whether by explicit stack-ranking, by performance-management systems that reward on-narrative contribution, by "culture fit" hiring, or by attrition of disaffected employees — then the surviving witness population has errors bounded above by the filter threshold by construction. No aggregator can produce corrective updates from such a population, because the corrective signal has been removed upstream of the aggregation rule. Receipt-lineage architectures, shape-preserving aggregators, and distribution-sensitive governance regimes are *necessary but not sufficient*: the sufficient condition requires both shape-preserving aggregation AND open witness inclusion.

**(T4) Temporal persistence.** A single dissident-removal event is enough. After one filtering event, the surviving population has non-zero mean bias $\bar{b}$, and the system equilibrates to a fixed point where plant-to-prior error is $|\bar{b}|$, all witnesses report zero error, and the aggregator has no signal to act on. The error is stable, not divergent. It cannot self-correct without re-introduction of non-aligned witnesses or an exogenous perturbation to $V$. A purge is cheaper and more durable than continuous capture: one successful filtering event at founding, at a merger, at a methodology rollout, at a leadership transition, produces durable governance drift that looks, from inside, like "we don't filter anymore."

### 1.3 What is distinctive

The adjacent literature is substantial. Consensus algorithms, social-choice theory, mechanism design, federated learning with regularization, and multi-armed bandits with shared priors all treat "agents coordinating around a shared signal" as a central object. The distinctive move here is to focus on a specific structural property that cuts across all of these: *the aggregator's inability to distinguish "no disagreement" from "balanced disagreement."* That distinction is the crux of the pathology. Mean aggregation destroys the information carried by the *shape* of disagreement. The cohort witness that was supposed to catch this is defeated not by malice or misprocedure but by the arithmetic of its own summary statistic.

The second distinctive move is to connect the aggregation-layer failure to witness curation, which forms a joint pathology that cannot be dissolved by fixing either layer alone. Papers that address the first without the second admit a "just use better aggregators" escape; papers that address the second without the first admit a "just use better hiring" escape. Both escapes are structurally closed here.

### 1.4 Paper roadmap

§2 develops the minimal dynamic model and the admissible-aggregator class. §3 proves the four theorems. §4 presents the aggregation-boundary probe (empirical demonstration that the no-free-lunch corollary of T1 is tight across the four canonical aggregator classes), the alias-compatibility demonstration, and the filter probe (empirical demonstration of T4's temporal persistence). §5 develops Agile/Scrum as the worked case study — chosen for the unusual legibility of the gap between its stated mechanism (retrospectives, adaptive replanning, feedback-driven ritual) and its enacted aggregation layer (velocity, burndown, OKR attainment, roadmap confidence). §6 discusses the constructive architectural implication — that the only aggregation class satisfying both freeze-freedom and stability refuses to aggregate at all, preserving per-witness receipts for downstream interpretation — and connects this to receipt-lineage architectures that have been proposed in adjacent work on AI agent governance. §7 addresses related work and adjacency. §8 discusses open problems: vector $V_t$, the governance binding problem (who authors $V_t$, not just how $V_t$ updates), and empirical calibration.

## Paper 24 §7 draft (related work / adjacency)

*Draft of the adjacency section. Purpose: locate the paper against neighboring literatures, mark what is shared and what is structurally distinct. Preempts the "isn't this just X with new branding?" response for each of the nearest X's.*

### 7. Related work

The paper's nearest neighbors span several disjoint literatures, none of which asks precisely the question addressed here but each of which owns some structural fragment of it. We name each, state what is shared, and state what is structurally different.

### 7.1 Distributed consensus and social choice

The distributed-systems consensus literature — Paxos (Lamport), Raft, and the broader Byzantine fault-tolerance family — treats "how does a distributed system agree on a value under failures" as its central question. The shared structural move with this paper is the presence of an aggregation or voting mechanism that reduces distributed observations to a common decision. The structural difference is that consensus protocols *assume* correct inputs, Byzantine inputs within a bounded fraction, or a known fault model; the pathology identified here is about correct procedure running on inputs whose distribution defeats the procedure's expressiveness. No Paxos-style protocol fails on balanced bias-split witnesses in the sense of Theorem 1, because Paxos is about value-selection, not value-correction. The aggregation-masking result is not a safety failure or a liveness failure in the consensus sense; it is an *observability* failure in a setting that uses consensus machinery as part of its governance stack.

Social-choice theory — Arrow's impossibility theorem (Arrow 1951), Gibbard-Satterthwaite (Gibbard 1973, Satterthwaite 1975), Condorcet paradoxes — is closer in flavor. Arrow proves that no aggregation rule over preference orderings satisfies a small axiom set; our Theorem 1 corollary ("no scalar aggregator is both freeze-free and stable under bias-split populations") is structurally similar in form — impossibility across a family — but operates on a different object. Arrow aggregates preferences (strategic, ordinal, action-shaping); Theorem 1 aggregates error signals (descriptive, cardinal, feedback-shaping). The social-choice results are about the *design* of aggregation rules under voter-behavior axioms; Theorem 1 is about the *observability* of a hidden system state under aggregator choice. They share the flavor of "impossibility across a class" but not the theorem. What is genuinely new is the link between this impossibility and dynamic system behavior: social-choice aggregation is typically one-shot, while our object is the closed-loop consequence of repeatedly applying a defective aggregation over time.

### 7.2 Federated learning, distributed estimation, and multi-agent bandits

Federated learning with shared priors or regularization (McMahan et al. 2017 and successors) is the nearest technical cousin. A central server aggregates gradient updates from distributed clients with heterogeneous data; the shared prior is the global model, the aggregator is typically FedAvg (mean) or a robust variant. The bias-split problem is a real open concern in this literature under the heading of "heterogeneous clients" or "non-IID data." The structural difference is that federated learning frames this as an *optimization* problem — find a better aggregation rule, a better regularizer, or better client-reweighting — whereas our Theorem 1 corollary says the problem has no solution within the scalar-aggregator class. Proposed fixes (FedProx, FedNova, personalized FL, clustered FL) are consistent with our result: each escapes mean-aggregation masking only by abandoning either the scalar-summary form or the assumption of a single shared prior. Our framing names the architectural conclusion federated-learning proposals increasingly reach without articulating the underlying impossibility: scalar summaries of heterogeneous populations are structurally blind in a way that no scalar fix can repair.

Multi-armed bandits with shared priors (Russo and Van Roy 2014, and successors in Bayesian exploration) and distributed estimation (Borkar 2008, Tsitsiklis 1984) treat related structural objects. Both share the minimal model of agents updating a common parameter on the basis of local observations. The structural difference is that both literatures model agents as *epistemic* units — attempting to learn the true parameter — rather than as *governed* units — aligning on a prior whose authority and update rules are institutionally determined. The witness-filter theorem (T3) has no analogue in these literatures because the witness inclusion is assumed.

### 7.3 Cybernetics and control-theoretic observability

Ashby's law of requisite variety (Ashby 1956) is the deepest structural cousin. Ashby's formulation — a regulator must match the variety of the regulated system — implies, in the aggregation setting, that a regulator with scalar output cannot regulate a system whose state has richer structure than a scalar. Theorem 1's corollary is essentially a specialization of requisite variety to a particular class of aggregators: first-moment scalar aggregators lack the variety to distinguish balanced bias-split populations from zero-error populations, and therefore cannot regulate the gap between the shared prior and the plant. Stafford Beer's Viable System Model (Beer 1972) takes this cybernetic insight to organizational design directly; the aggregation-masking result is compatible with Beer's work and can be read as a sharpening of *why* scalar management summaries fail in variety-rich organizations.

Control-theoretic observability (Kalman 1960) is another direct cousin. Observability asks when the internal state of a system can be reconstructed from its outputs over time; if the system is unobservable, no feedback controller can regulate it. The witness-filter theorem (T3) can be read as a statement about *induced* unobservability: the filter removes precisely the state components (agents whose error exceeds the threshold) that carry the information needed to reconstruct the plant-prior gap. The surviving system is, by construction, unobservable with respect to the signal the governance apparatus is attempting to regulate. Where standard observability analysis treats unobservability as a structural property of the plant, Theorem 3 identifies a class of governance choices that *produce* unobservability as a downstream consequence — a dynamic the control literature does not typically model because it assumes the observer is not adversarial to the measurement.

### 7.4 Organizational epistemology, groupthink, and the metrics critique

The groupthink literature (Janis 1972, Esser 1998) names many of the same empirical phenomena — organizations agreeing on wrong things, failure to surface dissent, after-the-fact recognition that warnings were given and ignored — but in social-psychological terms. Our framing is complementary rather than competitive: part of what looks like groupthink under the Janis framework is, mechanically, mean-aggregation masking and witness filtering. "Self-censorship" and "illusion of unanimity" are downstream effects of the aggregation layer producing no signal; the aggregation layer produces no signal because it is structurally blind to bias-split populations. The social-psychological and the mechanical explanations coexist: people do self-censor, *and* the aggregator would erase their dissent even if they did not.

The metrics-critique literature — Muller's *The Tyranny of Metrics* (Muller 2018), Goodhart's law, Campbell's law, and Deming's statistical process control critiques (Deming 1986) — is the practitioner-facing literature closest to the paper's implications. Muller catalogues cases in which metrics-driven governance produces pathological outcomes; Goodhart's law names the strategic-response mechanism (when a measure becomes a target, it ceases to be a good measure). Theorem 1 provides a specific structural account of *one mechanism* by which this happens: aggregated metrics are blind to bias-split witness populations, so an organization whose members produce genuinely informative but bias-split error signals will see "no disagreement" in the aggregate and "no need to correct" at the update rule. Theorem 3 provides the matching witness-filter mechanism. The metrics-critique literature documents the pathology; the theorems supply a class of mechanisms.

High-reliability-organizations work (Weick and Sutcliffe 2007, Roberts 1990) is an empirical cousin. The HRO literature identifies "deference to expertise" and "preoccupation with failure" as practices that maintain organizational attention on edge signals; in our framing, these practices are witness-inclusion-preserving interventions — they resist the drift toward alignment-correlated witness curation that Theorem 3 identifies as the upstream pathology. HRO practice and the constructive implication of our architecture (open witness inclusion plus shape-preserving aggregation) are structurally aligned, though the HRO literature does not state the formal impossibility that motivates them.

### 7.5 Wisdom of crowds and statistical aggregation

Galton's 1907 ox-weight experiment (Galton 1907) and its modern popularization as "wisdom of crowds" (Surowiecki 2004) establish the canonical case for aggregation: under independent errors with zero mean, the aggregate error shrinks as $1/\sqrt{n}$. The theorems in this paper can be read as identifying when this canonical case *fails*. Specifically: the conditions under which wisdom-of-crowds aggregation works (independent errors, zero-mean, non-filtered population) are precisely the conditions whose failure modes our theorems name. Balanced bias-split populations violate the independence assumption (Theorem 1); witness filtering violates the population assumption (Theorem 3). Wisdom-of-crowds is not wrong — it is narrow. The pathologies named here are what happens inside the regions of parameter space that wisdom-of-crowds implicitly excludes.

### 7.6 Controller-layer observational masking (Paper 23)

Paper 23 of the Δt framework series (Beck 2026a) proves a structurally parallel result at the controller layer: a non-self-identical controller — one whose internal composition changes across handoffs, fatigue cycles, or role transitions — can be observationally indistinguishable from a self-identical one under normal operation, with the divergence surfacing only under stress events that stress the controller's composition. The theorems here are the multi-agent analogue: a cohort whose internal $\varphi$-spread varies across members is observationally indistinguishable from a cohort with aligned $\varphi$ under stationary conditions, with the divergence surfacing only under strategic shift (Theorem 2).

The single-sentence braid point, stated explicitly for readers familiar with both: **organizations mistake compressed public alignment for resolved internal composition.** Paper 23's §3 masking theorem names the phenomenon at the controller layer; this paper names it at the organizational layer and supplies the specific aggregation-layer mechanism by which organizations fail to notice it even when they nominally have feedback loops. The two papers are distinct objects — the aggregation-layer mechanism is not derivable from Paper 23's controller-layer theorem — but they share a structural move and cross-cite naturally. Readers unfamiliar with Paper 23 do not need it to follow the present paper; readers familiar with Paper 23 will recognize the pattern immediately.

### 7.7 Receipt-lineage architectures and the constructive answer

The constructive architectural implication of Theorems 1 and 3 — that the only aggregation class satisfying both freeze-freedom and stability is one that refuses to aggregate at all, preserving per-witness receipts for downstream interpretation — connects to ongoing work on governance architectures for AI agent systems where receipt-based authority and per-action lineage are proposed as first-class primitives rather than implementation details (see, e.g., the agent-governor line of work). This paper's contribution to that literature is to identify the formal problem that such architectures solve: receipt-lineage is not one possible remedy among many, but the specific architectural answer the aggregation-boundary impossibility forces. Reciprocally, the witness-filter theorem (T3) identifies what receipt-lineage architectures *cannot* solve on their own: open witness inclusion must also be maintained, or the receipts produce no corrective signal because the signal has been curated upstream.

### 7.8 Downstream destinations (noted, not developed)

The theorems have implications for two downstream projects that are beyond the scope of this paper. The first is the application of the witness-filter and temporal-persistence results to organizational enclosure mechanisms — the pattern in which shared relational substrate is collapsed into a measurement regime whose aggregators are structurally blind to what they are enclosing. The second is the connection between Theorem 4 (a single filtering event produces durable drift without continued intervention) and what one might call temporal-capture dynamics — the class of institutional takeover mechanisms that rely on one-shot decisive events rather than continuous capture. Both extensions are flagged and not developed here.

## Related artifacts

- Sim: `/home/jbeck/git/lean/shared_vision.py` (scaffold alongside `ops_continuity.py`)
- Paper 23 connection: §3 masking theorem generalizes to shared priors; §1 two-axis carve generalizes to (coordination-gain, truth-tracking)
- Governor connection: receipt lineage over $V_t$ updates = admissibility for shared-prior authoring

## Open / deferred

- **Scalar vs. vector $V_t$.** Scalar is the cleanest toy; vector is where the alias-compatibility claim gets interesting (agents can align on some components and diverge on others).
- **Whether the governance layer wants its own paper eventually** (Paper 25?) or stays folded in.
- **Empirical calibration.** The regimes are recognizable ("cargo-cult ideology" in particular is a common organizational pattern) but operationalizing them with real measurements is a later-paper problem, probably a case-study companion.
- **Relationship to DeepSeek's brittleness spiral (from the Paper 23 pass).** Masked compensator → org overestimates robustness → cuts margin. That's a specific instance of the coordination-gain-exceeds-truth-tracking failure applied to the ops layer; it might be an appendix in whichever paper of the two it lands in.
