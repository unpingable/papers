# Premature Commitment and Belated Consequence as Dual Orientations of Δt Detachment

*Working note — 2026-04-23. Status: **paper-shaped theorem candidate after formalization pass.** Bucket: Paper 26 candidate. Decision deferred pending §6 empty-window case testing. Destinations non-exclusive: §-insert in Paper 15 or Paper 22, standalone working note, or Paper 26.*

> **Evening capture — 2026-04-23.** Conversation chain (paper-Claude corpus audit → chatty math pass → voice-in-the-room synthesis) produced formal content that promotes this from "nice duality" to "paper-shaped theorem candidate." Math preserved in §3 below. Saturday-recoverable from this note cold. Do not push tired.

> **Anti-inflation fuse.** The parts already exist in the corpus. What is new is the explicit duality, the two-curve formalization, and the empty-window condition. If the empty-window condition fails to produce concrete instances and the curve-shape/operating-point distinction collapses, this folds back into §-insert territory.

## Kernel

**One detachment, two directions.**

More formally: *premature commitment and belated consequence are dual orientations of Δt detachment: the former binds before admissibility has matured; the latter binds after consequence can still attach.*

## 1. Corpus status

A grep audit of `/home/jbeck/git/papers/preprint` on 2026-04-23 confirms:

- The phrase **"premature commitment"** does not appear as a named category. The concept is instantiated in Paper 15 ("commitment can become irreversible before verification could possibly complete"), Paper 13 ("force premature consensus / commit before quorum"), Paper 15 S-4 ("premature convergence"), Paper 19 ("premature remediation").
- The phrase **"belated consequence"** does not appear at all (zero matches). The concept is instantiated in Paper 2 (Δt ~ 10-20y between compliance and reputation), Paper 18 (hysteretic lock-in, T7), Paper 19 (ratchet deepening).
- **Symmetry between them is never stated.** Paper 15 treats Δt = t_commit − t_verify as a one-directional scalar. Paper 2 and Paper 18 treat lag-to-consequence as a separate phenomenon. No sentence in the corpus says "these are the same detachment, read from opposite ends."
- **Topology is absent.** Paper 16's signed geometry has orientation and sign but is not used to place premature/belated as opposite orientations on a Δt axis. Paper 22's four-layer decomposition (gauge/clock/estimation/actuation) is orthogonal to this pair — it asks *which layer* fails, not *which direction* the gap opens.

The ingredients are present. The unification is not.

## 2. Definitions

- **Premature commitment.** A binding event occurs before the admissibility / verification / consequence-evaluation process that governs it has matured. The binding precedes the information that would license it. Paper 15 owns this side.
- **Belated consequence.** A binding event has occurred, and the consequence arrives after the window in which it could still attach to the agent, the decision, the state, or the corrigibility budget that produced it. Paper 2 and Paper 18 own this side.

In both cases, the detachment is a *separation between the binding event and the information required to bind correctly*. The difference is orientation relative to the binding event on the Δt axis.

## 3. Formalization (chatty's math pass, 2026-04-23)

### 3.1 Binding event as coordinate

A binding event is a six-tuple:

$$ B = (o, e, a, t, s, d) $$

where $o$ = object, $e$ = evidence, $a$ = authority, $t$ = time, $s$ = scope, $d$ = durability. (Axes per `working/six-meets-six.md`.) A binding is valid iff each coordinate's admissibility score clears threshold:

$$ q_i(B) \geq \theta_i \quad \forall i \in \{o, e, a, t, s, d\} $$

General binding failure: the system treats $B$ as governing reality while one or more $q_i$ remain below $\theta_i$.

> **Dependency note.** The six-coordinate binding event is used only as a local validity model for $B$. It does not assume identity with the admissibility-family six. See `working/six-meets-six.md`, which currently treats the relation as partial overlap (two clean matches, splits, and gaps in each direction). This note's tradeoff hypothesis concerns the time axis only and does not depend on the full six-axis comparison resolving in any particular direction.

### 3.2 Two-curve model of the temporal axis

Isolating the time axis. Define:

- $m(t)$ = **admissibility maturity**: readiness to bind (generally rises with evidence, review, standing clarity).
- $c(t)$ = **consequence viability**: how much meaningful consequence can still attach (generally decays as assets move, memories fade, exposure windows close, procedural time expires).

Valid binding window:

$$ W = \{ t \mid m(t) \geq \theta_m \ \land \ c(t) \geq \theta_c \} $$

### 3.3 Duality is now a coordinate fact

Disambiguating the binding event. Let $t_\text{commit}$ = time at which the *action / commitment* binding occurs, and $t_\text{consequence}$ = time at which the *consequence / recognition / accountability* binding occurs. These are different events on the same temporal axis; conflating them is the banana peel.

- **Premature commitment:** $m(t_\text{commit}) < \theta_m$. The action-binding occurs before admissibility maturity.
- **Belated consequence:** $c(t_\text{consequence}) < \theta_c$. The consequence-binding occurs after consequence viability has decayed.

Premature and belated are dual failures: same time axis, opposite thresholds, distinct binding events.

Plain-English form: *premature commitment binds action before admissibility matures; belated consequence binds consequence after viability decays.*

### 3.4 Empty binding window (the portable result)

Define:

$$ t_\text{mature} = \inf\{t \mid m(t) \geq \theta_m\}, \quad t_\text{viable} = \sup\{t \mid c(t) \geq \theta_c\} $$

If $t_\text{mature} > t_\text{viable}$, then $W = \varnothing$: the system cannot both know enough and act in time.

Prose form: *the system becomes capable of binding truth only after truth can no longer govern consequence.*

**Name: empty binding window.** Not "empty admissibility window" — admissibility may eventually mature. The empty thing is the *overlap* between admissibility maturity and consequence viability.

**Definition.** An *empty binding window* is a regime in which admissibility maturity occurs only after consequence viability has decayed below the binding threshold.

This is a formal condition with concrete instances (climate; long-tail financial fraud; generational harm; some regulatory actions against faster-decay entities). It is the most portable single result in this note and the most likely to be referenced downstream. It travels well: anyone working on institutional design can ask "is my domain in the empty-binding-window regime" and the question has clear empirical content.

## 4. Topology

The two-curve model *is* the topology. Premature and belated are threshold failures on different curves over the same time axis; the valid window is their overlap. No signed-scalar framing required; no separate phase portrait needed unless it produces predictions the two-curve model doesn't.

## 5. Tradeoff hypothesis, reframed

Let $g$ = governance latency (review, quorum, validation, audit delay). Expected loss:

$$ L(g) = C_p \, P_\text{premature}(g) + C_b \, P_\text{belated}(g) $$

with (usually) $\partial P_\text{premature} / \partial g < 0$ and $\partial P_\text{belated} / \partial g > 0$.

**Conservation as special case, not main claim.** The earlier "Δt is conserved under the duality" formulation is what happens when governance latency only shifts the operating point on fixed curves. The stronger and more interesting claim:

> Good governance changes the curves — it does not just shift the operating point.

Curve-shape interventions: faster evidence maturity, clearer authority, tighter scope, reversible bindings, preserved consequence viability, explicit expiry/unbinding paths. Latency-only interventions redistribute failure and call it oversight.

**Theorem-candidate statement:**

> Temporal binding systems fail when admissibility maturity and consequence viability do not overlap. Premature commitment and belated consequence are dual failures at opposite boundaries of the valid binding window. Governance that only adds latency redistributes failure; governance that improves curve shape reduces it.

### 5.1 Governor has a dual

Governor is architecturally designed to measure and enforce admissibility maturity — it works the $m(t)$ side. The $c(t)$ side is a different architectural problem: preserve consequence viability long enough to bind safely. Primitives in that dual: expiry, reversibility, scope containment, anti-ratchet design, Continuity-backed preservation of consequence context. *Not tonight's problem. Flag for follow-on after Paper 26 lands.*

## 6. Falsification (the live question)

The working note rests on §6. Everything upstream is scaffold.

**Required: a concrete, named case where hardening one pole measurably shifts budget into the other.** Not a plausibility argument. A case with observable magnitudes on both sides.

Candidate cases to work through:

1. **FDA review latency.** Longer pre-market verification → lower premature-approval rate → longer lag between adverse signal and market withdrawal? Or does the verification gate *reduce* belated-consequence because adverse signal is never deployed at scale? (The gate may not redistribute — it may suppress both. If so, duality is violated or substrate-bound.)
2. **Pre-commit code review vs. post-deploy incident rate.** Increasing review depth → fewer premature merges → do incidents attach to code further from authorship (longer commit-to-incident lag) because code has been rewritten through review?
3. **Two-person-rule launch systems.** Do systems that require co-signing produce longer incident-attribution lag? Does the review layer absorb responsibility and delay consequence attachment?
4. **Central-bank forward guidance.** Commits early to bind expectations (reduces premature-commit in the sense of policy surprise) → does consequence (reputation, credibility damage) bind later, after the guidance regime has rotated out?
5. **Pre-registration in science.** Reduces premature commitment (outcome fishing) → does it extend consequence-lag (replication / retraction timelines grow)?
6. **Sarbanes-Oxley / post-Enron control regimes.** Added pre-commit verification to financial reporting → did consequence-lag for actual fraud grow (longer from event to accountability)?

Each case requires (a) a measured premature-commit rate or latency, (b) a measured consequence-lag or attribution rate, (c) an intervention event, and (d) observable redistribution.

**Latency-only vs curve-shape.** Cases must distinguish latency-only governance from curve-shape governance. An intervention that reduces premature commitment *and* preserves consequence viability (by preventing mass deployment, shortening evidence-maturity timelines, or containing scope) alters $m(t)$ or $c(t)$ rather than just shifting $g$ along them. Such an intervention **falsifies conservation but supports the design principle**. The FDA and Sarbanes-Oxley cases are particularly prone to this — they may be curve-shape interventions misread as latency-only. Mark each case explicitly: *latency-only* (tests conservation) or *curve-shape* (tests the design principle).

**Negative result also decisive.** If in every case hardening one pole reduces both (substrate improvement) or is orthogonal to the other (no redistribution), conservation is dead. But the two-curve model and the empty-binding-window condition can still hold. That is a §-insert for the duality / §-insert for the design principle, not a full paper on conservation.

## 7. Disposition

- **If §6 produces at least one concrete case of measurable redistribution:** Paper 26 candidate. Tentative title *"One Detachment, Two Directions: Temporal Binding Windows and Δt Failure"* or *"Premature Commitment and Belated Consequence as Dual Temporal Binding Failures."* Conservation-law framing held back until redistribution is demonstrated — if it survives §6, it can come back in a subtitle or theorem section.
- **If §6 produces only plausibility arguments:** Paper 15 §-insert naming the duality, no conservation claim. Or Paper 22 §-insert placing the duality orthogonal to the four-layer decomposition. The two-curve model and empty-binding-window condition can still land as §-inserts even without conservation.
- **If §6 produces counter-cases (hardening one pole reduces both via curve-shape change):** conservation claim dies; *design principle survives and strengthens.* "Good governance changes the curves" becomes the primary result, with conservation demoted to the pathological-case label.

## 8. Relationship to existing corpus

- **Paper 15** (cybernetic fault domains) owns the premature-commit side. The Δt = max(0, t_commit − t_verify) scalar in Paper 15 is the one-sided projection of the two-sided Δt axis proposed here.
- **Paper 2** (second law of organizations) and **Paper 18** (unauthorized durability) own the belated-consequence side. Hysteretic lock-in, ratchet deepening, and the compliance/reputation lag are all instantiations of the positive-orientation pole.
- **Paper 22** (no universal plant clock) decomposes timing failure by *layer*. This note decomposes by *direction*. Orthogonal cuts; both can coexist.
- **Paper 16** (signed geometry) has the machinery (signed axes, orientation) to host the topology if a phase-portrait framing is needed.
- **Paper 25** (epistemic border control) may be relevant to §6: observability asymmetry could be the substrate that forces the tradeoff, if forced-redistribution reduces to "the system cannot observe the pole it is not regulating."

## 9. Open questions

- Is the conservation claim tight (Δt budget strictly conserved) or loose (tradeoff-tendency under normal operating conditions)?
- Does the duality require a binding event, or can it apply to continuous processes where "binding" is diffuse?
- Is there a third orientation (simultaneous / co-located / null-Δt) that deserves naming, or is that just the regulative ideal?
- Does admissibility theory (working note: admissibility-control.md) give the substrate for the tradeoff — observability asymmetry as the mechanism by which hardening one pole forces budget into the other?

---

*Next action: work §6 against one concrete case end-to-end. FDA or pre-registration most tractable. If redistribution shows up in one, try the rest. If redistribution shows up in none, the paper does not exist and this becomes a §-insert.*
