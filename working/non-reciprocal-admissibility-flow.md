# Non-Reciprocal Admissibility Flow — Candidate Handle

**Status:** Candidate / generator-tested / primitive-status pending. Filed per name-early discipline. Explicitly **not promoted.** No `NonReciprocalAdmissibility.md` in primitives. No Lean module staged.

Filed 2026-05-15. Surfaced via attention-mechanism analogy (Gemini → ChatGPT pushback), but the handle survives outside that vocabulary — see five passing non-LLM domains below.

## Core keeper

> **A shapes what can count for B while pretending this is not an authority relation.**

The *pretending* is load-bearing. Mere asymmetry is not the cut.

## Hard distinction

- **Ordinary authority asymmetry:** A may bind B because A has standing. The authority relation is named.
- **Non-reciprocal admissibility flow:** A shapes B's admissible future state while the system presents the relation as neutral scoring, feedback, relevance, risk, merit, evaluation, optimization, or market signal. The authority relation is *disguised as measurement*.

Hierarchy exists. Markets are asymmetric. Institutions evaluate people. That alone does not earn a primitive. The cut is the laundering of authority through neutrality-shaped surfaces.

## Generator test (five questions)

1. **Directional coupling:** Does A affect B's future admissible state?
2. **No reciprocal standing:** Can B affect A in the same admissibility channel?
3. **No contestability:** Can B inspect, challenge, or force reweighting of A's influence?
4. **Surface neutrality:** Is the system described as scoring / ranking / attention / feedback / risk / merit / market signal rather than authority?
5. **State consequence:** Does B inherit obligations, reduced standing, degraded visibility, pricing, exclusion, or changed authorization because of the coupling?

If all five hit, the handle may be real.

## Five passing domains

| Domain | 1. Directional | 2. No reciprocal standing | 3. No contestability | 4. Surface neutrality | 5. State consequence |
|---|---|---|---|---|---|
| **Credit scoring** | ✓ | ✓ | mostly (FCRA narrow; model itself not contestable) | ✓ ("risk model," actuarial) | ✓ (loan, housing, employment) |
| **Platform ranking / moderation** | ✓ | ✓ | mostly (opaque appeal, opaque model) | ✓ ("relevance," "engagement," "policy") | ✓ (reach, monetization, visibility) |
| **Citation / prestige networks** | ✓ | ✓ (outsider citation has near-zero effect on elite) | ✓ (no formal channel) | ✓ ("merit," "impact factor") | ✓ (hiring, funding, publishing access) |
| **Procurement / vendor scoring** | ✓ | ✓ | ✓ (RFP opacity, scorecard opacity) | ✓ ("evaluation," "fit") | ✓ (vendor viability, exclusion) |
| **Employment / reputation** | ✓ | ✓ | ✓ | ✓ ("feedback," "performance," "culture fit") | ✓ (employability, severance, references) |

All five pass cleanly. The pattern survives outside attention-mechanism vocabulary, which is the bar for "not just a cute transformer analogy."

## Kernel-overlap audit

This handle is *adjacent to* but *does not collapse into* the following:

- **Compression Becomes Authority** (`project-compression-becomes-authority`, scouting essay). CBA is about **object substitution**: the score / proxy / compression becomes treated as the thing it measures. NRAF is about **relation laundering**: the relation doing binding work is represented as neutral measurement. CBA asks "what is the score?" (ontology of the score). NRAF asks "what kind of relation is this?" (relation-type confusion plus structural asymmetry). Sibling cuts, not nested.

- **SurfaceAuthorization** (`~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean`). SurfaceAuthorization asks whether the surface is authorized at all. NRAF is the case where *the surface presents as non-authoritative while doing authority work.* Same family ("authority shape mismatched to surface"), different failure mode. NRAF may compose with SurfaceAuthorization as a special case where the unauthorized surface specifically hides behind neutrality framing.

- **FiatAdmissibility** (`~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean`). FiatAdmissibility refuses unauthorized protocol extension for artifacts (artifact-kind × use-kind axis). NRAF is on a different axis: relation-shape × authority-disclosure. Not a UseKind extension.

- **Signal Authority** (`working/signal-authority-candidate.md`). Signal Authority is about *null/silence/timeout misclassified as verdict* (non-event manufactured into event). NRAF is about *acknowledged interaction laundered as non-authority* (event present, relation-type disguised). Different cut.

- **Admissibility decay family** (`working/admissibility-decay-family-note.md`). Decay-family primitives are about *stale licenses* (license once held, no longer valid). NRAF is about *unauthorized presentation* (license never declared as license). Orthogonal axis.

So it doesn't collapse. The handle names an actual animal.

## Non-promotion guard (explicit)

- **Do not create `NonReciprocalAdmissibility.md`** in primitives. Not earned.
- **Do not stage `LeanProofs/Admissibility/NonReciprocalAdmissibility.lean`.** Same posture as Signal Authority and Commitment Standing Decay — named, generator-tested, primitive-status pending, canonical Lean deferred.
- **Do not let the term breed.** Working note exists to prevent loss and prevent premature kingdom formation.

## Lean probe (sketch, not canonical)

Discipline: **Lean may probe the cut; Lean must not certify the primitive.**

A probe sketch lives at `~/git/lean/non-reciprocal-admissibility-flow-sketch.lean` (filed 2026-05-15, alongside `taxonomy-lean-sketch.lean` — top-level, not in `LeanProofs/Admissibility/`, not in lake build).

The probe proves exactly one theorem: `nraf_not_ordinary_authority`. Directional state-shaping + no reciprocal standing + neutral-surface presentation is not equivalent to ordinary authorized asymmetry. The minimal cut. Nothing more.

The probe does *not*:
- Prove that NRAF instances are bad (normative weight stays in this note)
- Prove any domain (credit, platform, etc.) instantiates the structure (generator test is the audit)
- Compose with SurfaceAuthorization or any other canonical kernel piece

If/when promoted to canonical primitive, composition audit with SurfaceAuthorization is the first formal task. Likely shape: NRAF is the special case of SurfaceAuthorization where the unauthorized surface specifically uses neutrality framing to extract authority. That's a hypothesis for the gate, not a theorem.

## Promotion gate

Conditions for candidate → doctrine:

- **Sixth spontaneous domain instance** arriving outside this filing context. Five domains came from a single brainstorm; a sixth showing up unprompted (in user's other work, in a paper draft, in a postmortem) is the signal that the cut is generative rather than constructed.
- **Paper draft makes the term load-bearing.** If a paper needs to say "this is an instance of non-reciprocal admissibility flow" to communicate its claim — and no existing primitive carries the work — the term has earned its keep.
- **Generator test sharpening.** Whether one of the five test questions is doing all the work and the others are decorative. Suspect candidates: question 3 (contestability) may collapse into question 2 (reciprocal standing) under most readings; needs disambiguation.
- **Composition audit:** how does NRAF compose with SurfaceAuthorization specifically? Is NRAF the *neutrality-disguised* sub-case of SurfaceAuthorization, or is it cross-cutting?

Not promoted. Filed.

## Markets specimen + measurement-import (NEAM, 2026-05-16)

Surfaced via NPC Alex's "Non-Equilibrium Attention Markets" piece (NEAM) and ChatGPT's read. NEAM derives softmax attention from MaxEnt over continuous Ising states, then argues that asymmetric `WQᵀWK` coupling breaks detailed balance, drives entropy production, concentrates the stationary attention distribution, and produces endogenous fat tails / crashes.

**Treat as: markets specimen for NRAF, with two useful measurement surfaces. Not a new primitive. Not a sixth gate-firing domain instance** (it's an import of measurement vocabulary, not a domain that needs the NRAF primitive to be communicable — markets discourse already has "asymmetric information," "front-running," "informed/uninformed").

**Useful imports (with guardrails):**

1. **Schnakenberg entropy production rate** `Π = ½ Σᵢⱼ (πᵢpᵢⱼ − πⱼpⱼᵢ) ln(πᵢpᵢⱼ / πⱼpⱼᵢ)` as a rate-like diagnostic for non-reciprocal Markov flux.
   - **Guardrail:** Π measures *entropy production from asymmetric flux inside a chosen Markov representation under NEAM modeling assumptions.* It is **not** an admissibility verdict. Otherwise the measurement quietly becomes the judge. The map from "Π is high" to "NRAF is occurring" requires a separate authority-status claim.

2. **Herfindahl-Hirschman Index over stationary distribution** `HHI = Σⱼ πⱼ²` as a scalar for attention/influence concentration.
   - **Guardrail:** HHI measures *concentration of effective influence.* It is **not** a laundering measure. Laundering requires the separate claim that the concentrated relation is presented as neutral measurement / scoring / market signal. Concentration without disguise is ordinary oligopoly; NRAF needs the surface-neutrality step (generator test Q4).

**Symmetrization is not moral repair.** NEAM treats symmetric coupling as the equilibrium baseline, but real markets may *require* asymmetry to function (price discovery, market-making, information aggregation). The NRAF question is not "is the coupling asymmetric?" — it is "which asymmetries acquire authority while denying they are authority relations?" Symmetrization restores detailed balance in the model; it does not restore admissibility legitimacy in the world.

**Public-facing payoff worth keeping:** endogenous fat tails as consequence of adaptive asymmetric attention topology rather than exogenous anomaly. Rhymes with reflexivity / structural fragility without collapsing into either. NEAM's attention-collapse → HHI spike → diffusion explosion → flash crash chain is the piece that earns the drama; it's also the piece NRAF *doesn't* need to import to stay a primitive candidate.

**ChatGPT's caveats that travel:** the adiabatic approximation (attention equilibrates fast, learning slow) is load-bearing and markets often violate it; "Π rises → crash" needs an explicit failure criterion (infinite relative to *what* — liquidity, margin, coordination bandwidth?); "efficient market = MaxEnt market" is a usefully delicious slogan and a rake.

**Lean tripwire (non-canonical, in existing sketch):** Appended to `~/git/lean/non-reciprocal-admissibility-flow-sketch.lean` as a `## NEAM measurement adapter — non-canonical lead` block. Encodes only the boundary shape via `DiagnosticMeasure` / `DiagnosticUse` / `diagnosticUseAllowed`, plus three tripwire theorems (`no_measure_authorizes`, `no_measure_declares_admissibility_failure`, `no_measure_declares_laundering`). No Markov plumbing, no Schnakenberg formula, no HHI formula, no markets structure. If a future change tries to use Π or HHI as authorization / verdict / laundering surface, the tripwires break. Audit step before promoting to canonical: check whether `NumericalAdmissibility.lean` already encodes the MeasurementKind × AuthorityUse pattern; if so, this sketch retires rather than competes.

---

**Cross-references:**

- `project-compression-becomes-authority` (memory) — sibling on object-substitution axis; same family of "scoring surface mistaken for substrate" pathologies
- `working/signal-authority-candidate.md` — sibling on null-as-verdict axis
- `working/commitment-standing-decay-candidate.md` — sibling on stale-license axis
- `working/admissibility-decay-family-note.md` — admissibility-decay family overview
- `~/git/lean/LeanProofs/Admissibility/SurfaceAuthorization.lean` — closest existing kernel piece
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — artifact-kind × use-kind axis (different cut)
