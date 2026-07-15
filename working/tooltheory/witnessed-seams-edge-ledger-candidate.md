# Witnessed seams — the edge-verdict ledger (CANDIDATE)

**Status:** CANDIDATE / non-binding. Scratch is justified; promotion is
conditional (gate below). Filed 2026-06-30 after a three-voice convergence
(ChatGPT + Claude-web + Claude-Code live check) on `SeamEdges.lean`.

Parent doctrine: `[[project-no-unifier-without-laundering]]`. Sibling:
`[[project-bridge-obligation-lattice]]`. Specimen: `~/git/lean/LeanProofs/Scratch/SeamEdges.lean`.

## The reframe (what raises SeamEdges' uniqueness)

My first review scored `SeamEdges` as a bridge-obligation specimen and dinged
the overlap with `SafetyBridge`/`NoFreeStandingBridge`/`ProjectionLaundering`.
The federation context moves it to a **different altitude**, and at that altitude
it is genuinely new:

> The kernels are the **vertices** of the federation graph. The three node
> shapes (existential-countermodel / conditional-rule / DeferredWitness) specify
> the vertices completely. The **edges** — directed pairs where one kernel's
> certificate becomes another's input — were left as assumed-passable glue.
> `SeamEdges` is the **edge-verdict ledger**: a type that forces every directed
> crossing to carry a verdict. It is NOT a new obligation kernel.

**No-unifier is the lower bound on seam cost.** If edge-labels reduced to a
node-property, that node-property would be the unifier `[[project-no-unifier-without-laundering]]`
proves can't exist. So seam-irreducibility is the **dual** of the
independent-failure-modes benefit: a monolith has one calculus and no seams (one
bug is global); a federation has independent failure modes but irreducible seams.
No-unifier is the impossibility theorem for "federation AND cheap seams." The
seams are the *price* of the property the architecture exists to buy, and the
price provably can't be discounted.

Keeper lines:
- *Expression can route the actor. It cannot ratify the route.*
- *A seam may translate evidence, restrictions, or requirements, but it may not
  launder expression, evidence, or convenience into authority.*
- The goat's badge is `axiom seam_AB : Cert_A → Req_B`. A witnessed federation is
  the one where every edge carries a verdict and zero edges carry that axiom.

## Empirical finding — the catalog is *starting*, not finishing

The thread asked: do the existing negative reachability results sit at **seams**
or **inside kernels**? Checked against the live Lean (2026-06-30):

- `Δs/Δk/Δh` are all nodes of **one** `Domain` type under **one** `edge`
  relation in `TaxonomyGraph.lean` (the 15-failure-mode diagnostic taxonomy).
  So `ds_not_reaches_dh` / `dk_not_reaches_dh` are **intra-graph
  non-reachability — NOT cross-kernel seam refusals.** (Sharper than the thread's
  "smells like negative crossing evidence" — the Lean is unambiguous: one node
  type, one edge relation.)
- The ONLY genuine cross-kernel seam refusals in the tree are
  `no_paid_authority_to_freshness` / `no_paid_freshness_to_authority`
  (`WitnessedReachability.lean`, codex 2026-06-29) — and those are
  **near-vacuous** (the WDC embedding bridges only freshness→freshness, flagged
  honestly in the docstrings).

**Conclusion:** the federation edge layer is essentially **unlabeled**. SeamEdges
is *starting* the edge catalog, not finishing it. The frontier is the full
realized edge set — bounded by the deployed governor's actual dataflow (linear-ish
in a fixed pipeline), NOT the k(k−1) all-pairs ceiling. Label the edges the
topology actually traverses.

## What SeamEdges legitimately owns vs must NOT mint

- **Owns (new):** the verdict vocabulary — `constructedBridge` / `constructedRefusal`
  / `unlabeled` / `axiomToken` / `sorryToken`, with the last three non-authorizing
  by construction. `bare_seam_not_authority_bearing` ("a `Cert → Req` is only
  syntax"). `authority_bearing_cases` (bridge|refusal are the only authority
  paths; no exclusivity claimed → no retired-trichotomy revival). This is a
  *ledger type for cross-kernel composition status* — a different object from the
  obligation kernels.
- **Must NOT mint:** `EdgeDiscipline`'s five obligation atoms. Those have homes:
  `noAuthorityWiden`≈`SafetyBridge.gap_blocks_safeStep_lift`/`AuthorizationBridgeGap`,
  `noStandingMint`≈`NoFreeStandingBridge`, `noCustodyErase`≈`ProjectionLaundering`,
  `noSpendDuplicate`≈`LinearSpendStanding`. Re-bundling them as fresh fields is
  "doctrine duplicate in a lab coat."
- **Reconcile two different fives.** SeamEdges' five *obligations-to-discharge*
  (preserve/no-mint/no-erase/no-duplicate/no-widen) are NOT the same list as the
  no-unifier **bridge tax**'s five *elements-to-name* (source surface, target
  surface, witness, licensed claim, residual scope). Related, not identical. The
  overlap map below must map BOTH.

## Specimen honesty (belongs in the SeamEdges header)

The `ExpressionFrame → RationCard` specimen discharges exactly **one** substantive
obligation: monotone narrowing (`lower_allowed_subset_base`, *frames may narrow,
may not widen*). `preservesObligations` is definitional; the other three atoms are
`True` (vacuous — structurally absent from this toy seam). Honest claim:

> SeamEdges demonstrates verdict typing for seams and proves one monotone-lowering
> specimen; the other obligation slots are scaffold/vacuous, not discharged.

Do NOT phrase it as "SeamEdges discharges the five edge obligations."

`beSane` rejected as expressive residue = *moss is not evidence*
(`[[feedback-outofscope-no-jurisdiction-over-moss]]`): soft caller intent does not
lower to hard policy.

## Path/verdict-composition layer — BUILT in scratch (2026-06-30)

The one layer that was *forced* (a missing joint between two already-open objects:
`WitnessedReachability` composes reachability, `SeamEdges` types single edges,
nothing composed the verdicts) is now a typed probe, NOT just a note:
`~/git/lean/LeanProofs/Scratch/SeamPathVerdicts.lean` (SCRATCH, compile-is-contact,
green, axiom-classified `propext`/`Quot.sound`, no `native_decide`/`Classical.choice`).

- Reuses `SeamEdges.EdgeVerdict` by projecting its tag (`EdgeVerdict.vclass`); no new
  `PathVerdict` enum minted (avoids the retired composition-classifier attractor).
- **Contamination half:** `hole_contaminates` (one token edge un-labels the path),
  `bare_path_not_wellLabeled` (a nonempty list of bare `Cert→Req` is still syntax).
- **Money theorem** `global_not_implied_by_local`: two constructed-bridge edges each
  inside their LOCAL budget compose to a path that breaks the GLOBAL budget. Per-edge
  bridges are ingredients, not a trajectory receipt — the no-unifier result shown
  operationally. `single_local_ok_is_global` confirms the gap opens at composition
  (length ≥ 2), not from a degenerate model.

Keeper: *local bridge receipts are ingredients, not a trajectory receipt; a path is
authority-bearing only through a constructed path verdict, never by the conjunction
of authority-bearing edges.*

The remaining three layers below stay **named, not currently scheduled**. Their dependencies and theorem shapes—not the absence of a runtime forcing case—govern formal development.

## Adjacent layers — named, formalize in dependency order

- **Declared edge-set / "no free edge"** — the governor's wiring is itself a claim
  (adding a seam needs authorization, dual to no-free-standing-bridge). Partly
  gestured at by `CounterfactualEdges` + `ControlPathIndependence` (*wiring ↛
  standing*). Second-order; needs the path layer first, but not a runtime consumer.
- **Readout over verdicts** — "the graph says this path is admissible" is itself a
  claim someone must have standing to rely on (`CanRead ⊬ MayReadout`). Closes the
  regress so the ledger isn't a free oracle. Open only if the path layer starts
  claiming operational authority.
- **Co-graph / backward flow** — reverse edges carry refusal/revocation/receipts
  (`RefusalPropagation` + `Mandamus` already live here, unjoined to the forward
  ledger). A forward bridge that ignores a backward revocation is laundering. More
  "unify existing pieces" than new frontier.

Not layers, just attributes (do not reify): edge *freshness* (diachronic cross-section
of the edge layer, governed by the existing Readout split) and edge *linearity*
(owned by LinearAccountant) — see next section.

## Open question (genuinely unresolved): does seam-crossing consume?

A bridge *theorem* is reusable (not consumed). But an instance-level crossing
*receipt* may need linear discipline when the source is authority-bearing —
cannot turn one spendable cert into several, refresh expiry, erase revocation, or
broaden downstream authority. For `expression → restriction`, no authority is
consumed (pure narrowing). For `Standing → Wicket` or `Wicket → LinearAccountant`,
linearity is likely load-bearing and the edge witness wants a linear flavor
(touches `~/git/linearaccountant/`). Unresolved — do NOT assume the analogy is
load-bearing until a real authority-bearing seam forces it.

## Promotion gate (before it leaves `Scratch/`)

1. **Overlap map** — for each `EdgeDiscipline` atom AND each bridge-tax element,
   name the existing Lean/prose home; declare reuse / shadow / illustration /
   divergence.
2. **No fresh doctrine atom** — SeamEdges may define verdict *status*; it may not
   redefine non-amplification / standing / custody / spend as if new. Refactor the
   obligation bundle into references/instances of existing homes.
3. **Specimen honesty** — vacuous obligations marked explicitly as non-discharge
   (header line above).
4. **Negative edge preserved** — `ConstructedRefusal` stays first-class; it is the
   deny-path-as-theorem half guarding the authority-adjacent seams, not ornament.
5. **No bare-function laundering** — `Cert → Req` remains syntax/evidence; never
   authority without a bridge verdict.

## Receipts

- `SeamEdges.lean` reviewed 2026-06-30: builds (exit 0, scratch/compile-is-contact),
  no sorry/admit/axiom decls; structural theorems zero-axiom, lowering theorems
  `propext`+`Quot.sound` (no `Classical.choice`).
- Δ-seam finding verified against `TaxonomyGraph.lean` (one `Domain` type, one
  `edge` relation) and `WitnessedReachability.lean` (auth↮freshness near-vacuous).
