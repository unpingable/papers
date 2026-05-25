# Calculus 2.0 — exit criteria

> **Status:** internal exit-criteria record. Not a 2.0 commitment.
> Companion to [[kernel-to-body-map]] and [[frontier-proof-obligations]].

## What "full body" means here

The 1.0 surface is named, versioned, and DOI'd. **Under this map**, Calculus 2.0 (the body) exists iff *all* of:

1. *Authorized ≠ Safe* is mechanically exhibited (`AuthorizedNotSafe.lean`).
2. A minimal safety bridge proves safety **only under explicit extra hypotheses** (`SafetyBridge.lean` with a non-trivial `SafetyEnv` obligation).
3. `LocalBoundary.MergeAdmissible` has **necessity** (for the named exposure-safety property under the current `LocalBoundary` model), not just sufficiency (`merge_admissible_necessary`).
4. At least three bad merge cases are formalized as `MergeAdmissible` violations.
5. Self-amendment is blocked without weakening the 1.0 transition story (wrapper module, no mutation to `StateTransition.lean` until forced).
6. Annex axes either compose (with a theorem that has a consumer) or are explicitly kept outside the surface.

Until all six land, "Calculus 2.0" is not a thing that exists. The map is allowed to point at an unbuilt body. *More modules, more theorems, more vibes* is not progress.

The "Under this map" qualifier is load-bearing: future Frontier 5 (currently reserved) or a downstream forcing case may change the body shape. This document is allowed to be revised. It is not a constitution.

## Phase 1 — verification criteria

Phase 1 of the body work is exactly one file: `LeanProofs/Admissibility/AuthorizedNotSafe.lean`. Verification:

- `lake build` (no args) passes; the new file is wired into root.
- `grep -rn "sorry" LeanProofs/` returns only the docstring-text references already documented in `Admissibility/README.md`.
- `AuthorizedNotSafe.lean` exhibits, in Lean, a state pair `s₀, s₁` and a `Step` such that `AuthorizedStep` holds on the transition and a `DefendedValue` (inline-defined, minimal) strictly decreases.
- The file's docstring states what 1.0 does not imply, names the wound, and points at `FRONTIERS.md` Frontier 1.
- The docstring includes the scope clause: *this proves `AuthorizedStep` does not imply preservation of arbitrary defended value; it does not prove that no safety bridge exists.*
- `WHAT-THE-LEAN-STACK-PROVES.md` gains one sentence: *authorization does not imply preservation of defended value; see `AuthorizedNotSafe.lean`.*

Root-wired means build-covered; it does not mean public-surface-promised. The 1.0 surface (named in `CalculusOne.lean`) is unchanged by Phase 1.

For each later slice (if and when it lands): the same five-step proof pattern from [[frontier-proof-obligations]], the same ledger update, the same non-claim disclosure.

## What this document is not

- Not a project plan. Slice ordering is in [[kernel-to-body-map]].
- Not a proof ledger. Per-frontier obligations are in [[frontier-proof-obligations]].
- Not a release schedule. None of the six conditions has a date.
- Not a sufficiency claim. Meeting all six lands the body *as currently mapped*. Frontier 5 reserved precisely because the map is allowed to learn.
