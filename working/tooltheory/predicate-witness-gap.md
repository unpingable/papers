# Predicate-witness gap — paper/Lean companion (lit-check + Lean target)

> **Canonical doctrine lives elsewhere — do NOT restate it here.** The constellation/runtime
> doctrine ("No authority from predicate satisfaction alone"; the §6 non-collapse chain;
> the plane mapping) is AG-Claude's canonical capture at
> `~/git/agent_gov/docs/cross-tool/predicate-witness-infrastructure-note.md`. This note is
> the **papers/Lean-scoped companion**: it holds the prior-art novelty analysis (paper scope)
> and the formal-target design (Lean scope) that the AG note doesn't carry, and it cites AG
> as the doctrine home. Filed 2026-06-25. Status: working / pre-ratified. Not a kernel.

## What this is and isn't

The AG note already self-identifies the seam as `signed≠witnessed` + `no_unifier_without_laundering`
wearing a privacy hat — i.e. **an instance of existing kernels, not a new family.** This
companion does not re-argue that. It records (a) where the claim sits against the *formal*
prior art a crypto/privacy reviewer would cite, and (b) what the defensible *Lean* object is.

## Corpus-kernel mapping (papers-side placement)

Within the boundary-kernels corpus the predicate-witness gap = **`FiatAdmissibility`** (the
category P is operator fiat unless separately witnessed) crossed with **`SurfaceAuthorization`**
(satisfying P *through* a credential surface ≠ P being an authorized category to bind through).
The *mechanism* — satisfaction quantifies over participants, admissibility quantifies over the
category-definition, different objects, so no satisfaction-evidence raises witness-status of P —
is a **quantifier-domain-mismatch non-lift**, the same skeleton as `calibrated≠correct`
(`prediction-markets-case.md`): aggregate-vs-instance there, participant-vs-category here. Third
"different objects" non-lift of the 2026-06 weekend. So: **sharp specimen of owned kernels, not
a new kernel.**

## Prior-art wall (codex/gpt-5.5, web-searched primary sources, 2026-06-25)

Overall verdict: **NOVEL-CONTRIBUTION, narrowly.** Surviving piece = *an explicit
predicate-witness layer + a formal separation/laundering criterion for credential/ZK aggregation
systems.* Not novel: anonymous credentials, issuer trust, schema governance, ZK limits,
classification politics.

| Question | Verdict | Closest primary ref |
|---|---|---|
| satisfaction ⟂ subject-identity already prior art? | **Yes, fully occupied** | Camenisch–Lysyanskaya, EUROCRYPT 2001 (anonymous credentials), doi 10.1007/3-540-44987-6_7 |
| predicate-witness layer: named-but-assumed-away, or formalized as irreducible? | **Named, assumed away (issuer/schema/policy trust); not formalized** | **W3C VC Data Model 2.0** — verifiability "does not imply the truth" of claims; verifier relies on issuer/policy trust |
| the no-go ("predicate-witness underivable from satisfaction primitives") — known result? | **No exact no-go.** Closest is generic ZK/IP semantics: proof establishes only the formal statement | Goldwasser–Micali–Rackoff 1989, *Knowledge Complexity of Interactive Proof Systems*, doi 10.1137/0218012 |
| classification-provenance distinct from Nissenbaum CI / Solove? | **Distinct; closest is Bowker–Star** (classification as authored infrastructure). CI = flow-appropriateness; Solove = aggregation/secondary-use harms | Bowker & Star, *Sorting Things Out* |

**The fatal objection (name it, defend against it):** *"VC/trust-management already says verifier
policy / issuer trust is external — you renamed trust governance."* The defense is NOT "trust is
external" (known). It is the **formal separation + the laundering criterion + the non-collapse
chain** as structure. Any paper/abstract on this MUST cite W3C VC 2.0 up front and say precisely
what's new beyond "issuer trust is external," or a credentials reviewer kills it on sight. The
four refs above are the armor; the AG note's anchor set (Nissenbaum/Solove/Douceur/etc.) does not
yet carry them — that's an absorption for AG-Claude's note, not a thing to restate here.

## Lean target (Lean-side scope)

**Target a SEPARATION result, NOT the grand impossibility.** Codex's sharpest finding: the strong
form ("predicate-witness underivable from satisfaction primitives, full stop") is at risk of being
**true-but-vacuous** — *different quantifier domains alone is not a theorem reviewers respect.*
Two free variables that don't entail each other is a type signature, not a result. The AG note's
§9 already leans separation (exposure-settled-yes / authorship-claimed-no); that instinct is right
and the "stronger and meaner impossibility" instinct is the trap.

**The real design work is prior to the theorem:** you must first define the *admissibility logic* —
what would *count* as a predicate-witness — or the separation is just two unequal symbols. Once
that exists, the defensible object is: exhibit a model where **subject-binding ∧
predicate-satisfaction hold but predicate-witness fails**, with the conflation step (reading the
satisfaction proof as predicate authority) identified as the laundering move. Same skeleton as the
`calibrated≠correct` separation; same witness-typing pattern as `NoFreeStandingBridge` /
witness-carrier.

**BUILT 2026-06-25 as fenced scratch:** `~/git/lean/LeanProofs/Scratch/PredicateWitnessSeparation.lean`.
`lake env lean` → EXIT=0; no sorry/admit/axiom/native_decide; both headline theorems depend on
`propext` only (standard built-in, via `simp`). Proves both:
- `satisfaction_does_not_determine_admissibility` (the two-world specimen — identical satisfaction
  projection, different admissibility);
- `no_satisfaction_bridge_to_admissibility` (`¬ ∃ f, ∀ w, f (ofWorld w) ↔ Admissible w` — no
  function of the satisfaction surface recovers admissibility; the laundering bridge does not exist).
Anti-vacuity lock held: `Admissible` depends on a witness-bearing `World` field that the projection
drops (same skeleton as `TemporalCustody.citation_validity_does_not_imply_execution_admissibility`).

**What it proves and does NOT:** underdetermination, NOT correctness. `PredicateWitness` is a
placeholder structure (real-ish fields, deliberately not `:= True`); the genuine introduction rules
are **prose debt owned by the AG note**, not supplied by Lean. Lean cannot witness aboutness.

**Gate:** the scratch *probe* needed no forcing consumer (that's the lighter scratch category, like
the sibling specimens). **Promotion** to a 1.0 / imported surface stays forcing-case-gated per AG
note §10 — a live predicate-bearing input the constellation must refuse; none yet.

## Provenance

Cross-model thread 2026-06-25 (operator + Claude + ChatGPT + DeepSeek) from an atproto/Community-
Notes screenshot; AG-Claude distilled the canonical doctrine note (see banner). This companion
adds the codex/gpt-5.5 prior-art pass (web-searched primaries) and the Lean-target design. Same
[[feedback-claude-common-mode-synthesis]] interferometry: a non-Claude lit pass, blind to the AG
note, independently reconstructed the authorship-vs-exposure seam and returned NOVEL-narrowly →
the fringe held. Sibling non-lifts: `prediction-markets-case.md` (calibrated≠correct),
`distributional-shadow-tombstone.md`.
