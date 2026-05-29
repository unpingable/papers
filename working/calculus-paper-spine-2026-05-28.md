# Calculus paper spine — Δt formal kernel + interpretation (2026-05-28)

**Status:** Decision record. Resolves the topology fork *"is paper 28 the calculus paper, or does paper 28 cite it"* in favor of the latter (Fork B). Filed at decision-record density; the live source of truth for the formal kernel is `~/git/lean/LeanProofs/Admissibility/` (safety-bridge family).

**Provenance:** Multi-model conversation 2026-05-28 (Claude Code main thread, Claude opus 4.8 on web, ChatGPT-conservative). The fork emerged after the safety-bridge family landed (bricks 0 / 1a / 1b / 2 + tier-1 ledger) and the question *"what does this mean for the paper sequence"* surfaced. All three voices converged on Fork B with specific corrections; this file bakes those in.

---

## Topology

```
{ "An Admissibility Calculus" preprint }
    formal-methods venue (arXiv cs.LO at minimum)
    sober title, NOT in Δt Zenodo numbering
    contribution: kernel + theorem family
              |
              | cited as the formal kernel by
              ↓
{ Paper 28 }
    Zenodo Δt series (extends 27)
    slug: "The Lie Is Cheaper Than the Proof"
    contribution: discharges the antecedent the kernel
    is structurally forbidden from asserting
              |
              | reads 2 / 3 / 25–27 as
              ↓
{ Δt corpus 2 / 3 and 25–27 as case-law evidence }
```

The two papers are **siblings, not sequential**. The preprint is in a different genre (formal-methods) with a different audience and venue. Numbering the preprint as Δt-N would bury it among critical-theory essays; merging the preprint into paper 28 would crash two contributions into one trench coat.

## What each paper is (and is not)

### Preprint — "An Admissibility Calculus: Authorization, Safety Bridges, and Value Decay"

*Sober working slug. Passes the formal-methods-reviewer test without reading as op-ed.*

**Contribution.** A small Lean-formalized admissibility kernel separating authorization (`Allowed`) from value-preservation evidence (`bridge` + `preserves` obligation), with the safety-axis trajectory triple (positive composition, negative composition, no-lift), the forgetful map turning "an authorized trajectory that does not lift to a bridged one" into a *definition*, and a second concrete witness over a textured `Nat`-valued multi-actor model. Type-level cost asymmetry: declaration (`= rfl`) is cheap; demonstration (`preserves` discharge) is the obligation.

**Thesis (working).** A system in which false / invalid claims are cheaper to emit than valid claims are to verify will tend toward authorization laundering unless proof obligations, witness standing, and admissibility gates are made structurally cheaper than unchecked assertion.

**Genre.** Formal methods. arXiv cs.LO at minimum; AI-safety venue possible if the framing supports it. **NOT in the Δt series numbering.**

**Source of truth.** `~/git/lean/LeanProofs/Admissibility/` safety-bridge family (`AuthorizedNotSafe(Witness)`, `SafetyBridge(Witness)`, `AuthorizedStepNotSafe(Witness)`, `SafetyTrajectory`, `AttestationLedger`). The preprint is exposition of finished work, not new construction.

**Earns preprint status by:** one irreducible theorem family — the trajectory triple + no-lift, replicated across two distinct witnesses (receipt-poison miniature + attestation-ledger). Not vibes, not "formal flavor." The bar is met.

**Is not:** institutional commentary, Δt synthesis, retrospective. The fence inside the kernel — *"kernel-legible all-green, NOT substantively-grounded legitimacy"* — is also the fence on this paper. The institutional argument lives in paper 28.

### Paper 28 — "The Lie Is Cheaper Than the Proof"

**Contribution.** Discharges the antecedent the formal kernel is *structurally forbidden from asserting*. The Lean stack proves a conditional — IF a system has this shape, THEN authorized trajectories diverge from defended value — with explicit institutional fences (degenerate model; not substantively grounded). Paper 28 argues the antecedent holds in the wild, with the 2 / 3 / 25–27 corpus as the witness collection for "institutions exhibit admissibility-control failure."

**Thesis (working).** The Δt failures described in Papers 25–27 are not merely temporal coordination failures. They are admissibility-control failures: systems preserve locally valid outputs after the authority conditions that made them actionable have decayed. Time does not merely delay control; it changes what may still count as control.

**Genre.** Critical theory / cybernetics. Zenodo Δt series numbering, extends paper 27.

**Why this is not a meta-essay.** The formal layer is *prohibited* from containing this argument — the kernel's soundness depends on the institutional fence. Without paper 28, the Δt-as-instantiation reading is operator-asserted rather than published. Naming the antecedent and arguing it holds in the corpus is non-derivative work, even though it cites both the formal kernel and the prior Δt papers. It is the soundness argument for the *reading*, not a wrapper.

**Is not:** a retrospective of the corpus; a tasteful summary; a manifesto without thesis; "here is my corpus, behold its wallpaper." Paper 28 has (a) a hard thesis (the antecedent claim) and (b) an evidence section (the 2 / 3 / 25–27 corpus as case-law witness collection). Without that structure it drifts into meta-essay; with it, the genre is structured-interpretation.

## Slug placement decision

The punchy slug ("The Lie Is Cheaper Than the Proof") goes on **paper 28**, not the preprint, because:

- The preprint proves the *type-level* cost asymmetry (`rfl` vs `preserves` obligation) and wants a title that reads as formal-methods exposition.
- The slug earns its resonance from the *economic / institutional* reading of the cost asymmetry — declaration cheap, demonstration dear, as a fact about how institutions behave. That is paper 28's contribution, not the preprint's.
- On the interpretive paper, rhetoric is *contribution*; on the formal preprint, the same rhetoric would read as op-ed cadence to a cs.LO reviewer.

## Sequencing decision

**Write the preprint first.**

Reasons:
- **Bounded.** Proofs exist; the work is exposition of finished material. Known quantity of effort.
- **Anchors paper 28.** Paper 28 is open-ended synthesis of 27 papers; against a *finished, citable* reference it is materially easier to write than against vapor.
- **No paper-laundering-via-citation.** Paper 28 cannot cite a ghost. The preprint must have a stable scaffold (title, abstract, claim list, formal objects, theorem targets, repo pointer) before paper 28's prose can forward-point.
- **Ship the done thing.** Lower-risk artifact lands while the synthesis takes its time.

The preprint does not need to be *published* before paper 28 drafts begin — but it does need a citable scaffold. arXiv timestamping is the natural floor.

## Guardrails (against known failure modes)

1. **Preprint earns its slot with an irreducible theorem family.** Already met. Hold the bar; do not let "formal flavor" replace the trajectory triple + no-lift as the load-bearing content.
2. **Paper 28 carries a hard thesis, not "behold the corpus."** The antecedent-discharge framing is what prevents drift into meta-essay. The corpus is the evidence section, not the contribution. If the draft of 28 starts looking like a literature review, the framing has slipped.
3. **Do not pull adjacent spines into this map.** Ops materialism (values-in-implementation-order, workstation sovereignty, compute-dependency) is a *separate* spine. Latent capitalism is a third. The Δt / admissibility spine is load-bearing *right now* specifically because it grew a formal kernel; the other spines stay adjacent until something forces them together. The temptation here is theory-of-everything; the discipline is one keystone at a time.
4. **No paper-laundering-via-citation.** Paper 28 cannot cite "preprint in preparation." Either the preprint has a citable scaffold by the time 28 cites it, or 28 waits.
5. **Fence discipline is not optional.** The kernel's institutional fence ("not substantively-grounded legitimacy") is what makes the preprint sound; paper 28's antecedent argument is what makes the fence non-defeatist. Drop the fence in the preprint and the kernel makes claims it cannot support. Drop the antecedent argument in 28 and the reading becomes operator-asserted. Both need to hold.

## What this map does NOT decide

- **Paper 28's exact venue / publication cadence.** Depends on the Zenodo Δt series rhythm and the preprint's arXiv timing.
- **Whether the preprint becomes a journal submission later.** First-pass is arXiv timestamping; journal trajectory is a separate decision after community contact.
- **Tier-2A / tier-2B specimens** (budget-margin / quorum). Filed at `working/tooltheory/calculus-2-tier-map-2026-05-28.md`; this spine does not gate on either, and neither is needed for the preprint to ship.
- **The Chronopolitics book** relative to either paper. The book sits at a higher integration tier than this spine resolves; the relationship is "book cites paper 28 cites preprint cites kernel" but the book's structure is not decided here.
- **Forks A or C.** A (paper 28 = the calculus paper, single artifact) is rejected; the genre mismatch is the deciding fact. C (technical-report-only, no preprint) is rejected because the kernel already has theorem-shaped content sufficient for preprint status — C is only the right call if the bridge does not yet earn the slot, and it does.

## Related records

- Tier map (2A / 2B sibling stressors): `working/tooltheory/calculus-2-tier-map-2026-05-28.md`
- ρ-drop decision (actor-inert base bridge): `working/tooltheory/safety-bridge-rho-drop-decision-2026-05-28.md`
- Live Lean source: `~/git/lean/LeanProofs/Admissibility/` (safety-bridge family)
- Frontier 1 status update: `~/git/lean/FRONTIERS.md` (status: structurally addressed 2026-05-28)
- Calculus 2.0 exit criteria: `working/calculus-2-exit-criteria.md` (predates this decision; still to be reconciled against the spine)
- Kernel-to-body map: `working/kernel-to-body-map.md` (Slice A — safety bridge — now built)
- PAPER-MAP anchor: `~/git/lean/PAPER-MAP.md` (safety-bridge family entry pending; natural follow-on to this spine)
