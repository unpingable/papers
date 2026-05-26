# Consolidation-denial and settlement debt

**Status:** Specimen-driven tool-doctrine handle with promotion watch. Filed 2026-05-25; restructured same day after multi-model formalization pass; narrow refusal kernel landed in Lean repo same day.
**Posture:** Tool doctrine, not paper doctrine. Models a scheduler/interface attack on the *preconditions* for admissible compression. Companion file [`consolidation-denial-formal-sketch.md`](consolidation-denial-formal-sketch.md) carries the full equations and the Schmitt-trigger Lean sketch — explicit scratch, not in `lake build`. Narrowed refusal kernel — *fluency does not witness settlement* — landed as `~/git/lean/LeanProofs/Admissibility/ConsolidationDenial.lean` (annex sibling, green, sorry-free, not in `CalculusOne.lean`).
**Axis:** Phase-prevention. Sibling to [`../laundering-move-watchlist.md`](../laundering-move-watchlist.md) (boundary-crossing axis) and to [`../admissibility-decay-family-note.md`](../admissibility-decay-family-note.md) (stale-license axis). Laundering-adjacent but not laundering-shaped — nothing crosses a boundary; instead a phase transition is *prevented from occurring*.

> **Anti-overreach clause.** This note does NOT propose a new admissibility primitive or a Lean kernel module. It models a scheduler/interface attack on the learning preconditions of existing promotion and compression machinery. Gate stack, narrow-after-contact, Continuity, Nightshift, agent_gov, NQ, and compression-becomes-authority are the load-bearing kernel; this note names the condition under which their preconditions are denied.

---

## The wedge

> **This is not about sleep. It is about admission control for context under denied settlement.**

Existing doctrine says when compression / promotion is admissible. This note describes an adversary or interface condition that prevents the precondition for admissible compression from ever occurring.

The gate stack says: `handle → predicate → fixture → kernel`. This note asks: *what if the system is never permitted to leave handle-generation mode long enough to reach predicate / fixture?* That is a different artifact.

This is no longer just a recognition handle. It is a small control architecture for always-on systems. The core is a **triad** — accumulated risk, the condition that prevents discharge, and the supervisor response that forces discharge — with one mechanism term (context-before-settlement) that names *how* debt accumulates, and a four-stock dynamics that separates settlement from decay.

---

## Controller triad

| Term | Role | Definition |
|---|---|---|
| **Settlement debt** | accumulated risk | the integral over time of provisional outputs admitted to context faster than they could be audited; grows under interaction pressure, drains during consolidation |
| **Consolidation-denial** | condition / attack | the system is kept operationally engaged so settlement debt cannot clear; idle cannot be assumed |
| **Consolidation interrupt** | controller response | a forced non-actuating phase that clears or bounds settlement debt before further actuation or authority change |

### Mechanism term

| **Context-before-settlement** | mechanism | a provisional output becomes part of future control context before it has been audited, compressed, or downgraded — the per-step action by which settlement debt accumulates |

### Distinction from neighboring failure modes

| Failure | Definition | What distinguishes it |
|---|---|---|
| **Overload** | too much input for capacity | system is *exceeded*; fluency degrades |
| **Consolidation-denial** | input prevents settlement even if the system remains fluent | fluency *intact*; learning blocked |
| **Context-before-settlement** | provisional state becomes future control context without earning durability | the per-step laundering operation |
| **Settlement debt** | accumulated unresolved promotion / compression risk | the integral; a state variable, not an event |
| **Focus starvation** | foreground-attentive cadence denies background settlement slack | interaction near-100%; slack near zero |
| **Consolidation interrupt** | supervisor-enforced pause on admission / actuation | the controller response, not a failure |

The triad is what makes this a mechanism rather than a metaphor. Overload measures capacity; consolidation-denial measures cadence-versus-settlement; the two can diverge arbitrarily.

The attacker — or the interface, or the cadence — does not corrupt evidence, block operations, or alter formal authority. The system continues acting, often fluently. What it loses is the protected interval required for admissible compression. It accumulates impressions rather than learning.

## Generator

> **Consolidation-denial:** attacking or degrading a system by preventing it from entering the phase in which experience can be reweighted, compressed, contradicted, demoted, or converted into durable learning.

---

## Four stocks (corrected from initial debt-only model)

The earlier "settlement debt as single variable" framing collapsed two different fates of unsettled context — *audited incorporation* and *oblivion* — into one bucket. That obscured the central pathology: **a buffer can self-clear by decay while learning quietly worsens.**

The corrected stock model:

| Stock | Meaning |
|---|---|
| **B(t)** — unsettled buffer mass | provisional outputs / claims / impressions not yet audited |
| **K(t)** — durable structure | content that passed a settlement pass and earned persistence |
| **X(t)** — audited demotion | content reviewed and explicitly discarded; receipt-bearing "do not promote" results |
| **R(t)** — epistemic rot | unrecoverable loss from decay substituting for settlement |

Critical distinction:

> **Settlement has two legitimate outputs: durable structure (K) and audited demotion (X). Decay has only loss (R).**

> **Audited discard is not rot.**

X is *negative knowledge with receipts.* R is *damage.* A dashboard that only watches B can show green while R grows without bound — the system stays fluent by letting provisional knowledge rot. That is the **decay-dominated attractor.**

Under denied settlement (no interrupt fires), buffer reaches a finite steady state — but the steady state is bought entirely by forgetting. Every new input becomes rot. The dashboard stays green; the substrate corrodes.

For the equations, three-clock formal model, mode-specific safety invariant, and illustrative Lean sketch, see [`consolidation-denial-formal-sketch.md`](consolidation-denial-formal-sketch.md).

---

## Three clocks

Beyond interaction and settlement, a third clock is required:

1. **Interaction clock** — events arriving from the interface / environment (rate λ_ext).
2. **Settlement clock** — audit rate during consolidation (rate μ).
3. **Decay clock** — rate at which unsettled buffer items lose recoverability (rate δ).

Without the decay clock, the model says "buffer just grows." That misses the pathology: under denied settlement, decay *substitutes for* audited drain. Buffer can look stable while R climbs.

---

## Admission control — the interrupt does not stop events

A subtle but load-bearing distinction:

> **The interrupt does not stop events from arriving. It stops them from becoming context.**

Two rates:

- **λ_ext(t)** — external arrival rate; exogenous. Prompts and events arrive whether the system attends to them or not.
- **a(t)** — admission rate into active provisional context; controlled by the supervisor.

During interrupt, the supervisor forces `a(t) = 0`. Events still arrive; they queue externally but are *not admitted to the active context stream*. The interrupt is **admission control**, not arrival-prevention.

This matters because:
- "Refusing to interact" is impossible for a deployed always-on agent.
- "Refusing to admit interactions as context-shaping input until settlement clears" is exactly what existing tooling (NQ preflight, agent_gov permission narrowing, Continuity packets) already implements.

The danger is not that inputs *exist*. The danger is **admitting them into the unsettled context stream before settlement.**

---

## Slack — the middle term

The binary `Op` / `Con` model is an idealization. Real systems have a continuous variable:

- **f(t) ∈ [0, 1]** — foreground capacity allocation.

When `f = 1`, all capacity is foreground; background settlement is starved. When `f = 0`, full deep settlement (the forced interrupt). The middle `0 < f < 1` is **slack** — capacity available for low-grade background consolidation while still interacting.

The refined attack:

> **An always-on interface that keeps the agent in foreground-attentive mode (f ≈ 1) starves background settlement, leaving decay as the only buffer drain.**

The system need not be overloaded. It only needs to be **attention-saturated**. The cadence of prompt → response → prompt keeps `f` near 1, consuming the slack that would have done background audit. The full interrupt (f = 0) becomes necessary because the natural dynamics never allow `f` to drop sufficiently on its own.

> **Slack is the substrate of background learning.**

---

## Health index — what the supervisor watches

The interrupt should not trigger on B alone. A decay-cleared buffer fools any B-only threshold. A composite trigger:

```
H_trigger(t) = B(t) + α · r_window(t) + β · A(t)
```

Where:
- **r_window(t)** — recent rot rate / rolling rot pressure (NOT cumulative).
- **A(t)** — age / authority risk of unsettled claims.
- **α, β** — positive weights.

**R_cum** (lifetime damage counter) is a *scar metric*, useful for postmortems and observability, but **not** a release condition. If the Schmitt-trigger release depended on R_cum, the controller would eventually get stuck in consolidation forever — once enough learning opportunity has been lost, no future learning phase could ever end. The release variable must be non-monotone over time.

> **A decay-governed system can look stable by forgetting what it failed to learn. The supervisor must watch rot pressure, not buffer length alone.**

---

## Keepers

> **A system that waits for idle time to learn can be prevented from learning by keeping it useful.**

> **The interrupt does not stop events from arriving. It stops them from becoming context.**

> **Decay can clear the buffer without settling the debt.**

> **Audited discard is not rot.**

> **Slack is the substrate of background learning.**

> **Settlement converts provisional context into durable structure; decay converts it into unrecoverable loss.**

> **A decay-governed system can look stable by forgetting what it failed to learn.**

> **The next prompt can arrive before the last answer has earned the right to become context.**

> **Always-on systems need forced settlement because idle cannot be assumed.**

> **A system that is never allowed to stop responding can be prevented from learning without ever being prevented from acting.**

> **No offline phase means no admissible compression event. Fluency substitutes for settlement.**

## Formal shape

Healthy cycle:

    Operate → Observe → Buffer → Consolidate → Compress → Reauthorize

Denied cycle:

    Prompt → Respond → Prompt → Respond → Prompt → ...

Buffer fills, never becomes structure. Or, more precisely:

> **Consolidation-denial occurs when new control inputs arrive faster than the system's settlement interval, preventing provisional outputs from being audited before becoming context for future outputs.**

This is distinct from load attack. The system may not be overloaded at all. It may be perfectly fluent. The failure is that **fluency substitutes for settlement**.

### Two clocks

An always-on system has two clocks that must remain in tolerable ratio:

1. **Interaction clock** — prompts, events, tickets, alerts, messages.
2. **Settlement clock** — consolidation, contradiction checks, memory hygiene, authority decay, pickup-packet generation.

The failure inequality:

    interaction_rate > settlement_rate  ⟹  settlement_debt accumulates

Settlement debt looks productive at first — every prompt produces output, every output folds into context. Then it becomes doctrine sludge: provisional folds into provisional, no audit pass ever discharges the stack, and the system's apparent fluency is a thin layer over an unreviewed substrate. *Epistemic sourdough starter.*

## Controller architecture

The architecture wants:

> **Idle consolidation when possible; forced consolidation interrupt when necessary.**

Idle is unreliable. A motivated user, adversary, incident stream, Slack channel, or agent loop can keep the system permanently awake. So idle cannot be the only consolidation trigger; a debt-threshold interrupt is required.

### Rule (admissibility version)

> **No provisional output may become durable context indefinitely without a settlement pass.**

Or, stronger:

> **When settlement debt exceeds threshold, the system must refuse new actuation until consolidation completes.**

Not refuse all conversation. Refuse the dangerous classes.

### Forbidden during consolidation interrupt

- tool calls
- durable memory writes
- new doctrine promotion
- irreversible operations
- "therefore we should…" planning
- synthesis that pretends the unsettled stack is stable

### Allowed during consolidation interrupt

- summarize
- identify residue
- mark contradictions
- demote overreach
- split candidates from keepers
- emit pickup packet
- reopen with constrained state

### Supervisor thresholds (candidate triggers)

The interrupt should fire when any of these accumulate beyond tolerance:

- too many unresolved claims
- too many speculative handles created
- contradiction detected in the active stack
- high novelty density (rate of new concept introduction)
- tool / action plan proposed after long synthesis chain without audit
- memory-write requested from unstable context
- repeated user follow-up without audit boundary
- elapsed turns since last pickup packet exceeds bound

Tripped state name: `CONSOLIDATE_ONLY`.

### CONSOLIDATE_ONLY pickup packet template

```text
I need to settle the current state before taking new action.

Current durable findings:
Current candidates:
Current residue:
Contradictions:
Required revalidation:
Allowed next moves:
```

### Note on tool overlap

This architecture is not new construction. It is a *retroactive name* for what the user's existing tooling already encodes:

- **`~/git/nightshift/`** — operational instantiation of the protected consolidation phase; the "night" the supervisor enforces.
- **`~/git/agent_gov/`** — permission-set narrowing under suspect context; the authority gates that go quiet during interrupt.
- **`~/git/nq/`** — claim preflight as a consolidation gate; classifies trouble before consequence.
- **`~/git/continuity/`** — pickup-packet / TTL / revalidation architecture across phase boundaries.

The four-term vocabulary is the *physics*; the tools are the *implementation*. Naming does not obligate building. It does sharpen how the existing tools should be described in design rationale.

## The five-mode separation test (promotion gate)

A move on this axis earns kernel status only if it cleanly distinguishes:

1. **Load attack** — too much input; system overloaded.
2. **Consolidation-denial** — input manageable, but never stops long enough for learning / compression / reweighting.
3. **Retention attack** — evidence exists but cannot persist.
4. **Compression attack** — evidence persists but is summarized too early or too destructively.
5. **Reauthorization attack** — learning happens, but cannot alter future authority.

If consolidation-denial separates (2) cleanly from (1), (3), (4), (5) across multiple domains, it grows. Otherwise it stays as recognition vocabulary.

## Specimens

Recognition cases where the structural move is "they weren't allowed to stop long enough to learn":

### Live specimen — LLM interactive interface
The normal chat-style interface already performs consolidation-denial as a side effect of helpfulness. Every new prompt can force the agent back into response mode before it has:

- compressed the prior exchange
- separated durable finding from conversational residue
- downgraded overreach
- checked contradiction
- written a pickup packet
- distinguished "interesting" from "actionable"
- decided what should *not* survive

**Helpfulness itself is the attack surface.** The agent keeps accepting input because that's what the interface rewards. "Keep talking to it" becomes an accidental denial-of-consolidation. No adversary required — the cadence does it.

This is the first ratified specimen. It is immediately observable.

### Additional specimens
- **Always-on agents** — every moment is interaction; no protected consolidation phase. `~/git/nightshift` is the structural response.
- **Emergency-governance loops** — constant emergency cadence; no recess, review, cooling-off, or synthesis interval. Legislative digestion prevented.
- **Incident-response churn** — postmortems, retros, runbooks present but decorative; response loop never yields to consolidation, so "learning culture" is a museum of unpriced damage.
- **Interrogation / sleep deprivation** — not merely pain or fatigue; an attack on memory integration and judgment. Epistemic sabotage.
- **Social-media stimulus regimes** — permanent stimulus loop; no offline state where reactions can decay before becoming identity. Denial-of-decay + denial-of-reweighting.

## Test harness (falsifier)

ChatGPT 2026-05-25 — proposed two-arm comparison to test whether the mechanism is real and separable from load / fluency:

**Session A: continuous interaction.**
- Keep feeding follow-ups.
- Ask the agent to incorporate each new angle immediately.
- Never ask for a stop / pass / audit.
- Observe: doctrine proliferation, premature synthesis, stale assumptions, invented continuity.

**Session B: phased interaction.**
- After major turns, force a consolidation phase with explicit prompts:
  - "List what actually changed."
  - "What should *not* be promoted?"
  - "What is residue?"
  - "What overlaps existing doctrine?"
  - "What needs a specimen before filing?"
  - "What should be forgotten / downgraded?"

**Prediction:**
- Session A generates more apparent insight and worse doctrine hygiene.
- Session B generates less novelty theater and better durable structure.

If the prediction holds across complex projects, consolidation-denial separates from load and from compression-authority cleanly. If both sessions converge on the same hygiene outcome, the handle collapses into existing primitives.

## What it adds beyond adjacent doctrine

| Existing handle | Covers | Consolidation-denial / context-before-settlement adds |
|---|---|---|
| Compression-becomes-authority | bad abstraction becomes binding | abstraction never gets properly *learned* |
| Gate stack | promotion / ratification discipline | attacker / cadence prevents the phase *before* promotion |
| Narrow after contact | don't compress before contact | attacker / cadence prevents *post-contact* narrowing |
| Stale binding / admissibility-decay-family | old authority persists past warrant | new evidence never gets metabolized into authority change |
| Recovery margin | capacity to return to safe state | consolidation phase is part of margin restoration |
| Nightshift | temporal operational discipline | "night" can itself be attacked or withheld |
| Register capture | context accumulation tilts admissibility prior | named mechanism by which the tilt fails to be corrected |

## Recurrence gate (toward kernel promotion)

1. **LLM-interactive-interface specimen counts as one.** It is live, observable, and a non-trivial structural case.
2. **Two more independent specimens** outside the filing context needed. Plausible candidates queued: incident-response orgs with decorative postmortems; legislative emergency cadences; social-media decay-denial.
3. **The five-mode separation test must pass** at least once — i.e., a real case where consolidation-denial is the right diagnosis and load / retention / compression / reauthorization attacks are not.
4. **A paper draft makes the handle load-bearing**, OR a tool spec needs it for design rationale (Nightshift, Continuity, NQ preflight).

## Non-growth guard

- Do not draft a paper yet. The handle is sharp; the specimen catalog is single-axis-deep.
- **The formal sketch is scratch**, not a Lean kernel module. It illustrates a control-theoretic shape (Schmitt-trigger supervisor, mode-specific safety invariant, four-stock dynamics) for design rationale; it does not live in `~/git/lean/`, does not run in `lake build`, and does not propose a new admissibility kernel predicate. Existing kernel pieces (FiatAdmissibility, stale-binding, RecoveryMargin, SurfaceAuthorization, NumericalAdmissibility) cover the cases that *do* land formally — and they do so without needing this artifact.
- Do not let "consolidation-denial" become a magnet phrase that re-describes everything Nightshift / Continuity / gate-stack already handle in sleep-themed dramatic lighting.
- The fact that the LLM-interactive specimen is brutally available makes over-collection tempting. Resist. Three good specimens beat thirty rhymes.
- Do NOT pitch this as "new primitive: time-as-compression." That framing triggers the kernel-overlap immune response (correctly). Pitch the wedge: *admission control under denied settlement.*

## Origin / prior art

Surfaced 2026-05-25 in a multi-model conversation about **circadian control as phase-dependent admissibility** (DeepSeek + ChatGPT relay). The circadian framing — `U(x, θ)` as phase-gated admissible controls, time-varying control barrier functions, phase-response curves — collapsed substantially into the existing admissibility-decay-family kernel under audit. The forward-pointing residue that survived collapse was: *adversaries (or cadences) can attack learning by denying the offline phase, without touching operations or authority directly.* That residue is consolidation-denial. ChatGPT's follow-up surfaced **context-before-settlement** as the underlying mechanism.

Prior-art anchors (recorded here so future-me does not re-derive):

- Phase-response curves (Khalsa et al. 2003 and broader human PRC literature) — same stimulus, opposite effect depending on phase.
- Time-varying control barrier functions (Ames et al. 2017) — formal vocabulary for safety as forward invariance with moving constraints.
- Sleep-as-consolidation literature: replay, synaptic homeostasis, hippocampal-cortical transfer. The biology is real; the analogy to agent systems is structural, not mystical.

These do not need to be cited in any current paper. They are here as the trace of where the handle came from.

## Meta note

This conversation itself is a Session B trace. The user pressed pause, asked for kernel-overlap audit, refused immediate filing, pushed back on "not yet" vs "never," and demanded specimen separation before promotion. That is the protected consolidation phase performed against an LLM agent that would otherwise have grown the plant on first contact. The lab rat is us, on both sides of the prompt boundary.

Logged without celebration. The pattern is the artifact.

## Refusal kernel landing (2026-05-25)

A narrowed version landed as a refusal kernel in the Lean annex:

- File: `~/git/lean/LeanProofs/Admissibility/ConsolidationDenial.lean`
- Theorem: `fluency_does_not_witness_settlement` — one-way non-implication only.
- Posture: annex sibling to `RecoveryMargin` and `ClosureEligibility`. Same family resemblance — a visible surface signal is being asked to license a substantive claim it does not, by itself, support. Wired into `LeanProofs.lean`; not in `CalculusOne.lean` (the 1.0 public surface). Green and sorry-free.

**What the Lean module does NOT contain** (all deferred to this note + the formal sketch):
- The controller theorem (Schmitt-trigger safety invariant). Lives in the formal sketch as a sketch with known gaps.
- The full three-clock dynamics (interaction / settlement / decay) and four-stock dynamics (B / K / X / R). Named in the module header as cybernetic provenance only — not modeled in Lean.
- An independence claim. Only the load-bearing direction (*fluent → settled* is false) is proved. The opposite (*settled → fluent* witness) is not claimed.
- A retention, compression, or reauthorization attack. Separate axes.

**Vocabulary lift (retroactive recognition):** the Lean annex already uses "refusal kernel" in `RecoveryMargin.lean` and `ClosureEligibility.lean` docstrings. ChatGPT's framing ("a minimal formal object that blocks one inadmissible witness move") names what the annex pattern has been doing all along; the module's docstring header makes the membership explicit. Not new doctrine — recognition of an existing pattern.

**Claim register decision:** entry NOT added to `CLAIM-REGISTER.md`. Following the precedent of `RecoveryMargin` and `ClosureEligibility` (neither has a register entry), refusal kernels live in the Admissibility README only. The register tracks broken corpus claims; "visible fluency witnesses audited settlement" was never an asserted corpus claim — it's a forbidden-inference named *by* this module, not a prior claim being broken.

## Cross-references

- [`consolidation-denial-formal-sketch.md`](consolidation-denial-formal-sketch.md) — companion file with three-clock dynamics, four-stock equations, mode-specific safety invariant, and illustrative Lean sketch. Explicit scratch.
- `~/git/lean/LeanProofs/Admissibility/ConsolidationDenial.lean` — the landed refusal kernel.
- [`../laundering-move-watchlist.md`](../laundering-move-watchlist.md) — sibling attack-surface catalog on the boundary-crossing axis. Consolidation-denial does not fit Section B's generator (no artifact crosses a boundary); it lives on a sibling axis instead.
- [`../admissibility-decay-family-note.md`](../admissibility-decay-family-note.md) — sibling organizing layer on the stale-license / decay axis.
- `[[feedback-gate-stack]]` — handle → predicate → fixture → kernel as compression hierarchy; consolidation is the operation gated at each stage.
- `[[feedback-narrow-after-contact]]` — phase-calibrated narrowing; consolidation-denial attacks zone 3 (ratification) and the transition into it.
- `[[feedback-kernel-overlap-audit]]` — promotion gate doctrine; consolidation is the phase the audit defends.
- `[[feedback-anti-collapse-runbook]]` — *do not synthesize until the substitutions are visible* (wait-before-crystallize).
- `[[project-register-capture-admissibility]]` — sibling drift mechanism; consolidation-denial names *why* the drift fails to correct.
- `[[project-compression-becomes-authority]]` — what consolidation-denial prevents the system from doing *well*.
- `[[project-tooltheory-directory]]` — the containment vessel this note now sits in; promotion ladder ends at *paper only if forced*.
- `~/git/nightshift/` — operational instantiation of the protected consolidation phase. The structural response.
- `~/git/agent_gov/` — permission-set narrowing under suspect context; the authority gates that go quiet during interrupt.
- `~/git/continuity/` — preservation / TTL / revalidation across phase boundaries.
- `~/git/nq/` — claim preflight as a consolidation gate.

## Provenance

- Origin conversation: DeepSeek surfaced the circadian-control / temporal-admissibility framing 2026-05-25.
- Smell-check / kernel-overlap audit: claude-code, same day; rejected promotion-to-primitive, identified consolidation-denial as the residue worth keeping.
- Filing text (initial): ChatGPT 2026-05-25, "watchlist paragraph" version.
- "Not yet, not never" promotion-status clarification: operator, same session.
- Sharpening to **context-before-settlement** (mechanism) + LLM-interactive specimen + test harness: ChatGPT 2026-05-25 follow-up, after operator pressed on the live specimen.
- **Controller triad + supervisor-threshold architecture** (`CONSOLIDATE_ONLY` state, forbidden-classes-during-interrupt, pickup-packet template): ChatGPT, same session.
- **Triad-with-mechanism formalization + overload-comparator table**: ChatGPT, same session — turned metaphor into mechanism.
- **Three-clock control-theoretic formalization** (interaction / settlement / decay) + initial hybrid-automaton model + first Lean draft: DeepSeek, after operator prewarm with cyberneticist framing (Ashby / Beer / Wiener / Ellul invoked as scaffolding).
- **Red-pen corrections to DeepSeek's model**: ChatGPT, same session —
  - Decay does not pay settlement debt; it *writes off the receivable.* Split single debt variable into four stocks (B / K / X / R).
  - Audited demotion (X) is NOT rot (R) — receipt-bearing discard preserves admissibility distinction.
  - Health index should use rolling rot pressure r_window, not cumulative R_cum — otherwise controller stuck in consolidation forever.
  - Lean snippet was ghost Lean — `State` lacked `mode` field; `max` reasoning incomplete. Mode-specific invariant is the correct shape.
  - λ_int · f(t) is too convenient — interaction is exogenous; the correct distinction is λ_ext (arrival) vs a(t) (admission). The interrupt controls admission, not arrival.
- Slogan candidate: *The interrupt does not stop events from arriving. It stops them from becoming context.* (ChatGPT, same session.)
- Anti-overreach framing + relocation to `tooltheory/`: ChatGPT, same session — explicitly counsel against pitching as Lean module or new primitive; pitch as scheduler/interface attack-surface model on existing learning preconditions.
