# Shared Vision as Coordinating Prior: Aggregation-Layer Masking and the Witness-Filter Pathology

**Author:** James Beck
**Status:** Preprint v0.1 (initial draft, 2026-04-22). Not yet pushed to Zenodo.
**DOI:** Not yet assigned.

## Abstract

Shared visions, strategic priors, and operating theses coordinate multi-agent systems by reducing policy divergence around a common token. We identify three structural failure modes by which such coordination produces persistently wrong steady states even when the system has working feedback, solicits dissent, and updates on reported error. First, any first-moment aggregator (mean, balanced weighted mean, rank-symmetric median) maps balanced bias-split witness populations to zero; the shared prior is therefore frozen by the arithmetic of the aggregation rule, not by any procedural refusal to update. Second, public alignment to a shared prior is alias-compatible with arbitrary internal compositional divergence under stationary conditions, with the divergence surfacing only under strategic shift. Third, witness inclusion correlated with prior-alignment defeats every aggregator — including shape-preserving receipt-lineage architectures — by removing signal upstream of aggregation; a single such filtering event produces persistent non-vanishing error with no internal mechanism for self-correction. The constructive consequence is that the only governance architecture satisfying both freeze-freedom and stability preserves per-witness receipts and maintains witness inclusion independent of prior-alignment.

## Formalization Status

The §3 result stack has multiple distinct strength classes — the ladder is deliberate, not an artifact of drafting:

| Result | Statement | Strength | Probe artifact |
|---|---|---|---|
| Theorem 1 (aggregation-layer masking) | **exact** (in expectation under (A1)–(A5)) | algebraic proof in §3.2 | aggregation-boundary probe row (MEAN, MEDIAN) §4.1 |
| Proposition 1 (no-scalar-free-lunch) | **probe-backed conjecture** | four-aggregator probe in §4.1 | full §4.1 table |
| Proposition 2 (alias-compatibility) | **exact in equal-gain regime; probe-backed beyond** | proof sketch in §3.4 | alias-compatibility probe §4.2 |
| Theorem 3 (witness-filter) | **exact** under (C1)–(C3) | algebraic proof in §3.5 | filter probe §4.3 |
| Theorem 4 (persistence) | **exact** under (D1)–(D4); fixed-point stable to internal dynamics | fixed-point proof in §3.6 | filter probe one-shot column §4.3 |

Two results are flagged as conjecture-strength rather than theorem-strength: Proposition 1 (no-scalar-free-lunch, where the scalar-aggregator class needs to be precisely fixed before the impossibility can be proved class-wide) and Proposition 2 (alias-compatibility, where the equal-gain case is exact but heterogeneous-gain and the precise post-shift functional form require a fully specified dynamical class). Promoting Proposition 1 to a theorem is flagged as the single highest-value item in §8.

## Key Contributions

1. **Three-layer structural account of coordinated-wrongness failure** — aggregation-layer masking, alias-compatibility, witness-filter pathology — jointly closing the "just use a better aggregator" and "just use better hiring" escape hatches by identifying the joint structural condition.
2. **Theorem 1** — Any first-moment aggregator freezes the shared prior under balanced bias-split witness populations, regardless of procedural gate. Dissent is arithmetically annihilated, not refused.
3. **Theorem 3** — Alignment-correlated witness inclusion defeats every aggregator, including shape-preserving receipt-lineage architectures. V-freeze is enforced upstream of aggregation.
4. **Theorem 4** — A single one-shot filtering event produces persistent non-vanishing error between the shared prior and reality, bounded below by the surviving population's residual bias. Self-correction requires exogenous witness reintroduction or exogenous prior perturbation.
5. **Constructive architectural corollary** — The only aggregation architecture satisfying both freeze-freedom and stability preserves per-witness receipts *and* maintains open witness inclusion. Either condition alone is insufficient.

## Files

| File | Description |
| --- | --- |
| `shared_vision_coordinating_prior.md` | Source markdown |
| `metadata.yaml` | Series metadata |
| `NOTES.md` | Changelog + open items + compression record |
| `README.md` | This file |

## Companion Artifacts

| Artifact | Location | Role |
| --- | --- | --- |
| Simulation | `../../../lean/shared_vision.py` | Scaffold for §4 probes (aggregation-boundary, alias-compatibility, filter) |
| Working note | `../../working/shared-vision-coordinating-prior.md` | Discovery-history archive; not part of the published artifact |

## Position in the Series

Multi-agent / organizational analogue of Paper 23's controller-layer observational-masking result. Paper 23 names the phenomenon at the controller layer with three-class strength typography (exact / first-order / ε-approximate); Paper 24 lifts the structure one scale up and supplies the specific aggregation-layer mechanism by which organizations fail to notice alias-compatibility even when they nominally have feedback loops.

The single-sentence braid (§7.6): **organizations mistake compressed public alignment for resolved internal composition.**

Paper 24 is not a prerequisite for Paper 23 and vice versa; the two papers cross-cite naturally.

## Status Notes

- v0.1 is a coherent first-pass draft, not yet whittled to DOI-ready shape. NOTES.md contains an explicit punch-list of next-pass branches (Proposition 1 theorem-ization, Theorem 2 Appendix A, probe-artifact reproducibility, Zenodo push).
- Per external review (chatty, 2026-04-22): preprint-close but DOI-not-yet. The compression pass has landed; the claim surface may tighten further once Proposition 1 is promoted and Paper 23 is formally in place.
- The scoping discipline in §5 is load-bearing: Agile/Scrum is presented as one worked example of a broader claim class, not as the target of the paper. The structural analysis is the contribution; the case study is illustrative.
