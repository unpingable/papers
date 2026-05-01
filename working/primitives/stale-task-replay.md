# Stale-Task Replay

**Status:** active primitive (graduated 2026-05-01 by user override on operational-recurrence grounds; chatty's "wait for 2–3 confirmations" gate explicitly overruled — the world has already peer-reviewed it)
**Originated:** 2026-05-01 (user identification mid-session; multi-model synthesis with chatty + claude-code)
**Primary home:** no current paper home — operational/cognitive primitive; closest adjacency is P23 (non-self-identical controller / hidden compensation lane) where stale-task replay is one mechanism producing latent operator load. May also instantiate as an example in any future agent-side admissibility paper.

## Working definition

A previously valid task remains active in plan-space after the world has already changed or satisfied the observation that opened it, causing action to be prepared or taken against a no-longer-open problem.

## Compact laws

> Open in memory is not the same as open in reality.

> A valid task can become invalid without becoming unbelievable.

> Remembered necessity is not current necessity.

## Distinction from stale binding

Same family — *memory outruns reality* — different load-bearing object.

| | Stale binding | Stale-task replay |
|---|---|---|
| Surface | authority / basis | plan / observation |
| Object that goes stale | binding | task state |
| Failure | action survives after its justifying basis moves | action proceeds against a task whose justifying observation has been satisfied |

The two are siblings, not sub-cases. A stale binding can persist with no task attached; a stale-task replay can fire against a perfectly fresh authority basis.

## Failure predicate

Stale-task replay is in play when all four hold:

1. A task was legitimately opened from some observation.
2. The underlying observation later changed, resolved, or was superseded.
3. The task remained cognitively or procedurally "open."
4. Planning or action proceeded against the remembered task state instead of re-observing the current world.

The diagnostic mark: the plan looks coherent. It fits a world that used to exist. The error is temporal, not logical — which is why it survives scrutiny longer than ordinary confusion does.

## Accidental vs intentional replay

The general pattern is Stale-Task Replay. The failure case is *accidental* — replay without a reality check, where the remembered task state silently stands in for verified observation. The intentional case is *defensive re-entry* (or *protective replay*) — replay performed deliberately, knowing reality may have moved, because reopening or reconfirming is cheaper than trusting closure. The two cases share the syntactic shape but separate on whether the replay carries a fresh observation.

Sharpened predicate:

> Stale-task replay becomes a failure when remembered openness silently substitutes for present verification.

Intentional replay is not a failure mode. It is sometimes a valid operational hedge — *"I know someone probably already touched this, but I'm walking the checklist anyway,"* or *"this was likely fixed, but I don't trust the handoff enough not to reconfirm,"* or *"the cost of replay is lower than the cost of a false negative"* — and sometimes neurotic self-soothing. The discriminator is the same in both: whether the replay contains a reality check or just drags the old task state forward unchanged.

Operational rule for the primitive: the question is not *did you replay,* but *did the replay contain a reality check.*

## Canonical sequence

1. Observe problem.
2. Open task.
3. Context switch / delay / continuity lag.
4. World changes (auto-resolution, sibling agent, supersession, prior closure).
5. Task remains "open" in working memory.
6. Agent plans or executes against the remembered task state.
7. Re-observation reveals the task was already satisfied.

## Mitigation

> Re-observe before act when task lifetime exceeds observation freshness.

Operational form:

- Tasks derived from live state need a freshness check at planning time.
- The more time / context-switches / handoffs between observation and action, the more mandatory the re-observation.
- *Remembered-open* and *confirmed-open* are different categories. Vocabulary discipline costs nothing and catches the failure cheaply.
- Closure beats continuity. If the world has already changed, the task should die fast — preferring premature retirement over inertial re-execution.

## Relation to corrective monotonicity

The structural parallel is *two-step recovery,* not just stale-state substitution.

- **Systems-side (corrective monotonicity).** Re-entry is two steps: a corrective transition that invalidates the failed basis `K`, then a forward transition that admits a fresh `K′` through the ordinary admissibility path. Eliding the second step — treating the corrective alone as if it had restored authority — is laundering.
- **Agent-side (stale-task replay).** Defensive re-entry is two steps: retirement of the remembered task state, then a fresh observation that licenses (or refuses) the next action. Eliding the second step — treating the remembered task state as if it were a verified observation — is the failure mode.

Both are *two-step recovery elided to one-step laundering.* The legitimate path always carries a fresh observation or a fresh basis; the failure path skips it and substitutes memory for verification. The compact line *open in memory is not the same as open in reality* sits on the same shelf as *recovery restores availability, re-entry restores admissibility.*

## Generators (typical causes)

- **Continuity lag.** Notes / scratchpad / journal persist better than the world snapshot.
- **Long-lived task windows.** Task remains alive over hours or days while the world keeps moving.
- **Incomplete closure signals.** The world changed but nothing explicitly retired the task in the working context.
- **Strong prior legitimacy.** Because the task was real when opened, it keeps its aura of correctness past expiry.
- **Multi-agent / multi-session work.** One agent or session resolved it; another kept the old task active in its own plan space.

## Symptoms

- Planning around a task that no longer needs doing.
- Preparing a deploy for something already deployed.
- Building rollback plans for state already corrected.
- Escalating a condition already resolved.
- Creating follow-up work on an already-satisfied prerequisite.

## Compact examples

- *Ops.* "Need to deploy admissibility export to Linode." Reality: Linode already has the current binary; admissibility is on the wire. The deploy plan is still being built.
- *Team workflow.* "Need to ack/fix alert X." Reality: alert auto-cleared or was resolved by a sibling. Handoff notes still frame it as active.
- *Writing / project.* "Need to add field Y to DTO." Reality: a different slice already added it. New plan drafted to add it again.

## Open questions / future work

- Does this graduate into an authoring primitive (e.g. drafting against an old outline after the argument has moved) as well as an ops primitive? The current working definition is general enough to cover both, but the symptoms differ.
- Is the right mitigation invariant *task-side* (freshness check at planning time) or *observation-side* (auto-retirement of dependent tasks when underlying observation resolves)? Probably both, but they're separable and one may be cheaper than the other in a given system.
- The primitive describes a failure shape, not yet a remedy architecture. The mitigation laws above are operational hygiene, not formal guarantees. A formal version — analogous to corrective monotonicity's `RecoveryEnv` gate — would type tasks against observation freshness and refuse to plan against unrefreshed task state. Speculative; do not implement until a concrete forcing case appears.
