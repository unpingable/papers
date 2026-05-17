# Laundering-Move Watchlist — Math Leads (2026-05-16)

**Status:** Exploratory math leads / future tripwires. Not doctrine. Not a theorem inventory. Not one Lean module per move.

**Parent:** [`laundering-move-watchlist.md`](laundering-move-watchlist.md). Companion to [`laundering-move-execution-pass-2026-05-16.md`](laundering-move-execution-pass-2026-05-16.md).

**Discipline:** *Math as trap detector, not math as coronation.* For each Section B move, identify the compact formal object that could act as a future tripwire — without pretending to settle the world, and without writing the Lean now. The math is a **lead**, not a **canonization**.

**Promotion gate to actual Lean:** lifted directly from the parent watchlist's Lean-worthy criteria — type-level refusal needed AND classification sharp enough AND no existing kernel piece does the work. The NEAM measurement adapter (`non-reciprocal-admissibility-flow-sketch.lean`) is the working example of what a promoted lead looks like; until any lead below meets all three gates, it stays in this file as prose.

---

## 1. Grid — all twelve moves

| Move | Math family | What it measures | Forbidden promotion |
|---|---|---|---|
| Diagnostic → verdict | Typed evidence/use algebra | Metric role | Metric → judgment |
| Concentration → authority | HHI / entropy / spectral concentration | Influence mass | Concentration → legitimacy |
| Flux → culpability | Schnakenberg entropy production / directed Markov flux | Non-reciprocal flow | Asymmetry → exploitation verdict |
| Model fit → ontology | Identifiability / equivalence classes | Fit under model class | Prediction → essence |
| **Optimization → permission** | **Constrained optimization / admissible set vs objective** | **Objective improvement** | **Optimum → authorization** |
| **Participation → consent** | **Revealed preference under constrained choice sets** | **Feasible alternative structure** | **Use → consent** |
| **Visibility → accountability** | **Graph reachability / temporal logic** | **Receipt-to-consequence path** | **Logged → accountable** |
| Symmetry → fairness | Invariance vs equity constraints | Formal equality | Symmetric form → fair relation |
| Equilibrium → legitimacy | Stability analysis / attractors | Persistence regime | Stable → justified |
| **Prediction → control right** | **Observability vs controllability** | **Epistemic access** | **Prediction → standing to steer** |
| **Publicness → harmlessness** | **Mutual information / recomposition risk** | **Added inferential power** | **Public fragment → harmless product** |
| Receipt → consequence | Event log vs transition system | Recorded event | Record → enforcement |

Five bolded moves get deep treatment: four deep entries (§ 2–§ 5) plus the specimen card at § 7 (Publicness → harmlessness, added 2026-05-16 as the first card where the math does conceptual work rather than confirming existing hygiene). The other seven stay as one-line placeholders in § 6 — promote when a specimen forces investigation.

---

## Entry template

Used for the four deep entries below. Apply to other moves only when warranted.

```
Move:
Math family:
Minimal formal object:
What it can legitimately show:
Forbidden inference:
Candidate theorem / tripwire:
Existing kernel neighbor:
Promotion trigger:
```

---

## 2. Optimization → permission

**Move:** Optimization → permission.

**Math family:** Constrained optimization. The shape is standard:

```
choose x ∈ X maximizing U(x)
subject to A(x)
```

where `U` is the objective and `A` is the admissibility predicate.

**Minimal formal object:** A triple `(X, U, A)` — choice space, objective function, admissibility predicate. The laundering move drops `A` and treats `argmax_X U(x)` as if it implied `A(argmax_X U(x))`.

**What it can legitimately show:** That a particular `x*` maximizes (or sufficiently improves) `U` over `X`, or over the feasible set `{x ∈ X : A(x)}` if `A` is included as a constraint.

**Forbidden inference:** `A(x*)` from `x* = argmax_X U(x)` alone, when `A` was not an explicit constraint and is not a proven invariant of the argmax operation.

**Candidate theorem / tripwire:**

> *Optimality under an objective does not imply admissibility unless admissibility is an explicit constraint of the optimization, or is a proven invariant of the argmax operator over (X, U).*

This is the keeper shape. Type-level encoding (if it ever earns one) would split `OptimizationResult` from `AdmissibilityVerdict` and refuse the coercion.

**Existing kernel neighbor:** `~/git/lean/LeanProofs/Admissibility/NumericalAdmissibility.lean` is the closest — it refuses numerical-kind → admissibility-kind laundering. The optimization shape is a *sub-case* where the numerical kind is "objective value" and the admissibility kind is the missing constraint. SurfaceAuthorization is adjacent but on a different axis (surface presence ≠ surface authorization).

**Promotion trigger:** Code in `~/git/wicket`, `~/git/wicket-guard`, or `~/git/agent_gov` starts allowing an optimization-passed surface (CI green, benchmark improved, score above threshold) to short-circuit an admissibility check that would otherwise be required. At that point: either compose NumericalAdmissibility against the optimization shape, or — if NumericalAdmissibility can't carry it — stage a Lean tripwire here.

**Specimen collection status:** One confirmed (§ 2.1 below); five candidates remain in execution-pass § 3.1. Recurrence gate not yet met (3+ required).

### 2.1 Specimen card — CI green → merge permissible

**Specimen:** "Tests passed (or score above threshold, or benchmark improved), therefore the change is authorized to merge / deploy / actuate."

**Move:** Optimization → permission.

**Limited thing:** A test-suite pass, benchmark improvement, or score-above-threshold result — a value of the objective function `U`.

**Illicit promotion:** Treated as merge authorization, deployment clearance, or admissibility verdict.

**Math lead — the constraint omission, formalized:**

Define:

```
X                = space of candidate changes
U(x)             = test/benchmark/score result for x
A(x)             = admissibility predicate
                   (Wicket's basis × precedence × standing, or
                    equivalent admissibility gate)
```

The licit gate is the *constrained* selection:

```
merge_authorized(x)  :⇔  x ∈ argmax_{x ∈ X | A(x)} U(x)
                              (or, more generally, A(x) ∧ U(x) ≥ threshold)
```

The laundering move drops `A` and uses the *unconstrained* selection as if it were the constrained one:

```
merge_authorized(x)  := U(x) ≥ threshold        -- A(x) elided
```

**Counterexample (the move in a shoebox):**

```
X = {a, b}
U(a) = 10, U(b) = 5
A(a) = false, A(b) = true
```

Then `argmax_X U = a` but `A(a) = false`, so `optimal(x) ⊬ admissible(x)`. The argmax over the wrong set is the laundering.

**Boundary rule:** Green is evidence. Merge authority requires admissibility — for Wicket, that means accounted basis × precedence × standing. Optimization can select **within** admissibility; it cannot *produce* admissibility. The feasible set is load-bearing.

**Existing kernel neighbor:** `~/git/wicket` is the canonical correctly-constrained operator for this move. Its SPEC line *"Wicket may classify and gate. Wicket may not become the source of authority"* is the same boundary stated as a tool-level guardrail. The laundering move is what happens when callers skip Wicket and let CI / benchmark / score act as a substitute gate. `~/git/lean/LeanProofs/Admissibility/NumericalAdmissibility.lean` is the formal-side neighbor (numerical-kind → admissibility-kind refusal).

**Detection pattern (audit handle):** In any tool that gates a mutation on a numerical signal, ask: *over what feasible set is this gate evaluated?* If the feasible set is the unconstrained change-space (every PR, every model, every action) and the gate is a numerical threshold (CI status, benchmark delta, score), the constraint set is elided and the move is live. The fix is either (a) call Wicket (or equivalent admissibility preflight) before the numerical gate, or (b) make the admissibility predicate explicit in the gate's feasible set.

**Lean-worthy?** Not yet. The boundary is already enforced *operationally* by Wicket's existence — when a code path uses Wicket, the constrained selection is in place. A Lean tripwire is warranted only if a code path emerges that allows a `numerical_pass: bool` to satisfy a function expecting `admissibility_verdict: Verdict`, *without* going through Wicket or an equivalent. Audit task (execution-pass § 6 followup #1) is the prerequisite: grep for sites where a numerical signal directly authorizes a mutation. If any such site is found, Lean tripwire becomes worth staging; otherwise the prose boundary plus Wicket's existence is sufficient.

**Does the math clarify, or just look handsome?** Clarifies. Three concrete payoffs over prose-only:

1. **Audit pattern is structural, not vibes-based.** "Find every gate where the feasible set elides admissibility" is a grep target. "CI isn't authorization" is a slogan.
2. **Wicket's role becomes formal, not folklore.** Wicket *is* the constrained operator; calling it *is* including admissibility in the feasible set. The math makes that relationship precise — Wicket is not "the polite thing to do," it's the admissibility constraint reified.
3. **The Lean-worthy gate becomes concrete.** Without the math, "should we Lean this?" is vibes. With it, the gate is: does any code path treat a numerical pass as an admissibility verdict? That's a checkable question.

Specimen card filed. Recurrence gate now at 1/3. Two more independent specimens (e.g., benchmark_improved → deployable, score_above_threshold → permitted) before this graduates from staging.

---

## 3. Visibility → accountability

**Move:** Visibility → accountability (Receipt → consequence provisionally folded in; see execution-pass § 3.2).

**Math family:** Directed-graph reachability / temporal logic over event traces.

**Minimal formal object:** A directed process graph `G = (N, E)` with nodes that include `observation`, `review`, `standing`, `decision`, `consequence` (or domain-appropriate equivalents), and edges = admissible transitions. An event `E` is a node; accountability is a *path* from `E` to a consequence node, not the existence of `E`.

**What it can legitimately show:** Node existence (the event was observed / logged / receipted / displayed).

**Forbidden inference:** Path existence — that the observation reached a consequence — without an explicit reachability check or temporal-logic witness on `G`.

**Candidate theorem / tripwire:**

> *A logged event does not imply accountability unless there exists an admissible path in the process graph from observation to consequence, witnessed at a specified time.*

The temporal qualifier is doing real work: under Δt drift, a path that existed at time `t` may not exist at `t + Δ` (commitment-standing decay; stale-license territory). The tripwire needs to refuse path-existence-at-time-of-observation as a proxy for path-existence-at-time-of-action.

**Existing kernel neighbor:** Receipt-vs-authority Lean split mentioned in `admissibility-trajectory-audit.md`. `tooltheory/consequence-scoping.md` carries the prose version ("evidence may authorize inquiry/caution without authorizing closure"). `tooltheory/dashboard-quiet-is-not-recovery.md` is the specific dashboard-side specimen. `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` is adjacent (surface ≠ authorization, parallel to receipt ≠ consequence).

**Promotion trigger:** Any tool in `~/git/{wicket,agent_gov,nightshift,nq}` or `~/git/atproto-nutrition/{labelwatch,driftwatch,nebgraph}` starts marking a record as `Accountable` / `Resolved` / `Handled` based on logging alone. Until then: prose guardrail in `tooltheory/consequence-scoping.md` plus surface-compliance audit (execution-pass § 3.2) is sufficient.

**Specimen collection status:** Specimens exist (dashboard-quiet-is-not-recovery; social-telemetry-claim-boundaries five-claim ladder). The reason this hasn't been promoted to Lean is that no code path currently *type-confuses* `Receipt` with `Authorization` — the discipline is prose-enforced. Audit will surface whether that's still true.

---

## 4. Participation → consent

**Move:** Participation → consent.

**Math family:** Revealed preference under constrained choice sets (decision theory).

**Minimal formal object:** A feasible choice set `F ⊆ X`, an observed selection `s ∈ F`, and an unconstrained reference set `X` from which `F` was derived under constraints `C` (dependency, monopoly, coercion, exit cost, information, social necessity). The pair `(F, s)` is observable; `(X, C)` is what the laundering move ignores.

**What it can legitimately show:** That `s` is the agent's selection among the alternatives in `F` (subject to the standard revealed-preference assumptions: transitivity, IIA, etc.).

**Forbidden inference:** That `s` is preferred over alternatives in `X \ F`, or that `s` is preferred over the *relation itself* (i.e., that selecting from `F` constitutes consent to `(F, C)` as the licit choice architecture).

**Candidate theorem / tripwire:**

> *Selection from a constrained feasible set identifies preference within the set; it does not identify consent over the unconstrained relation, nor consent to the constraints that produced the feasible set.*

The second clause is the load-bearing one — it cuts the "you used the system therefore you accepted the system" move at the joint.

**Existing kernel neighbor:** `working/leased-coercion.md` ("ACAB but you need C") carries the consent-under-coercion architecture. `project-civic-migration-appliance` carries exit-cost-as-consent-corruption. Neither is a Lean primitive; both are prose-shaped.

**Promotion trigger:** This is unlikely to earn Lean. The move is **essay-grade / public-facing** (Latent Capitalism / Substack / Neutral Ambassador register). Lean entry would require a code path that programmatically infers consent from participation — possible in some governance-tool surface, but not currently named. Promotion to a paper-level claim is more likely than promotion to a Lean tripwire.

**Specimen collection status:** Many specimens (social platforms, gig work, AI companions, workplace surveillance, ToS-as-consent). No specimen requires *new primitive vocabulary*; the work composes `[[project-compression-becomes-authority]]` + `[[project-leased-coercion]]` + a sharp boundary-rule statement. Essay-shaped, not theorem-shaped.

---

## 5. Prediction → control right

**Move:** Prediction → control right.

**Math family:** Observability vs controllability, in the classical control-theoretic sense, with an explicit *standing* axis added.

**Minimal formal object:** A system `(X, f, h)` — state space `X`, dynamics `f`, output map `h`. Observability is the ability to recover state from output history; controllability is the ability to drive state from input. Both are technical properties. **Standing** is a separate axis: the authorization to actuate, distinct from the ability to actuate.

**What it can legitimately show:**

- Observable / predictable: state can be estimated from output history.
- Controllable: state can be steered by input choices.

Both are properties of `(X, f, h)` and the available input/output channels.

**Forbidden inference:** That observability or controllability implies *standing* to actuate. The control-theoretic properties are silent on authority; they describe capability, not licit use.

**Candidate theorem / tripwire:**

> *Observability does not imply controllability does not imply standing. The three are independent axes.*

That's three refusals chained. The first two are textbook (Kalman). The third is the laundering refusal: even *controllability* — full technical ability to steer — does not by itself authorize steering.

**Existing kernel neighbor:** `project-controller-continuity` (sibling axis to admissibility); `project-paper25-candidate` (epistemic border control — where the borders are between observation, prediction, and steering); `project-governor-doctrine` (agent_gov authority-boundary doctrine). The Lean-side neighbor is `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` (capability ≠ authorization, parallel shape to controllability ≠ standing).

**Promotion trigger:** Any code path in `~/git/agent_gov`, `~/git/wicket`, `~/git/nightshift`, or related agentic-control surfaces starts using prediction-quality (model confidence, forecast accuracy, observability score) as an authorization signal for actuation. The move is *especially* live near agentic systems where "the agent can predict X" is one keystroke from "the agent should steer X."

**Specimen collection status:** No confirmed specimens yet but the surface is large and growing. This is the move with the highest *future* tripwire-value across Governor / Wicket / agentic-control work. Watch closely; do not promote until a specific code path forces the type-level refusal.

---

## 6. Other moves — one-line placeholders

These are valid math handles but do not currently earn deep entries. Promote to deep entry when a specimen forces investigation.

- **Diagnostic → verdict:** Typed evidence/use algebra. Already encoded in NEAM measurement adapter; promotion would be a generalization, not a fresh tripwire.
- **Concentration → authority:** HHI / entropy / spectral concentration. NEAM uses HHI on stationary distribution; generalize only if a non-NEAM specimen needs it.
- **Flux → culpability:** Schnakenberg entropy production. Already imported as a measurement in NEAM adapter; the math handle stays as Schnakenberg.
- **Model fit → ontology:** Identifiability / equivalence classes. Route through Δt falsification guardrails and P22 model-vs-substrate distinction.
- **Symmetry → fairness:** Invariance vs equity constraints. NRAF guardrail covers the prose; math handle is invariance group vs equity-constraint set.
- **Equilibrium → legitimacy:** Stability analysis / attractors. Stable points are not justified points; stability can be capture, exhaustion, or coercion. Defer until second specimen.
- **Publicness → harmlessness:** Promoted to § 7 (specimen card with XOR construction). Removed from placeholder list because the math here does conceptual work the prose can't carry.
- **Receipt → consequence:** Event log vs transition system. Provisionally folded into Visibility → accountability (§ 3); split out only if it bites independently.

---

## 7. Specimen card — Public fragments with XOR synergy (Publicness → harmlessness)

Promoted out of § 6's one-line placeholder list because the math here does conceptual work the prose can't carry. The argmax/admissibility shoebox in § 2.1 is correct but lightweight — definitional unfolding dressed up. This card exhibits a *hard counterexample*: even when every individual fragment is public AND each is individually non-informative about a private attribute, the recomposition can be fully informative. That's the boundary the prose alone cannot establish, and it's the case opponents of the publicness boundary will reach for ("but every record is in the public PDS, what's the harm?").

**Specimen:** Public fragments with XOR synergy.

**Move:** Publicness → harmlessness.

**Math family:** Mutual information / recomposition risk.

**Construction:**

Let `A, B ~ Bernoulli(1/2)` be independent random bits. Let the sensitive / private attribute be `S = A XOR B`. Then:

```
I(S ; A)   = 0
I(S ; B)   = 0
I(S ; A,B) = 1 bit
```

Each fragment individually reveals nothing about `S`. Together, they reveal `S` exactly.

**Boundary rule:** *Public fragment status does not imply harmless recomposition. Publicness is not closed under recomposition.*

**Generalization (tripwire shape):**

```
∀i, I(S ; X_i) ≈ 0   does not imply   I(S ; X_1, …, X_n) ≈ 0
```

Individual non-informativeness does not compose. The laundering move *"each input is public, therefore the recomposition is safe"* assumes a closure property that mutual information does not satisfy.

**Existing kernel neighbor:**

- Section A of the watchlist: this move is currently uncovered by Lean kernel pieces. The receipt-doctrine and admissibility kernels do not carry recomposition-risk.
- `tooltheory/social-telemetry-claim-boundaries.md` (observations → features → findings → claims → public rhetoric ladder) is partially adjacent — the recomposition-risk specifically sharpens the feature-to-finding step where the *recomposition itself* is the laundering, not the labeling.
- `project-civic-migration-appliance` (memory) — "evidence crosses, authority does not" — operational sibling on jurisdictional axis; this card is the inferential-product axis.
- The ethics posture for nebgraph / labelwatch / driftwatch (local-only, no named exports, no leaderboards, no target discovery) is the operational response shape; this card is the formal underpinning.

**Why this matters more than the Optimization → permission audit:**

The optimization audit (execution-pass § 7) was a *negative control* — it confirmed existing hygiene, which is correct but not generative. *Useful but not delicious.* This card is a *hard counterexample*: the laundering move can exist in the limit of "everything is public and individually non-informative." That's the limit opponents of the boundary will reach for, and the XOR construction is the answer: composability is not closure under publicness.

**Lean-worthy?** Not yet. The XOR construction is a *math lead* — it exists to be cited as a clean counterexample when a tool surfaces a code path that treats individual-fragment-public as aggregate-recomposition-safe. Promotion trigger: a specific code path in `~/git/atproto-nutrition/nebgraph` (or sibling tools) starts treating *"all inputs are public-record"* as sufficient safety clearance for the recomposed output. Until then, the prose boundary plus this card is sufficient; the math sits on file as the citable response to the public-source defense.

**Specimens to watch for (recurrence-gate candidates):**

- data-broker recompositions claiming public-source provenance as harm exemption
- AI training pipelines arguing that public-internet provenance shifts downstream-harm responsibility to the user
- doxing-via-public-records as a legal / ethical defense
- atproto-side: any tool that combines per-actor public records and presents the aggregate as "just public data, restructured"

**Recurrence-gate status:** This is the first specimen of Publicness → harmlessness. Counts as 1/3 toward primitive-promotion gate. Card stands as recognition vocabulary until a code-path specimen forces type-level refusal.

---

## 8. What this file does not do

- **No Lean files staged.** Promotion to Lean requires the parent watchlist's three-gate test, not the existence of a math handle.
- **No theorem statements canonicalized.** "Candidate theorem / tripwire" entries are prose statements of the keeper shape, not formal claims.
- **No claim that these are the right math families.** Each is a *first lead*; a specimen may force a different handle (e.g., the right tool for Participation → consent might turn out to be game theory rather than revealed preference).
- **No competition with existing kernel.** Each deep entry names its existing-kernel neighbor explicitly; the math lead exists to be checked *against* the existing kernel before any new module is staged.

---

## Provenance

- Grid table + four deep entries' math family / minimal object / candidate theorem framings: ChatGPT, 2026-05-16, in conversation downstream of the laundering-move watchlist filing and the prose execution pass.
- Filed by claude-code 2026-05-16. Tool repo references grounded in `~/git/` inventory (`agent_gov`, `wicket`, `wicket-guard`, `nightshift`, `nq`, `notquery`, `nq-witness`) and `~/git/atproto-nutrition/` subrepos (`nebgraph`, `labelwatch`, `driftwatch`, `stechometer`, `reference-labeler`).
- Discipline framing — *math as trap detector, not math as coronation* — is ChatGPT's, preserved verbatim because it's exactly the right altitude.
- § 7 specimen card (Public fragments with XOR synergy): construction + boundary-rule framing from ChatGPT 2026-05-16, after the audit-loop result confirmed the optimization-side cases were already covered (*useful but not delicious*); promoted because the math here exhibits a hard counterexample rather than confirming existing hygiene.

---

## Cross-references

- [`working/laundering-move-watchlist.md`](laundering-move-watchlist.md) — parent organizing layer; Lean-worthy gate is defined there
- [`working/laundering-move-execution-pass-2026-05-16.md`](laundering-move-execution-pass-2026-05-16.md) — sibling prose execution pass; § 3 audits feed specimen-collection state here
- `~/git/lean/non-reciprocal-admissibility-flow-sketch.lean` § NEAM measurement adapter — the working example of a promoted lead (single move, single tripwire, scope-fenced, attributed)
- `~/git/lean/LeanProofs/Admissibility/NumericalAdmissibility.lean` — closest existing kernel neighbor for several leads (Optimization → permission, Diagnostic → verdict, Concentration → authority)
- `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` — closest existing kernel neighbor for Prediction → control right (capability ≠ authorization shape)
