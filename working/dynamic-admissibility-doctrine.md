# Dynamic Admissibility (candidate doctrine)

*Status:* CANDIDATE / doctrine stub, filed 2026-07-06. Captured from a live
ChatGPT thread downstream of the sequent-admissibility island landing
(`working/sequent-admissibility-specimen.md`). **This is a wedge under a
door, not a flag through it** — named early per the name-early discipline,
NOT authorized to build. No Lean, no paper commitment.

## The distinction

**Static admissibility** (what the sequent specimen formalizes): given a
fixed context Γ, does a rule preserve derivability? Weakening/contraction/
exchange/cut are admissible because they forge no proof inside a frozen
judgment. Clean toy universe: no time, no actors, no hidden information, no
incentives.

**Dynamic admissibility**: given a state `S` and a transition `S ─a→ S′`, is
the action `a` admissible *as a transition* — accounting for how it changes
what future claims will mean and whether they can still be discharged?

```text
Static:   Γ ⊢ C                         (does this rule preserve derivability?)
Dynamic:  S ─a→ S′                       (does this action preserve the future
                                          conditions under which claims can be
                                          admitted?)
```

Here `S` carries more than a context: claims, receipts, actors, beliefs,
open obligations, reachable states, refusal modes, freshness.

## The maxim (the sharp form)

> **No action may improve its future standing by destroying, obscuring, or
> laundering the conditions under which its standing could later be checked.**

Equivalently: *a move is dynamically admissible iff it does not make future
admissibility lie.*

## Why this is a bigger animal than static admissibility

A locally permitted action can be globally corrupting because it mutates the
epistemic game board on which later claims are judged. Four firing shapes:

- **Signaling** — a locally "wasteful" move (costly credential, warranty,
  collateral, burned reputation) is admissible because it *produces evidence*
  that reshapes a future information state, not because of its immediate
  payoff. Action as evidence production.
- **Cover-up / audit destruction** — a locally allowed move (delete logs) is
  dynamically inadmissible because it destroys the future ability to
  discharge a claim. `delete logs now → later "trust me" cannot be checked`.
- **Agent delegation** — a tool call fine in isolation is inadmissible if it
  creates an unauditable side effect future review cannot reconstruct.
  `act now → receipt missing → later standing laundered through narration`.
- **Bureaucracy** — a review step that does not validate a claim can still
  change *who may rely on it later*. If the review was fake, it minted future
  fake standing. `reviewed ≠ true`, but `reviewed` may create procedural
  standing.

## Rough shape (not a build spec)

An action is dynamically admissible only if, for every reachable `S′`, future
claims depending on `a` remain dischargeable **and** no standing is minted by
the transition itself:

```text
Admissible(a, S)  iff  for every reachable S′,
                         future-claims-depending-on-a remain dischargeable
                       ∧ no standing is minted by the transition
```

## Relationship to existing repo doctrine

This is not new territory so much as the *transition-indexed generalization*
of things already named:

- **The static fossil** is [[project-sequent-admissibility-specimen]] — cut/
  weakening/contraction as the frozen-judgment version. Dynamic admissibility
  is the living animal with claws; the specimen is its skeleton.
- **The kernel already exists in prose** as [[project-authorization-laundering-arc]]:
  *post-state witness is not pre-state authority*. That IS dynamic
  inadmissibility for the cover-up case. Dynamic admissibility is its
  superclass.
- Composes with [[project-non-reciprocal-admissibility-flow]] (A shapes what
  counts for B while pretending non-authority — a transition that mutates
  B's future frame), [[project-continuous-admissibility-discharge]] (*true but
  inadmissible*; FICO/FCRA staleness), and the decay family
  [[project-admissibility-decay-family]] (freshness/staleness as a temporal
  transition invariant).

## Game-theory rhyme (related work, not a claim)

In game theory "admissible" ≈ "not (weakly) dominated." Sequential games
wreck the static cleanliness: a *strategy* is a contingent policy across time
and information states, so a locally dumb move can be globally admissible
because it reshapes beliefs (signaling), and subgame perfection asks whether a
continuation stays *credible* once its node is reached (the non-credible-threat
problem). Dynamic admissibility is the custody-flavored cousin: *does this
transformation preserve admissibility across future information states?* —
where the mutated resource is claim custody, not payoff.

## Register fence (binding)

This is **not** a universal calculus and does not license one. It is a design
constraint for *local* systems that transform claims over time. The moment it
tries to become a global admissible-predicate it is
[[project-distributional-admissibility-tombstone]] in a fresh mustache and
the no-unifier doctrine ([[project-no-unifier-without-laundering]]) governs.
Forcing-case calibration ([[feedback-forcing-case]]): do NOT invoke a forcing
case to start building a "dynamic admissibility calculus." File the wedge;
build nothing until a specific local system (AG gate, a Night Shift
reconciliation, a specific agent-tool transition) presents a bounded question.
