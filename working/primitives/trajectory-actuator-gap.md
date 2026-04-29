# Trajectory-Actuator Gap

**Status:** candidate
**Originated:** 2026-04-29 (user noticed mid-session — political-strategy "let's recreate the magic" pattern; chattY containment-rule pass)
**Primary home:** no current paper home — cross-cutting primitive (likely surfaces most in Latent Capitalism / Chronopolitics / Substack work, with adjacencies to P22 / P25 / P26)

## Naming note

*Causal Standing Gap* was considered and rejected. **Standing** is already load-bearing in Governor and the candidate primitives list with a Governor-native meaning: *authority/permission to testify, decide, or act.* This primitive concerns a different sense of "standing" — present-tense operational access to a control surface — and reusing the term would create exactly the semantic aliasing this directory exists to catch. *Trajectory-Actuator Gap* is collision-free, mechanical, and preserves the aphorism.

## Aphorism (keeper)

> *A history is not an actuator.*

## Formal object

A control situation has:

- state space $X$, input space $U$, dynamics $x_{t+1} = f(x_t, u_t, w_t)$
- exogenous disturbance / substrate context $w_t$ (weather, market, institutional state, opponent action, etc.)
- an actor with admissible input set $U_{\text{actor}} \subseteq U$ from current state $x_{\text{now}}$

An **observed historical trajectory** is $T = \{(x_t, u_t, w_t)\}_{t=0}^\tau$, possibly with partial observation, in which the system reached some salient state $x_*$.

A **post-hoc model** $M(T)$ explains the trajectory by identifying which inputs and disturbances drove the transition.

The **Trajectory-Actuator Gap** is the conflation:

> $M(T)$ well-formed $\implies$ $x_*$-like states are reachable from $x_{\text{now}}$ under $U_{\text{actor}}$.

The implication does not hold. Identification is not synthesis. Three failure layers:

1. **Substrate dependency.** The historical transition relied on $w_t$ the actor cannot reproduce.
2. **Input-set gap.** The historical $u_t$ may not lie in $U_{\text{actor}}$ (different actor, different access).
3. **State drift.** $x_{\text{now}} \neq x_0$; same inputs may not produce comparable trajectories under different preconditions.

## Failure predicate

An actor builds strategy from $M(T)$ as if it exposed a presently operable control pathway, without testing whether the inputs / timing windows / state preconditions / substrate disturbances were actor-controlled in the first place.

The Δt-flavored expansion: a contingent process distributed across time — relationships, trust, institutional weakness, media incentives, money channels, opponent error, local operators — gets compressed into a present-tense lever the actor pretends to hold.

## Diagnostic test (keeper)

> **Which parts of the historical transition do we actually have standing / access / capacity to affect now?**

Decompose the historical inputs/conditions into four categories:

- **Lever** — actor has present-tense actuation
- **Weather** — substrate condition; not actuated by anyone, including the actor
- **Opponent** — counterparty variable; not under actor's authority
- **Window** — timing-bounded; may have closed

If most of the historical alignment was weather/opponent/window, the proposed strategy is *invocation*, not action.

Inadmissible answers: "we have access to attention," "we have access to message," "we have access to the candidate," "we have access to vibes," "we have access to money if someone gives it to us." These describe surface effort, not standing over the inputs that mattered.

## Typical symptoms

- "X happened because Y aligned" $\to$ "let's do Y."
- Strategy decks built from case studies treated as recipes.
- Founder cargo-culting (*"X startup did Y and won"*).
- Political imitation strategy (*"the next Obama," "our Reagan moment"*).
- Research methodology imported from successful papers without the institutional infrastructure that hosted the original work.
- Anecdote-driven institutional change.
- Causal models tagged with confidence about *what mattered* but unstated about *who held the lever*.

## Used by / observed in

- **Latent Capitalism / Chronopolitics:** primary surface. Political-strategy retrospectives that upgrade interpretive access into intervention access; treating distributed contingent alignments as presently-operable control surfaces.
- **Substack writing on governance/strategy:** any piece that says "X worked because Y" and pivots to "we should do Y" without standing decomposition.
- **P22 (no universal plant clock):** adjacent. Different Δt regimes mean a successful past trajectory may not even be the same kind of object as a present-tense intervention.
- **P25 (substitution under observability asymmetry):** adjacent — chattY's framing is *trajectory substitution* (observed historical path substituted for an available control pathway) is structurally parallel to P25's target substitution, but the cause differs (see "Do not confuse with").
- **P26 (m(t)/c(t) duality, empty window):** adjacent. The historical event happened inside a window that may have closed. *History happened inside its window; the strategy proposes to act after that window has closed.*
- **Design-Basis Erasure:** sibling primitive — both are "import without preserving the load-bearing context," but the load-bearing thing differs.

## Do not confuse with

- **P25 / Substitution.** P25: target $V$ is *unsensed*, so the controller substitutes a sensible proxy $V'$. Trajectory-Actuator Gap: the trajectory $T$ is *observed and explained*, and the explanation is mistaken for a control surface. Cause differs (observability gap vs identification-synthesis conflation); shape rhymes.
- **Design-Basis Erasure.** That primitive transfers a *controller* to a new domain after losing its hazard model. This primitive transfers a *historical alignment* and treats it as if it were a controller in the first place. Sibling primitives: both involve "import without preserving the load-bearing context," but
  - Design-Basis Erasure: "this worked elsewhere, so import the ritual." — wrong because $H' \neq H$.
  - Trajectory-Actuator Gap: "this happened once, so reproduce the causal path." — wrong because the historical actor had inputs/standing the present actor lacks.
- **Causal-inference do-calculus.** Do-calculus formalizes the observation-vs-intervention distinction (the failure mode this primitive names is *why* do-calculus exists). Trajectory-Actuator Gap is the strategy-from-history specialization, expressed without requiring the do-operator machinery.
- **Hindsight bias / narrative fallacy.** Those name *psychological* errors in retrospective reasoning. Trajectory-Actuator Gap names a *structural* gap that holds regardless of psychological state — even a perfectly calibrated retrospective model, with no narrative inflation, fails to confer reachability.
- **Goodhart-style proxy gaming.** Different shape entirely; no proxy/agent dynamic is required here.
- **Standing (Governor-native primitive).** *Authority* to act vs *operational access* to the control surface. Different facets. See naming note above.

## Minimal example

A campaign analyst observes: *Obama 2008 succeeded because of a generational shift in turnout, an unpopular incumbent party, a media-savvy ground game, an opponent with severe money problems, and a financial crisis breaking in late September.*

The analyst writes a strategy memo: *"To replicate this, we should focus on generational turnout and a media-savvy ground game."*

Standing decomposition:

| Historical input | Category | Present actor's standing |
|---|---|---|
| Generational turnout shift | Weather | None — cohort math, not a lever |
| Unpopular incumbent party | Window | Conditional on world-state |
| Media-savvy ground game | Lever (partial) | Hires, resources |
| Opponent money problems | Opponent | None |
| Financial crisis (late Sept) | Weather | None |

The strategy treats all five as equally available. The Trajectory-Actuator Gap is the silent claim that historical alignment is operable now. **One-and-a-half-of-five** of the inputs were levers; the other three-and-a-half were substrate, window, or opponent. The memo prescribes invocation.

## Architectural rules (provisional)

- **Distinguish identification from synthesis.** A model that fits a trajectory is not a controller. State this explicitly when presenting historical case studies.
- **Run the standing test on every imported strategy.** Decompose inputs into Lever / Weather / Opponent / Window before treating any past trajectory as a recipe.
- **Tag factors in causal stories.** When listing "factors that produced X," annotate each with actor-standing class. Strategies built from mostly-weather lists are invocations, not plans.
- **Do not collapse a Δt process into an instantaneous lever.** Historical alignments are temporally extended; if the strategy presupposes simultaneous availability of conditions that took years to align, the gap is operating.
- **Acknowledge irreducible substrate.** Some historical successes were partly *weather*. The honest move is to plan for the lever-fraction and bound the weather-fraction explicitly, not to upgrade weather to lever rhetorically.

## Keeper aphorisms

> *A history is not an actuator.*

> *Observed trajectory is not control authority.*

> *Causal legibility does not confer causal standing.*

> *They compress a contingent Δt process into an imaginary instantaneous control surface.*

## Open questions

- **Composition with Design-Basis Erasure.** When an actor imports both a controller *and* a historical trajectory of that controller's success — e.g., "we'll run the X playbook the way they ran it in 2008" — is the failure additive (two errors stacked) or multiplicative (each masks the other)? Track if the composite shows up.
- **Standing-fraction as a measurable.** Can we operationalize the diagnostic test as a quantitative measure (fraction of historical inputs that are present-tense levers for the current actor)? If so, it could surface in P26's empty-window analysis as one component of "is this binding window even reachable?"
- **Pedagogical case studies.** Does this primitive imply case studies are operationally misleading by default, or just non-portable when treated as recipes? The honest answer probably distinguishes case-study-as-illumination (legitimate) from case-study-as-recipe (the failure mode).
- **Reverse case.** The dual is "trajectory not observed, but actuator available" — actor has the lever and doesn't know what to do with it. Different shape; do not collapse.

## Cross-references

- User's mid-session observation, 2026-04-29 (political-strategy retrospectives upgrading interpretive access to intervention access).
- chattY's pass: confirmed containment criteria all clear; named the *trajectory substitution* framing; rejected *Causal Standing Gap* on collision grounds; ranked alternative names; produced the working card.
- Containment rule: `README.md` in this directory. Six criteria all pass; primitive added as candidate, not promoted.
- Adjacent primitives: [Stale Binding](stale-binding.md); [Design-Basis Erasure](design-basis-erasure.md); P25 (Substitution, candidate, in candidates list); Standing (Governor-native, candidate, see naming note).
