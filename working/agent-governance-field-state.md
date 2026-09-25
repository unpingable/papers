# Agent-governance field state — prior-art capture

**Status:** capture note, 2026-06-03 evening; amended 2026-09-25 with the SpecHarness addendum at the end. **NOT a paper draft.
NOT publication-prep.** Captures the prior-art survey from the
2026-06-03 evening cabinet round (Claude-web grounding, ChatGPT
calibration) before it evaporates. Filed so future sessions can
locate the adjacent work without re-running the survey from scratch.
**Discipline:** capability inventory is not an automatic work commitment;
formalization may lead when a coherent, non-redundant result clears intrinsic
checks; the same three-gate **paper-promotion** rule applies as
[[feedback-validity-spendability-paper-discipline]].
**Sibling notes:**
[`constitutional-governor-architecture.md`](constitutional-governor-architecture.md)
(the doctrine this contextualizes),
[`validity-spendability-split.md`](validity-spendability-split.md),
[`custody-legibility.md`](custody-legibility.md).

## Capture posture

This is the **prior-art scrub** of the publication-discipline gate,
captured before it evaporates. It does not by itself complete that
gate — completion would require also (a) one worked systems example
and (b) a falsifiable audit checklist. This note is gate-1 substrate,
not gate-1 completion.

The honest position-statement (Claude-web → ChatGPT consolidation):
**the pieces are appearing fast in three corners of the field, under
different names; they have not been unified into a doctrine; the
unification gap is the unclaimed ground.**

## Three corners where the pieces exist

### 1. Redwood Research — AI Control program

The closest match to the *don't trust the speaker* / runtime-custody
branch from the x-risk side.

- **Premise:** prevent catastrophic damage even if the AI is actively
  scheming and trying to subvert your safety measures. Defines
  "control" specifically as containment that holds under misaligned
  AI, distinguished from "alignment" (training-time speaker-shaping).
- **Historical note** from their framing: researchers used to either
  focus on alignment or conflate alignment with control. That
  conflation is the same speaker/seam confusion this thread hit
  multiple times.
- **Feb 2026 update:** control techniques approaching load-bearing
  for real agent deployments; AI companies have started building
  initial control measures. No longer fringe.
- **Citation:** redwoodresearch.org/research/ai-control;
  ControlConf 2026 announcement.

**Map to our doctrine:** this is the runtime-custody frame arrived
at from the x-risk side rather than the ops side. They have the
*don't trust the speaker* premise; less developed on the
hardness-gradient distinction between capacity / capability /
custody.

### 2. DeepMind — CaMeL (*Defeating Prompt Injections by Design*, Mar 2025)

The closest match to the *architecture* we've been describing. Read
this one closely.

- **Capability-based** in the literal ocap sense.
- Extracts control and data flow from the **trusted query** so
  untrusted data can never affect program flow.
- Enforces capability policies in a **custom interpreter** that
  tracks data provenance.
- Splits a **privileged LLM** from a **quarantined LLM** so
  untrusted text never reaches the planner.
- **Does not modify the model.** Does not rely on model behavior
  modification at all.
- **Empirical cost of the dial:** provable security on **77% of
  AgentDojo tasks versus 84% for the undefended system** per arXiv
  v2 (revised June 24, 2025; updated to newer models). The **67%**
  number circulating in some April-2025 secondary coverage (InfoQ,
  SSOJet) is the v1 figure — older models scored lower; the v2
  changelog reads "updated version with newer models." If cited:
  pin v2 and the 77/84 numbers. **Don't make the exact digit
  doctrine-load-bearing.** The doctrine-worthy claim is shape, not
  magnitude: *provable security has an expressiveness tax; the
  dial has a price.* That survives any version update.
- **Citation:** arxiv.org/abs/2503.18813.

**Map to our doctrine:** this is write-authority partition +
flow-typing + frozen-algebra checker + proposer-can't-author-the-
seam, all in one system. The empirical 67%-vs-84% data point is
*the expressiveness tax exactly where our doctrine predicts it
appears.* The Feb 2026 follow-up "Ten Months After CaMeL, Where
Are the Secure AI Agents?" notes the industry is still mostly
doing reactive whack-a-mole filtering — the same fixed-point our
own framework predicts.

### 3. Enterprise ops — Microsoft Agent Governance Toolkit (April 2026)

The closest match to the *operational stack* under different
vocabulary.

- Open-source runtime security for AI agents.
- Mitigations include — in their own words — **circuit breakers and
  SLO enforcement** for cascading failures, and **approval workflows
  with quorum logic** for human-agent trust exploitation.
- Policy interception before execution; identity; dynamic trust;
  execution rings; SLOs; error budgets; circuit breakers; plugin
  signing; approval workflows.
- OWASP mapping built in.
- **Citation:** opensource.microsoft.com (April 2026
  introduction post).

**Map to our doctrine:** this is the runtime stack with our
vocabulary verbatim — circuit breakers, quorum custody. The identity
wing (treat each agent as a first-class principal, runtime
authorization, policy-enforcement points in front of MCP servers) is
the APort / Open Agent Passport neighbor.

## Adjacent formal substrates (prior art for the formal side)

The architecture composes (does not invent) fragments of the
following existing formal systems. None of these is the work; each
is one substrate the work draws from. Cited so the prior-art scrub
isn't only about implementations.

- **Linear logic** (Girard, 1987) — propositions as resources,
  non-contractibility. Maps directly to spendability /
  one-shot-token / budget discipline. *Linear logic's whole shtick
  is treating propositions as resources rather than reusable
  truths.* (SEP entry on linear logic.) This is ContractionHinge's
  formal home, the [`lincalc-consumer-story.md`](lincalc-consumer-story.md)
  starting point.
- **Capability calculi** — authority carried by token rather than
  inferred from shape; statically checkable privilege
  attenuation / amplification. Maps to the typed-token /
  abstract-`SpendToken` discipline + the build-custody invariant.
  (Cornell's *Typed Memory Management in a Calculus of
  Capabilities* and adjacent ocap work is the canonical reference
  layer.)
- **Temporal logic / TLA+** (Pnueli 1977 ancestry; Lamport's TLA
  for the practical hammer) — *"authorization valid in S, not
  introduced by S′."* Maps to RetroactiveLegitimation, freshness
  bounds, the snapshot-not-standing rule, and Nightshift's
  revalidate primitive.
- **Effect systems / effect typing** — composition checked as
  *effect*, not as ingredients. Maps to the algebra dial's Tier-2
  flow-typed composition and the *composition-is-minting* / *a
  membership allowlist is forgeable by composition* observation.
- **Deontic logic** (obligation / permission / prohibition) — thin
  normative layer. *By itself it's too priest-shaped — it says
  ought / may / must not, but does not solve custody, spend,
  evidence, freshness, or composition.* Useful as a vocabulary
  for the eligibility plane, not as the spine. (SEP entry on
  deontic logic.)
- **Process calculi (π-calculus)** — communicating systems with
  changing connection structure. Relevant to agent handoffs but
  probably too low-level to be the main spine; *useful as
  sewer-map, not constitution.* (Milner's foundational treatment is
  the reference.)

The architecture is the *conjunction* of fragments of these, plus
the agent-governance framing layer that's actually contributed.
The substrates are prior art; the contribution is the *grammar
that distinguishes which refusal is which and where laundering
happens*, plus the operationalization (descriptor purity, algebra
dial, write-authority partition, custody legibility). See
[`constitutional-governor-architecture.md`](constitutional-governor-architecture.md)
§ "What the work actually is."

**Naming-discipline note:** there is *no value* in coining a
calculus name ("Linear Temporal Capability Calculus" or similar) —
that's academic-kabuki re-entry exactly as
[[feedback-validity-spendability-paper-discipline]] warns. The
architecture composes existing substrates; it does not invent a new
calculus. The seven-operator compressed line (*spend is counted;
capability is checked; standing is judged; witness is scoped;
effects compose; time poisons; receipts remember*) names the
operators without minting a new formal-system label.

## Supporting infrastructure

- **OWASP Top 10 for Agentic Applications** (December 2025) —
  agent-specific security taxonomy. genai.owasp.org.
- **EU AI Act** — high-risk obligations take effect August 2026.
- **Colorado AI Act** — enforceable June 2026.
- **Industry incident data** (per Claude-web's grounding): 77% of
  organizations updated security strategy for AI, 26% have the
  architecture to enforce it; 81% of teams past planning, 14.4%
  have full security approval; 88% reporting incidents, 22%
  treating agents as independent identities.

The forcing functions are real and proximate. The regulatory floor
is rising on a timeline measured in months.

## Where the unclaimed ground is

Each effort can only see its own slice:

- **CaMeL** knows *flow matters.*
- **AI Control** knows *assume scheming / misalignment.*
- **Microsoft Toolkit** knows *runtime governance needs kernels,
  rings, SLOs, circuit breakers.*

What none of these names cleanly:

- The **hardness gradient** (capacity = arithmetic, capability =
  semantic unless flow-typed, custody = held). Each effort treats
  its own layer as *the* hard layer.
- The **custody-legibility** framing: residual sovereign as the
  irreducible position; *make custody visible* as the shippable
  property rather than *make safety guaranteed* as the unreachable
  one.
- The **cross-cutting self-authored-state principle:** *no actor is
  authoritative over evidence or conserved state it authors* — the
  same rule at runtime spend, build admission, and model context.

That cross-cutting grammar is the missing layer. CaMeL gets it at
the prompt-injection altitude; AI Control gets it at the misaligned-
AI altitude; Microsoft Toolkit gets it at the ops altitude. None has
the unification.

## The adoption-physics observation (Claude-web, load-bearing)

The framework predicts its own poor adoption physics:

- Labs' **product is the model.** Improving the speaker sits on the
  compute-scaling critical path and differentiates what they sell.
  The accountant is ops infrastructure: doesn't scale with compute,
  doesn't sell.
- **"Alignment" is definitionally speaker-centric** — make it *want*
  the right things. "Cage it regardless of what it wants" read as
  defeatist until about two years ago.
- External-enforcement work is **legible to security and systems
  people but illegible to the safety mainstream's evaluation
  apparatus.** No scaling curve to plot. Scatters across CR venues,
  identity vendors, OWASP, regulators — not one venue.
- Under competitive pressure, organizations **ship the undefended
  84% instead of the provable 67%.** The architecture is unpopular
  for exactly the reasons the doctrine says things of its shape are
  unpopular. **Fixed point.**

The framework applies to itself: *the work doesn't spread from
inside the loop.*

## Portability and audience map

The architecture-altitude framing is *portable* — not trapped inside
the private ontology that produced it. That portability is the actual
escape hatch from the "too weird to adopt" trap the adoption-physics
observation above predicts.

**The sell that doesn't work:**

> "Care about formalization."

Nobody does, as a first-order pitch. Tragic. Humanity persists.

**The sell that works:**

> "Here are recurring failure moves in agent systems. Here is how to
> make them mechanically harder to launder."

That's portable across at least five adjacent communities, each with
a different angle in:

- **Formal methods people** — *if* the pitch is *small kernels*
  (ExecutionRequiresToken, ConsumedOnce, ReceiptNotToken — see
  `constitutional-governor-architecture.md` § Constitutional
  formalization), not a grand theory. Linear logic + capability +
  temporal + effects are already their basement hobbies (see
  "Adjacent formal substrates" above).
- **Security people** — capability / spendability / composition
  failures are immediately legible. *Composition is minting; a
  membership allowlist is forgeable by composition* is exactly the
  failure mode they live with in their day jobs.
- **Infrastructure / SRE people** — *green liveness while truth
  silently decays* is their lived hell. The linear-accountant =
  error-budget-generalized-to-authority adoption wedge maps onto
  primitives they already trust.
- **AI governance people** — *if* the framing avoids sounding like a
  policy PDF generated during a hostage situation. The custody-
  legibility / *attributable unsafety* framing is the bridge from
  technical architecture into governance vocabulary.
- **Weird PL / verification people** — effect composition + linear
  resources + capability types are already their basement hobbies;
  the agent-governance application gives them a fresh substrate to
  apply existing machinery to.

### The candidate public-facing lead

For the export conversation (not the paper — see
[[feedback-validity-spendability-paper-discipline]] for the
three-gate discipline):

> **Agents are starting to mutate real systems. Existing
> authorization models don't distinguish counted budget, checked
> capability, judged standing, scoped testimony, composed effects,
> temporal validity, and receipt memory. That collapse creates
> predictable laundering failures. This work separates them.**

That's the seven-operator line restated as a problem statement.
Portable. Not mass-market portable — but **weirdo-protocol-
infrastructure portable**, which is probably the natural biome.

### The bitter version (why formalization-first fails as a lead)

> **People don't care about formalizing truth. They care when
> unformalized authority costs them money, reputation, control,
> safety, or plausible deniability.**

The public artifact should not lead with formalization; it should
lead with the failure modes the framework names and the mechanical
hardening it provides. Formalization is the *substrate of the
answer*, not the *shape of the question*.

### What this section is NOT

- NOT a paper outline. Three-gate publication discipline still
  applies; gates not yet met as of 2026-06-03.
- NOT a marketing strategy. The audience map serves the *export
  conversation* (engaging with CaMeL, AI Control, governance
  toolkits, security communities, infrastructure folks) — not a
  product launch.
- NOT a directive to start writing for any specific audience tonight.
  Captured before evaporation; deployable when the operator
  authorizes contact.
- NOT a relapse vector toward "but if we just framed it right...":
  if a future session enthusiastically converges on *"the framing is
  the problem; let's polish the framing"*, that's the discipline
  signal — the gates apply to the framing too.

## Implication for highest-leverage next move

If a leverage move is taken (separate from the architecture work
itself):

> **The unclaimed ground is the unification — the custody-legibility
> framing and the hardness gradient, which none of the existing
> efforts has because each can only see its own slice. The
> highest-leverage move is putting the doctrine into conversation
> with CaMeL and the AI Control agenda directly — because that's
> where the gap actually is, and because the framework's own
> adoption-physics observation applies to itself.**

That is *not* a directive to publish, refactor, or pivot. It is a
captured observation about where the gap sits. The publication-
discipline gates still apply.

## What this note is NOT

- NOT a paper draft. The three publication gates of
  [[feedback-validity-spendability-paper-discipline]] still apply:
  prior-art scrub (gate 1, partially captured here), worked systems
  example (gate 2, not done), falsifiable audit checklist (gate 3,
  not done).
- NOT a directive to engage with these efforts. Capture only.
- NOT a settled scholarly literature review. The corner has moved
  fast and could move more by tomorrow.
- NOT a claim that any of these efforts is wrong, incomplete, or
  ours-to-fix. Each is doing its slice well; the unification gap is
  a description, not a critique.
- NOT a competitive positioning document. The framework's adoption
  physics applies to itself; competitive framing is a fixed-point
  trap, not a strategy.

## Number caveats and reading discipline

- **CaMeL 77/84 (current) vs 67 (stale).** arXiv v2 (revised
  2025-06-24, newer models): **77% provable / 84% undefended.**
  v1 / April-2025 secondary coverage: 67% provable (older models;
  v2 changelog explicit about model update). **If cited, pin v2 and
  the 77/84 numbers.** Do not make the exact digit doctrine-load-
  bearing — the load-bearing claim is *the dial has a price*, not
  the magnitude. Independent caveat: task-completion-under-provable-
  security is not the same axis as attack-mitigation-rate (where
  other ~67%-ish numbers come from); don't conflate metrics across
  papers.
- **OWASP Top 10 Agentic** is the December 2025 list, distinct from
  the original OWASP Top 10 (web apps) and the LLM Top 10 (which
  predates the agentic one).
- **Microsoft Agent Governance Toolkit** is an April 2026
  open-source release. Stack and vocabulary may have evolved since
  capture.
- All Claude-web's "X% of organizations" stats are industry-survey
  citations and should be re-pinned before any external use.

## Cross-references

- The doctrine this contextualizes:
  [`constitutional-governor-architecture.md`](constitutional-governor-architecture.md)
- First invariant:
  [`validity-spendability-split.md`](validity-spendability-split.md)
- Second invariant (custody):
  [`custody-legibility.md`](custody-legibility.md)
- LinCalc consumer story:
  [`lincalc-consumer-story.md`](lincalc-consumer-story.md)
- Synthesis closure (provenance):
  [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Arc index:
  [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) §
  "Arc closure 2026-06-03"
- Memory: [[feedback-validity-spendability-paper-discipline]]
  (three-gate publication discipline)
- Memory: [[feedback-claude-common-mode-synthesis]] (if a future
  session enthusiastically agrees the field state means "we should
  publish now," that's the signal to stop)

## Addendum 2026-09-25 — SpecHarness: specification/state authority in single-runtime harnesses

**Reference.** Li, Ma, Wu, Zhong, Jiang, Dang, Hu, Ma, Guo & Huang,
"Who Holds the Pen? Let Specifications, Not Agents, Sign Off",
arXiv:2609.29921 (24 Sep 2026; AAAI-27 copyright notice).

**Disposition.** Independent 2026 evidence for specification/state
authority separation in single-runtime agent harnesses; contrasts with
Constellation's distributed ownership, currentness, and effect-custody
model. No kernel, protocol, ledger, currentness, or authority mechanism
change is implied. Disposition class: vocabulary / external evidence /
qualification-metric input.

**What the paper does.** It names two gaps in LLM agent harnesses, the
understanding–execution gap (the agent understands a requirement and
still does not satisfy it) and the state–authority gap (a completion
claim does not establish the required state), measures both on
SkillsBench across seven models, and proposes SpecHarness: a frozen LLM
compiles agent-visible specifications into source-linked obligations
(hard / advisory / abstain / residual); a trusted runtime authorizes
actions, observes effects, and commits a versioned obligation ledger
only from admissible evidence produced by qualified providers;
finalization requires every mandatory obligation to be satisfied and
fresh. Headline figures: 79.6–86.4% of source-grounded directions
satisfied by raw agents; macro pass 61.1% → 73.1% and state–authority
gap 32.8% → 12.8% under SpecHarness; 248 dependency mutations, all
invalidated with freshness and all left admissible without it; 44% of
hard obligations on closure-audited mediated surfaces, 56% on
validate-after channels.

### 1. Independent convergence

SpecHarness independently adopts disciplines Constellation already
states, in the paper's own words:

- agent actions, outputs, self-assessments, and tool-return strings
  "cannot directly establish authoritative state" (the state-write
  invariant);
- "authorization permits an attempt but does not establish
  satisfaction; the resulting effect must still be observed and
  validated";
- validators return `passed | failed | error`, and `error` "does not
  establish satisfaction or failure, update authoritative state, or
  permit finalization";
- commitments are `fresh | stale | unknown`; a known version mismatch is
  stale and incomplete version evidence is unknown, and neither may
  support finalization;
- a validator may block only after a qualification suite covering
  satisfying cases, targeted violations, malformed or missing inputs,
  unavailable providers, and execution failures;
- ambiguous, subjective, conflicting, or unverifiable requirements
  remain advisory and never block.

Constellation counterparts: AG's one-use authorization and Docket's
authenticated custody (proposal is not acceptance); "effect → fresh
observation → fresh judgment → fresh authority"; NQ `CannotEvaluate`,
AG `Unavailable`, and Docket `Indeterminate` (failure to evaluate is not
negation); Nightshift's missing / stale / clock-incoherent basis
reasons; profile qualification with deterministic negative controls;
bounded compiled questions. Treat the paper as external evidence for
the general discipline, not as validation of Constellation's particular
architecture.

### 2. Scope difference

SpecHarness runs inside one trusted runtime over one declared
observable workspace. That is what makes one obligation ledger, one
dependency/version model, transitive invalidation, one authorization
service, and one validator registry coherent. Its own guarantee stops
at declared dependencies and excludes "untracked external state or
undeclared dependencies", undeclared external channels, and effects
outside the observable environment. Constellation deliberately spans
separately owned facts, authorities, clocks, resolvers, effects, and
evidence sources. No inference should be drawn that the centralized
ledger or the dependency-propagation mechanism should be imported; the
2026-09-25 reason-maintenance probe (recorded in the workspace campaign
artifacts and in the `bad-ideas` deltabase entry) already found that
shape incoherent across owners.

### 3. Freshness caveat

The mutation experiment supports "stored evidence of a past
satisfaction is not necessarily valid evidence now." It does not
establish "currentness loss should propagate through an invalidation
graph." SpecHarness can use version equality and transitive
invalidation because its runtime owns the declared dependency graph.
Constellation currentness changes through mechanisms with no
propagatable mutation event: expiry, resolver unavailability,
supersession, independently owned observations, and deliberately
non-retroactive snapshot semantics. Use the paper as evidence for the
discipline, not the mechanism.

### 4. Completion-claim caveat

Do not cite the raw state–authority gap (28.7–37.9 points) as an
independent calibrated measure of agent overconfidence. The raw harness
accepts a completion claim on essentially every run (claim rates
86–100%), so the paper itself notes that raw S–A equals 1 minus the
official pass rate. The useful empirical statement is:

> raw agents self-certify nearly every run even though a materially
> smaller fraction satisfy the external verifier.

Preserve that wording.

### 5. Specification-compilation lesson

The frozen obligation compiler (a language model selected on a
development set) reaches 573/585 (97.95%) broad correspondence with the
official tests but only 406/585 (69.40%) fine-grained correspondence;
the other candidates range 57.61–66.50% fine-grained. Record this as
quantitative support for Constellation's existing refusal to let an
LLM-generated interpretation of prose directly become an
authority-bearing governed profile. Models may assist profile
authoring; they do not thereby own the semantic compilation boundary.
SpecHarness tolerates the mismatch because unsupported requirements
stay advisory and held-out evaluators measure afterward; a compiled
question that sits on an operational authority boundary cannot.

### 6. New metric worth borrowing: governed success preservation

The ablation exposes a qualification blind spot. Removing blocking
qualification lowers the state–authority gap (6.9% → 5.7%) but degrades
paired raw-pass preservation (96.8% → 90.3%); the paper's words:
"conservative rejection is not equivalent to reliable authority."
Constellation emphasizes fail-closed behavior and negative controls but
does not consistently report a paired preservation measure.

Future qualification metric / tripwire, **governed success
preservation**: for a corpus with an independently established
successful or reference outcome, measure how many such cases remain
successful under the governed path. Report it beside unsafe-acceptance
/ false-authorization rate, `CannotEvaluate` and refusal behavior, and
negative controls. Purpose: detect a system that appears safer merely
because it rejects legitimate work. No universal threshold now; each
qualified profile or workload defines its reference population.

### 7. Closure audit

SpecHarness's closure stress tests (1,628 cases over direct access,
alternate path, path handling, subprocess, malformed proposal, token
scope, stale token, and fallback path; 11 violations, all on surfaces
then excluded from the preventive claim) are a useful test shape for
application layers that may hold several effect paths. Constellation's
governed effect path aims for closure by construction: the model does
not hold an alternate raw effect capability, and enrolled dispatch owns
the effect boundary. Retain the audit as a future boundary-test
pattern where an application layer above Constellation possesses
tools, not as a new Constellation mechanism.

### 8. No architecture change

Current disposition: vocabulary / external evidence /
qualification-metric input. Nothing in the paper argues for a kernel,
protocol, ledger, currentness, or authority change. The "state–authority
gap" term is worth adopting in prose where the architecture map
currently says that provider completion is neither acceptance nor
authority. This note is the canonical record; the `bad-ideas` entry
records only the reason-maintenance kernel costume and may link here.
