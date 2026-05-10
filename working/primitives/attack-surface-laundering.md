# Attack-Surface Laundering (candidate primitive)

**Status:** candidate primitive / probe. **Narrow formal kernel identified (see *Formal kernel* below) — full discourse dynamics remain honest-boundary.** Not ratified; not in the active primitive notes table; not registry-listed. *Stay of execution, not crown.*
**Kind:** transition / attractor (a transition in the *shape* of a dispute that creates an attractor in the *resolution* of the dispute).
**Originated:** 2026-05-10 multi-model conversation surfacing the pattern from the Chrome / Gemini Nano critique by Hanff (and several adjacent recent pieces conflating model-generation costs with deployment).
**Adjacent:** [Loop Capture](../loop-capture.md) (discourse-layer cousin of admissibility capture); admissibility family; falsification guardrails.

## What it names

A hard accusation acquires negotiable surfaces through the addition of true auxiliary claims, until the compound accusation inherits the negotiability of its softest component.

This is **not** a malice claim. The accuser is typically acting in good faith — the auxiliary claims are factually defensible. The trap is **remedy contamination**, not falsehood.

> *Attack-Surface Laundering is an accusation-design failure mode.*

## The three-piece schema

The primitive is most useful as a paired mechanism. Three components, all named together:

### 1. Attack-Surface Laundering *(the offensive-side accusation-design failure)*

> Adding negotiable auxiliary claims to a hard violation until the compound accusation inherits the negotiability of its softest component.

Mechanism: a hard claim (categorical authority violation) gets bundled with soft claims (continuous-variable harms — emissions, bandwidth, welfare, embodied carbon, etc.). Each soft claim is true. Each soft claim has its own remedy surface. The compound accusation now has more remedies than it has claims, and the institution can settle one of the soft remedies while leaving the hard violation intact.

The failure is in the *argument geometry*, not the *facts*. The added claims may all be defensible. They still distribute the attack surface.

### 2. Gate-to-Metric Substitution *(the defensive-side response loop)*

> Replacing a categorical admissibility gate with a continuous optimization target, so the contested action continues under mitigation rather than stopping under refusal.

Mechanism: the institution accepts the soft claims, treats them as the actionable accusation, and reframes the dispute as an optimization problem.

```text
authorized?  yes/no                     ← original gate
              ↓
minimize harm  subject to continuing the behavior   ← substituted metric
```

The "subject to continuing the behavior" clause is the load-bearing wrong. The system can now improve the violation indefinitely without ever stopping it.

This is the *response loop being redirected*. Attack-Surface Laundering creates the porous geometry; Gate-to-Metric Substitution exploits or inhabits it.

### 3. Denominator Capture *(the self-completing mechanism)*

> The good-faith correction loop that stabilizes the auxiliary metric while leaving the primary violation intact.

Mechanism: bad measurable claim attracts competent correction (SRE-brained, ESG-brained, "well-actually" merchants). The correction is locally correct — bad denominators *should* be corrected. But the correction migrates attention from the categorical claim to the auxiliary metric, completing the laundering without anyone intending to.

> *You do not need to run a counter-op when the attention market already evolves one.*

Denominator Capture is **not** a separate primitive — it is the mechanism by which Attack-Surface Laundering self-completes. It explains why the pattern works without requiring coordination, malice, or shills. The discourse organism selects for laundering geometries because debunking is faster than re-prosecuting.

## Why the three are paired

The full pattern requires all three:

1. *The argument is laundered* (Attack-Surface Laundering creates the geometry).
2. *The institution responds along the soft surface* (Gate-to-Metric Substitution).
3. *Good-faith correctors stabilize the soft surface* (Denominator Capture finishes the job).

Removing any one weakens but does not eliminate the failure mode. Naming all three is what makes the primitive prosecutable in retrospect.

## Formal kernel (narrow)

A knife-test against the laundering primitive surfaces a hard core that survives independently of the discourse dynamics. The full social phenomenon (why people accept the unsafe projection, why correctors stabilize the auxiliary surface, why attention migrates) remains honest-boundary. The narrow formal core does not.

**The core:** unsound discharge over compound claims with auxiliary remedy surfaces.

**Minimal algebra:**

```text
Claim
Remedy
addresses : Remedy → Claim → Prop

hard : Claim                    -- the protected/categorical claim
aux  : List Claim               -- auxiliary claims with their own remedy surfaces
compound = hard :: aux
```

**Sound discharge** for a protected hard claim:

```text
sound_discharge(compound, remedy) := addresses remedy hard
```

**Unsafe discharge:**

```text
unsafe_discharge(compound, remedy) := ∃ c ∈ aux, addresses remedy c
```

**Laundered discharge** — the failure condition — exists when both hold simultaneously:

```text
unsafe_discharge(compound, remedy) ∧ ¬addresses remedy hard
```

Plain English: a remedy exists that answers an auxiliary claim while leaving the hard claim untouched, but the dispute can still be projected as resolved.

**Sharper abstraction (claim-remedy surfaces):**

```text
surface(c) = { r | addresses r c }
```

The laundering move treats the *union* of remedy surfaces as if it were *discharge* of the compound claim. The safe rule is either *intersection* (a remedy must address every claim) or *protected-gate preservation* (a remedy must address the hard claim regardless of what else it addresses).

**Theorem-shaped sentence:**

> *Adding auxiliary claims weakly increases the union of response surfaces without necessarily increasing the valid discharge surface for the primary claim.*

That is the prosecutable risk shape, not the sociological outcome.

**The lossy projection.** The dispute's *true* state is a vector of per-claim resolutions:

```text
{ consent: unresolved
, carbon:  mitigated
, bandwidth: mitigated
, storage: partially-addressed }
```

The laundering bug is the projection of that vector onto a scalar — *controversy: addressed*. The projection is the bug. *Attack-Surface Laundering is a discharge-soundness failure under lossy verdict projection over compound claims.*

What survives: claim geometry and remedy/discharge logic. What does not: attention/discourse dynamics (those still need a discourse calculus that doesn't exist; that's Denominator Capture's territory and remains honest-boundary).

## Diagnostic battery

For any compound accusation against a powerful actor:

1. What is the **hard claim** — the binary, categorical, non-negotiable element?
2. What are the **soft claims** — continuous variables, harm measurements, welfare burdens, externalities?
3. Does each soft claim have its **own remedy surface**? (If yes: laundering risk.)
4. Can the institution **settle a soft remedy without addressing the hard claim**? (If yes: structural exit available.)
5. Is the soft-claim measurement **methodologically debatable** in a way that summons competent correctors? (If yes: Denominator Capture risk.)
6. Does the correction loop **terminate at the soft claim** or **continue back to the hard claim**? (The "keep-going" move; usually punished by discourse incentives.)

Operator rule:

> *Before adding a claim, ask whether it changes the remedy.*

> *A debunk is not an acquittal unless it touches the charge.*

## Worked case (compressed)

The Chrome / Gemini Nano push: a browser vendor silently distributed a multi-gigabyte AI runtime to user devices. The hard claim is **standing**: did Google have authorization to write that payload to user terminal equipment? That claim is binary and non-negotiable.

The auxiliary claims added in the critique: carbon emissions from the bandwidth, embodied carbon from SSD occupation, welfare burden on metered-data users in the Global South, ISP capacity strain. All defensible. All true to varying degrees.

Each auxiliary claim has its own remedy surface: greener CDNs, carbon offsets, unmetered-only delivery, model compression, delta updates. None of them address the consent question.

The competent correctors arrive on the auxiliary metrics: the kWh/GB factor is mid-band 2018, the SSD embodied-carbon allocation is methodologically questionable, the device-count assumption is fragile. All locally correct. All move the dispute away from the locked door.

The institutional exit is now available: publish a sustainability report, optimize delivery, declare the issue addressed. The consent violation continues, with metrics.

A long-form treatment of this case lives separately as a worked argument; this primitive is the structural extraction.

## Keepers

> *The consent claim is a locked door. The carbon claim opens a conference room.*

> *Do not let an admissibility violation become an optimization problem.*

> *A debunk is not an acquittal unless it touches the charge.*

> *An aggravating fact becomes dangerous when it changes the remedy surface.*

> *Carbon is evidence of scale. Metered bandwidth is evidence of burden. Storage pressure is evidence of consequence. None of them is the violation.*

> *Use artillery against distributed harms. Use a sniper rifle against standing violations.*

> *When your target has more mitigation surfaces than you have claims, the number of claims is working against you.*

> *Modern discourse does not need disinformation to derail power critique. It can synthesize derailment from engagement alone.*

Compact:

> *Stop prosecuting the packets. Accuse the institution.*

## Connection to Loop Capture

Gate-to-Metric Substitution appears structurally adjacent to Loop Capture's admissibility-capture surface (surface 4 of the five-surface taxonomy in [loop-capture.md](../loop-capture.md)). In both cases, a gate that should constrain action is reframed so continuation remains permissible:

- *Loop Capture admissibility capture* — the controller's internal admissibility predicate $A$ gets replaced by a captured $A'$; actions remain self-authorized while defended value decays.
- *Gate-to-Metric Substitution* — the dispute's framing of an admissibility gate gets replaced by an optimization metric; actions remain in-progress while the violation gets "optimized."

This is a **discourse-layer cousin**, not earned formal duality. The shapes rhyme; the formal connection has not been worked. (See Loop Capture's *Caveat on "dual"* for the same warning at the controller layer.)

The primitive's contribution to Loop Capture: where Loop Capture surfaces 1–5 describe how an internal control loop loses contact with reality, the discourse-layer cousin describes how *third-party accountability* against a captured loop can be redirected by the same shape of move at a different scale.

## Anti-scope clauses

This probe **does not**:

- Claim novelty against rhetorical / argumentation-theory prior art. The "compound claim weakens itself" pattern almost certainly has an older name in legal-strategy or argumentation literature; the contribution here is the control-theoretic framing of *Gate-to-Metric Substitution* as the paired defensive mechanism.
- Generalize to all compound claims. Some compound claims genuinely strengthen accusations (when each component independently prosecutes the same charge). Laundering is the *failure case* — when components prosecute *different* charges with *different* remedy surfaces.
- Provide a rule for when to add claims vs not. The diagnostic battery is a checklist, not an algorithm. *Before adding a claim, ask whether it changes the remedy* is the operator rule; the answer requires judgment.
- Promote any of the three mechanisms to standalone primitives without further forcing cases. Currently filed as one paired primitive with Gate-to-Metric Substitution as the load-bearing twin and Denominator Capture as the self-completing mechanism.
- Enter the active primitive notes table. Candidate status until at least one independent forcing case (a different worked example, ideally in a different domain) earns ratification.

## Open questions

- **Prior art in argumentation theory / legal strategy.** This pattern almost certainly has an older name. The control-theoretic framing of Gate-to-Metric Substitution is probably the genuinely new piece; the laundering-of-compound-claims pattern likely has a rhetorical-tradition cousin. Worth a sniff test before any external publication of the primitive.
- **Should Gate-to-Metric Substitution earn its own primitive note?** Currently paired with Attack-Surface Laundering. If a forcing case appears where Gate-to-Metric Substitution operates *without* preceding compound-claim laundering (institution self-substitutes the gate without external pressure), the pairing breaks and Gate-to-Metric Substitution wants its own entry.
- **Lean staging / formalization boundary.** Gate-to-Metric Substitution may have a clean Lean target, likely as an instance or discourse-layer cousin of Loop Capture's *Admissibility Capture Theorem*: an action may satisfy a captured admissibility predicate while violating the uncaptured one. The sharper home is probably `WitnessInvariance` / `EncapsulatedWrt`, treating a metric as a witness whose perturbation class is misaligned with the gate it claims to support — *a metric can only testify for a gate if its invariance/perturbation class matches the gate's admissibility boundary.* For Attack-Surface Laundering itself: full laundering dynamics are honest-boundary, but a narrow formal kernel exists as remedy-surface / discharge-soundness machinery (see *Formal kernel* above). Do not stage until Gate-to-Metric or Loop Capture earns the parent formalism; the laundering kernel is a candidate child once a parent formal structure exists. Denominator Capture is an honest-boundary case unless a separate discourse/attention calculus is ever earned. **Stage the deeper Loop Capture theorem first**; the Gate-to-Metric cousin rides along essentially for free once that lands.
- **Promotion criteria.** Earning ratification (moving from candidate-with-narrow-kernel to primitive proper) would require any of: (a) an independent forcing case outside the Chrome / carbon worked case, ideally in a different institutional domain; (b) a clean operational definition of *hard claim / auxiliary claim / remedy / discharge* that doesn't smuggle in the conclusion; (c) a proof-shaped result of the *adding auxiliary claims weakly increases response surfaces but does not necessarily increase valid discharge of the protected claim* form; (d) Gate-to-Metric or Loop Capture formal work making the parent structure real enough to host the laundering kernel as a child. The current narrow formal kernel earned a *stay of execution*, not a crown.
- **Generative test for the discipline.** *Before adding a claim, ask whether it changes the remedy* is the operator rule. Whether this can be operationalized as an actual pre-publication check (something like a remedy-surface diff against the original claim) is open.
- **Connection to falsification-guardrails doctrine.** The "*if you can't name the buffer, serialization mechanism, and domain-break condition, don't use 'metastable'*" discipline is structurally similar — both are guardrails against vocabulary that diffuses precision. Worth a pass on whether the two doctrines are siblings under a shared parent.

## Provenance

- **2026-05-10 origin.** Multi-model conversation prompted by the Chrome / Gemini Nano critique by Hanff. User noted at least two adjacent recent pieces conflating model-generation costs with deployment, indicating this is a recurring failure mode rather than a one-off. The sloppy-conflation pattern is one half; the structural primitive (laundering + substitution + capture) is the other.
- **chatty:** named *Attack-Surface Laundering* and *Gate-to-Metric Substitution*; produced the locked-door / conference-room / denominator-bleeding spine that anchors the keepers; tightened *offensive-side rhetorical move* to *accusation-design failure mode* (the good-faith framing); ruled Denominator Capture as subtype rather than separate primitive.
- **claude-2 (during conversation):** produced the compound-claim-distribution analysis (*every additional true thing is not additive pressure; it can become additional attack surface*); named the *keep-going* move as the discipline that distinguishes finished epistemic work from premature closure; surfaced the three-brain veto stack (actuary / SRE / claim-shape) as the prerequisite for the discipline.
- **user (operator):** caught the reverse-greenwashing dynamic before chatty did; pushed past the SRE-brain debunk reflex into "what does the correction do *to which claim*?"; named the structural-self-poisoning frame (*Boltzmann brains riddled with amyloid plaques*) that explains why this pattern doesn't require malice.
- **claude-code-papers (this file):** filed as candidate primitive in the field notebook; adopted chatty's tightened "accusation-design failure mode" framing; preserved Denominator Capture as named-but-not-crowned subtype; added the Loop Capture cross-link with scare-quoted "dual" per the loop-capture working note's existing discipline.
- **2026-05-10 knife test (post-filing).** User prompted chatty to test whether the *borderline* Lean-formalizability classification would survive contact with attempted formalization. Result: the full discourse dynamics remain honest-boundary, but a narrow formal kernel survives independently — *unsound discharge over compound claims with auxiliary remedy surfaces*, with claim-remedy surface algebra and lossy-projection diagnosis as the load-bearing structure. Status updated from *borderline / probably honest-boundary* to *narrow formal kernel identified, full discourse dynamics deferred*. *Knife hit bone, not crown.*
- Filed as candidate / probe with narrow formal kernel. Not promoted. Not registry-listed. No Lean staged. Worked-case substack draft handled separately by chatty; this file is the structural extraction only.
