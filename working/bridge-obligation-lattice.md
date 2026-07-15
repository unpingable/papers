# Bridge obligation lattice — doctrine note

**Filed:** 2026-06-06. **Status:** doctrine note + Frontier marker. NOT a candidate Lean kernel. NOT a renaming of the project. NOT a new directory under `LeanProofs/Admissibility/`. Pre-ratified per name-early discipline; promotion gated on a worked Coupling-as-instance Lean spike.

**Naming discipline (load-bearing):** *"Admissibility Kernels" is the artifact name. "Calculus" is the deeper pattern the kernels instantiate, like mold in a Pittsburgh basement.* The 2026-06-03 calculus-vocabulary retirement still holds. This file is the doctrine note *underneath* Admissibility Kernels, not a rename attempt. The safe-form sentence: **together, the kernels suggest a calculus of admissible boundary crossings** — *suggest*, not *constitute*. The forbidden grandiosity stays in a footnote wearing an ankle monitor.

**Layer:** sits *underneath* the doctrine map's layer-map (`NoLift` / `NoSilentJoin` / `NoChainMagic`) as the orthogonal *"what does the crossing owe"* axis. Layer map factors by altitude (single-step / bundle / chain). Obligation lattice factors by preserved invariants. Both are useful; they're orthogonal.

## Static vs Dynamic kernels (the organizing axis)

The kernels split cleanly by what they refuse:

| Lane | What it refuses | Examples (existing + candidate) |
|---|---|---|
| **Static refusal kernels** | predicate discharge — *this evidence does not discharge that predicate* | `NoLift` instances (LogOnlyProvesEmission, ReceiptIsNotAuthority); `NoSilentJoin` (AggregateWitnessRequiresJoin); Freshness / SurfaceAuthorization / WitnessInvariance / ClosureEligibility / RecoveryMargin / CrossBoundary* / ConsolidationDenial / standing / receipt kernels |
| **Dynamic refusal kernels** | lawful mutation of the evaluation frame — *this transition cannot change what counts without preserving named obligations* | `SurfaceDeformationRequiresCoupling` (canonical Deform instance); checked Scratch `NoSilentProjection` (including the Deform/Exception separation); future candidate `NoSilentDelegation`; Revocation as a special case of Deform |

Static kernels are about *receipt ≠ authority, log ≠ truth, green ≠ covered, partial witnesses ≠ joined witness.* Dynamic kernels are about *event ≠ authority to change the surface, exception ≠ precedent, delegation ≠ amplification, projection ≠ source, deformation ≠ effective surface.*

**The sober positioning sentence:** *Backreaction is an annex to the kernel set that exposed a more general bridge-obligation layer.* The lattice in this file is the doctrine note explaining the common shape across dynamic kernels (and incidentally across some static ones — Join's coverage/preservation are obligation-set entries too).

## The doctrine line

> **A lawful crossing must say what it does not change.**

The obligation set IS the list of what the crossing doesn't change. Stated negatively:

> **A fog machine is a bridge with the empty obligation set.**

A "crossing" that names no preservation obligations is not a bridge — it's atmospheric. Same disease as the v1 SurfaceDeformation `requiresAdditionalWitness` Boolean (vibes with a badge), generalized to the taxonomy level. See [[documentation-keepers]] for both keeper forms.

## The recursive scar

> **The taxonomy must be admissible under its own NoSilentConversion.**

Classification claims are themselves claims. *"X is a specialization of Y"* must produce a `ConversionWitness X Y` or get refused. The discipline must catch its own architect. This is the load-bearing test against periodic-table-brain and against the move where four families get compressed to two by vibes. See § The NoSilentConversion gate below for the worked application that surfaced this rule.

## The obligation atoms (the actual primitives)

The bridge taxonomy is *not* by vocabulary — it is by **obligation set**. The primitives aren't the named crossings; they're ~5 preservation invariants a crossing may owe:

| Atom | What it preserves |
|---|---|
| **non-amplification** | output authority / capability ≤ input authority / capability |
| **temporal bounding** | scope + horizon + anti-retroactivity (the SurfaceDeformation witness fields) |
| **type fidelity** | advertised category matches behavior (the `DeformationWellTyped` discipline) |
| **freshness** | source / representation is valid within a time horizon (the `Freshness.lean` discipline) |
| **anti-precedent** | bypass does not mutate future rule meaning (the Exception-specific discipline) |

For workflow-altitude bridges (Join family), two more obligations apply that don't fit the single-step pattern:

- **coverage** — every required property is satisfied somewhere in the bundle
- **preservation** — the unified witness carries every required property forward

(These two are the `JoinWitness` two-field discipline from [[aggregate-witness-requires-join-candidate-2026-06-05]].)

## Bridge families as points in obligation-space

A bridge family is a **subset of these obligations**, not a box in a periodic table:

| Family | Obligation set |
|---|---|
| **Deformation** | {temporal-bounding, type-fidelity-if-labeled} |
| **Delegation** | {non-amplification, type-fidelity} |
| **Exception** | {temporal-bounding, anti-precedent} |
| **Projection** | {non-amplification, type-fidelity, freshness} |
| **Conversion** | {type-fidelity} (+ non-amplification if directionally upward) |
| **Join** (workflow) | {coverage, preservation, no-double-count, no-silent-amplification} |
| **Revocation** | reduces to Deformation; surface contraction/demotion with anti-retroactivity |
| **Lift** (atomic) | {type-fidelity}; the `NoLift` layer kernel canonical |
| **Escalation** | candidate; obligation set TBD, plausibly {non-amplification, type-fidelity} sharpened by capability-level monotonicity |

The taxonomy is a **lattice over obligations**, not a partition over vocabulary. Crossings can owe multiple obligations; families overlap when obligation sets overlap. This stops the false parent/child fights ChatGPT's "four plus satellites" cut produced.

## The NoSilentConversion gate (worked 2026-06-06)

ChatGPT's "opinionated cut" reduced nine bridge families to four-plus-satellites:

```text
Delegation = Convert authority-holder
Escalation = Convert capability level
Projection = Lift through representation
Exception  = Deform or bypass with horizon
Revocation = Deform/Convert downward
```

Run NoSilentConversion against the cut itself: does each child inherit the parent's obligations without needing a new preservation invariant?

- **Revocation = Deformation: HOLDS.** Surface contraction / demotion (literally `contractAuthority` / `demoteConstraintToTestimony` from the v3 SurfaceDeformation `DeformationType` enum), bounded by anti-retroactivity. Same obligation set. One honest reduction.
- **Delegation ≠ Conversion: FAILS.** Conversion changes the *type* while the bearer stays put. Delegation changes the *bearer* while the type stays put. Orthogonal axes. And Delegation carries an invariant Conversion has no analog for: **non-amplification** — B cannot receive more than A held. That's the entire agent-governance hellmouth: *"the system authorized this, so I'm authorized to do it"* is an unwitnessed delegation that *also* gained privilege. Conversion can't express that because it has no second principal.
- **Exception ≠ Deformation: FAILS.** A deformation changes the surface; an exception leaves the rule intact and bypasses it for a bounded window. Its defining invariant is the one Deformation structurally cannot have: **anti-precedent** — the bypass must not become precedent. An exception that changes future meaning is an illegal deformation with a siren taped to it. Reducing Exception to Deformation inverts its load-bearing property.
- **Projection ≠ Lift: FAILS.** Lift's danger is granting evidence *more* authority than it earned (upward arrow). Projection's danger is letting a lossy representation *stand in for* its higher-authority source — arrow points the other way. Projection smuggles in **freshness** that neither Lift nor Conversion carries: *"the dashboard says green"* — green of what, generated how, from which collector, under which freshness horizon.

**Pattern of failure:** every failed reduction fails by requiring a preservation clause the parent doesn't have. *Which is the unifier, recursed.* A lawful reduction must say what invariant it preserves from parent to child, exactly as a lawful crossing must say what it preserves. **Three of five reductions are silent conversions.** ChatGPT's taxonomy isn't admissible under its own calculus.

The test as a single rule:

> **A specialization is admissible only if it inherits the parent's obligations without needing a new preservation invariant.**

If the child needs an extra clause, it's a sibling wearing the parent's coat to keep the family count at four. See [[documentation-keepers]] keeper.

## The generic shape (with cautions)

There exists a generic witness underneath the families:

```lean
structure BridgeWitness (src tgt : Type u) (cross : src → tgt → Prop) where
  inEnvelope       : tgt → Prop
  preservesOutside : ∀ y, ¬ inEnvelope y → (/- source meaning -/ ↔ /- target meaning -/)
  -- plus whichever obligations from {non-amp, temporal, type, fresh, anti-precedent}
  -- this family owes
```

Every family instantiates `inEnvelope` and the cross relation differently and switches on its obligation set. The existing `CouplingWitness` (from the SurfaceDeformation v3 kernel) is the **Deform instance** of this generic, with the obligation set `{temporal-bounding, type-fidelity}` spelled out as the three invariance fields (`antiRetroactive` / `outsideScopeInvariant` / `afterHorizonInvariant`) plus `DeformationWellTyped`.

**Critical caution:** a too-generic `BridgeWitness` becomes **Receipt 2.0** if it can be inhabited without doing work. The abstraction earns its keep ONLY if `CouplingWitness` can be re-derived as a real instance and the existing SurfaceDeformation theorems still fall out. Until that spike compiles cleanly, the generic is doctrine only — not Lean.

## The Frontier note

> *Bridge families factor by obligation set, not by vocabulary. The taxonomy must be admissible under its own NoSilentConversion.*

The next artifact, if it happens, is one of:

- **Doctrine-first (this file).** Already shipped. A generic Lean spike is warranted only if the Coupling re-derivation poses a coherent, non-duplicative question; no consumer permission is required.
- **Lean spike:** `BridgeObligations.lean` as a category-2 scratch file with the generic `BridgeWitness` declared and `CouplingWitness` re-derived as its `Deform` instance. The existing v3 SurfaceDeformation theorems must still fall out. If they don't, the abstraction is goo and gets evicted.
- **NOT a `LeanProofs/Admissibility/BridgeObligations/` parallel directory.** Layer-map discipline: no roof for emerging taxonomies. The generic, if it ever lands, lands as a single file in `Scratch/`, not a hierarchy.
- **NOT one candidate-file-per-family.** Nine candidate files for the nine vocabulary families would be the periodic-table-brain failure mode. Families are points in obligation-space; document them in this lattice file as they're encountered, don't multiply files.

## What this doctrine says about existing kernels

The obligation-set framing organizes the corpus's existing kernels by *what they preserve*, not just by what they refuse. Sorted by static / dynamic lane:

**Static refusal kernels (predicate discharge):**

- **`LogOnlyProvesEmission`** (checked Scratch candidate) — owes {type-fidelity}; canonical NoLift instance at the audit-log altitude.
- **`SurfaceAuthorization.lean`** (standing-upgrade-block) — owes {non-amplification} at the surface level.
- **`Freshness.lean`** (metric-time decay) — owes {freshness} as a single-atom obligation; canonical instance.
- **`AggregateWitnessRequiresJoin`** (checked Scratch candidate) — owes {coverage, preservation, no-double-count}.
- **`ConsolidationDenial.lean`** (fluency ≠ settlement) — owes {type-fidelity, anti-precedent? — verify}.
- **`ClosureEligibility.lean`** + **`RecoveryMargin.lean`** — owe {coverage, type-fidelity}.
- **`CrossBoundary*`** family — owe {type-fidelity} at surface boundaries; revocation cases reduce to Deform (see below).
- **`WitnessInvariance.lean`** — owes {type-fidelity, non-amplification} at the regime axis.

**Dynamic refusal kernels (lawful mutation of the evaluation frame):**

- **`SurfaceDeformationRequiresCoupling v3`** (this round's kernel) — owes {temporal-bounding, type-fidelity}; **canonical Deform instance.**
- Revocation (special case) — reduces to Deformation via `contractAuthority` / `demoteConstraintToTestimony`; owes {temporal-bounding, anti-retroactivity}.
- `NoSilentProjection` now has a checked, fenced Scratch realization at `~/git/lean/LeanProofs/Scratch/NoSilentProjection.lean`. It reuses the resident obligation table, proves Lift cannot discharge Projection's freshness/non-amplification obligations, and proves both directions of the Deform/Exception separation (missing anti-precedent vs. missing type-fidelity). `NoSilentDelegation` remains prose-only. Further family files require distinct theorem content and overlap review, not a forcing case.

Each kernel's obligation set is its actual signature. The vocabulary name (NoLift / NoSilentJoin / NoChainMagic / Deform / etc.) is a *handle* over the signature, not the signature itself.

## Anti-cathedral discipline

Per the carry-forward from the 2026-06-04 / 2026-06-05 audits:

- **Do not** build `LeanProofs/Admissibility/BridgeObligations/` as a parallel directory.
- **Do not** create candidate files for the nine vocabulary families. Families are points in obligation-space; the lattice file IS the doctrine.
- **Do not** promote the generic `BridgeWitness` to a Lean file before the Coupling-re-derivation spike compiles.
- **Do not** treat "X is a specialization of Y" as a free move. ConversionWitness or refusal.
- **Do** revisit this file when a new kernel surfaces — add its obligation set; check whether it's a real new family or a sibling wearing a coat.

## Artifact-discharge discipline (added 2026-06-06)

The lattice and its kernel instances are one artifact-kind. They do NOT discharge the obligations of other artifact-kinds. Surfaced 2026-06-06 in AG Claude's review of this batch + ChatGPT's pocketing call. The full block lives in [[documentation-keepers]] § Multi-clause doctrine blocks; the operational summary:

> **Different artifacts discharge different obligations.** Lean kernels may identify/refuse a formal conversion; NQ gaps are discharged only by receipt, verdict, export, or runtime behavior; related-work maps record route signs and neighbors; external convergence supplies pressure, not implementation authority.

**Danger rule** (load-bearing for this lattice in particular): *the more the Lean kernels line up with NQ gaps, the more dangerous they become to NQ's filing discipline.* Similarity creates temptation: *"this theorem proves the gap shape, therefore NQ can mark the gap handled."* Wrong. A kernel in this lattice with obligation set `{X, Y}` refuses a class of formal conversions; it does NOT close an NQ gap that requires receipt-form discharge. The obligation-set framing makes this *more* dangerous, not less, because subset reasoning over obligation sets gives the goblin a typechecker for the wrong job.

When using this lattice to navigate NQ work or any other downstream consumer: route signs, not territory. Formalization may lead by fixing the obligation shape first. Runtime implementation still needs an explicit mapping, product priority, and evidence plan; the lattice is not a record that those calories have been spent.

## Cross-references

- [`anti-laundering-doctrine-map.md`](anti-laundering-doctrine-map.md) § The master frame — the doctrine altitude this lattice extends; layer-map (NoLift/NoSilentJoin/NoChainMagic) sits orthogonally.
- [`tooltheory/surface-deformation-requires-coupling-candidate-2026-06-05.md`](tooltheory/surface-deformation-requires-coupling-candidate-2026-06-05.md) — the Deform-instance canonical case; `CouplingWitness` is `BridgeWitness` + `{temporal-bounding, type-fidelity}`.
- [`tooltheory/aggregate-witness-requires-join-candidate-2026-06-05.md`](tooltheory/aggregate-witness-requires-join-candidate-2026-06-05.md) — the Join-instance canonical case; obligation set `{coverage, preservation}`.
- [`tooltheory/log-only-proves-emission-candidate-2026-06-05.md`](tooltheory/log-only-proves-emission-candidate-2026-06-05.md) — the Lift-instance canonical case; obligation set `{type-fidelity}` at the audit-log altitude.
- [[documentation-keepers]] — keepers from this round: *"A lawful crossing must say what it does not change"*; *"A fog machine is a bridge with the empty obligation set"*; *"The taxonomy must be admissible under its own NoSilentConversion"*; *"A specialization is admissible only if it inherits the parent's obligations..."*

## Provenance

Surfaced in 2026-06-06 multi-model exchange (ChatGPT proposing nine bridge families + the "four plus satellites" opinionated cut → claude-web running NoSilentConversion against the cut and catching three of five reductions as silent conversions → user / claude-web jointly proposing the obligation-set factorization → user landing the doctrine pair as keepers → Claude Code kernel-overlap audit confirming the obligation-set model is a genuine doctrine-level reframe orthogonal to the existing layer-map, filed this lattice doctrine file and the four keepers). The cut was a silent conversion; the test caught its own architect. The scar stays visible.
