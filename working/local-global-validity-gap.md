# Local-Global Validity Gap

**Status:** candidate primitive / exploratory
**Not:** paper-numbered, Lean-lifted, sheaf-committed
**Opened:** 2026-05-10
**Origin:** A/B between paper-claude and DeepSeek on "candidate dynamics equivalently large to admissibility." Both AIs surfaced four candidates (drift / coupling / saturation / mimicry). ChatGPT named the hinge: those four are *failure surfaces*; the actual primitive is the gap they share.

## The candidate

> **Locally valid operations can compose into a globally false system.**

The failure that survives local correctness. Every local check passes; the composed object lies.

## Why field-shaped

Not "no one has seen instances" — instances are everywhere. Field-shaped because the same structural failure recurs across substrates with different local costumes, and no existing frame names the missing proof obligation between local validity and global continuity.

Existing frames see *some* instances (concept drift, common-mode failure, alert fatigue, Goodhart, institutional isomorphism) but treat them as separate phenomena. The primitive is the shape they share.

## Four axes as test cases (not subfields)

| Axis | Obstruction kind | Local check that passes | Global property that fails |
|------|------------------|-------------------------|----------------------------|
| Drift | temporal | each step admissible | identity over time |
| Coupling | substrate | each component independent | independence under shared substrate |
| Saturation | representational | each input distinct | distinctions preserved through channel |
| Mimicry | semantic/formal | each form present | substance behind form |

The primitive is *not* one of these. The primitive is the gap they share.

## Core gate question

> Does the candidate failure explain a case where every local check passed, but the composed system became false?

If yes: instance of the gap. If no: different primitive.

## First formal skeleton (uncommitted)

Bare type-theoretic sketch, pre-sheaf:

```
LocalValid Γ i x          -- local validity at index i
Compatible Γ i j xᵢ xⱼ    -- pairwise compatibility on overlap
GloballyCoherent Γ xs     -- collection-level coherence
GlobalValid Γ xs          -- global validity
```

Anti-laundering target:

```
(∀ i, LocalValid Γ i xᵢ)  does not imply  GlobalValid Γ xs
```

The missing middle (provisional):

```
LocalValid everywhere
 ∧ Compatible across overlaps
 ∧ Continuity preserved
 ∧ No obstruction
 → GlobalValid
```

Sheaf vocabulary (cover / local section / compatibility / gluing / obstruction) available as probe. **Not committed.** Math serves the shovel; cut it if cases can't ground each term.

## Relation to admissibility

- Admissibility: *was this step allowed?*
- Local-Global Validity Gap: *do allowed steps compose?*

Adjacent but distinct. Admissibility lives at one cut; this lives at the composition of cuts. The six non-collapsible boundaries in the admissibility family are about what gets admitted; this is about what survives gluing.

## Anti-promotion rules

- Do not call this "sheaf cybernetics." Sheaf as probe only.
- Do not number a paper. Lives in working/ until ratification.
- Do not lift to Lean yet — kernel vocabulary unstable.
- Do not laundry every locally-correct/globally-broken failure into this. Many will be better-served by existing absorbers.

## Open questions

- Is the compatibility/gluing structure formalizable without sheaf machinery, or does the math become load-bearing?
- Do the four axes require distinct obstruction classes, or share one?
- What's the smallest example where the gap is *not* explainable by a single-frame existing absorber? (That example earns the primitive its keep.)

## Keeper

> Locally valid operations can compose into a globally false system.
