# Surface-Deformation-Requires-Coupling — candidate kernel

**Field-guide name:** TBD (no demon-name yet from the exchange). **Lean / doctrine name:** `SurfaceDeformationRequiresCoupling`. **Same object, two surfaces — not two candidates** (when a demon-name lands).

**Filed:** 2026-06-05. **Status:** v3 landed in corpus 2026-06-05. **Lean source at `~/git/lean/LeanProofs/Scratch/SurfaceDeformationRequiresCoupling.lean`** (430 lines including category-2 prelude). Not imported by `LeanProofs.lean`; not part of any 1.0 surface. Category-2 fenced scratch per the BoundaryTransit pattern. **Direct `lake env lean` check clean as of 2026-06-06** after corrections (Iff parenthesization in struct fields; five proof bodies rewritten for Lean 4 core compatibility — see [`lean-custody-ledger-2026-06-06.md`](lean-custody-ledger-2026-06-06.md) § Checked Scratch).

**Lean custody:** authoritative checked scratch source is `~/git/lean/LeanProofs/Scratch/SurfaceDeformationRequiresCoupling.lean`. Markdown Lean blocks below are explanatory mirrors only.

**Layer tag:** **`NoLift`** (atomic — single-step kernel). Composition sibling at **`NoChainMagic`** — see § Frontier.

## Claim

> **A candidate surface may differ from the original only if the difference is behaviorally witnessed by a typed coupling whose label matches its transform and whose effects are bounded by scope, horizon, and anti-retroactivity.**

Short form:

> **Show the coupling witness, and show that the label isn't lying.**

## The kernel shape (per v2 + envelope theorem)

The kernel models event-induced surface deformation:

- `Surface Claim` is an admissibility predicate: `admit : TimedClaim Claim → Prop`.
- `Event` carries `timestamp`.
- `SurfaceDeformation Claim` carries `deformationType : DeformationKind` (an enum: expandAuthority / contractAuthority / lowerThreshold / raiseThreshold / openPath / closePath / quarantineSurface / expireStanding / demoteConstraintToTestimony / convertTestimonyToConstraint) and `transform : Surface Claim → Surface Claim`.
- `applyDeformation surface delta := delta.transform surface`.
- `CouplingWitness event surface delta` is **indexed to all three** and carries:
  - `horizon : Nat` — upper bound on the deformation's temporal effect
  - `scope : TimedClaim Claim → Prop` — spatial restriction
  - `wellTyped : DeformationWellTyped surface delta` (the label-must-match-transform predicate; see § Type-design lessons)
  - `withinHorizon : event.timestamp ≤ horizon`
  - `antiRetroactive : ∀ c, c.timestamp ≤ event.timestamp → (surface.admit c ↔ (applyDeformation surface delta).admit c)`
  - `afterHorizonInvariant : ∀ c, horizon < c.timestamp → (surface.admit c ↔ ...)`
  - `outsideScopeInvariant : ∀ c, ¬ scope c → (surface.admit c ↔ ...)`
- `EffectiveSurface event surface candidate` is the relational `Prop` admitting only:
  - `original : SurfaceEquiv candidate surface → EffectiveSurface ...`
  - `deformed delta : CouplingWitness event surface delta → SurfaceEquiv candidate (applyDeformation surface delta) → EffectiveSurface ...`

Where `SurfaceEquiv left right := ∀ claim, left.admit claim ↔ right.admit claim` (behavioral, not intensional).

## The conservation law (in v3 — derivable from existing invariance fields)

> **No admissibility difference outside witnessed support.**

The envelope theorem is *derivable* — it falls out of the three invariance fields the v2 kernel already carries (`antiRetroactive` / `outsideScopeInvariant` / `afterHorizonInvariant`). Three contrapositives, one per field. The conservation law was always implied by the witness; the v3 patch just states it as one object. **Not a Frontier ticket** — it belongs in `SurfaceDeformationRequiresCoupling.lean` today.

Theorem: **`deformation_difference_within_envelope`** — if `surface` and `applyDeformation surface delta` differ on a claim `c`, then `c` falls inside the deformation envelope (`event.timestamp < c.timestamp ∧ c.timestamp ≤ w.horizon ∧ w.scope c`). Equivalently: outside the envelope, admissibility is conserved.

Keepers — three altitudes of the same rule:

- **Doctrine altitude:** *Lawful backreaction has compact witnessed support.*
- **Brutal altitude:** *No curvature without source.*
- **Operational altitude:** *If the surface changed here, show the source term.*

This is the corpus-wide rule for any predicate-deformation kernel; see [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) § Cross-cutting type-design rules § The conservation law for the doctrine-map-altitude statement.

Lean (added to v3 in claude-web sandbox 2026-06-05; pending paste to `~/git/lean/LeanProofs/Scratch/`):

```lean
/-- Behavioral disagreement between two surfaces at a particular claim. -/
def SurfaceDiffers {Claim : Type u}
    (left right : Surface Claim)
    (claim : TimedClaim Claim) : Prop :=
  ¬ (left.admit claim ↔ right.admit claim)

/-- The live envelope in which a valid deformation may differ from the base
    surface: after the triggering event, inside the named scope, at or before
    horizon. -/
def InDeformationEnvelope {Claim : Type u}
    (event : Event)
    {surface : Surface Claim}
    {delta : SurfaceDeformation Claim}
    (w : CouplingWitness event surface delta)
    (claim : TimedClaim Claim) : Prop :=
  event.timestamp < claim.timestamp ∧
    claim.timestamp ≤ w.horizon ∧
      w.scope claim

/-- Conservation law for lawful backreaction: if the old and deformed surfaces
    disagree at a claim, that claim must lie inside the witnessed deformation
    envelope. No admissibility difference exists outside witnessed support. -/
theorem deformation_difference_within_envelope {Claim : Type u}
    (event : Event)
    (surface : Surface Claim)
    (delta : SurfaceDeformation Claim)
    (w : CouplingWitness event surface delta)
    (claim : TimedClaim Claim)
    (h_diff :
      SurfaceDiffers surface (applyDeformation surface delta) claim) :
    InDeformationEnvelope event w claim := by
  constructor
  · by_contra h_not_after
    have h_le : claim.timestamp ≤ event.timestamp :=
      Nat.le_of_not_gt h_not_after
    exact h_diff (w.antiRetroactive claim h_le)
  constructor
  · by_contra h_not_within
    have h_after : w.horizon < claim.timestamp :=
      Nat.lt_of_not_ge h_not_within
    exact h_diff (w.afterHorizonInvariant claim h_after)
  · by_contra h_outside
    exact h_diff (w.outsideScopeInvariant claim h_outside)
```

`by_contra` + `Nat.le_of_not_gt` / `Nat.lt_of_not_ge` chosen over `push_neg` to be less import-goblin-prone.

## Type-design lessons (v1 → v2 → v3)

The v1 → v2 repair cycle exposed three rules that apply across the corpus, now filed in `anti-laundering-doctrine-map.md` § Cross-cutting type-design rules. Worked examples in this kernel:

1. **Behavioral equivalence, not intensional equality.** v1 used `candidate = surface` (propositional equality on a structure wrapping a `Prop`-valued function). Two extensionally identical surfaces weren't `=`. v2 introduced `SurfaceEquiv left right := ∀ c, left.admit c ↔ right.admit c` and restated the collapse theorems against it.
2. **Enum labels are testimony unless enforced.** v1's `deformationType : DeformationKind` was unconstrained testimony — a `.contractAuthority` label could be attached to a transform that *expanded* authority, and every theorem went through. v2 added `DeformationWellTyped surface delta` requiring label-shape-match (e.g., for `.contractAuthority`, `SurfaceImplies deformed surface`) and threaded it through `CouplingWitness.wellTyped`. **Sharp move:** v2 set `convertTestimonyToConstraint => False` deliberately — coercive category change cannot be certified honestly at this abstraction; needs a richer model than one admissibility predicate. Refuses the "signed label is witness" sin inside the kernel.
3. **Drop unconsumed Boolean flags.** v1's `requiresAdditionalWitness : Bool` was set on permissive/coercive deformations but no theorem consumed it. v2 deleted it. *"Vibes with a badge"* per the audit unit — a Boolean warning that no theorem enforces is testimony, not constraint.

## Managed insufficiency (the design discipline this kernel encodes)

> **Backreaction is managed insufficiency: the system permits bounded, witnessed loss of perfect recoverability so admitted events can lawfully deform the surface — *charged gross, not net, because cancellation is not the same as never having spent.***

The coupling witness is the licensed defect in perfect recoverability. The discipline is *neither* uncontrolled leakage *nor* perfect isolation — it is bounded, witnessed, temporary recoverability loss. Each witness field in `CouplingWitness` maps onto one face of preserved recoverability:

| Witness field | What it preserves |
|---|---|
| `antiRetroactive` | past recoverability |
| `outsideScopeInvariant` | out-of-scope recoverability |
| `afterHorizonInvariant` | post-window recoverability |
| `wellTyped` | the advertised deformation matches behavior (no label-lying) |

The conservation law (§ above) is the *aggregate* statement of this: behavioral difference is bounded by the envelope; outside it, recoverability is conserved. *A perfectly protected surface is inert. Legitimate deformation requires managed insufficiency.*

## Frontier: `SurfaceDeformationCompositionRequiresWitness` (NoChainMagic layer)

The v3 kernel is single-step from a fixed base. Chained deformations open horizon-laundering: s₀ → s₁ (witness w₁, horizon h₁) → s₂ (witness w₂, event at h₁, horizon h₂). Each step's witness is valid; the composite extends effect past any single horizon. **Same goblin, temporal trench coat.** Salami-sliced emergency powers.

**Core sentence (per the 2026-06-05 gross-vs-net round):**

> *Stepwise valid deformations do not silently compose; a composite witness must account for the gross ledger of behavioral flips, because cancellation is not the same as never having spent.*

### One family, not two paths

claude-web's earlier round proposed two lawful paths — show a composite witness, OR show a bounded spend ledger. The gross-vs-net analysis collapses them into one family: **the spend ledger IS the composite witness, in receipt form.** *A composite witness is a ledger you've proved closed.* The flip-count cost is honest *now* (read off the transform's actual behavior, not asserted), so the budget law isn't a separate kernel — it's the custody layer of the composition witness.

Mapping (per the corpus's four-receipt vocabulary):

| Layer | What it is |
|---|---|
| Spend ledger | **custody receipt** — the per-step gross flip-count, accumulated |
| Composite witness | **claim receipt** asserted over the spend ledger — proves the ledger closes inside a combined lawful envelope |

Same custody chain, different compression. Frontier-1 (`NoSilentSurfaceComposition`) and Frontier-2 (`RecoverabilityBudget`) from the prior round are the same object at different compression levels; recorded here as one family.

### Why charged gross, not net

Salami-slicing's signature is **small net endpoint difference + large gross per-step spend**. Round-trip a verdict (flip to admit at step 1, flip back at step 7) and the endpoint shows zero while the chain extended the effective horizon arbitrarily. Net is laundering-blind. The witness must be over the *gross* ledger. **Net is fakeable; gross isn't.**

### The honest flip-count cost (visor removed)

```text
spend(surface, delta) :=
  | { c ∈ envelope : ¬ (surface.admit c ↔ deformed.admit c) } |
```

The spend is computed from the transform's actual behavior, not asserted. The goblin doesn't get to write the number — it's read off the transform itself. The budgeted witness carries a **proof** that the derived flip-count is bounded, not a stipulated cost value:

```lean
structure BudgetedCouplingWitness
    (event : Event) (surface : Surface Claim) (delta : SurfaceDeformation Claim) where
  coupling   : CouplingWitness event surface delta
  budget     : Nat
  affordable : spend surface delta ≤ budget   -- derived, not declared
```

Per [[documentation-keepers]] keeper *"No fairy dust in the kernel"* — the line is *no asserted cost*, not *no cost*. Flip-count is honest because it's read; magic / complexity cost still isn't because it would require a notion of "simulate" not yet definable. Quarantine and authority-expansion (opposite political direction, identical stability spend) cost the same flip-count, which was the clarifying insight that earned the visor's removal.

### Composition status

**Per the layer-map discipline:** do NOT create a `LeanProofs/Admissibility/NoChainMagic/` directory or a parallel artifact yet. Composition family held as Frontier here; promote to its own candidate file only when a downstream consumer needs the gross-ledger composite witness mechanically.

**Practical blocker:** defining `spend` as a finite count requires either a `Finset (TimedClaim Claim)` domain or a measure. A real spend model needs a finite-claim-domain instantiation; the single-step kernel has no such domain because its `Claim` parameter is arbitrary `Type u`. The composition family is where the finiteness obligation has to be met — likely as a side-condition on the instantiating consumer, not as a kernel-wide axiom.

## Research note: the cleaned conjecture (NOT a kernel claim)

claude-web's original "magic cost" / Clifford-simulable framing was poetry with a badge — assumed an undefined complexity model over surfaces and transforms. The cleaned conjecture survives separately as a research-note shape, NOT as a kernel claim:

> **Conjecture (research note, not a kernel claim).** Nontrivial authoritative deformation has a complexity floor relative to the undeformed surface. If a deformation can be simulated by the original surface without loss of behavioral equivalence, it carries no new authority.

Careful phrasing: the conjecture is *not* "expensive means real." It is *"if it adds no behavior the old surface could not already represent, it is not a real deformation."* The corpus already expresses this much via `SurfaceEquiv` and the no-op collapse — *"a deformation collapses to no-op only if it is behaviorally equivalent to the original surface."* The cost / complexity version requires a separate primitive ("simulate") not yet definable in the kernel.

**Disposition:** stays as a research note here. Does NOT enter the Lean file as a theorem, an axiom, or a structural assumption. Per *"no fairy dust in the kernel"*: we already had to evict one enum for loitering; we are not re-introducing it under a complexity badge.

## v2 → v3 patch list (status 2026-06-05)

The v3 file in claude-web's sandbox carries items 1–7 below. The kernel is **"done enough to throw at the repo and let Lean be rude"** per the user's 2026-06-05 ledger. Pending operator paste to `~/git/lean/LeanProofs/Scratch/SurfaceDeformationRequiresCoupling.lean`.

1. ✅ `SurfaceEquiv` (behavioral equivalence) — v2
2. ✅ `DeformationWellTyped` + `CouplingWitness.wellTyped` field — v2
3. ✅ Removed `requiresAdditionalWitness` — v2
4. ✅ `EffectiveSurface` uses `SurfaceEquiv` — v2
5. ✅ `coupling_at_horizon_is_noop` lemma — v2
6. ✅ Composition deferred Frontier — v2 (refined in v3 to the single composition family with gross-ledger custody layer; see § Frontier)
7. ✅ `SurfaceDiffers` + `InDeformationEnvelope` + `deformation_difference_within_envelope` — **the conservation law (envelope theorem). Added to v3 by claude-web 2026-06-05.** Three contrapositives from existing witness fields; `by_contra` + `Nat.le_of_not_gt` / `Nat.lt_of_not_ge` instead of `push_neg`. Stated behaviorally via `SurfaceDiffers` (non-equivalence form), dodging `propext`.

## Sketch shape (NOT a build spec — name-early only)

See § The kernel shape, § The conservation law, and § v2 → v3 patch list above. The full v2 `.lean` source is in claude-web's sandbox; v3 (with the envelope theorem) would extend it. Both are category-2 scratch per the BoundaryTransit pattern — **not** imported into `LeanProofs.lean` and not public testimony. Public promotion requires a separate proof, overlap, custody, and compatibility review; a downstream consumer may supply evidence but is not mandatory permission.

## Phrasing note (load-bearing)

Per the master frame's audit-unit framing: the kernel does NOT prove "no other admissible surface exists." It proves *"this candidate surface does not discharge the effective-surface predicate without an indexed coupling witness whose label matches its transform and whose effects are bounded by the conservation envelope."* Type-accusation form, not equation-negation form.

## Non-claims

- **Not a build spec.** v2 + the envelope theorem describe candidate shapes; the actual module would be designed against existing kernel conventions and Cedar-style differential-randomized-testing if/when promoted.
- **Not an automatic build queue.** Name-early per [[feedback-name-early]]. A bounded Scratch probe may proceed when the kernel shape, conservation theorem, overlap, and controls are coherent. A policy-evolution / amendment-discipline / waiver-renewal consumer would supply priority and correspondence evidence, not permission.
- **Not a position** on whether `LeanProofs/Admissibility/SurfaceDeformationRequiresCoupling.lean` should ever join the import surface. If it lands at all, it lands in `Scratch/` first per the BoundaryTransit pattern; public promotion requires a separate custody and compatibility review, not a mandatory consumer.
- **Not part of any `NoLift/` / `NoSilentJoin/` / `NoChainMagic/` parallel directory.** Layer tags only.
- **Not a model of all institutional policy evolution.** Scope fence — single-step deformation, scope/horizon/anti-retroactivity bounded, no coercive category change at this abstraction.

## Cross-references

- [`log-only-proves-emission-candidate-2026-06-05.md`](log-only-proves-emission-candidate-2026-06-05.md) — atomic-layer sibling (`NoLift`); different kernel, same layer tag.
- [`aggregate-witness-requires-join-candidate-2026-06-05.md`](aggregate-witness-requires-join-candidate-2026-06-05.md) — workflow-layer sibling (`NoSilentJoin`); Frankenstein Witness as field-guide name.
- [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) § The master frame; § Cross-cutting type-design rules (the conservation law, behavioral equivalence, enum-label rules surfaced from this kernel's review).
- [[documentation-keepers]] — keeper phrases from this round: *"Show the coupling witness, and show that the label isn't lying"*; *"No curvature without source"*; *"Lawful backreaction has compact witnessed support"*; *"If the surface changed here, show the source term"*; *"Enum labels are testimony unless enforced by a well-typedness predicate"*; *"Behavioral equivalence, not intensional equality."*
- `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` — category-2 scratch precedent for the eventual landing pattern of v2+v3 if/when the file gets pasted into the corpus.
- `~/git/lean/LeanProofs.lean` — current import surface; if this kernel ever promotes, verify gap against `SurfaceAuthorization` / `Composition` / `CrossBoundary*` / `WitnessInvariance` first.

## Provenance

Surfaced in 2026-06-05 multi-model exchange:

1. Original v1 of `SurfaceDeformationRequiresCoupling.lean` drafted in claude-web's sandbox (not in this corpus).
2. Claude-web reviewed v1, flagged five load-bearing problems (`requiresAdditionalWitness` unused; `deformationType` unconstrained testimony; raw propositional equality on surfaces; `EffectiveSurface` relational not selector — actually fine, kept; composition open).
3. Claude-web patched to v2 (items 1–6 in the patch list above).
4. Claude-web extended with the Bianchi-identity conservation law and the envelope theorem (item 7; proposed for v3, not yet in v2).
5. Claude Code kernel-overlap audit confirmed the kernel as a genuine gap (no overlap with `SurfaceAuthorization` / `Composition` / `CrossBoundary*` / `WitnessInvariance` per grep). Filed this candidate file; three corpus-wide type-design rules promoted to the doctrine map; six keepers added.

Lean source remains in claude-web's sandbox at v2 + the proposed v3 patch; **not yet pasted** into `~/git/lean/LeanProofs/Scratch/`. When operator pastes, the landing follows the BoundaryTransit category-2 scratch pattern.

Side-quest yield: candidate kernel at atomic-layer (`NoLift`) with the conservation law as the missing invariant, composition sibling held as Frontier (`NoChainMagic`), three corpus-wide type-design rules earned from the review-and-repair cycle.
