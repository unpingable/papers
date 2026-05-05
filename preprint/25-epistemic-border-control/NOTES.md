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

## Classical-control citation-debt hardening pass (logged 2026-05-05)

**Problem.** Paper invokes finite-horizon observability matrix $O_T$, observability Gramian $W_o$, Kalman filter, LQR, $\sigma_\text{min}(O_T)$, posterior covariance projection — every load-bearing object is classical control-theory inventory — while the reference list contains zero classical control citations. Theorem 1 is the closed-loop reading of Kalman observability decomposition; Proposition 1 is the LTI Kalman posterior-Gramian formula. Currently reads as if the author may not know this. Reviewers in control / formal-methods communities will read it that way.

**Severity.** Medium-high if P25 reaches control / formal-methods readers; medium for Δt/admissibility audience. Not fatal. Untucked shirt, not broken zipper.

**Goal.** Own classical substrate explicitly; preserve novelty as the admissibility / proxy-authority reading. Internal warning label: **cite the classical math, claim the admissibility reading.** Do not let this become a new section explaining control theory to control theorists.

**Add references (minimum set).**

1. **Sontag, *Mathematical Control Theory* (2nd ed., 1998)** — observability decomposition. Cite at §3.1 / Theorem 1.
2. **Anderson & Moore, *Optimal Filtering* (1979)** *or* **Kailath, Sayed & Hassibi, *Linear Estimation* (2000)** — Kalman posterior covariance / Gramian scaling. Cite at §3.2 proof sketch.
3. **Francis & Wonham, "The Internal Model Principle of Control Theory" (Automatica 1976)** — exact regulation requires a model of the reference. Highest-leverage citation; structural anchor for the necessity claim. Cite in §6 (probably a new sub-section between §6.1 and §6.2, ~half the length of §6.1) or in §1 thesis.
4. *Optional:* **Åström & Murray, *Feedback Systems* (2nd ed., 2020)** — readable modern bridge. Add to §1 only if a reader-bridge sentence is needed.

**Placement summary.**

- §3.1 Theorem 1 proof: one sentence acknowledging this is the closed-loop reading of Kalman's observability decomposition [Sontag].
- §3.2 Proposition 1 proof sketch: one sentence citing the standard Kalman posterior-Gramian formula [Anderson & Moore / Kailath].
- §6 firewall section: new "vs internal model principle" item [Francis & Wonham], distinguishing classical impossibility from the admissibility reading.
- §1 or §6.5: spine-welding sentences (below).

**Spine-welding sentences (draftable core).**

> Classical observability results explain why the hidden target cannot be recovered from the proxy channel alone. The admissibility claim here is that a controller acting only on proxy-derived feedback cannot legitimately bind its action to the target it cannot observe.

> This is the partial-observability instance of the series' broader authority-binding refusal: a mechanism may be well formed at one layer while lacking standing to bind, mutate or authorize at another.

**Why this earns its keep three ways.**

1. Cleans control-theory citation debt before a reviewer does.
2. Owns the math substrate as classical, sharpening the §6 firewalls (Goodhart and performative prediction become contemporary distinctions; IMP becomes the structural anchor).
3. Surfaces P25's spine position — partial-observability instance of the same authority-binding refusal that lives in the Lean kernel (`AuthorizedStep`: stale basis cannot bind at mutation layer) and across the admissibility family. Currently implicit; making it explicit welds P25 into the series rather than letting it float as a one-off control-theory paper.

**Scope of the patch.** ~4–8 new sentences in the body, 3–4 new references. Hardening pass, not rewrite. Does not block P26/P27 spine work. Land before v0.3 → v1.0 ratchet, but doesn't have to be the next motion.

**Not P25 territory (recorded to prevent re-confusion).** Event-triggered / self-triggered control (Tabuada, Heemels, Lemmon) is **not** the right adjacency for P25 — that literature is about temporal sparsity of control updates under continuous-time dynamics, which belongs to P22 actuation / Δt timing, not to P25's spatial observability asymmetry. Earlier conflation corrected.
