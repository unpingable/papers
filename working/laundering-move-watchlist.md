# Laundering-Move Watchlist

**Status:** Candidate working note / organizing layer. Filed 2026-05-16.
**Posture:** Attack-surface inventory, not doctrine. Anticipatory but bounded. Name-early discipline, ratify lazily.

---

## Generator

> **An artifact with limited standing crosses a boundary into a stronger operational role without earning the transition.**

That is the bounded class. The set is open in instances but closed in shape. Recognition fires on the *crossing*, not on the artifact.

This watchlist is not a list of all laundering moves — that is impossible and the wrong frame. It is a **known-bad-boundary-crossing catalog**, organized so that a new specimen trips recognition fast:

- *"Ah. This is diagnostic→verdict laundering."*
- *"This is participation→consent laundering."*
- *"This is concentration→authority laundering."*

The systems-ops analogue: you do not predict every outage; you know cache-staleness, retry storms, partial failure, metric-becomes-target. Bounded class of failure topology, recognized before incident.

## Slogan

> **Explore laundering moves early. Canonicalize only the ones that keep escaping containment.**

That's the gate between haunted zoo and anti-laundering doctrine.

## Compressed-specimen quad

Multi-model relay 2026-05-18, ChatGPT compression of the laundering pattern as it lands at the admissibility boundary:

> *A risk score becomes a refusal.*
> *A story becomes a warrant.*
> *A vibe becomes policy.*
> *A dashboard becomes jurisdiction.*

Each line is a prose specimen of existing Section A / B entries — diagnostic→verdict + numerical-kind→admissibility-kind; narrative→standing; register-narrowness→admissibility-narrowness; visibility→accountability + receipt→consequence. Aphorism-shaped recognition vocabulary, not new primitives.

---

## Entry template

Apply per move when the move earns investigation. Most entries below are seed-level (move + boundary + rhetoric); full template comes later as recurrence justifies.

```
Move:
Limited thing:                  (what has restricted standing)
Illicit promotion:              (the unearned stronger role)
Typical rhetoric:               (the language that conceals the crossing)
Why tempting:                   (the local incentive that makes it look reasonable)
Boundary rule:                  (the correct posture)
Possible measurement:           (what would detect the crossing)
Known specimens:                (where it's been seen)
Lean-worthy only if:            (the promotion gate)
```

---

## Section A — Moves already encoded as kernel primitives

These are not candidates; they are existing kernel pieces re-labeled as laundering moves to surface the family resemblance. Use this section as a routing table: when a new instance arrives, check whether it's already an instance of one of these.

| Move | Existing primitive / kernel piece | What it forbids |
|---|---|---|
| **Proxy → substrate** | `project-compression-becomes-authority` | The score / compression / measure becomes treated as the thing measured |
| **Asymmetric flow → neutrality** | `working/non-reciprocal-admissibility-flow.md` + Lean sketch | Directional state-shaping presented as neutral scoring / feedback / risk |
| **Silence → revocation** | `working/signal-authority-candidate.md` | Missing ACK / timeout / null treated as verdict |
| **Stale license → current authorization** | `working/commitment-standing-decay-candidate.md` | Rhetorical continuity used to launder operational revocation |
| **Testimony → self-theory** | `project-testimony-vs-self-theory` | Admitting a witness's report ≠ admitting their preferred self-narrative |
| **Local validity → global validity** | `working/local-global-validity-gap.md` | Locally-valid composition presumed globally valid |
| **Register narrowness → admissibility narrowness** | `project-register-capture-admissibility` | Conversation register treated as prior over admissible world-states |
| **Missing action → physics** | `project-control-set-laundering` | Actions absent from controller-set treated as impossible-in-principle |
| **Surface → authorization** | `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` | Presence of a surface treated as authorization to bind through it |
| **Numerical kind → admissibility kind** | `~/git/lean/LeanProofs/Admissibility/NumericalAdmissibility.lean` | Numerical / metric kinds treated as admissibility verdicts |
| **Diagnostic → verdict (Π / HHI)** | NEAM measurement adapter in `non-reciprocal-admissibility-flow-sketch.lean` (2026-05-16) | Diagnostic measures self-promote into admissibility verdicts / authority grants |
| **Optimization → permission (tool-spec)** | `~/git/agent_gov/specs/core/DETECTOR_INTEGRATION_SPEC.md:197` ("detector signals can only tighten constraints, never loosen them"); `~/git/nq/docs/ARCHITECTURE_NOTES.md:122` ("NQ must not let green liveness collapse into admissible evidence") | Score / pass / metric grants authority instead of acting as constraint or evidence |
| **Receipt → consequence (tool-spec)** | `~/git/agent_gov/specs/core/PCAR-D.md` (receipt-before-consequence ordering; no silent consequence); `~/git/nq/docs/ARCHITECTURE_NOTES.md:138` ("NQ says what kind of trouble reality is reporting; Governor decides what kind of response is allowed") | Receipt presence presented as consequence presence, or receipt emitted after consequence to launder a silent action |
| **Optimization → permission (canonical operator)** | `~/git/wicket` (admissibility preflight; dimensional verdict basis × precedence × standing; "Wicket may classify and gate. Wicket may not become the source of authority") | Calling code skips Wicket and uses CI/benchmark/score as substitute gate |

That's fourteen existing kernel pieces, each enforcing a specific boundary-crossing refusal. Anti-laundering kernel already in place is denser than it looks from outside — eight Lean-side, six tool-spec / tool-architecture (added 2026-05-16 after audit-loop confirmed agent_gov and NQ have the refusals coded as live doctrine, not just as kernel claims).

---

## Section B — Moves named, not promoted

ChatGPT's 2026-05-16 seed list, lightly trimmed and cross-referenced. These are candidate handles, not primitives. None has its own Lean module; some overlap partially with Section A entries.

| Move | Limited thing | Illicit promotion | Cleanest existing neighbor |
|---|---|---|---|
| **Diagnostic → verdict** | metric or signal | judgment / failure declaration | NEAM measurement adapter; NumericalAdmissibility |
| **Concentration → authority** | attention share / mass | legitimacy / governing right | compression-becomes-authority (object axis); HHI section in NRAF |
| **Flux → culpability** | asymmetry of flow | exploitation claim | NRAF (asymmetry ≠ exploitation; needs Q4 surface-neutrality) |
| **Model fit → ontology** | predictive fit | claim about essence | Δt falsification guardrails (model isn't substrate) |
| **Optimization → permission** | objective improvement | authorization | none direct; Goodhart-adjacent; candidate |
| **Participation → consent** | use of the system | acceptance of the relation | leased-coercion (consent-under-coercion); candidate |
| **Visibility → accountability** | log / receipt / dashboard | actual consequence loop | observability-as-fix (#8 in reliability-practice file); receipt-vs-authority Lean split |
| **Symmetry → fairness** | formal symmetry | substantive fairness | NRAF guardrail ("symmetrization is not moral repair") |
| **Equilibrium → legitimacy** | system stability | justification | NEAM-adjacent; stability can be capture / exhaustion / coercion |
| **Prediction → control right** | epistemic access | operational standing | controller-continuity (sibling axis) |
| **Publicness → harmlessness** | public data | safety of recomposition | privacy-adjacent; civic-migration-appliance fragments; specimen card with XOR construction at `laundering-move-math-leads.md` § 7 (recurrence-gate 1/3) |
| **Receipt → consequence** | record of event | enforcement of consequence | sibling of visibility→accountability; receipt-doctrine adjacent |
| **Schedule → standing** | scheduled execution / cron firing | license to bind / authority for the action to matter | commitment-standing-decay-candidate; admissibility-decay family. Keeper (cron fossil, 2026-05-19): *Schedule is not standing.* — "this ran" laundering into "the world was in a valid state for it to run." |
| **True particular → whole-judgment warrant** (prosecutorial decomposition) | hedge / qualifier / fragment within a governing claim (the *particular*) | freestanding warrant for whole-object judgment, without the bridge-rule that would license the lift | `working/prosecutorial-decomposition.md` + `working/prosecutorial-decomposition-specimens.md` (filed 2026-05-21). Old evidentiary genus, platform-industrialized. Lineage anchor: prosecutor's fallacy (close cousin, not parent — PF is probability inversion, PD is broader fragment-to-whole laundering). Five-bridge taxonomy as spine: *materiality / representativeness / causality / sufficiency / standing*. Cousin of attack-surface-laundering (argument-geometry inverse). Keeper: *A true fact can still be inadmissible for the use being made of it.* Lean deferred — kernel candidate is broader `FragmentEvidence/BridgeRule/UnauthorizedLift` machinery, pending SurfaceAuthorization-reduction audit. |
| **Public label → environmental instrument** (label backflow) | descriptive classification term (label as metadata) | operational instrument inside the classified environment — badge, recruitment surface, enforcement convenience, identity infrastructure | `working/label-backflow.md` (filed 2026-05-21). Five-step dynamic (admin label → public circulation → adversarial uptake → identity crystallization → classifier contamination). Stakes anchors: TESCREAL (soft), NVE (hard). Failure modes: badge adoption / catchall expansion / stigma laundering / recruitment surface / false coherence / enforcement drift / adversarial rebranding. Keeper: *A label that can be read by its target can be used by its target.* Prior art audit required before promotion: Hacking's *looping effects of human kinds*, Callon/MacKenzie performativity. Sibling family with prosecutorial decomposition: both name objects acquiring authority/standing through unearned circulation steps. |
| **Control-path capture** (captured checker / dependent monitor) | checker whose sensing, power, logic, control, or refusal path is reachable from the checked party | admissible-check status / counterpower claim / "this is independent" certification | `working/tooltheory/control-path-independence-candidate-2026-05-29.md` (filed 2026-05-29). Architectural-laundering sibling of temporal revocation. Three-axis decomposition load-bearing: only *independence* is static-graph-checkable; *standing* (track record) and *coupling* (does the interlock have teeth) are orthogonal invariants unverifiable at this layer. Failure-mode taxonomy from the DeepSeek parallel-loop seed: 4 of 6 modes derivable from independence violations (service domestication / carrier capture / compliance-checkbox substitution / authorization composing); 2 of 6 stay as explicit obligations (loss-of-standing; welded-breaker). Keeper: *A parallel loop that shares the captured loop's sensors, memory, power, or interlock logic is not parallel — it is a decorative branch of the same controller.* Load-bearing product warning: any "Independent: PASS" verdict that does not declare standing and coupling as `NOT TESTIFIED AT THIS LAYER` is the stuck-at-safe failure mode it is supposed to detect. Lean module `Admissibility.ControlPathIndependence` reserved by name; build gated on consumer forcing case (NQ / Wicket / Governor refusal of a captured-checker claim). Cleanest existing-neighbor kernel-side anchor: `Derivation.BasisDerivation` open instance slot. |

Sixteen handles. Several have strong existing-neighbor matches — those should be checked for whether the existing primitive *already covers the move* before any new handle gets minted. Treat the handle column as recognition vocabulary, not as new doctrine.

---

## Section C — Systems-failure-mode bestiary

ChatGPT's analogy table 2026-05-16. Pure diagnostic device: when a laundering move has the *shape* of a familiar ops failure, name the analogue to accelerate recognition. Not a claim that the social move is the technical failure.

| Systems failure mode | Laundering analogue |
|---|---|
| Stale cache | Old premise treated as current warrant |
| Health check lies | Receipt / log treated as actual accountability |
| Metric becomes target | Diagnostic becomes optimization objective (Goodhart) |
| Retry storm | Repeated weak evidence treated as convergence |
| Split brain | Rival registers each claim exclusive authority |
| Clock skew | Evidence valid in one Δt treated as valid in another |
| TOCTOU | Claim checked under one condition, acted under another |
| Backpressure ignored | Refusal / defer signal treated as advisory noise |
| Partial failure | Local success reported as global validity |
| Schema drift | Same term keeps name while meaning changes |
| Privilege escalation | Observation right becomes mutation right |
| Cache stampede | Attention collapse masquerading as consensus |
| Circuit breaker bypass | Exception path becomes normal authority |
| Lock contention | Procedural bottleneck mistaken for legitimacy |
| Replay attack | Prior authorization reused after standing expires |

Diagnostic-only. Not a taxonomy promotion. The analogy table is allowed to be imprecise as long as it accelerates recognition; do not formalize the mapping.

**Cited fossil (2026-05-19):** the *Privilege escalation* row's canonical historical specimen is SNMP — *the same channel that observes state must not silently acquire standing to mutate it.* The SNMP management-plane is the worst-case fossil for what happens when observation and mutation share one vocabulary; the row is the abstract shape, SNMP is the worked example. Also surfaced in `authority-observable-not-constructible.md` (sealed-mint discipline) and `StateTransition.lean`'s `PolicyStore` trapdoor (only `Step.amendPolicy` may touch policy, even with mutation standing).

---

## Recurrence gate

A move in Section B graduates toward Section A (kernel primitive) only when:

1. **Three+ independent specimens** arrive outside the filing context. Same posture as NRAF's "sixth spontaneous domain instance" rule.
2. **A paper draft makes the handle load-bearing.** If communication of a claim requires the handle and no existing primitive carries it, promote.
3. **An existing primitive can't be stretched to cover the new specimen.** If the closest neighbor in Section A composes cleanly, the move is a sub-case, not a sibling — file it under the parent.
4. **Composition audit names which existing primitives the new move interacts with.** No orphan kingdoms.

If none of these fire over the move's natural lifetime, the entry stays as recognition vocabulary in the watchlist. That is the success state, not failure.

## Lean-worthy gate

A move earns a Lean encoding only when:

1. **The boundary needs type-level refusal.** Specifically: a function in the codebase risks accidentally treating the limited thing as the stronger role, and a type-level barrier would catch the misuse mechanically.
2. **The classification table is sharp enough to encode.** If the categories are still drifting in prose, Lean will solidify the drift.
3. **No existing kernel piece does the work.** Audit `NumericalAdmissibility.lean`, `SurfaceAuthorization.lean`, and `FiatAdmissibility.lean` first — most measurement-vs-authority refusals belong there.

The NEAM measurement adapter (added 2026-05-16 to `non-reciprocal-admissibility-flow-sketch.lean`) is the working example: tripwire-only encoding, scope-fenced explicitly, not in lake build, attribution preserved.

---

## Non-promotion guard

- **Do not create one Lean module per laundering move.** That is exactly the haunted-spreadsheet failure mode. Most moves stay as prose handles.
- **Do not let Section B inflate.** Twelve handles is already at the upper edge of useful. Adding entries should require a specimen, not a brainstorm.
- **Do not let Section C become precise.** It's an analogy table. Forcing rigor onto the ops↔social mapping converts diagnostic into doctrine.
- **Do not treat the watchlist as exhaustive.** The set is open in instances; the watchlist enumerates currently-recognized boundary-crossings, not all possible ones.

---

## Cross-references

- [`working/laundering-move-execution-pass-2026-05-16.md`](laundering-move-execution-pass-2026-05-16.md) — first prose execution pass; Section B routing, four immediate audits (Optimization → permission, Visibility/Receipt, Publicness, Participation), promotion blockers, repo-facing followups
- [`working/laundering-move-math-leads.md`](laundering-move-math-leads.md) — sibling math execution pass; grid + four deep entries (Optimization → permission, Visibility → accountability, Participation → consent, Prediction → control right); *math as trap detector, not coronation*
- `working/laundering-patterns-reliability-practice.md` — one domain's twelve specimens (SRE / reliability engineering). Domain-specific catalog *under* this watchlist; the twelve SRE patterns are mostly instances of moves above (notably observability-as-fix = visibility→accountability; metric capture = diagnostic→verdict + concentration→authority; acceptable-range drift = schema drift analogue).
- `working/cybernetic-failure-taxonomy/cybernetic-failure-taxonomy.md` — adjacent but different cut. The taxonomy classifies *failure types* (perception / model / control / governance / scale / metabolic); this watchlist classifies *boundary-crossing moves*. Orthogonal axes.
- `project-admissibility-decay-family` (memory) — superclass for stale-license primitives; sibling organizing layer at a different altitude (decay-axis specifically).
- [`working/tooltheory/consolidation-denial.md`](tooltheory/consolidation-denial.md) — sibling attack-surface handle on the *phase-prevention* axis (filed 2026-05-25, relocated to `tooltheory/` same day with companion formal sketch). Not in Section B because its generator differs: nothing crosses a boundary; instead a phase transition is prevented from occurring. Companion mechanism: *context-before-settlement.* Four-stock dynamics (B / K / X / R) separates audited demotion from rot. LLM-interactive interface is the live specimen.
- `project-compression-becomes-authority` (memory) — Section A entry with the most-developed prose (scouting essay form).
- [`working/governance-kernel-scope-correction.md`](governance-kernel-scope-correction.md) § "The diachronic layer" — the **diachronic dual** of this watchlist. This watchlist catalogs *synchronic boundary-crossings* (recognition fires on the crossing); that note catalogs *cultivation tells* — engineered input histories that make a crossing honestly pass (`LocallyAdmissibleDoesNotDischargeTrajectory`). Pattern-over-acts, not a single crossing; key on observable patterns, never intent. Kept there (not inflated into Section B) since its generator differs.
- `~/git/lean/non-reciprocal-admissibility-flow-sketch.lean` § NEAM measurement adapter — the working example of a Lean tripwire for a single laundering move; pattern to imitate (sparingly) if any other move earns Lean encoding.

---

## Provenance

- Generator framing + initial 12-move list + systems-failure analogue table: ChatGPT, 2026-05-16, in conversation following the NPC Alex NEAM piece and the appended Lean tripwire.
- Filed by claude-code 2026-05-16 as an organizing layer, with kernel-overlap audit confirming Section A entries already exist as primitives and Section B handles do not yet warrant promotion.
- Slogan: "Explore laundering moves early. Canonicalize only the ones that keep escaping containment." (ChatGPT, same session.)
