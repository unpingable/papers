# Safety-Bridge Kernel: Authorization and Value Preservation

*Axis 1 of the Admissibility Suite.*

**Author:** James Beck
**Affiliation:** Independent Researcher
**Status:** v0.2 axis-1 draft (2026-05-29 scaffold; 2026-05-30 canonicalization refresh; 2026-05-31 body prose for §1–§8 and appendices A/B; 2026-05-31 suite reframe + characterization layer in Lean). **Not yet published.** Title, abstract, claim list, theorem-target table stable; suite-context paragraph below reflects the 2026-06-03 cross-axis synthesis closure (see `working/source-basis-discipline-synthesis.md`). **Drafted:** §1 introduction, §2 formal apparatus, §3 trajectory separation result (sections 3.1–3.8), §4 two separating instances (4.1 receipt-poison, 4.2 Nat-valued attestation ledger), §5 scope and non-claims, §6 related work, §7 discussion, §8 conclusion, Appendix A module map, Appendix B build and reproducibility. **Deferred:** References section — bibliography locks at release. Body prose for §3/§4/§7/§8 still uses pre-characterization framing; the new characterization layer (`AuthPreserves`, `AuthorizationBridgeGap`, `MaximalBridge`, `BridgeComplete`, `HasForgetfulSection` + their theorems) lives in `SafetyBridge.lean` and is not yet exposed in the paper body — pending a §3 expansion or §3.9 subsection.
**Suite context:** This artifact is **Axis 1** of the admissibility suite (see `working/admissibility-suite-map.md`). Axis 2 (composition / merge admissibility) and Axis 3 (self-amendment / frontier mutation) remain open. A 2026-06-03 cross-axis synthesis pass closed *against* a single unifying "Admissibility Calculus" paper: what survives the synthesis is the **disciplined premise production** umbrella with two named species (source/temporal — this axis; multiplicity/resource — the ContractionHinge sibling) plus a per-species architecture-gap audit, not a unifying formal system (see `working/source-basis-discipline-synthesis.md`).
**Target venue:** Zenodo / arXiv-quality formal note; cited by Δt paper 28 ("The Lie Is Cheaper Than the Proof") as the formal substrate. No conference submission planned.
**Series:** Outside the Δt Zenodo numbering. Member of the admissibility suite; sibling artifact to Δt paper 28.

## Center of gravity

A small Lean 4 admissibility kernel that separates authorization from value-preservation evidence and proves, in three theorems plus a forgetful map, that the separation composes across trajectories. Authorization is a declaration; preservation must be witnessed by a separate bridge.

The keeper line from the Lean repo:

> *Authorization is a declaration (`= rfl`); preservation must be witnessed (`preserves` discharge).*

The preprint's contribution is the type-level cost asymmetry. The institutional reading of that cost asymmetry — that systems where unchecked assertion is cheaper than verified assertion tend toward authorization laundering — is the subject of the sibling paper, not this one.

## Position relative to the Δt series

This preprint is **not** numbered in the Δt series. Per the topology decision in `working/admissibility-suite-spine-2026-05-28.md`:

```
{ Safety-Bridge Kernel preprint }
    formal-methods venue (Zenodo / arXiv-quality formal note)
    contribution: kernel + theorem family
              |
              | cited as the formal kernel by
              ↓
{ Paper 28 (Δt series) }
    Zenodo Δt series, extends 27
    slug: "The Lie Is Cheaper Than the Proof"
    contribution: discharges the antecedent the kernel
    is structurally forbidden from asserting
```

(Working-title drift note: the diagram and the citation block below used the earlier slug *"An Admissibility Calculus: Authorization, Safety Bridges, and Value Decay"*; that slug was demoted during drafting. The current title is *Safety-Bridge Kernel: Authorization and Value Preservation* — see the post-2026-06-03 synthesis closure for why "calculus" is no longer the framing.)

The two papers are siblings, not sequential. The preprint proves a *conditional* (IF a system has this shape, THEN authorized trajectories diverge from defended value) with explicit institutional fences. Paper 28 argues the antecedent holds in real institutional substrates, with the Δt 2 / 3 / 25–27 corpus as case-law evidence. Merging the two would crash two contributions into one trench coat; numbering this preprint as a Δt paper would bury it among critical-theory essays.

The punchy slug ("The Lie Is Cheaper Than the Proof") deliberately lives on paper 28, where rhetoric is contribution; on the formal preprint, the same rhetoric would read as op-ed cadence to a cs.LO reviewer.

## Source of truth

The Lean repository at `~/git/lean` (public: <https://github.com/unpingable/lean>) is the canonical formal source. This preprint is exposition of finished work, not new construction. Identifier-drift between this preprint and the Lean source is checked by `tools/formalization_crosswalk.py`.

The eight safety-bridge family modules cited throughout:

| Module | Role |
|---|---|
| `LeanProofs/Admissibility/AuthorizedNotSafe.lean` | Single-step wound (StepAllowed layer, axiomatic) |
| `LeanProofs/Admissibility/AuthorizedNotSafeWitness.lean` | Wound consistency discharge (concrete miniature) |
| `LeanProofs/Admissibility/SafetyBridge.lean` | Abstract `SafetyEnv` primitive + per-hop-actor `AuthStep` / `SafeStep` gates + generic per-hop-actor `AuthorizedTraj E` / `BridgedTraj E` + generic `bridgedTraj_preserves` |
| `LeanProofs/Admissibility/SafetyBridgeWitness.lean` | Non-contamination bridge specimen |
| `LeanProofs/Admissibility/AuthorizedStepNotSafe.lean` | Verdict-layer wound transfer (brick 1a) |
| `LeanProofs/Admissibility/AuthorizedStepNotSafeWitness.lean` | Verdict-layer wound discharge + canonical `SafeAuthorizedStepC` gate (brick 1b); actor as field |
| `LeanProofs/Admissibility/SafetyTrajectory.lean` | Verdict-layer trajectory specialization: `AuthorizedTrajC` / `BridgedTrajC` + forgetful map + the brick-2 triple (`bridgedTrajC_preserves`, `authorized_trajectory_loses_value`, `no_bridgedTrajC_to_poison_end`) |
| `LeanProofs/Admissibility/AttestationLedger.lean` | Second concrete witness (tier-1, two-actor, Nat-valued); consumes the generic substrate directly (no bespoke trajectory types) |

## Files

| File | Description |
|---|---|
| `paper.md` | Main paper scaffold (sections, claim list, theorem-target table, scope fences). **Pre-draft.** |
| `metadata.yaml` | Metadata: title, series classification (non-Δt), abstract, keywords. |
| `NOTES.md` | Drafting plan, sequencing notes, lit-differential sketch. |
| `README.md` | This file. |

## Provenance

- Spine decision: `working/admissibility-suite-spine-2026-05-28.md` (Fork B; preprint sibling to paper 28).
- Tier map: `working/tooltheory/calculus-2-tier-map-2026-05-28.md`.
- ρ-drop decision: `working/tooltheory/safety-bridge-rho-drop-decision-2026-05-28.md`.
- Exit-criteria reconciliation: `working/calculus-2-exit-criteria.md` §Track split (closed 2026-05-29).
- Kernel-overlap audit: `working/tooltheory/safety-bridge-kernel-overlap-audit-2026-05-29.md` (closed 2026-05-29).

Both safety-axis minting gates closed before scaffold drafting began.

## Scope discipline

The preprint inherits the kernel's institutional fence — *"kernel-legible all-green verdict, NOT substantively-grounded legitimacy."* That fence is what makes the preprint honest as formal methods and what makes paper 28 non-derivative work. Separating these is the load-bearing decision; do not relitigate it in the preprint's prose.

## Citation (post-publication, placeholder)

```bibtex
@article{beck2026safetybridge,
  author = {Beck, James},
  title = {Safety-Bridge Kernel: Authorization and Value Preservation},
  year = {2026},
  doi = {[TBD]},
  url = {[TBD]}
}
```

## Related preprints

- **Δt paper 28** (forthcoming): "The Lie Is Cheaper Than the Proof" — interpretive sibling. Discharges the antecedent the formal kernel is structurally forbidden from asserting.
- **Δt P22** (*No Universal Plant Clock*): the series keystone. Cited here only as background motivation for the L/V divergence framing, not as a load-bearing dependency.
- **Δt P25** (*Epistemic Border Control*): companion negative-result paper; the projection-α framing in P25 §3.1 is the closest doctrinal sibling to the forgetful map here.
- **Δt P27** (*Obligation-Unsound Reconciliation*): the obligation-accounting layer that sits downstream of this kernel's verdict gate.

## Keywords

admissibility, authorization, safety bridge, value preservation, Lean 4, formal methods, kernel-legible verdict, trajectory triple, bridged trajectory, no-lift theorem, actor-inert bridge, attestation ledger, structural countermodel, L_t/V_t divergence
