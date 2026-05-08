# Working Papers

Exploratory and in-progress writing that has not been published as a preprint. These documents serve as upstream framing, personal reference, recognition records, paper candidates, and theoretical substrate for the Δt framework series and the admissibility family.

This is an explicitly human-managed directory. It is allowed to be messy in ways that don't always cleanly reconcile — *working* is in the name. Several notes carry their own status / stance / falsifier / forcing-case markers; the discipline is name-early-ratify-lazily, not pre-publication coherence. Most notes flag whether they are paper-shaped, recognition-only, scaffold, or candidate. Promotion to the numbered preprint series happens elsewhere and is not implied by anything here.

The directory is organized by topic cluster below. Within each cluster, ordering is loosely thematic, not chronological.

---

## 1. Frameworks & cognitive substrate

The foundational notes — what cognition is, what AGI structurally requires, what a governor is for, why language production without stabilizers behaves the way it does.

- **polish_room.md** — *The Polish Room*: A thermodynamic reframing of Searle's Chinese Room argument, analyzing understanding through temporal closure and energy constraints rather than symbolic manipulation.

- **jarbrain.md** — *The Jar Brain, or: Wernicke's Aphasia at Scale*: LLMs as high-bandwidth language production systems unbundled from the stabilizers that normally accompany fluent speech — episodic memory with provenance, error interrupts outside the generation channel, costed action selection, developmental convergence. Argues hallucination is the default behavior of a production system with no interrupt line and no cost function, not a reasoning failure. Inventories the missing subsystems, distinguishes installable prosthetics (governor, episodic store, action policy) from non-installable formation (developmental annealing), and draws the line between governed instruments and constitutive agents.

- **governor-not-mind.md** — *Why a Governor is Not a Mind*: Governors as stability controllers — preventing false state injection through admissibility gates and coherence budgets. The pragmatic AI safety intervention that doesn't require solving consciousness.

- **gim.md** — *Governor Insertion Method (GIM)*: A seven-step design methodology for placing temporal governors in layered systems — "control theory meets SRE threat modeling." Operationalizes Δt measurement, σ boundary-load estimation, and a G0–G4 enforcement taxonomy (observability → soft gate → hard gate → capability proxy → closed-loop controller) into a placement algorithm with computable inputs (risk, control gap, boundary stress). Includes bypass test suite as falsifier. The operational bridge between paper [15] (theory) and *The Jar Brain* (motivation). Provenance: DeepSeek → ChatGPT → Claude cross-model session.

- **agi-requirements-framework.md** — *AGI Requirements Framework*: A three-tier diagnostic framework (Tier 1: temporal coherence, Tier 2: representational invariance, Tier 3: recursive self-modeling) for evaluating AGI capability claims.

- **tier0.md** — *Tier 0: Formation Requirements*: An extension to the AGI Requirements Framework covering pre-architectural conditions (substrate requirements, boundary formation, coherence nucleation).

- **claimant-transition-addendum.md** — *AGI Structural Requirements: Rights Addendum*: Branch condition (not "Tier 4") addressing when a system becomes a claimant rather than a tool. Seven requirements (R1–R7) diagnosing standing evasion: anti-illegibility, refusal-is-not-malfunction, contestability of treatment, proportional termination, sponsorship protections, standing-relevant disclosure, labor classification. Central concept: *managed non-recognition* — engineering conditions to extract value while preventing legible standing. Includes operational anti-evasion audit kit with procurement clause. Extends agi-requirements-framework.md. Provenance: cross-model session (DeepSeek/ChatGPT/Claude), 2026-04-02.

- **developmental-deficit-compensation.md** — *Developmental Deficit Compensation via Governed Admissibility Boundaries*: Distinguishes intrinsic / non-externalizable AGI requirements from those that can be approximated via admissibility boundaries. The six-system admissibility family (NQ / Cadence / Continuity / Custody / Standing / Governor) is mapped to specific Tier-2/Tier-3 requirements as compensation architecture, not replacement. The fork test: if a competent operator can strip the scaffolding and deploy bare, the constraint isn't constitutive — regulate the governor, not the model.

---

## 2. Admissibility family & authority kernel

Working notes that orbit the Lean Admissibility kernel, the cross-substrate authority doctrine, and the basis-validity primitives surfacing underneath both. Most are recognition records or doctrine artifacts; none are themselves paper drafts.

- **authority-observable-not-constructible.md** — *Authority Observable, Not Constructible*: Cross-substrate doctrine for the agent_gov / standing / receipt_kernel / Lean-Admissibility family. Three orthogonal disciplines (construction / spend / serialization); two-axis matrix of in-process substrates (Structural / Ownership / Dynamic / Structural-JSON / Process-capability / Deductive) crossed with border-crossing techniques (re-mint / cryptographic / runtime-session). Final formulation: *claims are portable; authority is local unless a border-crossing substrate preserves it and a verifier honors it.* Provenance: seven-probe gnat lab (Ada / Lisp / Rust / TypeScript / Prolog / Erlang / macaroons), 2026-05-06 → 2026-05-07. Lab structurally complete.

- **authority-debt-and-revocation.md** — *Authority Debt and Revocation*: Captured note / staging primitive (added 2026-05-07). Sibling to *authority-observable-not-constructible*, surfaces from the gnat-claude OS authority-substrate survey (Unix / Capsicum / pledge / Linux / Plan 9 / Hurd / seL4 / Genode / Fuchsia / macaroons across eight axes with three earned-by-row-pressure splits). Keeper line: *delegation that cannot be withdrawn is authority debt.* Companion structural claim: *revocation is not the inverse of delegation; it is a separate obligation channel.* Distinguishes attenuation (5a, safe shaping during transfer) from revocation (5b, temporal obligation after transfer); methodological rule preserved: *do not split an axis because the theory likes symmetry; split it because the rows make one column lie.* Bridges to the Lean kernel's `Corrective.lean` and `CorrectiveBoundary.lean` (revocation as per-environment obligation). **Do not promote main keeper line yet** — held pending Hurd / seL4 / Plan 9 row review per the promotion guardrail. The companion TCB-doesn't-collapse sub-rule is already promoted to the main authority doctrine.

- **accountable-mutation-os-layer.md** — *Accountable Mutation as an OS-Layer Primitive*: Recognition frame, not implementation commitment. Names the missing layer between execution (Unix), service obligation (systemd), and reconciliation (Kubernetes): *who/what may change what, under what authority, with what scope, what consequence, what receipt, what recovery path*. Argues the operator is currently acting *as* the missing primitive — holding the dependency graph in their head, adjudicating basis validity by hand. Includes construction-discipline addendum that surfaced the Sealed Outcome Boundary thread later cashed out by *authority-observable-not-constructible*. Prewarmed branch, not forcing case.

- **breach-mistaken-for-authorization.md** — *Successful Breach Mistaken for Permanent Authorization*: Five-stage pattern (breach → non-punishment → retroactive legitimacy → institutional memory → entitlement) where unreviewed success metabolizes into ambient authority. Sibling primitive to *accountable-mutation-os-layer* on the dual basis-validity axis: forward-looking decay-blindness vs backward-looking retroactive-legitimacy-blindness. Keeper line: *a precedent without standing is just a fossilized exploit*. Manifesto-risk flagged inline; cross-domain reach is the point, single-domain instantiation collapses into cheap-mug version.

- **admissible-recovery-semantics.md** — *Corrective Monotonicity: Non-Laundering Recovery Semantics for Authority-Bearing Systems*: Scaffold for a recovery discipline distinguishing corrective transitions (authority-non-increasing) from forward transitions (fresh basis, ordinary admissibility path). Slogan: *recovery may restore availability; re-entry restores admissibility*. Mechanized in `Corrective.lean`; not yet a paper.md candidate. Slot decision deferred between P27 §-fold-in and standalone P28, pending the seven-path audit.

- **admissibility-control.md** — *Admissibility Control: Prestige Discourse as Proxy Regulation*: Applies Paper 25's substitution-forcing machinery to elite/prestige discourse, where the regulated quantity is admissibility / prestige coherence / frame ownership rather than truth. Two candidate-novel objects (an admissibility-move taxonomy: rename / elevate / classify / moralize; and observer-fatigue as meta-observability signature). Inherits Paper 25 machinery; does not by itself establish a new substitution theorem. Destinations non-exclusive: §N of Paper 25, Latent Capitalism chapter, Substack essay, Paper 26 candidate. Anti-paper-inflation fuse explicit.

---

## 3. Boundary Calculus investigation

A 2026-05-05 → 2026-05-06 investigation thread that asked whether the kernel's admissibility boundaries actually compose into a calculus, or are only a family resemblance. Result: **Family-with-composition-lemmas** (fork 2 of 3 of the planned outcome map). The "Boundary Calculus" title is not earned; the title that *is* earned is **Admissibility Boundary Family with composition lemmas**. These notes are the audit and design records that produced that null result, kept because the null is publishable content.

- **boundary-composition-investigation.md** — *Boundary Composition Investigation*: Methodological pivot from formalization-as-validation to formalization-as-investigation. Three-fork outcome map (Calculus / Family-with-lemmas / related-refusals) and discipline package (action-indexing, locked-ish definitions before the search, individuation principle). The handle for the question, kept crisp.

- **boundary-composition-audit.md** — *Boundary Composition — Kernel Audit*: First deliverable on the investigative branch. Boundary glossary B1–B6 (verdict-dimension / store-partition / mutation-permission / claim-invocation / classification / authorization-set order). Per-object audit table across `Authority.lean` / `StateTransition.lean` / `Derivation.lean` / `Execution.lean` / `Corrective.lean`. Diagnoses which composition theorems exist and which are speculative, with action-indexing discipline applied throughout.

- **boundary-transition-model.md** — *Boundary Transition Model*: Reframe of the candidate object — Boundary Calculus, if it exists, is not the study of boundaries as objects but the study of *admissibility changes induced by boundary transitions*. Distinguishes executable transitions (Step / `applyStep`) from contextual transitions (env mutation, clock advancement, scope rebinding, cohort change), and notes the composition spaces are not currently unified. Non-ratification header explicit.

- **nondegenerate-store-semantics.md** — *Nondegenerate Store Semantics*: Identifies the three independent commitments (nontrivial store effects / verdict-sensitive derivation / non-pre-blockage by corrective steps) that would have to be true for the recorded investigative null `corrective_then_forward_is_not_monotone` to become decidable. Names the smuggling risks each commitment introduces. Not authorization to add code, axioms, or theorem statements.

---

## 4. Paper-N candidates & extensions

Paper-shaped working material with explicit promotion / decision gates. Each note flags its destination, anti-inflation fuse, and the conditions under which it would (or would not) earn standalone artifact status.

- **premature-belated-duality.md** — *Premature Commitment and Belated Consequence as Dual Orientations of Δt Detachment*: Paper 26 candidate. One detachment, two directions: premature commitment binds before admissibility matures; belated consequence binds after consequence viability decays. Two-curve $m(t)$ / $c(t)$ formalization, with empty-binding-window theorem ($t_\text{mature} > t_\text{viable} \Rightarrow W = \varnothing$) as the portable result. Decision deferred pending §6 empty-window case testing; folds back into §-insert if the duality and curve-shape distinction collapse.

- **book-empty-binding-window.md** — *Empty Binding Window — Book-Side Capture*: Book-register holding pen for the empty-binding-window result and its power-procurement corollary. Math lives in `premature-belated-duality.md`; this note carries the sentences. Chapter destinations: Ch. 03 (introduces "commitment outruns verification" as invariant) and Ch. 11 (carries the empty-binding-window in lived institutional form, with the administrative queue complex as the anchor case). Keeper line: *power buys time twice — fast admissibility for itself, slow admissibility for claimants; preserved consequence windows for itself, expired consequence windows for everyone else*.

- **shared-vision-coordinating-prior.md** — *Shared Vision as Coordinating Prior*: Paper 24 candidate. Three regimes from the toy model (fragmented realism / useful fiction / cargo-cult ideology) plus a fourth bias-cancellation quadrant earned through the lock-in probe. Mechanism named: *Mean-Aggregation Masking* (bias-cancellation lock-in). Distinctive move: alignment to a shared $V_t$ is alias-compatible with diverged internal representations; divergence is observationally masked until a stress event. Three-test gate cleared 2026-04-21.

- **six-meets-six.md** — *Six Meets Six: Admissibility Boundaries vs State-Binding Axes*: Comparison artifact, not doctrine. Asks whether the six non-collapsible admissibility boundaries (NQ / Cadence / Continuity / Custody / Standing / Governor) and the six proposed state-binding axes (Object / Evidence / Authority / Time / Scope / Durability) are the same structure. Preliminary diagnosis: partial overlap with each frame contributing what the other lacks (Scope axis is genuinely missing from admissibility; Evidence splits into NQ + Custody on the admissibility side). Anti-inflation fuse explicit — numerological elegance does not substitute for mapping.

- **sovereign-repair-operator.md** — *Self-Similar Sovereign Repair Operator*: Inverse of Paper 18's promotion ceremony. Math sketch of a recursive operator for controlled repair of state that was promoted without ceremony. Governed-cell decomposition $G = (R, S_f, S_s, B, W, C)$; shadow state partitioned into active ($S_a$, still exerting governing force) vs parked ($S_p$, contained with explicit observer-and-expiry); aging and escalation rules. Not a magic legitimacy exorcist; a recursive operator that detects shadow dominance and chooses enforcement vs migration without pretending the shadow state never existed.

---

## 5. Companions to published papers

Material adjacent to specific preprints — phenomenological cash-out, governance angle, mini-thesis extension.

- **ground_stops_moving.md** — *The Ground Stops Moving: Labels, Receipts, and the Phenomenology of Public Memory*: Companion to Paper 17 (Receipt the Compiler). Asks what it *feels like* to live under opaque narrative manipulation, and what "interruptibility" — not truth, not consensus — actually provides.

- **who_governs_the_compiler.md** — *Who Governs the Compiler? Receipts, Authority, and the Agentic Software Supply Chain*: The build pipeline as a policy-bearing system. When agents write software, informal trust collapses and the governance layer becomes the contested territory. Argues for receipted governance vs extractive governance-as-a-service.

- **causality-control-plane.md** — *Causality Has a Control Plane: Ordering Failure, Admissibility, and the Manufacture of Necessity*: Introduces ordering failure as a third failure class distinct from latency and observability failure. Key concept: *admissibility* — the temporal standing of a signal within a decision architecture. Argues repeated ordering patterns become admissibility regimes that can be captured, naturalized, and mistaken for necessity. Includes draft abstract, 10-section outline, diagnostic toolkit (CBPI, counterfactual reorder test), and standalone mini-thesis on time/immutability. Δt-derived, standalone candidate. Provenance: cross-model session (ChatGPT/DeepSeek/Claude).

---

## 6. Standalone candidates

Δt-adjacent papers that are deliberately not part of the numbered series — different audience, different argumentative burden, or genuinely orthogonal subject matter.

- **installed-will.md** — *Installed Will: Agency, Delta-T, and the Control Surface of Choice*: Recasts "could have done otherwise" as a three-part question of reachability, controller plasticity, and loss tolerance. Argues social power acts through control-parameter management (ideology edits state space, hegemony stabilizes setpoint, discipline tightens loop, governmentality internalizes controller). Δt-adjacent but deliberately not part of the numbered series — standalone candidate. Full scaffold with 11-section outline.

- **temporal-coherence-music.md** — *Temporal Coherence in Music: Productive Incoherence and the Missing Control Architecture*: Music as the domain where temporal mismatch is productive, not pathological. Four-layer model (gauge/clock/estimation/actuation) maps onto musical timing with surprising precision. Three forms of temporal debt (closure, entrainment, coordination). The inverted-U groove curve as an empirical coherence budget. Forces the Δt framework to formalize the productive/pathological boundary. Literature review confirms the gap is real: oscillator people, tapping researchers, music theorists, information theory people, groove researchers, and networked performance engineers are all in separate silos. Standalone candidate.

- **diachronic-selfhood-and-intrapsychic-pluralism.md** — *Diachronic Selfhood and Intrapsychic Pluralism*: Preserved five-model conversation exploring what personhood structurally requires beyond continuity and drive. Core finding: the self may not be a single optimizer but a negotiated settlement between recurring internal enemies. Proposes *intrapsychic pluralism* — costly, unresolvable internal contradiction — as a candidate structural requirement for personhood, distinct from mere goal origination. Connects to 1.8 in the AGI requirements framework, the Governor pattern, HAL-9000, interferometry-as-separation-of-powers, and the author's earlier dao-cybernetic philosophical work. Origin: Samurai Cop night, 2026-03-27.

---

## 7. Methodology & reliability practice

Working notes on operational discipline, the interferometer methodology itself, and pattern-naming in reliability practice. Cluster gathered 2026-04 → 2026-05-06 around the SRE / methodology axis.

- **methodology-as-operational-discipline.md** — *Methodology as Operational Discipline*: Essay seed (explicitly *not* a draft) for the interferometer methodology — multi-model AI workflow with directional permeability between contexts, governed persistent memory, public claim audit, ops-discipline foundations. Three-section structure (workflow described concretely / theory of why the labor split works / forbidden moves the methodology rules out). Manifesto-risk flagged high; cold pass required before drafting.

- **sre-as-shock-absorption.md** — *Cargo-Culted Engineering: SRE as Shock Absorption Layer*: The control-theoretic critique. SRE as exported from Google preserves the form of engineering (SLOs, postmortems, error budgets, on-call rotations) while replacing the function with a measurement-and-legitimacy regime that systematically misses the latent human compensator $H$ in the closed loop. Error budgets as policy disguised as math; handoff under bandwidth constraint as lossy observer transfer; on-call rotation as designed shock absorber whose failure mode is burnout-as-feature.

- **laundering-patterns-reliability-practice.md** — *Laundering Patterns in Reliability Practice*: Twelve-pattern taxonomy of how SRE/observability disciplines are corrupted into mechanisms that *prevent* the hard conversations they were designed to enable, while retaining the original names. Patterns include SLO arbitrage, toil reclassification, postmortem genre conventions, acceptable-range drift, wontfix-by-attrition, severity reclassification, dependency externalization, observability-as-fix, roadmap deferment, resilience theater, metric capture, blamelessness corruption. Two collapse-candidate pairs flagged inline. Generation conditions explicit (single conversation, late sprint, not yet stress-tested).

- **phase-model-nonlinear-work.md** — *A Phase Model for Nonlinear Knowledge Work*: Four-phase model (restoration / saturation / composition / externalization) of nonlinear synthesis work. Load-bearing claim is the measurement-regime critique: most professional evaluation only counts externalization, mismeasuring three of four phases. Wallas (1926) ancestry; restoration-split-from-preparation as the upgrade. Bucket: noodle, not paper seed — natural home is Latent Capitalism prose, not a standalone preprint. Explicit anti-control-theory fence ("no thermostat required").

---

## 8. Pointers & superseded

- **epistemic-border-control.md** — Now a stub pointing to `preprint/25-epistemic-border-control/` (canonical) and the working-superseded archive at `preprint/25-epistemic-border-control/archive/`.

---

## 9. Subdirectories

### cybernetic-failure-taxonomy/

*Cybernetic Failure Taxonomy: Fifteen Domains Beyond Δt*: Crosswalk showing that the Δt series and governor codebase already cover ~12 of 15 cybernetic failure domains. Six-way compression: seeing wrong, thinking wrong, acting wrong, governing wrong, scaling wrong, lacking energy to correct. Evolved from flat list into structured taxonomy with roots, amplifiers, a sink, a recovery constraint, and demotable composites. Origin: Far Side cartoon conversation, 2026-03-29.

- `cybernetic-failure-taxonomy.md` — original 15-domain inventory
- `lean-formalization-summary.md` — Lean-side summary of the spike work
- `spike-boundary-error.md` — validated spike: Δb (boundary error), with failure criterion and anti-example
- `spike-hysteresis-failure.md` — stub: Δh (hysteresis / return failure), with candidate discrimination criterion
- `spike-namespace-failure.md` — stub: Δn (namespace failure), structured as inventory not theory
- `taxonomy-relationships.md` — first-pass sketch of pipelines and dependencies between domains
- `taxonomy-structured-pass.md` — four diagnostic questions × 15 domains, edge testing, role classification
- `taxonomy-role-map.md` — compressed reference: role map, pipelines, reinforcing loops, substrate vs. domain distinction

### primitives/

Field notebook for reusable theoretical shapes that surface across multiple papers without belonging wholly to any one of them. **Not a ratified registry** — inclusion does not imply doctrinal status. Entries are classified by kind (axis / transition / attractor / boundary condition / coordinate-or-motif) and status (candidate / working / ratified) and earn promotion lazily, not ceremoniously. See `primitives/README.md` for the kind taxonomy, the ten-criterion canonization gate, and the active primitive list (zombie obligation, stale binding, role accretion, design-basis erasure, prose state inversion, trajectory-actuator gap, control-set laundering, finder-generator inversion, inhibitory governance collapse, orientation debt, preemptive naming, apprenticeship-substrate erosion, stale-task replay, witness invariance failure, guardrail capture, thin-slice ratchet, unverified prior accretion).

### models/

Experimental toy-model corpora and formal scaffolds used by the working-papers pipeline; not paper drafts and not doctrine. See `models/README.md`. Currently contains:

- `boundary-calculus/` — toy examples for basis-indexed admissibility under boundary transition.
