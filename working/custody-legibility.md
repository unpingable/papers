# Custody legibility — second-invariant note (candidate)

**Status:** Candidate architecture invariant, 2026-06-03 evening.
**Live seam — expect amendments.** NOT ratified doctrine. NOT a paper.
NOT a Lean build task.
**Discipline:** file now; formalization may lead once a theorem or model clears
intrinsic scope, overlap, and non-vacuity review. Capability inventory is not an
automatic work commitment, and runtime integration remains separate.
**Companion notes:**
[`constitutional-governor-architecture.md`](constitutional-governor-architecture.md)
(architecture this lives inside),
[`validity-spendability-split.md`](validity-spendability-split.md)
(first invariant).

## Provenance

Surfaced 2026-06-03 evening from Claude-web's interrogation of the
constitutional-governor architecture. The question: *the linear
accountant is sovereign over spendability, but who holds the keys
to the accountant?* Cabinet engaged: ChatGPT (runtime-custody
reframe), DeepSeek (constitutional Lean route + SRE error-budget
adoption wedge), Agent Governor Claude (override management as
audit target), Claude-web (sovereignty regress, custody legibility
as shippable property, SWE/ops discipline split). Operator settled
the keeper and the two-invariant structure.

## The keeper

> **The override still exists; it just cannot be quiet.**

## Core claim

A harness cannot remove residual sovereignty. It can only relocate
custody. A defensible harness makes custody **legible**: any
privileged override, witness suppression, re-minting, lease reset,
or fence movement must emit externally anchored evidence outside
the actor's unilateral control.

The shippable property isn't safety — it's *custody legibility*.

## The residual sovereign (regress, not safety)

The architecture stack relocates sovereignty step by step:

1. Semantic governor: can be pleaded with (not sovereign).
2. Linear accountant: too dumb to plead with (sovereign over
   spendability — *but only because it doesn't read narrative*).
3. Whoever holds the accountant's keys: can re-mint, suppress
   witnesses, reset clocks (the real sovereign).
4. Whoever holds the key-holder accountable: ...

Every escape route confirms the regress rather than breaking it:

- **Hardware root of trust** relocates custody to HSM + key ceremony.
- **Threshold / m-of-n** diffuses the sovereign rather than removing
  it (the collusion threshold becomes the new one — shadow
  governance with a quorum).
- **Formal verification** proves the fence is well-built; silent on
  who can move the fence.

None of them reach a keyless system. They reach systems where the
key-holder is more exposed, more distributed, or more expensive to
be.

The regress doesn't terminate in safety. It terminates in *who
holds root.* Custody is the residual sovereign you couldn't
eliminate — you only ever pushed them further out.

## Custody legibility as the shippable property

Since you can't eliminate custody, the maximum-available property
is making custody *visible to a third party who wasn't in the room*.

The architecture buys this by making every override a witnessed,
externally-anchored, admissible event. The shippable claim is not:

```
the system is safe
```

It is:

```
unsafe acts are either impossible to spend or impossible to hide
```

Ugly. Correct.

> **You don't make the system safe. You make its unsafety
> attributable and costly.**

The category error all along: "true safety" was unavailable for the
same structural reason "sovereign governor" was. The impossibility
of the sovereign governor and the impossibility of true safety are
the same impossibility seen from opposite ends. Both bottom out in
custody; custody is held by someone; that someone is the
irreducible sovereign.

## The interferometer question (load-bearing falsifier)

The question that decides whether you've shipped the maximum
available or just a harness-with-extra-steps:

> **Can the override be silent?**

- If a sufficiently privileged operator can re-mint or suppress the
  witness *without producing a record that escapes their own
  control*, you're back to "trust the operator" and you've gained
  nothing structural.
- If the override necessarily mints a receipt that anchors outside
  the operator's reach, you've shipped the most that custody
  permits.

The seam to run the interferometer on: not whether the governor can
be talked out of its limits, but whether the *custodian* can act
without testifying against themselves.

## SWE / ops discipline split

The architecture has a discipline boundary that mirrors the layer
boundary:

**SWE owns the seam (build-time correctness):**
- Unforgeable capability envelope.
- Narrow descriptor (typed; no free-text pleading channel).
- Typed token (abstract `SpendToken`; no proposer-accessible
  constructor; see
  [`constitutional-governor-architecture.md`](constitutional-governor-architecture.md)
  § Constitutional formalization).
- No semantic regeneration path.
- Receipt ≠ token.
- Eligibility ≠ capacity.
- *Model alignment*, *policy language*, *prompt constitution*,
  *static refusal behavior* — all SWE concerns ABOUT THE SPEAKER,
  which is the wrong target. SWE owns the seam, not the speaker.

**Ops owns runtime custody (runtime correctness):**
- Accountant.
- Witness.
- Override receipts.
- Revalidation.
- Incident posture.
- Capacity exhaustion.

The field's mistake has been asking SWE to make the *speaker*
correct by construction. The feasible SWE job is making the *seam*
correct by construction. Construction-time correctness *proposes*;
runtime accounting *disposes*; and the channel between them must
be narrow and unforgeable.

The recursion worth keeping: **the discipline boundary has the
same shape as the layer boundary.** SWE/ops is semantic/accountant
one level up. The org chart recapitulates the architecture. The
same failure mode lives at both seams — if the propose side can
smuggle authority across into the dispose side, you've lost it
whether the smuggler is a jailbroken model or a SWE who shipped a
capability type rich enough to mint.

## The category error reframe

> **Agent safety is a runtime-custody problem misfiled as a
> build-time-correctness problem.**

Longer version:

> **The field keeps trying to make the speaker correct by
> construction. The tractable problem is making the custody
> boundary correct at runtime.**

Highest-level synthesis that survived the whole beating:

> **Do not prove the agent safe. Arrange the system so the agent
> cannot spend stories.**

That's the field's mistake in one line. The semantic-governor dream
(*train it to refuse, type it correctly, prove the contract*) is
the SWE dream: correctness-by-construction; get the rightness into
the artifact before it runs. The circuit-breaker stack is the ops
reality: assume the artifact is wrong, the operator is tired,
someone pushes the override at 3am, and build the accountability
machinery around that assumption.

Every "robust semantic governor" demo, on inspection, turns out to
be a harness: permission prompts, an allowlist, a sandbox, an
egress proxy, read-only mounts. The refusal isn't what holds; the
out-of-band boundary is. The whole empirical record of attempted
counterexamples is a record of harnesses, not governors.

Which is exactly why everything kept resolving to ops-shaped
artifacts. A harness is an operational artifact. SWE treats the
harness as a failure (*if we'd built it right we wouldn't need the
sandbox*). Ops treats the harness as the product, because ops has
never once believed you build it right.

## Error budgets as the adoption wedge

The adoption wedge that opens an ops org's door:

> **Linear accountant = error budget generalized from reliability
> to authority.**

SRE shipped the canonical "conserved quantity the semantic layer
can't argue past" twenty years ago. Product pressure, feature
urgency, the VP who really needs this launch — all semantic, all
persuasive, all powerless against a budget that's been spent.

The accountant covers, by family:

- Retry budget
- Mutation budget
- Blast-radius slots
- One-shot grants
- Tool-call allowance
- Egress allowance
- Override allowance
- Capability lease

Common property: **conserved spendability.** The error-budget
intuition transfers directly. You're extending the primitive's
domain (from reliability to authority), not asking ops to adopt a
cosmology.

This is the door-opener sentence, not "admissibility calculus" or
"ContractionHinge": *"It's error budgets for agent authority."*

## Relationship to the constitutional architecture

This note covers the **witness custody** domain of the constitutional
governor stack (see
[`constitutional-governor-architecture.md`](constitutional-governor-architecture.md)
§ "Build vs runtime: the third custody domain").

**Three custody domains with different hardness** (per Claude-web's
correction, 2026-06-03 evening — the domains are NOT parallel):

1. **Runtime custody (capacity).** Arithmetic. Mechanically
   preventable. *Validity is not spendability.* (See
   [`validity-spendability-split.md`](validity-spendability-split.md);
   linear accountant is the enforcement mechanism.)
2. **Build custody (capability).** Semantic unless bounded by a
   frozen algebra of approved primitives. Hardness is a *dial*, not
   a constant: open authoring → semantic admission, legibility only;
   algebra-bounded → checkable; fixed registry → membership check.
   (See `constitutional-governor-architecture.md` § "The algebra
   dial.")
3. **Witness custody (override).** Held. Residual sovereign; never
   eliminated. Only ever made legible, attributable, costly to hide.
   *Custody must not be silent. The override still exists; it just
   cannot be quiet.* (This note.)

The hardness gradient (resting form):

> **Spend is counted. Capability is flow-checked or semantically
> judged. Custody is held and witnessed. Never pretend those are
> the same refusal.**

The cross-cutting principle underneath all three domains
(per `constitutional-governor-architecture.md` § "The substrate
clarification"):

> **No actor is authoritative over evidence or conserved state it
> authors.**

Custody legibility is the third instantiation: an actor's
self-authored claim that they didn't override is not authoritative
about whether they overrode. The witness has to come from outside
the actor's write set, not because the witness lives somewhere
specific, but because the actor cannot author their own
exoneration.

(Earlier drafts said *"checked or judged"* and elided the flow-typing
requirement; that elision smuggled a Tier-1 membership-allowlist
into the middle slot when only Tier-2 flow-typing actually
recovers checkable hardness. See
`constitutional-governor-architecture.md` § "Composition is
minting.")

Three failure modes, three *differently-hard* breakers. Runtime
gives you the accountant (arithmetic refusal). Build gives you the
signed-capability registry IF the algebra dial is set tight enough
— otherwise it gives you witness only. Witness gives you the
externally-anchored override receipt. The parallel grammar of an
earlier draft (*"may not mint capacity, capability, or custody"*) is
rhetorically clean and technically conflated; it goes here only as a
record of the symmetry error this domain framing corrects.

Honest compressed form:

> The agent may propose actions, spending, tools, and custody
> changes.
>
> **Spendability** is mechanically bounded: only the Linear
> Accountant may mint or consume capacity.
>
> **Capability promotion** is bounded only when novelty is
> constrained to a frozen algebra of approved primitives; otherwise
> it is a semantic admission event and must be witnessed,
> attributable, and externally reviewable.
>
> **Custody** is never eliminated. Privileged override, seam
> widening, witness suppression, or capability promotion must not
> be silent.

## What this is NOT

- NOT a paper. Same three-gate discipline as
  [[feedback-validity-spendability-paper-discipline]] applies here.
- NOT a Lean build task. The Lean route (per
  `constitutional-governor-architecture.md` § Constitutional
  formalization) would prove *witnessed_override_emits_receipt*-type
  theorems; not opened here.
- NOT a claim that you can eliminate the sovereign. The whole point
  is that you can't; the move is to make sovereignty *legible*.
- NOT a "SWEs are bad at this" claim. SWE owns the seam, which is
  the bounded thing they're uniquely good at. The mistake is
  pointing SWE thinking at the wrong layer.
- NOT a module rename. Existing kernel artifacts unchanged.
- NOT *finalized*. Live seam. Expect amendments.

## Runtime triggers and formal posture

Concrete consumer demand makes the runtime side actionable:

- **Agent Governor:** override management audit (per
  `GOV_GAP_VALIDITY_SPENDABILITY_SPLIT_001`) wants the
  override-receipt rule.
- **NQ:** witness layer specification needs the role-purity
  distinction and the external-anchor property for override
  testimony.
- **Wicket / WLP:** privileged-actor lease overrides need the
  receipt-not-token + cannot-be-quiet rule.
- **Audit / incident response:** real incident where the question
  *"who held root when this happened"* doesn't have a clean answer
  surfaces; this note is the candidate framework.
- **Lean work:** does not wait for those consumers. Once the override-receipt
  invariant has a coherent model, non-vacuous theorem target, and overlap/proof
  controls, the constitutional-formalization route may establish the contract
  first (see companion note).

Runtime integration is parked until a concrete target fixes the schema. Formal
investigation is currently unscheduled, not consumer-blocked. Live seam; amend as
needed.

## Cross-references

- Architecture this lives inside:
  [`constitutional-governor-architecture.md`](constitutional-governor-architecture.md)
- First invariant:
  [`validity-spendability-split.md`](validity-spendability-split.md)
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
- Memory: [[feedback-validity-spendability-paper-discipline]]
  (publication discipline applies)
