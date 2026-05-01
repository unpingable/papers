# Ops Is Control with a Non-Self-Identical Controller

**Author:** James Beck
**Status:** Preprint v1.0 (published on Zenodo 2026-04-24).
**DOI:** [`10.5281/zenodo.19055415`](https://doi.org/10.5281/zenodo.19055415) (concept) — record: <https://zenodo.org/records/19715302>

## Abstract

We study two distinct failure modes of controller continuity in operational systems. **Continuity of action** concerns whether the controller can still intervene in time: handoff distortion, authority-routing delay, and fatigue-induced contraction loss jointly consume a viability budget that can be stated as a single inequality. **Continuity of identity** fails when the controller's real composition differs from the nominal controller in ways the measurement-and-authority map cannot resolve: under three sufficient masking conditions, latent human compensation becomes structurally unidentifiable from observed outputs. Classical control assumes the controller is self-identical across time. Operations begins where that assumption breaks.

## Formalization Status

§3.3's Operational Masking Theorem has three distinct strength classes — the ladder is deliberate, not an artifact of drafting:

| Case | Statement | Formal artifact | Sim artifact |
|---|---|---|---|
| (i) projection | **exact** | Lean (`LeanProofs/OpsMasking.lean`) | bit-exact trajectory match (`demo_projection_masking`) |
| (ii) null-space | **first-order over horizon $T$** | prose + observability matrix $O_T$ | 4-step masked window, then detectable (`demo_nullspace_masking`) |
| (iii) aliasing | **up to resolution $\varepsilon$** | prose + $L^2$ bound | (not yet exhibited) |

The Lean module provides the general lemma `trajectory_eq_of_projected_eq` (two controllers with pointwise-equal projected actions produce identical trajectories under any plant dynamics and measurement map) and the paper-form corollary `projection_masking`. Cashout class: **bridge artifact**. Cases (ii) and (iii) are paper-level only; the full weakly-unobservable subspace construction for a nonlinear global (ii) is flagged as deferred (Isidori Ch. 6).

## Key Contributions

1. Decomposition of operational controller-continuity failure into two orthogonal axes — *continuity of action* (§2: viability under handoff reset, authority delay, fatigue) and *continuity of identity* (§3: identifiability of the realized controller composition under the primary measurement-and-authority map).
2. **Continuity-budget inequality** $\tau_{\text{auth}} + \delta_{\text{serial}}(B) + \delta_{\text{reorient}}(\theta) + \delta_{\text{ambig}}(L) < T_{\text{exit}}$ (§2.4) — four non-substitutable knobs governing whether rescue is reachable. The $\delta_h$ decomposition makes the inequality diagnostic: improving handoff bandwidth shrinks only $\delta_{\text{serial}}$ and cannot substitute for fixing fatigue or reducing scene ambiguity.
3. **Institutional Ruin Condition** (§2.2) — separating technical ruin from governance-induced ruin via a delayed set-valued reachability statement.
4. **Operational Masking Theorem** (§3.3) — three sufficient conditions (projection, measurement null-space, gain aliasing) under which latent human compensation is structurally unidentifiable from outputs observed under the primary measurement-and-authority map.

## Files

| File | Description |
| --- | --- |
| `non_self_identical_controller.md` | Source markdown |
| `non_self_identical_controller.pdf` | Built PDF (cold-reading copy) |
| `metadata.yaml` | Series metadata |
| `NOTES.md` | Changelog + open items |
| `README.md` | This file |

## Companion Artifacts

| Artifact | Location | Role |
| --- | --- | --- |
| Lean kernel | `../../../lean/LeanProofs/OpsMasking.lean` | Case (i) projection masking, exact |
| Simulation | `../../../lean/ops_continuity.py` | Pressure chamber for §2 continuity budget, §3.3 cases (i) and (ii) |

The simulation instantiates the augmented state $\xi_t = (x_t, \hat x_t, c_t, \theta_t, A_t)$ with structured (biased/omissive) handoff loss, authority expansion after $\tau_{\text{auth}}$ delay, fatigue wear and fracture, and toggleable latent compensator $H_t$. A finer-grid phase sweep exhibits the §4.5 Case A distinction — ruin is governance-induced when $\tau_{\text{auth}}$ exceeds a threshold, flat across handoff bandwidth values within the tested range.

## Position in the Series

Dynamical hinge between Paper 21 (observer integrity under procedural sociality) and Paper 22 (no universal plant clock). §3 extends Paper 21's static observer-integrity result to controller composition; §2 operationalizes Paper 22's actuation layer with institutional authority explicitly in the loop. See §5 for the full positioning argument.

## Status Notes

- v1.0 published to Zenodo 2026-04-24. §6 carries a punch-list of next-pass branches (related-work expansion, real-data §4 hardening, governance-witness family extraction) — candidates for a future v1.x rather than v1.0 blockers.
- The §1 operationalization paragraph following the bolded thesis is load-bearing: it disowns the metaphysical reading of "non-self-identical" and pins the math to controller-side identifiability. Independent flags from DeepSeek, chatty, and the Lean signature check converged on this as the single highest-priority defensibility patch.
