# Where Admissibility Fits — Candidate Shapes

**Status:** working inventory.
**Not a roadmap. Not commitments. Not public positioning.**

This file records candidate project shapes, adapter ideas, sibling-repo tweaks and paper leads surfaced while drafting [where-admissibility-fits.md](where-admissibility-fits.md).

The companion application map explains how outsiders can recognize the work.
This file records doors noticed during that mapping.

Most items here will not be pursued.
Some may become specs, papers, adapters or sibling-repo issues.
Many are just named so they stop haunting the operator.

**Per-item schema:** five fields, no essays. *Register / Why it matters / Why not now / Natural owner / Revisit when.* If an item starts wanting more than five lines of substance, it's outgrown this file and belongs as its own working note or spec.

**Origin:** 2026-05-09 multi-model brainstorm (claude-code-papers / claude-agent-governor / claude-nq) synthesized through chatty.

---

## Tweaks to existing siblings

### Lean-checker shadow for Wicket
- **Register:** Wicket / formal verification
- **Why it matters:** kernel small enough (~1.4k LOC) to Lean-check; two implementations of one doctrine says more than "we wrote it down"
- **Why not now:** no forcing case; Lean cluster (Authority/StateTransition/Derivation/Execution/Corrective) still settling
- **Natural owner:** AG floor + claude-code-papers (Lean side)
- **Revisit when:** Lean cluster stabilizes, or a Wicket-side issue surfaces that the shadow would catch

### WASM component for Wicket
- **Register:** Wicket / deployment shape
- **Why it matters:** in-process gate, no IPC; lets the kernel ride into runtimes that refuse sidecars
- **Why not now:** deployment surface before conformance story risks premature productization
- **Natural owner:** AG floor
- **Revisit when:** a specific runtime asks for it, or conformance story stabilizes

### Conformance-suite framing for Wicket
- **Register:** Wicket / external standard
- **Why it matters:** SPEC + fixtures + multiple implementations turns "ratification surface" into something others can work against
- **Why not now:** premature without a second implementation in motion
- **Natural owner:** AG floor (kernel) + claude-code-papers (SPEC discipline)
- **Revisit when:** Lean-checker shadow earns

### LSP-shaped admissibility server
- **Register:** Wicket / editor surface
- **Why it matters:** AG daemon already at long-running JSON-RPC; editors consume admissibility verdicts the way they consume typecheck
- **Why not now:** editor-integration market for admissibility currently empty
- **Natural owner:** AG floor
- **Revisit when:** an editor/IDE consumer asks for it

### Lift WIF-composition vocabulary into NQ
- **Register:** NQ / vocabulary fold-in
- **Why it matters:** NQ adapters already do WIF-composition without naming it; explicit vocabulary (declared $D_i$, $D_A$, regime intersection, threshold accumulation) makes discipline composable across adapters
- **Why not now:** nothing structural — most "earned" item; probe just stabilized
- **Natural owner:** NQ floor
- **Revisit when:** now (status: ready when NQ has bandwidth)

### Aggregator-contamination handling for NQ adapters
- **Register:** NQ / adapter discipline
- **Why it matters:** structured place to declare the aggregation rule's own perturbation surface; load-bearing for eval and supply-chain adapters
- **Why not now:** no specific adapter forcing the issue
- **Natural owner:** NQ floor
- **Revisit when:** bundle with the WIF-composition vocabulary lift

### Aggregate-WIF Lean staging
- **Register:** Lean / formal staging
- **Why it matters:** three target theorems already named in the WIF-composition probe — Lemma 1 foundational, Lemma 3/4 counterexamples
- **Why not now:** no forcing case or paper home
- **Natural owner:** claude-code-papers (Lean side)
- **Revisit when:** paper draft needs the formalization, or counterexample becomes strategically useful

---

## New project candidates

### Eval admissibility layer
- **Register:** cross-sibling / new
- **Why it matters:** "the eval passed" treated as authority; evals are witness systems with contamination basis, regime, aggregator $D_A$. Whole paper/product wound.
- **Why not now:** owner ambiguous; probably wants paper before code home becomes legible
- **Natural owner:** TBD — NQ extension, Wicket adapter, or new project
- **Revisit when:** the LLM self-consistency paper below lands

### Conformance suite as published standard
- **Register:** cross-sibling / external boundary object
- **Why it matters:** Wicket conformance suite framed as published external standard rather than internal discipline; externally visible boundary object
- **Why not now:** needs a second implementation first
- **Natural owner:** AG floor + claude-code-papers
- **Revisit when:** Lean-checker shadow earns

---

## Paper-writing candidates

### Distributed-systems consensus + correlated failures
- **Register:** paper / vocabulary fold-in
- **Why it matters:** existing case studies (Jepsen, S3 us-east-1, CrowdStrike, log4j, Fastly); WIF-composition supplies formal frame. Vocabulary-and-keepers heavy, light on new theorems
- **Why not now:** P25/P26/P27 cluster not settled
- **Natural owner:** claude-code-papers
- **Revisit when:** cluster settles, or an outage in the news creates a forcing case

### LLM self-consistency / multi-agent debate critique
- **Register:** paper / hot-topic critique
- **Why it matters:** keeper *self-consistency is not corroboration* has polemic teeth; field making textbook Lemma 3 errors at scale
- **Why not now:** same queue issue; publication timing matters before the field's vocabulary calcifies
- **Natural owner:** claude-code-papers
- **Revisit when:** P25/P26/P27 cluster settles, before the field self-corrects

### "Where Admissibility Fits" public compression
- **Register:** paper / app-map → front-page seed
- **Why it matters:** eventual unpingable front page seed
- **Why not now:** per chatty — *let the paper repo absorb the weirdness and see which mappings survive repeated explanation*
- **Natural owner:** claude-code-papers (compression) + AG (consistency check)
- **Revisit when:** mappings stabilize across several explanations to outside readers

### Admissibility-kernel reverse-gap frontiers (Lean-first; Drive/Control as paper-frontier)
- **Register:** Lean frontier notes + paper-frontier candidate
- **Why it matters:** AGI requirements doc reverse-pass surfaced four real frontiers where the kernel doesn't yet deliver what the doc demands. Load-bearing wound is **admissibility ≠ safety bridge** — kernel says actions are authorized, not that authorized actions are safe. *Authorized garbage is still authorized.* Three frontiers are Lean-first (safety bridge, belief coherence, non-self-modification of binding layer); Drive/Control Tension is paper-frontier first.
- **Why not now:** First-pass discipline is *frontier notes, not theorem claims* (no sorry stubs); second-pass is *minimal counterexamples before positive theorems*; positive theorems wait for the third pass. Sequence runs by dependency order (load-bearing first), not tractability order.
- **Natural owner:** claude-code-papers (Lean side, frontiers 1-3); paper companion candidate for Drive/Control (frontier 4) deferred until conceptual work surfaces the right primitive.
- **Revisit when:** the Lean frontier notes' first-pass becomes second-pass (counterexamples land); OR a paper draft needs the safety-bridge primitive; OR the AGI requirements doc gets a citation pass and the Lean companion needs to be ready. **Filed at `~/git/lean/FRONTIERS.md` (2026-05-10).**

### Loop Capture (synthesis-shaped paper candidate)
- **Register:** paper / synthesis across spine
- **Why it matters:** adversarial-mechanism formalization of why P22 / P25 / P27 / admissibility family / WIF-composition rhyme; the admissibility layer (*authorized wrongness*) is the differentiator from Boyd / reflexive-control / Goodhart prior art. Working note at [loop-capture.md](loop-capture.md).
- **Why not now:** P25/P26/P27 cluster not settled; position question open (standalone P28 / P22 reframe / spine-integrating synthesis); reflexive-control prior-art posture needs careful framing to avoid Reviewer 2 ambush
- **Natural owner:** claude-code-papers
- **Revisit when:** P25/P26/P27 cluster settles AND position question (a/b/c) decided

---

## Cross-cuts between siblings

Connections surfaced by the brainstorm — not projects, just places where one sibling's machinery should know about another's. Kept brief by design.

- **Receipts as admissibility-claims with $D_A$.** AG receipts are themselves witness aggregators (caller-asserted + system-derived + provenance composed into one verdict). The aggregation rule has a perturbation surface. Worth a pass on whether the receipt format makes $D_A$ legible.
- **NQ Prom adapter discipline ≅ WIF-composition discipline.** NQ already does what WIF-composition formalizes. Bidirectional payoff: NQ gets a formal frame; WIF-composition gets a forcing case for the open audit-operationalization question.
- **Wicket-as-kernel + AG-as-elaborator ≅ Lean kernel + Lean elaborator.** Architectural pattern, not a project. Surfacing the analogy tells PL/formal-methods readers what discipline AG is borrowing.
- **NQ "cannot-testify" ≅ Wicket "openFinding".** Same structured-non-answer move at different layers (witness vs verdict). Worth a pass on whether vocabulary should align across the cabinet, or whether the layer distinction is doing useful work.
- **Boundary calculus / admissibility-cybernetics / receipt doctrine family.** Three-way conceptual family naming the standard normative-control-system shape: transition rules, regulation rules, evidence rules. *Boundary calculus decides what changes at the crossing; admissibility-cybernetics decides whether the crossing may control anything; receipt doctrine decides what survives the crossing as evidence for future crossings.* Family is currently asymmetric on the papers side: boundary calculus has a working corpus at [models/boundary-calculus/](models/boundary-calculus/) (seven examples, status *toy corpus / non-doctrinal*); admissibility-cybernetics has the new interpretive note at [cybernetics-and-admissibility.md](cybernetics-and-admissibility.md); receipt doctrine is named-but-unfiled — don't manufacture the third sibling note until a forcing case appears. Revisit when receipt doctrine starts being used across multiple docs/specs, or when boundary calculus earns standalone primitive promotion.
  - **Binding Reconciliation annotation (2026-05-10).** Operator-facing handle for the triad already present across Lean machinery (`Authority` + `StateTransition` + `Execution` via `AuthorizedStep`) and receipt persistence: *execution is not completion; a binding transition must reconcile action, authority, and consequence.* Likely the conceptual spine of receipt doctrine if/when that sibling is written. Status: pressure increasing on receipt doctrine, no forcing case yet. **Not a new primitive** — operator-facing gloss over existing machinery, not new structure. Surfaced from a joke about "triple-ledger accounting" that turned out to have shape; chatty proposed *Binding Reconciliation* as the cleaner handle (avoiding the accounting/blockchain naming swamp where triple-entry already lives). Captured here so the keeper isn't lost; not promoted because the structure is already implemented in Lean and parked under receipt doctrine — minting a new primitive would be the gloss eating its own substrate.

---

## Deliberate non-pursuits

Doors named, then closed. If a forcing case ever appears, the closure is a position to argue against, not a default to slide past.

- **Wicket-as-policy-DSL** — OPA/Rego gravity well; the LOC tripwire is doing load-bearing work
- **Wicket-as-MCP-server** — SPEC §2 already names this as a non-goal; transport-coupled service shape is wrong for the kernel
- **Smart-contract precondition gate** — doctrine probably doesn't survive contact with on-chain incentive design
- **Insurance underwriting / claims adjudication** — useful for *borrowing vocabulary*, not for being
- **Spec-led hardware verification harness** — shape fits, institutional fit doesn't
- **Build-system gate (Bazel/Nix-shaped)** — real shape match, but Bazel's institutional position means actual integration would be enormous

---

## Re-prune triggers

Look at this list again when:

- Lean-checker shadow earns a forcing case (would unlock conformance-suite framing)
- A specific outage or ML safety thread creates a forcing case for the distributed-systems or LLM self-consistency papers
- NQ has bandwidth for the WIF-composition vocabulary lift
- An external implementer asks "where do I start" — push the conformance-suite framing
- The where-admissibility-fits.md app map gets compressed for the front page (re-sort against whatever framing wins)
- Six months pass with no movement on any item — prune aggressively, don't drift

## Provenance

- 2026-05-09 multi-model brainstorm (AG / NQ / papers-lean) → chatty synthesis → claude-code-papers organized into this inventory.
- Initial draft was rich-annotation; trimmed 2026-05-09 (same session) to fixed five-field schema per chatty's *do not let the candidate file become the most interesting document*. Annotations preserved where the cabinet/owner signal pays for itself; cut everywhere else.
- Filed as working inventory. Companion to where-admissibility-fits.md; one-way cross-link (candidate file knows about the app map; reverse link deliberately omitted to keep the app map clean for eventual front-page compression).
