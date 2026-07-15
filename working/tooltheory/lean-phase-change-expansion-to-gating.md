# Lean phase change: expansion → gating

**Status:** UNRATIFIED working note. Posture, not theorem detail.
**Date filed:** 2026-06-09.
**Custody:** `working/tooltheory/`. Not a Lean module. Not kernel-adjacent.
The note governs Lean work; it does not promote into it.

**Policy correction (2026-07-14):** “gating” below governs priority, scope, and public custody, not permission to formalize. A coherent claim, countermodel, or specification may be developed in Scratch before a tool/runtime consumer exists, and the formal contract may lead later code. Runtime adoption or citation names an intended contract; conformance requires an explicit mapping plus runtime evidence or a refinement proof. Intrinsic model, theorem-shape, overlap, proof/axiom, and non-vacuity checks remain.

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

## Priority and promotion rule

The following conditions raise priority and can support later public promotion of a new Lean kernel:

1. A tool decision would change.
2. A runtime boundary needs a receipt.
3. Prose asserts a dependency, bridge, or non-conversion.
4. A human/model proposes a conversion that needs testing.
5. A consumer would benefit from a reusable checker/law.

If none hold, the default priority is to keep the candidate in
`working/tooltheory/` or `working/admissibility/` with the motivating
question named. That is a triage default, not “prose only”: a bounded
Scratch formalization may proceed from a coherent statement and may
lead implementation.

## Immediate build order (today's three pending items)

Per Fable's bucket-1 analysis, the items whose priority evidence had
already arrived:

1. **Receipt linter / generated seam inventory.** The motivating
   failure already happened twice this week (manufactured-receipts incident;
   see [[receipt-integrity-and-seam-graphs]]). Weekend-scale.
   Retires an entire drift class.
2. **Router closed-set certificate metatheorem** in
   `TopologyRouterCandidate.lean`. ~30 lines. Makes the router's
   negatives general instead of ad hoc; rides the same `lake build`.
3. **StateTransition matrix cells as hygiene.** 12 `rfl`-shaped
   theorems closing the cells §3a of [[seam-graph-candidate]] still
   indicts. Half-hour batch. Do *not* call the result "orthogonality
   square closed" without naming the layer.
4. Nightshift-local claim routing — parked by current priority pending
   runtime-path pressure ([[conversion-router-candidate]],
   [[project-nightshift-forcing-consumer]]); a coherent formal contract
   may nevertheless lead that path.
5. NQ TESTIMONY_DEPENDENCY V2 — future priority/instantiation evidence
   if it lands.

## Cross-tool watch

Nightshift now talks to Agent Governor as well as NQ.

**Interop stress case:** one tool consumes another tool's refusal as
input to its own decision (e.g., agent_gov reads `ns.wlp_refusal.v1`
and demotes a binding; or Nightshift reads a governor refusal and
declines to cook).

Do not promote or deploy a universal refusal schema merely from this
watch item. A bounded formal schema or countermodel may be developed
first if its scope is coherent; runtime conformance would still need
the exact interop mapping and evidence. The brochure swamp begins when
the bounded contract is silently advertised as universal.

## Non-goals

- No new kernel families for taxonomy growth.
- No "topology" unless real topology appears.
- No Cedar-for-claims (see [[cedar-shaped-certificate-checker-candidate]]).
- No verified-governance framing.
- No generic platform before a second caller exists.

## Working phrase

> Lean is where `therefore` goes to get checked.

## Claim-custody substrate (index phrase, not new direction)

The constellation as a whole — NQ / Nightshift / Wicket / WLP /
Continuity / Lean / tooltheory — is best understood as **a claim-
custody substrate**: a small operational stack that prevents
claim-surface laundering by requiring receipts, bridges, cuts, or
refusals at every boundary.

Role split (not a new architecture, a name for what already exists):

- **NQ** — testimony production. Bounded observations under named
  evaluator / route / SQL contract / freshness state / dependency
  chain. Emits, does not decide.
- **Nightshift** — claim-routing and closure consumer. First place
  the apparatus becomes operational. Receives testimony; routes
  toward Wicket Intent / WLP Authorization / Continuity handling /
  refusal.
- **Wicket / WLP / Continuity** — authority separations (gates), not
  microservices. About write authority and conversion authority.
- **Lean** — development surface for establishing and checking the
  vocabulary contract; it may lead subsequent tool code. Lean need
  not sit in the runtime path: a tiny extracted or separately
  implemented checker can enforce the mapped contract. Adjudicates
  conversions, not the world.
- **tooltheory** — containment layer for receipt-integrity rule,
  generated inventories, conversion-router candidate, genre
  diagnosis, framing/method notes. Keeps the Lean tree from becoming
  a junk drawer of philosophical weather systems.

The substrate framing is index, not direction. It does not itself
promote modules, propose a unifier, or promote the federation into a
system. It names what the rest of the working notes are already about;
bounded Scratch formal work needs no additional consumer permission.

## The diagnostic

When did a new kernel last change a decision in one of the tools
(NQ / Nightshift / agent_gov / wicket / wlp) — not inform a docstring,
**change a decision**?

- Recent → high implementation/promotion priority.
- Have to think about it → lower current priority; the feeling of
  diminishing returns is useful triage evidence, not a prohibition on
  coherent formal development.

## Provenance and common-mode caveat

This note synthesizes Fable (Anthropic web 2026-06-09) +
chatgpt independent agreement on the build ordering. **Common-mode
caveat** ([[feedback-claude-common-mode-synthesis]]) applies to the
slogan-shaped phrases ("Lean is where `therefore` goes to get
checked," "gating phase," "claim-custody substrate"). The check that
saves these from being vibe-grounded is that the load-bearing
artifact-level claim — the receipt linter is the next real build — is
**receipt-grounded**: the forcing failure happened, on the record,
twice this conversation. That receipt supports this note's priority
posture; the framings live in tooltheory custody and can be revised
when reality reshapes them.

## Doctrine links

- [[receipt-integrity-and-seam-graphs]] — the linter (build 1) note.
- [[conversion-router-candidate]] — Nightshift-scoped, parked by
  current priority pending runtime pressure (build 4); formal work may
  lead the runtime path.
- [[seam-graph-candidate]] — current snapshot inventory; becomes
  build output once 1 lands.
- [[cedar-shaped-certificate-checker-candidate]] — superseded; what
  not to call the linter.
- [[genre-diagnosis-lean-admissibility]] — vocabulary-mill failure
  mode (§7); informs the rule above.
- [[feedback-lean-phase-change-gating]] — memory-tier pointer to
  this note + the five-condition rule.
- [[feedback-forcing-case]] — historical forcing-case discipline; the
  five conditions remain priority/promotion evidence, not build
  permission.
- [[project-nightshift-forcing-consumer]] — the named runtime
  consumer that raised build 4's priority and supplied a concrete
  instantiation target.
