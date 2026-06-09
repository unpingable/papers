# Conversion-router candidate (Nightshift-scoped)

**Status:** UNRATIFIED scoping pin. Forcing consumer named; surface
inventory and build commit pending.
**Date filed:** 2026-06-09.
**Custody:** working note in `working/tooltheory/`. Not a Lean module,
not a Rust crate, not promoted.

## Decision recorded

**Forcing consumer found.** Nightshift (`~/git/scheduler/crates/nightshiftd/`)
is the named runtime consumer of conversion-routing answers. Today's
WLP3 refusal landed (`witness-2026-06-09-wlp3-refusal-implementation.md`)
made the first dangerous conversion mechanically operational:
*freshness unresolved ⇏ authorization*, emitting `ns.wlp_refusal.v1`.

The remaining dangerous conversions Nightshift will need a checker for
(in roughly the order Nightshift's pipeline encounters them):

- receipt present ⇏ authority
- witnessed ⇏ admissible
- authorized ⇏ safe
- freshness unresolved ⇏ authorization *(landed today as WLP3 refusal)*
- Wicket Outcome exists ⇏ WLP authorization exists
- refusal propagated ⇏ mandamus obligation, unless locus bridge exists
  (links to `Mandamus.lean` per [[project-refusals-need-receipts]])

## Scope: Nightshift-local, not general

Build a **Nightshift-local conversion-route schema + checker**, scoped
to surfaces that appear on Nightshift's actual packet → Wicket → WLP
pipeline (Path A) and its refusal variants (Path A.5 + WLP3). **Do
not** build generic conversion-routing infrastructure. The trick is
keeping it Nightshift-local until runtime pressure proves it deserves
to escape containment.

## Explicitly NOT Cedar

Cedar comparison was useful for diagnostic purposes only and should
not appear in this artifact's marketing or design language:

- Cedar is **closed-world authorization**; this is **open-world
  epistemic conversion**. The engine's "no route" is about the
  inventory, never about the world.
- Cedar's policy *is* the authority; here the policy is a checker on
  receipts, never the source of authority.
- Cedar adjudicates **permission to access resources**; this
  adjudicates **admissibility of claim conversions**. Blurring the
  two would be exactly the laundering the kernels block.
- Calling this "Cedar for governance," "authorization language," or
  "policy DSL" would commit the corpus's founding crime in its own
  marketing. Refused. See [[cedar-shaped-certificate-checker-candidate]]
  for the diagnostic-only treatment.

## Naming candidates (doctrine-neutral preferred)

- `nightshift-convroute` (project-scoped, transparent)
- `claimroute` (doctrine-neutral, general)
- Receipt artifact kind: `ns.claim_route.v1` or `ns.conversion_preflight.v1`

## Reusable core (what Lean would actually prove)

Strip prose, this survives — and is exactly what the Lean side should
hold:

- finite labeled digraph + reflexive-transitive closure;
- **path certificate soundness** — a router-returned path is a real
  Reach witness;
- **closed-set certificate soundness AND completeness** — if ¬Reach
  A B, the reachable set from A is itself a certificate; every
  negative answer ships with an independently checkable witness;
- **bridge-addition monotonicity** — `Reach E ⊆ Reach (E ∪ {e})`;
  bridges only add routes; corollary: "B unreachable in E∖Bridges ⟹
  every A→B path crosses a bridge edge" — the precise content of
  *no route without bridge*.

Optional fifth (linter-grade, not theorem): every encoded edge's
`receipt-URI` field resolves to an existing declaration. Useful CI;
not a theorem; calling it one would be the manufactured-receipt move.

## Build shape (5 steps)

1. **Data file** — `surfaces`, `edges {src, dst, type, receipt-URI,
   custody}`, `cuts {src, dst, kind, receipt-URI}`. TOML or JSON.
   Includes `tree_or_build_id` field (receipt-integrity rule from
   [[external-model-find-corrective-boundary]]).
2. **Router** — BFS for positive path; closed-set certificate for
   negative; open / missing-bridge result.
3. **Checker** — ~50 lines, independently verifies path or closed-set
   certificate; does not trust router output. **This is the piece to
   prove correct in Lean and port.**
4. **Lean model** — the four soundness/completeness theorems above.
   Tiny.
5. **Generated markdown** — seam inventory becomes build output, not
   hand-maintained scripture. *The inventory rot hit twice this week
   is the motivating bug report.*

## Response shapes (per Nightshift pipeline)

```json
{
  "verdict": "path",
  "path": ["nq.finding", "witnessed", "admissible_with_scope", "closure_candidate"],
  "receipts_used": [...]
}
```

```json
{
  "verdict": "blocked",
  "cut": "freshness_unsettled_blocks_wlp_authorization",
  "certificate": ["witnessed", "wicket_intent", "wicket_outcome"],
  "missing_bridge": "freshness_to_wlp_authorization",
  "refusal_receipt": "ns.wlp_refusal.v1"
}
```

```json
{
  "verdict": "open",
  "missing_bridge": "standing_to_mutate",
  "note": "no theorem-backed edge or cut registered"
}
```

The blocked verdict on a Freshness-unsettled packet should reference
`ns.wlp_refusal.v1` — closing the loop with today's WLP3 implementation.

## Receipt artifact fields (candidate)

```json
{
  "artifact_kind": "ns.claim_route.v1",
  "from_surface": "...",
  "to_surface": "...",
  "verdict": "path|blocked|open",
  "edge_receipts": [],
  "cut_receipts": [],
  "missing_bridge": null,
  "closed_set_certificate": [],
  "source_receipt_ids": [],
  "tree_or_build_id": "..."
}
```

## TBD before any code commit

- **Surface inventory.** The 5–10 seed surfaces from Path A / A.5 are
  not yet enumerated in this note. Source-of-truth grounding required:
  the integration sweater (`~/git/agent_gov/working/nightshift-integration-sweater.md`),
  the actuation-boundary doctrine
  (`~/git/cartography/doctrine/nightshift-actuation-boundary.md`),
  and the WLP3 closure spec
  (`~/git/agent_gov/working/wlp3-closure-and-artifact-inventory.md`)
  need a read pass before any surface name is committed to schema.
  Until then, the surface list in this note is **deliberately empty**
  — placeholder discipline, not vocabulary mill priming.
- **Crate home.** `~/git/scheduler/crates/nightshiftd/` (in-process)
  vs. new sibling crate vs. external utility. Decision deferred until
  the checker's actual call site is known.
- **Lean home.** `~/git/lean/LeanProofs/Admissibility/` as
  UNRATIFIED-CANDIDATE module (sibling to `NoFreeStandingBridge.lean`,
  `TopologyRouterCandidate.lean`) vs. a separate `~/git/lean`
  subtree. The four theorems are file-scoped tiny; a single
  `ConversionRouter.lean` is probably the right home.

## Non-goals (explicit)

- Not topology (no closure operator; absence is first-class).
- Not Cedar-for-governance (see disclaimer above).
- Not verified agent policy (verification scope is the routing
  algebra; agent behavior is out of scope).
- Not a general-purpose conversion-routing infrastructure.
- Not a unifier across kernels (per [[project-no-unifier-without-laundering]]).
- Not semantic completeness over the world (the engine knows the
  inventory, not the world).

## Build trigger (when this stops being a parking pin)

Either:
- Nightshift's runtime hits the second non-Freshness blocked
  conversion and the team decides ad-hoc handling is no longer
  viable, OR
- The wicket / wlp / continuity boundaries surface a third refusal
  kind that demands the same artifact-emission pattern.

Whichever lands first concretizes the surface inventory and converts
this note's TBDs into committed schema.

## Doctrine links

- [[cedar-shaped-certificate-checker-candidate]] — the diagnostic
  Cedar-comparison material that informed this scoping decision.
  Superseded as the live design artifact; preserved as analysis
  archive only.
- [[seam-graph-candidate]] — typed-edge vocabulary this design
  consumes.
- [[genre-diagnosis-lean-admissibility]] — self-limiting genre
  description; the "Lean checks the map, not the governing" framing
  belongs in this design's first paragraph if/when built.
- [[external-model-find-corrective-boundary]] — receipt-integrity
  rule (status moves on grep/build receipts against named tree)
  enforced via the `tree_or_build_id` field in the receipt artifact.
- [[feedback-forcing-case]] — gates whether and when this design
  moves from scoping pin to build commit.
- [[project-no-unifier-without-laundering]] — explains why the
  Nightshift-local scoping is structurally required; a general
  conversion router would be the kind of unifier the doctrine refuses.
- [[project-refusals-need-receipts]] — Mandamus locus, the
  refusal-propagation link in the dangerous-conversions list.
