# Projection laundering across the representation boundary

**Status:** Candidate refusal-kernel residue. Not promoted doctrine. Filed 2026-05-26 after multi-model relay (DeepSeek + ChatGPT + operator). Sibling to [[uncertainty-custody]] — PL is *upstream* of UC's gate. Scratch Lean annex built 2026-05-30 under the [annex-probe queue](annex-probe-queue-2026-05-29.md)'s five-criterion test; see §"Lean annex — built status" below. Not imported into `LeanProofs.lean`; no public-surface promotion; no doctrine mint.

**Posture:** A refusal-kernel form of an existing vocabulary entry ([[compression-becomes-authority-vocabulary]]). The shape is already covered at *essay-vocabulary* level by "compression-authority laundering"; the residue worth filing is (a) the paired negative+positive theorem structure that gives the vocabulary a kernel-level form, and (b) the explicit composition with [[uncertainty-custody]] as a two-stage representation-pipeline custody.

**The audit was the gate.** Multi-model relay sprawled across substrate-specific compression families before clamping to the substrate-agnostic refusal kernel. The earned residue is below.

---

## Core sentence

> **Projection laundering is the representation-stage failure mode where compression erases the predicate a downstream custody gate requires in order to refuse consequential action.**

This is the audit-survivor sentence. Everything else hangs off it. If the note is trimmed to one paragraph in a future audit, keep this one.

## The keeper

> **A projection may simplify evidence. It may not erase the conditions under which evidence was allowed to bind.**

## The kernel — paired negative + positive

The viable formal object is two paired theorems:

- **Negative (failure mode):** if the projection erases a custody-relevant predicate AND the downstream policy treats the projected artifact as sufficient authority, then there exists a state where the original belief demanded deferral but the system acts consequentially.

- **Positive (remedy):** if the projection preserves the custody-relevant predicate AND the downstream policy respects the preserved signal, then no must-defer state can produce a consequential action through the artifact-only policy.

The structure:

```
Belief --projection--> Artifact --policy--> Action
          │                         │
          └── must preserve         └── must respect
              refusal predicates       refusal signals
```

## Composition with uncertainty-custody

PL is *upstream of* UC. The pipeline:

| Stage | Discipline | Reference |
|---|---|---|
| Projection (Belief → Artifact) | Loss-aware: preserve refusal predicates | This note |
| Gate (Artifact → Action) | Uncertainty custody: respect refusal signals | [[uncertainty-custody]] |

Either stage failing produces laundering; both passing blocks it. PL says *the gate cannot enforce a predicate it cannot see*. UC says *the gate, given the predicate, must refuse appropriately*. Together they form representation-pipeline custody.

This is a genuine new composition not present in either parent note.

> **Composition-vs-calculus guard.** The PL/UC composition is a *pipeline* composition — predicates connected by data-flow across a representation boundary — not yet a refusal-*calculus* composition theorem of the form `A ⇏ B; B required for C; therefore A ⇏ C`. Pipeline composition does not earn the word "calculus" and does not retire the brake in [[refusal-kernel-to-refusal-receipt-seam]]'s versioning ladder.

## Overlap audit

| Existing primitive / kernel | Coverage of PL | Conclusion |
|---|---|---|
| [[compression-becomes-authority-vocabulary]] | Same failure family at *vocabulary* level. CBA names "compression-authority laundering" as essay/public-facing vocabulary and routes to FiatAdmissibility. | **PL is the refusal-kernel form of CBA.** Same relationship as ConsolidationDenial-Lean to consolidation-denial-tool-note. |
| `FiatAdmissibility` (Lean annex) | CBA-vocabulary explicitly routes here: artifact-kind × use-kind. PL refines: a `lossy-projection` artifact for `binding-authorization` use → `denied` or `requiresMediation` unless `loss-signal` is preserved. | Closest formal slot. PL could land as a more-specific cell in FA, or as a sibling refusal kernel. |
| `SurfaceAuthorization` | Adjacent: collapsed surface ⇏ cause attribution. Surface-loss is structurally similar to projection-loss but axis differs (causes vs. predicates). | Sibling, not subsumption. |
| `WitnessInvariance` | Cousin: WI tests witness-output invariance under wrong perturbation. PL is about projection-erasure of predicate. Both are "information-loss" failures; quantifier-shape differs. | Mirror/cousin. |
| Refusal-kernel family (Fluent⇏Settled, etc.) | Operator family covers shape fully. PL is a new candidate row at *projection-boundary* layer. | Same family, new specimen. |
| [[uncertainty-custody]] | Downstream composition partner, not overlap. UC's `ArtifactSignalsDefer` is exactly what PL's projection must preserve. | Composition, not overlap. |
| P25 (Epistemic Border Control, published) | Substitution under observability asymmetry: V′ regulated, V ground truth. PL applies the same shape to representation-projection. | Closely adjacent; PL would be downstream specimen of P25's substitution machinery. |
| [[project-laundering-move-watchlist]] | Generator: artifact crosses into stronger role without earning transition. PL is exactly an instance. | Watchlist genus. |
| [[prose-state-inversion]] | Same authority-laundering pattern, different substrate. PSI = prose ⇏ structured-state authority. PL = compressed-artifact ⇏ rich-belief authority. | Sibling under shared genus. |

**Audit conclusion:** the shape is **fully covered** at vocabulary level by CBA and at routing level by FiatAdmissibility. The residue worth filing rather than discarding:

1. **The paired theorem structure** (negative + positive) — gives concrete refusal-kernel form to CBA's prose framing. CBA owns the public name; PL owns the predicate-level theorem pair.
2. **The PL/UC composition** — two-stage representation-pipeline custody is new vocabulary not present in either parent.
3. **The recognition handles** — `ProjectionLaundering` (failure), `loss-aware projection` (remedy), `ErasesDefer` / `PreservesDefer` (predicate pair).

## Lean annex — built status (2026-05-30)

`LeanProofs/Admissibility/ProjectionLaundering.lean` exists as a scratch annex. Built under the [annex-probe queue](annex-probe-queue-2026-05-29.md) five-criterion test, not under downstream-consumer force. Green; not in `LeanProofs.lean`; no public-surface promotion; no paper citation.

Discipline preserved:

- The compile is *contact*, not publication. Green says the paired neg+pos shape is coherent enough that future arguments don't have to be re-derived from chat vapor. It does **not** say PL is doctrine.
- CBA still owns the public name. PL owns the kernel slot.
- The PL/UC composition stays prose-only until a downstream consumer (NQ / Wicket / Governor) demands a citation.
- The two-gate ladder still applies: `module ≠ public surface ≠ paper claim ≠ platform verdict`. Each `≠` is its own gate.
- The audit was the gate. The compile is a second receipt; the doctrine receipt is still upstream.

Build invocation:

```bash
cd ~/git/lean && lake build LeanProofs.Admissibility.ProjectionLaundering
```

The sketches below remain the recoverable artifact. The annex names them `projection_launders_deferral` and `loss_aware_projection_blocks_deferral_laundering` exactly; predicate names (`ErasesDefer`, `PreservesDefer`, `ArtifactOnlyIncautious`, `PolicyRespectsDeferSignal`) match. Annex-file structure differs from the sketches only in (a) namespacing under `Admissibility.ProjectionLaundering`, (b) explicit-argument style (no top-level `variable` block) for parity with the `ConsequencePartition` annex, and (c) the policy-incautious hypothesis is named (`ArtifactOnlyIncautious`) rather than left inline.

## Lean reserve — recognition handles, not implementation obligations

Original framing, preserved unchanged. The sketches below were written as recognition handles; the 2026-05-30 annex compile honored them as such (drop-in, no proof complexity) rather than as authorization to promote.

> **These sketches are recognition handles, not implementation obligations. Absence of Lean here is the intended state unless a downstream consumer forces the proof. "Sketched-not-built" is not a synonym for "obviously next."**

### The Lean did its job before existing

The pass that produced these sketches was not wasted. The discipline is that the Lean shape *forced the prose to separate*:

- *projection erases custody predicate* from *projection merely simplifies evidence*
- *artifact-only incautious policy* from *defer-respecting policy*
- *failure-mode theorem* from *paired-remedy theorem*
- *substrate-agnostic refusal kernel* from *substrate-specific compression families*

That's the marrow. The proof is preserved below as a refusal shape, not promoted as a public surface. The discipline:

> **Prose owns discovery. Lean owns refusal.**

> **The proof is preserved as a refusal shape, not promoted as a public surface.**

### Reserved theorem shapes — scannable handles

| Name | English | Where |
|---|---|---|
| `projection_launders_deferral` | Erasing-projection + incautious-policy → ∃ state where belief must-defer and policy acts consequentially. | Sketch 1. |
| `loss_aware_projection_blocks_deferral_laundering` | Defer-preserving-projection + defer-respecting-policy → ∀ must-defer states, the policy is non-consequential. | Sketch 2. |
| `ErasesDefer` / `PreservesDefer` | Dual predicates over `Belief → Artifact` projections. The conjugate pair is the recoverable object. | Both sketches. |

These names are the recoverable artifact even if the code blocks below rot. If a future session needs to cite the refusal shape without re-deriving it, the table is the index.

### Sketch 1 — Negative theorem (projection_launders_deferral)

```lean
variable (Belief Artifact Action : Type)
variable (MustDefer : Belief → Prop)
variable (Consequential : Action → Prop)
variable (ArtifactSignalsDefer : Artifact → Prop)

def ErasesDefer (project : Belief → Artifact) : Prop :=
  ∃ b : Belief, MustDefer b ∧ ¬ ArtifactSignalsDefer (project b)

def ArtifactOnlyPolicy
    (project : Belief → Artifact)
    (policy : Artifact → Action) : Belief → Action :=
  fun b => policy (project b)

theorem projection_launders_deferral
    (project : Belief → Artifact)
    (policy : Artifact → Action)
    (h_policy_incautious :
      ∀ a : Artifact,
        ¬ ArtifactSignalsDefer a → Consequential (policy a)) :
    ErasesDefer project →
    ∃ b : Belief,
      MustDefer b ∧
      Consequential ((ArtifactOnlyPolicy project policy) b) := by
  rintro ⟨b, h_def, h_no_signal⟩
  exact ⟨b, h_def, h_policy_incautious (project b) h_no_signal⟩
```

### Sketch 2 — Positive theorem (loss_aware_projection_blocks_deferral_laundering)

```lean
def PreservesDefer (project : Belief → Artifact) : Prop :=
  ∀ b : Belief, MustDefer b → ArtifactSignalsDefer (project b)

def PolicyRespectsDeferSignal (policy : Artifact → Action) : Prop :=
  ∀ a : Artifact, ArtifactSignalsDefer a → ¬ Consequential (policy a)

theorem loss_aware_projection_blocks_deferral_laundering
    (project : Belief → Artifact)
    (policy : Artifact → Action)
    (h_preserve : PreservesDefer project)
    (h_policy_respects : PolicyRespectsDeferSignal policy) :
    ∀ b : Belief,
      MustDefer b →
      ¬ Consequential ((ArtifactOnlyPolicy project policy) b) := by
  intro b h_def
  exact h_policy_respects (project b) (h_preserve b h_def)
```

**Build triggers (original):** only if (a) NQ / Wicket / Governor needs a concrete projection-laundering refusal in code, (b) CBA essay drafting forces a citation to the Lean form, (c) a downstream paper requires the formal pair.

**What actually fired (2026-05-30):** the annex-probe queue's five-criterion test — audit done, shape bounded, sketches near-Lean, the bounded question ("is the paired neg+pos a kernel, or prose wearing a lab coat?") was real, and public-surface promotion stays gated. Green confirms the structure. The original build triggers above still govern promotion to public surface; this compile did not.

## Anti-goals

- **Do NOT** sprawl into substrate-specific compression families. The kernel is substrate-agnostic; specific substrates are downstream consumers, not kernel content.
- **Do NOT** mint a new framework called "Compression Custody" or "Representation Custody" — [[compression-becomes-authority-vocabulary]] already owns this name space at the public-essay level.
- **Do NOT** build the Lean module pre-emptively. Both proofs are one-line; the readiness signal is fake-easy. Same discipline as [[uncertainty-custody]].
- **Do NOT** treat this as a new empire or new family. It is one row in the operator family, with a vocabulary parent and a downstream composition partner already on disk.

## Keepers (compact stack)

> **A projection may simplify evidence. It may not erase the conditions under which evidence was allowed to bind.**

> **The gate cannot enforce a predicate it cannot see.**

> **Projection laundering: a representation boundary erases a custody-relevant predicate while downstream policy treats the projected artifact as sufficient authority.**

> **Loss-aware projection: the loss record preserves the predicates downstream authority will need.**

> **PL upstream of UC: the projection must preserve what the gate must respect.**

> **A representation pipeline has custody obligations before the explicit custody gate ever runs.**

> **Compression-authority laundering owns the public name. Projection-laundering owns the kernel slot.**

## Cross-references

- [[uncertainty-custody]] — downstream composition partner. PL's `ArtifactSignalsDefer` is exactly what UC's gate respects.
- [[compression-becomes-authority-vocabulary]] — essay-vocabulary parent. PL is the refusal-kernel form of CBA's "compression-authority laundering."
- [[refusal-kernel-to-refusal-receipt-seam]] — operator-family parent. PL is a new candidate row at the *projection-boundary* layer.
- [[laundering-move-watchlist]] — sibling attack-surface inventory. PL is an instance of the watchlist generator.
- [[prose-state-inversion]] — sibling under shared authority-laundering genus, different substrate.
- [[witness-invariance-failure]] — cousin (information-loss under perturbation vs. under projection).
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — closest formal slot if Lean is forced.
- `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` — adjacent surface-loss kernel.
- `preprint/25-epistemic-border-control/` — P25 ancestor: substitution under observability asymmetry. PL is one specimen of the family P25 governs.

## Provenance

- **2026-05-26**, multi-model relay. Viable kernel: *"a downstream custody gate cannot protect uncertainty if the upstream representation has already erased uncertainty."* ChatGPT proposed `projection laundering` / `loss-aware projection` as the failure/remedy name pair.
- **Containment trace:** initial relay expansion was substrate-specific and broad; ChatGPT clamped to the narrow substrate-agnostic kernel. DeepSeek produced the earned-version Lean. ChatGPT cleaned up type-variable hygiene (explicit `Action`, explicit `project` arg) and added the **paired positive theorem** for loss-aware projection — the half DeepSeek hadn't sketched. Parameter named `project` rather than `compress` because compression is one projection mode, not the only one.
- **Filed:** claude-code, 2026-05-26, after audit confirmed (a) shape was covered by CBA vocabulary at essay level + FiatAdmissibility at routing level, (b) the paired theorem structure + the PL/UC composition were the genuine new residue, (c) operator's instruction was *working note first; Lean if it refuses to stay prose; do not let it breed*.

## Park state

Updated 2026-05-30 to reflect the scratch-annex compile.

Next session's input — if the topic recurs — should:

1. Check whether NQ / Wicket / Governor / CBA essay has demanded a citation. (Still gates public-surface promotion.)
2. Check whether the PL/UC composition has been used in a fixture, paper, or downstream design pass.
3. Only then consider importing the scratch annex into `LeanProofs.lean` or citing it from a preprint. **The annex existing is not the citation trigger.**

Until then: scratch only. The audit was the first receipt; the green compile is the second receipt; the doctrine receipt is still upstream.

> **The audit was the gate. The compile is the receipt. The forcing case is still upstream.**

(That keeper is shared with the annex-probe queue's park state; PL inherits it.)
