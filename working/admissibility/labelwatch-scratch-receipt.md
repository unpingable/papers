# Labelwatch — scratch receipt

**Filed:** 2026-06-08. **Status:** scratch receipt for the fenced Lean spike. **NOT doctrine. NOT a paper. NOT a primitive. NOT promoted.** Companion to `~/git/lean/LeanProofs/Scratch/Labelwatch.lean` — fenced scratch, Custody-Class: SCRATCH, not imported by `LeanProofs.lean`, no 1.0 surface, no paper anchor, no promotion path. Receipt only.

## The arc

Specimens drove the formal motion across this slice:

| Step | What it forced |
|---|---|
| **001 / 002** | A witnessed label alone does not imply a render observation or an applied constraint. The non-laundering property is about *permitted derivations from evidence bundles*, not about factual non-occurrence. EvidenceInput / DerivedJudgment separation; AdmissibleFromInput depends only on observable evidence. |
| **D-001** | Execution surface as an axis. moderation.bsky.app + !takedown was auto-classified as render-execution-gap because the schema lacked execution surface. !takedown converts at hosting/PDS layer. Added `ExecutionSurface`; threaded surface through `PolicyDocumentation`, `ExecutionObservation`, `ConstraintClaim`, and `ConversionGap`; added surface-coherence check on the full-bundle constructor. |
| **D / D.5 / E / F** (Labelwatch side; NOT in this Lean slice) | Exporter, undeclared emission, freshness, provenance gates. These surfaced in detection-lane work without forcing changes to the current Lean fragment. Recorded for arc completeness; no Lean formalization. |
| **003 / Driftwatch** | Opt-in consumer adoption distinct from emitter declaration distinct from global platform default. Same skywatch.blue + fringe-media label witnesses two different effective scopes (Case A: emitter_declared; Case B: opt_in:driftwatch). Required new vocabulary: `ConsumerScope`, `ConsumerAdoption`, `ConsumerActionObservation`. Forced the two non-inference theorems below. |

## What landed in Lean

```text
~/git/lean/LeanProofs/Scratch/Labelwatch.lean
  Build: lake build LeanProofs.Scratch.Labelwatch — green, 1.5s
  Lines: 686
  Sorries: 0
  Warnings: 0
  Imported: no (fenced)
  Custody: SCRATCH per header
```

**Types (observation/documentation level):**

```text
ExecutionSurface          : render | hosting | mixed | unknown
LabelObservation          (with timestamp)
PolicyDocumentation       (with executionSurface, publishedAt)
PolicyWitness             (typed; not consumed by any current constructor)
ExecutionObservation      (with surface, executionContext, timestamp)
AuditOutcome              : no_consumer_found_converting | consumer_found_converting | inconclusive
AuditEvent                (with scope, outcome, timestamp)
ConsumerScope             : global_platform | emitter_declared | opt_in consumer_id
ConsumerAdoption          (consumerId, artifactId, adoptedAt)
ConsumerActionObservation (consumerId, subject, constraint, surface, executionContext, timestamp)
ConstraintClaim           : label_observed | documented_conversion_path | constraint_applied
                          | no_default_constraint_followed | consumer_scope
```

**EvidenceInput** is observation-only (no verdict-shaped fields). **DerivedJudgment** contains `gap : Option ConversionGap` and `effectiveScope : Option ConsumerScope`, both computed by pure functions from EvidenceInput.

**Admissibility constructors (six, positive only):**

- `from_label`
- `from_label_and_policy_doc` (claim carries policy's executionSurface)
- `from_full_coherent_bundle` (with surface-coherence check)
- `from_audited_no_default`
- `from_emitter_only_scope` — REQUIRES a witnessed LabelObservation, not just absence of adoption
- `from_consumer_adoption_and_action`

**No constructor produces `.global_platform`.** That refusal is structural — admitting it would require platform-witness evidence not modeled here.

## The load-bearing theorems

```lean
-- Derivation-shape non-laundering (carried forward from 001/002):
label_alone_cannot_derive_constraint_applied
label_and_policy_doc_cannot_derive_constraint_applied
spec_demo_full_admits_constraint_applied      -- positive paired counterpart

-- Structural separation (carried forward):
derived_judgments_require_independent_witness  -- specimen-track local — see Caveat 1
admissibility_pure_of_evidence_input
deriveJudgment_pure_of_evidence_input

-- Spec003 / Driftwatch non-inference theorems (this slice's load-bearing additions):
no_cross_consumer_inference
  -- Adoption by consumer C does not imply adoption by consumer D.
  -- Proof: cases on the only opt_in-producing constructor; the
  -- index unification forces ca.consumerId = d, which contradicts
  -- the hypothesis that no ca in the bundle has consumerId = d.

no_global_promotion
  -- Opt-in consumer adoption does not promote to global_platform.
  -- Proof: structural — there is no constructor producing
  -- .global_platform; cases auto-discharges all branches.
  -- (Name caveat — see Caveat 4(a) below.)
```

**Same testimony yields different effective scopes:**

```lean
spec003a_derived_scope : effectiveScope = some .emitter_declared
spec003b_derived_scope : effectiveScope = some (.opt_in "driftwatch")
spec003a_and_spec003b_scopes_differ
```

The Driftwatch counterexample to the accidental rule *"third-party → no conversion"* is now formally captured.

## Caveats (all five, recorded in the Lean file's separation-invariant section)

1. **Theorem name overclaim.** `derived_judgments_require_independent_witness` proves what's more accurately stated as `admissible_claims_require_label_anchor`. The proof shows every current constructor needs a LabelObservation — specimen-track local. The broader principle is enforced structurally by the type signature of `AdmissibleFromInput`. Kept under the broader name as a fenced marker.
2. **`AuditEvent.scope` is the laundering pressure point** for absence claims. `no_consumer_found_converting` is safe only if scope is precise (consumer/context/surface/time-named). The type system does not enforce scope precision; that is a Labelwatch-side discipline question for the producer of AuditEvent records.
3. **`ExecutionSurface` appears as input evidence ONLY as a field of `PolicyDocumentation` or `ExecutionObservation`.** Not as a free-standing surface verdict in EvidenceInput. The classifier reads surface from PolicyDocumentation; the derived `execution_gap_policy_present surface` inherits surface from that read.
4. **`ConsumerScope` and the no_global_promotion name** (updated post-review):
   - (a) `no_global_promotion` is named more broadly than what it proves. The proof is fenced to *this consumer-adoption fragment*: no constructor here produces `.global_platform`. It is NOT a general claim that no evidence anywhere can ground `.global_platform`. A future patch admitting a platform-witness constructor would legitimately derive it. More honest names: `opt_in_adoption_does_not_promote_to_global` or `no_global_scope_from_consumer_adoption_fragment`. Rename when a platform-witness constructor is added.
   - (b) Non-globality is preserved STRUCTURALLY through `ConsumerScope.opt_in cid` (the consumerId tag is the non-global-provenance marker). The Lean side preserves the SCOPE caveat structurally; it does NOT model arbitrary caveat-list inheritance (e.g., named caveats `non_global_provenance`, `consumer_local_scope_only` carried as a free-form set). That is the correct boundary for this slice.
5. **`classifyEffectiveScope` first-adoption-wins** is a quiet policy (deterministic but not loud about its choice). Operator's stated preference: in a future multi-consumer slice, >1 ConsumerAdoption should return `none` (unsupported/ambiguous), not silently take the first. Current single-consumer reading is a known partial; the fail-over-first preference is the next likely D-style bite if multi-consumer specimens appear before the classifier is patched.

## Verifications (post-review)

- ✓ `from_emitter_only_scope` requires `(l : LabelObservation)` AND `(hLabel : e.labelObs = some l)`. Absence of consumer adoption alone is NOT sufficient. Absence of testimony does not turn into scoped testimony.
- ✓ Build green; sorries: 0; warnings: 0; fenced.
- ✓ All caveats inline in Lean file.

## What this slice does NOT claim

- Not a theory of moderation. Not a calculus over Labelwatch corpora. Not a paper claim.
- Not a complete encoding of D/D.5/E/F findings (exporter, undeclared emission, freshness, provenance gates). Those surfaced detection-lane-side without forcing changes here; future Lean slices can pick them up if they push back.
- Not a multi-consumer adoption model. One named consumer, one label, one receipt — per Spec003 guard.
- Not a model of arbitrary caveat-list inheritance. Scope-caveat only; that's the boundary.
- Not a generalization beyond the four ConstraintClaim shapes and six AdmissibleFromInput constructors currently encoded.

## Closure

```text
Lean state:           frozen at Spec003-revision
                      EvidenceInput / DerivedJudgment separation preserved
                      ExecutionSurface schema patch preserved
                      ConsumerScope / ConsumerAdoption / ConsumerActionObservation added
                      Five caveats inline; two updated post-review

Specimen track:       001/002 → D-001 → 003
                      Driftwatch counterexample formalized
                      D/D.5/E/F detection-lane findings unencoded
                      (recorded as arc context, not Lean obligations)

Next likely D-style bites (named, NOT building):
                      - Multi-consumer adoption (classifyEffectiveScope
                        fail-over-first preference)
                      - Platform-witness constructor (would force
                        no_global_promotion rename)
                      - Caveat-list-as-data (arbitrary inheritance model)
                      - D/D.5/E/F formalization if Labelwatch
                        detection pushes back

No promotion. No paper-shape motion. No further Lean changes
authorized; the next move is on the Labelwatch detection-lane side
when a specimen actually forces one of the named bites.
```

## Cross-references

- Lean file: `~/git/lean/LeanProofs/Scratch/Labelwatch.lean`
- Sibling scratch receipts: `bridge-interface-spike.md`, `provenance-profiles-scratch-receipt.md`
- Doctrine adjacency: `~/git/papers/working/no-unifier-without-laundering.md` (federation discipline)
- `[[project-lean-custody-state]]` — custody-class discipline honored
- `[[project-label-backflow]]` — adjacent prior framing (the "label readable by target can be used by target" shape) — different axis; not the same calculus

## Curdling guard

Fenced scratch only. No Lean module promoted. No primitive minted. No paper-shape motion. The Lean file declares Custody-Class: SCRATCH in its header. Five caveats inline.

---

**One coherent specimen track. One fenced Lean fragment. Five inline caveats. Three structural refusals (label alone, opt-in to global, cross-consumer inference). Standing down.**
