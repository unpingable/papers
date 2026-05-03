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

## Series-spine connections and deferred targets

Items below were scavenged from the superseded working note (archived 2026-05-03 at `archive/epistemic-border-control.working-superseded-2026-05-03.md`). Status: **preserved for future review, not promoted into the draft.** Promotion into preprint body, references, or §8 expansion is a separate decision, deliberate, preferably after P27 stabilizes.

### Latent Capitalism substrate connection

The data-center example is Latent-Capitalism-adjacent: opaque procurement, captured tax abatements, infrastructure burden shifted onto public commons. The substitution mechanism names a specific *defense* by which enclosure resists scrutiny — make the scrutiny itself reputationally contaminated, so the regulator switches from regulating enclosure to regulating the discourse about enclosure. The rhetoric of "truth-tracking" continues; the controlled variable is now reputational contamination.

Shorthand: **contamination-as-enclosure-defense.** Not promoted into §7 — adding it there risks making the data-center example the paper's emotional center, which `CANDIDATES.md` already flags as a scope risk. Belongs as a series-spine / Latent Capitalism bridge for future writing.

### §8 edit pin — receipt-lineage as architectural enforcement

The working note articulated the architectural escape sharper than §8 currently does:

> Admissibility gates as refusing to collapse $T_t$ and $R_t$ into a single $Y_t$ — keeping separate accounting for object-level claim quality, reputational risk, institutional opacity, and contamination state. Receipt-lineage as the architectural enforcement that these states cannot be silently unified.

§8's third bullet ("Witness-cohort heterogeneity") and the closing paragraph touch the idea but do not name *receipt-lineage as the architectural enforcement* — the bridge to Governor's mechanical layer. Folding into §8 is content promotion (imports Governor machinery into P25); deferred until after P27 stabilizes its receipt-durability vocabulary.

### Deferred literature targets (beyond v0.1 references)

Beyond Perdomo / Pagan / Sprenger / Dwork / Manheim-Garrabrant cited in §6, future drafts should also survey:

- Epistemic network effects
- Social epistemology of moderation
- Goodhart variants beyond Manheim-Garrabrant 2018
- Credibility-weighting schemes
- Misinformation-diffusion models

Chatty's first-pass spike found the four primary citations; the broader review is deferred work, not gating v0.1.

### ICU contrast case (sibling instantiation candidate)

Paper 23's deferred ICU case may apply here too — a domain where target-substitution is especially stark and ethical stakes are high. Status: possible sibling instantiation, not planned §7 expansion. High-stakes examples have gravity wells.
