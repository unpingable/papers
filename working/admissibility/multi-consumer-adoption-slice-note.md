# MultiConsumerAdoption — slice note

**Filed:** 2026-06-08. Companion to `~/git/lean/LeanProofs/Scratch/MultiConsumerAdoption.lean`. Custody-Class: SCRATCH. Not imported. No paper anchor. No promotion path. No discharge use.

## Witnessed (via `leanctx`)

- HEAD at slice start: `1dca12b3` (clean) — pre-work decl probes returned `at_sha`.
- `decl Adopts` / `decl Consumer` / `decl GloballyAdopted` → `gap_blocks` (no prior corpus claims on these names at HEAD). Clean slate for the abstract vocabulary.
- `decl ConsumerAdoption` → witnessed at `Labelwatch.lean:128` (Spec003's moderation-domain structure). NOT imported by this slice.
- Clean at_sha rebuilds: `LeanProofs.Scratch.TemporalCustody` and `LeanProofs.Scratch.RetroactiveFigLeaf` both `status: pass`, `custody_scope: at_sha`.
- New module compiles cleanly: `lake build LeanProofs.Scratch.MultiConsumerAdoption` → `status: pass`, 363ms.
- Build receipt for the new module: `custody_scope: working_tree_only` (file untracked at build time), `discharges: ['build_passes_in_worktree']`. **NOT** a discharge of `build_passes_at_sha`. Honest.

## Asserted / advisory (NOT witnessed)

- Vocabulary correspondence: that `Consumer`, `Evidence`, `AdoptionRegistry`, `Adopts`, `GloballyAdopted` map onto the intended multi-consumer phenomenon. The Lean code encodes a small extensional-adoption algebra; the interpretation as "no cross-consumer inference, no local-to-global lift" is the author's claim, not the harness's.
- Adjacency to Labelwatch's `ConsumerAdoption` (Spec003 work). The two are NOT the same type. Labelwatch's structure is moderation-specific (carries `artifactId`, `adoptedAt`, etc.). This slice's `Consumer × Evidence` pair is deliberately abstract. The adjacency is in shape, not in signature.
- Small-negative-theorem shape: structural choice, not witnessed identity.

## What landed

```text
3 structures:           Consumer, Evidence, AdoptionRegistry
2 predicates:           Adopts, GloballyAdopted
3 specimens:            consumerA, consumerB, evidenceX, asymmetric_registry
4 theorems:
  positive (vacuity guards):
    consumerA_adopts_evidenceX
    consumerB_does_not_adopt_evidenceX     (paired negative instance)
  negative (THE theorem):
    cross_consumer_adoption_does_not_imply
  negative (corollary):
    local_adoption_does_not_imply_global
```

Load-bearing claim (specimen-bound — the `r` is fixed to `asymmetric_registry`, not universally quantified):

```
∃ A B : Consumer, ∃ e : Evidence,
  Adopts asymmetric_registry A e ∧ ¬ Adopts asymmetric_registry B e
```

This is a *specimen exists* claim, not a *for-all-registries* claim. The theorem exhibits one registry in which local adoption fails to imply cross-consumer adoption. A general "no registry can support cross-consumer inference without a bridge" statement would require quantifying over registries and is NOT what is proved here.

Similarly the corollary `local_adoption_does_not_imply_global` is about the specific `asymmetric_registry`:

```
Adopts asymmetric_registry consumerA evidenceX ∧
  ¬ GloballyAdopted asymmetric_registry evidenceX
```

Two negated-universal wrappers (`not_all_cross_consumer_lifted`, `not_all_local_adoption_globalizes`) refute the corresponding blanket rules directly. Closing docstring names the two bridge shapes (`PropagatesAdoption` for trust-graph closure, `AllowsGlobalLift` for platform-default rules) that would be required to license cross-consumer or local-to-global inference, and **refuses to build them**.

Unless explicitly stated as a universal theorem, the Lean result is a specimen/counterexample; broader doctrinal interpretation remains advisory.

## Non-goals honored

- No import of `Labelwatch`, `TemporalCustody`, `RetroactiveFigLeaf`, or any other module.
- No modifications to any existing module.
- No bridge predicates built — only described in docstring.
- No generalized subscription-graph or trust-lattice calculus.
- No claim that this "formalizes" Labelwatch's `ConsumerAdoption` or any prose doctrine.

## The refusal tripod

This is the third sibling-shaped negative kernel:

```text
TemporalCustody:        freshness does not transfer across time (citation → execution)
RetroactiveFigLeaf:     post-validation does not authorize backward (cite → decision)
MultiConsumerAdoption:  adoption does not globalize across consumers (A → B)
```

Each is a tiny `¬ implication` with an explicit-bridge docstring and no imports of its siblings. The three together suggest a recurring shape: every silent path from one party/time/scope to another requires an explicit bridge predicate; the kernel's job is to refuse the silent path. *Recorded here as advisory* — the harness witnesses each module's build independently; the "tripod" framing is the author's claim.

## Curdling guard

Fenced scratch. Custody-Class: SCRATCH per Lean file header. Not imported. No paper anchor. No promotion. Specimen sibling to the two prior scratch kernels, not an extension.

---

**One small negative theorem + one corollary. Build witnessed via leanctx (worktree-scope, honestly demoted). Vocabulary correspondence advisory. Standing down.**
