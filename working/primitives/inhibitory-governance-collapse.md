# Inhibitory Governance Collapse

**Status:** active primitive (recurrence ratifies — cron, Kubernetes reconciliation, auto-remediation, alert routing, agent plans, and organizational routines all instantiate it; not speculative)
**Originated:** 2026-05-01 (multi-model synthesis with chatty + claude-code; the failure mode itself is older and well-documented across control theory and ops literature, but not previously named on this shelf)
**Primary home:** no current paper home — operational / control-loop primitive. Closest adjacencies: P23 (non-self-identical controller / controller continuity lane) and P27 (obligation-unsound reconciliation, where one of P27's K8s examples is essentially this primitive)
**Shelf:** system primitive, sibling to `stale-binding.md`, `stale-task-replay.md`, `design-basis-erasure.md`, `role-accretion.md`, `apprenticeship-substrate-erosion.md`. Distinct from meta-doctrine primitives like `preemptive-naming.md`

**Aliases:**
- *GO/NOGO Collapse* — control-systems / aerospace register; emphasizes the missing inhibitory pole.
- *Propulsive Agency* — sharper but uglier; emphasizes that the system has propulsion without steering.

File under the main name. Aliases are alternative slogans, not separate primitives.

## Keeper

> Execution without inhibition is not agency. It is momentum with permissions.

Alternates worth keeping in reserve:

> The test of agency is not whether it can act, but whether it can stop acting when the premise rots.

> A control loop without a NOGO path is not autonomous; it is unattended propulsion.

## Working definition

A system retains the ability to execute learned or declared routines while losing, bypassing, or failing to install the ability to inhibit, revise, or abort those routines when conditions change.

## Failure predicate

Inhibitory Governance Collapse is in play when:

> Continued execution remains operationally available after the system has lost, bypassed, or degraded the capacity to detect premise invalidation and halt or revise the action.

The diagnostic mark: from the outside, behavior looks coherent because routines are still intact. The artifact each routine emits passes review. What has broken is not execution; it is the path by which execution can be interrupted, redirected, or aborted when the premise that justified it no longer holds.

## Mechanism

Canonical sequence:

1. A routine exists with a triggering condition and an execution path.
2. Trigger fires.
3. System executes.
4. Environment changes, threat appears, premise decays, or signal contradicts the in-flight action.
5. System lacks an adequate inhibition / NOGO path — either it was never installed, was bypassed for throughput, or has degraded to vestigial.
6. Execution continues, because *continue* is operationally cheaper than *re-evaluate*.
7. Behavior remains coherent on inspection — the routine is structurally intact, the artifacts look right.
8. Agency has collapsed into momentum. The system is propelled, not governed.

The key step is 5–6: the inhibitory capacity is the load-bearing object, and once it is missing, the cost asymmetry between *continue* and *re-evaluate* selects continue every time.

## Diagnostics

Two questions that locate the primitive:

> What stops this action once it has begun?

If the answer is *nothing unless a human notices*, the primitive is in play.

> Can the system distinguish *continue routine* from *the premise that justified this routine is gone*?

If the answer is *no, or only with significant added latency*, the primitive is in play.

The diagnostic is not "did the system make a bad decision." Bad decisions can be made by systems with intact inhibition. The diagnostic is specifically about the *stop path* — its presence, its latency, its bypass conditions, its degradation under load.

### Executive-system diagnostic battery (organizational register; generalizable)

Every command system has a threshold where routine delegation should stop and direct judgment should re-enter. Concealed incapacity is the failure mode where that threshold is submerged until no sharp signal reaches actual command — the system continues to emit command-shaped outputs while the stop / revise / rebind path becomes inaccessible or untestable. This is Inhibitory Governance Collapse expressed at the executive layer: routines persist, signatures land, statements ship; what is missing is the working feedback loop between apex judgment and the machinery underneath.

The battery operationalizes the two questions above (*what stops this action*, *can the system distinguish continue-routine from premise-gone*) as five observable pressure tests. Stated in executive / organizational register; the same shape generalizes — to agent loops (what forces plan interruption?), Kubernetes and other control loops (what escapes reconciliation and demands operator judgment?), and AI agents (what breaks routine continuation and triggers re-authorization?). The translations differ by surface; the load-bearing object — *can a non-routine signal still reach a judgment surface that can override the machinery* — is the same.

**1. Reversibility test.** Can the apex actually override a recent, consequential subordinate decision and produce rapid, measurable re-alignment? Legitimate delegation is leased, not gifted: the principal can revoke. Concealed incapacity fails the test — the counter-command either cannot be issued coherently or is silently re-interpreted into a stylistic suggestion that gets ignored.

**2. Unscripted interrogation.** Can the apex meaningfully discuss the rationale, trade-offs, and details of a delegated domain when pulled out of script? Legitimate delegation preserves a working model in the delegator's head; concealed incapacity fragments under unscripted pressure and routes the question back to a deputy.

**3. Accountability trace.** Can the apex personally explain why a particular course was chosen over alternatives — exposing the deliberative process in a way that is electorally, reputationally, or personally answerable? Legitimate delegation has a recoverable signature moment; concealed incapacity has only retrospective narrative attached to artifacts the apex did not actually decide.

**4. Crisis concentration.** Under genuine non-routine stress, does the apex's presence become operationally denser or visibly superfluous? Legitimate delegation systems condense command back to the top under crisis; concealed incapacity systems keep producing speeches and statements while real coordination happens elsewhere ad hoc.

**5. Delegation waterline.** Every system has a threshold below which delegation is genuine and above which the apex must personally engage. Legitimate delegation keeps that waterline visible and movable — the apex can decide *on this issue I need raw data before anyone acts.* Concealed incapacity submerges the waterline: handlers and pre-digestion ensure no issue requiring undiluted personal cognition ever reaches the top, while ritual outputs continue to fill the verification gap.

The waterline test is the keeper of the battery. It generalizes most cleanly across registers: in every command system, ask *what threshold lets a non-routine signal reach actual judgment, and is that threshold honest about its own height.*

Battery keeper:

> The difference between delegation and concealed incapacity is whether non-routine pressure can still summon real command from the top.

These tests do not turn *is command still real* into vibes about decline. They turn it into observable pressure events — reversal attempts, unscripted questions, accountability moments, crises, and waterline transgressions — whose results are legible whether or not the legitimating performance is intact.

## Distinguishing from neighbors

| Neighbor | What it names | Distinction |
|---|---|---|
| **Stale binding** | the authority/intent binding persists past validity | adjacent — stale binding describes *why* the routine still has standing to execute; inhibitory governance collapse describes the *missing stop path* once execution is in flight |
| **Stale-task replay** | task remains active in plan-space after world satisfied or changed it | sibling on the agent-side — stale-task replay is about *initiation* against a changed world; inhibitory governance collapse is about *not stopping* once initiated. The "did the replay contain a reality check" predicate from stale-task replay is a special case of "what stops this action" |
| **Design-basis erasure** | the controller no longer knows the wound it was designed around | upstream cause — when the design basis is erased, one of the things that erodes is the inhibition criteria, because inhibition often encoded the original hazard model |
| **Obligation-unsound reconciliation (P27)** | controller correct relative to declared state but wrong relative to operator consequence | sibling — P27's failure mode includes one of this primitive's clearest examples (k8s reconciles toward stale desired state). P27 frames it via obligation accounting; this primitive frames it via missing NOGO. Same animal, different vocabulary |
| **Role accretion** | system or person keeps acting from accumulated role after scope changed | downstream consequence — role accretion is one of the ways inhibitory governance collapse expresses at the human layer (the senior keeps adjudicating cases the role no longer covers because nothing has retired the role's executable surface) |

The distinguishing object is specifically *inhibition* — halt, interrupt, revise, abort. The other primitives may share mechanism components, but only this one names the missing stop-path as the load-bearing failure.

## Examples

- **`cron` / scheduled jobs.** Job runs on schedule; the assumption that justified it expired three months ago; nothing in the cron path checks the assumption. The job runs anyway, often producing artifacts that downstream consumers treat as authoritative.
- **Auto-remediation.** Remediation routine triggers on a symptom; the symptom shape is now produced by a different cause; the remediation does the wrong thing repeatedly because the trigger-to-action binding has no premise validation.
- **Kubernetes reconciliation.** Controller observes drift between observed and desired state and reconciles toward desired. Desired-state record has gone stupid (was authored under a condition that no longer holds, or was authored by a process whose authority has lapsed). Reconciliation continues; the cluster is now authoritatively wrong. (Same animal as P27's "controller-correct, operator-unsound.")
- **Alert routing.** Alert fires; routing escalates per matrix; incident context has changed (e.g. underlying system is intentionally being modified, or the alert is responding to a planned action). Escalation continues mechanically.
- **LLM agent multi-step plans.** Plan has steps 1–5. Step 2's output invalidates the premise of step 3. Agent does not have a "halt and re-plan" capability that fires on premise change; agent proceeds to step 3.
- **Organizational routines.** Leader delivers a cached riff to a question whose substance has shifted; the stimulus-response layer still works. Committee continues approving decisions in a category that no longer maps to current operating reality. Quarterly reviews continue producing the artifact even after the artifact has stopped being read.

These are not exhaustive. The primitive applies wherever there is a routine, a trigger, an execution path, *and* the absence of a structurally separate inhibition path with its own access to current state.

## Relation to today's corrective monotonicity work

Adjacent but not identical. Today's Lean kernel (`LeanProofs/Admissibility/Corrective.lean`) and the working note `working/admissible-recovery-semantics.md` are about *recovery* transitions: after a failure has occurred, the corrective transitions that respond cannot mint authority off the failed basis. That primitive operates at the *recovery boundary*.

This primitive operates at the *in-flight execution surface*. The failure is not about post-failure authority laundering; it is about pre-failure inhibition being absent so that the routine continues *into* failure rather than halting at premise invalidation.

Both turn on the same underlying object — *premise validation under change* — but at different phases. Corrective monotonicity says: when you handle a failure, do not laund er. Inhibitory Governance Collapse says: do not arrive at the failure in the first place because your routine could not stop. The first is a recovery discipline; the second is a control-surface discipline.

The mechanism analog is real but should not be over-claimed. They are complementary primitives addressing different phases of the same control-system pathology, not redundant restatements.

## Open questions

- **Mitigation shape.** Installing a NOGO path is not free — every separate inhibition surface adds latency, complexity, and its own failure modes. The honest mitigation is not "always have a stop path"; it is "the inhibition surface should be at least as well-installed as the execution surface, and degrade no faster." How to operationalize that asymmetrically across cron / k8s / auto-remediation / agent plans is genuinely open.
- **Detection vs prevention.** As with stale-task replay, the primitive admits a diagnostic version (catch routines that lack stop paths) and a constraint version (refuse to install routines without one). The constraint version is heavy; the diagnostic version is more deployable. Both have a place.
- **Connection to the Δt framework.** The primitive feels like an instantiation of "buffer / serialization / domain-break" geometry from the falsification-guardrails register, but at the agent / control-loop level rather than the substrate level. Whether the framework's vocabulary is the right home for it is open; for now it lives here as a working primitive.
- **Whether this graduates into a paper claim.** Currently a primitive, no paper home. P27 is the closest adjacency (and the K8s example overlaps directly), but P27's spine is obligation accounting, not inhibition. If a paper ever wants to argue specifically about the missing NOGO path as the load-bearing failure, this primitive becomes a candidate kernel. Until then, working primitive is the right level.
