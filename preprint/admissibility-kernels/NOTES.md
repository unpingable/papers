# NOTES — drafting plan

**Filed:** 2026-05-29
**Status:** v0.2 axis-1 drafting plan. Not paper content. Suite reframe 2026-05-31: this artifact is **Axis 1** of the admissibility suite per `working/admissibility-suite-map.md`. Axes 2 (composition) and 3 (self-amendment) are separate kernel notes. Post-2026-06-03 synthesis closure, no unifying calculus paper is the target — surviving structure is the "disciplined premise production" umbrella over separate species. Lean characterization layer (`AuthPreserves`, `AuthorizationBridgeGap`, `MaximalBridge`, `BridgeComplete`, `HasForgetfulSection` + theorems) lives in `SafetyBridge.lean` as of 2026-05-31 and is candidate for inclusion in a §3 expansion (probably §3.9 collapse iff, §3.10 obstruction, §3.11 maximal-bridge corner).

## Sequencing

1. ✅ Title + abstract + claim list + theorem-target table (this scaffold pass).
2. ✅ §2 (formal apparatus) full draft (2026-05-31). Core apparatus items in formal-methods register; both load-bearing decisions surfaced (actor-inertness, per-hop-actor in substrate); v0 simplifications stated.
3. ✅ §3 (irreducible theorem family) full draft (2026-05-31). Sections 3.1–3.8: single-step wound; verdict-layer transfer; bridge dischargeability; positive composition; negative composition; no-lift; forgetful map; doctrinal mapping fence. Loop-Capture institutional reading kept to one fenced paragraph in §3.8.
4. ✅ §4 (two witnesses) full draft (2026-05-31). §4.1 receipt-poison miniature (short); §4.2 Nat-valued attestation ledger (longer), with `protocolHappyPath` acid test surfaced as multi-actor confirmation. Ledger language tightened per ChatGPT pass to avoid blockchain-cosplay register.
5. ✅ §5 (scope and non-claims) full draft (2026-05-31). Six bullets per the original plan.
6. ✅ §1 (introduction) full draft (2026-05-31). Thesis paragraph tightened per ChatGPT pass — "authorized trajectory family may contain paths whose endpoints fall outside the bridged trajectory family" — avoids "permanently and irreversibly" overclaim.
7. ✅ §6 (related work) full draft (2026-05-31). Four clusters per the lit-differential sketch below; Δt cross-references noted as background context only.
8. ✅ §7 (discussion) + §8 (conclusion) full draft (2026-05-31). §7 three-observation shape (cost asymmetry, composability, doctrinal handoff); §8 one paragraph. §7 tightened per ChatGPT pass — "real systems instantiate the antecedent" rather than "exploit this cost asymmetry."
9. ✅ Appendix A (module map) full draft (2026-05-31). 13 rows; clean per-row format (no merged-cell artifacts in row 7 — generic and verdict forgetful maps split to separate rows).
10. ✅ Appendix B (build and reproducibility) full draft (2026-05-31). ChatGPT rewrite: no Google-redirect URL, clean fenced bash block, "audited before release candidates" rather than "continuously audited."
11. ⏳ References — venue-dependent; defer formatting until target venue is locked.

## Lit-differential sketch

Four formal-methods clusters surface in §6:

1. **Authority / capability discipline.** Bundled-construction (mutation standing + claim verdict together) is the capability-style move; the safety-bridge family extends it with a third dimension (bridge witness). Cite: Miller's *Object Capabilities and Subjective Aggregation*; Lampson; Levy's authority-logic line. Differential: we do not classify state by capability level; the bridge is value-preservation discipline over a single externally-defined observable.
2. **Refinement / simulation.** Forgetful map is *not* refinement — it is witness-degradation. A `BridgedTraj` is not an implementation of an `AuthorizedTraj`; it is a stronger witness over the same trajectory shape. Cite: Abadi-Lamport's *Composing Specifications*; Lynch's I/O-automata framework. Differential: forgetful map is a function between inductive families with the same step-by-step structure; refinement is over behaviors.
3. **Information flow under transition.** Goguen-Meseguer noninterference and the subsequent declassification literature are the closest in spirit — bridge dischargeability is declassification-flavored. Cite: Goguen-Meseguer 1982; Sabelfeld-Myers survey; Sabelfeld-Sands declassification dimensions. Differential: we floor a single externally-defined observable, not classify state by security level. The bridge does not "declassify" — it admits the action only when value preservation is independently witnessable.
4. **Resource and obligation semantics.** Separation logic (O'Hearn-Reynolds-Yang); Hoare-CSP; obligation logics. Differential: bridge is not a resource accounting predicate; defended value is observable, not consumable. Closer kin to separation logic's "resources are values that flow through state" than to noninterference.

The four clusters frame the contribution as **a fifth flavor**: structural bridge discipline over a single defended-value floor, with the load-bearing innovation in the trajectory triple's no-lift theorem.

## Scope-fence checklist

Before any section ships, the scope fence must read:

- [ ] Kernel-legible all-green ≠ substantively-grounded legitimacy. (paper 28 fence)
- [ ] Conditional, not categorical. (`AND it does not certify safety in any specific system`)
- [ ] Structural bridges are conservative; maximal bridge collapses into preserves-restated.
- [ ] Not a unified calculus. Safety axis only; composition and self-amendment open as separate kernels.
- [ ] Not a process calculus; not refinement; not a complete safety policy; not certification.

The fence is checked in §5 explicitly; the introduction signposts it; §3 carries it on the Loop-Capture mapping note.

## What the preprint must NOT do

- Argue that real institutions exhibit the L/V divergence. That is paper 28.
- Introduce new Lean modules. The Lean source is finished; the preprint is exposition.
- Claim a unified-calculus framing. The frame was retired post-2026-06-03 synthesis closure; axes ship as separate kernels.
- Re-litigate the actor-inert vs actor-sensitive bridge decision. Ratify by stating it; defer the actor-sensitive extension as named-but-not-implemented.
- Cite the Δt corpus as load-bearing evidence. Δt-series references are background motivation only.

## What forces a re-scaffold

If any of the following changes between now and first draft, redo this scaffold:

- A new theorem lands in `SafetyTrajectory.lean` or `AttestationLedger.lean`. (Note: the trajectory-global → per-hop actor refactor at the generic layer *already landed* 2026-05-30 — see `working/tooltheory/trajectory-canonicalization-2026-05-30.md`; theorem-target table and §2 / §4 scaffold-direction notes refreshed.) Probably triggers an §4 expansion.
- A tier-2 model (budget-margin or quorum) lands. Triggers a "tier-2 preview" subsection in §3 or §7.
- Paper 28 starts drafting. May reshape §1 framing — though Fork B explicitly says the preprint goes first, so this should not be a forcing event.

## Venue and sequencing

Spine page (`working/admissibility-suite-spine-2026-05-28.md`) says: write the preprint first, paper 28 second. The preprint does not need to be *published* before paper 28 drafts begin, but it does need a citable scaffold (this) before paper 28 can forward-point.

Target venue: arXiv cs.LO at minimum. AI-safety venue (e.g. AI Safety Workshop, ICML SafeML, NeurIPS Safety) possible if framing supports. Decide after first draft; do not pre-format for a specific venue at scaffold stage.

## Identifier drift

Theorem names in this scaffold were verified against `~/git/lean/LeanProofs/Admissibility/` as of 2026-05-29 and refreshed against the post-canonicalization source on 2026-05-30 (manual + report-only drift check; see drift-check log in this directory if filed). The crosswalk automation (`tools/formalization_crosswalk.py`) should be run again before any draft revision touches the theorem-target table.

## Open question for v0.1 → v1.0 draft

The Loop-Capture mapping in §3 — how much should the preprint say about it? Two postures:

- **Minimal:** name the doctrinal mapping in one sentence as a downstream reading the no-lift makes available; fence it; move on.
- **Light gloss:** spend a paragraph on the mapping shape (legitimacy holds along the whole trajectory, value falls, no retrofit lift) explicitly framed as *a reading paper 28 will develop, not a claim of this paper*.

Lean toward minimal. The preprint's job is the formal kernel; the gloss invites the wrong kind of reviewer attention. Confirm at first-draft pass.
