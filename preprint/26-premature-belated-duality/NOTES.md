# Paper 26 — Working Notes

## Status

**v0.0-stub — 2026-04-28.** Scaffold only. Substantive content lives in `working/premature-belated-duality.md`. Book companion (`working/book-empty-binding-window.md`) carries the prose-narrative version.

## Decision deferred

This could become:

1. Paper 26 proper.
2. A §-insert in Paper 15 or Paper 22.
3. Standalone working note.
4. A book chapter (likely *Chronopolitics*).

Promotion gate: §6 empty-window case testing produces concrete instances; curve-shape / operating-point distinction does not collapse under scrutiny.

## Anti-inflation fuse

From the working note: the parts already exist in the corpus. What is new is (1) the explicit duality, (2) the two-curve formalization, and (3) the empty-window condition. If these three don't earn their keep, fold back to §-insert.

## Position in the series

- P22: no universal plant clock (regulation outruns plant).
- P23: non-self-identical controller (controller-layer masking).
- P24: shared vision coordinating prior (aggregation-layer masking).
- P25: epistemic border control (target unsensed; substitution forced) — *spatial* sibling.
- P26: premature/belated duality (temporal seam fails) — *temporal* sibling.

## Working note pointers

- Primary: `working/premature-belated-duality.md`
- Book companion: `working/book-empty-binding-window.md`
- Cross-reference for binding-event six-tuple: `working/six-meets-six.md` (partial-overlap analysis with admissibility-family six)

## Empty-window promotion gate

**Status: candidate gate material; not yet promoted into draft.**

P26 earns paper status only if the empty-window condition distinguishes cases that the existing Δt papers would otherwise blur. This section sharpens the gate above ("§6 empty-window case testing produces concrete instances") with a working taxonomy and a four-condition promotion test, neither yet ratified.

### Working definition

An empty-window failure occurs when, under the admissibility rules of a given binding regime, no time satisfies both admissibility maturity and consequence viability:

$$W = \{ t \mid m(t) \geq \theta_m \land c(t) \geq \theta_c \} = \emptyset$$

Note the relativization to a binding regime: emergency power, injunctions, provisional holds, precautionary rules, and kill switches are not "solutions" within the original window — they are *regime changes* that alter $\theta_m$, preserve $c(t)$, or create temporary consequence-holding authority. Empty-window failure is a property of the regime, not of the universe.

### Candidate empty-window types

1. **Natural-latency empty window.** The evidence needed to act legitimately cannot arrive before the consequence window closes. Examples: environmental exposure where causality can only be proven after irreversible harm; medical/public-health signals where statistical confidence matures after the intervention window; infrastructure degradation where root-cause proof arrives after lock-in. Cleanest formal case — nobody needs to be evil; reality is rude.

2. **Procedural empty window.** The institution's admissibility process takes longer than the consequence horizon. Examples: court review after demolition/deportation/merger/firing/eviction/data-deletion; public-comment periods after procurement is functionally locked; audit findings after budget authority has expired. Sharpened framing: *procedure can preserve legitimacy by consuming the time in which legitimacy could still attach to consequence.*

3. **Manufactured empty window.** Power manipulates the curves: compresses its own admissibility, preserves its own consequence, slows others' admissibility, or accelerates others' consequence decay ("power buys time twice"). Chronopolitics gravity well — belongs in P26 as a downstream case, not the spine, otherwise the paper drifts into "power bad with clocks."

4. **Ontological empty window.** The system does not recognize the binding event type until after the consequence-bearing moment has passed. Examples: labor harms recognized only after employment classification settles; algorithmic discrimination recognized only after enough affected cases accumulate; infrastructure burden recognized only after "temporary" deployment has become operational dependency. Strongest bridge to admissibility-family work — the event type itself becomes nameable too late.

### Four-condition promotion test

**Superseded by sharpened candidate (see "Ratification-candidate sharpened test" below). Retained as historical record of the pre-sharpening state.**

A candidate case should satisfy all four:

1. Binding would have consequence only before time $t_c$.
2. Binding becomes admissible only after time $t_m$.
3. $t_m > t_c$.
4. Changing the relation requires changing the authority/process/event class, not merely improving execution.

If ordinary process improvement can create overlap, the case is probably a *belated-process failure*, not an *empty-window failure*. The fourth condition is the discriminator — without it, every slow institution becomes an empty-window example, which is the failure mode that turns this from a primitive into slop.

### Ratification-candidate sharpened test (2026-05-04)

**Status: ratification candidate after end-to-end case-test exercise** in `CASE_TESTS.md`. Six cases run (climate, FDA, Brasília, pre-registration, Sarbanes-Oxley, platform-worker classification); test refined through compression pass, sharpening pass, and ontological breaker. Not yet ratified — held items below remain open.

#### 1. Revised condition #4

> **Residual event-class mismatch.** Within the specified counterfactual regime, the residual gap that survives feasible execution improvement (intake, automation, staffing, portal integration, surveillance throughput) is closable only by changing authority structure, entitlement definition, burden of proof, consequence timing, or event class.

Conditions 1–3 unchanged from the superseded version.

#### 2. Counterfactual regime selection rule

> A case must declare the regime under which condition #4 is evaluated. The default regime follows the claimed sub-type. Natural-latency and ontological cases default to any-feasible-configuration; procedural and manufactured cases default to the prevailing authority/incentive regime. Overrides are allowed only when the case explains why the default regime misstates the source of the residual gap.

#### 3. Compact subtype matrix

| Claimed sub-type | Default regime | Feasible execution improvement (per-subtype shorthand) | Override burden |
|---|---|---|---|
| Natural-latency | Any feasible configuration | Measurement, modeling, early warning, faster response | Show the latency is institutionally produced, not physical/causal |
| Procedural | Prevailing authority/incentive regime | Staffing, intake, automation, portal integration, queue redesign | Show reforms are predictably reconstituted by the regime |
| Manufactured | Prevailing authority/incentive regime | Procedural improvements plus anti-gatekeeping reforms attempted in the jurisdiction | Show the delay is not reproduced by interested authority |
| Ontological | Any feasible configuration | Better detection, classification, review, documentation | Show the missing event class already exists and only execution lags |

The third column is per-subtype shorthand. Underlying per-regime feasibility specification (status-quo bounded by political durability; any-feasible bounded by physical/technological possibility) lives in `CASE_TESTS.md` § Sharpening pass.

#### 4. Anti-cosplay enforcement (how the rule + matrix prevent regime-shopping)

The selection rule and matrix are enforced by three layers that prevent authors from picking the counterfactual that produces their preferred classification:

1. **The sub-type claim is itself accountable.** An author cannot pick "natural-latency" to get the any-feasible default unless they can defend the case as physically/causally produced. The override burden in the rightmost column is the test the claim must survive — and the same defense applies in reverse if the author is *justifying* a sub-type claim that determines a favorable regime.
2. **The default regime locks once sub-type is claimed.** Sub-type determines regime; the author cannot pick sub-type based on which regime they prefer without paying the override burden.
3. **Overrides carry a specific argumentative burden, not a general "I prefer this regime" license.** The override-burden column names the specific move required. The case has to argue, on its own facts, that the default regime misstates the source of the residual gap.

The mechanism is not airtight — a determined author can still cherry-pick by misclassifying the sub-type. But misclassification is now a falsifiable move (specific burden, specific case facts) rather than a hidden judgment call. Without this enforcement layer, the matrix becomes bespoke classification laundering with better typography. The framework's job is not to make all judgment go away; it is to make the judgment visible enough to audit.

#### 5. Ontological clarification

The ontological override burden ("show the missing event class already exists and only execution lags") requires "exists" to mean **codified-and-operative-as-binding-event**, not merely conceived or proposed. Without this disambiguation, the matrix produces inconsistent classifications on cases where reform is in motion but not complete (the platform-worker test case, post-2017 California cohort). With the sub-clause: pre-2014 platform workers stay ontological; post-2017 California reclassifies to manufactured.

The companion framing (per chatty mid-pass) is: closure of an ontological case requires *making a new binding event operative*, not improving execution within the existing one. This prevents the any-feasible regime from accidentally swallowing event-class creation as ordinary execution improvement.

#### 6. Held refinements (candidate, not promoted)

- **Sub-type-by-phase.** Cases can transit sub-types over time (Case 6's pre-2014 / post-2017 split). The matrix currently treats sub-type as a per-case property; it may need to handle sub-type-by-phase explicitly. One case-domain shows the transit; promotion requires a second.
- **Politically-reproduced empty-window** (candidate child of manufactured). Two cases (Brasília, SOX/complex fraud) share an adversarial-closure shape distinct from one-time engineered slowness, where reform measures are reconstituted by interested parties through alternative gating mechanisms. Promotion would slot it as a manufactured child with its own override burden ("show the slowness is inertial rather than adversarially renewed"). Held until a third confirming case or a counter-case (manufactured-but-not-politically-reproduced).

Both held items are candidate, not promoted. The matrix above (with anti-cosplay enforcement) is the standing ratification candidate; promoting either held item would require modifying it.

### Provenance

Taxonomy and four-condition test from chatty's structural pass, 2026-05-03. Sharpened test (revised #4, regime selection rule, matrix, anti-cosplay enforcement, ontological clarification, held refinements) from claude-code's case-test exercise plus chatty's mid-pass nudges, 2026-05-04, documented in `CASE_TESTS.md`. Recorded as candidate gate material per name-early discipline; ratification deferred pending override-burden standard-of-evidence sharpening and additional ontological / politically-reproduced cases.
