# NOTES — drafting plan

**Filed:** 2026-05-29
**Status:** scaffold-stage drafting plan. Not paper content. Bake out into `paper.md` as sections firm up.

## Sequencing

1. ✅ Title + abstract + claim list + theorem-target table (this scaffold pass).
2. ⏳ §2 (formal apparatus) full draft. The five definitions need to be readable in formal-methods register without leaking Lean syntax into the body. Block diagram or two-row table of the apparatus may be load-bearing for legibility.
3. ⏳ §3 (irreducible theorem family) full draft. The longest section. Each theorem gets its honesty discussion in a paragraph; the no-lift theorem gets the most ink. The Loop-Capture mapping note is the only spot where institutional reading appears, fenced.
4. ⏳ §4 (two witnesses) full draft. Attestation ledger gets ~2× the receipt model's space. The wound-is-authorized framing is the load-bearing observation.
5. ⏳ §5 (scope and non-claims) — write at any time; the fence list is stable.
6. ⏳ §1 (introduction) — write last. Hardest section to write before §3 is settled, because the introduction promises what §3 delivers.
7. ⏳ §6 (related work) — write after §3 settles. Knowing what we did and didn't prove is the precondition for honest positioning.
8. ⏳ §7 (discussion) + §8 (conclusion) — short; write after §6.
9. ⏳ Appendix A (module map) — generate from theorem-target table.
10. ⏳ Appendix B (build and reproducibility) — short.

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
- [ ] Not Calculus 2.0 (full label). Safety axis only; composition and self-amendment open.
- [ ] Not a process calculus; not refinement; not a complete safety policy; not certification.

The fence is checked in §5 explicitly; the introduction signposts it; §3 carries it on the Loop-Capture mapping note.

## What the preprint must NOT do

- Argue that real institutions exhibit the L/V divergence. That is paper 28.
- Introduce new Lean modules. The Lean source is finished; the preprint is exposition.
- Claim the "Calculus 2.0" label. The label is gated on composition + self-amendment axes, both open.
- Re-litigate the actor-inert vs actor-sensitive bridge decision. Ratify by stating it; defer the actor-sensitive extension as named-but-not-implemented.
- Cite the Δt corpus as load-bearing evidence. Δt-series references are background motivation only.

## What forces a re-scaffold

If any of the following changes between now and first draft, redo this scaffold:

- A new theorem lands in `SafetyTrajectory.lean` or `AttestationLedger.lean` (e.g. the trajectory-global → per-hop actor refactor at the generic layer). Probably triggers an §4 expansion.
- A tier-2 model (budget-margin or quorum) lands. Triggers a "tier-2 preview" subsection in §3 or §7.
- Paper 28 starts drafting. May reshape §1 framing — though Fork B explicitly says the preprint goes first, so this should not be a forcing event.

## Venue and sequencing

Spine page (`working/calculus-paper-spine-2026-05-28.md`) says: write the preprint first, paper 28 second. The preprint does not need to be *published* before paper 28 drafts begin, but it does need a citable scaffold (this) before paper 28 can forward-point.

Target venue: arXiv cs.LO at minimum. AI-safety venue (e.g. AI Safety Workshop, ICML SafeML, NeurIPS Safety) possible if framing supports. Decide after first draft; do not pre-format for a specific venue at scaffold stage.

## Identifier drift

Theorem names in this scaffold are verified against `~/git/lean/LeanProofs/Admissibility/` as of 2026-05-29. The crosswalk automation (`tools/formalization_crosswalk.py`) should be run again before any draft revision touches the theorem-target table.

## Open question for v0.1 → v1.0 draft

The Loop-Capture mapping in §3 — how much should the preprint say about it? Two postures:

- **Minimal:** name the doctrinal mapping in one sentence as a downstream reading the no-lift makes available; fence it; move on.
- **Light gloss:** spend a paragraph on the mapping shape (legitimacy holds along the whole trajectory, value falls, no retrofit lift) explicitly framed as *a reading paper 28 will develop, not a claim of this paper*.

Lean toward minimal. The preprint's job is the formal kernel; the gloss invites the wrong kind of reviewer attention. Confirm at first-draft pass.
