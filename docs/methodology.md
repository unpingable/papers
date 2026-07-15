# Δt Framework — Methodology

A short orientation to *how* the work is produced, not what it claims. Written for someone who has landed on a paper, the formalization repo, or a working note and wants to know what kind of project this is before deciding whether to engage.

The methodology is named here so other surfaces can link to it instead of rebuilding the explanation inline. None of the moves below are novel individually; the contribution is the *combination*, applied consistently across a long-running research program.

## What this is

The Δt framework is a growing preprint series (see [Zenodo](https://zenodo.org/communities/delta-t-framework)) plus working notes, on systemic failure, temporal mismatch, authority collapse, and recovery under degraded conditions. The papers develop much of the theory in prose; a [companion Lean repo](https://github.com/unpingable/lean) also develops, audits, and sharpens selected claims by translating them into definitions and theorem statements and checking what survives. Where an operational implementation exists or is planned, the formal contract may precede and lead that code.

This is independent open-source work by James Beck, an independent researcher with an SRE / operator background, writing primarily for two audiences: people who care about systemic failure modes in technical and organizational systems, and people building AI agents who need a vocabulary for *governance* rather than *capability*. The tone is operational rather than disciplinary: the framework is written to be used, audited, and revised.

## The interferometer

Most of the conceptual work uses **multi-model triangulation across specialized AI sessions**, not a single chat. Different sessions hold different roles:

- *Repo / formal-work register* — daily implementation, file edits, theorem-proving, audit bookkeeping.
- *Authorial register* — book-side prose and chapter-level writing.
- *Structural pushback / skeptical review* — adversarial reading, scope-trimming, catching laundering.
- *Research / scout* — survey of adjacent literature and primitives, identifying strain sites.
- *Epistemological governance* — cross-cutting calibration and admissibility discipline.

The AI sessions produce readings, objections, drafts, and formalization pressure. **Synthesis and publication decisions are made by direct human review.** The methodology is not AI-generated research; it is instrumented independent research with adversarial registers and public audit artifacts. The distinction matters for misclassification: a reader who treats the artifacts as model output rather than as human-authored work mediated through specialized review sessions will draw the wrong conclusions about what the methodology can and cannot warrant.

The sessions are kept deliberately separate. Artifacts produced in one session can be shared into another for review, but the conversational context doesn't carry across — a casual riff in one chat doesn't pollute a rigorous-review chat in another. Each session also has known calibration tendencies: some lean conservative (good at catching scope creep, prone to over-trimming); some lean activity-biased (good at making progress, prone to over-building); some lean toward narrative coherence at the expense of structural rigor. The combination *triangulates under asymmetric bias* and catches things any single register would miss.

The methodology is itself documented as it evolves — see [`working/methodology-as-operational-discipline.md`](../working/methodology-as-operational-discipline.md) for the essay-seed version.

## The audit register

The companion Lean repo carries a **public claim register** in [`CLAIM-REGISTER.md`](https://github.com/unpingable/lean/blob/main/CLAIM-REGISTER.md). Every claim that has been formally examined gets a status:

- **BROKEN** — Lean falsified the claim or showed it conflated distinct concepts. The original prose overreached.
- **STALE** — Not wrong, but framed in a way the formal pass showed is imprecise.
- **SOUND** — Survives formalization; correctly framed.
- **OPEN** — Not yet testable; needs further work.
- **ADMITTED** — A theorem stated and deliberately not proved, with the admission itself being the load-bearing record (see e.g. *"investigative null"* shapes where the question is genuinely undecidable in current vocabulary).

The register is meant to be read as the *primary methodological commitment of the project*, not a defensive disclaimer. Most research that gets falsified or narrowed in private is rewritten quietly; here the falsifications and narrowings are kept as part of the public record. **Displaying the failure is the discipline.** A claim that survived the formal pass is more reliable for a reader; a claim that broke is evidence about which prose moves were doing real structural work versus which were useful for discovery but couldn't carry formal weight.

This shape only makes sense once the audit register is read as part of the methodology rather than as hedging. Without that frame, *"some claims survive, some break"* reads as either a cop-out or a genre convention. With it, the breakage is the result.

## The labor split

The work uses **a deliberate split between conceptual architecture and formal verification**:

- *Prose* is good at discovery — finding the right shape of a question, hearing recurrences across domains, recognizing primitives that haven't been named yet. Most of the framework's distinctive contributions arrive in prose first.
- *Formal verification* is good at audit and investigation — distinguishing structural claims from slogans that were useful for discovery but too loose to carry formal weight, and sometimes exposing the usable architecture before an implementation exists. Lean does not replace conceptual discovery, but it is not required to wait downstream of runtime code. A formal contract may lead implementation.

Both halves are load-bearing. Skipping the formal pass leaves prose theory free to drift; skipping the conceptual pass produces formalization without architectural purpose. The ratio matters: most papers in the series are prose-first with selected formalization; the Lean repo carries the audit substrate, not the theory itself.

When the formal pass catches something the prose obscured — a hypothesis the prose was implicitly assuming, a boundary case where the doctrine breaks, two distinct concepts being collapsed under one name — that's evidence the methodology is working. Several primitives in `working/primitives/` and several preprint revisions trace directly to formal-pass findings.

## Formalization, promotion, and conformance

These are three separate decisions:

1. **Formal development** may begin when there is a coherent, non-redundant theorem or type boundary to investigate. It does not require a shipping consumer, a forcing case, or prior runtime adoption. The formalization is allowed to lead the code.
2. **Promotion** decides whether a proved artifact joins a public or compatibility-bearing surface. Proof scope, overlap, anti-vacuity controls, naming, custody, and release stability govern that decision. Runtime use may supply useful correspondence evidence, but it does not grant permission to develop the theorem.
3. **Runtime conformance** is a claim about an implementation. It requires an explicit mapping from runtime behavior to the relevant definitions and theorems, plus implementation evidence or a refinement argument. Merely citing a theorem identifies an intended contract; citation alone is not evidence that the implementation conforms to it.

This separation preserves the anti-cathedral controls without turning YAGNI into a veto over mathematics. A proposed formal artifact can still be refused because its statement is vacuous, duplicates existing substrate, smuggles an unjustified bridge, or lacks stable semantics. It cannot be refused merely because no consumer has arrived yet.

## Honest compounding

Every retraction keeps the foundation clean. When a claim is reclassified from SOUND to BROKEN, the affected papers are updated (or marked stale and re-issued); the register records the move; future work cites the corrected version. **The audit register is append-only in spirit**: a status can change as evidence accumulates, but the history of how it changed is preserved.

The long-term asset of the project is not any specific theorem; it is the corpus's honesty. A reader five years from now should be able to reconstruct what was claimed, what was retracted, and why — without having to reverse-engineer it from internal contradiction. This is also why the work is published openly on Zenodo with persistent DOIs rather than chased through traditional venues; the publication model is structured around making retraction *easy and visible* rather than expensive and invisible.

## What this is not

- **Not a claim that Lean proves the whole theory true.** Lean is a forcing function against theory-by-metaphor, not a substitute for case studies, simulations, operational evidence, or empirical work in the relevant domains.
- **Not a manifesto.** The framework develops failure-mode primitives that ought to be portable; the methodology described here is one way of producing them, not a prescription for how others should work.
- **Not a credentialed academic project.** Independent research, no university affiliation, no funding-bound deliverables. The series is structured so that the artifacts (papers, formalizations, working notes) are the contribution; the framework's value is whether anyone finds the primitives useful in their own diagnostic work.
- **Not an oracle.** The series tag is *"a lab notebook, not an oracle."* Some claims are speculative, some are tentative, some are wrong — and the register tells you which are which. The framework earns trust by being legible about its own confidence levels, not by performing certainty.

## Pointers

- Project root: [unpingable.github.io](https://unpingable.github.io/)
- Papers (prose): [github.com/unpingable/papers](https://github.com/unpingable/papers)
- Lean (formal audit): [github.com/unpingable/lean](https://github.com/unpingable/lean)
- Audit register: [`CLAIM-REGISTER.md`](https://github.com/unpingable/lean/blob/main/CLAIM-REGISTER.md)
- Module → paper crosswalk: [`PAPER-MAP.md`](https://github.com/unpingable/lean/blob/main/PAPER-MAP.md)
- Paper → module crosswalk: [`docs/formalization-index.md`](formalization-index.md)
- Author: James Beck — [ORCID 0009-0009-5524-767X](https://orcid.org/0009-0009-5524-767X)
