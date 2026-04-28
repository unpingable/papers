# Paper 25 — Working Notes

## Status

**v0.0-stub — 2026-04-28.** Scaffold only. Substantive content lives in `working/epistemic-border-control.md`. This directory exists to reserve the paper number and make the candidate visible alongside published siblings.

## Gate items

1. **Single-agent sim.** Done (2026-04-22). `~/git/lean/paper25_substitution.py`. Power-law phase transition observed (T_rms_asym / T_rms_clean = 333 at α_T/α_C=0.01 → 1.9 at α_T/α_C=10). Two substitution channels identified: (a) pure observability asymmetry; (b) filter Gaussian model ignorant of Poisson crank shocks. Paper 23 Gramian bridge operationalized (T-axis rotates into ker(O_T) as α_T→0; alignment 0.9999 → 0.044).
2. **Sibling-vs-§N adjudication.** Resolved 2026-04-22 by algebraic argument (homogeneous agents with shared C_obs yield O_T^stack = 1_N ⊗ O_T; kernel and observability subspace unchanged; aggregation reduces variance as O(σ²/N) but does not rotate the subspace). P25 is sibling to P24, not §N.
3. **Literature differential.** Pending. Targets: Perdomo, Pagan, Sprenger, Dwork.

## Position in the series

P22→P26 escalating negative results:

- P22: regulation can outrun what it regulates (no universal plant clock).
- P23: controller may not be self-identical (controller-layer masking).
- P24: witness population may be structurally wrong even with feedback (aggregation-layer masking).
- P25: target may be unsensed; substitution is forced.
- P26 (candidate): temporal seam may fail (premature/belated duality).

P24 §7.6 names the masking trilogy explicitly: P23 (identifiability masking) / P24 (observational aliasing) / P25 (substitution forcing).

## Working note pointer

Substantive content: `working/epistemic-border-control.md`.

Sim artifacts: `~/git/lean/paper25_substitution.py`, plus `paper25_*.png` in `~/git/lean/`.
