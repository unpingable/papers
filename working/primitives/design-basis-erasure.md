# Design-Basis Erasure

**Status:** candidate
**Originated:** 2026-04-29 (user noticed mid-session — Governor controls leaking into book-prose review; chattY + claude-code containment-rule pass)
**Primary home:** no current paper home — cross-cutting primitive

## Aphorism (keeper)

> *A controller without its wound becomes decorative law.*

Bureaucracy is one *instance* / affect of this failure mode, not the mechanism. The mechanism is **procedure preserved, hazard model lost.**

## Formal object

A control situation is a triple $(P, H, C)$:

- $P$ — plant / domain being governed
- $H$ — hazard / specific failure mode being controlled against
- $C$ — controller / procedure that produces a stabilizing action signal targeting $H$

$C$ is **well-designed** for $(P, H)$ when its action signal loads on $H$ specifically.

The **design basis** of $C$ is the hazard model + plant assumptions + historical wound that made $C$ valid for $(P, H)$.

**Design-Basis Erasure** occurs when $C$ is transferred to a new domain $(P', H')$ in which $H$ is absent or weakly present, and $C$ is applied as if $H' = H$. Surface form (procedures, rituals, vocabulary) crosses the boundary; the design basis does not.

## Failure predicate

$C$ stabilizes against an absent or wrong error signal in $(P', H')$. Concretely:

- The procedure runs.
- It does not control $H'$.
- It may obstruct or distort processes that *would* actually control $H'$.

## Diagnostic test (keeper)

> **If this controller were removed in the imported domain, what specific failure would re-emerge?**

If the answer is concrete (*"X would happen because Y"*) — the controller is loaded on a real hazard.

If the answer is abstract (*"rigor would be lost," "we'd be sloppy," "it'd feel less serious"*) — the controller is decorative law.

"Produces good vibes / signals seriousness / aligns with peer practice" is **not** an admissible answer. Those are second-order benefits of the surface form, not load-bearing on any hazard.

## Typical symptoms

- Imported procedures whose enforcement intensity is decoupled from their hit-rate.
- Vocabulary drift: governance terms used in domains without governance constraints ("ratification" applied to prose drafts).
- Anti-patterns enforced where the original failure mode doesn't exist (e.g., insisting agile retrospectives produce three action items in contexts where requirements don't change).
- Rejection of generative ambiguity, drafting freedom, or exploration in the name of admissibility/rigor.
- Practitioners cannot articulate the hazard their controller addresses — only the controller's surface form.

## Used by / observed in

- **P24 (aggregation-layer masking, Agile case study):** Agile rituals are a controller for "small co-located team + rapidly changing requirements." When transferred to managerial-governance contexts (OKRs, roadmaps, quarterly reviews), the design basis is erased; retrospectives become theater. P24 names this implicitly via its scoping discipline; Design-Basis Erasure makes the import-mechanism explicit.
- **`working/sre-as-shock-absorption.md`:** SRE practices (oncall, runbooks, error budgets) are controllers for production-load + reliability-budget hazards. Imported into adjacent domains (incident review, organizational change, postmortem culture) without the original load model, they produce decorative practice.
- **Governor / agent_gov vocabulary leakage (originating case, 2026-04-29):** ratification, admissibility, receipts are controllers for unauthorized-durable-action hazards in semi-agentic operations. Imported into prose drafting — where the hazard is premature freezing, not unauthorized action — the controller stabilizes against an absent error signal.
- **Compliance-controls into small orgs:** SOX/equivalent audit controls are designed for publicly-traded large-org hazards (shareholder fraud, accounting opacity). Imported into startups, they regulate against absent hazards and obstruct present ones.

## Do not confuse with

- **P25 / Substitution.** P25: target is *unsensed*, controller substitutes a sensible proxy. Design-Basis Erasure: controller is *imported* pre-built for a *different* target. Both produce wrong-target action; the *cause* differs — observability gap (P25) vs design-basis transfer (this). Adjacent, not identical.
- **Goodhart-style metric gaming.** Goodhart: an agent games a proxy. Here: no agent gaming required; the failure is structural in the transfer.
- **Generic "bureaucracy" critique.** Bureaucracy is an affect; this primitive names a specific mechanism. Many bureaucracies have intact design bases and do real work; many lean orgs have decorative non-bureaucratic controllers. The mechanism cuts across the affect.
- **Cargo cult science / cargo cult software.** Closest folk antecedent. Names the surface-imitation pattern but does not separate the mechanism (design-basis transfer) from the symptom (looks-like governance).
- **Ordinary procedural overhead.** Some procedures are slow without being decoratively applied. The diagnostic question separates them.
- **Stale Binding.** Both involve "wrong context for the controller/binding," but at different levels: stale binding is *intra-system temporal* (truth moved, decision didn't notice). Design-basis erasure is *inter-domain transfer* (controller imported without its hazard model).

## Minimal example

Agile retrospectives in two contexts.

**Context 1 (design basis intact):** small co-located team, two-week sprints, requirements change weekly based on user feedback. Retrospective at sprint end: *"what helped us adapt this week, what blocked us."* Action items: tooling fixes, communication adjustments. Hazard $H$ = failure to adapt fast enough. Controller = structured reflection cadence. Action signal loads on $H$.

**Context 2 (design basis erased):** distributed enterprise team, 18-month roadmap, requirements set annually by leadership. Retrospective ritual imported. Cadence enforced ("retros must produce three action items"). Hazard $H$ (slow adaptation to weekly requirement change) does not load — adaptation timescale is annual, not biweekly. The retrospective ritual now controls *nothing*; it generates ceremonial action items that do not address any active failure.

Diagnostic test on context 2: *if you removed retrospectives, what specific failure would re-emerge?* Likely answer: *"people would feel like we're not learning from sprints."* Vibes, not a hazard. Decorative.

## Self-application

The primitives field-notebook in this directory is itself a controller. Its design basis: cross-paper terminology drift, where five papers would otherwise localize the same shape under five names and require later reconciliation.

If the field-notebook discipline (statuses, brutal template, candidates list, "do not confuse with" sections) is transferred to a context without that hazard — a single-paper project, or a project with ontology already settled — the discipline becomes decorative. *Soup with bylaws.*

The README's "anti-patterns" section is the controller keeping its wound visible: *promotion ceremonies, soup with bylaws, primitive-shaped papers, renaming* are exactly the symptoms that emerge when the hazard is absent and the discipline runs anyway.

The primitive applies to itself. Useful reflexive check: any time this directory's discipline starts feeling like ritual rather than dedup, run the diagnostic test on the field-notebook itself.

## Architectural rules (provisional)

- **Don't transfer a controller without its hazard model.** When importing a procedure, vocabulary, or ritual from another domain, name the hazard explicitly. If the hazard doesn't apply, leave the controller behind.
- **State the design basis on the controller at origin.** Document what failure the controller addresses where it was built. Future transfer-attempts can then test whether the hazard travels.
- **Apply the diagnostic test on import.** *If we removed this controller in the new domain, what specific failure would re-emerge?* If the answer doesn't name a concrete hazard present in the new domain, abort the import.
- **Distinguish controller from aesthetic.** A controller produces a stabilizing action signal against a hazard; an aesthetic produces a sense of seriousness. Don't import the aesthetic and call it governance.

## Keeper aphorisms

> *A controller without its wound becomes decorative law.*

> *Procedure preserved, hazard model lost.*

> *The controller travels. The plant model does not.*

## Open questions

- **Composition with Stale Binding.** Some controllers age out: the original hazard fades but the controller remains. That is design-basis erasure within a single domain via *temporal* drift rather than transfer. Track whether this is the same primitive, a temporal special case, or a sibling.
- **Dual case (hazard without controller).** This primitive describes controller-without-hazard. The dual — hazard present, no controller — is also a real failure mode but a different shape. Do not collapse.
- **Partial hazard loading.** Real transfers are rarely "$H$ fully present" or "$H$ fully absent." Some controllers address part of $H'$ and are decorative for the rest. Classification gets fuzzy at the boundary; the diagnostic test handles the fuzzy region acceptably (per-component application).

## Cross-references

- User's mid-session observation, 2026-04-29 (Governor controls leaking into book-prose review).
- chattY's pass: confirmed containment criteria all clear; named "bureaucracy is symptom not mechanism"; framed the diagnostic question; wrote the scope brief that drove this draft.
- Containment rule: `README.md` in this directory. Six criteria all pass; primitive added as candidate, not promoted.
- Adjacent primitives: P25 (Substitution, candidate); [Stale Binding](stale-binding.md); Versioned Semantics (candidate).
