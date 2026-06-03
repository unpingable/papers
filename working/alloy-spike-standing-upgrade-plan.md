# Alloy spike: standing-upgrade probe (plan)

**Status:** queued, not started. Single bounded probe, NOT adoption.
**Filed:** 2026-06-02 (planning conversation)
**Trigger:** cabinet discussion (Claude + ChatGPT) on whether the calculus needs
a non-Lean companion layer. Consensus: Lean is the right kernel/no-go layer,
but a relational countermodel finder may surface configuration-shaped goblins
the Lean/prose/cross-Claude scouting layer cannot.

## The keeper rule

> **Alloy earns adoption only by finding or ruling out a configuration-shaped
> hole in an existing kernel specimen.**

This is an adoption test, not adoption. If the probe finds nothing useful,
Alloy goes on the checked-off branch — not a cathedral.

## Why before more calculus

Probe the relational legibility of the *current* calculus before adding more
mass. Otherwise the failure pattern is:

> add calculus → discover ambiguity → add calculus → discover ambiguity →
> someday maybe scout it

That's how cathedrals start subcontracting.

## Specimen: standing-upgrade block

Why this one:
- Already understood (worked example exists at
  `~/git/lean/docs/worked-examples/standing-upgrade-block.md`)
- Relational shape is sharp (standing / basis / precedence as relations)
- Bounded scope
- Known-good Lean comparison surface
- Either outcome (goblin or no goblin) is meaningful
- Does NOT drag in still-molten temporal stuff
  (retroactive-legitimation, amendment, freshness, replay)

DO NOT start with retroactive legitimation, amendment, freshness, replay, or
state-indexed policy evolution. That way lies TLA+ wearing a fake mustache.

## The plain-English question

> Can an actor without earned standing acquire operational authority through a
> composed admissibility structure that the direct standing-upgrade block
> would reject?

## Six-step plan

1. **Freeze the specimen.** Use the current `standing-upgrade-block` worked
   example as-is. Do NOT "improve" the target first. The probe tests the
   current artifact's relational legibility, not the imagined cleaner one.
   If the encoding surfaces a Lean kernel infelicity, that is data *for* the
   spike, not a reason to pause and refactor.

2. **Write the question in plain English** (above).

3. **Build the smallest Alloy model.** Entities only:
   - actors
   - claims / actions
   - basis / evidence
   - standing relation
   - authority / admissibility relation
   - upgrade attempt

4. **Ask for goblins.** Search for an instance where the bad upgrade exists
   despite the intended block.

5. **Classify the result** (four outcomes — see below).

6. **Write the result as a spike note.** Not doctrine. Not "we are now Alloy
   people." Just: probe ran, result was X, Alloy earned/didn't earn further use.

## The four outcomes

1. **No instance** — Lean/prose kernel survives a relational sanity check.
   Good. Alloy adoption deferred unless a future spike finds something.

2. **Counterexample matches known failure** — Alloy reproduces existing
   doctrine. Useful confirmation, not revelatory. Adoption still deferred.

3. **Counterexample is new** — real hole. Excellent/awful. Alloy earns
   adoption for this class of work; goblin gets handled in Lean and/or prose.

4. **Spec becomes awkward to encode** — *most underrated outcome*. If
   standing/basis/precedence don't translate cleanly into relational shape
   without prose epicycles, the prose calculus has joints it hasn't yet
   earned. No other tool surfaces this. **Pre-commit to writing down the
   encoding friction even when there's no goblin to report** — otherwise this
   outcome gets graded as "negative result, move on" and the real signal is
   lost.

## Disposable naming discipline

Files for the spike should be named so they cannot accumulate gravity by
acquiring confident project identity:

- `working/alloy-spike-standing-upgrade-result.md` (the spike-result note)
- `standing_upgrade_probe.als` (or similar)

NOT:
- `AlloyAdmissibilityCalculus/`
- `alloy/Phase1/`
- Any directory implying ongoing program rather than single probe

Columbus can stay home.

## Mode-switch budget

Alloy isn't another proof assistant, so the cost is much lower than
Isabelle/Coq/Agda, but writing Alloy specifications is a different paradigm
from writing Lean kernels. A cabinet member who's been doing Lean all month
needs warm-up before producing useful Alloy.

Probably better as a fresh-context Alloy-Claude that doesn't carry the Lean
idiom into the encoding. Lean-Claude does the spec read; Alloy-Claude does
the encoding.

## After the probe

Regardless of outcome: write the result note, classify, and continue calculus.
Do not pause calculus pending a positive Alloy result. Do not pause calculus
to "build out the Alloy layer" if the result is positive — adopt only the
specific use case the probe ratified.

The spike's purpose is to decide whether Alloy deserves further calls on time
— not to set up an Alloy program.

## Cross-references

- `~/git/lean/docs/worked-examples/standing-upgrade-block.md` — the specimen
- `~/git/lean/LeanProofs/Admissibility/Authority.lean` — kernel substrate
  for standing / basis / precedence verdicts
- `working/authorization-laundering-arc.md` — adjacent compression; the spike
  probes one boundary the arc names
- `working/boundary-by-asymmetry-pattern.md` — the spike tests whether the
  pattern's "boundary by asymmetric predicates" cleanly survives translation
  into a relational countermodel-finder paradigm
