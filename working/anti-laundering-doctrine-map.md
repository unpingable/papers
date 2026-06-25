# Anti-Laundering Doctrine Map

**Filed:** 2026-06-04. **Status:** family map. Names what's covered, what's candidate, what's adjacent. Prevents candidate-explosion from looking like orphaned doctrine acne.

## The master frame: missing conversion witness

**Filed 2026-06-05** as the compression surface for what the family below actually *is*.

> **The admissibility corpus can be read as a laundering detector: it rejects silent promotions between institutional object-kinds unless a conversion witness binds the source, target, surface, scope, and issuing authority.**

The family table below enumerates *which* silent promotions are refused. The master frame names *why* they share a shape: each row is a forbidden conversion from one kind of institutional object (receipt, log, status, label, observation, policy allow, prior validity, partial coverage) into another (authority, truth, coverage, enforcement, standing, execution right, current validity, total coverage). A conversion may proceed *only* through a witness whose type binds the conversion itself — not merely the destination kind.

**The conversion-witness binding rule.** A witness "supporting authority" generically is a skeleton key and re-introduces the laundering surface the kernel is supposed to refuse. A typed conversion witness must bind:

- **source kind** (what is being converted from)
- **target kind** (what is being converted to)
- **surface / object** (which specific thing the conversion attaches to)
- **scope / time** (when and where the conversion is valid)
- **issuer / authority** (who minted the witness, under what standing)

Destination-only witnesses are not witnesses; they are unmarked claims. This rule operationalizes [`tooltheory/admissibility-related-work-map.md`](tooltheory/admissibility-related-work-map.md) § Substrate guidance § Candidate carrier sketch guardrail #5 at the doctrine-map altitude.

**Provenance.** Surfaced in a multi-model exchange 2026-06-04 (ChatGPT extending the Lean-underexposed-lane idea → DeepSeek sketching candidate kernels → ChatGPT correcting the destination-only-witness trap → kernel-overlap audit confirming non-novel-substance / novel-compression). The frame is keep-worthy; the parallel `LeanProofs/Admissibility/NoLift/` directory the exchange briefly proposed was refused as cathedral-by-rename — the kernels it would contain already exist as named modules in `LeanProofs.lean`'s import surface. See [[documentation-keepers]] for the *"Lean as laundering detector"* keeper phrase.

### Two axes of the conversion failure: TOCTOU (temporal) vs laundering (type) — added 2026-06-22

The master failure — *a check does not license a use* — fails along two orthogonal axes,
which map onto two fields of the conversion-witness binding rule above:

- **Temporal axis (scope/time binding fails) = TOCTOU.** The check *was* the right kind of
  evidence and *was* valid; time passed; the bound state moved. Time-of-check-to-time-of-use.
  This is the corpus's freshness / temporal-custody seam — formalized as
  `TemporalCustody.lean`'s `citation_validity_does_not_imply_execution_admissibility`
  (valid-at-check ⊬ admissible-at-use), surfaced as an attack surface in P14
  (temporal-attack-surface) and P15 (cybernetic-fault-domains: FileSnapshot + stale-base
  detection is the operational TOCTOU defense), and rowed in `laundering-move-watchlist.md`.
- **Type / jurisdiction axis (source/target-kind binding fails) = the laundering kernels.**
  *No time needs to pass.* The check was never the right *kind* of evidence for the use —
  a venue-state read as a world-state, an aggregate read as an instance, a settlement read
  as truth. `signed≠witnessed`, `resolved≠true`, `calibrated≠correct`, `priced≠witnessed`.
  No race, zero-length window, same "check ⊬ licensed use" failure.

TOCTOU is therefore **no-free-standing-bridge on the temporal axis**; the laundering family
is **no-free-standing-bridge on the type axis**. TOCTOU is named prior art (McPhee 1974
coined the term; Bishop & Dilger 1996 formalized the file-race version) — cite, don't coin;
the corpus's move is (a) lifting it off the filesystem substrate into authority/admissibility
vocabulary and (b) placing it as one axis of a two-axis failure whose other axis has no
TOCTOU analog. One sharpening the systems literature lacks: the temporal-custody theorem
refuses the lift by default *even with a zero-length race window and no state change* —
validity is evaluated at execution time, not citation time, so citation-time validity never
transfers without an explicit retroactive-discharge bridge made visible in the proof. That
is stronger than "minimize the race window." Both fixes also share a shape: TOCTOU's
*atomicity* fix = the handoff-atomicity / Governor-serializes-non-commutative-transitions
note; TOCTOU's *capability* fix = the witness-carrier model (carry the witness through to
use, don't re-resolve a stale name).

### The layer map (added 2026-06-05)

The master frame applies at three layers. Each layer names a refusal and a missing mediating object:

| Layer tag | Refusal | Missing object |
|---|---|---|
| **`NoLift`** | No silent lift | Conversion witness (source kind → target kind) |
| **`NoSilentJoin`** | No silent join | Join witness (bundle ⊨ requirements) |
| **`NoChainMagic`** | No self-certifying chain | Composite witness (chain ⊨ promotion) |

These are **layer-tags, not a module/directory hierarchy.** The 2026-06-04 audit refused a parallel `NoLift/` directory as cathedral-by-rename; the same refusal extends to `NoSilentJoin/` and `NoChainMagic/`. The atomic-layer instances are the family rows below (already mapped to existing modules). The workflow-layer kernel is held as candidate: [`tooltheory/aggregate-witness-requires-join-candidate-2026-06-05.md`](tooltheory/aggregate-witness-requires-join-candidate-2026-06-05.md). The sequence-layer claim is shaped but has no candidate file yet; no downstream consumer has earned the build.

**Meta-discipline (the keeper):** *Indexed or it didn't happen.* A mediating object is admissible only when indexed to the exact objects it mediates — the conversion witness binds source AND target; the join witness binds bundle AND requirements; the composite witness binds the chain. Unindexed witnesses are **existential laundry** — a witness exists somewhere, therefore treated as applicable here. Same disease across all three layers; same fix across all three layers; same goblin in increasingly elaborate costumes.

**Type-level lesson:** *the theorem is less important than the type you cannot construct.* Refusal lives at the API boundary as an uninhabited argument position, not as a failed match at runtime. The corpus's existing instances: BoundaryTransit's witness-must-be-OUTPUT discipline; the typed-revocation pattern in `CrossBoundary*` modules where `isRevocable Receipt = false` makes the `ValidRevocation` constructor uninhabited for receipts. The negative theorem is one line; the indexed type structure is the argument.

**Provenance (workflow-layer extension).** 2026-06-05 multi-model continuation (ChatGPT extending the workflow-not-more-Pokémon idea → DeepSeek sketching workflow kernels → ChatGPT correcting the unindexed-join trap → DeepSeek refining with the two-field discipline → ChatGPT promoting the meta-rule to *"indexed or it didn't happen"* and naming *"existential laundry"* → Claude Code kernel-overlap audit confirming workflow-layer as genuine gap). Keepers in [[documentation-keepers]]; candidate kernel in tooltheory.

### The audit unit and operational discipline (added 2026-06-05)

**Comprehensive framing (the whole cursed pocket knife):**

> *This is formal claim-admissibility auditing for institutional speech acts: given a sentence doing institutional work, identify the predicate it tries to discharge, the evidence actually present, the witness actually required, and prove that the present evidence cannot discharge the predicate unless an indexed witness is produced.*

**The audit unit:** *This evidence does not discharge that predicate.*

The corrected formulation (load-bearing): the corpus does NOT prove "no witness exists." It proves *"the present evidence cannot discharge the required predicate without the indexed witness."* The organization may have the witness elsewhere — produce it. *X ≠ Y* is a type joke; *X cannot discharge P without witness W* is a type accusation.

**The 7-step procedure** (operationalizes the audit-unit at every level — atomic, workflow, sequence):

1. Find the sentence people routinely get away with saying.
2. Find the predicate it is being used to discharge.
3. Find the evidence actually present.
4. Find the witness the predicate actually requires.
5. Show that the present evidence type cannot construct / discharge the required witness type.
6. Index the witness to the exact actor / object / scope / time.
7. Name the theorem as the sentence people can no longer say without producing the missing object.

**Human interface:** *Ask for the missing witness.*

**Field-guide vs Lean naming.** Workplace-demon names and Lean/doctrine names are *the same object, two surfaces* — not two candidates. The naming split is curated in [[documentation-keepers]] and at the per-candidate header in `tooltheory/`. Filed examples:

| Field-guide name | Lean / doctrine name |
|---|---|
| Frankenstein Witness | `AggregateWitnessRequiresJoin` |
| (no candidate yet — atomic) | `LogOnlyProvesEmission` |

Do not split a single object into a field-guide candidate AND a Lean candidate. They are two surfaces of one kernel.

**Field-guide schema** (the human-facing format; held in [`tooltheory/admissibility-field-guide-2026-06-05.md`](tooltheory/admissibility-field-guide-2026-06-05.md)):

- Demon — workplace-demon name
- Common sentence — the institutional speech act
- Predicate being discharged — what the sentence claims to settle
- Evidence actually present — what was actually shown
- Required witness — the indexed witness that would discharge the predicate
- Refusal — the audit-unit statement
- Meeting incantation — the human-interface ask

### Cross-cutting type-design rules (added 2026-06-05)

Three rules surfaced in the 2026-06-05 SurfaceDeformation review/repair cycle. Each applies across the corpus, not just to that kernel.

**The conservation law (No curvature without source).** Any modification to an admissibility surface or predicate has compact witnessed support. Outside the witness envelope (after the event, inside scope, at or before horizon), admissibility is conserved. Operational form: *if the surface changed here, show the source term.* GR analogy: event = source term; coupling witness = field equation; surface difference = curvature; scope + horizon = support of perturbation; invariance guards = conservation constraints. Applies to: any kernel where a predicate evolves over time. Worked theorem shape (from the SurfaceDeformation candidate, v3): `deformation_difference_within_envelope` — if old and deformed surfaces differ on a claim, the claim must satisfy `event.timestamp < claim.timestamp ≤ w.horizon ∧ w.scope claim`. **The theorem is *derivable* — three contrapositives from the witness's `antiRetroactive` / `afterHorizonInvariant` / `outsideScopeInvariant` fields, not a new axiom.** The conservation law is always implied by a correctly-fielded witness; the worked theorem just states it as one object. Keepers: *"No curvature without source"* / *"Lawful backreaction has compact witnessed support"* / *"If the surface changed here, show the source term."*

**The composition refinement (gross, not net).** When the conservation law extends to chained deformations, the budget must be charged **gross**, not net, because cancellation is not the same as never having spent. Salami-slicing's signature is small net endpoint difference + large gross per-step spend; a chain that flips a verdict at step 1 and flips it back at step 7 shows zero net endpoint while extending the effective horizon arbitrarily. Honest cost model: flip-count `spend(surface, delta) := | { c ∈ envelope : verdict flipped } |`, read off the transform's actual behavior — not asserted. The composition witness is the spend ledger proved closed; budget ledger and composite witness are not two paths but two compression levels of the same custody chain (custody receipt and claim receipt over it, respectively). Applies to: any kernel where chained predicate-deformations could re-introduce horizon-laundering. Keepers: *"Net is fakeable; gross isn't"* / *"A composite witness is a ledger you've proved closed"* / the *charged gross, not net* clause on the managed-insufficiency doctrine line.

**Behavioral equivalence, not intensional equality.** When kernels compare admissibility predicates, surfaces, or witness types, the comparison must be behavioral (`∀ claim, left.admit claim ↔ right.admit claim`), not intensional propositional equality (`left = right`). Without `funext`/`propext`, two extensionally identical surfaces aren't structurally `=`, and the corpus refuses claims about *behavior*, not about *function objects*. The v2 SurfaceDeformation patch concretized this as `SurfaceEquiv`. Applies to: any kernel comparing predicates / surfaces / witness types / admissibility decisions. Without this rule, theorems prove something stronger than the corpus semantically needs and end up false or unprovable for behaviorally-identical-but-structurally-distinct inputs.

**Enum labels are testimony unless enforced by a well-typedness predicate.** An enum constructor naming a transform (e.g., `deformationType : ContractAuthority`) is unwitnessed testimony about behavior until threaded through a predicate that constrains the transform to actually match the label. Same disease as a self-asserted JSON `{"basis": "external"}` field, one floor up — *the label is not the witness* applied to enum constructors. Worked example: the SurfaceDeformation v2 patch added `DeformationWellTyped` requiring (for `contractAuthority` labels) `SurfaceImplies deformed surface`; without the predicate, a `.contractAuthority` label could be attached to a transform that *expands* authority, and every theorem in the file would go through unbothered. Per [[documentation-keepers]] keeper: *"Enum labels are testimony unless enforced by a well-typedness predicate."* Applies to: any enum-bearing kernel where the label asserts something about the carrier's behavior.

**Provenance.** These three rules surfaced in the 2026-06-05 claude-web review of `SurfaceDeformationRequiresCoupling` (v1) + claude-web's v2 repair pass + the Bianchi-identity conservation-law extension. Candidate file with full kernel description: [`tooltheory/surface-deformation-requires-coupling-candidate-2026-06-05.md`](tooltheory/surface-deformation-requires-coupling-candidate-2026-06-05.md).

## The family

Each row names one *bad inference* the corpus exists to refuse. The right-hand column points at the Lean modules or candidates that own the refusal at the formal layer; the left-hand column names the family so a new instance can be classified before being filed.

| Family                       | Bad inference refused                                            | Where it lives                                                                                       |
| ---------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Surface boundary**         | revoked / spendable / valid on A ⇒ same on B                     | `SurfaceAuthorization.lean` (collapsed-surface refusal); standing-upgrade-block specimen             |
| **Declaration completeness** | partial coverage ⇒ total coverage; survival ⇒ closure            | `ClosureEligibility.lean`; `RecoveryMargin.lean`                                                     |
| **Witness identity / provenance** | sample exists ⇒ trustworthy / provenanced witness           | `WitnessInvariance.lean` (encapsulation / regime axis); provenance is a candidate gap                |
| **Custodian binding**        | observed / instrumented ⇒ accountable                            | candidate, [`custodian-binding-accountability-candidate.md`](custodian-binding-accountability-candidate.md) |
| **Freshness / expiry**       | was true ⇒ still admissible                                      | `Freshness.lean` (metric-time axis)                                                                  |
| **Fluency / settlement**     | output reads coherent ⇒ settled                                  | `ConsolidationDenial.lean`                                                                           |
| **Cross-boundary mint**      | failure / exposure / degradation on A ⇒ same on B                | `CrossBoundary{Exposure,Degradation,FailureMint,Cascade}.lean`                                       |
| **Authorization vs safety**  | authorized ⇒ value-preserving                                    | safety-bridge family (`SafetyBridge.lean`, `SafetyTrajectory.lean`, `AttestationLedger.lean`)        |
| **Composition / unification**| local refusal composes ⇒ unified judgment form                   | doctrine: [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md); not a Lean theorem |

## How to use this map

Before filing a new candidate working note that names a refusal:

1. **Classify it against the family table.** If the bad inference matches an existing row, the candidate is either (a) a new specimen of an existing family (annex / specimen work), or (b) a sharper restatement of an existing refusal (rewrite the existing module's docstring, not a new file).
2. **If the inference doesn't match any row**, the candidate is opening a new family. That is a heavier move — name it, but do not build Lean until a downstream consumer requires the distinction mechanically (per the doctrine file's bridge-tax discipline).
3. **If the inference matches a row but the existing modules don't cover the specific operational failure mode the candidate names**, the candidate is a *forcing case* on an existing family. File it; the existing module may need to be extended, or a sibling kernel may need to be added.

## Meta-pattern: control-flow laundering

Some anti-laundering refusals can be reintroduced by the checker's *control flow* rather than by its *domain model*. This is an implementation-level preservation rule that applies to ALL refusal families above; it is not a separate row.

**The pattern.** Monadic short-circuiting (`Except.bind`, `do`-notation, first-failure-wins validators, early-return gate chains) collapses a multi-failure attempt into a single refusal. The domain model can be perfectly typed and the kernels can each return typed failures, and the *checker's evaluation strategy* still launders `[failure₁, failure₂, failure₃]` into `[failure₁]`. A complete diagnosis is converted into the first encountered failure, and independent refusal grounds are silently erased.

**The rule.** Boundary checkers that claim to preserve refusal structure must use validation/applicative-shaped accumulation: run all relevant kernels, preserve each typed failure, avoid netting failures into a scalar verdict. The idiomatic clean code (early return, monadic bind) is wrong here. The awkward accumulating form is correct, and the awkwardness is load-bearing.

**Where this came from.** Discovered structurally in `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` (a fenced scratch encoding of the boundary-checker pattern). The Lean type system rejected the obvious idiomatic shape — `Except`-based aggregation forced a confession that monadic structure would have eaten the multi-failure diagnosis. The 8-way exhaustive match in that file is intentionally ugly because the ugliness is what prevents the laundering. Any future kernel-abstraction layer must be validation/applicative-shaped, never plain `Monad`.

**Operational translations (non-Lean code).** The Lean scratch is *category 2* (fenced proof-of-encodability), but the four implementation idioms it rejected translate directly into design rules for NQ / AG / Rust / Python code without needing to ship any Lean:

1. **No caller-supplied admissibility.** Witnesses are output, never input. APIs that accept a "verified" or "trusted" flag from the caller are reintroducing self-mint.
2. **No early-return validators where all failures matter.** Short-circuiting aggregators (`Result::?`, `Either.bind`, `try` chains, gate-cascade returns) launder multi-failure cases into single-failure refusals. Where complete diagnosis is the point, use accumulating / validation-shaped aggregation.
3. **No boolean "valid" APIs for authority transitions.** Boolean returns convert "passed" into an uninspectable scalar. Authority-bearing checks should return typed verdicts carrying either the admissibility evidence or the typed refusal, not `bool`.
4. **No reusable witness unless explicitly versioned / scoped.** A witness should be tied to the specific attempt, time, and (if relevant) policy version it was minted under. "Trusted token" / "session" abstractions that elide the binding are replay laundering with better PR.

These translations are the bridge from "proof-shaped toy discovered something in Lean" to "non-Lean code that doesn't lie." Citable outside the formal context.

**Why this isn't a sixth row.** It is not a domain refusal (it doesn't refuse a class of bad inferences across surfaces). It is a preservation rule for the implementation of any domain refusal. Filing it as a row would dilute the family taxonomy; filing it here keeps the row structure clean and surfaces the meta-rule where checkers will actually consult it.

## Lean filing discipline (two admissible categories)

The earlier rule "no Lean without a downstream consumer" was too narrow. Two categories of Lean filings are admissible in the corpus, and conflating them is the failure mode to watch for:

1. **Public / promoted kernels** — wired into `LeanProofs.lean`, part of the 1.0 compatibility surface (or earned annex). Requires a downstream consumer that mechanically needs the distinction. Bridge-tax discipline per [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md) applies.
2. **Fenced scratch proof-of-encodability** — scratch annex labeled as such, NOT wired, NO promotion path, NOT used as discharge. Allowed when it demonstrates that a doctrine *can* be structurally encoded. Pays its rent by forcing the architecture to confess which implementation idioms are inadmissible (see meta-pattern above). The productive use of formal methods is not "prove the system correct" but "use the proof-shaped toy to discover which implementation idioms are inadmissible." Lean's role in category 2 is the compiler as adversarial reviewer, not as ratification authority.

The failure mode the original rule was guarding against — Lean masquerading as discharge — fires only when category-2 work is presented or used as category 1. Fenced scratch that stays fenced is genuinely productive. `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` is a category-2 filing: it structurally encodes three of the family rows above (custodian binding's self-attestation half, freshness, declaration completeness's zero-evidence degenerate case), explicitly names the standing-kernel gap, and surfaced the control-flow laundering meta-pattern as a side effect of refusing to be elegant.

## What this map is NOT

- Not a formal taxonomy. Rows are operational categories, not type-theoretic partitions.
- Not exhaustive. New families can be added; old families can be retired if their refusal turns out to be a special case of another row.
- Not a paper. This is internal navigation for the working-notes layer; if a paper ever needs to cite the family structure, it cites the individual kernel modules, not this map.
- Not a license to build. Files referenced here are the substrate; building a new kernel in any row still requires the per-row forcing-case discipline.

## Composes with

- The doctrine file [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md) names the meta-rule: cross-family implications require an explicit bridge theorem stating which row's refusal condition is being preserved. This map names the rows; the doctrine file governs how they cross.
- The Lean repo's `LeanProofs/Admissibility/README.md` "Refusal kernel taxonomy" section is the formal-layer sibling of this map.

## Provenance

Filed 2026-06-04 after a candidate (`custodian-binding-accountability-candidate.md`) needed a parent to prevent it from looking orphaned. The retroactive realization that the corpus has been building a small family of refusal-kernel patterns prompted the map; the patterns predate this filing.
