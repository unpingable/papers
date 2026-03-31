# Taxonomy Structured Pass: Four Questions × 15 Domains

**Status:** Systematic diagnostic. Testing each domain against Chatty's four questions, then testing untested edges.

---

## The Four Questions

1. **Independent?** Can this arise on its own, or does it usually require prior failures?
2. **Generative?** Does it mostly generate downstream failures, or mostly describe an end-state?
3. **Invertible?** Is it ever a beneficial mechanism under the right sign?
4. **Primitive?** Does it name a primitive failure mode, or a recurrent bundle of other modes?

---

## Perception Domains

### Δo — Observability Failure
*Can't see own state, or sees a fake proxy*

| Question | Answer |
|---|---|
| Independent? | **Yes, but also induced.** Sensor failure is independent. But Δb → Δo is common: the boundary excludes what matters, so observability is aimed at the wrong thing. Two flavors: broken sensor vs. sensor pointed at wrong target. |
| Generative? | **Strongly generative.** Can't see → model drifts (Δm), gain miscalibrated (Δg), can't detect authority drift (Δw). Almost everything downstream gets worse. |
| Invertible? | **Yes.** Deliberate non-observation: privacy boundaries, information firewalls, need-to-know. Not seeing everything is sometimes correct scoping, not failure. |
| Primitive? | **Primitive.** Clear, single mechanism. |

**Role: Root/generative.** Can arise independently, spawns many downstream failures.
**Therapeutic inversion: deliberate opacity / privacy / information scoping.**

### Δs — Signal Corruption
*Channel between world and controller is distorted*

| Question | Answer |
|---|---|
| Independent? | **Yes.** Goodhart dynamics, performative reporting, propaganda — these can arise without prior failures. Someone decides to game the metric. That's an independent act, not a downstream symptom. |
| Generative? | **Generative.** Δs → Δm → Δg is a clean pipeline. Corrupted signal causes model drift causes gain mismatch. |
| Invertible? | **Partially.** Signal filtering, noise reduction, lossy compression — these are deliberate signal modification that serves the controller. But they're not really "corruption under the right sign." More like: signal *shaping* is healthy, signal *distortion without the controller knowing* is Δs. The failure is the deception, not the modification. |
| Primitive? | **Primitive.** Distinct from Δo (Δo = can't see; Δs = can see but what you see is wrong). |

**Role: Root/generative.** Independent origin, feeds the perception-to-model pipeline.

### Δn — Namespace / Semantic Failure
*Can't name the thing happening to it; vocabulary lags reality*

| Question | Answer |
|---|---|
| Independent? | **Yes — arguably the most independent.** Namespace gaps aren't caused by other failures. They're caused by the world changing faster than vocabulary, or by the vocabulary never having existed for that phenomenon. This is genuinely upstream. |
| Generative? | **Strongly generative.** Δn → Δb (can't name → wrong boundary), Δn → Δo (can't name → can't categorize observations), Δn → Δm (can't name → model can't represent), Δn → Δh (can't name the baseline → can't recognize non-return). Feeds almost everything. |
| Invertible? | **Tricky.** Deliberate ambiguity? Strategic vagueness? These exist (diplomatic language, constructive ambiguity in treaties) but they're not really "namespace failure under the right sign." They're more like Δn *tolerance* — accepting that some things shouldn't be named yet. The inversion might be: premature naming can be its own failure (ontology forcing, Paper 11). So the therapeutic inversion of Δn is actually knowing when *not* to name. |
| Primitive? | **Primitive and root-level.** Single, clear mechanism. No upstream dependencies. |

**Role: Root.** The deepest generative failure. Meta-failure: makes other failures harder to diagnose.
**Therapeutic inversion: constructive ambiguity / restraint from premature naming.**

### Δm — Model Drift
*Internal model no longer matches environment*

| Question | Answer |
|---|---|
| Independent? | **Weakly.** Usually downstream of Δs (bad signal), Δo (can't observe), Δn (can't categorize), or Δb (wrong boundary). But Paper 7's Δt-constrained inference is a genuinely independent cause: the model drifts because there isn't time to update it, even when signals and naming are fine. So: independent under time pressure, usually dependent otherwise. |
| Generative? | **Moderately.** Δm → Δg (wrong model → wrong gain), Δm → Δa (wrong model → wrong intervention layer). But it doesn't spawn framing or governance failures — it's contained to the control layer. |
| Invertible? | **Yes.** Deliberate model simplification — ignoring known complexity to maintain actionability. Every useful model is "wrong" in the Δm sense; the failure is when the drift is *unrecognized* or *consequential*. |
| Primitive? | **Primitive but weakly independent.** It names a real mechanism, not a bundle. But it's usually a symptom of upstream perception failures. |

**Role: Transmission.** Sits between perception and control. Translates upstream perception failures into downstream control failures.
**Verdict: Keep, but reclassify from "perception" to "transmission." It's the bridge, not the origin.**

---

## Control Domains

### Δg — Gain Mismatch
*Controller too hot or too cold for environment*

| Question | Answer |
|---|---|
| Independent? | **Yes.** A controller can simply be miscalibrated without upstream failures. Tuned for one environment, deployed in another. No perception or naming failure required. |
| Generative? | **Weakly.** Δg mostly describes an end-state in control behavior. If gain is wrong, the output is wrong — but it doesn't typically *cause* other failure domains. It causes bad outcomes, not cascading domain failures. |
| Invertible? | **Yes, trivially.** Gain tuning is the whole point of control theory. Hot gain = fast response. Cold gain = stability. The "right" gain is context-dependent. |
| Primitive? | **Primitive.** Classic control theory concept. |

**Role: Operational / terminal.** Mostly an end-state. Independent origin, low downstream propagation.

### Δa — Actuation Mismatch
*Knows what's wrong, interventions too weak / blunt / wrong layer*

| Question | Answer |
|---|---|
| Independent? | **Yes.** You can diagnose correctly and simply lack the right tools. No upstream failure required. |
| Generative? | **Low.** Δa mostly describes "can't act effectively." It doesn't spawn other failure domains — it just means the current failure doesn't get fixed, which eventually feeds Δh (persistence). |
| Invertible? | **Not really.** Hard to see a beneficial version of "has the wrong tools." Constraint-based design (deliberately limiting actuation options) exists, but that's scoping, not mismatch. |
| Primitive? | **Primitive.** Clear, single mechanism. |

**Role: Operational / terminal.** Independent, non-generative.

### Δk — Coupling Mismatch
*Too tight (cascade) or too loose (no coherent response)*

| Question | Answer |
|---|---|
| Independent? | **Yes.** Coupling is an architectural property, not a downstream symptom. Systems are built with coupling — sometimes it's wrong. |
| Generative? | **Moderate.** Δk → Δx is a real edge: wrong coupling at one scale causes cross-scale destabilization. Tight coupling enables cascades. |
| Invertible? | **Yes.** Tight coupling enables fast coordination. Loose coupling enables modularity and fault isolation. Both are design choices with tradeoffs, not inherently pathological. |
| Primitive? | **Primitive.** Engineering concept, well-defined. |

**Role: Operational, but with one important downstream edge (→ Δx).** More generative than Δg or Δa.

---

## Governance Domains

### Δw — Write-Authority Drift
*Temporary exceptions gain durable governing power without legitimate promotion*

| Question | Answer |
|---|---|
| Independent? | **Yes.** This arises from the structure of exception-handling itself, not from upstream failures. Someone gets temporary authority; nobody revokes it. That's a governance mechanism failure, not a perception or naming failure. |
| Generative? | **Yes.** Δw → Δc (authority drifts → consequences detach from the now-illegitimate authority). Δw → Δh (drifted authority normalizes). |
| Invertible? | **Interesting.** Deliberate authority delegation with sunset clauses is the healthy version. The failure isn't delegation — it's the absence of revocation. So the therapeutic form is: temporary authority *with* active return mechanisms. |
| Primitive? | **Primitive.** Paper 18 established this as a distinct, well-defined mechanism. |

**Role: Governance root.** Independent origin in the authority layer, generates downstream governance and persistence failures.

### Δc — Consequence Detachment
*Authority, action, and consequence stop cohabiting*

| Question | Answer |
|---|---|
| Independent? | **Rarely.** Almost always downstream of something: Δb (wrong boundary → consequences route outside), Δw (authority drifts → consequences no longer track authority), or Δn (can't name the consequence pathway). Can it arise alone? Maybe in very simple cases (decision-maker is physically removed from impact zone), but even that is arguably Δb. |
| Generative? | **Moderately.** Δc → Δh (detachment normalizes). But mostly Δc describes an end-state in the governance layer rather than generating new failure types. |
| Invertible? | **Yes.** Deliberate consequence buffering: limited liability, insurance, diplomatic immunity. These are *intentional* consequence detachment that serves a function. The failure is when it's *unrecognized* or *unaccountable*. |
| Primitive? | **Primitive mechanism, but usually a symptom.** The mechanism (authority ≠ consequence) is distinct and real. But it's downstream more often than not. |

**Role: Downstream / custody.** Mostly receives from Δb, Δw. Describes a governance end-state.
**This is the one Chatty predicted: Δc is downstream more often than upstream.**

---

## Scale / Recursion Domains

### Δx — Scale Inversion
*What stabilizes one scale destabilizes another*

| Question | Answer |
|---|---|
| Independent? | **Sort of.** It's a property of multi-scale systems, not a failure in any single component. But it requires some upstream failure or intervention to trigger — it's what happens when a correct-at-one-scale action hits a scale boundary. So: not caused by prior *failures* exactly, but not self-originating either. It's a *system property* that activates when interventions cross scales. |
| Generative? | **Yes, but as amplifier.** It doesn't create new failure types — it takes whatever failure or intervention exists and inverts its sign at a different scale. Amplifier/inverter, not generator. |
| Invertible? | **Yes.** Multi-scale stabilization exists: interventions deliberately designed to be coherent across scales. Paper 1's coherence criterion is basically the therapeutic form of Δx. |
| Primitive? | **Primitive, but more "system property" than "failure mode."** It's not a mechanism that breaks — it's a geometric fact about multi-scale systems. |

**Role: Amplifier.** Chatty was right — Δp and Δx both belong in the amplifier/transmission category, not as roots. Δx amplifies whatever crosses a scale boundary.

### Δr — Recursion Capture
*Feedback loops feeding mostly on own outputs*

| Question | Answer |
|---|---|
| Independent? | **Can be, but often downstream of Δp.** If the reward sign is correct, recursion is self-limiting (negative feedback). Recursion capture usually requires either Δp (inverted reward) or Δs (corrupted signal that makes the loop look productive). Independent case: echo chambers where the recursion *is* the product. |
| Generative? | **Yes.** Δr → Δw (recursive loop captures authority), Δr → Δm (loop's outputs become the model's inputs, so the model converges on the loop's reality). |
| Invertible? | **Yes.** Recursion is the basis of all learning. Feedback loops feeding on own outputs = practice, rehearsal, skill acquisition when the sign is right. Δr failure is recursion *without external correction signal*. |
| Primitive? | **Primitive.** Distinct mechanism, well-defined. |

**Role: Can be root or downstream.** Independent when the recursion IS the system (platforms, echo chambers). Downstream when it's enabled by Δp or Δs. Generative — can spawn authority and model failures.
**The Δr → Δw edge Chatty flagged is real:** recursive loops can capture authority. Paper 20 (frame capture) → Paper 18 (unauthorized durability) is this pipeline.

---

## Metabolic Domain

### Δe — Energy / Maintenance Deficit
*Knows what to do, lacks surplus to do it*

| Question | Answer |
|---|---|
| Independent? | **Yes.** Resource depletion is an external constraint, not caused by other cybernetic failures. You can have perfect perception, naming, boundaries, and governance — and still lack the energy to act. |
| Generative? | **Yes, in a specific way.** Δe doesn't cause *new failure types*. It prevents *correction* of existing failures, converting them from recoverable to permanent (→ Δh). It's a failure-persistence amplifier. |
| Invertible? | **Not exactly.** "Having energy" isn't the therapeutic inversion of Δe — it's just... not failing. Slack, surplus, reserves — these are the *absence* of Δe, not its beneficial form. Unlike Δh (which has a genuine healthy form in stabilization), Δe doesn't have a "good version of energy deficit." |
| Primitive? | **Primitive.** Single mechanism, well-defined. Paper 9 covers this as capacity-constrained stability. |

**Role: Constraint / persistence enabler.** Not a root in the causal sense (doesn't distort perception or framing). Root in the constraint sense (can't be fixed by fixing other failures — you just need more energy). Feeds Δh specifically.
**Reclassify from "root" to "constraint."** It's not upstream of other failures the way Δn is. It's orthogonal — a resource constraint that determines whether other failures are recoverable.

---

## Persistence Domain

### Δh — Hysteresis / Return Failure
*Can't return to sane baseline after triggering condition is removed*

| Question | Answer |
|---|---|
| Independent? | **No.** Δh is always downstream. Something else caused the shift; Δh is the failure to return. It requires a prior failure or trigger plus a persistence mechanism. |
| Generative? | **Yes, but laterally.** Δh → Δn (normalized state overwrites vocabulary for baseline — Chatty's "book-ish" edge). Δh → Δc (non-return hardens consequence detachment into permanent structure). Δh doesn't generate new failure *types* so much as it *locks in* existing failures and then erodes the ability to recognize them. |
| Invertible? | **Yes — this is the strongest therapeutic inversion in the taxonomy.** Hysteresis as stabilization: anti-flap, damping, regime persistence against transient noise. The governor's `hysteresis.py` is literally this. Same mechanism, opposite sign. The failure criterion from the spike: pathological when the persistence mechanism is self-referential rather than environment-referential. |
| Primitive? | **Primitive.** Clear mechanism, sharp failure criterion (from the Δh spike). Not a bundle. |

**Role: Universal sink + lateral generator.** Receives from everything. Generates lateral effects (Δh → Δn, Δh → Δc) by normalizing what should be temporary. Best therapeutic inversion in the taxonomy.

---

## Cross-Cutting Domain

### Δp — Polarity Inversion
*Reward/punishment sign flips; system punishes correction, rewards concealment*

| Question | Answer |
|---|---|
| Independent? | **Yes, but with a caveat.** Polarity inversion can be deliberately imposed (perverse incentives, institutional reward structures) — that's independent. But it can also emerge from Δr (recursion captures the reward signal) or Δs (corrupted signal flips the apparent sign). So: sometimes root, sometimes downstream. |
| Generative? | **Strongly generative.** Δp → Δr (inverted sign makes loops self-reinforcing), Δp → Δg (controller calibrated to wrong sign), Δp → Δs (system starts generating signals that confirm the inverted polarity). |
| Invertible? | **The whole domain is about inversion.** The "therapeutic" version is: deliberately inverting reward to break a pathological pattern (contrarian strategies, creative destruction, "do the opposite"). But that's more of a hack than a stable mechanism. |
| Primitive? | **Primitive.** Single mechanism: sign flip. |

**Role: Reclassify from root to root/amplifier hybrid.** When it arises independently (imposed perverse incentives), it's a root. When it emerges from recursion or signal corruption, it's downstream. Either way, it's strongly generative. Chatty was half-right: it amplifies, but it can also originate.

---

## Untested Edges

### Δm → Δb (model drift causing boundary error)
**Verdict: Weak edge.** If your model drifts, you might draw boundaries based on the drifted model — but that's a stretch. More commonly, Δb is upstream of Δm: wrong boundary → observing the wrong thing → model drifts. The reverse direction (Δm → Δb) would require the model to be *the reason* you drew the boundary wrong, which implies you had the right boundary once and then your model shifted and you redrew. That's possible but rare. **Demote this edge.**

### Δr → Δw (recursion capture causing write-authority drift)
**Verdict: Real edge.** When a feedback loop captures a system, it starts generating its own authority to persist. Paper 20 (frame capture) → Paper 18 (unauthorized durability) is exactly this: the captured frame writes itself into governance. The loop doesn't just self-reinforce operationally — it captures the authority layer to protect itself. This is how platform recommendation algorithms become de facto editorial policy without anyone authorizing that transition. **Promote this edge.**

### Δh ↔ Δc (hysteresis hardening consequence detachment)
**Verdict: Real, bidirectional.** Δc → Δh: consequence detachment persists long enough to normalize, and now "that's just how it works." Δh → Δc: a system stuck in a non-return state loses the feedback pathways that would reconnect authority to consequences. They reinforce each other. This is the "institutional sclerosis" loop: consequences detached long ago (Δc), the detachment normalized (Δh), and now the normalization itself prevents reconnection (Δh → Δc). **Nasty reinforcing loop. Keep.**

### Δn ↔ Δh (normalization destroying vocabulary for baseline)
**Verdict: Real, and this is the "book-ish" one.** Δh → Δn: once a pathological state normalizes, the system loses the vocabulary for what "before" was. The new state *becomes* the namespace. You can't articulate what you'd return to because the language for it has been overwritten. Δn → Δh: if you can't name the baseline, you can't recognize that you've failed to return to it, so the non-return is invisible. **Mutually reinforcing. This is how "new normal" becomes permanent — not just because the system can't return, but because it can't name what it would return to.**

---

## Revised Role Classification

### Roots (can arise independently, strongly generative)
- **Δn** — namespace failure. Deepest root. Meta-failure.
- **Δo** — observability failure. Independent, strongly generative.
- **Δs** — signal corruption. Independent, feeds perception-to-model pipeline.
- **Δw** — write-authority drift. Governance root.

### Amplifiers / Transmission (take existing failures and worsen or spread them)
- **Δp** — polarity inversion. Root/amplifier hybrid. Flips sign on everything downstream.
- **Δx** — scale inversion. Pure amplifier. Inverts sign across scale boundaries.
- **Δm** — model drift. Transmission bridge between perception and control. Usually downstream.
- **Δk** — coupling mismatch. Amplifies cascades (tight) or prevents coherent response (loose).

### Operational / Terminal (end-states in the control layer)
- **Δg** — gain mismatch. Mostly end-state.
- **Δa** — actuation mismatch. Mostly end-state.

### Governance Downstream
- **Δc** — consequence detachment. Usually downstream of Δb or Δw.

### Junction (sits between layers, high connectivity)
- **Δb** — boundary error. Key junction between framing and governance.

### Constraint
- **Δe** — energy deficit. Orthogonal resource constraint. Determines recoverability.

### Sink (receives from everything, locks failures in)
- **Δh** — hysteresis. Universal sink. Best therapeutic inversion.

### Composites (don't promote)
- **Δi** — identity failure. = Δn + Δr + Δw. No independent residue.

### Recursion (context-dependent role)
- **Δr** — recursion capture. Root when recursion IS the system. Downstream when enabled by Δp/Δs. Generative via Δr → Δw.

---

## Revised Pipeline Map

```
ROOTS                          CONSTRAINT
  Δn ──→ Δb ──→ Δc ──────┐      Δe ────────┐
  │       ↑↓      ↑       │       │          │
  │      (Δn)    Δw ──→ Δc│       │          │
  │               ↑       ↓       ↓          │
  ↓              Δr      Δh ←────Δh          │
  Δo                     ↕ ↑                 │
  │                     Δn  │                │
  Δs ──→ Δm ──→ Δg         │                │
                            │                │
AMPLIFIERS                  │                │
  Δp ──→ Δr ──→ Δw ────────┘                │
  Δk ──→ Δx                                 │
                                             │
TERMINAL                                     │
  Δa          (any uncorrected failure) ─────┘
                    → Δh (via Δe)
```

(This is approximate. The actual graph has more edges than a clean diagram supports.)

---

## What Changed From the First Pass

1. **Δe reclassified from "root" to "constraint."** It's not upstream of other failures the way Δn is. It's orthogonal — determines whether failures are recoverable, doesn't cause them.

2. **Δp reclassified from "root" to "root/amplifier hybrid."** Sometimes independent, sometimes downstream of Δr or Δs. Chatty was right to question its root status.

3. **Δo promoted.** Was in the perception bucket but not highlighted. It's actually a strong root — independent, strongly generative, and has a real therapeutic inversion (deliberate opacity).

4. **Δm reclassified from "perception" to "transmission."** It bridges perception and control. Usually downstream, rarely originates. Chatty and first-pass disagreed on this; the four questions confirm: Δm is a bridge, not a source.

5. **Δr → Δw edge confirmed.** Recursion capture can generate write-authority drift. This is the Paper 20 → Paper 18 pipeline.

6. **Δh ↔ Δn mutual reinforcement confirmed.** The "book-ish" edge is real: normalization destroys vocabulary for baseline, which prevents recognizing non-return. This is possibly the most important edge in the whole graph for the book's argument.

7. **Δc confirmed as mostly downstream.** Chatty predicted this. Consequence detachment is real but it's a governance end-state, not a generator.

---

## Summary Verdicts

| Domain | Primitive? | Role | Therapeutic Inversion? |
|---|---|---|---|
| **Δn** | Yes | Root | Constructive ambiguity / restraint from premature naming |
| **Δo** | Yes | Root | Deliberate opacity / privacy / information scoping |
| **Δs** | Yes | Root | Signal shaping (but failure is deception, not modification) |
| **Δm** | Yes (weak) | Transmission | Deliberate model simplification |
| **Δg** | Yes | Terminal | Gain tuning (the whole point of control theory) |
| **Δa** | Yes | Terminal | Not really |
| **Δk** | Yes | Operational + amplifier | Tight=coordination, loose=modularity |
| **Δw** | Yes | Governance root | Delegated authority with sunset clauses |
| **Δc** | Yes | Governance downstream | Deliberate consequence buffering (liability, insurance) |
| **Δb** | Yes | Junction | Appropriate scoping (when outside controller exists) |
| **Δx** | Yes | Amplifier | Multi-scale coherent design (Paper 1) |
| **Δr** | Yes | Context-dependent | Recursion as learning / practice / skill acquisition |
| **Δe** | Yes | Constraint | Not really (absence of deficit isn't inversion) |
| **Δh** | Yes | Sink | Anti-flap / damping / regime stabilization |
| **Δp** | Yes | Root/amplifier hybrid | Deliberate contrarian inversion (hack, not stable) |
| **Δi** | **No — composite** | Syndrome | N/A — decompose into Δn + Δr + Δw |
