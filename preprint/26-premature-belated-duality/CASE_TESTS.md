# Paper 26 — Case Tests for the Four-Condition Promotion Test

*Working note — 2026-05-04. Status: **gate-test execution.** Source of the four conditions: `NOTES.md` §"Four-condition promotion test" (chatty 2026-05-03). Source of case template: `working/premature-belated-duality.md` §"Chatty paper-shaping pass — 2026-05-01."*

## What this file is

The four-condition test was added to `NOTES.md` on 2026-05-03 as candidate gate material for P26 promotion. The conditions are:

1. Binding would have consequence only before time $t_c$.
2. Binding becomes admissible only after time $t_m$.
3. $t_m > t_c$.
4. Changing the relation requires changing the authority/process/event class, not merely improving execution.

Condition 4 is the discriminator. Without it, every slow institution becomes an empty-window example.

This file runs six candidate cases. The first three (climate, FDA, Brasília) are scored against the original NOTES.md four-condition test, and the postmortem section revises #4 from where they bent it. The next two (pre-registration, Sarbanes-Oxley) are scored against the compressed revision, to test whether the compression survives contact with cases that were flagged as possible breakers. The sixth (platform-worker classification) is an end-to-end ontological-category breaker test against the prescriptive matrix produced by the sharpening pass.

- **Generational climate harm** — natural-latency, expected clean Type C. Calibration.
- **FDA pre-market approval** — adversarial. The "execution improvement vs. event-class change" question is exactly the field reformers and skeptics fight over.
- **Brasília administrative queue cascade** — the book's anchor case (Ch. 11). If #4 reclassifies it as Type B (belated-process), that's a seam to find before the book hardens around it.
- **Pre-registration in science** — case where event-class change actually happened. Tests whether the test recognizes a successful resolution.
- **Sarbanes-Oxley and complex financial fraud** — case where event-class change was *partial*. Tests whether the compressed test handles residual gaps after incomplete reform.
- **Platform-worker classification harms, 2009–2024** — ontological breaker. Tests whether ontological default to any-feasible survives, whether "event class itself missing" classifies differently from manufactured delay, and whether the override-burden standard needs sharpening.

---

## Case 1: Generational climate harm

### Binding event

A specific, justiciable binding: a claim by individuals born 2050–2100 against firms emitting 1990–2030 for harm caused by sea-level rise, ecosystem collapse, or attributable extreme-weather mortality. The binding action is the legal recognition that emitter X owes claimant Y, with recoverable damages.

### m(t): admissibility maturity

Requires:

- Population-scale attribution science mature enough to allocate harm shares to specific emitter cohorts (not "fossil fuel use writ large" but "Annex-I emitter X, 1990–2030, shares Z% of cohort Y's harm").
- Legal infrastructure recognizing intergenerational tort or its functional equivalent.
- Plaintiff cohort actually existing and harmed (otherwise no standing).

Earliest plausible $t_m$: ~2070 for the 2050-cohort plaintiff class, since attribution maturity follows harm manifestation by ~10–20 years and legal recognition follows attribution by another decade.

### c(t): consequence viability

Decays via:

- Defunct emitters (corporate dissolution, M&A absorption into entities that did not commit the original act).
- Asset dispersion (dividends paid out, capital returned, parent companies indemnified).
- Decision-maker mortality (no one to depose, no one to hold accountable in the moral sense).
- Political-will erosion (the constituency that would have demanded accountability has aged out or assimilated to the new climate baseline).

For most 1990–2030 emitter / 2050-cohort claimant pairs, $t_c$ has already decayed below $\theta_c$ by $t_m$.

### Scoring against the four conditions

1. Consequence only before $t_c$? **Yes.** Recovery against a dissolved entity with dispersed assets is not consequence in any meaningful sense.
2. Admissible only after $t_m$? **Yes.** Attribution science cannot mature before harm manifests at population scale.
3. $t_m > t_c$? **Yes** for the relevant emitter / claimant pairing.
4. Closing the gap requires authority/process/event-class change, not execution improvement? **Yes.** Faster epidemiology, larger cohort studies, more aggressive standing rules — none can shorten the multi-decade interval between emission and manifest harm. Closure requires changing the binding event from "individual tort against specific emitter" to a different class entirely (intergenerational trust, no-fault industrial-harm fund, constitutional climate right). That is event-class change.

### Verdict

**Type C — empty-window.** All four conditions hold. Calibration confirmed: the test correctly classifies a case that intuition unambiguously identifies as empty-window.

### What P26 uniquely explains

Prose would call this "the law moves too slow for climate." The two-curve formalism distinguishes this from "the law just needs to move faster" — the gap is not in execution, it is in the structure of the binding event itself. No amount of process acceleration can compress the manifestation latency. The legitimate response is event-class change, not throughput improvement. That distinction is what #4 is asserting.

---

## Case 2: FDA pre-market approval (mass-market chronic-use drugs)

### Binding event

FDA approval of a new chemical entity for a mass-market chronic-use indication (e.g., a long-acting cardiovascular or psychiatric drug). The agency binds the market by certifying safety and efficacy at a defined evidence threshold; this binding licenses mass exposure.

### m(t): admissibility maturity

Full admissibility — characterization of population-scale safety, sub-population effects, long-term effects, drug-drug interactions in real-world polypharmacy — requires post-market exposure data accumulated over years to decades. Phase III trials (typical $n$ = 3,000–10,000, duration 1–4 years) characterize neither rare adverse events nor long-term effects.

### c(t): consequence viability

The "consequence" of the approval decision attaches to two distinct populations:

- **Pre-exposure population**: consequence viability is high; if the drug is withdrawn before they take it, harm is averted.
- **Post-exposure population**: consequence viability decays asymmetrically. Withdrawal does not undo exposure; harm already incurred is not reversed by removing the drug from market.

For mass-market chronic-use drugs, the post-exposure population accumulates rapidly — often millions within a few years of approval. The consequence-viable window for the original approval decision (preventing inappropriate exposure) closes quickly.

### Scoring against the four conditions

1. Consequence only before $t_c$? **Partial.** Some consequences (preventing exposure) do close. Others (regulatory legitimacy, precedent for future approvals, civil liability) attach indefinitely.
2. Admissible only after $t_m$? **Yes.** Long-term and rare-event safety profiles cannot be characterized faster than population exposure accumulates them.
3. $t_m > t_c$? **Often yes** for mass-market chronic-use indications. By the time long-term safety is characterized, mass exposure is locked in.
4. Closing the gap requires authority/process/event-class change, not execution improvement? **Contested.** This is the fight.

#### The fight at #4

Reformers' position: improve trial design (larger Phase III, longer follow-up), better post-market surveillance (active rather than passive AE reporting, real-world-evidence platforms, AI-assisted signal detection), faster regulatory response to signals. All execution improvement.

Skeptics' position: the gap between "approved for use" and "characterized at population scale" is structural — you need the population exposure to characterize the population effects. No amount of trial enlargement substitutes for actual deployment. The gap is irreducible.

Where the test bends: condition 4 forces a binary classification ("execution OR event-class") onto a continuum. Reality: some of the gap is closable by execution (better surveillance), some isn't (manifestation latency for long-tail effects). The condition as stated does not specify how much execution-improvement potential disqualifies a case as Type C.

A sharper reading: the *residual* gap after maximum feasible execution improvement is what matters. For mass-market chronic-use drugs, the residual is non-zero and structural — you cannot characterize 20-year effects in less than 20 years of exposure. Closing the residual requires changing the binding event class itself: from "approval as gatekeeping certification" to "conditional approval with mandatory long-term post-market study and pre-committed withdrawal triggers." That is event-class change.

Under the sharpened reading: **Type C, but only after explicitly assessing residual.**

### Verdict

**Borderline Type C.** The case passes #4 only under a sharpened reading that distinguishes the residual gap (after feasible execution improvement) from the total gap. As stated in NOTES.md, condition 4 leaves this ambiguous.

### What this case does to the test

It surfaces that #4 is binary over a continuum. The condition needs either (a) explicit reference to a residual after feasible execution improvement, or (b) a stronger phrasing that makes clear closure requires changing what is bound, not how. Both refinements are in the postmortem.

---

## Case 3: Brasília administrative queue cascade

### Binding event

A claimant's binding to an entitlement program (SNAP, disability, housing assistance, prior-authorization care). The state binds the relationship by approving or denying. The binding licenses material support — food, medical care, shelter, income.

### m(t): admissibility maturity

Claimant-side admissibility requires:

- Documentation collection (often across institutions that themselves have queues).
- Prior-authorization navigation.
- Initial denial → appeal → reconsideration → re-submission cycles.
- Cross-program coordination where any one program's denial cascades into others.

Engineered slow. Per book companion (`working/book-empty-binding-window.md`): claimant admissibility maturity is the slow side by *design*, not by accident.

### c(t): consequence viability

Consequence decays via:

- Eviction (housing assistance after eviction does not restore housing).
- Job loss (disability after career collapse does not restore career trajectory).
- Savings exhaustion (SNAP after asset depletion does not restore the household's pre-crisis position).
- Health degradation (prior-auth approval after disease progression does not restore the earlier disease stage).
- Plaintiff dispersal in cascade (the household that filed has now moved, separated, or lost contact).

### Scoring against the four conditions

1. Consequence only before $t_c$? **Yes.** Each entitlement has a consequence-viable window beyond which the support no longer attaches to the harm it was designed to prevent.
2. Admissible only after $t_m$? **Yes.** The administrative process is the gate.
3. $t_m > t_c$? **Often yes**, particularly for cascading multi-program cases.
4. Closing the gap requires authority/process/event-class change, not execution improvement? **This is the seam.**

#### The seam at #4

Reformers (administrative-state defenders) point to demonstrably effective execution improvements:

- Single-portal applications (CalFresh, BenefitsCal-style integrations).
- Automated/passive eligibility determination (Medicaid auto-renewal where data exists).
- Presumptive eligibility (issue benefits while verification pends).
- Proactive enrollment (pre-fill applications from existing administrative data).

Where these have been deployed, gaps measurably close. By a literal reading of #4, this looks like execution improvement closing the window — which would classify the case as Type B (belated-process), not Type C.

The book's framing (`working/book-empty-binding-window.md`) reads the case differently: the slowness is **procurement**, not failure. The administrative queue is engineered, and where reform measures are deployed, opposing political forces reconstitute the slowness through new gates (work requirements, fraud audits, "integrity" measures, citizenship verification, signature-match challenges). To make execution improvement *durable* requires re-binding what is being licensed: from "verification of deservingness" to "presumptive entitlement." That is event-class change.

Under the literal reading: **Type B (belated-process).**
Under the book's framing: **Type C, but only relative to a counterfactual that holds the political-will-to-re-erect-the-queue constant.**

#### What the case reveals about #4

Condition 4 is silent on counterfactual specification. "Can execution improvement close the gap?" depends on:

- *Holding political/institutional pressure constant*: in some jurisdictions, yes.
- *Under any feasible political configuration*: no, because the slowness is the political product the queue exists to deliver.

The book is operating in the second counterfactual — it reads the queue as architecturally engineered, so closure requires architectural change. The four-condition test, as written, sits closer to the first counterfactual — it asks whether *any* execution improvement could close the gap.

These are different questions and they classify the case differently.

### Verdict

**Type B under the literal reading of #4. Type C only under the book's stronger counterfactual.** The book anchor case is P26-compatible, but only with the four-condition test sharpened to specify which counterfactual it evaluates against. As written, the test would reclassify Brasília as belated-process, which would leave Ch. 11 leaning on a case that the formalism does not endorse.

This is a real seam. The fix is either to sharpen #4 (specify the counterfactual) or to acknowledge in the book chapter that the case is *manufactured-empty-window* (taxonomy item 3 in NOTES.md), which already builds the political counterfactual into the sub-type.

---

## Postmortem: where condition 4 bent

Three findings, in order of severity.

### Finding 1: #4 is silent on counterfactual specification

Surfaced by the Brasília case. "Closing the gap requires more than execution improvement" requires a counterfactual: under what feasible institutional/political configuration are we evaluating execution potential? Two reasonable answers (status-quo political pressure vs. any feasible configuration) classify the same case differently.

This is the most consequential finding because it directly affects whether the book's anchor case is supported by the formalism.

**Candidate fix:** Make the counterfactual explicit. Two options:

- **Strict counterfactual**: "no feasible execution improvement, under any plausible political configuration, can close the gap." Sets a high bar; classifies engineered-slowness cases as Type B (belated-process) unless the engineering itself is structurally locked in.
- **Status-quo counterfactual**: "no execution improvement deployable under prevailing institutional incentives can close the gap." Lower bar; classifies engineered-slowness as Type C when the political will to re-erect the queue is durable.

The status-quo counterfactual is closer to what the book wants. It also tracks the manufactured-empty-window sub-type already named in NOTES.md.

### Finding 2: #4 is binary over a continuum

Surfaced by the FDA case. The question "execution improvement OR event-class change" forces a binary on a continuum. Real cases often have both: some of the gap is closable by execution, some is structural to the binding event. The condition does not specify how much residual structural gap qualifies a case as Type C.

**Candidate fix:** Reframe #4 as a residual condition: "after feasible execution improvement is applied, the residual gap is non-zero and structural to the binding event class." This makes the test address what reformers and skeptics actually fight over — the residual — rather than the total gap.

### Finding 3: The taxonomy in NOTES.md should be load-bearing in #4

NOTES.md already names four sub-types (natural-latency, procedural, manufactured, ontological). The four-condition test treats these as descriptive categories that share a common test. The case results suggest the sub-types correspond to different ways #4 is satisfied:

- **Natural-latency**: #4 satisfied trivially. Physical causality timelines are not closable by political configuration. (Climate case.)
- **Procedural**: #4 typically *fails*. Execution improvement closes the gap; this is belated-process, not empty-window.
- **Manufactured**: #4 satisfied only under status-quo counterfactual. (Brasília case.)
- **Ontological**: #4 satisfied because the event-class itself does not yet exist (no $\theta_m$ defined).

If the sub-types correspond to different #4 satisfaction modes, the test should probably be stated as a per-sub-type matrix rather than a single uniform condition.

---

## Compressed revision of condition #4 — 2026-05-04

*Status: candidate revision after compression pass. **Not ratified.** Conditions 1–3 unchanged.*

> **4. Residual event-class mismatch.** Within the specified counterfactual regime, the residual gap that survives feasible execution improvement (intake, automation, staffing, portal integration, surveillance throughput) is closable only by changing authority structure, entitlement definition, burden of proof, consequence timing, or event class.

The counterfactual regime is per-case data, not test data. Each case must declare which regime it is evaluated against. Cases evaluated under different regimes may classify differently — that is informative about the case, not a defect of the test.

### Subtype matrix

| Sub-type | Counterfactual regime | #4 typical outcome |
|---|---|---|
| Natural-latency | Any feasible configuration | Passes (physical causality not closable by political reform) |
| Procedural | Status-quo regime | Fails (reform measures close the gap; classifies as Type B) |
| Manufactured | Status-quo regime | Passes (slowness reconstituted by political incentive) |
| Ontological | Any feasible configuration | Passes (event class itself missing) |

### The Brasília fork (preserved as candidate P26 move)

The administrative-queue case classifies differently under different counterfactual regimes:

- **Under any-feasible-configuration**: Type B (belated-process). Single-portal apps, presumptive eligibility, auto-renewal demonstrably close the gap where deployed.
- **Under status-quo regime**: Type C (manufactured-empty-window). The slowness is reproduced by the governing arrangement; reform measures, where deployed against political opposition, get reconstituted as new gates (work requirements, fraud audits, integrity measures, signature-match challenges).

The fork is not a flaw of the test. It is what makes the manufactured sub-type analytically distinct from procedural failure: same surface, different durability under political pressure. P26's central move is that the choice of counterfactual is itself a political claim — naming the regime under which a window is or is not empty is part of what the framework lets a reader see clearly.

### What this compression still owes (after Cases 4 and 5)

- "Feasible execution improvement" is still a primitive. What counts as feasible inside a given regime probably needs a short per-regime example list, otherwise #4 inherits the smuggled-counterfactual problem one level down (it just shifts from "what counts as execution" to "what counts as feasible execution within this regime").
- The subtype matrix is currently descriptive (which regime tends to pair with which sub-type). It is not yet prescriptive (whether case-authors must justify their regime choice, and against what standard).
- Cases 4 and 5 (below) added the candidate sub-type **politically-reproduced empty-window** as a child of the manufactured category. Whether this earns its keep as a named sub-type or stays absorbed in "manufactured" is undecided.

---

## Case 4: Pre-registration in scientific publication

### Binding event(s)

Two paired bindings, separated by the event-class change pre-registration introduces:

- **Pre-pre-reg**: Publication binds a finding as admissible scientific knowledge. Implicit "this hypothesis was predictively tested" claim baked into the significance-test framing.
- **Post-pre-reg**: Publication binds the *registered protocol's* outcome (positive or null) as admissible. Hypothesis-test status is now a concurrent property of the binding, not a post-hoc reconstruction.

### Pre-pre-reg case scoring

$m(t)$ for "this hypothesis genuinely had predictive support before the data were seen": requires replication, meta-analysis, exposure of analytical degrees of freedom — decades.

$c(t)$ for "prevent this finding from contaminating downstream literature": decays at publication. Once cited and propagated into meta-analyses and follow-on funded work, contamination is locked in. Retraction does not retract downstream citations.

1. ✓ — consequence has a viable window only before downstream propagation.
2. ✓ — distinguishing a genuine prediction from after-the-fact narrative requires the registration to have occurred *before* the data were seen, which by definition is impossible after the fact.
3. ✓ — $t_m$ (decades) >> $t_c$ (months to years for a high-impact paper).
4. **Passes under any-feasible-configuration.** No execution improvement (better journal review, larger reviewer pools, faster post-publication review, AI replication tools) can reconstruct after the fact a registration that did not occur. Closure requires changing the event class — from "publication-as-admissibility-binding" to "registered-protocol-compliance-as-admissibility-binding." That is exactly what pre-registration is.

### Effect on the compressed test

Confirming. Pre-registration is a worked example of the test's prescription in action: a community identified a Type C empty-window failure, made the event-class change the test prescribes, and closed the window. The post-pre-reg binding is no longer an empty-window because the binding event has changed.

This case shows the framework has *policy traction*: the classification it produces (Type C requires event-class change, not execution improvement) corresponds to a recognized real-world resolution path. Communities that recognize a Type C failure can in principle do something about it.

The compression survives this case.

---

## Case 5: Sarbanes-Oxley and complex financial fraud

### Binding event

Financial-reporting accuracy binding via audit attestation (auditor's signature; post-SOX §404 internal-controls report; post-SOX §906 CEO/CFO criminal attestation). This binding licenses investor capital allocation against the reported numbers.

### m(t): admissibility maturity

Detecting fraud at scale requires forensic reconstruction, whistleblower exposure, third-party reconciliation — typically after a precipitating event (liquidity crisis, short-seller report, criminal investigation). For *simple* fraud (revenue overstatement, expense capitalization), $m(t)$ shortened materially post-SOX. For *complex* fraud (off-balance-sheet structures, multi-jurisdiction shells, related-party concealment, asset-substitution), $m(t)$ remains years to decades.

### c(t): consequence viability

Decays via firm collapse (Enron, Lehman, Wirecard), executive judgment-proof status (post-bankruptcy clawback partial at best), investor dispersal, criminal-statute-of-limitations clocks.

### Conditions

1. ✓ — recovery and accountability windows close at firm collapse.
2. ✓ — fraud detection requires evidence accumulation that the fraud is, by design, suppressing.
3. **Conditional.** Simple fraud post-SOX: often $t_m \leq t_c$. Complex fraud post-SOX: still $t_m > t_c$.
4. **Brasília-style fork applies again.**

### Fork

- **Under any-feasible-configuration**: Type B for most fraud. Radical reform — public-utility auditors replacing the private big-4 model; real-time SEC monitoring against hashed transaction records; mandatory beneficial-ownership registries with criminal concealment penalties — could plausibly close the gap for nearly all classes. Closure is *executable* under sufficient political will.
- **Under status-quo regime**: Type C for complex fraud. The residual gap is reproduced by the political acceptability of complex financial structures (offshore shells, opaque related-party intermediaries) and by the auditor-incentive structure (paid by the audited firm). Reform measures are reconstituted: SOX itself was attacked as overreach within years; EGRRCPA (2018) peeled back parts of Dodd-Frank; PCAOB enforcement remains contested.

### Effect on the compressed test

Confirming, with two added observations:

1. **Partial event-class change leaves residual.** SOX *was* event-class change (added §906 criminal attestation, §404 internal-controls reporting). It closed the window for simple fraud but left a structural residual for complex fraud. The compressed #4 handles this gracefully: SOX-style controls are absorbed into the post-SOX prevailing regime's "feasible execution improvement," and #4 asks what survives. Survives → complex-fraud residual → Type C under status-quo.
2. **The fork pattern repeats.** Same structural shape as Brasília: same case, different regime, different classification. This is not coincidence. It is a recurring property of cases where the slowness has *political producers* rather than physical causes. Worth flagging as a candidate sub-type of manufactured: **politically-reproduced empty-window** — slowness renewed by interested parties even after reform attempts. Distinct from the broader manufactured category, which includes one-time engineered slowness; the politically-reproduced sub-type names the *renewal mechanism* explicitly.

The compression survives this case as well.

---

## Compressed-version verdict

Cases 4 and 5 do not break the compressed #4. Both classify cleanly under it, and Case 5 surfaces a candidate refinement (politically-reproduced as a sub-type of manufactured) rather than exposing a defect.

Net read across all five cases:

- Original #4 (NOTES.md, chatty 2026-05-03): bent on Cases 2 and 3.
- Compressed #4 (this file, 2026-05-04): handled Cases 4 and 5 cleanly; still untested against ontological-category cases (no candidate ran in this file).
- The Brasília fork is now a recurring pattern, not a one-off. Cases 3 and 5 both showed it. This raises the framework's central political move from "one anchor case has this structure" to "this structure is what manufactured-empty-window means."

Promotion gate (chatty 2026-05-01): "If a case cannot show type C, it may still support P26 but does not promote it." Three of five cases show clean Type C (climate, pre-pre-reg, SOX status-quo); two show conditional Type C requiring counterfactual specification (FDA, Brasília). Gate satisfied at the case-existence level, in stronger form than after the original three-case pass.

**Status of the compressed #4**: not yet ratified, but no longer the bleeding edge. The bleeding edge is now (a) the per-regime example list for "feasible execution improvement," (b) the prescriptive form of the subtype matrix, and (c) whether "politically-reproduced empty-window" earns naming as its own sub-type.

---

## Sharpening pass — 2026-05-04

*Status: prescriptive subtype matrix and counterfactual regime selection rule, with per-regime feasibility specification folded in as foundation. Politically-reproduced sub-type held as candidate, not promoted. Compressed #4 not ratified.* **All artifacts in this section are candidate, not ratified.**

### Why a prescriptive rule is needed

The compressed #4 plus subtype matrix let us classify a case once its sub-type and regime are declared. They do not yet say *which regime* a case must declare. Without that constraint, the framework collapses into a chooser menu — an author picks the regime that classifies their preferred case the way they want. Academic buffet, terrible lighting.

This pass addresses five questions:

1. What counterfactual regime must a case declare?
2. What is the default regime by sub-type?
3. What justifies overriding the default?
4. What counts as feasible execution improvement inside each regime?
5. What prevents an author from choosing the counterfactual that produces their preferred classification?

### Per-regime feasibility (foundation)

The "feasible execution improvement" primitive is regime-relative.

**Status-quo regime — feasible execution improvement is bounded by *political durability*.**

- *Includes*: process tuning within current authority structure (faster intake, automation, staffing within existing budget); workflow redesign without legislative change (single-portal apps within existing eligibility frameworks; automated cross-program checks); tool deployment within existing oversight frameworks (AI signal detection, real-world evidence within FDA's existing authority); reform measures politically durable in the relevant jurisdiction's recent history.
- *Excludes*: reforms attempted and reconstituted (work requirements substituted for streamlined eligibility; integrity audits substituted for presumptive eligibility; EGRRCPA-style rollbacks of post-Enron controls); reforms exceeding prevailing political acceptability (public-utility auditors replacing big-4; mandatory beneficial-ownership registries with criminal concealment penalties); reforms requiring legislative change against entrenched opposition.

**Any-feasible-configuration — feasible execution improvement is bounded by *physical/technological/economic possibility*.**

- *Includes*: everything in status-quo, plus reforms within technological capability regardless of political durability (real-time blockchain-hashed monitoring of regulated transactions; presumptive entitlement at scale; public-utility auditor model); reforms requiring legislative change in counterfactual political configurations.
- *Excludes*: reforms that violate physical causality (faster epidemiology than cohort accumulation can produce; pre-registration after the fact; characterizing 20-year drug effects in less than 20 years of exposure); reforms that violate definitional constraints (event class doesn't yet exist — ontological cases).

The distinction bottoms out in observables: status-quo asks "has this reform been politically durable in jurisdiction X" (answerable from track record); any-feasible asks "is this reform within demonstrated technological/physical capability" (answerable from the engineering literature and physical constraints). The smuggled-counterfactual problem is pushed out to questions that have empirical content rather than philosophical ones.

### Counterfactual regime selection rule (candidate)

> **A case must declare the regime under which condition #4 is evaluated. The default regime follows the claimed sub-type. Natural-latency and ontological cases default to any-feasible-configuration; procedural and manufactured cases default to the prevailing authority/incentive regime. Overrides are allowed only when the case explains why the default regime misstates the source of the residual gap.**

### Compact matrix

| Claimed sub-type | Default regime | Feasible execution improvement (per-subtype shorthand) | Override burden |
|---|---|---|---|
| Natural-latency | Any feasible configuration | Measurement, modeling, early warning, faster response | Show the latency is institutionally produced, not physical/causal |
| Procedural | Prevailing authority/incentive regime | Staffing, intake, automation, portal integration, queue redesign | Show reforms are predictably reconstituted by the regime |
| Manufactured | Prevailing authority/incentive regime | Procedural improvements plus anti-gatekeeping reforms attempted in the jurisdiction | Show the delay is not reproduced by interested authority |
| Ontological | Any feasible configuration | Better detection, classification, review, documentation | Show the missing event class already exists and only execution lags |

The third column is per-subtype shorthand, not a replacement for the per-regime feasibility specification above. It gives case-authors a quick handle; ambiguous cases route back to the foundation.

### Anti-cosplay mechanism (answer to Question 5)

Three layers prevent authors from choosing the counterfactual that produces their preferred classification:

1. **The sub-type claim is itself accountable.** An author cannot pick "natural-latency" to get the any-feasible-configuration default unless they can defend the case as physically/causally produced. The same defense burden applies in reverse if the author is *justifying* a sub-type claim that determines a favorable regime.
2. **The default regime locks once sub-type is claimed.** Sub-type determines regime; the author cannot pick sub-type based on which regime they prefer without paying the sub-type override burden.
3. **Overrides carry a specific argumentative burden, not a general "I prefer this regime" license.** The override-burden column names the specific move required. The case has to argue, on its own facts, that the default regime misstates the source of the residual gap.

The mechanism is not airtight. A determined author can still cherry-pick by misclassifying the sub-type. But misclassification is now a falsifiable move (specific override burden, specific case facts) rather than a hidden judgment call. The framework's job is not to make all judgment go away; it is to make the judgment visible enough to audit.

### Politically-reproduced (candidate child sub-type, held — not promoted)

Two cases (Brasília Case 3, SOX/complex-fraud Case 5) classify cleanly under the existing manufactured category but share a closure-problem shape distinct from one-time engineered slowness:

- **One-time engineered slowness**: closure problem is *inertial*. A simple reform could close the gap and would not be reconstituted because no active interest opposes closure.
- **Politically-reproduced slowness**: closure problem is *adversarial*. Reform measures, where deployed, are reconstituted by interested parties through alternative gating mechanisms (work requirements substituted for streamlined eligibility; EGRRCPA-style rollbacks of post-SOX controls). Closure measures must withstand active opposition.

If promoted later, this would slot as a child of manufactured with its own matrix row: same default regime, different override burden ("show the slowness is inertial rather than adversarially renewed"). The closure-strategy implication is real — adversarial cases require anti-reconstitution machinery (sunset clauses with strong defaults, anti-rollback provisions, constitutional rather than statutory entrenchment, insulated enforcement funding) or shifts in the underlying political economy.

**Why kept candidate**: two cases is below the threshold for taxonomy promotion, and both classify cleanly under the un-refined manufactured category. Naming the sub-type now would buy the closure-strategy distinction at the cost of taxonomy proliferation, before the prescriptive matrix is itself ratified. Wait for one or two more cases.

### What still needs work (after sharpening pass)

- **Override-burden standard of evidence.** The right-column language ("show the latency is institutionally produced") does not yet specify the standard ("show" how — empirically? counterfactually? to what bar?). Tightening the standard is probably what brings the matrix from candidate to ratifiable. Next pass.
- **Ontological category untested by full case run.** No case in this file has worked an ontological candidate end-to-end (algorithmic discrimination before the legal category existed; gig-worker harms before classification settled). The compressed #4 plus matrix should be tested against at least one ontological case before ratification.
- **Politically-reproduced ratification.** Either a third confirming case (Brasília + SOX + one more politically-reproduced manufactured case) or a counter-case (a manufactured case that is *not* politically-reproduced, where the inertial/adversarial distinction has analytic bite) is needed to settle whether this earns sub-type status.

---

## Disposition for P26 promotion

What the case-test exercise tells us about whether P26 earns paper status:

- **The test does have bite.** All three cases received differentiated readings. The test is not vacuous.
- **The test is not yet ratifiable as written.** Two of three cases bent the test (FDA, Brasília). The bending was informative — it surfaced the counterfactual and residual issues — but the test as written would misclassify cases the framework wants to keep.
- **At least one clean Type C case exists** (climate). This is the bare minimum chatty's 2026-05-01 promotion gate required: "If a case cannot show type C, it may still support P26 but does not promote it." Climate shows Type C. Promotion gate item satisfied at the case-existence level.
- **The book anchor case is provisionally compatible** but only under the sharpened test. If the sharpened test does not earn ratification, Ch. 11 either needs a different anchor or needs to acknowledge the case is manufactured-empty-window rather than the strong empty-window claim.

**Recommended next move (not authorized — flag, not action):** sharpen #4 per the candidate revision above, then rerun this file with one or two additional cases (pre-registration in science, Sarbanes-Oxley) to see whether the sharpened version holds. If it does, the test is ratifiable and P26 is paper-shaped. If it doesn't, the case-test exercise has produced a §-insert worth of material on empty-window detection but not a paper.

---

## Case 6: Platform-worker classification harms, 2009–2024 (ontological breaker)

*Compact end-to-end test of compressed #4 plus prescriptive matrix against an ontological-category candidate. Goal: attack the matrix, not extend the file.*

### Selection rationale

Chosen over algorithmic-discrimination because the event-class crystallization timeline is documented and recent (AB5 2019, UK Supreme Court *Uber v Aslam* 2021, Prop 22 saga 2020–2024, EU Platform Work Directive 2024), so the temporal scope of "missing event class" is empirically observable rather than asserted.

### Binding event

A worker's binding to platform-employer labor protections — minimum wage, overtime, unemployment, workers' comp, anti-discrimination, collective bargaining — under conditions where the platform controls scheduling, dispatch, and pricing. Pre-classification: the binding cannot fire because the legal class to which protections attach ("employee") does not fit the platform configuration, and the alternative class ("independent contractor") fits but carries none of the protections.

### m(t): admissibility maturity

Requires either (a) the legal/administrative class "platform worker / dependent contractor" to exist with attached protections, or (b) the existing employee class to be authoritatively reinterpreted to cover platform workers. Pre-2019 in the US: neither held. ABC test had not been applied to platforms in published case law; legislative codification absent.

### c(t): consequence viability

Decays via worker exit (younger cohorts replacing harmed workers); platform restructuring through subsidiary networks; arbitration enforcement (worker claims locked out of class actions); statute-of-limitations clocks (2–3 years for wage claims); platform exit-threats from jurisdictions (Uber threatening to leave California pre-Prop 22). For most pre-2019 cohort/platform pairs, $t_c < \theta_c$ by the time classification matures.

### Compressed #4 scoring

Under any-feasible-configuration: no execution improvement (better wage-and-hour enforcement under existing categories; more aggressive Borello application; faster DOL audits) can construct after the fact a legal class that did not exist when the harm occurred. Closure requires changing the event class — codifying "platform worker" with attached protections (AB5 model), or extending "employee" via authoritative reinterpretation (UK *Uber* 2021 model). Passes #4 under any-feasible.

### Counterfactual regime selection rule application

The case claims **ontological** sub-type. Default regime per matrix: **any-feasible-configuration**. Under this default, the pre-classification cohort classifies as Type C.

The case has a **temporal seam** that stress-tests the sub-type claim. Pre-2014ish: the platform-worker category genuinely had not been conceived; the legal vocabulary lagged the technological/economic development. Post-2017ish: the category was conceived, AB5 was on the table, and Prop 22 was specifically funded by interested platforms to prevent codification. By 2020 the sub-type has effectively shifted from ontological (no class exists) to manufactured-with-politically-reproduced character (class conceivable and proposed, blocked by reconstitution). Same harm domain, different sub-type by phase.

The matrix as written does not say whether the case must declare its sub-type for a temporal scope or for the case-domain as a whole.

### Matrix application — override burden test

For an author claiming ontological for the post-2017 California cohort, the override challenger invokes the ontological override burden: **"Show the missing event class already exists and only execution lags."** By 2017 in California, AB5 was drafted and pending; the class arguably *existed as a legislative proposal*. The challenger argues: the class exists as text; what's missing is only execution (legislative passage + implementation). Under this challenge, post-2017 California reclassifies to procedural or manufactured.

The author counter-argues: a legislative proposal is not the event class itself; the class is missing until codified and judicially enforceable. Under this defense, ontological holds.

The override burden as stated does not adjudicate. "Already exists" is ambiguous between *conceived/proposed* and *codified/operative*.

### Verdict

**Does ontological defaulting to any-feasible-configuration survive?** Yes for clean pre-classification cases (pre-2014 platform workers; algorithmic discrimination pre-administrative-legibility). The default makes sense because no execution improvement within the existing binding event can close the gap; closure requires making a new binding event operative. (Sharpening per chatty mid-pass: the loose framing "political reconfiguration cannot change the class is absent" is wrong — political reconfiguration *can* create the class, which is exactly what AB5 did. The sharper claim is that the existing binding event has no execution path to closure; only event-class creation does. This also prevents the any-feasible regime from accidentally swallowing event-class creation as ordinary execution improvement.) Any-feasible regime correctly identifies this as not closable by execution improvement of any kind within the existing binding event. Default survives.

**Does "event class itself missing" classify differently from procedural or manufactured delay?** Yes when the class is genuinely unconceived. Ambiguously when the class is conceived but uncodified due to political opposition. The post-2017 California cohort straddles ontological and manufactured because the class exists in text and is blocked by interested authority. The four sub-types are not mutually exclusive across temporal phases of the same case-domain.

**Does the override-burden standard need sharpening before ratification?** Yes — and this case is the concrete evidence. The ontological override burden fails to specify what "exists" means: *conceived/proposed* vs *codified/operative*. Different readings produce different rulings on the same cohort. Candidate sharpening: "exists" = **codified-and-operative-as-binding-event**, not merely conceived or proposed. With this sub-clause, pre-2014 platform workers stay ontological; post-2017 California reclassifies to manufactured. Without it, the matrix produces inconsistent classifications on the same case.

### What still needs work (after ontological breaker)

- **Ontological override burden — disambiguate "exists."** Adopt "codified-and-operative-as-binding-event" or equivalent. Without this, the matrix is ambiguous on the most contested cases (where reform is in motion but not complete). Highest-value sharpening before ratification.
- **Sub-type-by-phase (candidate refinement, held — not promoted).** Cases can transit sub-types over time (Case 6's pre-2014 / post-2017 split). The matrix currently treats sub-type as a per-case property; it may need to handle sub-type-by-phase explicitly. Hold as candidate; do not modify the matrix until a second case-domain shows the same transit.
- **Politically-reproduced ratification still pending** (carried forward).

---

## Provenance

- Four conditions: NOTES.md §"Four-condition promotion test" (chatty 2026-05-03).
- Case-test template: `working/premature-belated-duality.md` §"Suggested next artifact: CASE_TESTS.md" (chatty 2026-05-01).
- Brasília book-side framing: `working/book-empty-binding-window.md`.
- This file: claude-code, 2026-05-04. Cases 1–3 scored against the original four conditions; postmortem from where the cases bent the test; compression pass on #4 (same day) producing a candidate revision plus subtype matrix; Cases 4–5 (pre-registration, Sarbanes-Oxley) scored against the compressed revision; sharpening pass (same day, prompted by chatty's "academic buffet" warning) producing the prescriptive counterfactual regime selection rule, compact matrix, and anti-cosplay mechanism, with per-regime feasibility folded in as foundation; Case 6 (platform-worker classification) as compact end-to-end ontological breaker against the prescriptive matrix. Politically-reproduced sub-type held as candidate, not promoted. Sub-type-by-phase surfaced as candidate refinement, held. Compressed #4 not ratified. Highest-value remaining sharpening: ontological override-burden disambiguation ("exists" = codified-and-operative). Next move per user direction: extraction into NOTES/CANDIDATES as ratification candidate.
