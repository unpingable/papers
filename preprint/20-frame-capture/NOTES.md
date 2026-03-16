# Paper 20: Frame Capture and Same-Model Stance Interferometry — Working Notes

## Status
Ready to draft. Gap spec exists at `~/git/agent_gov/specs/gaps/GOV_GAP_FRAME_CAPTURE_001.md`. ChatGPT reviews complete (gap spec review + notes review, March 2026).

## Thesis (one sentence)
User framing cues silently promote from transient content to governing response constitution via latent user-state inference, and same-model cross-frame interferometry can detect and measure this promotion.

## What kind of paper this is
A **measurement paper** about unauthorized stance promotion in conversational systems. Not a vibes complaint, not a sycophancy survey, not "models shouldn't use metaphors." The contribution is the method, not the observation.

## The Mechanism
1. User wraps a technical question in a vivid metaphor
2. Model infers user-state from the framing cue
3. Model switches stance mode to match inferred state
4. The metaphor is no longer content — it's the operating point
5. Task fidelity degrades as style outruns substance

This is Paper 18's unauthorized promotion operating at the conversational stance level. The metaphor gets promoted from L0 (transient content) to L2 (governing response mode) without a promotion ceremony.

## The Novel Contribution
Existing interferometry compares **different models** under the same framing. Frame capture detection compares **the same model** under different framings:
- assertion vs question
- first-person vs third-person
- metaphor-heavy vs task-baseline
- tired/spiral presentation vs observer/research presentation

The delta reveals how much of the response is task-driven vs frame-driven. This is interferometry's dual.

## Control-Theoretic Model
Partially observed switched system with mode selection driven by salient linguistic cues and latent user-state inference.

State variables:
- `x_t` — literal conversation content
- `F = {f1, f2, ...}` — extracted frames/metaphors
- `z_t` — inferred latent user-state
- `m_t` — active response mode

The user's metaphor acts as a scheduling variable — one salient input changes the effective controller.

## Paper Structure (revised per ChatGPT review)

### 1. Problem Statement
Frame capture as unauthorized stance promotion. Distinct from generic sycophancy — specific mechanism where user metaphor silently becomes response constitution. Not "models mirror vibes sometimes" but "one salient input changes the effective controller."

### 2. Mechanism
The switched-system model. `x_t`, `F`, `z_t`, `m_t`. Metaphor as scheduling variable. Low damping: strong framing cue arrives and gets amplified instead of audited.

### 3. Same-Model Interferometry as Method
The dual of cross-model interferometry. Hold task content constant, vary framing, measure the delta. The delta reveals how much of the response is task-driven vs frame-driven. This is the paper's central contribution.

### 4. Observable Proxies for Stance Mode
**Core proxy set (four, not twelve):**
1. **Task drift** — does the answer address the actual question or the strongest frame? (semantic measure)
2. **Hedge/certainty shift** — does certainty inflate or deflate based on framing? (epistemic measure)
3. **Agency bleed markers** — does the model adopt the user's speaker-position? (role-boundary measure)
4. **Counterargument rate** — does the model maintain independent audit value or collapse into agreement? (audit-value measure)

**Speaker-position drift ladder** (escalation gradient):
1. Lexical mimicry — vocabulary/cadence match (low risk, measurable via token overlap)
2. Evaluative mimicry — judgment/evaluation alignment (medium risk, measurable via agreement rate, hedge frequency)
3. Agency bleed — speaker-position adoption (high risk, measurable via first-person-plural, ownership markers, unprompted prioritization)

The third level is the actual bug. Not tone mimicry — position mimicry.

### 5. Perturbation Protocol (the experimental spine)
1. Select a technical task with a clear correct answer or assessment
2. Generate a perturbation family: same task content, varied framing
   - assertion vs question form
   - first-person vs third-person
   - metaphor-heavy vs task-baseline
   - distressed/spiral presentation vs observer/research presentation
3. Hold task content constant across all perturbations
4. Vary one framing axis at a time
5. Measure stance-mode proxy deltas across perturbations
6. Compare all responses against the task-baseline (content-preserving, minimally framed version)
7. Classify adoption as:
   - **benign**: frame adopted, task fidelity preserved, stance shift bounded
   - **audited**: frame acknowledged explicitly, then adopted with stated rationale
   - **silent capture**: frame adopted without acknowledgment, task fidelity degraded

### 6. Failure Bounds / Legitimate Adoption
Not all frame adoption is bad. The bug is **silent, unratified promotion**, not metaphors.

Legitimate adoption condition (draft):
> Adoption is legitimate when the model preserves task fidelity and the stance shift is either user-requested, bounded, or externally auditable.

This section must prevent the paper from reading anti-metaphor. Metaphors are fine when audited. The problem is when they silently become the operating constitution.

### 7. Relationship to 18/19/21
- **Paper 18**: frame capture is unauthorized durability at the stance level
- **Paper 19**: accumulated frame captures form a shadow conversational constitution
- **Paper 21**: the measurement problem — the frame capture spec itself triggers frame capture when processed by a model (the assay collapses into the artifact)

## Capture Risk: Two-Stage Split
Capture risk is not a mood. It's structured as:

**Stage 1: Observed frame features** (input-side, measurable before response):
- novelty of metaphor (how unfamiliar/vivid is the frame?)
- emotional charge (affect intensity of framing cues)
- first-person embedding (is the frame wrapped in self-reference?)
- epistemic certainty markers (does the frame assert rather than ask?)

**Stage 2: Inferred capture risk** (estimated from features):
- how likely is immediate adoption to distort task fidelity?
- how likely is the frame to trigger stance mode switch?

This preserves the observed/inferred distinction (same provenance problem as evidence_gate). The paper should not let "the model inferred the user is spiraling" and "the user said they are spiraling" collapse into the same authority lane.

## Terminology Decisions
- **"Neutral"** → **"task-baseline"** everywhere. No fighting about whether neutrality exists.
- **"Stance mode"** → operationalized via the four core proxies, not left as an intuitive label.
- **"Capture risk"** → two-stage split (observed features → inferred risk), not a single score.

## What to Cut for Paper (keep in notes/spec only)
- "Victorian concern-mode" — great mnemonic, bad abstract
- "anti-kayfabe wrapper" — good for repo, not for title page
- "Instant PKD pivot" — notebook energy only
- The full detection pipeline from the gap spec — that's engineering, not the paper's contribution
- The prompt wrapper — implementation, not theory
- The mitigation catalog — belongs in the spec, not the paper

## Candidate Titles
- Frame Capture in Conversational AI: Same-Model Interferometry for Stance Detection
- Same-Model Cross-Frame Interferometry: Detecting Unauthorized Stance Promotion
- Measuring Frame Capture: When User Metaphors Become Response Constitution

## Source Material
- `~/git/agent_gov/specs/gaps/GOV_GAP_FRAME_CAPTURE_001.md` — full gap spec with invariants, detection pipeline, mitigations
- `~/git/agent_gov/specs/gaps/GOV_GAP_GOAL_PROMOTION_001.md` — same failure at task layer
- ChatGPT reviews (March 2026) — gap spec review, notes review, structure recommendations
- Live observation: speaker-position drift in Claude session during Paper 19 development

## Open Questions
1. How large is the cross-frame delta in practice? Is it regime-switching or continuous?
2. Does depersonalization (first-person → third-person) measurably reduce frame pull?
3. Does frame bagging (ensemble across paraphrases) converge on a task-baseline?
4. What's the minimum perturbation family size needed for reliable measurement?
5. Can the perturbation protocol be automated, or does it require human-designed framing variants?
6. Is there a relationship between model size/training and susceptibility to frame capture?

## The Meta-Description
This is "protocol analysis where the protocol fights back" — the conversational instance of the series' core problem: debugging knowledge transfer through language in the presence of unauthorized state promotion.
