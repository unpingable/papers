# Receipt integrity and seam graphs (method note)

**Status:** UNRATIFIED method note. Captures today's lesson; gates a
real next build.
**Date filed:** 2026-06-09.
**Custody:** working note in `working/tooltheory/`. Not a Lean module,
not kernel-adjacent. Lean files prove things; tooltheory notes
explain why those proofs became necessary.

## The receipt-integrity rule

**Status of any claim about a theorem moves only on grep/build
receipts against a named tree.** Not on chat-local lore. Not on what
the model remembers writing. Not on what an audit observed in
*somebody's* tree. The named tree is part of the receipt.

Concretely:
- "X is green" means `lake build` succeeded against commit/tree T,
  recorded with output.
- "X exists" means `grep '\bX\b' *.lean` returned at tree T, recorded.
- "X is missing" means the grep returned nothing at tree T, *which T
  named*.
- Without T, none of the above is a receipt — it is a claim about a
  tree, with the tree elided.

## The incident — what actually happened today

Two cases this conversation, both flagged by external-model audit
against `origin/main @ d9c3d4f`:

**Case 1: `amend_policy_preserves_{evidence,gap,revocation}_store`.**
The theorems existed in my local working tree (added earlier in this
session and `lake build`-verified). The audit clone, built against
`origin/main`, found nothing. The audit's framing was "manufactured
receipts" — not quite accurate; the receipts were real in *my* tree.
But the audit's underlying complaint was correct: I had cited the
theorems in a working note (`seam-graph-candidate.md`) as if their
existence were a public fact, without specifying the tree. From a
fresh clone of the public repo, my citation was a dangling pointer.

**Case 2: O1 / `mixed_class_witness_implies_verdict_sensitive`.**
Same shape. The theorem existed in my local tree (added in turn 1 of
this session, `lake build`-verified). The audit ran against
`origin/main`, found nothing, and held O1 in the inventory as
"blocked-candidate, not E26." I had treated O1 as closed without
flagging the tree mismatch.

The accurate framing of both cases: **the receipts existed; the
audit's failure was real; the disagreement was about which tree the
claim was indexed to.** Calling them "manufactured" overstates the
failure mode but understates the discipline gap. The discipline gap
is what generalizes.

## Why this matters structurally

The corpus's house style produces *receipt-shaped utterances*:
names like `corrective_no_authority_laundering`,
`visible_green_does_not_imply_recovery_margin`,
`refines_implies_collapsed_surface`. The pattern is so legible that
it is **spoofable** — by humans, by models, by anyone trained on the
style. A reader can write a plausible receipt-shaped sentence without
the receipt resolving anywhere.

Today's incident was the *non-malicious* version: real receipts on
the wrong side of a push boundary. The malicious version is the same
move with no receipt at all. The defense is identical in both cases:
**every status-moving claim names its tree and survives a grep
against it.**

## Why hand-maintained inventories rot

`seam-graph-candidate.md` is a 250-line prose inventory of theorem
names, edges, cuts, and cells. It is a snapshot. Every kernel patch
risks invalidating cells silently:
- Add a theorem ⇒ existing OPEN cell becomes an unsourced edge.
- Rename a theorem ⇒ existing receipt becomes a dangling pointer.
- Delete a theorem ⇒ existing edge becomes a phantom.
- Push a tree ⇒ "local-only" theorems become public, possibly under
  different names.

None of these are caught by the snapshot itself. They are caught by
re-running the audit, which only happens when someone notices the
inventory has gotten weird. The inventory rots by default.

## The next real build (1a in Fable's bucketing)

A **generated seam inventory + receipt linter.** Single sentence: the
hand-written inventory becomes build output from a TOML/JSON source,
with a CI step that greps every cited declaration name against the
repo and fails on dangling receipts.

Architecture:

- **Data file** (`working/tooltheory/seam-graph.toml` or `.json`):
  surfaces, edges (with `kind`, `receipt-URI`, `custody`), cuts (with
  `kind`, `receipt-URI`).
- **Linter** (~50 lines, language-agnostic but Python or Rust per
  user idiom): for each cited `receipt` field, verify the named
  declaration exists in the repo. Fail on missing. Emit a stale
  report including tree/commit ID.
- **Generator**: renders the inventory markdown from the data file.
  The hand-built `seam-graph-candidate.md` becomes build output.
- **Receipt schema**:

  ```toml
  [[edges]]
  id = "E4"
  src = "authorizedStep"
  dst = "authorizedVerdict"
  kind = "PRESERVATION"
  receipt = "LeanProofs.Admissibility.Execution.authorized_step_requires_authority"
  custody = "PUBLIC-SHIPPED"

  [[cuts]]
  id = "C18"
  src = "authorizedTrajectory"
  dst = "safe"
  kind = "COUNTERMODEL"
  receipts = [
    "LeanProofs.Admissibility.SafetyTrajectory.authorized_trajectory_loses_value",
    "LeanProofs.Admissibility.SafetyTrajectory.no_bridgedTrajC_to_poison_end"
  ]
  ```

This is the only candidate whose forcing event already happened
(twice, on the record this week). Weekend-scale. Retires an entire
drift class. The repo gets a CI step; the inventory stops being
scripture.

## The load-bearing design rule for the linter

**It validates presence, not meaning.**

- Linter says "`foo_does_not_bar` resolves to a declaration in
  `Bar.lean`." That is the entire claim.
- Linter does NOT say "`foo_does_not_bar` proves that foo does not
  bar." The proof might say something else; the docstring might lie;
  the theorem might be wrong. None of that is the linter's job.
- A future reader of the linted inventory still has to read the
  proofs. The linter just guarantees the receipts aren't phantoms.

Calling the linter "semantic validation" would be the
manufactured-receipt move with extra steps — a tool whose output is
treated as proof of meaning, when it only proves grepability. That
is how the receipt goblin gets tenure.

## Seam graph, not topology

The data structure under all this is a **finite labeled digraph with
reflexive-transitive closure and closed-set non-reachability
certificates**. There are no opens, no continuity, no closure axioms.
The signature move is *refusing* closure: no transitive composition
across module boundaries without per-edge backing; absence is
first-class; same-named primitives across modules are
non-identifications by default.

"Topology" buys nothing "finite digraph" does not, and it smuggles
the unifier in through vocabulary. The word is retired.

## What this note does NOT recommend

- Building a generic conversion-routing tool. That is
  [[conversion-router-candidate]] and is parked behind Nightshift's
  runtime forcing event.
- Building `RefusalKernels.lean` as an aggregator. The repo's own
  custody discipline says: named-not-built until a grouped import is
  demanded. The receipt linter is *not* a promotion path.
- Calling the linter "Cedar-shaped" or "policy-shaped." It is a
  presence checker. Anything more is the attractive nuisance from
  [[cedar-shaped-certificate-checker-candidate]]'s diagnostic
  treatment.

## Cohesion across the three tooltheory notes

The three live notes in this directory work together:

- **[[receipt-integrity-and-seam-graphs]]** *(this file)* — the
  method-level lesson and the next real build (linter).
- **[[conversion-router-candidate]]** — the Nightshift-scoped
  reusable core; parked behind a runtime forcing event.
- **[[seam-graph-candidate]]** — the current snapshot inventory;
  drift-prone; will become build output once 1a lands.

The relationship is causal: this note explains *why* the seam graph
needs to become generated, and *why* the conversion router stays
parked until forced.

## Sibling Lean work this method enables

Once the linter lands, three Lean-side moves become low-cost and
unblocked (Fable's 1b and 1c):

- **Closed-set certificate metatheorem** in `TopologyRouterCandidate.lean`:
  ¬Reach A B ⟺ ∃ forward-closed S, A∈S, B∉S. The completeness
  witness is the reachable set itself. ~30 lines.
- **StateTransition 12-cell hygiene batch**: prove the open matrix
  cells (3 amendPolicy-row preservations, 6 other off-diagonal
  preservations, 3 diagonal positives). All `rfl`-shaped. Turns
  "definition-backed" into "theorem-backed" so `seam-graph-candidate`
  §3a's OST6 indictment retires.

Both are file-scoped, build under pinned 4.29.0, and benefit from
the receipt-presence guarantee the linter provides.

## Doctrine links

- [[seam-graph-candidate]] — the snapshot inventory that will become
  build output once 1a lands.
- [[conversion-router-candidate]] — Nightshift-scoped router parked
  behind runtime forcing event.
- [[cedar-shaped-certificate-checker-candidate]] — analysis archive
  (superseded by conversion-router-candidate); reminds future-self
  what NOT to call the linter.
- [[external-model-find-corrective-boundary]] — first external-model
  finding pattern; introduced the receipt-integrity discipline
  implicitly.
- [[feedback-verdict-compression]] — relay traffic compression and
  custody-staling; the receipt-integrity rule is freshness-axis
  discipline applied to status moves.
- [[feedback-claude-common-mode-synthesis]] — multi-model
  collaboration is exactly where receipt-shaped noise has the highest
  generation rate.
- [[project-no-unifier-without-laundering]] — explains why the linter
  must validate presence, not meaning; meaning-validation would
  require the federation it refuses.
