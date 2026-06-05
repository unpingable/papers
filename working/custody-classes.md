# Lean Custody Classes

**Filed:** 2026-06-05. **Status:** vocabulary ratification. Pins the five custody classes a `.lean` file may declare, and the two-layer marker convention. ANNEX added 2026-06-05 with forcing case from the Phase 2 audit. Sibling to [`wiring-is-not-folder-placement.md`](wiring-is-not-folder-placement.md) ([[project-wiring-vs-folder-placement]]) and [`promotion-claims-require-custody-witnesses.md`](promotion-claims-require-custody-witnesses.md).

## The headline

> **`Custody-Class:` is the grep target. `Custody:` prose remains the explanatory receipt.**

The marker tells you *which class* a file is held in; the prose tells you *why*. Either alone is insufficient: a class label without prose is a stamp nobody can audit; a prose paragraph without a class is rich, ungreppable, and silently asymmetric across files.

## The five classes

| Class | Meaning |
|---|---|
| `PUBLIC-SHIPPED` | Relied-upon public kernel surface. Imported by the public aggregator (`LeanProofs.lean` or its public equivalent) **and** named in the kernel-surface aggregator (`AdmissibilityKernels.lean`). The corpus stands behind the signature; breaking it requires explicit ratification. |
| `ANNEX` | Compiled supporting material intentionally included in the repository's admissibility corpus but not part of the public shipped kernel surface. Annex files may support examples, named extensions, consumer specimens, or doctrine-adjacent coverage. They are scope-declared and regression-covered, but not promoted as public kernel authority. |
| `SCRATCH` | Fenced exploratory material, not relied upon. Compiles, may be used by other scratch, but is not imported by the public aggregator. No promotion claim. |
| `UNRATIFIED-CANDIDATE` | Candidate material not yet promoted. Named in a doctrine note as a candidate for promotion, with a forcing-case discriminator pending. Compiles. Build-covered if a candidate aggregator includes it. Not part of the public claim. |
| `DEPRECATED` | Retained but no longer current authority. Held for rename trail, import alias during a move, or historical artifact under a deletion-soon flag. Should carry a target removal date or a forwarding pointer. |

### How the five classes separate

The five classes partition `.lean` files along two questions: *Is it in the public build?* and *What is the corpus's posture toward the signature?*

| | Public build | Not in public build |
|---|---|---|
| **Authority promised** | `PUBLIC-SHIPPED` | — |
| **Compiled support, no signature promise** | `ANNEX` | — |
| **Exploratory / fenced** | — | `SCRATCH` |
| **Candidate for promotion** | (rarely) | `UNRATIFIED-CANDIDATE` |
| **Outgoing** | `DEPRECATED` (during sunset) | `DEPRECATED` (during sunset) |

`PUBLIC-SHIPPED` and `ANNEX` both sit in the public build but differ on whether the signature is a public claim. `SCRATCH` and `UNRATIFIED-CANDIDATE` both sit outside the public build but differ on whether the file is on a promotion track. `DEPRECATED` cross-cuts — it is the only class defined by trajectory rather than current posture.

### Classes excluded by design

Three candidate classes from earlier drafts remain excluded:

- **PUBLIC-SHIM** — empty cell until a real downstream consumer forces it. The current move policy is no shims unless breakage is documented; until then a shim file would be a memorial plaque for a mistake nobody has made.
- **ARCHIVAL** — collapses into `SCRATCH` with extra ceremony. If a file is genuinely no longer of interest, it should be deleted, not relabeled. If it's still useful as record, `SCRATCH` covers it.
- **SPECIMEN / DEMO** (subsumed under `ANNEX`) — consumer specimens that exercise the public surface in concrete settings (the SafetyBridge family, ConsolidationDenial, Examples) were briefly considered as a distinct class. They are `ANNEX` per the same rule that covers kernel-adjacent extensions: compiled support, not signature-promised. A separate class would split ANNEX without changing the custody guarantees.

A sixth class added later must clear the same bar: a forcing case, not a vibe. ANNEX was added 2026-06-05 because the Phase 2 audit identified 24 of 47 files that fit none of the original four — a clear forcing case. Future additions should be backed by an audit, not a hunch.

### Consistency with the kernel aggregator

The ANNEX definition above matches the language used in `LeanProofs/Admissibility/AdmissibilityKernels.lean`'s "Annex (ANNEX custody class — compiled support, not public surface)" section. The aggregator enumerates ANNEX files in two sub-groups (kernel-adjacent annex; consumer specimens); this doctrine file declares the class itself. The two layers are designed to agree.

## The marker convention

The two-layer convention sits inside the existing module docstring:

```lean
/-
Custody-Class: PUBLIC-SHIPPED
Custody:
  This file is canonical because <reason — typically: imported by the public aggregator,
  commit-hash + lake-build proof gate + ratification rule on changes to its key types>.
  A definition matching this signature elsewhere does not inherit this anchoring.
-/
```

The `Custody-Class:` line:

- appears exactly once per file
- carries one of the five ratified strings, no others
- is the grep target a checker script (Phase 3) verifies

The `Custody:` paragraph:

- preserves whatever existing custody narrative the file already carries
- remains free-form prose
- is human-legible, not machine-checked

Where an existing file already has a `Custody:` paragraph (a dozen or so as of this filing), it stays. The `Custody-Class:` line is added above it. Where a file has no custody material at all, both are added: the class is whichever class the Phase 2 audit assigns; the prose is one sentence stating the reason.

## What this is not

- Not a build-system change. Class labels are docstring discipline.
- Not a promotion mechanism. Adding `Custody-Class: PUBLIC-SHIPPED` to a file does not promote it; the promotion is the import in the public aggregator, of which the class label is the receipt.
- Not a substitute for the per-file custody prose. Class without prose is exactly the laundering surface the prose was added to close.

## Sibling discipline

The reason classes are necessary is the discipline named in [`wiring-is-not-folder-placement.md`](wiring-is-not-folder-placement.md) ([[project-wiring-vs-folder-placement]]): folder placement is not custody, and the three concepts (physical location / build coverage / public claim status) are independent. A class label is the per-file receipt for the third concept, decoupled from the first two.

The companion rule, in [`promotion-claims-require-custody-witnesses.md`](promotion-claims-require-custody-witnesses.md), states the dual: a promotion claim made in memory, README, or doctrine without an artifact-level custody witness is itself an admissibility failure. Class labels are the artifact-level witness.
