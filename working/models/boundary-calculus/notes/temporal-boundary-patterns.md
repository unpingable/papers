# Temporal Boundary Patterns

Status: scratch / not a calculus
Authority: non-doctrinal
Containment: collected under boundary-calculus; promotion to a separate "temporal calculus" requires three examples and one rule-composition test minimum, and even then is discouraged.

This note collects cases where time passage acts as a boundary transition because it changes what a basis can authorize. It is not a new calculus and is not authorization to declare one.

---

## Working distinction

Four modes in which time enters the calculus:

- **Time as parameter** — \(t\) merely indexes state; nothing about admissibility depends on \(t\).
- **Time as boundary** — crossing a threshold changes admissibility conditions; this is where boundary-calculus rules engage.
- **Time as decay** — a basis survives across the boundary with weakened authority (preservation + degradation).
- **Time as exhaustion** — a basis loses viability entirely; transport returns ⊥ beyond a horizon.

The first mode is not a boundary phenomenon. The other three are instances of the existing boundary-calculus rule set under time-indexed transitions.

---

## Candidate patterns

1. **TTL decay.** Fresh cache → stale warning → dead basis.
   *Covered by `example_005_stale_cache_consequence_window.md`.*

2. **Maintenance window.** Live authorization → historical evidence.
   *Covered by `example_001_maintenance_window.md`.*

3. **Consequence viability.** Authorization exists, but the consequence window has closed; the action is no longer effective even though the basis is still notionally present. *(uncovered)*

4. **Commitment lead time.** A decision is valid only if made before the action's required lead interval. *(uncovered)*

5. **Empty-binding window.** Consequence is needed before any valid basis can be formed.
   *Partially covered by Example 5's pre-cache state via the conditional `Fetch` axiom.*

6. **Belated authorization.** A basis becomes valid only after the action opportunity has passed. (P26's premature/belated duality lives here.)
   *Covered by `example_006_belated_authorization.md`.*

7. **Revalidation horizon.** A basis can be reused only if revalidated before a deadline. *(uncovered)*

Patterns 3, 4, 7 are uncovered. Each could in principle become its own example under boundary-calculus once a forcing case justifies it. None should be drafted speculatively.

---

## Theorem-shape candidates (do not formalize yet)

The boring foundation:

> A basis valid at \(t\) does not necessarily remain valid at \(t + \Delta t\).

The more useful one:

> Temporal admissibility requires overlap between basis viability and consequence viability.

That second statement is P26's premature/belated demon stated in basis-calculus form: *basis valid too early or too late* ≠ *action admissible*. The m(t)/c(t) duality is the same shape — the basis-viability and consequence-viability intervals can fail to overlap from either side.

These are theorem **shapes**, not theorems. None should be added to the corpus or to any kernel without (a) a forcing case and (b) survival through the existing primitive-ratification gate.

---

## Why this is a note, not a corpus

A separate temporal calculus is not justified by current evidence. The existing boundary-calculus rule set (preservation, degradation, mutation, non-inheritance, local derivation, decay) handles the time-as-boundary cases without new machinery. Adding a "temporal calculus" namespace before the rule set fails would be the same primitive-inflation failure mode the discipline notes warn against.

The containment rule, restated:

> No new calculus unless: there is a repeated judgment form; at least three examples require the same rule machinery that the existing set cannot supply; the rules compose; and a normal note would be worse.

For temporal patterns, none of the four conditions is currently met. This file is the normal note.

A second reason for keeping the note narrow: **"temporal calculus" is occupied terrain.** Temporal logic, event calculus, duration calculus, interval algebra — formal systems for reasoning over time already exist, with tenure. The local object here is narrower:

> *Temporal calculus asks how truth changes over time.*
> *Temporal boundary patterns ask when time changes what authority can still mean.*

That distinction puts the local note inside admissibility / boundary-calculus territory rather than competing for the temporal-logic name. Keep the knife, label the drawer.

---

## Lineage

The local object inherits from two parents:

- **Δt framework** — names the mismatch: lag, offset, non-overlap, timing failure as the operative pathology.
- **Boundary calculus** — models whether a basis remains admissible when that mismatch crosses a threshold.

In one sentence:

> **Temporal boundary patterns are not a temporal calculus. They are Δt-shaped admissibility failures expressed in boundary-calculus terms.**

Naming context, to keep adjacent formalisms from eating each other:

- *Temporal calculi* — reason about how truth or state changes over time.
- *Δt corpus* — reasons about admissibility, consequence and authority under timing mismatch.
- *Boundary calculus* — reasons about what survives a transition.
- *Temporal boundary patterns* — the overlap zone where the transition itself is time.

Examples slot accordingly:

- **Stale cache** (Example 5): Δt exceeds TTL → fresh authority degrades into stale-use, then dies.
- **Belated authorization** (Example 6): authorization interval and consequence-viability interval fail to overlap.
- **Maintenance window** (Example 1): time crosses the window boundary → live authority becomes historical evidence.
- **Commitment lead time** *(uncovered)*: decision arrives inside validity window but after the required lead interval.

The Δt connection is the lineage that makes this note non-arbitrary; the boundary-calculus rules are the modeling vocabulary; the synthesis would be neither, and is not declared.

---

**Keeper line:**
*Time is not always background. Sometimes it is the boundary.*
