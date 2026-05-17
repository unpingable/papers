# Laundering-Move Watchlist — Execution Pass 1 (2026-05-16)

**Status:** First application pass over Section B of the laundering-move watchlist. Routes named handles into existing primitives, identifies immediate repo-facing audits, and marks which candidates need specimen collection before promotion.

**Parent:** [`laundering-move-watchlist.md`](laundering-move-watchlist.md). This pass uses the watchlist's generator (*artifact with limited standing crosses a boundary into a stronger operational role without earning the transition*) and recurrence gate (*3+ independent specimens / paper load-bearing / existing primitive can't stretch / composition audit names neighbors*).

**Discipline:** Execution should **reduce ambiguity, not create more kingdoms.** No new primitives in this pass. No new Lean modules. No new paper directories. The pass is a router and a gap-finder.

---

## 1. Scope

This pass covers Section B's twelve named-not-promoted handles. For each: route it (into an existing primitive, or as a real gap requiring specimen collection), name the immediate audit target if any, and mark whether the move should be folded, deferred, or promoted for collection.

Out of scope: writing the math leads (separate file: [`laundering-move-math-leads.md`](laundering-move-math-leads.md)); auditing the prose of every existing primitive (only the four that surfaced as repo-facing risks).

---

## 2. Routing table

| Move | Status | Routing decision |
|---|---|---|
| Diagnostic → verdict | **covered** | NumericalAdmissibility + NEAM measurement adapter; no new primitive |
| Concentration → authority | **mostly covered** | Route under Compression Becomes Authority; promote only if HHI-style concentration becomes load-bearing in a non-NEAM specimen |
| Flux → culpability | **covered** | NRAF subcase; asymmetry is evidence, not guilt; explicit guardrail already in NRAF working note |
| Model fit → ontology | **probably covered** | Route under Δt falsification guardrails (model ≠ substrate) and P22 four-layer decomposition (model isn't the system) |
| Optimization → permission | **live gap** | First real candidate; specimen collection target (see § 3.1) |
| Participation → consent | **essay-grade candidate** | Public-facing / Latent-Chrono-Substack-shaped; not Lean yet (see § 3.4) |
| Visibility → accountability | **repo-facing risk** | Audit receipt/log/dashboard language across NQ/AG/Nightshift/Wicket/labelwatch/driftwatch (see § 3.2) |
| Symmetry → fairness | **covered** | NRAF guardrail ("symmetrization is not moral repair"); no promotion |
| Equilibrium → legitimacy | **candidate** | Needs specimens beyond NEAM/stability-as-capture; defer until second instance |
| Prediction → control right | **Governor/Wicket relevant** | Watch closely around agentic-control surfaces; see [`laundering-move-math-leads.md`](laundering-move-math-leads.md) § 4 for the observability/controllability/standing math lead |
| Publicness → harmlessness | **nebgraph / atproto live wire** | Execute as ethics/perimeter audit against `~/git/atproto-nutrition/nebgraph` + civic-migration-appliance + labelwatch/driftwatch (see § 3.3) |
| Receipt → consequence | **fold candidate** | Provisionally fold into Visibility → accountability; revisit only if it bites independently (see § 3.2 footnote) |

---

## 3. Immediate audits

### 3.1 Optimization → permission — *specimen collection*

**Bad crossing:** "It improves the objective, therefore it is allowed."

**Likely live specimens** (to be confirmed by actual repo / corpus pass):

- CI passed → merge is permissible (Wicket-adjacent)
- tests passed → change is safe (Wicket-adjacent)
- benchmark improved → deployment is legitimate (Governor / agentic control)
- engagement metric increased → product change is justified (civic / platform analogues)
- agent achieved goal → action was authorized (P25 / P27 / controller-continuity territory)
- SLO within bounds → user harm is not real (reliability-practice file specimen #1)

**Boundary rule:** *Optimization result is evidence. It is not standing, authorization, consent, legitimacy, or consequence clearance.*

**Section A check:** NumericalAdmissibility forbids numerical-kind → admissibility-kind laundering (closest neighbor), but the optimization shape is specifically *constraint-dropping* rather than kind-confusion. The composition might be: Optimization → permission as a sub-case of NumericalAdmissibility where the metric is an objective function and the missing kind is admissibility. Worth checking after specimen collection.

**Action:** Open a small specimen log at `working/specimens-optimization-permission.md` if a *third* independent specimen arrives (specimen log earns its own file at 3+; staged inline until then).

**Promotion blocker:** Need 3+ independent specimens from different domains (Wicket-CI, agent_gov-benchmark, civic-engagement, agentic-control). Currently **one confirmed**: "CI green → merge permissible" filed as a worked specimen card in [`laundering-move-math-leads.md`](laundering-move-math-leads.md) § 2.1, with Wicket as the canonical correctly-constrained kernel neighbor. Five candidates remain for audit.

### 3.2 Visibility → accountability (+ Receipt → consequence) — *receipt-language audit*

**Bad crossing:** "It was logged / receipted / displayed / observable, therefore accountability exists."

**Existing material that already does this work — DO NOT duplicate:**

- `tooltheory/dashboard-quiet-is-not-recovery.md` — "proxy quiet ≠ substrate recovery" (Nightshift register)
- `tooltheory/consequence-scoping.md` — "evidence may authorize inquiry/caution without authorizing closure"
- `tooltheory/social-telemetry-claim-boundaries.md` — five-claim doctrine for observations → features → findings → claims → public rhetoric ladder
- `tooltheory/labelwatch-driftwatch-admissibility.md` — tool-specific anti-laundering case
- Receipt-doctrine fragments in `admissibility-trajectory-audit.md` (receipt-vs-authority Lean split)

The audit is **routing existing material under a common boundary name**, not generating new prose.

**Audit checklist (surface-level grep + targeted review):**

| Surface | Audit target | Question |
|---|---|---|
| `~/git/wicket` (+ `wicket-guard`) receipts | `Receipt`, `Authorized`, `Accountable`, `Enforced`, `Ensures` | Does any field promote receipt-presence to consequence-presence? |
| `~/git/nq` (+ `notquery`, `nq-witness`) findings | finding-status language | Does "finding logged" carry implicit "finding addressed"? |
| `~/git/agent_gov` gate receipts | gate-pass / gate-fail vocabulary | Does pass-receipt act as authorization rather than as one piece of admissibility evidence? |
| `~/git/atproto-nutrition/{labelwatch,driftwatch}` dashboards | dashboard-as-deliverable language | Does dashboard quiet imply substrate quiet? (Already covered by `dashboard-quiet-is-not-recovery.md` — check for surface compliance) |
| `~/git/nightshift` coordination surfaces | "handled," "covered," "addressed" | Does coordination-presence imply consequence-presence? |
| UI surfaces broadly | "proof," "guarantee," "ensures," "accountable," "verified" | Are these load-bearing claims or evidence claims? |

**Boundary rule (universal):** *Receipt is evidence of an event. It is not enforcement, redress, standing, refusal, or consequence.*

**Receipt → consequence folding note:** Provisionally folded into this section. Both moves enforce the same refusal at type-level: *event-recording ≠ event-consequence*. If a future specimen makes Receipt → consequence operationally distinct from Visibility → accountability (e.g., a system where receipts are *required* for consequence but also *insufficient*, and the laundering is specifically the insufficiency-elision), split them then.

**Lean-worthy only if** code starts letting `Receipt` satisfy an `Authorization` / `Consequence` / `Enforcement` type. The math lead is at [`laundering-move-math-leads.md`](laundering-move-math-leads.md) § 2 (graph-reachability framing).

**Action:** Grep pass across NQ / AG / Wicket / Nightshift / labelwatch / driftwatch source for the audit-checklist vocabulary. Surface findings in this section as they accumulate. No new file until findings warrant.

### 3.3 Publicness → harmlessness — *civic / observatory perimeter audit*

**Bad crossing:** "The records are public, therefore recomposition is harmless."

**Boundary rule:** *Public fragments can become a private intelligence product when recomposed, ranked, clustered, or exported.*

**Existing material with the right posture:**

- `project-civic-migration-appliance` (memory) — local-only, no named exports, no leaderboards, no target discovery
- `tooltheory/social-telemetry-claim-boundaries.md` — already enforces feature ≠ finding ≠ claim → public rhetoric boundary
- `tooltheory/labelwatch-driftwatch-admissibility.md` — observatory-side anti-laundering case

**Audit targets:**

- `~/git/atproto-nutrition/nebgraph` — graph recomposition of public atproto records; primary live wire for this move. Any output that combines fragments across accounts / time / labelers is exactly the recomposition surface the boundary rule names.
- `~/git/atproto-nutrition/{labelwatch,driftwatch,stechometer,atproto-stats}` — observatory-side surfaces; any export / share / publish operation that promotes feature into finding into public claim
- `~/git/atproto-nutrition/reference-labeler` — labeler-side; any recomposition of labels across accounts
- civic-migration-appliance specimens that touch account-level identifiers
- Any leaderboard, ranking, or "interesting accounts" surface — should not exist

**Composition note:** Publicness → harmlessness composes with Concentration → authority (recomposed product can concentrate inference even when no single fragment did) and Visibility → accountability (publication may be presented as the consequence rather than as a new evidence event with its own admissibility).

**Action:** Treat as composition specimen, not new primitive. The boundary rule and existing ethics posture are sufficient prose. Promote only if a recomposition specimen surfaces that the existing posture didn't catch.

### 3.4 Participation → consent — *essay-grade, not Lean-grade*

**Bad crossing:** "They used the system, therefore they accepted the relation."

**Boundary rule:** *Participation under dependency, monopoly, habit, coercion, social necessity, or degraded alternatives is not consent.*

**Existing material partially in this neighborhood:**

- `working/leased-coercion.md` — "ACAB but you need C"; consent-under-coercion architecture
- `project-civic-migration-appliance` — exit cost as consent corruption
- Latent Capitalism / Substack register adjacent

**Likely specimens** (for essay, not specimen-log):

- social platforms (ToS-as-consent fiction)
- gig work (algorithmic management framed as voluntary)
- AI companions (dependency framed as preference)
- workplace surveillance (employment framed as authorization)
- chatbot dependency framed as user preference

**Shape:** Public-facing essay / Substack / Neutral Ambassador surface. Compose with `[[project-compression-becomes-authority]]` and `[[project-leased-coercion]]` rather than minting a new primitive.

**Action:** Defer to writing register. Not a Lean target. If essay surfaces a specimen the existing primitives can't carry, revisit promotion gate.

---

## 4. Deferred / covered moves

- **Diagnostic → verdict, Concentration → authority, Flux → culpability, Symmetry → fairness, Model fit → ontology:** No execution work needed. Routing recorded in § 2.
- **Equilibrium → legitimacy:** Defer until second specimen beyond NEAM (e.g., a political-stability specimen, a market-equilibrium-as-justification specimen from outside transformer/attention work).
- **Prediction → control right:** No prose execution; math lead is the active artifact (see math-leads file § 4).

---

## 5. Promotion blockers

Across this pass, the moves that *could* graduate to primitive status are blocked on:

| Move | Blocker | What would unblock |
|---|---|---|
| Optimization → permission | Zero confirmed specimens; six candidate audit targets | 3+ independent confirmed specimens across distinct domains |
| Participation → consent | No specimen requires new primitive vocabulary | Essay surfaces a specimen existing primitives can't carry |
| Equilibrium → legitimacy | One specimen (NEAM-adjacent) | Second independent specimen |
| Publicness → harmlessness | Existing ethics posture sufficient | Recomposition specimen the posture didn't catch |

No move is unblocked in this pass.

---

## 6. Repo-facing followups

Concrete actions that fall out of this pass:

1. **Grep pass** across `~/git/{wicket,wicket-guard,agent_gov,nightshift,nq,notquery,nq-witness}` and `~/git/atproto-nutrition/{labelwatch,driftwatch,nebgraph,stechometer,reference-labeler}` source for receipt-language audit checklist (§ 3.2). Findings → fold into this file or split into `working/receipt-language-audit-findings.md` if findings warrant.
2. **Specimen log** at `working/specimens-optimization-permission.md` opens when a second independent optimization→permission specimen arrives. Not before.
3. **Composition audit** at math-leads level for Visibility → accountability + Receipt → consequence (see math-leads file § 2) before any Lean tripwire is staged.
4. **Cross-link from `tooltheory/dashboard-quiet-is-not-recovery.md`** to the watchlist's Visibility → accountability entry once that entry has more than the routing line. (Skip in this pass — premature.)
5. **No new working files except the two created in this pass** (this file + math leads). Hold the line.

---

---

## 7. Audit-loop results (2026-05-16)

Two grep passes run against `~/git/{wicket,wicket-guard,agent_gov,nightshift,nq}` (Pass 1) and the same plus `~/git/atproto-nutrition/` (Pass 2). Co-occurrence patterns used rather than the user's raw single-word OR (single-word OR returned thousands of hits dominated by domain vocabulary).

### Pass 1 — Optimization → permission

```
Repos checked:        wicket, wicket-guard, agent_gov, nightshift, nq
Suspicious hits:      0 confirmed specimens
Confirmed specimen?   no
Code confusion?       no (one risk surface flagged; see below)
Follow-up:            retire as "covered in live tools," not just in kernel
```

**What surfaced instead** — anti-laundering doctrine already coded into the live tools:

- `nq/docs/ARCHITECTURE_NOTES.md:122` + `nq/docs/gaps/COVERAGE_HONESTY_GAP.md:186,313` — *"NQ must not let green liveness collapse into admissible evidence."* The move is named at doctrine level, three places.
- `nq/docs/PRODUCT_SURFACES.md:63` — *"CI lies, deploy scripts lie, monitoring probes lie, backup jobs lie. 'Tests passed' is not 'safe to merge'; 'deploy script exited 0' is not 'service healthy'; 'backup ran' is not 'data is recoverable.'"* The exact specimen list, framed as older-than-agents lineage.
- `agent_gov/specs/core/DETECTOR_INTEGRATION_SPEC.md:197` — *"Detector signals can only tighten constraints, never loosen them. A clean coherence score cannot grant new authority — only a dirty one can revoke permissions or demand more proof."* Explicit doctrine-level refusal of Optimization → permission.

**Risk surface flagged (not a specimen):** `agent_gov/src/governor/coherence_budget.py:511` `check_closure_gate(claims, unknowns, threshold, has_human_waiver) → ClosureDecision.ALLOW`. Returns `ALLOW` when `u_t ≤ threshold`. This is `Invariant I` of seven (per `specs/core/INVARIANTS_SPEC.md:194`), so the composition is the constrained version — but the name `ClosureDecision.ALLOW` reads at the call site like a global authorization. If a future change collapsed the seven-invariant composition into "this one check passed → allow," it would be the laundering move in code form. Currently safe by composition discipline; flag for naming-clarity review if any new caller appears that uses `check_closure_gate` alone.

### Pass 2 — Visibility / Receipt → accountability / consequence

```
Repos checked:        wicket, wicket-guard, agent_gov, nightshift, nq, atproto-nutrition
Suspicious hits:      0 confirmed specimens
Confirmed specimen?   no
Code confusion?       no
Follow-up:            retire as "covered in live tools," not just in tooltheory
```

**What surfaced instead** — receipt-doctrine already typed, ordered, and fail-closed across agent_gov / NQ / nightshift:

- `agent_gov/specs/core/PCAR-D.md:19,113,119,581` — *"Every consequential event MUST produce a receipt. Receipts are emitted before or atomically with consequence. There is no silent consequence."* + *"Post-hoc receipt emission (action first, receipt later) violates the 'no silent consequence' invariant."* PCAR-D enforces receipt-before-consequence ordering, which is exactly the anti-laundering shape: a receipt cannot be presented as evidence of consequence after the fact.
- `agent_gov/docs/doctrine/standing_and_receipts.md:28` — *"Every transition that changes force, standing, or consequence must be represented as an explicit receipt with typed parentage."* Receipts are typed, not free-form.
- `agent_gov/docs/adr/0006-governor-called-not-governor-native.md:49` — *"Governor does not natively reason. It performs clerical cognition with closed consequence surfaces... Uncertainty fails closed."* Receipts are evidence; reasoning is elsewhere.
- `nq/docs/ARCHITECTURE_NOTES.md:138` — *"NQ says what kind of trouble reality is reporting; Governor decides what kind of response is allowed."* Receipt-side (NQ) and consequence-side (Governor) split at the tool boundary, not just at the prose boundary.
- `nightshift/tests/horizon_cross_run.rs:438` — *"fresh_arrival with no receipt must fail-closed as Missing"* — fail-closed on missing receipt.
- `agent_gov/libs/mcp_governor/src/mcp_governor/receipt_emitter.py:89` — *"Fail-closed: if receipt write fails, raises (caller must handle)."*

### Aggregate result

**The math finds the boundaries the tools have already drawn.** Both laundering moves the audit was looking for are not just kernel-covered (Section A of the watchlist) — they're enforced at the *live-tool architecture level*, with explicit doctrine prose in agent_gov / NQ specs that uses the same anti-laundering vocabulary the math-leads file does. The kernel-neighbor claim from math-leads § 2 (Wicket is the canonical correctly-constrained operator) generalizes: NQ's "trouble vs. response" split, agent_gov's PCAR-D receipt-before-consequence ordering, and the detector-can-only-tighten doctrine are all the same shape — admissibility separated from optimization, receipt separated from consequence, by design.

**Implications for the watchlist:**

- **Section A is even denser than filed.** NQ-doctrine and agent_gov PCAR-D should be added as kernel-piece entries alongside `NumericalAdmissibility.lean` and `SurfaceAuthorization.lean`. They're not Lean kernel, but they're tool-spec kernel, and they enforce the same refusals.
- **Recurrence gate for Optimization → permission: still at 1/3.** The audit confirmed zero new specimens. The CI-green specimen card in math-leads § 2.1 stays; no second specimen surfaced.
- **Recurrence gate for Visibility → accountability + Receipt → consequence: still at 0/3.** No specimens; existing tooltheory + agent_gov PCAR-D + NQ split + nightshift fail-closed pattern fully covers the boundary.
- **No Lean tripwire warranted.** Neither move needs type-level refusal — the doctrine is already enforced at composition / tool-decomposition / fail-closed levels.

**Lesson on the audit pattern itself:** the user's broad rg keyword list returned dominant noise (single keywords like "gate" / "test" / "threshold" appear in thousands of legitimate uses). The signal lives in *co-occurrence* of evidence-language and authority-language on the same line. Future audit passes should default to the co-occurrence pattern.

### Follow-up actions

1. **Add NQ + agent_gov PCAR-D + detector-integration spec to watchlist Section A** as tool-spec kernel-piece entries (alongside the Lean kernel pieces). Done in a tiny edit, not a new file.
2. **Retire the receipt-language audit from execution-pass § 6 followup #1** — no action needed; tool architecture enforces.
3. **Keep specimen card watch for Optimization → permission** at 1/3 — open a new card if benchmark-improved → deployable or score-above-threshold → permitted surfaces in another tool.
4. **Note `check_closure_gate` naming as a risk surface** — not a specimen, but worth a callout if any new caller uses it standalone.

No new working files. No Lean staged. No watchlist inflation.

---

## Provenance

- Execution-pass structure + routing-table content + four audit framings: ChatGPT, 2026-05-16, in conversation downstream of the laundering-move watchlist filing.
- Audit-loop results (§ 7): claude-code 2026-05-16, two co-occurrence grep passes against `~/git/{wicket,wicket-guard,agent_gov,nightshift,nq}` (+ `atproto-nutrition` for Pass 2).
- Filed by claude-code 2026-05-16; tool-inventory grounded in `~/git/` repos (`wicket`, `wicket-guard`, `agent_gov`, `nightshift`, `nq`, `notquery`, `nq-witness`, `continuity`) and `~/git/atproto-nutrition/` subrepos (`nebgraph`, `labelwatch`, `driftwatch`, `stechometer`, `reference-labeler`, `atproto-stats`). Initial draft scoped tool-search to `~/git/papers/` only and incorrectly excluded `nebgraph`; corrected on operator feedback.
- Companion file: [`laundering-move-math-leads.md`](laundering-move-math-leads.md) — math-side execution pass over the same Section B moves.

---

## Cross-references

- [`working/laundering-move-watchlist.md`](laundering-move-watchlist.md) — parent organizing layer
- [`working/laundering-move-math-leads.md`](laundering-move-math-leads.md) — sibling math execution pass
- [`working/laundering-patterns-reliability-practice.md`](laundering-patterns-reliability-practice.md) — domain-specific specimen catalog (SRE / reliability)
- [`working/tooltheory/`](tooltheory/) — receipt-language and consequence-scoping material already in place
- `~/git/lean/non-reciprocal-admissibility-flow-sketch.lean` § NEAM measurement adapter — Lean tripwire pattern to imitate sparingly
