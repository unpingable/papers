# Paper 18: Unauthorized Durability

**A Composable Governance Primitive for State Promotion in Adaptive Systems**

James Beck, Independent Researcher — March 2026

**DOI:** [10.5281/zenodo.18940008](https://doi.org/10.5281/zenodo.18940008)

## Abstract

Adaptive systems that accept inputs at multiple timescales face a structural governance problem: transient signals can silently acquire durable governing force. The failure mode is not influence per se but *unauthorized durability* — the promotion of lower-tier state into higher-tier authority without legitimate write paths. This paper formalizes the problem as a multiscale control model with four state classes mapped to four authority tiers, derives six invariants and five write barriers, and introduces the *promotion ceremony* — a composable governance primitive for controlling when lower-tier state may acquire higher-tier legitimacy. The same protocol governs runtime-to-policy promotion and policy-to-constitutional updates, yielding no exempt layer where real authority hides unaudited.

## Formalization Status

`PersistenceModel.lean` in `~/git/lean/LeanProofs/` is the formalization of this paper's central mechanism. Cashout classes: **sharpen** + **bridge artifact**. Paper-ready.

Formalized claims that sharpen or extend the prose:

- Detached commits (not idle time) burn rollback capacity — cumulative commitment, not "long enough" duration
- Episode recoverability ≠ lifetime recoverability — individually-recoverable episodes can accumulate into irrecoverability
- Hysteretic is absorbing for internal events (machine-verified lock-in)
- External repair produces **restructured**, not aligned — operability without original resilience (novel relative to prose)
- Restructured systems can fail again, faster (novel relative to prose)
- Three-way recovery taxonomy: internally recoverable / externally repairable / locked in

Revision candidacy: **v1.1 with formalization appendix**, possibly **v1.2** if the reframing ripples into the abstract or key contributions. See [`docs/formalization-index.md`](../../docs/formalization-index.md) for the full crosswalk.

## Key Contributions

- Four-tier authority model (L0 runtime, L1 context, L2 durable policy, L3 constitutional) with coupled state dynamics exhibiting timescale separation
- Six invariants and five write barriers constraining unauthorized state promotion
- The promotion ceremony as a composable, scale-invariant governance primitive (proposal, evaluation, attestation, application, audit)
- Recursive governance: the same ceremony governs the system's own doctrine updates
- Seven-class threat taxonomy including ontological spoofing and observer capture
- Worked attack path: prompt injection through context recurrence to attempted durable promotion

## Files

| File | Description |
|------|-------------|
| `unauthorized_durability.md` | Paper source (Markdown) |
| `unauthorized_durability.pdf` | Compiled PDF |
| `metadata.yaml` | Paper metadata |
| `NOTES.md` | Working notes, review feedback, and design context |
| `paper.md` | Raw multi-model conversation that generated the idea |
| `figures/tier_model.tex` | TikZ source for Figure 1 |
| `figures/tier_model.png` | Figure 1 as PNG |
| `figures/tier_model.pdf` | Figure 1 as PDF |

## Build

```bash
pandoc unauthorized_durability.md -o unauthorized_durability.pdf \
  --pdf-engine=xelatex \
  -V mainfont="Libertinus Serif" \
  -V mathfont="Libertinus Math" \
  -V monofont="Libertinus Mono" \
  -V geometry:margin=1in \
  --toc -V colorlinks=true
```

## Related Papers

- **Paper 12** — Bounded Lattice Inference: governor architecture, typed receipts, NLAI ([doi:10.5281/zenodo.18145346](https://doi.org/10.5281/zenodo.18145346))
- **Paper 15** — Cybernetic Fault Domains: commitment boundaries ([doi:10.5281/zenodo.18686130](https://doi.org/10.5281/zenodo.18686130))
- **Paper 16** — The Gain Geometry of Temporal Mismatch: shear, leverage, capture ([doi:10.5281/zenodo.18717619](https://doi.org/10.5281/zenodo.18717619))
- **Paper 17** — Receipt the Compiler: propaganda as hidden epistemic policy ([doi:10.5281/zenodo.18841815](https://doi.org/10.5281/zenodo.18841815))
