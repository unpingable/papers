# Paper 24: Shared Vision as Coordinating Prior — Working Notes

## Status

**v1.0 — 2026-04-28.** Promoted from working-note seed to preprint artifact and published on Zenodo (record 19861996; version DOI `10.5281/zenodo.19861996`; concept DOI `10.5281/zenodo.19861995`). Pre-publish punch list (per chatty's review, 2026-04-22, plus a 2026-05-01 cold-read pass): compression pass landed; Theorem 4 wording tightened from "stable fixed point" to "absorbing fixed-point family"; abstract softened from "arbitrary internal compositional divergence" to "hidden local-gradient compositional divergence" to match Proposition 2's scope; Theorem 2 → Proposition 2 demotion (codex review) reflected in the four-result stack. The claim surface may tighten further once Proposition 1 is promoted to theorem.

**Next branches, rough cost order:**

1. **Cold reread and prose polish.** Compression pass was substantial; a cold read will catch residual workshop-floor wording.
2. **Proposition 1 → Theorem.** The no-scalar-free-lunch claim is currently probe-backed conjecture. A proof requires fixing the scalar-aggregator class (continuous? Lipschitz? permutation-invariant? bounded?) and exhibiting the structural trade-off between freeze-freedom and stability within that class. This is the single highest-value next item.
3. **Theorem 2 appendix.** The proof sketch cites Appendix A (deferred); the alias-compatibility computation deserves full treatment for rigor.
4. **Probe artifacts made reproducible.** `shared_vision.py` exists as scaffold; a cleaned-up version matching the §4 probe tables exactly is worth producing.
5. **Zenodo push** after (1), ideally after (2) as well.

## The four-result stack (worth preserving under hardening)

The paper's spine is a three-layer pathology plus a temporal-persistence result, not "four independent theorems." Future edits should not flatten the layered structure into a bulleted theorem list without the layer annotations:

- **Theorem 1 — Aggregation-layer masking (exact under stated hypotheses).** First-moment aggregator + balanced bias-split ⇒ V-freeze in expectation. Named: *Mean-Aggregation Masking* in the body. Proved in §3.2.
- **Proposition 1 — No-scalar-free-lunch (probe-backed conjecture).** No scalar aggregator is simultaneously freeze-free on balanced bias-splits and stable on asymmetric populations. Four-aggregator probe in §4.1 exhibits every tested aggregator satisfying (P1) ↔ violating (P2). Formal proof deferred (§8, item 1).
- **Proposition 2 — Organizational alias-compatibility (scope-conditional).** Public action-level alignment is independent of $\varphi$-spread under stationary $V$; divergence surfaces proportionally under strategic shift. Structurally parallel to Paper 23 §3.3 case (i), lifted one scale.
- **Theorem 3 — Witness-filter (exact under stated hypotheses).** Alignment-correlated filter + 1-Lipschitz aggregator ⇒ update bound $|V_{t+1} - V_t| \leq \eta \tau$ regardless of aggregator. Corollary: shape-preserving aggregation is necessary but not sufficient.
- **Theorem 4 — Persistence of dissident-filter effects (exact under stated hypotheses).** One-shot filter + non-zero residual bias ⇒ fixed point with plant-error = $|\bar{b}_S|$, bounded below by filter threshold, no self-correction without exogenous witness reintroduction.

The three-class strength typography (exact theorem / probe-backed proposition / proof-sketch theorem) is deliberate. Flattening it loses the thing that makes the claim surface honest.

## Compression record (what moved from working note to preprint)

The working note (`working/shared-vision-coordinating-prior.md`) contained the discovery archaeology: dated "this morning's finding" entries, "closing closing" probe logs, gating bookkeeping, repo pointers, and several restatements of the same mechanism across discovery passes. The preprint `shared_vision_coordinating_prior.md` contains the result at each layer stated once, in a single section, with proof or proof-sketch. Key compression decisions:

- Stripped chronology ("morning pass," "evening sharpening," "very late," "closing closing").
- Consolidated six separate mechanism restatements (result stack × discovery-time passes) into one treatment per section.
- Demoted "no scalar aggregator is both freeze-free and stable" from implicit-theorem to explicit Proposition 1 with scope flag.
- Moved Agile from "emotional center" risk zone to one worked example in §5, with explicit scope language (*illustration, not target*).
- Moved working-note publication-gating language to NOTES.md.
- Removed repo-path pointers from body; kept only the companion-artifact reference to `shared_vision.py`.

## Changelog

### 2026-04-22

- Preprint artifact created. Four-theorem + one-proposition structure (§3), three-probe empirical section (§4), Agile case study scoped (§5), architectural-implication section (§6), compressed related-work section (§7), open/deferred (§8), 24 references.
- Working note retained in place at `working/shared-vision-coordinating-prior.md` for discovery-history reference. Not part of the published artifact.
- Sim scaffold remains at `~/git/lean/shared_vision.py`.

### 2026-04-22 (post-codex / gemini review)

External independent reviews (codex, gemini-cli) prompted the following tightening pass. Codex flagged five proof-soundness issues; gemini flagged five adjacency / under-citation issues. Both reviews were single-pass, no iteration.

**Math-soundness edits (codex-driven):**

- **§3.2 Theorem 1** — Strengthened hypotheses to close the proof gap codex flagged: the step from $\Phi(\mathbb{E}[E_t]) = 0$ to $\mathbb{E}[\Phi(E_t)] = 0$ requires either linearity of $\Phi$ or odd-symmetry of $\Phi$ combined with noise symmetry. Added explicit equilibrium-regime assumption (A4) and noise-symmetry assumption (A5) for the odd-symmetric case. Streamlined proof.
- **§3.4 Theorem 2 → Proposition 2** — Demoted from theorem to proposition. The original theorem's claim that action-divergence $D$ is $\varphi$-invariant under stationary $V$ is false in the standard linear setting (cross-agent variance depends on $(b - \varphi)$ spread). Reformulated as an *identifiability-collapse* claim: $D$ depends on $(b, \varphi)$ only through the combined offset $(b_i - \varphi_i)$, so when $b$ is not independently observable, $D$ cannot identify $\varphi$-spread from $b$-spread. Exact in the equal-gain regime; heterogeneous-gain and post-shift functional form left as scope-flagged. Removed the unsupported $\Theta(\|\varphi\|^2 |\Delta V|^2)$ scaling claim.
- **§3.5 Theorem 3** — Replaced the "1-Lipschitz in each coordinate" hypothesis (which gives an $L^1$-type bound, not the sup-norm bound the proof needed) with the explicit sup-norm-bounded condition $|\Phi(E)| \leq \|E\|_\infty$. Updated §2's aggregator-class definition to match. The result is now exactly what the proof actually establishes.
- **§3.6 Theorem 4** — Narrowed the necessity clause from "cannot be reduced without (a) re-introducing $|b_i| \geq \tau$ witnesses or (b) exogenous $V$-perturbation" to the more defensible "the fixed point is stable to internal dynamics under fixed cohort and fixed update rule; escape requires exogenous intervention (cohort modification, rule change, or direct $V$-perturbation)." Codex correctly noted that adding low-bias witnesses also fixes the error.
- **§6** — Softened the "the only architecture satisfying both freeze-freedom and stability" claim to a conditional statement: in its current probe-backed form, the architectural recommendation is design-strength against the probed aggregator classes; the universal claim depends on Proposition 1 promoting to theorem.

**Adjacency edits (gemini-driven):**

- **§7.1** — Added paragraph on epistemic democracy (Condorcet jury theorem extensions, List & Goodin 2001) and a brief Aumann-agreement-theorem mention. Theorem 3 reframed as a dynamic violation of epistemic-democracy independence and competence axioms.
- **§7.2** — Added paragraph on performative prediction (Perdomo et al. 2020) as the contemporary ML analogue of Theorem 3: model state determining its own training distribution = governance-layer prior determining witness inclusion.
- **§7.5** — Renamed from "Wisdom of crowds and statistical aggregation" to "Robust statistics, wisdom of crowds, and statistical aggregation." Added a substantial paragraph on robust statistics — breakdown-point theory (Huber 1964) and influence-function analysis (Hampel 1971) — as the most direct technical cousin of Theorem 3 and Proposition 1. Softened the wisdom-of-crowds framing per gemini's novelty-overclaim flag: the contribution is *control-theoretic dynamic formalization* of conditions that wisdom-of-crowds explicitly identifies as requirements, not first-time identification of the failure conditions. Added Page (2007) diversity-prediction theorem reference.
- **References** — Added six new entries: List & Goodin (2001), Aumann (1976), Perdomo et al. (2020), Huber (1964), Hampel (1971), Page (2007). Total references: 30.

**What was NOT changed:**

- Abstract — the qualitative claims survive the demotion (alias-compatibility is still alias-compatibility) and the proof tightenings (claims become more, not less, precise). No abstract edits needed.
- Section numbering — kept 1–8 intact; new adjacency content folded into existing subsections rather than spawning new ones.
- §5 case study (Agile) — unchanged; chatty's discipline (Agile as illustration not target) remains intact.

## Open / deferred

- **Proposition 1 theorem-ization.** Highest-value next item. See §8, item 1.
- **Case (iii)-style extension.** The framework's aggregation-layer pathology has three sufficient conditions (first-moment + balanced bias-split; Lipschitz aggregator + alignment-filter; one-shot filter + residual bias). A fourth sufficient condition — aggregator linearity in noise at the null space of witness second-order structure — is conjectured but not developed. Exploratory only.
- **Vector $V_t$.** Sketched in working note. Left for sequel.
- **Binding problem.** Who authors $V_t$, under what legitimacy. Connects to admissibility-family work.
- **Non-managerial applications.** Federated learning, distributed estimation, multi-arm bandits, scientific consensus. Each merits its own worked development.
- **Empirical calibration.** Real organizational bias-distribution data would let the theorems be applied as post-hoc diagnostics rather than illustrative theory.
- **Remediation dynamics.** Theorem 4's "active reintroduction required" clause raises a transition-dynamics problem not addressed by the static fixed-point analysis.

## Parallel track

Paper 23 ("Ops Is Control with a Non-Self-Identical Controller") is the immediate sibling. The braid point is stated explicitly in §7.6: *organizations mistake compressed public alignment for resolved internal composition.* Paper 23's §3.3 Operational Masking Theorem names the phenomenon at the controller layer with three-class strength typography (exact / first-order / ε-approximate); the present paper lifts the structure to the multi-agent / organizational layer and supplies the specific aggregation-layer mechanism. The two papers cross-cite naturally.

The admissibility family (separate working track) is the receipt-lineage architecture line referenced in §6 and §7.7. The present paper's §6 architectural-implication argument identifies the formal problem that receipt-lineage solves: it is the specific answer that Theorem 1 and Proposition 1 jointly force. The admissibility-family paper (in preparation) supplies the reciprocal: the general architecture for which Paper 24's receipt-preservation requirement is one instance.

## Downstream (noted, not developed)

The witness-filter and temporal-persistence results have implications for organizational-enclosure analysis (a working track under the *Latent Capitalism* volume) and for temporal-capture dynamics (a working track under the *Chronopolitics* volume). Both extensions are flagged in §8 and explicitly not developed in Paper 24. The paper's strength is the structural analysis; the applied extensions belong in their respective volumes, not in the preprint.
