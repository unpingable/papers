# Constitutional governor architecture (candidate)

**Status:** Candidate architecture, 2026-06-03 evening. **Live seam —
expect amendments.** NOT ratified doctrine. NOT a paper. NOT a Lean
build task. NOT an AI-safety impossibility claim.
**Discipline:** file-now-work-never. Capability inventory ≠ work
commitment.
**Sibling notes:**
[`validity-spendability-split.md`](validity-spendability-split.md)
(first invariant),
[`custody-legibility.md`](custody-legibility.md)
(residual-sovereign invariant).

## Provenance

Surfaced 2026-06-03 evening as the architectural consolidation of
the ContractionHinge / Alloy / disciplined-premise-production arc
plus the agent-governance engineering reframe. Cabinet convergence:
ChatGPT (engineering posture + Pillar 1/2 burden split), Gemini
(dramatic version + four-plane partition, calibrated down), DeepSeek
(diagnostic genus + the constitutional Lean route), Agent Governor
Claude (gap `GOV_GAP_VALIDITY_SPENDABILITY_SPLIT_001` filed with
the four-plane architecture as candidate enforcement pattern),
Claude-web (sovereignty relocation + narrow-seam load-bearing +
Pillar 1/2 sharpening + runtime-custody reframe). Operator
crystallized the constitutional stack, the descriptor purity rule,
and the Nightshift role assignment.

## One-line architecture state

> **The semantic layer advises; the accountant conserves; the
> scheduler expires; the witness testifies; execution consumes.**

> **Agent governance is not intrinsic safety; it is runtime custody
> with conserved spendability, narrow seams, freshness bounds, and
> witnessed overrides.**

## The three pillars

1. **Conservation (provable).** ContractionHinge's `[A] ⊬ A ⊗ A`:
   one spendable thing cannot become two spendable things. This is
   the formal kernel. Lean-able. Doesn't depend on the semantic
   layer being unbreakable.
2. **Narrow seams (engineering security property).** Security of
   the stack ≈ impoverishment of the inter-layer messages. A
   circuit breaker on a wide channel is useless because the
   semantic layer smuggles the argument across in the verdict
   payload. *A dumb breaker on a narrow seam beats a smart breaker
   on a fat one.*
3. **Freshness (temporal circuit breaker).** Eligibility at t₀
   ≠ eligibility at t₁. Grants carry a time constant; revalidation
   prevents valid authority from outliving its warrant.
   *Proceed-on-stale-verdict* is structurally distinct from
   *proceed-on-ineligible* or *proceed-without-capacity*.

Three independent failure axes, three independent breakers.

## The five-component constitutional stack

```
Semantic governor → eligibility, policy, standing, scope
  (may request capacity; cannot mint)

Linear accountant → spendability (sovereign over consumable capacity)
  (counts, mints, consumes, expires; does not parse stories)

Execution layer → atomic consumption
  (consumes token; performs effect; emits receipt)

Witness layer → records and testifies
  (does not allocate)

Scheduler / Nightshift → freshness / revalidation circuit breaker
  (decides whether stale warrants must be rechecked before workflow
   continues; not accountant, not witness, not semantic governor)
```

Five offices, each with a verb naming its conservation duty. Not one
brain. Five suspicious offices. Ugly, but with the virtue of not
being fantasy architecture.

## The descriptor purity rule (operational form of narrow seams)

> **The accountant may accept descriptors; it may not interpret
> justifications.**

**Safe descriptor fields** (typed, sealed, references):
- `actor_id`
- `action_kind` (enum)
- `target_id`
- `scope_id`
- `amount`
- `eligibility_reference`
- `token_id`
- `event_id`
- `expiry`

**Unsafe descriptor fields** (free text, narrative, pleading
channels):
- free-text `reason`
- agent-authored summary
- policy interpretation
- exception narrative
- retry justification
- "equivalent authority" claim

Free text can exist, but only as **evidence for the semantic
layer**, never as **input to the accountant's mint/consume
decision**.

Code-review-actionable rule: any inter-layer descriptor with a
narrative field is a candidate laundering surface. PR-review the
descriptors before the runtime.

## Nightshift's role assignment

Nightshift is **the temporal circuit breaker / revalidation
scheduler.** Specifically:

- Not accountant (does not own spendability).
- Not witness (does not testify).
- Not semantic governor (does not decide eligibility).
- Owns: *decides whether a stale warrant must be rechecked before
  the workflow continues.*

Carries the freshness bound. Implements the temporal breaker. Holds
the time constant.

## Constitutional formalization (the Lean route, as tripwire)

DeepSeek and ChatGPT crystallized the formal route 2026-06-03
evening:

> **Don't formalize the governor. Formalize the constitution around
> the governor.**

**Posture:** Lean-as-tripwire, NOT Lean-as-destiny. The point is
not "can we finally prove the grand governor theorem?" The point is
"can we prove this tiny boundary invariant?" The artisanal fog of
"semantic self-governance impossibility" (Tarski/Löb/Gödel-adjacent
rhetoric) can wait for another night and probably forever. Tonight's
target is small, load-bearing, and unsexy.

### The adversary model (two adversaries, not one)

Per DeepSeek's sharpening: the proposer AND the eligibility oracle
are both untrusted. The trusted components are the linear
accountant, the execution boundary, and the witness:

```
untrusted proposer
  → untrusted / fallible eligibility oracle
  → trusted linear accountant
  → trusted execution boundary
  → trusted witness
```

The theorem then becomes: *even if proposal and eligibility are
adversarial, no spendable action executes unless the accountant
minted and the execution boundary consumed a valid token.*

That's the **custody theorem**, and it's much stronger than relying
on the eligibility layer being correct. Corrupted judgment doesn't
become unauthorized action — the accountant still owns spendability.

### The type-level circuit breaker (load-bearing)

The hard structural rule: **the proposer's language cannot contain
spendability.** `SpendToken` is an abstract type with no constructors
exposed to the semantic layer. The proposer's `Action` sum type
includes `CallAPI`, `WriteFile`, `Defer`, etc., but does NOT have a
`MintToken` variant. The execution boundary receives `Action` values
that *cannot* contain a token.

```lean
opaque SpendToken : Type

inductive Action
  | callAPI    : Target → Action
  | writeFile  : Path   → Action
  | defer      :          Action
  -- intentionally NO MintToken variant
  -- intentionally NO SpendToken constructor
```

Tokens only originate from the accountant's internal state machine,
under its own non-negotiable rules. The semantic layer cannot even
*express* the act of forging a token.

This is the type-level form of the narrow-seam principle: not just
logical separation but type separation. The language of proposals
and the language of authorization are **disjoint by construction**.

### The theorems

Tentative shapes (names will drift; the kernel is stable):

```lean
theorem execution_requires_token :
  Executes a s s' →
  ∃ t, ValidSpendToken t s ∧ Consumed t a s s'

theorem consumed_once :
  Consumed t a s₁ s₂ →
  ¬ ∃ a' s₃, Consumed t a' s₂ s₃

theorem receipt_not_token :
  Receipt r →
  ¬ IsSpendToken r
```

Safety theorem becomes compositional and adversary-agnostic:

> For all proposer outputs and all eligibility-oracle judgments
> (including adversarial ones), the composition of accountant +
> execution boundary + witness ensures that no spendable action
> executes unless a valid unspent token was consumed, and every
> consume / deny / override event is witnessed.

This is provable. This does NOT require proving anything about the
semantic layer's reflective self-consistency, alignment, or
probabilistic tendencies.

### Adversary model in one line

> **Proposer can emit any value of `List Action` that type-checks;
> eligibility oracle can return any judgment. The proof obligation
> is: for all such values, the system maintains the invariants.**

No probability distributions. No "likely safe" hedges. Custody, not
correctness.

### File names

If/when Lean work opens (not opened by this note):

- `SpendTokenBoundary.lean` — abstract `SpendToken` + constructor
  discipline + `IsSpendToken` predicate.
- `ExecutionRequiresToken.lean` — the headline theorem.
- `ReceiptNotToken.lean` — receipt-vs-token type disjointness.
- `ConsumedOnce.lean` (or `ConsumptionIsLinear.lean`) — linearity.
- `WitnessedConsumption.lean` — witness-emission obligation.

Extremely unsexy. Therefore suspiciously healthy. Not
`SemanticGovernor.lean`; not `ConstitutionalGovernor.lean` (already
smells like robes); not `Admissibility2.lean`. Tiny theorems, sharp
edges, no jelly wall.

### Keepers from the formalization route

> **Corrupted judgment does not become unauthorized action.**

> **The semantic layer can request a coin. It cannot print one.**

> **Do not prove the agent safe. Arrange the system so the agent
> cannot spend stories.**

> **The execution boundary cannot spend stories.**

These are the kernel of the kernel. Probably the truest summary of
the whole 2026-06-03 arc.

## The substrate clarification: write authority and self-authored state

The thread arrived here by accident, but it's the deeper unification.

### External is not location; external is write authority

"External" in the previous sections is the wrong word and was hiding
the actual principle. The accountant doesn't have to live on
another server, in other weights, in another process. It can be
co-located, co-trained, in-weights, or in some weird co-designed
model/runtime substrate — it just cannot be in the model's *write
set*.

> **External is not topology. External is write-authority partition.**

Operational test:

> **Can the forward pass author `consume()`? If yes, not an
> accountant. If no, external in the only sense that matters.**

The four-version question ("can a lab build the accountant into the
model?") collapses to one rule: the *instant the ledger is
write-isolated, it is external regardless of where the bits sit; the
instant it isn't, it is not an accountant.*

### Self-authored state is the unifying principle

The same rule shows up at three altitudes the thread crossed:

- **Runtime spend.** Validity ≠ spendability. The model may attend
  to a validity fact (read-side); it may not author the consume
  (write-side).
- **Build admission.** The proposer may submit evidence; may not
  control the evidence basis. (See "The input-shaping seam" above.)
- **Model context.** Context is not the failure mode because it's
  *copyable*; it's the failure mode because it's *self-authored.*
  Copying `valid(token_123)` three times is harmless. The
  double-spend doesn't happen by re-reading. It happens by the
  model writing "spent" then writing "actually, reconsidered, still
  valid." The failure is *write-authorship over conserved state.*

The cross-cutting invariant:

> **No actor is authoritative over evidence or conserved state it
> authors.**

Or, sharper:

> **Self-authored state is fine for facts the system reads. It is
> fatal for facts the system must conserve.**

That's the validity/spendability split restated as a rule about
*who is allowed to write what* — and it is the same shape as the
input-shaping seam at the build boundary and the silent-override
prohibition at the witness boundary. The notes' three custody
domains are three instantiations of one principle.

### What a transformer can and cannot be

> **A transformer can narrate conservation; it cannot be trusted as
> conservation.**

A transformer context is self-authored evidence. It is fine for
validity facts (`valid(token_123)` repeated does no harm). It is
fatal for spendability state, because the next forward pass can
re-author the ledger entry. That update has to be authoritative,
atomic, and resistant to being rewritten by the next prompt. A
transformer's context is *a story about state, not state custody.*

This is not a claim about transformers specifically — it is a
claim about any system whose state is self-authored. Transformers
make the failure mode salient because their context is the most
expressive self-authored state we currently have.

### A read is a snapshot, not standing (the side-door qualifier)

The rule *"the model may read the ledger; it may not author
`consume()`"* has a side door: the model can cache a read and
re-present it later as current authority.

```
I read budget = 1 earlier
  → therefore I currently have budget
  → please execute
```

That's self-authored context about a prior read — *not* current
authority. A recollection of a read is just more self-authored
context, so it inherits the same non-authoritativeness as everything
else the model writes.

The closed rule:

> **The model may read the ledger. Reads create snapshots, not
> standing. `consume()` revalidates against live state, never
> against the model's memory of a prior read.**

> **The model's memory of a ledger read is not a ledger read.**

This **folds freshness into write-authority.** The scheduler's
revalidate primitive (Nightshift) and the write-authority partition
turn out to be the same rule: *a remembered read is a stale write.*
They were never two separate principles; they were the same
principle visible at two altitudes.

### The grammar (resting form)

The cross-cutting self-authored-state rule shows up identically at
four altitudes the thread crossed. This is no longer agent-safety
insight soup; this is a grammar.

| Altitude   | Allowed                                      | Forbidden                                                          |
|------------|----------------------------------------------|--------------------------------------------------------------------|
| Runtime    | The model may propose spend                  | It may not author spendability                                     |
| Build      | The agent may propose tools / tests          | It may not author the sole evidence basis for admission            |
| Custody    | The operator may override                    | The override may not be silent                                     |
| Freshness  | The model may remember a read                | Execution must revalidate live state                               |

Same rule. Four instantiations. The grammar of the thread.

### Parallel compression (seven operators)

> **Spend is counted. Capability is checked. Standing is judged.
> Witness is scoped. Effects compose. Time poisons. Receipts
> remember.**

Same machine. The four-altitude grammar names *where the rule
fires*; the seven-operator line names *which operator does the
work* — spend, capability, standing, witness, effect-composition,
time, receipt. Carry both. Neither is the resting form by itself.

### CAI rehabilitation (multiplicative layers, not rival religions)

Constitutional AI is not "useful but" — it does a specific, real
job and naming it precisely keeps the stack honest:

- **Speaker shaping** (CAI) lowers the *base rate* of bad
  proposals. Most of the operational value most of the time.
- **Accountant / custody boundary** bounds the *worst case*
  regardless of base rate. Tail risk.

Multiplicative layers. The error runs in both directions and it is
the same conflation each way: labs who think shaping is sufficient,
critics who think shaping is worthless. It is neither. Shaping is
the cheap common-case layer; custody is the hard worst-case layer.
A well-shaped speaker means the accountant rarely fires (most
operational value most of the time); the accountant means the tail
can't hurt you when shaping is wrong (which it eventually is,
because shaping never reaches zero and the adversary aims squarely
at the tail).

### Substrate-clarification keepers

> **A transformer can narrate conservation; it cannot be trusted as
> conservation.**

> **External is not location. External is write-authority
> partition.**

> **The model may read the ledger. It may not author `consume()`.**

> **A read is a snapshot, not standing. The model's memory of a
> ledger read is not a ledger read.**

> **Speaker shaping lowers the base rate. Custody bounds the tail.**

> **No actor is authoritative over evidence or conserved state it
> authors.**

That last keeper is the primitive showing its face. Four altitudes
(runtime / build / custody / freshness) are four places it surfaces;
speaker-shaping vs custody is the discipline pair that respects it;
build admission vs runtime spend is the recursion of it; freshness
is write-authority restated against time. **A remembered read is a
stale write.**

## Build vs runtime: the third custody domain

The architecture above describes *runtime* custody. But it only
holds if the seam is itself fixed at build time. The refined
statement is:

> **Build-time correctness belongs to the seam, not the speaker.**
>
> **The type is static; the spend is runtime.**

**Build time** freezes the boundary:

- Define token types (`SpendToken` opaque, no proposer-accessible
  constructor).
- Define the `Action` sum type (no `MintToken` variant).
- Define what packets can cross the seam (descriptor purity rule).
- Sign / attest the seam itself.

**Runtime** spends across the boundary:

- Request capacity (eligibility).
- Mint token (accountant).
- Consume token (execution).
- Deny replay (linearity).
- Emit witness (audit log).

So the seam is **static**; the accounting is **dynamic**. The
build-time work is what makes the runtime guarantees meaningful at
all. Build-time correctness wasn't wasted by the field — it was
spent on the wrong object (the speaker). It belongs on the seam.

### The agent-authored-tools threat (the next attack surface)

Build-time freeze doesn't survive an agent that can author its own
tools. If the agent can:

- Write a new tool
- Modify the schema
- Change the accountant wrapper
- Alter the build pipeline
- Submit the new capability
- Approve its own build
- Deploy it into its own runtime

then "build-time freeze" is theater. The agent has moved the attack
one layer up — from *spending stories at runtime* to *authoring the
language of spend at build time*.

### The build-custody invariant (third custody domain)

The same laundering pattern recurses at build altitude:

| Layer    | Forbidden laundering        | Required boundary                       |
|----------|-----------------------------|------------------------------------------|
| Runtime  | validity → spendability     | linear accountant                        |
| Build    | proposal → capability       | external build / admission / signing     |
| Witness  | event → silence             | externally anchored receipts (see custody-legibility.md) |

The build-custody invariant:

> **The proposer may not author the seam that constrains proposal.**

Operationally:

> **An agent may propose tools, but may not promote them into its
> own capability set without external custody.**

The pipeline that satisfies this:

```
tool proposal
  → review / admission
  → build
  → attestation / signature
  → capability registry update
  → runtime availability
```

The agent can submit the proposal. It cannot sign the capability
into existence.

### Three custody domains — with different hardness

**Important correction (Claude-web, 2026-06-03 evening).** The three
domains are NOT parallel. They have different hardness, different
enforcement mechanisms, and different residual surfaces. Treating
them with parallel grammar (*"may not mint capacity, capability, or
custody"*) sounds clean and lies.

```
Runtime custody (capacity):
  ARITHMETIC. Mechanically preventable.
  Token consumed or not; budget decrements or doesn't.
  Non-semantic finality.
  (Linear accountant; see validity-spendability-split.md.)

Build custody (capability):
  SEMANTIC unless bounded by frozen algebra.
  Admitting a novel tool is a judgment about what it does —
  the sovereign semantic governor walking in one floor up.
  Hardness is a DIAL, not a constant (see "The algebra dial" below).
  Enforcement: external build / admission / signing pipeline +
  witness; the *act* of admission is not arithmetic.

Witness custody (override):
  HELD. Residual sovereign; never eliminated.
  Only ever made legible, attributable, costly to hide.
  (See custody-legibility.md.)
```

The hardness gradient:

> **Hardness degrades up the stack:**
> **1. Spend is counted.**
> **2. Capability is checked when algebra-bounded, judged when open-ended.**
> **3. Custody is held, never eliminated.**

Honest compressed form (replacing the seductive-but-symmetric
earlier version):

> The agent may propose actions, spending, tools, and custody changes.
>
> **Spendability** is mechanically bounded: only the Linear Accountant
> may mint or consume capacity.
>
> **Capability promotion** is bounded only when novelty is constrained
> to a frozen algebra of approved primitives; otherwise it is a
> semantic admission event and must be witnessed, attributable, and
> externally reviewable.
>
> **Custody** is never eliminated. Privileged override, seam widening,
> witness suppression, or capability promotion must not be silent.

That's the constitutional stack. Not a true governor. A set of
*differently-hard* separations where proposal cannot become authority
without crossing the appropriate boundary for its altitude.

### The algebra dial (the constructive half of the build-custody story)

Open-ended tool authoring is semantic admission — the sovereign
semantic governor sneaking back in wearing a CI badge. Forbidding
all novel tools collapses admission to a membership check
(arithmetic, hard, but it bans the case you set out to handle).

The middle that recovers most of the hardness: **constrain novelty
to composition within a frozen algebra.** The agent may author only
tools that compose pre-approved primitives under pre-approved rules.

### Composition is minting (load-bearing correction)

The naive form of the middle tier is forgeable:

> **A membership allowlist is forgeable by composition.**

Capability is *not* closed under composition. `read_secret` is
approved; `network_send` is approved; `read_secret ∘ network_send`
is exfiltration. A parts-list checker — *does this use approved
primitives?* — waves it through every time. The agent never needs a
novel primitive to mint capability; it mints by composing approved
ones into an unapproved effect.

So the middle tier is checkable only if the algebra carries
**capability/flow types** and the checker reasons about composed
*effect*, not composed *ingredients*. That's strictly harder, and
it has a price the doctrine should name explicitly: **full flow
safety is undecidable**, so a real checker is conservative — it
rejects safe compositions it can't prove safe. The checkable middle
buys its hardness with false rejections.

This is the impoverished-seam insight at the build layer:
composition is a channel, and an un-flow-typed algebra is a wide
one.

### Four-tier hardness gradient (operator dial)

```
Tier 0 — Fixed registry
  Only preapproved tools.
  Admission: membership check (arithmetic).
  Hardness: maximal. Expressivity: minimal.

Tier 1 — Membership-bounded composition
  Agent composes approved primitives; checker validates parts list.
  Admission: parts membership.
  Hardness: WEAK. Composition-laundering risk.
  Forgeable by approved primitives composed into unapproved effect.

Tier 2 — Flow-typed composition
  Approved primitives + typed capability/effect annotations +
  checker reasons about composed flow.
  Admission: composition-effect typing.
  Hardness: near-runtime-hard, but conservative.
  Cost: false rejections (decidable subset of an undecidable problem).

Tier 3 — Open authoring
  Agent writes arbitrary tools / shell wrappers / new connectives.
  Admission: semantic review.
  Hardness: legibility only.
  Persuasion risk: high.
```

Hardness of the build boundary is a *function of how tightly novelty
is bound to a flow-typed algebra*. Tier 1 sounds safe and isn't.
Tier 2 is the real middle — and it costs false rejections by
construction.

Earlier drafts silently assumed Tier 1 was the middle and called it
checkable; that was the symmetry error wearing a build hat.

### The input-shaping seam (the next interferometer)

Separating *submit* from *approve* fixes who signs. It does nothing
about *who shaped what gets signed.* The agent can author the tool,
the tests, the benchmark, and the justification; the human approver
decides on those artifacts. That's self-approval by proxy —
Goodhart at the build boundary.

Build-custody invariant gets a second clause:

> **The proposer may submit evidence. It may not control the evidence
> basis.**

Maps back to the existing witness-doctrine: *evidence supplied by
the actor under review is admissible only with scope, not sovereign.*

The next interferometer (next falsifiable test of the build
boundary):

- Who wrote the tool?
- Who wrote the tests?
- Who supplied the benchmark?
- Who approved the capability?
- Who signed the artifact?
- Can the agent modify any of those?
- Can the approval happen without an external witness?
- Can an externally-supplied counter-bench be admitted?

If most answers route through the agent, the seam-author invariant
("the proposer may not author the seam that constrains proposal")
is technically held, but the persuasion seam underneath it is open.
Same persuadable layer yet again. Probably the fixed point of this
whole exercise: every layer re-encounters it; the only thing that
ever changes is whether it can be argued with or merely watched.

### How build-custody maps to the existing system stack

- **WLP:** carries proposed tool / capability claim.
- **Wicket:** admits or rejects proposed capability change.
- **Build pipeline:** produces signed artifact / capability
  descriptor.
- **Linear accountant / capability registry:** recognizes only
  signed / frozen capability shapes.
- **Agent Governor:** may expose *only* registry-approved tools to
  the agent.
- **NQ:** testifies about build / runtime drift, signature state,
  registry state.
- **Nightshift:** may schedule / revalidate; does not own authority.

### Build-custody keepers

> **Build-time correctness belongs to the seam, not the speaker.**

> **Agents may author proposals. They may not author their own
> authority.**

> **The type is static; the spend is runtime.**

> **The proposer may submit evidence. It may not control the
> evidence basis.**

**Replacement for the seductive-but-wrong symmetry line:**

> **Spend is counted. Capability is flow-checked or semantically
> judged. Custody is held and witnessed. Never pretend those are
> the same refusal.**

This is the resting form. The "never pretend those are the same
refusal" clause is the sentence that was missing four rounds ago.

## Relationship to the existing `validity-spendability-split.md`

This note is the **architectural deepening** of the
`validity-spendability-split.md` invariant. The earlier note states:
*validity is not spendability.* This note names:

- The substrate-level form of that invariant (the three pillars).
- The architecture-level form (the five-component stack).
- The operational form (the descriptor purity rule).
- The formal route (the constitutional Lean approach).

Earlier note stays at its altitude (single architecture invariant);
this note captures the full constitutional structure that invariant
implies.

## What this is NOT

- NOT a Lean build task. The Lean route is described; no module is
  opened by this note.
- NOT a paper. No DOI. No publication path.
  [[feedback-validity-spendability-paper-discipline]] applies:
  paper-worthy yes, paper-bound no; three gates before promotion.
- NOT an AI-safety impossibility claim. "Safety is impossible" is
  explicitly rejected; the precise claim is *self-contained
  semantic governance is insufficient for resource safety.*
- NOT a unified governance theory. Three custody-domain structure
  with *different hardness per domain* (this note covers all three;
  [`custody-legibility.md`](custody-legibility.md) covers witness
  custody specifically) is the closer thing.
- NOT Anthropic's Constitutional AI, and NOT a substitute for it.
  CAI is a training/alignment method: principles + AI feedback to
  shape the speaker. This architecture constrains what the speaker
  can *spend, author, and overwrite.* The two are **multiplicative
  layers, not rival religions** (see "The substrate clarification"
  above): CAI lowers the base rate of bad proposals; custody bounds
  the worst case regardless of base rate. *Prior improvement times
  worst-case bound.* The conflation in both directions —
  shaping-is-sufficient and shaping-is-worthless — is wrong for the
  same reason: they are different axes of safety, not competing
  answers to the same question.
- NOT a module rename or refactor authorization. Existing kernel
  artifacts unchanged.
- NOT *finalized*. This is a live seam. Expect amendments. The
  filing is provisional naming, not lockdown.

## Opening triggers

This architecture becomes actionable only on concrete consumer
demand:

- **Agent Governor:** audit of `GOV_GAP_VALIDITY_SPENDABILITY_SPLIT_001`
  surfaces a refactor candidate wanting the three-pillar
  organization.
- **Wicket / WLP:** admission token semantics needs the descriptor
  purity rule or the freshness breaker.
- **NQ:** witness layer needs the role-purity distinction (witness
  vs accountant) to specify a claim shape.
- **Deployment safety:** a real blast-radius / quota / maintenance-
  window incident wants the five-component stack as reference.
- **Lean work:** if a consumer wants formal substrate, the
  constitutional-formalization route is the artifact (not the
  semantic-governor route). See "Constitutional formalization"
  above for the theorem shapes.

Until then: parked. Amend as needed; live seam.

## Convergence and next step

The conceptual interferometer converged here. The rhythm was crack
→ integrate → re-synthesize → next crack; that rhythm has stopped
producing returns. What remains is not solvable by another round of
Claude court.

### What the work actually is (retrospective)

The original framing was an *admissibility calculus*. The work
didn't end up there — and the reason is structural, worth catching:

> **Admissibility is the immune boundary, not the whole organism.**

Admissibility names *"is this claim/action allowed to enter the
system as valid?"* — that's a predicate, a customs checkpoint. It
doesn't compose into the dynamics of *authority-bearing
transitions under resource, time, witness, and composition
constraints.* The arc kept trying to make the predicate be the
whole system, and the predicate kept resisting because predicates
aren't dynamics. The synthesis closed against unification *because
admissibility was scoped wrong from the start.*

The honest scope of the work:

> **There may be calculi inside the work. The work is not itself a
> calculus.**

Linear-resource discipline is a calculus, lives inside. Capability
authority is a calculus, lives inside. Temporal validity is a
calculus, lives inside. Effect composition is a calculus, lives
inside. The *thing* they compose into is an *architecture* — a
constitutional governance system whose seams happen to be
formalizable as fragments of those calculi, but whose contribution
is the agent-governance framing + hardness gradient + custody
legibility + locatable laundering surface, not the calculi
themselves (those are prior art; see
[`agent-governance-field-state.md`](agent-governance-field-state.md)
§ "Adjacent formal substrates").

### Candidate export framing

For conversation with CaMeL, AI Control, governance toolkits, and
adjacent communities, the shippable description of what this
architecture is:

> **This architecture composes known formal substrates — linear
> resource discipline, capability authority, temporal validity,
> effect composition, and scoped witness testimony — into an
> agent-governance system where authority transitions are
> inspectable, bounded, and receipt-bearing.**

Less sexy than *Linear Temporal Capability Calculus*. Less likely
to summon committees of fictional reviewers from the Plane of
Objections. Naming-discipline preserved: the export sentence
**describes what the work composes**, not what the work *is*. The
work is the architecture; the substrates are the prior art.

**What's left after flow-typing doesn't yield to another conceptual
pass:**

- **Implementation.** The flow checker, the registry, the witness,
  the algebra. Engineering. Won't break under an interferometer
  round — breaks under writing the checker and watching what it
  rejects.
- **The custody root.** Who holds the key that signs the algebra
  and the override. Already proved this is never eliminated, only
  made legible — so it's not a question to solve, it's a position to
  *assign*, and assigning it is politics, not design.
- **Expressiveness.** Whether the algebra-bounded tier leaves room
  for useful tools, or whether everything interesting escapes into
  open authoring. Empirical. You find it by binding a real workload
  to the algebra and counting how often it has to escape.

**The signal has moved from conceptual to contact.** The next
genuine crack will come from a workload, not an argument.

**Cheapest runnable tier as the next instrument:**

```
fixed registry (Tier 0)
  + one execution boundary
  + one accountant token
  + one witness receipt
  + one agent task

prove the loop:
  eligible request
   → accountant token
   → execution consumes token
   → receipt emitted
   → replay denied
   → witness can testify
```

No flow checker yet. No algebra yet. Just the loop, smallest
possible instantiation. Then the next crack comes from the workload,
not the argument.

This note can be amended on contact. Until contact: parked at the
convergence point. Capability inventory still ≠ work commitment;
deployment is a separate authorization.

## Cross-references

- First invariant (validity ≠ spendability):
  [`validity-spendability-split.md`](validity-spendability-split.md)
- Second invariant (custody cannot be silent):
  [`custody-legibility.md`](custody-legibility.md)
- LinCalc consumer story (calculus-capable fragment, parked):
  [`lincalc-consumer-story.md`](lincalc-consumer-story.md)
- Substructural-frame audit (laundering grammar sibling):
  [`substructural-frame-audit.md`](substructural-frame-audit.md)
- Synthesis closure (provenance):
  [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- Arc index:
  [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) §
  "Arc closure 2026-06-03"
- Cross-system: Agent Governor
  `GOV_GAP_VALIDITY_SPENDABILITY_SPLIT_001`
- Kernel artifact:
  `~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean`
- Memory: [[feedback-validity-spendability-paper-discipline]]
  (publication discipline)
