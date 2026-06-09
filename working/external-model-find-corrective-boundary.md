# External-model find: CorrectiveBoundary dependency-arrow reversal

**Status:** receipt 2026-06-09. Patch landed and built green. Not doctrine.
**Patched file:** `~/git/lean/LeanProofs/Admissibility/CorrectiveBoundary.lean`
**Build:** `lake build LeanProofs.Admissibility.CorrectiveBoundary` ✔ 702ms;
full repo `lake build` ✔ (8306 jobs).

## Exportable lesson

> **The artifact-level claim survives Claude common-mode; the patch's
> exact term does not. Always run the compiler.**

Cross-model verification chain produced a *real* find — a falsified
dependency claim in a Lean structure docstring — and a *plausible* patch
that needed local typechecking to converge. Hand-trace caught the shape
of failure, not the exact line.

## What happened

External model (Anthropic web release named "Fable", same-day launch,
common-mode with Claude Code) was given a stale brief by ChatGPT asking
it to discharge a `sorry` in `Corrective.lean`. Fable cloned the
`unpingable/lean` repo, found the `sorry` had already been resolved a
month prior (2026-05-07) in `CorrectiveBoundary.lean` via genuine
model-dependence rather than axiom-laundering, and then went looking for
real seams in the resolved artifact.

It found one: the docstring on `NondegenerateStoreSemantics` claims the
three commitments are "independently meaningful prerequisites that the
third depends on" — a dependency claim that the structure itself
refutes in both directions:

- **(3.3) → (3.2) is provable.** Pigeonhole on the intermediate state:
  if a two-step `[corrective, forward]` sequence flips authority from
  not-authorized to authorized, then at least one step flipped it.
  So `verdict_sensitive` is a *consequence* of `mixed_class_witness`,
  not a prerequisite.
- **(3.3) ↛ (3.1).** Counter-model: identity `applyUpdate` with
  nondegenerate `appendRevocation` + a perverse `BasisDerivation` that
  reads revocation-store membership as a basis grant. The `recordRevocation 1`
  step then mints authority via a corrective channel while `applyUpdate`
  stays trivially identity. `revoked_never_admissible` discharges
  vacuously by declaring nothing revoked. This is exactly the laundering
  shape `Corrective.lean`'s open question #4 names.

So the docstring's three-flat-prerequisites framing was wrong: the
structure is **(3.1) independent / (3.2) entailed / (3.3) load-bearing**,
not a uniform list. `NondegenerateStoreSemantics` is explanatory
packaging, not a minimal basis.

## Verification chain

| Step | Actor    | Result |
|------|----------|--------|
| Find | Fable    | Artifact-level claim correct (pigeonhole valid, counter-model sound) |
| Critique | ChatGPT  | Three refinements: mirror field shape, name the counterclaim, mandate docstring fix |
| Audit | Claude Code (this session) | Verified `IsCorrective`/`IsForward` classification, traced `decideAuthority` reduction on the perverse env, confirmed `papers/working/...` cited path is a cross-repo legibility issue (not a missing file) |
| Patch | Claude Code | Applied v2 patch as Fable wrote it |
| Build | `lake` | **Red on first try.** Line-by-line below. |
| Fix | Claude Code | One-line correction, see below |
| Rebuild | `lake` | Green |

## Diagnosed gap between hand-trace and elaborator

Fable's pre-diagnosis listed two risk coordinates with fallbacks. The
actual failure was a **third** coordinate it didn't flag:

- **Risk #1 (Fable's call: low):** `decide` calls in
  `mixed_class_witness_holds`. **Correct.** Both `decide` calls fired
  first try on the perverse env's concrete `decideAuthority` reduction.
  Precedent prediction from `Witness.decideAuthority_*` machinery held.
- **Risk #2 (Fable's call: known-fragile):** the `rw [hpost]; rw [hmid]; exact hpre`
  chain in the pigeonhole proof. **Correct shape, lower risk than
  predicted.** Worked first try once the surrounding `set` was removed.
- **Risk #3 (Fable's call: known-fragile):** `set ... with hvΓ` goal
  abstraction unifying with the existential body. **Fable wrote the
  spot; the actual failure was upstream of it.** `set ... with` is a
  Mathlib tactic. The file imports only `LeanProofs.Admissibility.Authority`
  and gets no Mathlib transitively. Lean reported `unknown tactic` on the
  `set` line itself, never reaching the unification concern.
- **Unflagged failure mode:** "tactic availability under the file's
  import graph" was not in Fable's risk catalog. The hand-trace
  reasoned about *what `set` would do* without checking whether `set`
  was importable.

**Fix:** applied Fable's own fallback ("drop the `set` entirely and
inline"). With `set` removed, `by_cases hmid : decideAuthority env (applyStep ops Γ sc) a K = decideAuthority env Γ a K`
works directly, and `rw [hpost, hmid]; exact hpre` closes the goal in
one line. `by_cases` is available without Mathlib — sibling
`GuardCollapse.lean` uses it on identical decidable-equality cases.

The fallback existed in the brief. The recovery was one line. But
"compiled as written" would have been false.

## Calibration data point

Fable's hand-trace was **shape-correct but not line-correct**. Useful
enough that recovery cost ~30 seconds; misleading enough that "I
hand-checked it against v4.29.0 semantics" should not be read as
"compiler-ready." The thing it could not simulate was the file's import
context, which gates which tactics are even legal names — not a
semantic question, a namespace question.

If reusing Fable (or any toolchain-blocked external model) for proof
work:

- Take the find seriously when it's artifact-level (logic, types,
  counter-models exhibitable inline).
- Take the patch's *direction* seriously when the model has read the
  file.
- Do not take the patch as compiler-ready. The compiler is the only
  authority on whether the term elaborates.
- Specifically watch for tactic availability — that's the failure mode
  hand-trace cannot catch.

## Doctrine connections

- **[[feedback-claude-common-mode-synthesis]]** — Fable is on the
  common-mode side of the interferometer. The artifact-level claim
  (pigeonhole + counter-model) survives common-mode because it's
  inspectable. The framing ("explanatory packaging, not a minimal
  basis") that both Fable and ChatGPT converged on is synthesis-altitude;
  it's probably right, but two Claude-family models agreeing on phrasing
  is not vendor independence. The doctrinal phrasing in the new
  docstring should be considered candidate, not ratified.
- **[[feedback-verdict-compression]]** — Fable's "I can prove I can't
  build" move (verifying the 403 from the elan release endpoint instead
  of asserting the toolchain block from memory) is the freshness-axis
  discipline applied to its own capability claim. Worth reinforcing as
  a positive pattern: *refuse to relay your own past assertions
  un-rechecked*.
- **[[feedback-live-audit-over-cached-roadmap]]** — Fable's first move
  on the stale brief was to clone and check current state rather than
  work from the brief's snapshot. Same shape.
- **[[project-no-unifier-without-laundering]]** — the find itself is in
  the family: a docstring claim that asserted a free composition
  (between three structure fields) where no such composition exists.
  The structure was quietly carrying a laundering shape in its prose.

## Cross-repo provenance seam (separate issue)

`CorrectiveBoundary.lean:24` and `:467` both cite `papers/working/nondegenerate-store-semantics.md`.
The file exists in `~/git/papers/working/` — a sibling repo to
`~/git/lean/`. From a fresh clone of the public `unpingable/lean` repo,
the path resolves to nowhere; from the local two-repo workspace, it's
fine. Fable read this as "unreachable provenance pointer." It's not
quite that — the file exists — but it is a real cross-repo legibility
issue: the public Lean artifact has citations that require the sibling
repo to be cloned for the references to resolve. Not patched in this
pass. Filed for future cleanup: either inline the commitment text or
rewrite the citation to make the cross-repo dependency explicit.
