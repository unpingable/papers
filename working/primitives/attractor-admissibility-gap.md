# Attractor-Admissibility Gap

*(working aliases: Stability ≠ Admissibility; Convergence Without Admissibility; Stable-but-Misplaced Equilibrium)*

**Status:** candidate
**Kind:** boundary condition (with transition flavor — the failure manifests as an interpretive transition from convergence-certificate to admissibility-certificate that was never licensed)
**Originated:** 2026-05-09 (user-side framing of "is the equilibrium well-placed?" as a question distinct from "is motion around the equilibrium stable?"; ChatGPT distillation through equilibrium-shift / parameter-dependence / region-of-attraction / attractor-quality framings; inadmissible-perch toy case as the seeding worked instance)
**Primary home (paper):** none yet. Candidate cross-pointers: P22 (failure-geometry — AAG surfaces in the estimation layer when the controller estimates around a stale or mispositioned reference), admissibility-control taxonomy, methodology essay on certificate scope.

## Aphorism (keepers)

> *A certificate of convergence is not a certificate of admissibility.*

> *Stability is a property of motion around a reference. It is not, by itself, a verdict on the reference.*

Cluster-master keeper (the certificate-scope theorem this primitive belongs to):

> *Stability certifies motion under a model; it does not certify the admissibility of the reference, the closure of the world, or the validity of any recovery path.*

> *A no-win scenario is often a theorem over a closed action surface, not a property of the world.*

Closure-caveat keepers (the symmetric pair):

> *Do not launder convergence into inevitability.*

> *Do not launder possibility into rescue.*

> *The light may be an oncoming dragon. But the tunnel may fork.*

Endogenous-recovery keepers:

> *Recovery is not proof against AAG. Recovery is another controller whose admissibility must be evaluated.*

> *The tunnel forks because the organism is partly made of tunnel-forking machinery.*

Survival-laundering keeper (the four-step chain — quadruple-laundering guardrail):

> *Escape is not the same as recovery; recovery is not the same as restoration; survival is not a retroactive authorization of the trap.*

Restoration-vs-healing keepers (engineered systems' rollback cheat):

> *Restoration is not recovery by healing; it is recovery by custody over prior state.*

> *A restore point is not a recovery certificate unless its provenance, scope, context, and obligations still hold.*

Toy-instance form:

> *A locally stable perch is not, on its own evidence, an admissible refuge.*

## Kernel

A stability / convergence certificate proves behavior **relative to a chosen equilibrium, attractor, or reference frame**. It does not, on its own, prove the equilibrium is itself admissible. A system can be **locally well-behaved** — perturbations decay, motion is bounded, the Lyapunov function does what it should — while the operating point, basin of attraction, or embedding has drifted into a region the operator would not consent to if asked.

The certificate is scope-bounded. The failure is scope-overreach: treating a convergence certificate as if it extended to admissibility of the reference. The system converges. It converges *to the wrong thing*.

The crime scene is not divergence. It is **stable convergence to an inadmissible attractor**.

## Formal-ish shape

Indexed by parameter / context $p$:

- $V_p(x)$ — Lyapunov function under context $p$
- $e(p)$ — equilibrium / attractor under context $p$
- $B(e(p))$ — basin of attraction
- $S$ — admissible region
- $x_0$ — initial condition

Stability claim:

$$\dot V_p(x) \le 0$$

— $V_p$ is non-increasing along trajectories, i.e., Lyapunov stability of $e(p)$. **Note:** $\dot V_p \le 0$ alone gives non-increase / Lyapunov stability, *not* asymptotic convergence to $e(p)$. Asymptotic convergence requires either strict decrease off the equilibrium ($\dot V_p < 0$ on $\{x \neq e(p)\}$) or an invariance argument (LaSalle's invariance principle: trajectories accumulate in the largest invariant subset of $\{x : \dot V_p(x) = 0\}$). The body text below sometimes uses "convergence" colloquially for "settles to the modeled attractor"; the underlying formal claim is whichever Lyapunov / invariance condition the system actually satisfies.

Admissibility claim (separate):

$$e(p) \in S$$

or stronger:

$$B(e(p)) \subseteq S$$

or, weakest acceptable:

$$\text{trajectory}(x_0) \subseteq S$$

The Attractor-Admissibility Gap is the failure mode:

$$\dot V_p \le 0 \quad \text{but} \quad e(p) \notin S \quad \text{(or } B(e(p)) \cap S^c \neq \emptyset \text{)}$$

— certified stability (or, where the stricter conditions hold, certified convergence) of an uncertified attractor.

## Four named cases

The gap manifests in four structurally distinct shapes. Naming them keeps the primitive from blob-collapsing:

1. **Stable bad attractor.** $e(p) \notin S$. The system converges beautifully to the wrong place. Cleanest version. Inadmissible-perch toy case; compliance-theater organization.
2. **Unsafe basin.** $e(p) \in S$ but $B(e(p)) \not\subseteq S$. Recovery exists; the route to recovery passes through inadmissible territory. Trajectory leaves $S$ before returning. Stability holds; admissibility doesn't, transiently.
3. **Context-shifted equilibrium.** $p \to p'$. The old Lyapunov certificate still "works" locally, but the reference has moved out from under it. Pendulum-on-accelerating-platform; AF 447's regime handoff. The certificate is *historically valid* and *currently inapplicable*.
4. **Certificate laundering.** *"It converges"* gets rhetorically laundered into *"it is acceptable."* The structural gap (1)–(3) is one thing; (4) is the **social transmission** of the gap — a narrow technical certificate spent as a broad authority claim. **This is the doctrinal payload.** Without (4), AAG would just be a control-theory caveat. With (4), it is a primitive about how scoped certificates get spent past their scope by operators, managers, and downstream consumers who never read the fine print.

Cases (1)–(3) are control-theoretic; (4) is the operator-side / institutional surface that makes (1)–(3) dangerous in practice. A clean instance of AAG can involve any one or any combination.

## Closure conditionality (and the dual laundering risk)

AAG as stated above is **closed-system by default**. The formal-ish shape assumes:

$$\dot x = f(x, p)$$

— fixed dynamics, fixed admissible region, fixed action surface, fixed boundary conditions. Real systems are usually more open:

$$\dot x = f(x, p, u, w, \eta)$$

where $u$ is internal/control action, $w$ is bounded disturbance, and $\eta$ is the **unmodeled-perturbation variable** — exogenous actor, accident, regime change, branch event, intervention, or coupling the model omitted. Closure is a modeling assumption, not a fact about the world.

This produces a **second laundering risk**, mirror-image of case (4):

| Direction | Misread | Fallacy |
|---|---|---|
| Comfort laundering | convergence-cert → admissibility-cert | *"It converges, therefore it's fine."* (Original AAG payload — case 4 above.) |
| Doom laundering | bad-attractor-cert → inevitability-cert | *"It converges to a bad attractor, therefore nothing can alter it."* (The closure-overreach mirror.) |

Doom laundering is the **closure assumption mistaken for a metaphysical claim**. A bad-attractor certificate says: *under the modeled dynamics and available internal controls, the attractor is bad.* It does not say: *the world contains no branching, intervention, rupture, accident, or regime change.* That stronger claim requires the model to capture all relevant interventions, couplings, and branch points — which closed-system stability proofs do not, by construction, do.

### Hope-as-control guardrail

The symmetry creates its own laundering hazard going the other way. Once you concede porosity, the temptation is to spend it:

> *"An external rescue is possible, therefore the present trajectory is admissible."*

This is the **hope-as-control fallacy** — the dual of doom laundering. Porosity does not authorize an inadmissible attractor unless the intervention itself has *standing, probability, latency, mechanism, or trigger* — i.e., unless the rescue is part of the modeled or governed action surface. Possibility is not a controller. Pointing at unbounded porosity to justify a bad plan is changing the rules without modeling the rule-change mechanism.

### Endogenous recovery: the third source of basin-change

Living, engineered, and organizational systems often contain internal repair / regeneration / supervisory controllers above the original control surface $u$. Further-extended formal:

$$\dot x = f(x, p, u, w, \eta, c_1, c_2, \ldots, r)$$

where $c_i$ are nested higher-order controllers and $r$ is repair / regeneration capacity. The closure assumption is loosened a second time: not only can $\eta$ disturb from outside, but the system's own higher-order controllers can alter trajectory, basin, or attractor in ways the base dynamics $f(x, p, u)$ do not capture.

Examples:

- **Biology:** immune response, clotting, fever, sleep, wound healing, apoptosis, autophagy, microbiome shifts.
- **Engineering / informational:** watchdogs, self-test, supervisor controllers, snapshots, replicas, failover, reconstruction from declarative config, replacement.
- **Organizational:** postmortems, escalation paths, incident commanders, succession, replacement of personnel.

But endogenous recovery is **another controller, not magic.** It has scope, latency, cost, failure modes, and pathological overreach. *A bad-attractor certificate that ignores recovery controllers is over-pessimistic; a recovery argument that does not audit the recovery controller is over-optimistic.* Both are AAG-shaped scope errors.

### Recovery typology (two orthogonal axes)

**Outcome axis** — what kind of state the system reaches after recovery:

| Outcome | What it means |
|---|---|
| Restorative | Returns to prior admissible basin. |
| Compensatory | Reaches a *new* admissible basin with degraded capacity. |
| Sacrificial | Survives by burning structure / capability / standing. |
| Pathological | The recovery controller becomes the new harm. |

**Mechanism axis** — how recovery is achieved:

| Mechanism | What it is |
|---|---|
| Endogenous repair | System's internal repair / regeneration controllers. (Biology-style; immune, clotting, regrowth.) |
| Sacrificial escape | Exit by losing capability. (Animal gnaws off leg; immune kills tissue; layoff to save firm.) |
| External intervention | Exogenous actor moves the metronome. (The $\eta$ variable.) |
| Restorative rollback | Prior known-good state reloaded. (Snapshot, restore, revert, re-image, replay, failover.) |
| Reconstruction | Rebuild from source / spec / receipts rather than from prior runtime state. (Declarative config; rebuild from event log; rebuild from blueprint.) |
| Replacement | Abandon the instance; preserve function elsewhere. (New unit; new tenant; succession.) |

The two axes are **orthogonal**. A rollback (mechanism) can produce a restorative outcome (clean restore) or a pathological outcome (rollback to a contaminated snapshot). Naming both axes lets the analyst say *what was achieved* and *how* without conflating them.

**Allostasis as an explicit subcase.** Biology often uses *allostasis* (operating-point shift to survive) rather than *homeostasis* (return to prior baseline). Allostasis is structurally a compensatory recovery via endogenous repair — and it is itself an AAG-shaped move when the new operating point is inadmissible. *"Return to baseline"* and *"regain admissible function"* are not always the same target.

### Rollback-specific failure modes (the engineered cheat with its own laundering risk)

Rollback / restoration is largely unique to engineered and informational systems — biology mostly cannot do it. But each rollback class has its own failure surface:

- **Snapshot already contaminated.** The known-good basis was already bad at snapshot time.
- **Backup missing external dependencies.** Restored state assumes context that no longer holds.
- **State internally valid, context-invalid.** The restore is consistent on its own but inconsistent with the world it now lives in.
- **Event replay reproduces the bad trajectory.** The log replays the same path that produced the failure.
- **Rollback destroys post-snapshot obligations.** Receipts, commitments, or external state that accumulated after the snapshot cannot be undone.
- **Replica has the same hidden fault.** Failover to an identically-broken instance.
- **"Known good" means "last time we checked."** Provenance gap between snapshot and current admissibility verdict.

Unifying claim: *restoration is custody over prior state, not healing; rollback is not a recovery certificate.*

### The certificate-scope cluster

Putting it together, the structural family AAG belongs to is a **five-clause certificate-scope cluster.** Each clause is a separately-issued certificate whose scope can launder in either direction (false comfort or false doom):

1. **Convergence ≠ admissibility.** A stable basin can be outside the valid operating region. *(AAG proper.)*
2. **Bad attractor ≠ inevitability.** A bad-attractor certificate binds the closed/modeled system, not the world. Porosity matters.
3. **Porosity ≠ authorization.** External rescue does not justify continuing toward a bad attractor unless the intervention is modeled, available, bounded, or governed. *(Hope-as-control fallacy.)*
4. **Escape ≠ recovery.** Sacrificial survival (limb, tissue, structure, standing) exits the trap but does not restore the system.
5. **Restoration ≠ valid recovery.** Rollback / snapshot / rebuild only counts when the restore basis has provenance, scope, context validity, and obligation continuity.

Each clause is necessary; none subsumes the others. (1) without (2) over-claims; (1)+(2) without (3) becomes hope-as-control; (1)+(2)+(3) without (4) lets sacrificial survival pass as recovery; (1)+(2)+(3)+(4) without (5) lets rollback pass as recovery. The cluster is what AAG is *part of*; AAG is the headline clause.

### Nearby formal handles for the open-system extension

- **Input-to-state stability** — how bounded external inputs affect stability.
- **Robust stability** — whether stability survives perturbations / uncertainty.
- **Hybrid systems / impact maps** — pendulum hits wall, state jumps, dynamics switch.
- **Viability / controlled invariance** — whether a system can be kept inside an acceptable set given controls *and* disturbances.
- **Reachability** — what states can be reached if external inputs are allowed.
- **Stochastic stability / rare events** — freak occurrence rights the capsized ship.
- **Open-world model error** — the real system has couplings the model omitted.

These are the toolkit for moving an AAG analysis from closed-system framing to open-system framing without losing scope discipline. Each gives a different way to say *"intervention is part of the model"* with bounds attached.

## Failure predicate

AAG occurs when:

1. A stability / convergence certificate exists for the system relative to attractor $e(p)$.
2. The attractor itself is not in the admissible region (or its basin overlaps inadmissible regions in a way that the trajectory enters or settles outside $S$).
3. The certificate is treated by the operator (or a downstream consumer) as if it covered admissibility, not just convergence.
4. The certified motion proceeds — toward the inadmissible attractor — without the gap being announced or audited.

(1)+(2)+(3) is the structural gap. (4) is the operational consequence. All four are required for the primitive to bite. (1)+(2) without (3) is just a known-but-acknowledged operating-point question. (3) without (1)+(2) is just operator confusion about what the certificate covers.

## Diagnostic test (operator-facing)

1. **Was the equilibrium / reference / operating point validated separately from the convergence proof?** If the only artifact is a stability certificate, admissibility was not checked.
2. **Did the equilibrium shift?** Parameter, regime, frame, or context changes shift $e(p)$. If the certificate was issued before the shift and not re-issued, AAG is the verdict.
3. **Does the basin of attraction overlap the inadmissible region?** Even if $e(p) \in S$, $B(e(p)) \cap S^c \neq \emptyset$ means trajectories from some initial conditions land outside admissibility. Convergence covers behavior; admissibility covers reachability.
4. **Counterfactual reference-swap.** Would a competent operator, given the certificate, judge that they would *consent to the system converging to this reference*? If no, the certificate is being read past its scope.
5. **Closed- or open-system framing?** A bad-attractor verdict in a closed model is conditional on closure. Has the open-system extension been examined — external interventions and endogenous recovery controllers?
6. **If recovery is being invoked, has the recovery mechanism been audited?** Outcome (restorative / compensatory / sacrificial / pathological) and mechanism (endogenous / sacrificial / intervention / rollback / reconstruction / replacement) both need naming. Survival is not retroactive authorization; rollback is not a recovery certificate without provenance, scope, context, and obligation continuity.

## Worked instances

**Inadmissible-perch toy case.** A small mobile system settles into a locally stable position on a larger object that is not itself an admissible refuge — the larger object will move, has hostile surfaces, or otherwise lies outside the smaller system's intended habitat. Local stability of occupation is real and certifiable; admissibility of the occupied state is a separate question, and unlicensed under the convergence certificate alone. The toy case is intentionally low-stakes: its job is to make the certificate-scope distinction crisp before scaling to high-stakes instances.

**Pendulum on accelerating platform (control-theory canonical).** A pendulum in an accelerating room aligns with **effective gravity** $\mathbf{g}_{\text{eff}} = \mathbf{g} - \mathbf{a}_{\text{room}}$, not inertial gravity. Stability around the new equilibrium is fully valid; the natural frequency $\omega_0 = \sqrt{g_{\text{eff}} / L}$ is correct. But if the operator wanted "hang straight down relative to inertial gravity" or "hang straight down relative to the room with the room at rest," the locally-stable equilibrium is mispositioned. The certificate is valid for the wrong reference.

**Goodhart-shape control loop.** A controller drives a measured proxy $M$ to its target $M^*$ with a clean stability certificate. If $M$ has displaced from the operator's actual goal $G$, the system is converging stably around $M^*$ — which is not the equilibrium the operator would consent to. Distinct from Goodhart-as-feedback-loop: AAG can occur in a single shot, without iterated optimization pressure. The certificate-scope misread is the mechanism, not the optimization-pressure feedback.

**Org-level: stable dysfunction.** An organization with a stable equilibrium around compliance theater. Perturbations (audits, reorgs, leadership changes) get absorbed; the system returns to the same compliance-theater attractor. Lyapunov-shape stability is real. The equilibrium itself is inadmissible from the operator's actual-goal frame, but anyone who only inspects the convergence behavior will see a well-regulated system.

**Aviation / regime-switching: AF 447 (2009).** Aircraft entered "alternate law" after airspeed sensor failure. Within alternate law, the controller's local dynamics were stable. The pilots' mental model was still "normal law" — they were reading the local-stability behavior as if the regime-admissibility had not changed. Stability certificate held within the new regime; admissibility of operating in that regime under those crew-procedural assumptions did not. AAG at the regime-handoff seam.

## Adjacency map

- **Witness Invariance Failure.** Direct sibling on the certificate-misreading axis. WIF: sensitivity certificate misread as independence certificate (sensitivity → independence is the unlicensed transition). AAG: convergence certificate misread as admissibility certificate (convergence → admissibility is the unlicensed transition). Same shape, different domain. *If a "Certificate-Scope Misread" family ever earns its own meta-entry, WIF and AAG are its two charter members.*
- **Trajectory-Actuator Gap.** Naming-parallel and conceptually adjacent. TAG: observed historical trajectory mistaken for available control surface. AAG: stable basin of attraction mistaken for admissible operating region. Both are *thing-in-one-frame* read as *authorization-in-another-frame*; different frames (history → control vs convergence → admissibility), same shape.
- **The certificate-laundering family (WIF / AAG / TAG together).** Cross-primitive thesis worth pinning explicitly: *a narrow technical certificate says one scoped thing; the operator / social / managerial layer spends it as a broader authority claim.* WIF, AAG, and TAG are three instances of this family on three different certificate types (witnessing / convergence / trajectory). The family pattern is: **scoped artifact → unscoped authority transfer**, with the transfer typically silent. If a meta-primitive ever earns the name *Certificate-Scope Laundering* or similar, these three are the charter members and case (4) of AAG (certificate laundering) is the central mechanism.
- **Design-Basis Erasure.** Adjacent. DBE: a controller is imported without its hazard model. AAG: a certificate is read as covering scope its issuance never licensed. DBE is at the controller-import layer; AAG is at the certificate-interpretation layer. They can compose: a certificate imported without its scope context is the AAG-via-DBE pathway.
- **P22 (failure geometry across gauge / clock / estimation / actuation).** AAG surfaces in the estimation-and-reference layers when the controller is regulating around a stale, mispositioned, or inadmissible equilibrium. Specifically: when the gauge is healthy, the clock is healthy, but the *reference* embedded in the estimator has drifted out of admissibility, P22's four-layer decomposition flags the seam where AAG lives.
- **Goodhart's law.** Distinct mechanism. Goodhart is iterated optimization pressure on a proxy. AAG is a one-shot or persistent certificate-scope misread; no optimization pressure required. AAG can produce Goodhart-shaped failures (stable convergence around a displaced metric) without the feedback loop that Goodhart names.
- **"Stability is not authorization" doctrine.** AAG is the formal-certificate cousin of the admissibility-family slogan. The doctrine is the operating principle; AAG is the named gap that makes the slogan load-bearing — *the certificate is what the slogan is warning you not to misread.*
- **Coherent wrongness (corpus motif).** Distant cousin. Coherent wrongness is internal-consistency-as-cover-for-error. AAG is local-validity-as-cover-for-global-misplacement. Both are surface-validity masking deeper failure; different mechanisms.

## Do not confuse with

- **Lyapunov instability.** That is the system *not* converging. AAG presupposes the system *does* converge — just to the wrong thing. The whole nasty point.
- **Modeling error.** A wrong model produces a wrong certificate. AAG can occur with a *correct* certificate whose scope is being overread. The certificate may be entirely valid.
- **Goodhart's law.** Goodhart is iterated feedback-driven proxy optimization. AAG is certificate-scope misread; no iteration or optimization pressure required.
- **Robustness failure.** Robustness asks: *does the certificate hold under perturbation?* AAG asks: *does the certificate, even when it holds, mean what we think it means?* Different question, different layer.
- **Witness Invariance Failure.** Sibling, not duplicate. WIF is about evidence/witnessing; AAG is about control/convergence. Same family of certificate-misreads, different domains.
- **Operating-point ambiguity.** If the operating point was honestly unclear and the operator flagged it, that is open-question state, not AAG. AAG requires the certificate to be *treated as if* it had answered the admissibility question.

## Three-layer guardrail (anti-universal-acid)

Not every system that converges to something we don't like is AAG:

1. **Honest scoped certificate.** Certificate is explicitly scoped to convergence relative to a stated reference; operator separately validates the reference against admissibility. Both checks pass. No AAG.
2. **Certificate-scope ambiguity.** Certificate's scope is unclear; operator either flags the ambiguity (recoverable) or overreads it (the failure pathway). Recoverable cases are *adjacent* to AAG, not yet AAG.
3. **AAG proper.** Certificate is valid within scope; operator (or downstream consumer) reads it as covering admissibility; system converges stably to an inadmissible attractor; the gap is undisclosed.

Diagnostic discipline: before invoking AAG, rule out (a) "the certificate was actually wrong" (modeling error), (b) "the certificate was honestly ambiguous and someone clarified" (recoverable), and (c) "the certificate held but admissibility was independently validated" (no gap). The primitive earns its keep when the certificate is valid, the reference is inadmissible, and the certificate is being treated as if it had cleared the reference.

## Architectural rules

- **Stability certificates must be paired with operating-point validation.** Two artifacts, not one. Their composition is what licenses operation; neither alone does.
- **Scope must be explicit on the face of the certificate.** *What* is being certified, *relative to what*, under *what context*. A certificate that does not state its reference is structurally inviting AAG.
- **Reference changes require re-issuance.** Parameter, regime, frame, or context shifts move $e(p)$. The old certificate does not transfer.
- **Audit the basin-region containment, not just convergence.** *Does $B(e(p)) \subseteq S$?* is the load-bearing question for safety; *does $\dot V_p \le 0$?* is the load-bearing question for stability. They are different questions and require different artifacts.
- **Recovery is itself a controller.** Any recovery argument must audit the recovery mechanism for scope, latency, cost, failure modes, and pathological overreach. *"Has a recovery controller"* is not the same as *"recovery is admissible."*
- **Restoration requires custody, not just presence, of basis.** A restore point's admissibility depends on provenance, scope, context validity, and obligation continuity. Rollback to a contaminated snapshot is rollback laundering, not recovery.
- **Name the recovery on both axes.** Outcome (restorative / compensatory / sacrificial / pathological) and mechanism (endogenous / sacrificial / intervention / rollback / reconstruction / replacement) are orthogonal. Conflating them lets sacrificial survival pass as restoration.

## Lean / formal status

No Lean module yet. The cleanest formal hook would compose with existing admissibility kernels:

```
StabilityCertificate(system, e, p) ∧ ¬AdmissibleAttractor(e, S) → ScopeMismatch
B(e) ⊄ S → AdmissibilityFailure  (independent of stability around e)
```

Structurally close to: WIF's invariance-vs-sensitivity formal split (where the certificate of one property is being misread as a certificate of another). If both ever land in Lean, they likely co-locate under a `CertificateScope/` family rather than each starting a separate directory. Not staged; probe-grade only.

## Used by

Cross-cutting. No paper currently treats this as load-bearing. Candidate cross-pointers:

- **P22 (failure-geometry keystone).** AAG is the named gap that surfaces at the estimation-and-reference seam in the four-layer decomposition. When all four layers (gauge / clock / estimation / actuation) are individually healthy but the reference embedded in estimation has drifted out of admissibility, AAG is the diagnostic.
- **Admissibility-family papers.** AAG is the formal-certificate sibling to "stability is not authorization." If a future admissibility-family meta-paper consolidates the doctrine, AAG belongs in its taxonomy.
- **Methodology / certificate-scope work.** Pairs naturally with WIF as a two-instance demonstration that *scoped certificates require operator-side scope discipline.* Could anchor a methodology section on certificate hygiene.
- **P25 (epistemic border control).** Adjacent. P25's policy core regulates around an observation-equivalence class; AAG could surface as the failure where a policy is locally stable around an observationally-equivalent class but the class itself is inadmissible. Worth a one-line cross-reference if P25 drafts.

## Promotion guardrail (candidate → working)

Hold as candidate until at least one of:

1. A non-control-theory worked instance from a substantively different domain (cognitive, institutional, linguistic, biological) earns the substrate-general claim. Inadmissible-perch + pendulum + AF 447 + compliance-theater currently span animal-behavior / mechanical / aviation / institutional, but all four lean control-theory in shape. A cleanly non-control-shaped instance would be worth more than a fifth control instance.
2. A paper-side citation slot uses one of the keeper aphorisms in prose, with the primitive cited rather than dragged.
3. A live diagnostic case where naming AAG routes the fix (operator separates the two artifacts; admissibility audit gets done; gap closes).

Until any of those land, the keeper stays in primitives, not in main doctrine.

## Provenance

- **2026-05-09 origin.** User-side question separating "is motion around this equilibrium stable?" from "is the equilibrium itself well-placed?"; explicit naming of the second question as the load-bearing one.
- **Multi-model lineage:**
  - **ChatGPT:** equilibrium-shift / operating-point-shift framing, parameter-dependent stability, region of attraction / viability kernel, attractor quality, formal hooks ($V_p$, $e(p)$, $B(e(p))$, $S$), toy-instance aphorism, "boundary/certificate distinction first, not a new kingdom" disposition.
  - **user:** original "is the equilibrium well-placed?" framing as distinct from local stability; inadmissible-perch toy case (locally observed); "do it as probe" decision.
  - **claude-code-papers:** this primitive entry, naming as Attractor-Admissibility Gap (parallel to Trajectory-Actuator Gap), boundary-condition-with-transition-flavor kind classification, slot-in-constellation (WIF as direct sibling, TAG / DBE / P22 as adjacencies), formal-status assessment.
- **2026-05-09 follow-up.** User-side sharpening through ChatGPT: explicit four-named-cases enumeration; **certificate laundering named as the doctrinal payload** (case 4) — without it, AAG is a control-theory caveat; with it, AAG is a primitive about social/managerial transmission of scoped certificates as unscoped authority claims; cross-primitive family thesis pinned (WIF / AAG / TAG share the *scoped artifact → unscoped authority transfer* shape). Folded back into Four named cases section and Adjacency map.
- **2026-05-09 closure-and-recovery extension.** Several rounds of sharpening, in order:
  - **Closure caveat** (ChatGPT): AAG is closed-system by default; second laundering risk is *doom laundering* (bad-attractor cert misread as inevitability); hope-as-control fallacy is the dual guardrail.
  - **Endogenous recovery** (ChatGPT, biology-prompted): living/engineered systems contain higher-order repair controllers $c_1, \ldots, r$; recovery is itself a controller and must be evaluated for admissibility; pathological-recovery cases (autoimmune, chronic inflammation, stroke-from-clotting) demonstrate the failure mode.
  - **Outcome axis of recovery** (ChatGPT, basin-escape-as-irreversible-loss): four-mode taxonomy — restorative / compensatory / sacrificial / pathological. Survival-laundering keeper: *"escape ≠ recovery; recovery ≠ restoration; survival is not a retroactive authorization of the trap."*
  - **Mechanism axis of recovery** (ChatGPT, engineered-systems extension): six-mode taxonomy — endogenous repair / sacrificial escape / external intervention / restorative rollback / reconstruction / replacement; rollback-specific failure modes; "restoration is custody over prior state, not healing."
  - **Five-clause certificate-scope cluster** (ChatGPT, consolidation move): AAG is clause (1) of a five-clause cluster; cluster master keeper *"stability certifies motion under a model; recovery certifies an admissible path out of that model's failure regime; neither certifies the world contains no other branches"*; sharper version *"a no-win scenario is often a theorem over a closed action surface, not a property of the world."* Folded into Closure conditionality and aphorism sections.
- Filed candidate / default-density per `feedback-note-density-subtypes.md` — but with the certificate-scope cluster gestating inside, this entry has crossed into rich-staging by virtue of bridging control theory + biology + engineered/informational + organizational substrates with converging vocabulary. Not promoted. No Lean formalization staged.
