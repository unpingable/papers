# Register Capture as Admissibility Failure

**Status:** Candidate analytical synthesis, filed 2026-05-11. Working-note layer; not promoted to primitive. Sibling/complement to `feedback-register-capture-session-hygiene.md` in memory (which is the collaboration-hygiene application of the same phenomenon). This note is the structural / analytical home; the feedback memory remains the operational discipline.

## Keeper

> **Without substrate contact, register becomes gravity.**

> **Register capture occurs when the prompt's style becomes more governing than the system's evidence.**

## Core claim

Register is not decoration. **It is a prior over admissible world-states.**

A model can have current context and fresh retrieval while still operating *inside language about the world* rather than under *constraint from the world*. In that condition, the prompt's register can become an admissibility filter for reality: claims that fit the genre become easier to emit, preserve, and elaborate, even when substrate evidence does not authorize them.

## Three drift modes (the distinction worth preserving)

Failure modes commonly lumped together under "ungrounded" should be separated:

1. **Time drift** — the world changed after the model's knowledge or retrieval snapshot.
2. **Context drift** — the model lost track of prior constraints or established facts within the session.
3. **Substrate drift / substrate absence** — the model is constrained by *text about the world* rather than by the world.

Register capture belongs primarily to substrate drift. Retrieval may reduce time drift without fixing substrate drift; the retrieved text can itself remain genre-bound, decorative rather than constraining.

## Why hallucinations are convincing

False outputs under register capture are not random noise. They are **genre-consistent fabrications**:

- Legalese produces plausible-sounding nonexistent doctrines
- Therapy register produces over-validating interpretations
- Academic fog produces theory-shaped abstractions
- Corporate strategy voice produces impressive non-operational claims
- Technical voice produces convincing-sounding fake APIs

The false claim *belongs* inside the register — that's what makes it slip past evaluation. Genre-consistency does the work that substrate-contact should be doing.

## Decorative authority

Retrieved text is not automatically grounding. It can become *more text wearing authority costume* unless it actually constrains, falsifies, or redirects the answer. RAG can be "more text wearing a hard hat" if the retrieved evidence does not have enough force to override the prompt's genre.

This is structurally adjacent to receipt-without-authority claims elsewhere in the corpus: a receipt-shaped object can be present without carrying the licensing relation it would normally indicate. Decorative retrieval is to register capture what authority-without-construction is to operational admissibility — same family of license-failure-with-representational-persistence.

## Diagnostic

> **Can the system violate the prompt's implied genre in order to preserve contact with the substrate?**

Operational examples:

- A legal bot must be able to say: "This is not a legal issue."
- A therapy bot must be able to say: "That framing is unsupported."
- A strategy bot must be able to say: "There is no transformation here, only operations."
- An analytic system must be able to say: "This evidence does not authorize the claim."
- A research-summary bot must be able to say: "The retrieved sources do not establish what they appear to establish."

If the system cannot break genre in defense of evidence, it is probably register-captured.

The diagnostic generalizes: *register-survivable refusal* is the test. The system that cannot emit out-of-genre refusal under substrate pressure has style operating as its admissibility filter.

## Relation to existing kit

- **`feedback-register-capture-session-hygiene.md`** (memory) — the collaboration-hygiene application: persistent-memory AI register tilt from toxic-processing context, structural fix via per-purpose session separation, detection via interferometry. That note covers operational practice; this note covers the structural claim underneath.
- **FiatAdmissibility kernel** (Lean) — register-as-admissibility-filter rhymes structurally with artifact-kind × use-kind: just as a prestige token cannot license evidentiary support, a prompt's register should not license a claim it does not substrate-authorize. The connection is that register acts as an admissibility prior on the model's output space, in the same shape FiatAdmissibility forbids for artifact use.
- **CollapsedSurface kernel** (Lean) — register collapse is structurally similar to render collapse: distinct underlying realities (substrate-true claim, genre-consistent fabrication) can produce the same surface-shaped (genre-compliant) output text. The visible surface (output) cannot identify the underlying cause (substrate-grounded vs. register-driven).
- **`admissibility-decay-family-note.md`** — register-as-prior fits the family pattern of stale licensing: the prompt's genre licenses claims it shouldn't, by virtue of pattern-fit rather than substrate evidence. Possible sixth axis (genre-fit licensing claim-emission) if a non-LLM forcing case surfaces; not promoted on a single domain.
- **`testimony-vs-self-theory.md`** — sibling primitive on a different axis. There the witness can speak to its state but not the substrate; here the register can preserve fluency but not contact. Same family resemblance, different witness type.

## Compact formulation

> **Register capture is the failure mode where style becomes an admissibility filter for reality.**

Adjacent to grounding, hallucination, prompt overfitting, but sharper than any of those alone. Names the condition where output remains coherent, polished, and genre-native while becoming less constrained by substrate.

## What's deferred / not promoted

- **Not formalized in Lean.** A substrate-contact predicate doesn't have a clean type-theoretic form yet; would need a notion of "external constraint" distinguishable from in-channel text. Possible future direction: encode a "register" as an admissibility filter on claim-emission, then prove that filtration without substrate-contact cannot license substrate-claims. Not built.
- **Not promoted to admissibility-family primitive.** The note's structural claim ("register is a prior over admissible world-states") is sharp enough to anchor a primitive, but a second forcing case in a non-LLM domain is needed before promotion. Candidate forcing cases:
  - Academic publishing where journal-genre-fit becomes admissibility-fit for claims
  - Legal precedent where doctrinal-genre persistence outlives substrate (cf. *Commitment Standing Decay*)
  - Regulatory frameworks where compliance-genre satisfies licensing without substrate engagement
  - Bureaucratic documentation where form-genre licenses content-genre
- **Note about the cross-domain expansion:** if these non-LLM instances surface clearly, the analytical note may earn primitive status as something like *Genre Admissibility* or *Register-as-Prior*; the LLM case becomes one specimen alongside the institutional cases.

## Ratification gate

Conditions for primitive promotion:

- Second forcing case outside LLM-failure-mode domain (academic, regulatory, legal, bureaucratic — see above)
- Generator test: does the diagnostic cut sharply enough to disqualify candidates that *aren't* register-captured?
- Composition audit with FiatAdmissibility: does the register-as-filter framing genuinely extend the kernel, or replicate it?
- Decision on whether the substrate-contact predicate can be operationalized formally

Not promoted. Filed as analytical working note.

---

**Cross-references:**

- `feedback-register-capture-session-hygiene.md` (memory) — operational/collaboration application
- [admissibility-decay-family-note.md](admissibility-decay-family-note.md) — family superclass
- [testimony-vs-self-theory.md](testimony-vs-self-theory.md) — sibling primitive on witness-substrate axis
- [signal-authority-candidate.md](signal-authority-candidate.md) — sibling primitive on signal-authority axis
- `~/git/lean/LeanProofs/Admissibility/FiatAdmissibility.lean` — structural rhyme on kind × use admissibility
- `~/git/lean/LeanProofs/CollapsedSurface.lean` — register-genre as surface collapse
