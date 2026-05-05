# Zombie Obligation

**Status:** candidate
**Kind:** boundary condition (with attractor flavor — systems fall into this state by default when re-derivation is not budgeted)
**Originated:** 2026-05-05 (claude-code session, after DeepSeek "software ecology" riff + chatty structural pushback; user routed to claude-code for operational knife rather than authorial register)
**Primary home (paper):** none yet. Candidate destinations: future "Operational Afterlives" essay/chapter, or sibling paper to the admissibility family. Decision deferred.

## Formal object

Let $J_t$ be the **justification graph** at time $t$: the predicates and grounding facts that make an obligation admissible.

Let $O_t$ be the **obligation graph** at time $t$: the bindings that constrain action and produce operational consequence when honored.

An obligation $o \in O_t$ is:

- **Live** at $t$ if executing or honoring $o$ produces operational consequence.
- **Justified** at $t$ if $J_t$ entails $o$'s admissibility — i.e., the target the obligation serves is itself live, and the binding from target to obligation is current.

A **zombie obligation** at time $t$:

$$o \in O_t \text{ is live} \quad \wedge \quad J_t \not\vdash \text{admissibility}(o) \quad \wedge \quad \nexists \text{ expiration event that removed } o \text{ from } O_t.$$

Compactly: **the obligation graph survives the disappearance of the justification graph.**

## Failure predicate

Zombie obligation occurs when:

1. An obligation continues to bind action.
2. The justifying target / regulation / contract / customer / decision-context has lapsed, vanished, been superseded, or become untestable.
3. No removal mechanism (TTL, sunset clause, ownership review, re-derivation gate) has fired.
4. Continued honoring of the obligation produces operational consequence — cost, blocking, gating, attention, ceremony.

The four conditions are jointly required. Removing any one of them lands the case in a neighboring primitive (see *Do not confuse with*).

## Typical symptoms

- Cron job running for a product that was sunset two reorgs ago.
- Compliance process for a regulation that was repealed or superseded.
- Weekly meeting whose decision function vanished but whose attendance is enforced.
- Dashboard everyone checks because everyone checks it.
- Compatibility shim for a customer who churned.
- IAM exception created for a migration that ended three years ago.
- Architecture rule inherited from a vendor / platform constraint that no longer applies.
- "Do not touch this" lore around a system nobody can explain — the obligation no longer protects the system; it protects the organization from discovering why it is afraid.
- Test gate that asserts a property no current code path can produce.
- Auth scope still granted because granting it once was easier than re-deriving who needs it.

## Used by

Cross-cutting. No paper currently treats this as load-bearing. Adjacencies:

- **Admissibility family** — zombie obligation is a structural admissibility refusal: the obligation cannot legitimately bind action because its justification basis has lapsed. Sibling shape to P25's "stale basis cannot bind at mutation layer" but on the obligation side rather than the authority side.
- **Controller continuity** — zombie obligations are one mechanism by which a controller's effective binding-set drifts from its declared binding-set without composition discontinuity.
- **P27 obligation-unsound reconciliation** — adjacent but distinct: P27 handles the case where the controller is correct but the operator (the human / org context) is unsound. Zombie obligation handles the case where the operator is unsound *because* the obligation graph has detached from the justification graph.

## Do not confuse with

- **Stale Binding.** Stale binding: target still exists; basis is old. Zombie: target / justification has lapsed entirely.
- **Substitution / proxy regulation (P25).** Substitution: target exists; observable cannot reach it. Zombie: target has gone away; obligation persists anyway.
- **Authority Decay** (candidate, primitives README). Authority decay: authorization technically valid after the basis for authority expired — the *right to act* has decayed. Zombie obligation: the *requirement to act* has decayed. Dual shapes on opposite sides of the gate; do not collapse. A system can have decayed authority *and* zombie obligations simultaneously, and they fail differently.
- **Controller Continuity discontinuity.** Controller continuity: composition changes across handoffs. Zombie: composition can be perfectly continuous; the issue is what the controller is still bound to.
- **Orphaned Causality** (candidate). Orphaned causality: evidence survives but loses the binding needed to accuse. Zombie: obligation survives without the justification needed to admit it. Evidence vs obligation; both have orphan-graph shape but different load-bearing referent.
- **Ordinary legacy.** Legacy: old, working, justified — old code can be alive and admissible. Zombie: old, working, *not* justified, *still* binding. Legacy is age; zombie is justification-rot.

## Minimal example

A SaaS company runs a nightly cron that exports billing records to a partner's SFTP. The partnership ended in 2022 when the partner was acquired and their integration deprecated. The cron still runs nightly, the SFTP credentials are still rotated by the secrets-management team, the export still appears on the on-call runbook ("if export fails, page the integrations team"), and the integrations team still includes "billing-export" in their service inventory. No customer is on the receiving end. No one has been on the receiving end for three years. The obligation continues to bind: rotation work, on-call cognitive load, runbook entries, audit-checklist items, occasional 3am pages when the export fails. There is no removal mechanism — sunset of the partnership did not register as sunset of the obligation, because the obligation graph and the justification graph were never bound by an expiration link.

## Architectural rules

Per the doctrine fragment:

- **Obligations have owners.** An obligation without an owner cannot be re-derived; it can only be obeyed by inertia.
- **Justifications have expiry.** A justification without an expiry mechanism fossilizes into "we have always done it this way."
- **Continuing action requires re-derivation, not inherited compliance.** Periodic re-derivation is the gate; absence of re-derivation is itself a zombie-creation event.
- **Afterlives are inventoried, not assumed.** A retired system's residue (cron, IAM, runbook entries, alerts, schemas, dependencies) must be tracked through removal, not allowed to age out informally.

## Admissibility test

For any persistent obligation, ask:

1. What target does this obligation serve?
2. Is that target still live? When was it last re-derived?
3. Who owns the consequence of honoring this obligation? Of stopping?
4. What evidence revalidates the obligation?
5. What expires it?
6. What happens — concretely, named — if we stop obeying it?

An obligation that cannot answer (1)–(5) and whose answer to (6) is "we don't know" is a zombie obligation candidate. The admissibility refusal is then: a controller (human or mechanical) acting on this obligation cannot legitimately bind action through it, because the basis the obligation rested on is no longer admissible.

## Keeper aphorisms

- **Live obligation, dead justification.**
- **Legacy is not age. Legacy is obligation without re-derived justification.**
- **An obligation becomes zombie when it retains operational force after its motivating target can no longer be established.**
- **Software is not done when it ships. It is done when its afterlife is admissible.**
- **The obligation graph survives the disappearance of the justification graph.** (load-bearing form)

## Open questions / ratification gates

- Generator test: does this name a new boundary, or is it a coordinate produced by stale-binding × authority-decay × controller-continuity? Working hypothesis: new boundary, because the *operator* failure (no re-derivation budgeted) is structurally distinct from any of the parents — none of them name "the obligation graph and the justification graph were never linked by an expiration mechanism" as the load-bearing fact.
- Reuse test (working-status promotion): cited across multiple papers/projects without semantic drift. Currently zero papers; would need P27 binding work or an "Operational Afterlives" essay to earn working status.
- Formal-stress test (ratified-status promotion): formal object survives counterexample pressure. Specifically: is the obligation/justification graph distinction strong enough to carry a Lean formalization, or does it collapse into existing kernel vocabulary (StepAllowed × authorized AuthorityClaim with a temporal index on the basis predicate)? Open.
