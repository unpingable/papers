# Corpus Map — Internal Diagnostic

**Status:** Internal diagnostic, phase 1 of the map work. NOT a public landing page. May expose construction state. Section 7 is deliberately ruthless. Sibling to [collaborator-entry-map.md](collaborator-entry-map.md), which is the public-interface seed (phase 2 candidate). This note's job is to audit *that* one — and the corpus underneath it — for whether it is honest about its own entrances.

**Date filed:** 2026-05-10.

**Rule it enforces:** *A map may point to embedded material, but it must not call embedded material an entrance.* The internal map exists to find places where the public-interface candidate is about to violate this.

---

## 1. Core problem (what the work is doing)

The corpus investigates a recurring failure: **systems authorize action faster than they preserve basis, standing, consequence, and contestability.** Across substrates (control theory, ops, AI agents, civic systems, software supply chains, formal proof) the same shape recurs — methodological convenience gets promoted into evidentiary rule, evidentiary rule fossilizes into effective ontology, and the *standing-of-claims* layer disappears under engineering vocabulary.

The framework's distinctive move is to keep apart what most systems collapse:

> **Monitoring asks what happened. Admissibility asks whether what happened may be used.**

That line is already canonical in `collaborator-entry-map.md`. Keep it.

## 2. Shortest thesis (compressed claims)

Five load-bearing claims, in approximate order of mass:

1. **Intent → action collapse is unsafe without an admissibility middle.** (Governor / agent_gov body of work.)
2. **No universal plant clock.** Distributed control fails along four orthogonal axes — gauge, clock, estimation, actuation — with ratio relationships that decompose every prior result. (P22 keystone.)
3. **Local validity does not guarantee global continuity.** Locally valid operations can compose into globally false systems. (Candidate primitive, 2026-05-10, not yet ratified.)
4. **Reconciliation can be controller-correct while operator-unsound.** Success of the loop is not testimony to soundness of the system. (P27 spine; controller-continuity work.)
5. **Testimony is not theory of substrate.** Admitting a signal does not admit the signal's preferred system diagram. (Candidate, 2026-05-10, just filed.)

These are not the only claims. They are the load-bearing five if you had to triage in case of fire.

## 3. Artifact families (what exists, where)

Five families, each a different register, each with its own location:

- **Published preprints (Δt framework series).** P01–P24 on Zenodo at v1.0+ (several at 1.0.1 or 1.1 after revision). Concept DOIs per paper. Located: `preprint/01-*` through `preprint/24-*`. Status: shipped, citable, immutable per version.
- **Scaffolded preprints.** P25 (Epistemic Border Control, v0.2-draft), P26 (Premature-Belated Duality, v0.3 status "1.0-candidate"), P27 (Obligation-Unsound Reconciliation, v0.0-stub). Each has metadata.yaml + README.md + CANDIDATES.md + NOTES.md; substantive content for P25/P26 lives in `working/`. Located: `preprint/25-*`, `preprint/26-*`, `preprint/27-*`.
- **Working notes.** ~50 files in `working/`, including paper candidates, doctrine stubs, recognition records, methodology notes, companions to published papers. Organized by topic cluster per `working/README.md` (nine clusters). Includes the `primitives/` field notebook and `cybernetic-failure-taxonomy/` subdirectory.
- **Lean formalization.** Separate repo at `~/git/lean/`. `LeanProofs/Admissibility/` holds Authority, StateTransition, Derivation, Execution, Corrective, CorrectiveBoundary, WitnessInvariance. `lake build` green, no `sorry`. Proof-gate-only CI per repo doctrine.
- **Substack archive (separate corpus).** `~/git/neutral.zone/` (Hugo site). Neutral Ambassador series, Δn case law, naming interventions. Not part of the preprint series; serves as public translation layer for civic systems / NQ-shaped material.
- **Software kernels (referenced, not in this repo).** Wicket (admissibility kernel), agent-governor (deployment substrate), NQ (witness-standing broker). Pointers exist in `collaborator-entry-map.md`; some not public.

## 4. Path inventory (what entrances exist, intact / embedded / missing)

The public-interface candidate proposes paths for different reader types. Audit:

- **For ops/SRE readers** → NQ witness/testimony / reconciliation failure
  - **Intact pieces:** P15 (Cybernetic Fault Domains), P22 (No Universal Plant Clock), P23 (Non-Self-Identical Controller), `working/sre-as-shock-absorption.md`, `working/laundering-patterns-reliability-practice.md`
  - **Embedded, not entrance:** NQ witness/testimony doctrine — lives across multiple working notes and the agent-governor kernel docs, but no consolidated piece a cold reader can hand-hold from
  - **Gap:** no single "NQ in 10 pages" essay
- **For AI governance readers** → Agent Governor / admissibility middle
  - **Intact pieces:** P10, P11, P12, P18, P19, P20, P21, `working/jarbrain.md`, `working/governor-not-mind.md`, `working/gim.md`
  - **Embedded, not entrance:** governor doctrine — memory note says "cite when writing family paper, don't extract as standalone"
  - **Gap:** no standalone "governor in 10 pages" piece. The doctrine is dispersed.
- **For formal-methods readers** → Δt / Lean boundary pieces
  - **Intact pieces:** P22, Lean repo `~/git/lean/LeanProofs/Admissibility/`, `working/boundary-composition-audit.md`, `working/boundary-composition-investigation.md`
  - **Status:** comparatively well-served. The repo doctrine ("Lean proves, papers publish") makes the entrance honest — Lean readers go to Lean repo, paper readers go to P22.
- **For civic / political readers** → civic systems literacy / authority laundering
  - **Intact pieces:** Substack archive (~/git/neutral.zone/), `working/breach-mistaken-for-authorization.md`, `working/ground_stops_moving.md`, P17 (Receipt the Compiler), P19 (Shadow Governance)
  - **Embedded, not entrance:** civic-systems-as-operating-system framing is implicit across substack essays but not consolidated as a doctrine page
  - **Gap:** no single "civic systems literacy" entrance essay. Substack archive is browse-only.
- **For "weirdos of taste and stamina"** → enter through the full machinery
  - **Status:** functional. Anyone with appetite can start at P22 and walk both ways. This path is intact by virtue of not pretending to be a tutorial.

## 5. What this work is not (anti-scope)

Per existing notes plus the falsification guardrails memory:

- Not a universal theory of everything. The Δt framework has falsification guardrails specifically to prevent it from becoming a universal solvent.
- Not "alignment, but with more nouns." The frame is admissibility/governance/standing, not value alignment.
- Not AI safety policy advocacy.
- Not an observability product.
- Not formal-methods hobbyism. Lean is a proof-gate, not the artifact.
- Not an agent runtime. Wicket / agent-governor are admissibility kernels, not LLM scaffolds.
- Not a demand that every pattern become a paper, primitive, or spec. Anti-collapse runbook is built specifically against this.
- Not peer-reviewed. Venue is Zenodo + books per explicit choice; not seeking academic publication.

## 6. Canonical entry candidates (curated short list, with custody receipts)

**Receipt template required for each entry:**

> **Claim:** what the artifact asserts or licenses
> **Artifact:** name + location
> **Canonical version:** DOI / commit / version tag
> **Verification:** proof gate / Zenodo / peer-review status / explicit "informal"
> **Change rule:** what must happen for the canonical version to advance

Pointing at named artifacts without these fields is the parasitic layer the rest of the kernel work is built against — *prose claims about artifacts* instead of *receipts for artifacts*. The template is boring on purpose. Same template used by the public-facing essay when it cites the kernel.

---

### P22 — No Universal Plant Clock (series keystone)

- **Claim:** Four-layer decomposition (gauge / clock / estimation / actuation) is the foundational failure geometry of distributed control; prior framework work reduces to ratio relationships across these layers.
- **Artifact:** `preprint/22-no-universal-plant-clock/`
- **Canonical version:** v1.1; concept DOI `10.5281/zenodo.19119617`; version record `19671885`
- **Verification:** Zenodo-immutable per version; not peer-reviewed (Zenodo + books venue per explicit choice)
- **Change rule:** version bump → new version DOI; metadata.yaml + README updated; concept DOI persists

### P23 — Non-Self-Identical Controller (ops/SRE entrance)

- **Claim:** Ops is hybrid control with a non-self-identical controller; four failure families (handoff, escalation, hidden compensation, fatigue); projection + observability masking is the novel pair.
- **Artifact:** `preprint/23-non-self-identical-controller/`
- **Canonical version:** v1.0; DOI `10.5281/zenodo.19055415`; record `19715302`
- **Verification:** Zenodo-immutable per version; not peer-reviewed
- **Change rule:** as above

### P17 — Receipt the Compiler (civic-adjacent entrance)

- **Claim:** Propaganda as hidden epistemic policy; architecture of legible memory.
- **Artifact:** `preprint/17-receipt-the-compiler/`
- **Canonical version:** v1.0; DOI `10.5281/zenodo.18841815`; record `18841815`
- **Verification:** Zenodo-immutable per version; not peer-reviewed
- **Change rule:** as above

### P15 — Cybernetic Fault Domains (theory↔engineering bridge)

- **Claim:** Commitment outruns verification; cybernetic fault-domain taxonomy.
- **Artifact:** `preprint/15-cybernetic-fault-domains/`
- **Canonical version:** v1.0; DOI `10.5281/zenodo.18686130`; record `18686130`
- **Verification:** Zenodo-immutable per version; not peer-reviewed
- **Change rule:** as above

### P10 — You Need More Than Just Attention (AI-governance entrance)

- **Claim:** Invariant requirements for temporal coherence in AI systems.
- **Artifact:** `preprint/10-invariant-requirements-temporal-coherence/`
- **Canonical version:** v1.0; DOI `10.5281/zenodo.18039926`; record `18039927`
- **Verification:** Zenodo-immutable per version; not peer-reviewed
- **Change rule:** as above

### Lean Admissibility kernel (formal-methods entrance)

- **Claim:** Authority verdicts, mutation algebra, read-side bridge, authorized step composition, corrective monotonicity, witness invariance, artifact-kind × use-kind admissibility (FiatAdmissibility), Governor-facing collapsed-surface refusal gate (SurfaceAuthorization), NQ-facing visible-green-vs-recovery-margin refusal (RecoveryMargin), NS-facing one-step closure-eligibility refusal (ClosureEligibility), numerical-kind × numerical-use admissibility (NumericalAdmissibility), public-receipt-refinement recovery doctrine for SurfaceAuthorization (PublicReceiptRefinement) — proven, not asserted.
- **Artifact:** `~/git/lean/LeanProofs/Admissibility/` (Authority, StateTransition, Derivation, Execution, Corrective, CorrectiveBoundary, WitnessInvariance, FiatAdmissibility, SurfaceAuthorization, RecoveryMargin, ClosureEligibility, NumericalAdmissibility, PublicReceiptRefinement) + root sibling `LeanProofs/CollapsedSurface.lean`
- **Canonical version:** HEAD of `~/git/lean` main branch; commit pending as of 2026-05-12
- **Verification:** `lake build` green; CI proof-gate-only per repo doctrine; no `sorry`
- **Change rule:** ratification note + proof update; lake build must stay green; new theorems require docstring + sibling-module audit; changes to ArtifactKind / UseKind / classify (FiatAdmissibility), to the SurfaceStatus × ActionKind × Breaker gate (SurfaceAuthorization), or to the ThreatState × SlackState × IntervalOutcome verdict (ClosureEligibility) require explicit ratification
- **Scope fences worth preserving:** ClosureEligibility is a one-step closure kernel, not a persistence model — caller-supplied direct handoff→closure comparison; no trace/waiver/authority modeling. SurfaceAuthorization encodes the refusal gate, not the recovery epistemology (Breaker stays abstract). RecoveryMargin proves the independence of visible-green from recovery-margin, not a recovery dynamics

### Substack archive — Neutral Ambassador (civic-public entrance)

- **Claim:** Naming interventions, Δn case law, civic-systems-as-operating-system framing.
- **Artifact:** `~/git/neutral.zone/` (Hugo site)
- **Canonical version:** HEAD of `~/git/neutral.zone` main branch; commit `88eee4a` as of 2026-05-11
- **Verification:** ⚠️ informal — essays, not formal claims; no proof gate; not Zenodo-immutable
- **Change rule:** standard editorial; no canonical-version semantics beyond commit history

### `working/collaborator-entry-map.md` (public front-page candidate)

- **Claim:** Aspiring public front-page introduction to the corpus for capable readers from outside the operator's vocabulary.
- **Artifact:** `working/collaborator-entry-map.md`
- **Canonical version:** ⚠️ not yet shipped; lives in `working/` as seed (status header at file end acknowledges this)
- **Verification:** ⚠️ working note; not promoted
- **Change rule:** promotion gated by §9 of this internal map; canonical-entries section using the receipt template above is required for promotion

### `working/jarbrain.md` (governance/cognition entrance candidate)

- **Claim:** LLMs as high-bandwidth language production systems unbundled from stabilizers; hallucination as default behavior, not reasoning failure.
- **Artifact:** `working/jarbrain.md`
- **Canonical version:** ⚠️ working note; would need framing before public-handing
- **Verification:** ⚠️ working note; not preprint
- **Change rule:** promotion to preprint via the standard preprint-directory ceremony (numbered slot + metadata.yaml + Zenodo push)

---

**Curated minimum public set (8 entries above).** Entries marked ⚠️ are *embedded entrances*, not *canonical entrances*: they exist as material but lack the verification or change-rule custody that lets them be handed cold. Three of the eight are missing canonical verification/change-rule custody. That is the load-bearing fact, and it is what §8 (Gaps) and §9 (Promotion gate) act on.

## 7. Construction state (the ruthless layer)

Status taxonomy (honest):

- **Published v1.0+:** P01–P24 (24 papers, all on Zenodo, citable, immutable per version)
- **Scaffolded only:** P25 (v0.2-draft, content in working/), P26 (v0.3, status "1.0-candidate" — close to ship), P27 (v0.0-stub)
- **Working notes, paper-shaped:** `premature-belated-duality.md` (→P26), `shared-vision-coordinating-prior.md` (already shipped as P24), `installed-will.md`, `temporal-coherence-music.md`, `causality-control-plane.md`, `jarbrain.md`, `governor-not-mind.md`, `gim.md`
- **Working notes, doctrine / recognition records:** `authority-observable-not-constructible.md`, `authority-debt-and-revocation.md`, `accountable-mutation-os-layer.md`, `breach-mistaken-for-authorization.md`, `admissible-recovery-semantics.md`, `admissibility-control.md`, others
- **Candidate primitives (named, not ratified):** control-set laundering, local-global validity gap (filed 2026-05-10), testimony-vs-self-theory (filed 2026-05-10), plus the active list in `working/primitives/`
- **Doctrine stubs:** declared-substitution stubs (per `project-admissibility-doctrine-stubs.md` memory)
- **Methodology notes (not for citation):** `methodology-as-operational-discipline.md`, `phase-model-nonlinear-work.md`, `narrow-after-contact.md`, `anti-collapse-runbook.md`
- **Lean:** thirteen `Admissibility/` modules (Authority/StateTransition/Derivation/Execution/Corrective/CorrectiveBoundary/WitnessInvariance/FiatAdmissibility/SurfaceAuthorization/RecoveryMargin/ClosureEligibility/NumericalAdmissibility/PublicReceiptRefinement) plus root `CollapsedSurface`; lake build green; no sorry
- **Substack archive:** Hugo site, separate repo, not numbered, browse-only
- **Software kernels:** Wicket / agent-governor / NQ — exist as code, not all public, not all in this repo
- **Parked / superseded:** `working/epistemic-border-control.md` (now pointer to P25); various drafts archived under preprint dirs
- **Speculative:** Δm (predicted seventh admissibility boundary), various sketches in `primitives/`

**What this looks like from outside:** a 27-paper preprint series (24 shipped, 3 in motion) with a thick supporting layer of working notes, a Lean kernel, a parallel essay corpus, and three sibling software projects. *That is what's actually there.* The internal map's job is to keep that visible without dressing it as a curated product.

## 8. Gaps blocking public promotion of `collaborator-entry-map.md`

What must be true before phase 1 → phase 2 (i.e., before `collaborator-entry-map.md` becomes the public front page rather than a working seed):

**Hard blockers:**

1. **No consolidated NQ entrance piece exists.** Reader for ops/SRE path cannot be handed one document. Either write it, or `collaborator-entry-map.md` must explicitly say "NQ doctrine is currently embedded across [...]; consolidation forthcoming."
2. **No consolidated Governor entrance piece exists.** Same problem on the AI-governance path.
3. **No civic-systems-literacy consolidating piece exists.** Substack archive serves as the corpus but has no curated entry. Same issue.
4. **Software kernel pointers are incomplete.** `collaborator-entry-map.md` line 65 says "Pointers exist in the candidate-shapes inventory" — this needs to either be a real link or the section needs scoping back to what's public.

**Soft blockers (would be nicer):**

5. **No "8-item minimum public set" currently exists as a links list anywhere.** The list is reconstructable but not curated.
6. **`collaborator-entry-map.md` currently runs ~160 lines and ends mid-section in this read.** Need to confirm it has a clean ending before promoting.
7. **No explicit version / status header on `collaborator-entry-map.md`** flagging that it is a working seed, not the front page. Already partially present at top; could be sharper.

**Honest gap-mode option:** ship `collaborator-entry-map.md` *with explicit gap markers* — "consolidated NQ entrance: in progress" — rather than waiting for all three consolidations. This trades polish for honesty, which is in-character. Per the agreed rule: the map *may* point to embedded material, but *must not call* it an entrance. Marking gaps as gaps satisfies the rule.

## 9. Promotion gate (phase 1 → phase 2)

Conditions for promoting `collaborator-entry-map.md` from working seed → public front page:

- [ ] Hard blocker 1 OR explicit "in progress" marker for NQ path
- [ ] Hard blocker 2 OR explicit "in progress" marker for Governor path
- [ ] Hard blocker 3 OR civic path scoped to Substack archive only (with "browse-only, no curated entry" disclaimer)
- [ ] Hard blocker 4 resolved (kernel pointers either real or scope-back)
- [ ] Status header at top of `collaborator-entry-map.md` clarifies it is *the* public front page, not a seed
- [ ] One pass to confirm the document has a clean ending and no embedded TODOs
- [ ] **Canonical-entries section added to `collaborator-entry-map.md` using the receipt template from §6** (claim / artifact / canonical version / verification / change rule). Without per-entry receipts, the public map points at *prose claims about* canonical artifacts rather than *receipts for* them — the parasitic layer the kernel work is built against.

**Recommendation (not authorization):** if the user wants to ship the public interface soon, the path of least resistance is to convert hard blockers 1–3 into "in progress" markers rather than gate the map on completing three new entrance pieces. The map's job is to route, not to be the entrance itself. Routing to honest gaps is better than not routing.

If the user wants to do the consolidation work first, the smallest gap is NQ (per earlier triage — doctrine may need consolidating, but the source material is closer to ready than Governor's).

---

**Cross-references:**
- [collaborator-entry-map.md](collaborator-entry-map.md) — public-interface seed, the artifact this diagnostic audits
- [where-admissibility-fits.md](where-admissibility-fits.md) — applicability fence
- [where-admissibility-fits-candidates.md](where-admissibility-fits-candidates.md) — candidate applications inventory
- `working/README.md` — full working-notes inventory by cluster
- `working/primitives/README.md` — primitives field notebook
- `project-p25-spine-note.md` (memory) — series spine note
- `project-paper22-keystone.md` (memory) — keystone paper context
