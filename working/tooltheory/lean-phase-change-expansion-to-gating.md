# Lean phase change: expansion → gating

**Status:** UNRATIFIED working note. Posture, not theorem detail.
**Date filed:** 2026-06-09.
**Custody:** `working/tooltheory/`. Not a Lean module. Not kernel-adjacent.
The note governs Lean work; it does not promote into it.

## Claim

The Lean / admissibility work has moved from **expansion** to **gating**.

- *Expansion* asked: can this vocabulary be made crisp enough to
  formalize? Answer: yes. It produced real banked value —
  countermodels, non-conversions, dependency-arrow corrections,
  custody discipline, the receipts-at-every-boundary habit that
  propagated into NQ and Nightshift.
- *Gating* asks: a proposed `therefore` at a tool/prose boundary
  wants to fire. Does it pay the toll?

Continuing kernel production at the expansion rate doesn't multiply
the banked value. It risks the vocabulary-mill failure mode named in
[[genre-diagnosis-lean-admissibility]] §7.

## Rule

Do not add new Lean kernels unless at least one is true:

1. A tool decision would change.
2. A runtime boundary needs a receipt.
3. Prose asserts a dependency, bridge, or non-conversion.
4. A human/model proposes a conversion that needs testing.
5. A forcing consumer demands a reusable checker/law.

If none hold, the candidate goes into `working/tooltheory/` or
`working/admissibility/` with the forcing event named, and stays
there.

## Immediate build order (today's three pending items)

Per Fable's bucket-1 analysis, the items whose forcing events have
already fired:

1. **Receipt linter / generated seam inventory.** Forcing event
   already happened twice this week (manufactured-receipts incident;
   see [[receipt-integrity-and-seam-graphs]]). Weekend-scale.
   Retires an entire drift class.
2. **Router closed-set certificate metatheorem** in
   `TopologyRouterCandidate.lean`. ~30 lines. Makes the router's
   negatives general instead of ad hoc; rides the same `lake build`.
3. **StateTransition matrix cells as hygiene.** 12 `rfl`-shaped
   theorems closing the cells §3a of [[seam-graph-candidate]] still
   indicts. Half-hour batch. Do *not* call the result "orthogonality
   square closed" without naming the layer.
4. Nightshift-local claim routing — only when runtime path demands
   it ([[conversion-router-candidate]], [[project-nightshift-forcing-consumer]]).
5. NQ TESTIMONY_DEPENDENCY V2 — future forcing event when it lands.

## Cross-tool watch

Nightshift now talks to Agent Governor as well as NQ.

**Forcing event:** one tool must consume another tool's refusal as
input to its own decision (e.g., agent_gov reads `ns.wlp_refusal.v1`
and demotes a binding; or Nightshift reads a governor refusal and
declines to cook).

Until then, do *not* design a universal refusal schema. Keep this as
an interop watch item. The brochure swamp begins exactly here.

## Non-goals

- No new kernel families for taxonomy growth.
- No "topology" unless real topology appears.
- No Cedar-for-claims (see [[cedar-shaped-certificate-checker-candidate]]).
- No verified-governance framing.
- No generic platform before a second caller exists.

## Working phrase

> Lean is where `therefore` goes to get checked.

## The diagnostic

When did a new kernel last change a decision in one of the tools
(NQ / Nightshift / agent_gov / wicket / wlp) — not inform a docstring,
**change a decision**?

- Recent → keep producing.
- Have to think about it → gating phase has arrived; the feeling of
  diminishing returns is accurate, not a sign the work was hollow.

## Provenance and common-mode caveat

This note synthesizes Fable (Anthropic web 2026-06-09) +
chatgpt independent agreement on the build ordering. **Common-mode
caveat** ([[feedback-claude-common-mode-synthesis]]) applies to the
slogan-shaped phrases ("Lean is where `therefore` goes to get
checked," "gating phase," "claim-custody substrate"). The check that
saves these from being vibe-grounded is that the load-bearing
artifact-level claim — the receipt linter is the next real build — is
**receipt-grounded**: the forcing failure happened, on the record,
twice this conversation. That receipt is what licenses adopting this
note as posture; the framings live in tooltheory custody and can be
revised when reality reshapes them.

## Doctrine links

- [[receipt-integrity-and-seam-graphs]] — the linter (build 1) note.
- [[conversion-router-candidate]] — Nightshift-scoped, parked behind
  runtime forcing event (build 4).
- [[seam-graph-candidate]] — current snapshot inventory; becomes
  build output once 1 lands.
- [[cedar-shaped-certificate-checker-candidate]] — superseded; what
  not to call the linter.
- [[genre-diagnosis-lean-admissibility]] — vocabulary-mill failure
  mode (§7); informs the rule above.
- [[feedback-lean-phase-change-gating]] — memory-tier pointer to
  this note + the five-condition rule.
- [[feedback-forcing-case]] — broader forcing-case discipline; the
  five conditions are forcing-case discipline applied to kernel
  production.
- [[project-nightshift-forcing-consumer]] — the named runtime
  consumer that flipped build 4 from parked to scoped.
