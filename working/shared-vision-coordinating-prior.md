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

## Related artifacts

- Sim: `/home/jbeck/git/lean/shared_vision.py` (scaffold alongside `ops_continuity.py`)
- Paper 23 connection: §3 masking theorem generalizes to shared priors; §1 two-axis carve generalizes to (coordination-gain, truth-tracking)
- Governor connection: receipt lineage over $V_t$ updates = admissibility for shared-prior authoring

## Open / deferred

- **Scalar vs. vector $V_t$.** Scalar is the cleanest toy; vector is where the alias-compatibility claim gets interesting (agents can align on some components and diverge on others).
- **Whether the governance layer wants its own paper eventually** (Paper 25?) or stays folded in.
- **Empirical calibration.** The regimes are recognizable ("cargo-cult ideology" in particular is a common organizational pattern) but operationalizing them with real measurements is a later-paper problem, probably a case-study companion.
- **Relationship to DeepSeek's brittleness spiral (from the Paper 23 pass).** Masked compensator → org overestimates robustness → cuts margin. That's a specific instance of the coordination-gain-exceeds-truth-tracking failure applied to the ops layer; it might be an appendix in whichever paper of the two it lands in.
