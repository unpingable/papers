# Six Meets Six: Admissibility Boundaries vs State-Binding Axes

*Status: **working comparison, not doctrine.** Purpose: determine whether the six non-collapsible admissibility boundaries and the six proposed state-binding axes are the same structure, distinct structures, or partially overlapping scaffolds. Candidate mapping artifact; no promotion until axis-for-axis comparison survives.*

> **Anti-inflation fuse.** "Six keeps appearing" is an observation, not a finding. Numerological elegance does not substitute for mapping. If the two sixes don't align under honest comparison, the recurrence is coincidence and the binding-grammar claim loses its "this is the unification layer" framing.

## Axes under comparison

### Proposed state-binding axes (candidate, 2026-04-23)

Source: conversation synthesis 2026-04-23 (duality discussion → chatty's six expansion).

1. **Object** — what is being bound?
2. **Evidence** — what warrants the binding?
3. **Authority** — who has standing to bind it?
4. **Time** — when may it bind?
5. **Scope** — where / how far may it propagate?
6. **Durability** — how long may it persist / how may it unbind?

### Admissibility family (extant, stress-tested 2026-04-08)

Source: `working/developmental-deficit-compensation.md:40-48` (verbatim table).

| Boundary | System | What it governs |
|----------|--------|----------------|
| Observability | NQ | Infrastructure state claims |
| Temporal | Cadence | Data freshness and coherence |
| Persistence | Continuity | Cross-session memory |
| Artifact | Custody | Review/approval validity |
| Entitlement | Standing | Scoped actor authorization |
| Action | Governor | Post-verdict action authorization |

Predicted seventh (not in the six): **Δm / model adequacy.** Papers 7 and 22 describe the failure mode; no existing system asks "is the model consuming admissible evidence still calibrated?"

## Preliminary mapping

| Binding axis | Nearest admissibility boundary | Match strength | Notes / mismatch |
|---|---|---|---|
| Object | *(none obvious)* | **none / weak** | No admissibility system asks "is this the right representation?" Closest is Δm (predicted seventh) — calibration-of-model-against-world. If Object maps anywhere, it maps to the predicted seventh, not to the extant six. |
| Evidence | NQ + Custody | **partial (split)** | The admissibility six splits Evidence into **NQ** (measurement validity / is the sensor healthy?) and **Custody** (review validity / has the artifact been reviewed?). The binding-six collapses these. Either the binding-six is under-specified or the admissibility-six is over-specified. Diagnostic: can you have passed-NQ-but-failed-Custody? (Yes — instrument healthy but no review done.) Can you have passed-Custody-but-failed-NQ? (Yes — reviewer approved stale/wrong-instrument data.) They are non-collapsible in the admissibility sense. |
| Authority | Standing | **strong** | Direct match. "Who has standing to bind" ≡ "scoped actor authorization." |
| Time | Cadence | **strong** | Direct match. "When may it bind" ≡ "data freshness and coherence." |
| Scope | *(none)* | **none** | **Live wire.** The admissibility six has no scope-propagation axis. Closest analogs are partial: Standing gates an actor's reach, Governor gates post-verdict action, but neither asks "did this bound state escape its warrant into other contexts?" Paper 19 (ratchet / dependency mass) and Paper 18 (unauthorized durability) touch adjacent ground but neither names scope as a first-class axis. If the binding-six survives, this is the genuinely new axis it contributes. |
| Durability | Continuity | **partial** | Related but not identical. Continuity = persistence of *evidence / memory / provenance*. Durability = persistence of *bound state*. A state can be durable without its evidence being preserved (zombie state without receipts) and evidence can be preserved for a state that has been correctly unbound. Diagnostic: can you have passed-Continuity-but-failed-Durability? (Yes — receipts preserved, but the state itself cannot be safely unbound.) They are related layers, not the same layer. |
| *(unmapped)* | Governor | — | Governor is the **action gate** — it consumes verdicts from the other five and authorizes action. It is not an axis of binding; it is the terminal enforcement layer. In the binding-grammar frame, Governor is where all six binding conditions are resolved into a go/no-go, not itself one of the six. |

## Preliminary diagnosis (suspect but promising)

**The two sixes are not the same structure.** They are on different dimensions:

- The **admissibility six** decomposes by *boundary type in a signal→action pipeline* (observability, temporal, persistence, artifact, entitlement, action). It answers "what kind of signal / evidence / authorization does this boundary gate?"
- The **binding six** decomposes by *validity question for state transition* (what, how-warranted, who, when, where, how-long). It answers "what condition must be satisfied for this binding to be legitimate?"

Under honest mapping:

- **2 of 6 map cleanly:** Authority↔Standing, Time↔Cadence.
- **1 of 6 maps partially:** Durability↔Continuity (related but distinguishable).
- **1 of 6 splits on the admissibility side:** Evidence → NQ + Custody (admissibility is finer-grained here).
- **2 of 6 don't map:** Object (→ Δm predicted seventh?), Scope (→ not present anywhere in admissibility family).
- **1 admissibility system doesn't appear in binding:** Governor (it's the action gate, not an axis).

If this holds up, the disposition is **Option 3: partial overlap**. The overlap (Time, Authority, Evidence-with-splitting, Durability-ish) is load-bearing. The non-overlap is where each frame contributes what the other doesn't.

## What each frame might contribute that the other doesn't

*(Stated as hypothesis; not yet earned.)*

**Binding grammar contributes to admissibility family:**
- **Scope axis.** Warrant overrun as a genuinely missing admissibility boundary. The admissibility family has no system that asks "did this bound state escape its authorized scope?" Paper 19 brushes it; no admissibility system formalizes it. *If this survives, it is a predicted eighth admissibility system (after Δm/seventh).*
- **Object axis.** May or may not be a new axis, or may collapse into the predicted Δm seventh (model adequacy / representation calibration). Needs disambiguation.

**Admissibility family contributes to binding grammar:**
- **Evidence is not one axis; it is two.** NQ (measurement validity) and Custody (review validity) are non-collapsible. The binding-grammar Evidence axis is under-specified. Proposed refinement: split Evidence into **Evidence-sensed** (NQ-shaped) and **Evidence-reviewed** (Custody-shaped).
- **Governor is not an axis; it is the enforcement layer.** The binding-grammar six may need a seventh element — or an explicit statement that the six are *conditions* and enforcement is a separate stage.
- **Δm predicted seventh.** Model adequacy / representation calibration may be where "Object" actually lives.

## Formal distinction (chatty pass, 2026-04-23)

Admissibility pipeline:

$$ A = (a_1, a_2, \ldots, a_6) $$

where each $a_i$ is a **boundary / validator / control surface**.

Binding event:

$$ B = (o, e, r, t, s, d) $$

where each coordinate is a **validity dimension** (object, evidence, role/authority, time, scope, durability).

The mapping between them is a relation, not a bijection:

$$ a_i \rightarrow \{B_j\} $$

A validator can inspect multiple dimensions. A dimension can require multiple validators. The "six meets six" count is incidental to this relation — no reason to expect axis-for-axis correspondence, and preliminary mapping confirms there isn't one.

## Live wire: Scope test

Define a **warrant envelope**:

$$ \Omega(B) $$

as the set of contexts where a binding is valid, given its evidence, authority, timing, object, and durability constraints. Let $S_\text{applied}$ be the set of contexts where the bound state actually propagates. Then:

$$ \text{warrant\_overrun}(B) \iff S_\text{applied} \not\subseteq \Omega(B) $$

**Working case 1 (NQ → semantic creep, software-native).**

- NQ observes: "host X has WAL bloat at generation $g$." Evidence valid. Custody valid. Standing valid. Governor permits operational note.
- Downstream: scoped diagnostic becomes "service X is unhealthy," then "team X is unreliable," then "do not trust this platform."

Not primarily evidence, authority, or time failure. The original binding was valid *inside* $\Omega$; it failed when it escaped its warrant envelope.

**Working cases 2–5 (non-software, to keep Scope visibly general).**

- **Medical → employment.** A medical test validates "risk factor present." Insurance / workplace systems bind it as "person is unreliable." Binding correct at origin; warrant overrun at downstream propagation.
- **School discipline → institutional record.** An incident report validates "incident occurred in context $X$." Downstream systems bind it as "student is dangerous across contexts." Correct-at-origin, scope-overrun downstream.
- **Financial audit → reputation.** An audit note validates "control deficiency in unit $X$." Board / investor narrative binds it as "company culture is fraudulent." Valid narrow evidence; illegitimate broad binding.
- **Model proxy → individual.** A model flags "proxy-correlated risk at population level." Institution binds it as "individual culpability." Object failure compounds with scope overrun.

All five cases share the structural signature: valid at origin, warrant overrun downstream, no existing admissibility boundary gates semantic propagation. If Governor doctrine doesn't explicitly gate downstream propagation (working assumption: it doesn't), **Scope is a genuinely new axis** — either a predicted eighth admissibility system (after Δm/seventh) or a cross-system invariant.

## Live wire: Object test

**Referential vs material, formal distinction.**

- **Object failure (referential):** the evidence supports one referent; the binding attaches to a different referent.

$$ o_\text{evidenced} \neq o_\text{bound} $$

Question: *did we bind the right thing?*

- **Δm failure (material remainder):** the referent is correct; the model fails to preserve relevant material properties of its referent.

$$ M(o) \not\simeq o \quad \text{(informally: the model does not preserve what matters about } o \text{)} $$

Question: *did our model of the thing preserve what mattered?*

Examples:

- Evidence concerns a host, binding attaches to a service → **Object**.
- Evidence concerns a sample, binding attaches to population → **Object** (often compounds with Scope).
- Procedure validates a document, institution treats it as validating underlying reality → **Object**.
- Model detects pattern in proxy data, binding attaches to human subject → **Object** + **Δm** (referent wrong *and* model fails to preserve substrate).
- Service modeled correctly but unmodeled physical/storage substrate causes failure → **Δm**.
- Human behavior reduced to metric residue → **Object** + **Δm** combo.

Decision rule: if correcting the referent fixes the failure without introducing a new material variable → Object. If referent is correct but the world exceeds the model → Δm. Some failures are combos. Reality, rude as ever.

## The two math tests (resolution condition)

1. **Scope survives** if there exists a valid initial binding whose downstream propagation exceeds its warrant envelope *without violating existing admissibility boundaries at the point of creation*.
2. **Object survives** if there exists a wrong-referent binding *not reducible to Δm, Standing, Evidence, or Scope*.

If both survive, the binding grammar contributes two genuinely new axes to the admissibility family's dimensional account (not as new pipeline boundaries, but as validity questions the existing six do not fully cover). If only Scope survives, that alone is a real contribution. If neither survives, the binding grammar collapses to a rotation.

## Other tests (secondary)

- **Fail-one-pass-the-other across the pair.** For each proposed binding axis, can you construct a failure that is purely that axis without activating any admissibility boundary? Apply per-axis.
- **Evidence collapse test.** Can you construct a case that is pure "Evidence" failure without being either NQ or Custody specifically? If every Evidence failure is one or the other, Evidence is the admissibility family's naming, not the binding grammar's.
- **Governor placement confirmed.** Governor is not an axis — it is the **action gate** that decides whether a binding may transition into action. It inspects axes; it is not one. Treating Governor as the "authority axis" would be a category error; Standing is the authority axis, Governor is the gate that may validate standing before transition. *This is now settled in the note.*

## Dispositions

1. **Same six, different orientation.** Ruled out by preliminary mapping. The two frames are on different dimensions (boundary-type vs validity-question).
2. **Different sixes, superficial recurrence.** Partially supported — the "six" count appears to be coincidence, not architectural inevitability. The admissibility family is six because of pipeline decomposition; the binding grammar is six because of the what/how/who/when/where/how-long question set. These converge on the number six for different reasons.
3. **Partial overlap; overlapping subset becomes load-bearing.** **Current best fit.** Two clean matches, two partial, two gaps in each direction.
4. **Existing six needs revision.** Possible — if Scope survives as a genuine axis, the admissibility family may need a seventh (or eighth, after Δm) admissibility system.
5. **Proposed binding six collapses under mapping.** Possible if the tests above show Scope reduces to Standing-or-Governor and Object reduces to Δm.

### Current disposition, per chatty pass 2026-04-23

> **Partial overlap. Binding grammar is a transition-validity lens. Admissibility six is a pipeline-boundary model. Scope appears underformalized. Object requires Δm comparison before promotion.**

One tentative live hypothesis: **Scope / warrant overrun is probably a real missing axis.** Rest stays provisional. No "constitution" language promoted.

## Immediate next actions

- Work Test 2 (Scope failure case) first. It is the highest-leverage test: if Scope is a rotation of existing admissibility boundaries, the binding-grammar claim loses most of its novelty-weight. If Scope is genuinely distinct, the admissibility family has a missing axis.
- Work Test 3 (Object vs Δm) second.
- Defer the conservation-law claim from `premature-belated-duality.md` §5 until the axis set is stable. The tradeoff hypothesis is about one axis (Time); it does not depend on the full six being right.

## Open questions

- Is the predicted Δm / model-adequacy seventh the same as the proposed "Object" binding axis, or different?
- If Scope survives as a new axis, does it belong as an admissibility system, or is it a property of how the existing systems interact (a cross-system invariant, not a seventh boundary)?
- Are the "seven shared invariants" of the admissibility family (possession ≠ permission, no silent promotion, receipted mutations, explicit validity decay, fail closed, preserved history, context-dependent admissibility) orthogonal to either six, or do they correspond to specific axis-pairs?

---

*Status after this pass: the two sixes are not identical. Partial overlap with meaningful structural disagreement. The "unification layer" claim from earlier in the conversation is not yet earned; it rests on Scope being real and Object being distinct from Δm. Both tests pending.*
