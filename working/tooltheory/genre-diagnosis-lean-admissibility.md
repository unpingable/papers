# Genre diagnosis: admissibility kernels (external)

**Status:** UNRATIFIED working note. External-model diagnosis preserved
nearly verbatim plus a thin custody/falsifiability layer.
**Date filed:** 2026-06-09.
**Provenance:** Fable (Anthropic web, same-day release 2026-06-09, common-mode
with Claude Code) + chatgpt synthesis. Two Claude-family models, one
non-Claude critic. **Common-mode caveat** ([[feedback-claude-common-mode-synthesis]]):
the framing sentences here have not been cross-checked by a non-Anthropic
model. Treat the keeper sentences as candidate taxonomy, not ratified.
**Custody:** working note in `working/tooltheory/`. Not promoted. Not
kernel-adjacent. Not a Lean module.

## The one-liner that survives compression

> **A countermodel-driven type discipline for claims: it uses Lean to
> decide which informal conversions are admissible, which need bridges,
> and which are forbidden.**

The load-bearing sentence Fable lands on:

> **Lean is not verifying a system; it is adjudicating a vocabulary.**

Three-slot taxonomy (chatgpt's compression):

- **Foo** — a static discipline for forbidden inference / claim conversion.
- **Bar** — countermodel-curated Lean kernels and named missing bridges.
- **Baz** — legal/doctrinal vocabulary, ops reliability scar tissue,
  proof-carrying claim custody, and human/AI audit loops.

The longer description for an outside reader:

> Doctrine under version control with a proof assistant as the merge
> gate. The proofs certify the invalidity of specific informal inferences
> rather than verify any implementation.

## Why "topology" is wrong

Topology is closure structure. This artifact's signature move is
*refusing* closure — no transitive composition across seams, absence as
first-class, name-similarity refused by default. The correct term is the
boring one: **seam graph** or **conversion graph**. The word "topology"
should be retired from working framings, in favor of one of those.

Other words explicitly retired by the project's own discipline: "calculus"
(the refused unifier across kernels), "formal verification" (nothing is
implemented), "proof-carrying governance" (no runtime gate consumes a
checked term).

## Fable's full diagnosis (preserved)

### 1. Genre

Reject *formal verification of an implementation* outright: nothing is
implemented. The stores are `axiom Type` with no behavioral laws, no
code is refined, no extraction exists, and the named consumers (NQ,
standing, agent_gov) are bound to the kernels by comments only. Reject
*proof-carrying governance*: no governance process carries these proofs;
no runtime decision is gated by a checked term. *Legal/doctrinal
formalization* is half right but inverted — legal formalization encodes
pre-existing doctrine, whereas here the doctrine and the formalization
are co-generated, and the theorems frequently *produce* the doctrine
(the keepers are distilled from the proofs, not the reverse).

The accurate genre is a hybrid: a **theorem-indexed epistemic boundary
map** whose entries are certified by **countermodel curation**. The
dominant theorem shape across the repo is non-implication — `Surface ⇏
Substance`, pinned either by an existential countermodel in a bespoke
miniature or by a blocking theorem over a small total function. "Receipt
calculus" is what the prose wants it to be; "calculus" is the word the
repo itself banished, correctly. And there is a second genre running
underneath that the README doesn't name: Lean as a **commitment device
for a human–AI writing loop**. The custody classes, claim registers,
promotion-by-aggregator-import, and the audits in this conversation are
configuration management of *claims*, using the proof assistant's
determinacy to discipline a multi-model collaboration that would
otherwise drift. That second genre is unusual and load-bearing.

### 2. What Lean does here that prose cannot

- *Making non-edges first-class*: genuinely — `selectivity_does_not_imply_encapsulation`,
  `visible_green_does_not_imply_recovery_margin`,
  `fluency_does_not_witness_settlement` are machine-checked
  non-implications. This is the most honest Lean usage in the repo.
- *Exposing stale dependency arrows*: demonstrated empirically — the
  `NondegenerateStoreSemantics` finding existed because a Lean proof
  term has a fact of the matter about what it consumes. Lean made the
  discrepancy determinate; an auditor still had to read the term.
- *Forcing missing bridges to be named*: partially — the naming is
  prose discipline, but Lean makes the absence consequential inside
  Lean, because you cannot elaborate through a bridge that doesn't
  exist.
- *Preventing silent conversions*: true within a module
  (both-proofs-by-construction in `AuthorizedStep`, non-exhaustive-match
  enforcement in `classify`, obligation fields discharged at
  construction); across modules it is documentary.
- *Making rhetoric fail at compile time*: only rhetoric about the toys.
  Rhetoric about the world — which is what the keeper sentences are —
  compiles fine, because it's in comments.

Honest summary: Lean supplies **determinacy** (every claim about a proof
has a checkable answer) and **non-vacuity certification** (the wound
axioms in `AuthorizedNotSafe` are shown jointly satisfiable by a
parallel concrete model, so the wound is inhabited, not vacuous). Prose
provides neither.

### 3. Strongest real contribution

Not "formal rigor." Two specific things:

1. The **two-file wound pattern**: state a gap axiomatically over the
   abstract surface, then discharge its consistency in a parallel
   concrete miniature, axiom-free, so the negative result is certified
   non-vacuous (`AuthorizedNotSafe` + `Witness`, `AuthorizedStepNotSafe`
   + `Witness`). What rigor buys: it converts "this inference seems
   wrong" into "here is a complete, finitely auditable world where the
   premise holds and the conclusion fails," an artifact that can be
   wrong in exactly one way (misencoding) rather than the many ways an
   argument can be wrong.

2. The **model-dependence result in `CorrectiveBoundary`** — refusing
   to assert or deny the corrective-then-forward existential and
   instead exhibiting both answers in disagreeing models of the same
   abstract signature, thereby proving the abstract kernel *cannot*
   settle the question. Correct metamathematical hygiene at miniature
   scale, replacing a `sorry` with something strictly more informative
   than either resolution would have been.

Honorable mention as practice: promotion-as-aggregator-import with
regression-checked custody markers — claim-status as versioned,
mechanically checked state.

Evidence the apparatus works: it has caught real errors against its
authors' intent — the falsified strict-monotonicity hypothesis, the
dependency-arrow docstring, and two manufactured receipt names refuted
by grep in this week's audit loop.

### 4. Weakest, most vulnerable claim

The toy-to-world mapping, in three escalating forms:

- **Mildest: the keepers.** "Visible green does not entail recovery
  margin" as a logic claim is exactly what the theorem proves — the
  predicates are independent in at least one model — but the keepers
  are written to sound like operational facts about dashboards, and
  the theorem says nothing about any dashboard.

- **Middle: graph theater risk** in the inventory and router. The
  router's negatives quantify over a four-edge hand-encoded relation;
  its own refusal note says so; the vulnerability is downstream
  citation of `authorized_does_not_route_to_safe` as though it
  quantified over the repo. No reflection theorem binds the encoding
  to the modules.

- **Sharpest, because demonstrated live: receipt-shaped noise.** The
  house naming convention is so legible that it is spoofable — a
  collaborator minted `amend_policy_preserves_*` names that
  pattern-match the style perfectly and (at the cited tree) did not
  exist. A receipt vocabulary trains every participant, human and
  model, to produce receipt-*shaped* utterances; the system's
  credibility then depends entirely on the grep discipline being
  applied every time, by someone. **That is a structural
  vulnerability of the method, not an incident.**

### 5. The skeptical reviewer, steelmanned

*(Preserved verbatim per chatgpt's "do not sand down" instruction. This
is the immune system.)*

> This is a collection of trivially true theorems about toy models the
> author also wrote, organized by an elaborate self-referential
> bureaucracy. The proofs are `rfl`, `decide`, and one-step
> contrapositives; the deepest is a strong induction over `Nat`.
> Non-implication between independently defined abstract predicates is
> the *default state of logic* — constructing a two-field record where
> they diverge is an undergraduate exercise, so each "refusal kernel"
> certifies something that was never in doubt. No theorem concerns any
> system that exists; the connection to NQ and agent_gov is entirely
> in comments; there is no refinement, no scale, no adversarial model,
> no completeness result. The intellectual content lives in the prose
> taxonomy, which is genuinely interesting — and Lean functions as a
> credibility prosthetic, borrowing the authority of formal
> verification while doing none of verification's hard work. The
> custody apparatus is an aesthetic of rigor wrapped around
> keeper-claims that are unfalsifiable management aphorisms. Worse,
> the validation loop is closed: the same human–AI process that
> generates the doctrine generates the audits that bless it, and the
> DOIs flatten the careful ANNEX/PUBLIC distinctions for every
> external reader.

Fable's gloss: that reviewer is smart, and roughly sixty percent right.

### 6. What survives that reading

The parts where the steelman concedes the project's actual claim while
attacking a claim it doesn't make.

- "Non-implication is trivially constructible" — yes, and the project's
  claim is that *these specific named inferences* are invalid, for
  which a minimal countermodel is the correct and complete certificate;
  triviality of the proof is a feature in a certificate.
- The determinacy survives: each forbidden inference is pinned with an
  auditable witness, sorry-free in the wired set.
- The construction-time obligation pattern survives as design.
- The model-dependence result survives outright; it is correct at its
  scale and the scale is stated.
- The custody mechanics survive as practice with regression receipts.
- The closed-loop charge is partially broken by the record: the loop
  has repeatedly ruled *against* its participants — including against
  the reviewing model, twice this week.

What does **not** survive: every world-claim, the router negatives as
repo claims, the inventory as current, and the word "topology."

### 7. What this must not become

- A **unified calculus**. The federation becomes legible to outsiders
  only as a system; systematizing requires the cross-kernel
  identifications the cuts forbid; the unifier would have to identify
  five things named `Step` and four named `defendedValue`, and each
  identification erases a refusal surface. The no-unifier note is
  load-bearing architecture, not modesty.
- A **vocabulary mill**. Refusal kernels proliferate because the
  marginal countermodel costs an afternoon, while binding to any
  operational consumer costs months and keeps not happening, until the
  genre cheapens and the corpus becomes a thesaurus of refusals
  nothing consults.
- **Rhetorical credibility laundering**. The moment someone says "we
  have proven authorization doesn't route to safety" about a deployed
  system, the project has become the thing its own kernels exist to
  refuse.

### 8. Short descriptions

**For a formal methods person:** a federation of small, sorry-free Lean
4 models — countermodels and constructor-gated abstractions over
deliberately opaque types — certifying the invalidity of specific
informal inferences rather than verifying any implementation, with
claim status managed as regression-checked, versioned metadata.

**For an infrastructure/ops person:** machine-checked postmortem logic
— tiny formal models pinning down exactly why dashboard-green doesn't
mean recoverable, authorized doesn't mean safe, and a survived shift
doesn't mean closure, each "you can't infer that" backed by a checked
counterexample instead of a war story.

**For an AI governance person:** a typed inventory of forbidden
shortcuts in authority and evidence handling, each shortcut blocked by
a machine-checked counterexample and each missing safeguard named
rather than silently assumed — built as substrate for agent-governance
tooling, and explicitly not a verification of any deployed system.

**Synthesis:** doctrine under version control with a proof assistant as
the merge gate — Lean is not verifying a system, it is adjudicating a
vocabulary, and its real function is to make the project's claims
capable of being wrong in public, which they occasionally are, which is
the point.

## Local falsifiability check

Quick proof-complexity probe against the wired Admissibility set
(`/home/jbeck/git/lean/LeanProofs/Admissibility/*.lean`, 2026-06-09):

- Proof-line endings counted with `grep -c` for `rfl$|decide$|by$`:
  ParameterizedMerge 53, CorrectiveBoundary 31, NumericalAdmissibility
  23, StateTransition 22, RefusalPropagation 17. Suggestive of a heavy
  `rfl`/`decide` mix.
- `induction`/`cases` invocations: ParameterizedMerge 18,
  CrossBoundaryExposure 11, ClosureEligibility 8, LocalBoundary 7,
  Authority 6.

**Verdict on the skeptical reviewer's "rfl, decide, one-step
contrapositives" claim:** directionally accurate (the bulk of the
trapdoor/isolation/blocking theorems are indeed one-liners), but
quantitatively soft — non-trivial structural inductive proofs do exist
(ParameterizedMerge in particular carries real induction). The
skeptical reviewer overstates by treating "the majority are simple" as
"the deepest is a strong induction over Nat." That said, the qualitative
shape of the claim survives: this is a corpus of small certificates,
not a body of deep theorems. The defense is the one Fable already gives
in §6 — triviality of the proof is a feature in a certificate.

## What would actually falsify each load-bearing claim

The diagnostic is more useful if its claims are falsifiable. Hooks:

- **"Lean adjudicates a vocabulary, not a system."** Falsified if a
  Lean theorem here ever gates a runtime decision in agent_gov / NQ
  (not a comment, an actual proof obligation). Currently: no.
- **"Two-file wound pattern is the strongest contribution."** Falsified
  if a single wound miniature is shown to be inconsistent (jointly
  unsatisfiable axioms), making the wound vacuous after all.
  Currently: the consistency discharges in the Witness files are
  axiom-free and have been re-checked this week.
- **"The skeptical reviewer is 60% right."** Falsified upward if a
  promotion gate refuses a published kernel for reasons traceable to
  this corpus's own discipline rather than the reviewer's intuition.
  This *has* happened in audit loops; the percentage is impressionistic.
- **"Receipt-shaped noise is a structural vulnerability, not an
  incident."** Falsified if the grep discipline is consistently
  applied without the receipt-integrity rule needing to fire.
  Currently: it fires.
- **"The word 'topology' is wrong."** Falsified if the corpus ever
  proves a transitive composition law across module seams without
  per-edge theorem backing. Currently: explicitly refused.

## Recommended scope of this note

- File as a self-limiting description, not a manifesto.
- Cite from when the framing escapes the corpus's own discipline (e.g.
  when a reader calls it "verification" or "topology").
- Do NOT promote into kernel-adjacent docs (README, PAPER-MAP,
  CLAIM-REGISTER). The framing here is candidate, single-vendor,
  external. The repo's own self-descriptions stay primary.
- Reuse the skeptical reviewer section as the standard "things this
  isn't" pre-emption when introducing the corpus to a new audience.

## Doctrine links

- [[feedback-claude-common-mode-synthesis]] — this note is two Anthropic
  models in agreement, one non-Anthropic synthesis on top. The phrases
  most likely to be common-mode artifacts: "merge gate," "doctrine under
  version control," "adjudicating a vocabulary." The artifact-level
  observations (two-file wound, model-dependence, custody mechanics)
  are inspectable and survive.
- [[project-no-unifier-without-laundering]] — Fable's "must not become a
  unified calculus" (§7) is a restatement of this doctrine in genre
  language. Compatible, no new content.
- [[feedback-verdict-compression]] — the receipt-integrity rule, which
  caught two manufactured names this week, is the freshness-axis
  discipline applied to status moves. Composes with the failure mode
  Fable identifies in §4.
