# Loop Capture

**Status:** rich staging note / synthesis candidate.
**Position:** open.
**Likely role:** adversarial-mechanism synthesis across P22 / P25 / P27 / admissibility family / WIF-composition.
**Do not assign paper number until P25/P26/P27 settlement and position decision.**

**Originated:** 2026-05-09 multi-model brainstorm from the "Control-Theoretic Sun Tzu" thread; chatty zhuzh pass + prior-art sniff test 2026-05-09; claude-code-papers cross-corpus mapping + filing 2026-05-10.

**Working public hook:**

> *Boyd gave us the shape of victory. Control-Theoretic Sun Tzu gives us the shape of its theft.*

> **Scope discipline.** Do not treat Loop Capture as a replacement for P22 / P25 / P27. Treat it as the **adversarial dual** of the spine (see *Role* below) unless the positioning question is later resolved otherwise. This warning exists because the cross-corpus connections are dense enough that the synthesis framing can quietly mutate into a master-paper claim it has not earned.

---

## Role: adversarial dual of admissibility

Loop Capture is not a new ontology. It is the adversarial inversion of the existing spine — the same coordinate system rotated from *failure diagnosis* to *adversarial exploitation*.

**Polarity flip:**

| Existing spine                                                  | Loop Capture                                                                        |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| How does a system preserve admissible action under uncertainty? | How does an adversary make inadmissible action remain admissible-looking under uncertainty? |
| Where can the loop lose contact with reality?                   | How can someone exploit that loss of contact while the loop still thinks it is governed? |
| *May this system act, given its evidence, standing, scope, and consequence?* | *How can those same gates be made to pass while the defended value is being degraded?* |

**Roles in the constellation:**

- **P22.** What layers can drift / mask / misbind.
- **P25.** What happens when the real target is unsensed and substitutes appear.
- **P27.** What happens when the controller is correct but operator reality is unsound.
- **Admissibility family.** What makes action valid or invalid.
- **WIF / witness work.** How independent channels resist co-capture.
- **Loop Capture.** How an adversary turns those seams into self-authorized wrongness.

Loop Capture is one of those roles. It is not the umbrella over them.

**Containment keepers:**

> *Loop Capture does not introduce new machinery; it reverses the sign on the existing machinery and asks how validity becomes an attack surface.*

> *Loop Capture is not the master paper. It is the adversarial-mechanism paper.*

> *This is a map of attack surfaces, not a throne.*

**Caveat on "dual."** The framing is conceptual, not yet formal. The current claim is that the *role* is dual — enough to keep the synthesis from drifting into master-paper claims, not enough to assert mathematical structure that hasn't been proved. *Do not formalize by vibes.*

The safe and dangerous framings:

- **Safe:** *Loop Capture is the adversarial inversion of admissibility.*
- **Dangerous-but-interesting:** *Loop Capture may be the dual of admissibility.*

Pair definitions, in their loosest form:

> **Admissibility.** Conditions under which action may validly proceed.
>
> **Loop Capture.** Conditions under which invalid / value-degrading action is made to proceed as valid.

Candidate dual axes (named, not earned):

| Admissibility condition | Adversarial counterpart        |
| ----------------------- | ------------------------------ |
| evidence                | evidence laundering            |
| standing                | standing spoofing              |
| scope                   | scope expansion                |
| authority               | authority capture              |
| receipt                 | legitimacy signal preservation |
| witness                 | witness co-capture             |

**The earning test.** Loop Capture earns formal duality iff every admissibility condition has a corresponding capture transformation that *preserves local pass/fail shape* while *reversing defended-value consequence*. Most candidate pairs above are plausible but unproven; some may collapse, some may need refinement, some may have no counterpart at all. The table is a hypothesis register, not a proof.

**Pin label:**

> *Possible duality candidate: Loop Capture as adversarial dual of admissibility. Do not formalize by vibes.*

**Dependency direction.** This runs one way. Loop Capture cannot be defined without the spine — you cannot describe the exploit until you know what counts as valid action. The synthesis depends on the spine; it does not subsume it.

---

## Prior-art warning: reflexive control

Loop capture must not be framed as the invention of adversarial decision-frame manipulation. The closest strategic prior art is Soviet/Russian **reflexive control** (Vladimir Lefebvre, then Timothy Thomas in the Western analytical literature): shaping or supplying the basis on which an adversary makes decisions so that the adversary voluntarily chooses the initiator's desired outcome. In Soviet military doctrine since the 1960s; modernized in Russian information-warfare literature post-2014; current US/NATO analysis of gray-zone operations leans heavily on it.

Loop capture differs by moving the claim into a control/admissibility register. It asks *how* the manipulated decision frame remains internally legitimate: which sensor, estimator, objective, admissibility, or reporting surface was captured; how legitimacy/value divergence persists; and how action remains self-authorized while defended value decays.

Working distinction:

> *Reflexive control names the strategic manipulation of the adversary's decision basis.*
> *Loop capture formalizes the feedback/governance mechanism by which that manipulation becomes internally valid action.*

Sharper:

> *Reflexive control explains how the enemy gets inside the decision frame. Loop capture explains how the captured frame continues to pass its own gates.*

Other adjacent prior art to engage carefully (not exhaustive; chatty's sniff test): OODA / Boyd; false-data injection and stealthy attacks in cyber-physical systems security (Pasqualetti / Dörfler / Bullo and successors); Goodhart's law and specification gaming; performative prediction; adversarial ML; organizational cybernetics; metric-gaming in institutional sociology; observability/SRE incident literature.

The likely contribution is the splice, not the inventory:

> *Loop capture generalizes several known failure modes into a single governance/control-theoretic pattern.*

The novel-ish joint is the **admissibility layer**: the system remains procedurally valid while becoming externally wrong. Existing literature stops at bad data, bad model, bad metric, bad incentive. This adds **authorized wrongness**.

---

## Open positioning question

Loop capture may be:

1. A standalone numbered paper.
2. A reframe or extension of P22's gauge / clock / estimation / actuation decomposition.
3. A synthesis paper integrating P22, P25, P27, the admissibility family, WIF-composition, and non-adversarial primitives such as stale binding / zombie obligation.

Current leaning: **(3)**. Loop capture appears to be less a new isolated primitive than the adversarial-mechanism synthesis that explains why several existing corpus elements rhyme.

---

## Core idea and central naming

**Core definition:**

> Loop capture occurs when adversarial influence alters a system's sensing, interpretation, objective, admissibility, or reporting conditions such that the system continues producing internally legitimate actions while degrading the value it exists to defend.

**Central naming — authorized wrongness:**

> *Authorized wrongness:* action that is locally valid under the system's governance rules while degrading the value those rules exist to protect.

That's the bridge between control theory and Governor / Wicket / admissibility. It prevents the paper from collapsing into "bad metrics bad" — the point is not merely wrong optimization, the point is wrong optimization **with papers**.

**Formal heart:**

> *Loop capture is sustained divergence between legitimacy signal and defended value.*

In symbols:

```text
ΔL_t ≥ 0 while ΔV_t < 0
```

where $L_t$ = internal legitimacy / authorization confidence and $V_t$ = defended value.

**Sharpest single line:**

> *The enemy does not seize the controls. The enemy edits the world in which the controls make sense.*

---

## Candidate abstract

> Modern adversarial systems often do not need to seize control, interrupt operation, or falsify every signal. They can instead capture the loop by which a system senses, interprets, authorizes, acts, and reports on itself. We call this pattern **loop capture**: adversarial influence over the internal conditions of valid action, producing self-authorized behavior that degrades the value the system exists to defend while preserving legitimacy signals. This paper formalizes loop capture as divergence between internal legitimacy and defended value across feedback systems, distinguishes it from compromise, deception, and Goodhart-style proxy failure, and identifies sensor, estimator, objective, admissibility, and reporting capture as recurring surfaces. We argue that defenses require independent witnesses, validity-regime audits, and explicit separation between evidence, authorization, action, and report.

---

## Formal skeleton

Discrete-time system:

```text
x_t        true system state
y_t        observed signal
b_t        belief / estimated state
J          internal objective / loss / reward
A          admissibility / authorization predicate
u_t        action
m_t        report / legitimacy signal
V          defended value / true objective
U_adv      adversary utility
a_t        adversarial influence
Γ          governance/context state
L_t        internal legitimacy / authorization confidence
```

Normal loop:

```text
x_{t+1} = f(x_t, u_t, w_t)
y_t     = h(x_t, v_t)
b_t     = E(b_{t-1}, y_t, u_{t-1})
u_t     = π(b_t, J) subject to A(b_t, u_t, Γ)
m_t     = M(b_t, u_t, Γ)
```

Captured loop (transformations applied by adversarial influence $a_t$):

```text
y'_t = C_y(y_t)          sensor capture
E'   = C_E(E)            estimator capture
J'   = C_J(J)            objective capture
A'   = C_A(A)            admissibility capture
M'   = C_M(M)            reporting capture
π'   = C_π(π)            controller/policy capture, optional
```

Then:

```text
b'_t = E'(b'_{t-1}, y'_t, u'_{t-1})
u'_t = π'(b'_t, J') subject to A'(b'_t, u'_t, Γ)
m'_t = M'(b'_t, u'_t, Γ)
```

**Capture condition (the formal heart):**

```text
InternalLegitimacy(loop') = true       (L'_t high)
Detector(m'_t)            = quiet
V(x'_{0:T})               decreases
U_adv(x'_{0:T})           increases
u'_t                      remains system-authorized
```

Plain English:

> The victim takes actions it can justify, using evidence it accepts, toward goals it believes are valid, while the real defended objective decays.

**Differential / sensitivity signature** (candidate clean diagnostic):

```text
|∂u / ∂a|       large
|∂d / ∂a|       small      (d = detector output)
∂V / ∂a         negative
∂U_adv / ∂a     positive
```

> Adversarial influence strongly affects action, weakly affects detection, harms defended value, improves adversary value.

---

## Capture surfaces (the taxonomy)

Five surfaces. Do **not** add more without genuine missing structure — taxonomy expansion is the spice-rack failure mode.

### 1. Sensor capture
$y'_t = C_y(h(x_t))$ — the system sees the wrong world.
Examples: poisoned telemetry, adversarial inputs, fake demand signals, missing scrape targets, synthetic sentiment, dashboards with sampling/aggregation artifacts.
> *The plant did not lie. The instrument translated reality into doctrine.*

### 2. Estimator capture
$b'_t = E'(b_{t-1}, y_t, u_{t-1})$ — signal may be valid; interpretation is wrong.
Examples: stale priors, biased classifiers, bad forecasting models, normalized failure in postmortems, interpretive frames that convert anomaly into "expected behavior."
> *The enemy need not falsify the signal if they can teach the estimator what it means.*

### 3. Objective capture
$J' \neq V$ — system optimizes the wrong target. Includes Goodhart / specification gaming, but is one surface, not the whole structure.
> *The army wins every battle listed on the wrong map.*

### 4. Admissibility capture *(the distinctive layer)*
$A'(b_t, u_t, \Gamma) = \text{true}$ — system approves action using corrupted authority conditions.
Examples: stale evidence authorizes irreversible action; advisory output treated as authorization; current prompt treated as durable standing; missing policy silently promoted to permission; self-certification accepted as evidence; green report treated as ground truth; scope/basis/standing laundered through procedural form.
> *The door did not fail. The credential became fictional.*

This is where agent-governor / Wicket / NQ / admissibility primitives plug in. See **Cross-corpus mapping** below.

### 5. Reporting capture
$m'_t = C_M(m_t)$, $\text{Detector}(m'_t)$ quiet — self-accounting remains coherent while reality diverges.
Examples: green dashboards during material decay; burndown chart healthy while product is not shipping; OKRs improving while defended value collapses; postmortems that preserve institutional self-image; metrics generated from captured belief rather than external state.
> *The report is not late to the disaster. The report is part of it.*

Probable Chronopolitics bridge: narrative-preserving feedback corruption.

---

## Properties (theorem-ish claims)

Labeled claims, Lean-friendly without theorem-prover tuxedo night yet:

- **Legitimacy Preservation Claim.** Captured loops can preserve internal validity signals.
- **Value Divergence Claim.** Internal legitimacy can increase while defended value decreases.
- **Speed-Amplification Claim.** If capture creates negative defended-value drift per iteration, faster loops accelerate damage. *(Anti-Boyd corollary: a fast OODA loop around false state is just high-frequency self-harm.)*
- **Witness Necessity Claim.** A loop whose detectors consume only captured reports cannot reliably detect capture.
- **Boundary Claim.** Direct actuator compromise is not loop capture; it is takeover. The classifications are disjoint.

---

## Nearby failures (drywall table)

This table is boring on purpose. It does the reviewer-sludge work.

| Failure type        | What happens                                  | Why not loop capture              |
| ------------------- | --------------------------------------------- | --------------------------------- |
| Actuator compromise | Attacker directly controls action             | Controller bypassed               |
| Outage              | System cannot act correctly                   | Legitimacy loop may fail too      |
| Deception           | False belief injected                         | May not produce authorized action |
| Goodhart            | Proxy becomes target                          | Only objective layer              |
| **Loop capture**    | Valid process drives adversary-serving action | Governance relation captured      |

---

## Case matrix (not full case studies yet)

Build the matrix before writing the cases. Prevents the haunted-airport failure mode.

| Domain                | Capture surface           | Internal legitimacy signal | Defended value degraded     |
| --------------------- | ------------------------- | -------------------------- | --------------------------- |
| SRE / dashboarding    | reporting                 | green dashboards           | reliability                 |
| agile theater         | reporting / objective     | burndown, velocity         | shipped utility             |
| recommender systems   | objective                 | engagement score           | user / social value         |
| agent tools           | admissibility             | "authorized" action        | operator intent / scope     |
| safety filtering      | estimator / admissibility | compliant output           | task correctness            |
| supply chain          | estimator                 | demand forecast            | inventory / capacity        |

---

## OODA relation

OODA mapped onto loop variables:

```text
Observe  → y_t
Orient   → b_t = E(...)
Decide   → π(b_t, J)
Act      → u_t
```

Loop capture attacks the interfaces:

```text
Observe  → corrupt y
Orient   → corrupt E
Decide   → corrupt J / A
Act      → let u remain authorized
```

**Important distinction.** OODA is often rendered as speed doctrine: cycle faster than the enemy. Loop capture says:

> *Tempo is downstream of epistemic integrity.*

**Anti-Boyd theorem candidate** (Speed-Amplification Claim, formal form):

If $\mathbb{E}[V(x_{t+1}) - V(x_t) \mid \text{captured loop}] < 0$, then reducing loop latency increases value-loss rate per wall-clock time.

> *Agility is safe only when orientation remains coupled to reality.*

---

## Boundaries / anti-sludge rules

Hard distinctions to prevent the paper becoming "everything is manipulation":

1. **Not actuator compromise.** Direct attacker control of the actuator is takeover.
2. **Not mere deception.** Deception may feed capture, but loop capture requires redirected self-authorized action.
3. **Not mere Goodhart.** Goodhart is objective/proxy capture only. Loop capture spans five surfaces.
4. **Not merely bad decision-making.** The decision may be locally valid; the validity regime is what has been captured.
5. **Not merely system failure.** In loop capture the system continues to function according to its own rules.

**Definition with boundaries baked in:**

> Loop capture is adversarial influence over a control system's internal conditions of valid action, causing the system to produce self-authorized behavior that degrades its defended objective while preserving internal legitimacy signals.

---

## Witness / defense concepts

Reject phrasing like "uncorrupted oracle." Use:

> *Independent witness.* A witness does not need perfect truth — it must fail differently.

Defense patterns:

- independent witness channels
- perturbation sensitivity analysis (does the witness respond to perturbations the captured channel misses?)
- defended-value vs reported-value divergence checks
- external measurement channels not co-captured
- receipt-gated authorization
- explicit standing / scope / basis checks
- refusal to authorize irreversible action from stale or captured evidence
- disagreement-preserving telemetry
- postmortems that audit the validity regime, not just component behavior

---

## Cross-corpus mapping

This is what makes loop capture a synthesis-shaped object rather than a standalone primitive. The corpus connections are dense.

### Connection to P22 (foundational failure geometry)

P22's four-layer decomposition (gauge / clock / estimation / actuation) is *already a capture-surface taxonomy in different vocabulary*.

*This mapping is not merely comparative; it is the main evidence for the open positioning question, because it shows which parts of Loop Capture are already latent in P22 and which parts are genuinely introduced by the admissibility/reporting layer.*

The mapping is roughly:

| Loop capture surface | P22 layer        | Notes                                                 |
| -------------------- | ---------------- | ----------------------------------------------------- |
| Sensor               | gauge            | Direct overlap                                        |
| Estimator            | estimation       | Direct overlap                                        |
| Objective            | (cross-cuts)     | P22 doesn't separate; loop capture does               |
| Admissibility        | (new surface)    | Loop capture's distinctive contribution               |
| Reporting            | (new surface)    | Loop capture's distinctive contribution               |
| —                    | clock            | P22 distinguishes; loop capture currently folds in    |
| —                    | actuation        | Loop capture treats actuator compromise as out-of-scope (boundary claim) |

The reframe question: does loop capture *extend* P22 by adding admissibility + reporting surfaces, or does P22's ratio analysis become a special case of loop capture's legitimacy/value divergence? Position decision pending.

### Connection to P25 (epistemic border control)

Loop capture is what happens when border control fails on the inbound side — when adversarial state crosses the boundary disguised as admissible evidence. P25's Theorem 1 (observation-equivalent states force policy-equivalence) is *exactly* the Witness Necessity Claim: if all detectors consume only captured reports, distinct true states map to indistinguishable internal traces.

### Connection to P27 (obligation-unsound reconciliation)

P27's *controller-correct, operator-unsound* is *exactly* sustained $L_t / V_t$ divergence. Loop capture names the adversarial mechanism by which P27's pattern becomes weaponized rather than emergent. P27 is the constructive closer for the non-adversarial case; loop capture extends to adversarial.

### Connection to admissibility family (six non-collapsible boundaries)

Admissibility capture (surface 4) is the adversarial extension of stale binding / zombie obligation / authority-debt. The non-adversarial primitives describe the shape; loop capture describes how the shape gets weaponized.

### Connection to WIF-composition

The Witness Necessity Claim is the WIF-composition probe's *audited failure-surface orthogonality* under adversarial conditions. The probe requires that witnesses fail independently under atomic perturbations; loop capture requires that at least one witness fail differently from the captured channel. Same doctrine, different framing. The probe's two-route discipline (corroborative composition vs aggregate-invariance composition) extends directly to the adversarial setting: corroboration requires non-co-captured witnesses; aggregate-invariance requires the aggregator itself to be uncaptured and invariant under admitted perturbations.

### Connection to Attack-Surface Laundering (discourse-layer cousin)

Gate-to-Metric Substitution — named in [primitives/attack-surface-laundering.md](primitives/attack-surface-laundering.md) — appears structurally adjacent to Loop Capture's admissibility-capture surface (surface 4 of the five-surface taxonomy). In both cases, a gate that should constrain action is reframed so continuation remains permissible:

- *Loop Capture admissibility capture* (controller layer) — the controller's internal admissibility predicate $A$ gets replaced by a captured $A'$; actions remain self-authorized while defended value decays.
- *Gate-to-Metric Substitution* (discourse layer) — the dispute's framing of an admissibility gate gets replaced by an optimization metric; actions remain in-progress while the violation gets "optimized" against continuous-variable harms.

Same shape, different scope. The Loop Capture working note's *Caveat on "dual"* applies identically here: the framing is conceptual, not earned formal duality. Treat as **discourse-layer cousin**, not as proven structural identity.

The Attack-Surface Laundering primitive's contribution to Loop Capture: where surfaces 1–5 describe how an internal control loop loses contact with reality, the discourse-layer cousin describes how *third-party accountability* against a captured loop can be redirected by the same shape of move, at a different scale, by good-faith actors with no malicious coordination.

### Connection to Lean machinery

The existing Lean kernel (Authority + StateTransition + Derivation + Execution + Corrective + WitnessInvariance, all in `~/git/lean/LeanProofs/Admissibility/`) covers most of the *admissibility capture* theorem already, in non-adversarial form:

- `AuthorizedStep` ("stale basis cannot bind at mutation layer") *is* the admissibility-capture boundary theorem for the non-adversarial case
- `EncapsulatedWrt` / `EncapsulatedWithinRegime` give the formal vocabulary for "captured channel = channel that moves under perturbations it claimed encapsulation against"
- `classify : Step → StepClassification` is the verdict surface where admissibility capture would surface as a misclassification

Generalizing to adversarial: introduce a capture transformation $C$ on the relevant predicates, prove that the classify verdict can preserve `Authorized` while the underlying step violates the uncaptured admissibility predicate. That's the *Admissibility Capture Theorem*; it's incremental on existing machinery, not from-scratch.

---

## Lean formalization strategy

Do **not** start with continuous control. Discrete and algebraic.

Possible Lean objects:

```lean
State
Observation
Belief
Objective
Admissibility
Action
Report
TrueValue
AdversaryUtility
GovernanceContext
```

Core predicates:

```lean
Authorized : Belief → Action → GovernanceContext → Prop
InternallyLegitimate : Loop → Prop
DefendedValueDecreases : Trace → Prop
AdversaryUtilityIncreases : Trace → Prop
Captured : Loop → Loop → Prop
```

Useful theorem targets, in rough priority order:

1. **Internal authorization does not imply defended-value preservation** (especially when internal objective differs from true defended value).
2. **Observation-equivalent states are indistinguishable inside the loop** without an independent witness. *(Lifts P25 Theorem 1.)*
3. **Captured objective makes locally rational action globally destructive.** Local minimization of $J'$ can monotonically degrade $V$.
4. **Reporting can remain green while defended value decreases**, if the report predicate consumes belief/report state rather than true state.
5. **Forced actuation is not loop capture.** Boundary theorem; classify direct actuator compromise as takeover.
6. **Admissibility Capture Theorem.** An action may satisfy captured $A'$ while violating uncaptured $A$. *Formalizes authorized wrongness.* Direct extension of `AuthorizedStep`.
7. **Independent Witness Theorem.** If all report/detector channels are functions of captured belief, capture may be internally undetectable. Detection requires at least one channel not co-captured by the same transformation. *Direct lift from WIF-composition's audited orthogonality.*
8. **Speed-Amplified Erosion.** Under negative drift per iteration, shorter cycle time increases wall-clock damage rate. *(May stay as paper math rather than Lean first pass.)*

---

## Paper structure candidate

*Note: under positioning option (3) — synthesis paper — the structure below shifts toward integrating P22/P25/P27 case studies under one frame rather than treating them as separate sections. Current outline is the standalone-paper version; revise on position decision.*

1. **Introduction: Victory Without Compromise.** Systems can be redirected without takeover. The threat is not broken controls, but captured validity conditions.
2. **Background.** Feedback control; OODA; reflexive control; Goodhart / specification gaming; adversarial ML / sensor attacks; organizational dashboards / metrics. *(Reflexive control gets prominent placement per prior-art posture.)*
3. **Definition: Loop Capture.** Formal definition; boundary against compromise, deception, Goodhart, and simple failure.
4. **Formal Model.** Discrete-time loop; capture transformations; internal legitimacy vs defended value; sensitivity signature.
5. **Capture Surfaces.** Five surfaces with examples and keepers.
6. **Properties.** Internal validity preservation; detector blindness; relative observability; speed-amplified erosion; witness necessity; self-authorized adversary-serving action.
7. **Case Studies.** Drawn from case matrix; selected for surface coverage rather than dramatic appeal.
8. **Defenses.** Independent witness architectures; receipt-gated authorization; external value checks; adversarial perturbation tests; validity-regime audits; reporting / evidence / authorization separation.
9. **Conclusion.** Boyd gives loop supremacy. Reflexive control gives strategic redirection. Loop capture gives the formal mechanism by which redirection remains internally legitimate.

---

## Aphorism bank

Use sparingly. Section openers and epigraphs only — they will try to take over otherwise.

Highest-priority:

> *The enemy does not seize the controls. The enemy edits the world in which the controls make sense.*

> *A witness need not be pure. It must fail differently.*

> *The report is not late to the disaster. The report is part of it.*

> *A fast OODA loop around false state is just high-frequency self-harm.*

> *Reflexive control explains how the enemy gets inside the decision frame. Loop capture explains how the captured frame continues to pass its own gates.*

Reserve bench:

> *The system remains internally valid while becoming externally wrong.*

> *A captured loop does not merely act wrongly. It explains itself correctly according to its captured frame.*

> *The plant did not lie. The instrument translated reality into doctrine.*

> *The door did not fail. The credential became fictional.*

> *Agility is safe only when orientation remains coupled to reality.*

> *The attacker does not need root if they can make the system's own root of trust point at fiction.*

> *Boyd gave us the shape of victory. Control-Theoretic Sun Tzu gives us the shape of its theft.*

---

## Filing notes

- Do **not** assign paper number until P25/P26/P27 cluster settles AND position question (a/b/c) decided.
- Do **not** expand the taxonomy to a sixth surface without genuine missing structure. The five are dangerously complete.
- Do **not** collapse loop capture into Goodhart in the prose. Goodhart is one surface (objective) of five.
- Do **not** overclaim novelty. The framing is *Western control-theoretic admissibility-layer formalization of the reflexive-control pattern*, not invention.
- Re-read this note when: P25/P26/P27 cluster settles; a forcing case appears (specific incident or paper that would benefit from formalized loop-capture vocabulary); the WIF-composition probe earns a Lean staging that the loop-capture work could ride; the admissibility family paper earns its sequence position.

---

## Provenance

- **2026-05-09 origin.** "Control-Theoretic Sun Tzu" thread surfaced loop capture as a serious paper candidate; multi-model brainstorm (operator + chatty + DeepSeek touched it) developed the formal skeleton, taxonomy, OODA relation, and aphorism bank.
- **chatty (zhuzh pass + prior-art sniff test).** Cut taxonomy expansion; added legitimacy/value divergence as formal heart; named *authorized wrongness* as central concept; added nearby-failures table and case matrix as sludge prophylaxis; quarantined aphorisms; identified reflexive control as the closest strategic prior art and the obvious Reviewer 2 ambush; wrote the prior-art and position boxes used verbatim above.
- **claude-code-papers (this file, 2026-05-10).** Folded chatty's draft into the working/ structure with the prior-art warning up front per operator instruction. Added cross-corpus mapping section connecting loop capture to P22 / P25 / P27 / admissibility family / WIF-composition / Lean kernel — the connections that suggest position (3) (synthesis paper). Marked status as rich-staging note (earns the density per note-subtypes discipline because it bridges multiple already-mature converging registers).
- Filed as working note, no paper number, position open. Not committed (per current cluster discipline). Companion entry added to [where-admissibility-fits-candidates.md](where-admissibility-fits-candidates.md) under paper candidates.
