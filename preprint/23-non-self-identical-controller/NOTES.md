# Paper 23: Non-Self-Identical Controller — Working Notes

## Status

**v0.1 — 2026-04-21.** Frozen for cooling. Local source only; Zenodo push deferred until after cold reread. The artifact has crossed into "real object" territory: real spine, scoped claims, proof-shaped objects, Lean support where it counts, sim support where it helps, and enough fences that future-me shouldn't have to apologize for it. Further work on 23 is polish/hardening, not conceptual rescue.

**Next possible branches, in rough order of cost:**

1. **Grammar/prose polish pass on cold reread.** One-shot fixes caught so far and landed this session; more likely on a cold read.
2. **Adjacency spike promotion.** The four "differs from X because Y" paragraphs in §6 are strong enough to become a §1.2 "Position relative to adjacent literature" or a §7 related-work stub. ~200-300 words of prose promotion.
3. **Two TikZ figures.** (a) Augmented-state $\xi_t$ hybrid diagram with flows-inside-$C_\theta$ and jumps on handoff/authority/fracture. (b) Tie-line example timeline showing thermal clock, $\delta_h$ component breakdown, and $\tau_{\text{auth}}$ window. High visual ROI.
4. **Lean expansion to cases (ii) and (iii).** Natural next formalization targets. Case (ii) formalization needs a 2D plant and finite-horizon observability; case (iii) needs a parametric controller family with an $\varepsilon$-closeness bound.
5. **Zenodo push** after cold reread + any of the above. v0.1 or v0.2 depending on how much polish.

**Not in the scope of Paper 23:** ICU contrast case, real-data §4 hardening from PJM/ERCOT post-mortems, governance-witness family extraction (admissibility family paper), shared-vision coordinating-prior model (Paper 24 candidate — see `working/shared-vision-coordinating-prior.md`).

## Thesis (one sentence)

Operations is control in the regime where the controller is *non-self-identical* — partially reconstituted across handoffs, partially supplemented by latent undocumented compensation, and partially under-resolved by the system's own measurement-and-authority map — and the paper decomposes that failure into two orthogonal axes (continuity of action, continuity of identity) each with its own formal apparatus.

## The §3.3 strength ladder (worth preserving under hardening)

The Operational Masking Theorem states three sufficient masking conditions at three distinct levels of formal strength:

- **(i) projection masking — exact.** $\Pi(C+H) = \Pi(C)$ pointwise ⇒ outputs coincide exactly. Formalized in Lean as `projection_masking`; exhibited in the sim as bit-exact trajectory match under saturating authority.
- **(ii) measurement null-space masking — first-order over horizon $T$.** The observability matrix $O_T$ annihilates $B H_t$ ⇒ outputs coincide to first order over the full horizon. Upgraded from "first-order, local" on 2026-04-21; sim demonstrates the finite-horizon feature via a 2D plant where H-induced δy grows triangularly and is below noise floor for 4 steps.
- **(iii) local gain aliasing — up to resolution $\varepsilon$.** $C+H$ observationally within $\varepsilon$ (in $L^2(\Omega)$) of a parameter-shifted nominal controller. Definition in §3.1 made explicit 2026-04-21 (previously the case (iii) conclusion escaped its own definition).

The three-class typography is load-bearing. Future edits should not flatten the ladder into "three sufficient masking conditions" without the strength annotations — doing so loses the thing that makes the theorem honest.

## Changelog

### 2026-04-22

- **§6 swap: "Notes for next pass" → "Adjacency and distinction."** Removed workshop-residue §6 from the paper body per external review (chatty, 2026-04-22): the preprint should not ship with process-narration and "next-pass branches" in the shipped artifact. Replaced with a compact 5-paragraph §6 Adjacency and distinction that promotes the four adjacency buckets (switched/hybrid, viability, identifiability, human supervisory control) from their pre-lit-review "differs from X because Y" form into a compressed, defensive anti-misreading shield. Per chatty's rule of thumb: does each paragraph sharpen the reader's understanding of the paper's object, or prove I've seen adjacent discourse? Only the first kind kept.
- Lean-status detail (case (i) in `OpsMasking.lean`, deferred cases (ii) and (iii), signature note on $\text{proj}$ vs $\Pi_{A_t}$) moved here to NOTES; see "Lean status" section below.
- ICU contrast case and second-Case-A-example items were already in the Open/deferred section below; no change needed.

### 2026-04-21 (morning / afternoon)

- §1 operationalization paragraph added after the bolded thesis. Disowns the metaphysical reading of "non-self-identical" and pins the claim to controller-side identifiability. Independent flags from DeepSeek, chatty, and the Lean signature check converged on this as the highest-priority defensibility patch.
- §3.1 case-(iii) honesty patch. Added explicit ε-approximate masking case alongside deterministic and stochastic cases so the definition covers what §3.3 case (iii) actually achieves.
- §3.2 and §3.3 case-(ii) upgrade. Replaced pointwise first-order statement with finite-horizon first-order: $CA^k B H_t = 0$ for $k = 0, \ldots, T-1$, equivalent to $BH_t \in \ker O_T$. Closes the honesty gap without importing full weakly-unobservable subspace machinery.
- §2.4 $\delta_h$ decomposition. Split the effective reorientation delay into $\delta_{\text{serial}}(B) + \delta_{\text{reorient}}(\theta) + \delta_{\text{ambig}}(L)$. The continuity-budget inequality is now four-term and explicitly diagnostic: bandwidth tooling cannot substitute for fatigue or scene-ambiguity reduction. §4.3 and §4.5 cross-references updated.
- §6 updated with three breadcrumbs: Lean-done note, bounded adjacency spike (four-bucket "differs from X because Y"), coherent-checkpoint landing.
- Lean module `LeanProofs/OpsMasking.lean` created and verified building. Three theorems: `trajectory_eq_of_projected_eq` (general), `observations_eq_of_projected_eq` (corollary), `projection_masking` (paper form).
- Simulation `ops_continuity.py` created. Instantiates the augmented state, exhibits Case A governance-induced ruin in phase sweep, exhibits case (i) projection masking bit-exactly, exhibits case (ii) finite-horizon masking over a 4-step window.

### 2026-04-21 (evening — final polish pass)

- Abstract grammar fix: "Operations begins" → "Operations begin".
- §2.1 opener on handoff modeling tightened: the "first-pass simplification" sentence now names the omissive/noisy contrast up front rather than burying it.
- §3.3 case (ii) theorem statement gains a parenthetical clarifying the equivalent finite-horizon observability-matrix form ($O_T = [C; CA; \ldots; CA^{T-1}]$), matching the terminology used in the proof sketch so a reader doesn't have to bridge it themselves.
- PDF rebuilt.

## Lean status

Projection-masking case (i) is formalized in `LeanProofs/OpsMasking.lean` as `projection_masking`, built on a more general lemma `trajectory_eq_of_projected_eq`: under any plant dynamics $f$ and measurement map $h$, two controllers whose *gated* actions agree pointwise produce identical plant trajectories and observations from any initial state. The paper-form corollary takes actions in an additive type and asserts $\Pi(C+H) = \Pi(C)$ pointwise ⇒ outputs coincide exactly. Deterministic case only. Cases (ii) (measurement null-space, first-order) and (iii) (local gain aliasing, $\varepsilon$-resolution) remain paper-level and are not yet Leaned.

One signature note for future Lean work: in the current formalization the gate is a fixed function $\text{proj} : U \to U$ rather than the paper's authority-state-indexed $\Pi_{A_t}$; for case (i) this is harmless (the masking hypothesis is already pointwise and absorbs any gate-state dependence), but lifting to $\text{proj} : X \to U \to U$ is required if a future module wants to carry $A_t$ explicitly — e.g., to formalize the §2 continuity-budget inequality, where authority delay is the load-bearing object. The §2 ADT bound itself remains imported scaffolding and is intentionally not Leaned.

## Predicted governance family

The admissibility family's spatial receipts (authorization, provenance) predict a temporal-axis sibling: handoff receipts, authority-routing receipts, operator-state receipts, continuity witnesses. This is a structural prediction, worth pulling into the family paper when it gets written — not a scope expansion for Paper 23.

## Open / deferred

- **Full weakly-unobservable subspace version of case (ii).** The current finite-horizon first-order statement is honest and demonstrable; a fully nonlinear global version requires the Isidori construction and is deferred.
- **Case (iii) sim demo.** Aliasing case is in the prose and has an $L^2$ bound, but the sim does not yet exhibit it. Would require a parametric controller family and a second controller differing by $\Delta\theta$ with actions matching $C+H$ within ε — doable, not a gap.
- **Real-data hardening of §4.** The worked example is explicitly *illustrative, not diagnostic*. Post-mortem data from published grid incidents (PJM, ERCOT) would let the continuity-budget inequality be applied as a real post-hoc diagnostic instead of a composed scenario.
- **Governance-witness family extraction.** §6 flags the predicted admissibility-family sibling — handoff receipts, authority-routing receipts, operator-state receipts, continuity witnesses. Future paper, not this one.
- **ICU / medical handover contrast case.** Makes the identity-continuity axis viscerally obvious. Deferred as "framework generalizes" material for a companion paper; ethical static would swallow the formal object on first pass.
- **Second example of §4.5 Case A.** Published grid timelines with explicit τ_auth and T_exit numbers would convert the inequality from hypothetical to post-hoc diagnostic.

## Parallel track

Paper 24 ("Shared Vision as Coordinating Prior") was promoted from working-note seed to preprint artifact on 2026-04-22; see `preprint/24-shared-vision-coordinating-prior/`. The structural connection to Paper 23 is explicit: Paper 23's §3 Operational Masking Theorem names alias-compatibility at the controller-composition layer; Paper 24 lifts the same structural move to the multi-agent / organizational layer and supplies the specific aggregation-layer mechanism by which organizations fail to notice the alias-compatibility even when they nominally have feedback loops. The single-sentence braid (Paper 24 §7.6): *organizations mistake compressed public alignment for resolved internal composition.* The two papers cross-cite naturally; neither is a prerequisite for the other.
