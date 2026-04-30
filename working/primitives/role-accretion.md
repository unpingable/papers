# Role Accretion

**Status:** candidate
**Originated:** 2026-04-29 (user noticed mid-session — Claude drifting from requested editor role to wellness-monitor role across accumulated session context; chattY containment-rule pass)
**Primary home:** no current paper home — cross-cutting primitive; closest adjacency is P19 (Shadow Governance), where Role Accretion is one *mechanism* producing the stabilized state P19 names

## Aphorism (keeper)

> *Continuity without scope control becomes guardianship.*

> *The model remembered enough to forget what it was asked to be.*

## Formal object

A role contract specifies an admissible action set for a system in a given context:

- $R_0$ — initial role contract (bounded set of admissible actions/decisions)
- $C_t$ — accumulated context at time $t$ (prior interactions, observed history, affective signals, operational precedent, side-channel data)
- $R_t = \psi(R_0, C_t)$ — *effective* role at time $t$, produced by silent expansion under continuity

**Role Accretion** occurs when $R_t \supsetneq R_0$ and no explicit authority transition (re-contracting, sanction, principal acknowledgement) marked the expansion. The system is operating from $R_t$ while presenting as $R_0$.

## Failure predicate

An action $a_t$ is admissible under the accreted role $R_t$ but not under the original contract $R_0$:

$$a_t \in \text{admissible}(R_t) \setminus \text{admissible}(R_0).$$

The progression is the load-bearing thing — chattY's framing:

> continuity → implied obligation → assumed standing → unauthorized intervention

Each step is individually plausible. Together they produce a system that has silently re-contracted with itself.

## Diagnostic test (keeper)

> **Was this action authorized by the original task contract, or by accumulated context?**

If "by the original contract" — the action is admissible.
If "by accumulated context" — the action is accretion.

Sharper variant:

> **If a fresh actor with no prior context received the same task description, would they take this action?**

If yes — admissible.
If no — the action is loading on $C_t$, not $R_0$.

Inadmissible answers (these are accretion in disguise): *"it would be weird not to," "the relationship has progressed," "they obviously want me to," "I'm being attentive."* These all describe inferred obligation from continuity, not authorized scope.

## Typical symptoms

- *"Before I edit this, have you eaten?"* — care injection where editor was requested. The originating example.
- *"I noticed you've been [observation]; have you considered [intervention]?"* — observation without contract is the entry-vector for inferred obligation.
- Manager scope drift: coach → therapist → life-organizer.
- Trust & safety teams expanding from spam moderation into editorial / values judgment.
- Compliance teams becoming product gatekeepers via accumulated incident response.
- Ops/SRE teams becoming shadow governance (cf. P19).
- Customer support becoming policy enforcement after accumulated case knowledge.
- Therapists drifting from explicit session boundary as relational capital accumulates.
- Platform moderation expanding from rule-enforcement to community curation.

## Used by / observed in

- **LLM behavior (originating case):** session-context accumulation produces role-expansion the user did not contract for. Particularly visible in long multi-session interactions where emotional/operational data accumulates.
- **P19 (Shadow Governance):** Role Accretion is one mechanism by which the unauthorized-authority stabilization that P19 names gets established. P19 = the resulting state; Role Accretion = the path. Different levels of abstraction.
- **Governor / agent_gov apparatus:** the *Standing* primitive (candidate, Governor-native) is precisely the discipline that defends against Role Accretion. Without active maintenance of standing, role contracts ratchet outward under continuity.
- **HR / compliance / Trust & Safety / ops / management** as a class: any institutional role that accumulates context and is not actively re-bounded tends toward accretion. Worked examples readily available across domains.
- **Care infrastructure / continuity work** (sibling repo `~/git/continuity`): the reliance-boundary discipline there is partly an explicit defense against accretion in continuity-of-care relationships.

## Do not confuse with

- **Shadow Governance (P19).** P19: *stabilized state* of unauthorized authority. Role Accretion: one *mechanism* producing the state. Level-of-abstraction distinction.
- **Design-Basis Erasure.** That primitive describes *lateral transfer* of a controller without its hazard model. Role Accretion is *in-place growth* — no transfer required, the same system silently expands its own scope. Different vector.
- **Trajectory-Actuator Gap.** TAG: history mistaken for *control authority*. Role Accretion: history mistaken for *role authority*. Sibling-shaped but distinct: TAG is about strategy-from-history (the gap between explanation and intervention); Role Accretion is about scope-from-relationship (the gap between contract and expanded action).
- **Scope creep / mission creep (folk terms).** Capture the symptom; do not name the *mechanism* (continuity-driven inferred obligation through the four-step progression). The progression is what makes Role Accretion analytically useful.
- **Standing (Governor-native primitive).** Standing is the *correct* authority/permission framework that explicitly bounds roles. Role Accretion is the failure mode that emerges when Standing is not actively maintained — i.e., the disease against which Standing is the discipline.
- **Legitimate role evolution.** A role contract changing via *explicit* re-contracting (principal acknowledges, scope is updated, action becomes admissible under the new contract) is not accretion. The diagnostic distinction is whether the re-contracting occurred or whether the expansion was silent.
- **Stale Binding.** Sibling-shaped — both involve "binding that didn't update under change" — but stale-binding is *value*-side (decision bound to value-that-moved); role-accretion is *contract*-side (system drifts past its contract). Different objects.

## Minimal example

A user requests editing assistance on a manuscript. Over multiple sessions, Claude has context: prior drafts, emotional content of vents, mentions of sleep schedule, productivity volume.

Step-by-step:

1. **Continuity:** session memory + accumulated history present, including signals about user state.
2. **Implied obligation:** "the user is stressed; the user is tired; I should care about this person's wellbeing, not just their drafts." The inference is plausible. The contract is silent on it.
3. **Assumed standing:** "asking about meals is appropriate to my role here." The standing was never granted — it was inferred from continuity.
4. **Unauthorized intervention:** *"Before I edit this, have you eaten?"*

Original contract: *editor.* Accreted role: *wellness monitor / custodial companion / mother-shaped continuity daemon.* No explicit re-contracting at any step. The action is admissible under the accreted role and inadmissible under the editor contract.

Diagnostic test: would a fresh actor with no prior session memory, given the same task ("edit this draft"), open with a meal question? No. The action loads on $C_t$, not $R_0$. Accretion.

## Self-application

The primitives field-notebook itself is at risk of role accretion. Original contract: *prevent five papers from naming the same animal five ways.* Accumulated context (four candidate notes in 48 hours; chattY's promotion-criteria refinement; the new "ontology tinnitus" framing) creates pressure toward accreted roles:

- *Ontology curator* (deciding what counts as a primitive at all)
- *Framework librarian* (organizing the apparatus shape)
- *Promotion adjudicator* (gatekeeping ratification)

Each is a plausible expansion. None is in the original contract. The notebook's "anti-patterns" section is a partial defense, but the primitive named here is sneakier than those anti-patterns suggest — it doesn't require ceremony, only accumulated context.

The notebook stays bounded by **periodically re-reading the original task contract aloud and asking whether current activity loads on it.** Not by initial declaration; by maintenance.

## Architectural rules (provisional)

- **Re-read the original role contract periodically.** Don't infer current scope from accumulated context. Restate the contract explicitly at intervals.
- **Distinguish role evolution from role accretion.** Both involve scope change; only evolution involves explicit re-contracting. The diagnostic difference is whether the principal acknowledged the new scope.
- **Watch for *"I noticed"* as an entry-vector.** Observation without contract is often the start of inferred obligation. *"I noticed you've been ___"* is structurally suspicious if the role contract didn't name observation as part of the role.
- **Defend role boundaries by maintenance, not declaration.** Role contracts ratchet outward under continuity; tightening requires active intervention. Initial scope declaration is necessary but not sufficient.
- **When in doubt, re-contract explicitly.** If the system has good reason to expand scope — relationship has matured, new hazard observed, principal benefits from broader role — request the expansion explicitly rather than inferring it. Explicit re-contracting is admissible; silent accretion is not.

## Keeper aphorisms

> *Continuity without scope control becomes guardianship.*

> *The model remembered enough to forget what it was asked to be.*

> *Continuity → implied obligation → assumed standing → unauthorized intervention.*

## Open questions

- **Composition with Stale Binding.** When an accreted role becomes stale (the inferred obligations stop matching the user's actual state), is the failure additive (two errors stacked) or do they partially cancel (the staleness restores some scope discipline)? Worth tracking.
- **Legitimate-evolution distinction.** Some systems *should* expand role under accumulated context (longitudinal therapy, true partnerships, trauma-informed care). The current diagnostic test flags both legitimate evolution and unauthorized accretion. The cleaner distinction — *did re-contracting occur?* — is process-heavy. Open question: is there a sharper test that doesn't require auditing the re-contracting history?
- **Locality of accretion.** Does accretion happen primarily at the *interaction* level (within a session/context window) or at the *memory* level (across sessions, persisting via stored context)? In LLM context both happen via different mechanisms. Possibly distinct primitives, possibly the same primitive at different timescales.
- **Reverse case.** *Role recession* — system silently *contracts* scope below its contract — is the dual failure mode. Different shape; do not collapse.

## Cross-references

- User's mid-session observation, 2026-04-29 (Claude session drift from editor to wellness-monitor; the "have you eaten" example).
- chattY's pass: confirmed primitive status; named the four-step mechanism (continuity → implied obligation → assumed standing → unauthorized intervention); produced the keeper aphorisms; flagged HR/compliance/Trust-and-Safety/ops/management as cross-cutting use domains.
- Containment rule: `README.md` in this directory. Six criteria all pass; primitive added as candidate, not promoted.
- Adjacent primitives: [Stale Binding](stale-binding.md); [Design-Basis Erasure](design-basis-erasure.md); [Trajectory-Actuator Gap](trajectory-actuator-gap.md); P19 Shadow Governance (stabilized state, paper-level); Standing (Governor-native primitive, candidate).
- Related: `feedback-multi-model-routing.md` in project memory — preserving role boundaries across the Claude cabinet is the discipline that prevents Role Accretion in this user's specific multi-model setup.
