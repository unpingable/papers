# Premature Commitment, Belated Consequence, and the Empty Binding Window

*A Two-Curve Framework for Temporal Detachment in Bound Decisions*

**James Beck**
Independent Researcher
2026-05-04 — Draft v0.2

---

## Abstract

Many institutional failures are attributed to "slow process" or "execution shortfall." This paper argues that a structurally distinct class of failure — empty binding windows — is hidden inside that vocabulary. Plainly: an empty binding window exists when the system can only know enough to act after acting would no longer matter. We formalize the temporal seam as a two-curve model: admissibility maturity m(t), informally whether the system knows enough to bind, and consequence viability c(t), informally whether binding can still matter. The valid binding window W is the set of times on which both curves are above their thresholds. Three failure orientations follow: premature commitment binds while m has not matured; belated consequence binds after c has decayed; empty-window failure is the regime in which W is empty for all t. Distinguishing empty-window failure from ordinary process delay requires a discriminator: residual event-class mismatch. Closure requires changing the event class itself, not merely improving execution. Because the discrimination depends on what counts as feasible execution, we introduce a counterfactual regime selection rule and a subtype matrix that name which regime applies by default and what override burdens are required to deviate. Worked cases — generational climate harm, FDA pre-market approval, administrative-queue cascades, Sarbanes-Oxley and complex fraud, scientific pre-registration, platform-worker classification — demonstrate the framework across natural-latency, manufactured, and ontological sub-types. The result is sibling to spatial substitution failures (Paper 25 [8]) on a temporal axis, and orthogonal to the four-layer decomposition (Paper 22 [5]). The framework's central political move is making the regime choice explicit: the same case can classify differently under different counterfactuals, and naming the regime is part of what the framework lets a reader see clearly.

---

## 1. Introduction

A familiar pattern in institutional analysis: an outcome is bad; the inquiry ends with "the process took too long." The diagnostic stops there because process velocity is a legible parameter. If only it had moved faster, the harm would have been averted. Reform proceeds by adjusting throughput.

This paper argues that a meaningful subset of these failures are not process velocity failures at all. They are regimes in which there exists no time at which the action could be both legitimately bindable and consequentially viable — regardless of how fast the process moves. Plainly: the system can only know enough to act after acting would no longer matter. We call these *empty binding windows*. Naming them is necessary because the response strategy is qualitatively different: throughput improvement does not close an empty window; only changing what is being bound, by whom, under what authority, can.

The phenomenon has a temporal-detachment shape that pairs naturally with a spatial-detachment shape developed elsewhere. *Epistemic Border Control* (Paper 25 [8]) showed that systems may face spatial substitution under observability asymmetry — when a target variable is unsensed, regulation falls back on a measurable proxy whose closure relation to the target is not preserved (the proxy-substitution dynamic catalogued in the Goodhart-variants literature [25]). The present paper argues that a temporal sibling exists: when the time-axis evidence required for legitimate binding does not arrive before the consequence window closes, a similar substitution dynamic operates, with a similar fallback to whatever surrogate is available — speed, ceremony, retroactive blame, performance reassurance.

The paper makes four contributions:

1. A two-curve formalization of the temporal seam (§2) that distinguishes admissibility maturity from consequence viability and locates the binding window in their overlap.
2. A three-orientation taxonomy of binding failure (§3) that separates premature commitment, belated consequence, and empty-window failure as structurally distinct.
3. A discriminator (§4) — *residual event-class mismatch* — that distinguishes empty-window failure from ordinary process delay.
4. A counterfactual regime selection rule and subtype matrix (§5) that constrain how the discriminator is applied, with an enforcement layer that prevents framework-driven classification laundering.

Worked cases (§6) cover three of the four sub-types the matrix names — natural-latency, manufactured, and ontological. Relations to adjacent series results follow (§7). The framework is presented as a working draft: enough discrimination to classify a useful set of cases, with explicit limitations (§8) on what remains rough.

The argument is positive in form but negative in import. Like related results in *No Universal Plant Clock* (Paper 22 [5]) and *Epistemic Border Control* (Paper 25 [8]), it identifies a class of failures that admit no purely procedural fix. The framework's value is to make these failures visible to analytical vocabulary that currently absorbs them under the more comfortable label of "slow process."

---

## 2. Formal Setup

A *binding event* is the moment at which a decision moves from candidate to operative — when authority attaches the decision to a system, a person, or a state, and the system henceforth treats the decision as governing. Binding events are ubiquitous: regulatory approvals, judicial rulings, commercial contracts, administrative determinations, scientific consensus settlement, internal organizational decisions. They are points at which uncertainty terminates and downstream behavior is conditioned on the binding having occurred.

Companion analysis decomposes a binding event $B$ along several coordinates — object, evidence, authority, time, scope, durability — with a per-coordinate admissibility score and threshold; the present paper isolates the time coordinate and brackets the others.

On the time axis, two functions characterize the readiness state of the binding:

**Admissibility maturity** $m(t)$ — informally, *whether the system knows enough to bind.* The readiness to bind. Generally increasing: as evidence accumulates, deliberation completes, and standing clarifies, $m$ rises. Pre-binding activity (verification, review, deliberation, consultation) is the activity by which $m$ rises.

**Consequence viability** $c(t)$ — informally, *whether binding can still matter.* The capacity for binding to attach meaningful consequence. Generally decreasing: as assets move, memory fades, exposure windows close, statutes expire, plaintiff cohorts disperse, and political will degrades, $c$ falls. The consequence-viable window is the set of times when binding still produces effects worth producing.

The valid binding window $W$ is the set of times on which both curves are jointly above their thresholds:

$$W = \{ t \mid m(t) \geq \theta_m \ \land \ c(t) \geq \theta_c \}$$

A binding at time $t$ is valid only if $t \in W$. $W$ can be a proper interval, multiple disjoint intervals, or empty.

A schematic picture of the four cases the framework distinguishes:

```
Time →                                      θ = threshold

(a) Normal overlap          m(t) _____/--------         W non-empty;
                            c(t) --------\_____         binding within W
                                  [ ─── W ─── ]

(b) Premature commitment    m(t) ___/-------            bind at t with
    (Type A)                c(t) ------\____            m(t) < θ_m
                                ↑bind here

(c) Belated consequence     m(t) _____/-------          bind at t with
    (Type B)                c(t) ------\______          c(t) < θ_c
                                              ↑bind here

(d) Empty window            m(t) ____________/---       m crosses θ_m
    (Type C)                c(t) ------\___________     only after c
                                                        falls below θ_c;
                                                        W = ∅
```

We disambiguate two binding events that the temporal model places on the same axis:

- **Action binding** at $t_\text{action}$: the decision is committed; resources are allocated; the system is reconfigured around it.
- **Consequence binding** at $t_\text{consequence}$: the decision's effects attach to the responsible parties — recovery, accountability, learning, course correction.

These are distinct events. Conflating them is a common source of analytical error. The three failure orientations of the next section are defined on these two event labels.

---

## 3. Three Failure Orientations

The two-curve model exposes three structurally distinct failure modes, each defined by which of the two binding events occurs outside W. We label them as follows, and use the labels as shorthand throughout §6:

- **Type A — premature commitment.** Binding occurs at $t$ with $m(t) < \theta_m$.
- **Type B — belated consequence.** Binding occurs at $t$ with $c(t) < \theta_c$.
- **Type C — empty-window failure.** $W = \emptyset$ over the relevant span; no $t$ satisfies both threshold conditions.

### 3.1 Premature commitment

The action binding occurs at $t_\text{action}$ with $m(t_\text{action}) < \theta_m$. The decision is taken before the evidence, deliberation, or standing necessary for legitimate commitment has matured. *Cybernetic Fault Domains* (Paper 15 [3]) develops this side as cybernetic premature convergence; *Premature Remediation* (Paper 19 [4]) characterizes a related failure. Common forms: commit before quorum; deploy before validation; regulate before causal model; irreversible action before review.

The corrective response is to extend deliberation, defer action, raise the admissibility threshold, or build reversible intermediate states. These are throughput-decreasing, latency-increasing measures.

### 3.2 Belated consequence

The consequence binding occurs at $t_\text{consequence}$ with $c(t_\text{consequence}) < \theta_c$. By the time accountability, recovery, or course-correction can attach, the consequence-viable window has decayed. *Toward a Second Law for Organizations* (Paper 2 [1]) characterizes this for the long-Δt compliance/reputation lag; *Unauthorized Durability* (Paper 18 [2]) formalizes the hysteretic lock-in version. Common forms: damages awarded after the firm dissolves; retraction issued after the citation cascade; regulatory action after harm has propagated; ratchet deepening past the point of recovery.

The corrective response is to preserve consequence viability — accelerate consequence binding, maintain assets in escrow, hold recovery infrastructure available, prevent dispersal. These are throughput-increasing or preservation measures.

### 3.3 Empty-window failure

$W$ is empty for all $t$ in the relevant span. There is no time at which both $m \geq \theta_m$ and $c \geq \theta_c$ hold. Neither premature commitment nor belated consequence is *the failure* — both are forced by the geometry. If the system commits before $m$ matures, the commitment is premature; if it waits, $c$ decays before $m$ arrives.

This is the structural failure. It is qualitatively distinct from the first two because no operating-point adjustment within the existing curves can produce a valid binding. Closure requires changing what is being bound, not how the existing binding is timed.

The premature/belated pair is a duality on the same axis. The empty-window failure is the third orientation: the regime in which the duality has no resolution.

---

## 4. Empty-Window Discriminator

The empty-window failure is the contribution this paper exists to name. Its theoretical importance depends on a discriminator that distinguishes it from ordinary belated-process failure — a slow institution that could close the gap with throughput improvement.

Without a discriminator, the framework collapses into "every slow institution is an empty-window failure" and ceases to mean anything specific. We develop the discriminator in two iterations.

### 4.1 Initial four-condition test

A candidate empty-window case satisfies all four:

1. Binding has consequence only before some time $t_c$.
2. Binding becomes admissible only after some time $t_m$.
3. $t_m > t_c$ (the windows do not overlap on this case).
4. Closing the relation requires changing the authority/process/event class, not merely improving execution.

The first three conditions are direct consequences of the formal setup. The fourth — the discriminator — does the work. Without it, every slow institution becomes an empty-window example, since any system can be characterized as having "windows that fail to overlap" when described loosely enough.

### 4.2 Compression: residual event-class mismatch

The fourth condition admits two readings that produce different classifications. One reading treats "improving execution" as a binary: any execution improvement that closes the gap moves the case to belated-process; only cases where no execution improvement is possible qualify as empty-window. This reading misclassifies cases like FDA pre-market approval, where some of the gap is closable by execution improvement (better trial design, faster surveillance) and some is structural to the binding event (population-scale safety profiles cannot be characterized in less time than population exposure provides).

The compressed form of condition #4:

> **Residual event-class mismatch.** Within the specified counterfactual regime, the residual gap that survives feasible execution improvement (intake, automation, staffing, portal integration, surveillance throughput) is closable only by changing authority structure, entitlement definition, burden of proof, consequence timing, or event class.

The compression does three things. First, it reframes the discriminator as residual rather than total — what survives execution improvement, not whether any execution improvement is possible. Second, it names a counterfactual regime as part of the test specification, eliminating the smuggled counterfactual that the original #4 contained. Third, it provides an open list of what counts as event-class change (authority structure, entitlement definition, burden of proof, consequence timing, or event class itself) so that "execution improvement" is operationally distinguishable.

### 4.3 Why residual matters

The residual framing captures a property of empty-window failure that prose tends to blur: the gap between "approved for use" and "characterized at population scale" in pharmaceutical regulation, the gap between "claim filed" and "claim adjudicated" in administrative law, the gap between "harm occurred" and "harm legally recognized" in algorithmic discrimination — none are pure execution failures, and none are pure event-class failures. Each contains both, and the residual after maximum feasible execution improvement is the part that earns the empty-window classification.

A purely execution-framed analysis leaves the residual invisible. A purely event-class-framed analysis dismisses cases that have any execution-tractable component. The residual framing splits the difference and makes the structural part of the gap analytically visible.

---

## 5. Counterfactual Regime Selection

The compressed #4 is regime-relative: "within the specified counterfactual regime." Without specifying which regime, the discriminator does not classify; it permits multiple classifications. The selection rule pins this down.

### 5.1 Two regimes

We distinguish two counterfactual regimes within which feasibility can be evaluated.

**Status-quo regime.** Feasible execution improvement is bounded by *political durability*. What counts as feasible is what would be deployable under prevailing institutional incentives, accounting for opposition reconstitution. This includes process tuning within current authority structure, workflow redesign without legislative change, tool deployment within existing oversight frameworks, and reform measures politically durable in the relevant jurisdiction's recent history. It excludes reforms attempted and reconstituted (e.g., work requirements substituted for streamlined eligibility), reforms exceeding prevailing political acceptability, and reforms requiring legislative change against entrenched opposition.

**Any-feasible-configuration.** Feasible execution improvement is bounded by *physical, technological, and economic possibility*. What counts as feasible is what is within demonstrated technological capability and physical/economic constraints, regardless of political durability. It includes the status-quo set plus reforms requiring legislative change in counterfactual political configurations. It excludes reforms that violate physical causality (faster epidemiology than cohort accumulation can produce) or definitional constraints (event class doesn't yet exist).

The two regimes ask different questions. Status-quo asks: under prevailing political pressure, is the gap closable? Any-feasible asks: under any feasible configuration, is the gap structurally closable at all? Both are legitimate; they answer different questions. The framework's discipline is requiring case-authors to declare which question they are answering.

### 5.2 Selection rule

> A case must declare the regime under which condition #4 is evaluated. The default regime follows the claimed sub-type. Natural-latency and ontological cases default to any-feasible-configuration; procedural and manufactured cases default to the prevailing authority/incentive regime. Overrides are allowed only when the case explains why the default regime misstates the source of the residual gap.

### 5.3 Subtype matrix

We classify candidate empty-window cases into four sub-types, each with its default regime and override burden:

| Claimed sub-type | Default regime | Feasible execution improvement | Override burden |
|---|---|---|---|
| Natural-latency | Any feasible configuration | Measurement, modeling, early warning, faster response | Show the latency is institutionally produced, not physical/causal |
| Procedural | Prevailing authority/incentive regime | Staffing, intake, automation, portal integration, queue redesign | Show reforms are predictably reconstituted by the regime |
| Manufactured | Prevailing authority/incentive regime | Procedural improvements plus anti-gatekeeping reforms attempted in the jurisdiction | Show the delay is not reproduced by interested authority |
| Ontological | Any feasible configuration | Better detection, classification, review, documentation | Show the missing event class already exists and only execution lags |

The third column gives per-subtype shorthand for what counts as feasible execution improvement; ambiguous cases route back to the foundational regime definitions in §5.1.

To make the override-burden language concrete: an author overriding a *procedural* default to manufactured must show not merely that reforms have been slow or contested but that they are *predictably reconstituted* — for example, that streamlined-eligibility measures, where enacted, are reliably replaced with work requirements or integrity audits that restore the original burden, or that §404 controls, where enacted, are reliably eroded by carve-outs that recreate the pre-reform exposure. The bar is a pattern of reform-and-recapture, not a single contested decision.

The ontological override burden carries a separate clarification: "exists" must mean *codified-and-operative-as-binding-event*, not merely conceived or proposed. Without this disambiguation, contested cases (where reform is in motion but not complete) admit both ontological and manufactured classifications depending on the reader's preferred framing. The companion framing is that closure of an ontological case requires *making a new binding event operative*, not improving execution within the existing one. This prevents the any-feasible regime from accidentally swallowing event-class creation as ordinary execution improvement.

### 5.4 Anti-cosplay enforcement

The selection rule plus matrix can be regime-shopped if the sub-type claim itself is unconstrained. The framework prevents this through three layers.

First, the sub-type claim is itself accountable. An author cannot claim "natural-latency" to obtain the any-feasible default unless they can defend the case as physically/causally produced. The override burden in the rightmost column is the test the claim must survive — and the same defense applies in reverse if the author is *justifying* a sub-type claim that determines a favorable regime.

Second, the default regime locks once the sub-type is claimed. Sub-type determines regime; the author cannot pick sub-type based on which regime they prefer without paying the override burden.

Third, overrides carry a specific argumentative burden, not a general "I prefer this regime" license. The override-burden column names the move required. The case must argue, on its own facts, that the default regime misstates the source of the residual gap.

The mechanism is not airtight. A determined author can still cherry-pick by misclassifying the sub-type. But misclassification is now a falsifiable move (specific burden, specific case facts) rather than a hidden judgment call. The framework's job is not to make all judgment go away; it is to make the judgment visible enough to audit. Without this enforcement layer, the framework becomes bespoke classification laundering with better typography.

---

## 6. Worked Cases

We illustrate the framework through six cases (across five subsections) spanning three of the four sub-types — natural-latency, manufactured, and ontological. The procedural sub-type is named in the matrix but not exemplified here. Each case is presented in narrative form; per-case scoring scaffolds (m(t), c(t), threshold-by-threshold) appear in supplementary material.

### 6.1 Generational climate harm — natural-latency Type C

Consider a justiciable claim by individuals born 2050–2100 against firms emitting 1990–2030 for harm caused by sea-level rise, attributable extreme-weather mortality, or ecosystem collapse.

Admissibility maturity for individual-vs-individual binding requires population-scale attribution science to allocate harm shares to specific emitter cohorts (the developing field of climate event attribution [11], building on industrial-carbon-producer accounting [12]), a legal infrastructure recognizing intergenerational tort or its functional equivalent, and a plaintiff cohort that has actually been harmed (otherwise no standing — see *Juliana v. United States* [13] for the standing barrier in U.S. federal court). Earliest plausible $t_m$ is unlikely to precede mid-century for the 2050-cohort plaintiff class.

Consequence viability decays through corporate dissolution, asset dispersal, decision-maker mortality, and political-will erosion. For most 1990–2030 emitter / 2050-cohort claimant pairs, $c(t_\text{consequence})$ has plausibly decayed below threshold by $t_m$.

The case claims natural-latency. Default regime: any-feasible-configuration. Under this regime, no execution improvement (faster attribution science, more permissive standing rules, larger cohort studies) appears to close the multi-decade interval between emission and manifest harm. Closure plausibly requires changing the binding event class entirely — from individual tort against specific emitter to intergenerational trust, no-fault industrial-harm fund, or constitutional climate right.

The case satisfies all four conditions and the override burden does not apply (the latency is physical/causal). It is an empty-window failure under the natural-latency sub-type. The framework identifies a case that intuition assigns to the empty-window regime.

### 6.2 FDA pre-market approval — borderline residual case

The FDA's approval of a new chemical entity for a mass-market chronic-use indication is a binding event: agency certification licenses mass exposure.

Admissibility maturity for full safety profile — including rare adverse events, long-term effects, and interaction effects in real-world polypharmacy — requires post-market exposure data accumulated over years to decades. Phase III trials characterize neither rare events nor long-term effects.

Consequence viability for the approval decision attaches to two distinct populations: pre-exposure (consequence still preventable by withdrawal) and post-exposure (consequence already incurred; withdrawal does not undo exposure). For mass-market chronic-use drugs, the post-exposure population accumulates rapidly; the consequence-viable window for the original approval decision closes within a few years.

The case classification depends on which counterfactual regime applies. Reformers point to execution-improvement potential: larger trials, longer follow-up, active-rather-than-passive surveillance via systems such as FDA Sentinel [14], real-world-evidence platforms, AI-assisted signal detection. Skeptics point to a structural residual and to the political-economy of the approval process [15]: characterizing 20-year effects requires 20 years of exposure.

The compressed #4 splits the difference. The residual after feasible execution improvement is non-zero and structural to the binding event class — "approval as gatekeeping certification under uncertainty." Closing the residual requires changing the binding event class itself: from approval to conditional approval with mandatory long-term post-market study and pre-committed withdrawal triggers, or from agency certification to a different licensing regime entirely.

Under either regime, FDA pre-market approval for mass-market chronic-use drugs satisfies the compressed #4 once the residual is properly framed. The case is borderline because it has a substantial execution-tractable component; it earns Type C classification on the residual rather than the total gap.

### 6.3 Administrative-queue cascades and complex financial fraud — manufactured/status-quo fork

Two cases illustrate the manufactured sub-type and the regime-selection problem it surfaces.

**Administrative-queue cascade.** A claimant's binding to an entitlement program (food assistance, disability, housing assistance, prior-authorization care) under conditions where state administration controls eligibility verification through process design. Documentation collection, prior-authorization navigation, denial-and-appeal cycles, and cross-program coordination produce admissibility maturity timelines that, on the reading developed by Herd and Moynihan [16] under the rubric of administrative burden, exceed the consequence-viable window for the underlying need (food insecurity, housing loss, untreated illness, lost employment trajectory).

**Sarbanes-Oxley and complex fraud.** A binding of financial-reporting accuracy via audit attestation. For simple fraud, the post-SOX regime narrows the gap: §906 criminal-attestation requirements (18 U.S.C. §1350) plus §404 internal-controls reporting (15 U.S.C. §7262) [17] are widely understood to advance $t_m$ for many disclosure failures, though the empirical evidence on §404 specifically is mixed [18]. For complex fraud — off-balance-sheet structures, multi-jurisdiction shells, related-party concealment — the residual gap remains, and $t_m$ frequently exceeds $t_c$ (firm collapse precedes detection).

Both cases share a structural feature: classification depends on the chosen counterfactual regime.

Under any-feasible-configuration, both arguably classify as Type B (belated-process). For administrative-queue cascades, reform options with operational track records exist — single-portal applications, presumptive eligibility, automated cross-program checks — though their distributional effects under sustained political pressure are contested. For SOX/complex fraud, more radical reforms (public-utility auditors replacing the private big-four model, real-time SEC monitoring, mandatory beneficial-ownership registries) could plausibly narrow the gap. Closure is *in principle executable* under sufficient political will.

Under status-quo regime, both arguably classify as Type C (manufactured empty-window). Reform measures, where deployed against political opposition, are reconstituted as new gates: work requirements substituted for streamlined eligibility; integrity audits substituted for presumptive determination; legislative carve-outs (e.g., the JOBS Act of 2012's exemption of Emerging Growth Companies from §404(b)) peeling back parts of post-Enron controls.

On this reading the slowness is reproduced by interested parties; closure under prevailing political pressure requires changing the political-economic configuration that produces the renewal, not just deploying the next round of reform.

The fork is informative rather than defective. It is what makes the manufactured sub-type analytically distinct from procedural failure: same surface, different durability under political pressure. The framework's central political move is making the regime choice explicit. A claimant arguing for reform is properly served by the status-quo classification (the gap is reproduced by interested authority, and a one-shot reform will be undone). A regulator estimating the structural-impossibility upper bound is properly served by the any-feasible classification (some closure is achievable in principle). Both are legitimate; the discipline is naming which question is being answered.

### 6.4 Pre-registration in science — successful event-class repair

Pre-registration in scientific publication is the worked example of a community recognizing an empty-window failure and resolving it through event-class change.

Pre-pre-registration: publication binds a finding as admissible scientific knowledge. Admissibility maturity for "this hypothesis genuinely had predictive support before the data were seen" requires replication, meta-analysis, and exposure of analytical degrees of freedom — decades. Consequence viability for "prevent the finding from contaminating downstream literature" decays at publication. Once cited and propagated into meta-analyses and follow-on funded work, contamination is locked in. Retraction does not retract downstream citations.

Under any-feasible-configuration, this is an ontological Type C. No execution improvement (better journal review, faster post-publication review, AI replication tools) can construct after the fact a registration that did not occur. The relevant binding event ("finding bound as established knowledge") is admissible only on conditions that publication itself cannot satisfy.

The community's response was event-class change: a new binding event ("registered protocol's outcome bound as admissible") was made operative through pre-registration infrastructure (Open Science Framework registries [10]; the Registered Reports format originating in Chambers's *Cortex* initiative [19]; the broader reproducibility program articulated in Munafò et al. [20]; funding-body pre-registration requirements). Under the new binding event, $m(t)$ is concurrent with publication (the registered analysis is part of the binding) and $c(t)$ is extended (the registration creates a durable record).

The case is doubly instructive. It demonstrates the framework's policy traction — communities that recognize an empty-window failure can in principle do something about it. And it confirms the ontological clarification: "exists" means *codified-and-operative*. Pre-registration as concept existed for decades before it was codified-and-operative; the empty-window resolution required not the concept but the operative infrastructure.

### 6.5 Platform-worker classification — ontological breaker / clarification

The platform-worker classification case (gig-economy labor 2009–2024) is the ontological breaker test that produced the codified-and-operative clarification.

A worker's binding to platform-employer labor protections — minimum wage, overtime, unemployment, workers' compensation, anti-discrimination, collective bargaining — under conditions where the platform controls scheduling, dispatch, and pricing. Pre-classification, the binding cannot fire because the legal class to which protections attach ("employee") does not fit the platform configuration, and the alternative class ("independent contractor") fits but carries none of the protections.

The case has a temporal seam. Pre-2014 (approximately): the platform-worker category genuinely had not been conceived; the legal vocabulary lagged the technological/economic development. The binding event ("platform worker bound to labor protections") did not exist as an operative class. The case is unambiguously ontological under any-feasible-configuration; closure requires creating a new binding event entirely.

Post-2017 (approximately): the category was conceived; AB5 was drafted and pending in California, eventually codifying the ABC test for employee classification [21]; the UK Supreme Court would rule in *Uber BV v Aslam* [2021] UKSC 5 [23]; the EU Platform Work Directive would land in 2024 [24]. Concurrently, Proposition 22 (2020) was specifically funded by interested platforms to prevent codification of the new event class for gig drivers in California [22], and parallel reconstitution efforts followed in other jurisdictions.

The post-2017 cohort straddles ontological and manufactured. Under one reading of the ontological override burden — "show the missing event class already exists and only execution lags" — the class arguably exists as a legislative proposal, and the case reclassifies to manufactured. Under the alternative reading, a legislative proposal is not the operative event class, and the case remains ontological. Different rulings on the same cohort.

The framework resolves this with the codified-and-operative clarification. "Exists" means *codified-and-operative-as-binding-event*. With the clarification: pre-2014 platform workers stay ontological; post-2017 California reclassifies to manufactured (where the event class is in motion but not complete, and closure depends on the political-economic configuration that determines whether the codification process completes or is reconstituted). Same case-domain, different sub-types by phase, both correctly classified.

This case is also the empirical evidence for one of the framework's open refinements (§8): cases can transit sub-types over time. The matrix as currently developed treats sub-type as a per-case property; the platform-worker case suggests it may need to handle sub-type-by-phase explicitly. We hold that refinement as candidate, not promoted.

---

## 7. Relation to Adjacent Results

The empty-window framework sits in a constellation of negative results across the present series. We identify three explicit relationships.

*No Universal Plant Clock* (Paper 22 [5]) decomposes timing failure by *layer* — gauge, clock, estimation, actuation. The four-layer decomposition asks: in which layer of the regulatory architecture does the timing failure live? The empty-window framework asks an orthogonal question: regardless of which layer is involved, in which *direction* on the temporal axis does the gap open between the binding action and the binding consequence? The two decompositions can coexist on the same case. A given empty-window failure can be characterized as both an estimation-layer maturity failure (Paper 22 [5]) and an empty-window failure of the manufactured sub-type (this paper). Neither characterization subsumes the other.

*Epistemic Border Control* (Paper 25 [8]) establishes a spatial substitution failure: when a target variable is unsensed, regulation falls back on a measurable proxy whose closure relation to the target is not preserved. The present paper is the temporal sibling. Both are negative results in the same family — failures that no purely procedural fix can close, where the architectural response is to restructure the binding rather than to optimize within it. The relationship is sibling, not subsumption: spatial substitution and temporal detachment are independent failure axes that can coexist on the same system.

The two-paper pair carries a stronger joint claim than either alone. A system can have spatial substitution without temporal detachment (an unsensed-target failure within a temporally tractable binding window) or temporal detachment without spatial substitution (a properly-sensed target whose binding window is empty). Systems with both — including many of the institutional failures most resistant to reform — face a joint problem that neither sub-framework alone makes visible.

*Obligation-Unsound Reconciliation* (Paper 27 [9]) is currently scaffolded; the relationship is preliminary. We expect Paper 27 [9] to import the m(t)/c(t) framing for evidence horizons, causality horizons, and substrate-accusation horizons. Paper 27 [9] should not absorb the full premature/belated duality; it should import horizons, not the temporal-seam argument. This expectation is provisional and will be tightened (or revised) when Paper 27 [9] leaves scaffold status.

---

## 8. Limitations

The framework is a working draft from a series of stress-tests rather than settled doctrine. Four limitations require explicit naming.

**Override-burden standard of evidence.** The matrix override columns use "show X" language without specifying the standard of evidence (empirically? counterfactually? to what bar?). Cases on the boundary between sub-types — the platform-worker post-2017 California cohort, before the codified-and-operative clarification was added — produced inconsistent classifications because "show" was undertheorized. The codified-and-operative clarification addresses one specific case; the general standard remains rough. This is the highest-value remaining sharpening.

**Politically-reproduced as candidate sub-type.** Two cases (administrative-queue cascade, SOX/complex fraud) suggest a manufactured child sub-type characterized by adversarial closure: reform measures, where deployed, are reconstituted by interested parties through alternative gating mechanisms. Naming this sub-type would buy a closure-strategy distinction (adversarial vs inertial closure are different problems requiring different responses, including anti-reconstitution machinery: sunset clauses with strong defaults, anti-rollback provisions, constitutional rather than statutory entrenchment, insulated enforcement funding). Held as candidate, not promoted; promotion would require a third confirming case or a counter-case (a manufactured failure that is *not* politically-reproduced, where the inertial/adversarial distinction has analytic bite).

**Sub-type-by-phase as candidate refinement.** The platform-worker case shows a single case-domain transiting sub-types over time (ontological pre-2014; manufactured post-2017). The matrix as developed treats sub-type as a per-case property. The transit suggests sub-type-by-phase may need explicit treatment. Held as candidate; promotion requires a second case-domain showing the same transit, since one case is below the threshold for matrix-structural change.

**Curve-shape vs operating-point.** The two-curve model isolates the temporal axis and treats m(t) and c(t) as exogenous given the case. In practice, intervention can change the curves (faster evidence maturity, longer consequence preservation, reversibility infrastructure) rather than just shifting the operating point along fixed curves. The framework distinguishes execution improvement (operating-point) from event-class change (curve-shape, in part), but the boundary is not always sharp. Cases that look like operating-point shifts may be enabled by latent curve-shape interventions. We have not formalized the operating-point/curve-shape distinction beyond the per-regime feasibility specifications in §5.1.

---

## 9. Conclusion

The contribution this paper claims is small but specific: empty-window failures are not slow processes. They are regimes where legitimacy and consequence never overlap.

This distinction matters because the response strategies are qualitatively different. Slow processes admit throughput improvement: faster intake, larger staff, better tools, automated decisions, parallel pathways. Empty-window failures do not. The intervention they admit is event-class change — restructuring what is being bound, by whom, under what authority, with what consequence-preservation infrastructure. Confusing the two costs years of misdirected reform energy and accumulates downstream institutional failure.

The framework's central political move is making the counterfactual regime choice explicit. The same case can classify differently under different regimes. Under prevailing political incentives, a manufactured empty-window may be structurally unfixable; under any feasible political configuration, it may be resolvable in principle. Both classifications are legitimate; they answer different questions. The framework's work is to make the question being answered visible to the analytical vocabulary.

We have not built a settled doctrine. The override-burden standard is still rough; two candidate refinements (politically-reproduced as sub-type, sub-type-by-phase as a per-case property) are held in candidate state. What we have built is a framework with enough discrimination to classify a useful set of cases, enough enforcement to resist regime-shopping, and enough explicit limitations to be falsifiable rather than universal.

The empty-window framework is a temporal sibling to the spatial substitution result of *Epistemic Border Control* (Paper 25 [8]) and an orthogonal complement to the layer decomposition of *No Universal Plant Clock* (Paper 22 [5]). Together they identify a class of institutional failures that no procedural fix can close — failures whose response strategies live in the architecture of binding rather than in the optimization of execution.

The vocabulary for this kind of failure is currently absorbed under the more comfortable label of "slow process." Getting it back is the work.

---

## References

[1] Beck, J. (2024). Toward a Second Law for Organizations. Δt Framework series, Paper 2. Zenodo.

[2] Beck, J. (2025). Unauthorized Durability: Hysteretic Lock-in and the Ratchet of Premature Commitment. Δt Framework series, Paper 18. Zenodo.

[3] Beck, J. (2025). Cybernetic Fault Domains. Δt Framework series, Paper 15. Zenodo.

[4] Beck, J. (2025). Premature Remediation. Δt Framework series, Paper 19. Zenodo.

[5] Beck, J. (2026). No Universal Plant Clock: A Four-Layer Decomposition of Δt Failure. Δt Framework series, Paper 22, version 1.1. Zenodo. doi:10.5281/zenodo.19119617

[6] Beck, J. (2026). The Non-Self-Identical Controller. Δt Framework series, Paper 23. Zenodo. doi:10.5281/zenodo.19055415

[7] Beck, J. (2026). Shared Vision as Coordinating Prior. Δt Framework series, Paper 24. Zenodo. doi:10.5281/zenodo.19861995

[8] Beck, J. (2026). Epistemic Border Control: Substitution under Observability Asymmetry. Δt Framework series, Paper 25. Forthcoming.

[9] Beck, J. (forthcoming). Obligation-Unsound Reconciliation. Δt Framework series, Paper 27.

[10] Nosek, B. A., et al. (2015). Promoting an open research culture. *Science*, 348(6242), 1422–1425.

[11] Stuart-Smith, R. F., Otto, F. E. L., Saad, A. I., Lisi, G., Minnerop, P., Lauta, K. C., van Zwieten, K., & Wetzer, T. (2021). Filling the evidentiary gap in climate litigation. *Nature Climate Change*, 11(8), 651–655.

[12] Frumhoff, P. C., Heede, R., & Oreskes, N. (2015). The climate responsibilities of industrial carbon producers. *Climatic Change*, 132(2), 157–171.

[13] *Juliana v. United States*, 947 F.3d 1159 (9th Cir. 2020). (Standing barrier in U.S. federal climate litigation by youth plaintiffs.)

[14] Behrman, R. E., Benner, J. S., Brown, J. S., McClellan, M., Woodcock, J., & Platt, R. (2011). Developing the Sentinel System — A national resource for evidence development. *New England Journal of Medicine*, 364(6), 498–499.

[15] Carpenter, D. (2010). *Reputation and Power: Organizational Image and Pharmaceutical Regulation at the FDA*. Princeton University Press.

[16] Herd, P., & Moynihan, D. P. (2018). *Administrative Burden: Policymaking by Other Means*. Russell Sage Foundation.

[17] Sarbanes-Oxley Act of 2002, Pub. L. No. 107-204, 116 Stat. 745 (codified in scattered sections of 15, 18, 28, and 29 U.S.C.). §404 codified at 15 U.S.C. §7262; §906 codified at 18 U.S.C. §1350.

[18] Coates, J. C., IV (2007). The goals and promise of the Sarbanes-Oxley Act. *Journal of Economic Perspectives*, 21(1), 91–116.

[19] Chambers, C. D. (2013). Registered Reports: A new publishing initiative at *Cortex*. *Cortex*, 49(3), 609–610.

[20] Munafò, M. R., Nosek, B. A., Bishop, D. V. M., Button, K. S., Chambers, C. D., Percie du Sert, N., Simonsohn, U., Wagenmakers, E.-J., Ware, J. J., & Ioannidis, J. P. A. (2017). A manifesto for reproducible science. *Nature Human Behaviour*, 1, 0021.

[21] California Assembly Bill 5 (2019), ch. 296, 2019 Cal. Stat.; codified at Cal. Lab. Code §§ 2775–2787 (the "ABC test" for employee classification).

[22] California Proposition 22 (2020), the *Protect App-Based Drivers and Services Act*; constitutional challenge largely resolved in *Castellanos v. State of California*, 14 Cal. 5th 716 (2024).

[23] *Uber BV v Aslam* [2021] UKSC 5. Supreme Court of the United Kingdom.

[24] Directive (EU) 2024/2831 of the European Parliament and of the Council of 23 October 2024 on improving working conditions in platform work. *Official Journal of the European Union*, L series, 11 November 2024.

[25] Manheim, D., & Garrabrant, S. (2018). Categorizing variants of Goodhart's Law. arXiv:1803.04585.

---

*Status: v0.2 draft, 2026-05-04. Companion working material: `working/premature-belated-duality.md`, `working/six-meets-six.md`, `preprint/26-premature-belated-duality/CASE_TESTS.md`, `preprint/26-premature-belated-duality/NOTES.md`. Not yet pushed to Zenodo. External-literature citation pass completed in v0.2.*
