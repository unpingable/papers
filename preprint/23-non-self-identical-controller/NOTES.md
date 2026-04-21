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

## Open / deferred

- **Full weakly-unobservable subspace version of case (ii).** The current finite-horizon first-order statement is honest and demonstrable; a fully nonlinear global version requires the Isidori construction and is deferred.
- **Case (iii) sim demo.** Aliasing case is in the prose and has an $L^2$ bound, but the sim does not yet exhibit it. Would require a parametric controller family and a second controller differing by $\Delta\theta$ with actions matching $C+H$ within ε — doable, not a gap.
- **Real-data hardening of §4.** The worked example is explicitly *illustrative, not diagnostic*. Post-mortem data from published grid incidents (PJM, ERCOT) would let the continuity-budget inequality be applied as a real post-hoc diagnostic instead of a composed scenario.
- **Governance-witness family extraction.** §6 flags the predicted admissibility-family sibling — handoff receipts, authority-routing receipts, operator-state receipts, continuity witnesses. Future paper, not this one.
- **ICU / medical handover contrast case.** Makes the identity-continuity axis viscerally obvious. Deferred as "framework generalizes" material for a companion paper; ethical static would swallow the formal object on first pass.
- **Second example of §4.5 Case A.** Published grid timelines with explicit τ_auth and T_exit numbers would convert the inequality from hypothetical to post-hoc diagnostic.

## Parallel track

Paper 24 candidate ("Shared Vision as Coordinating Prior") captured as a working-note seed at `working/shared-vision-coordinating-prior.md` with companion sim scaffold at `lean/shared_vision.py`. Bucket: **model-seed with paper potential, not yet promoted.** Three-test gate defined in the working note. The connection to Paper 23 is structural: Paper 23's §3 masking result at the controller-composition level, Paper 24's shared-vision claim at the multi-agent / organizational level — same alias-compatibility failure family, different scales. Paper 24 is exploratory-first; promotion only after the sim produces the three proposed regimes (fragmented realism / useful fiction / cargo-cult ideology) as distinct phases and the governance layer integrates cleanly.
