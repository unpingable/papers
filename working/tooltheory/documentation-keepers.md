# Documentation Keepers — Fossil-Bed Pass

**Filed:** 2026-05-20 (separated from parked-leads register as a different artifact type).
**Shape:** documentation-legibility holding area, not a deferred-build register.
**Status:** TODO list for an external-reader-legibility pass on existing tool documentation (NQ, authority docs, related working notes).

## What this is

Keeper sentences that already capture existing doctrine but are sharper than what currently lives in the canonical docs. Filing them here keeps them visible until a documentation-housekeeping pass places them in their canonical homes.

**This is not new doctrine.** Every keeper here points to a load-bearing claim that already exists in code, working notes, or kernel modules. The work is *legibility*, not *invention*.

**This is not a deferred-build register.** A keeper that doesn't get placed during the next docs pass loses nothing structural; the underlying claim is already in place. The keepers exist to lower the cold-reader cost of entering the tool docs.

## Distinguishing from parked-leads

| Parked-leads | Documentation keepers |
| --- | --- |
| Deferred build candidates | Sentence-level filing work |
| Reopen triggers gate construction | Placement triggers gate documentation passes |
| Custody state: *preserved, non-binding, reopenable* | Custody state: *waiting for the next docs pass* |
| Lives at *handle* stage in gate stack | Doesn't live in the gate stack at all — it's downstream of already-earned doctrine |

If a keeper here turns out to *not* already be in place — i.e., the underlying claim is missing, not just unstated — it becomes a parked lead and migrates to `parked-leads.md`. Otherwise it stays here until the docs pass.

## Keeper inventory (seed)

Initial seed for the inventory. Add entries as they surface; trim as they land in canonical homes.

| Keeper sentence | Candidate canonical home | Underlying claim already in |
| --- | --- | --- |
| *"A log line is a witness statement, not substrate contact."* | NQ docs / witness-discipline section | NQ `cannot_testify` discipline + `WitnessInvariance` kernel |
| *"A cached answer is not fresh authority."* | Authority docs / freshness section | `Freshness.lean` + `working/primitives/stale-binding.md` |
| *"Claims are portable; authority is local unless a border-crossing substrate preserves it and a verifier honors it."* | Authority docs / serialization section (already present in `authority-observable-not-constructible.md`) | `working/authority-observable-not-constructible.md` |
| *"Once authority crosses serialization, it is no longer authority; it is a claim requiring verification/reminting."* | Authority docs / serialization section | Same — sharper compression of the gnat-lab finding |
| *"A collapsed surface may authorize inquiry. It may not authorize attribution."* | `SurfaceAuthorization.lean` docstring (already there) + downstream tool docs | `Admissibility/SurfaceAuthorization` |
| *"Narrative may route attention to receipts, but may not authorize mutation."* | Chronopolitics manuscript / authority docs | `FiatAdmissibility.classify` + `compression-becomes-authority-vocabulary.md` |
| *"Lucky is not authorized."* | Wicket / AG receipt documentation (when those land) | `working/primitives/post-hoc-authorization.md` + `SurfaceAuthorization` |
| *"Staleness says the map is old. Skew says which way it lies."* | `working/primitives/memory-skew.md` (already there) | `AxisSkew.lean` + `memory-skew.md` |
| *"A handle is not a predicate. A predicate is not a fixture. A fixture is not a kernel."* | Methodology docs / audit-procedure spec | Memory [[feedback-gate-stack]] |
| *"Not earned is a custody state, not a truth value."* | `working/parked-leads.md` framing section (already there) | `working/parked-leads.md` |
| *"People are naming the cliff; I'm formalizing the guardrail geometry."* | `admissibility-as-pre-authorization-layer.md` external-pitch section | `working/tooltheory/admissibility-related-work-map.md` § Overlap determination (Priority 0 synthesis) — the altitude-differentiation claim |
| *"The external world is converging on the problem statement. The corpus survives as a lower-altitude formal/refusal substrate, not as the first naming of the concern."* | `admissibility-as-pre-authorization-layer.md` external-pitch section | Same — the spike's strategic-result framing after codex + ChatGPT both pulled back the "first to name" overclaim |
| *"Lean as laundering detector."* | `admissibility-as-pre-authorization-layer.md` external-pitch section / README headers | `anti-laundering-doctrine-map.md` § The master frame (added 2026-06-05) — compression of the corpus's anti-laundering work, surfaced in 2026-06-04 multi-model side-quest exchange and kernel-overlap-audited as non-novel-substance/novel-compression |
| *"Indexed or it didn't happen."* | `anti-laundering-doctrine-map.md` § The master frame / methodology docs | The conversion-witness binding rule (master frame, source/target/surface/scope/issuer) — sharper one-line compression surfaced in 2026-06-05 workflow-layer extension exchange |
| *"Existential laundry."* | `anti-laundering-doctrine-map.md` § The master frame as the named genus | Generic genus name for "a witness exists somewhere, therefore treated as applicable here" — instances already in corpus (typed-provenance laundering, cross-boundary laundering, the DeepSeek warning), genus was previously unnamed |
| *"The bundle is not the join."* | `tooltheory/aggregate-witness-requires-join-candidate-2026-06-05.md` short-form doctrine line / external pitch | Workflow-layer compression: distributed satisfaction across partial witnesses is not unified admissibility; the join is the missing mediating object |
| *"The theorem is less important than the type you cannot construct."* | BoundaryTransit-style scratch file headers / methodology docs | `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` (witness-output-not-input + 8-way match) + typed-revocation pattern in `CrossBoundary*` — refusal as uninhabited argument position, not failed match at runtime |
| *"This evidence does not discharge that predicate."* | doctrine map § The master frame as the audit-unit framing; field-guide schema | The corrected formulation: not *"no witness exists"* (overstates) but *"the present evidence cannot discharge the required predicate without the indexed witness"* — the organization may have the witness elsewhere; produce it |
| *"X ≠ Y is a type joke; X cannot discharge P without witness W is a type accusation."* | doctrine map § The master frame; methodology docs | Sharpening of how the corpus phrases its refusals — accusation form is operational; equation-negation form is rhetorical |
| *"The object required for admissibility is not the object they are holding."* | external-pitch / README headers / `admissibility-as-pre-authorization-layer.md` | Single-sentence compression of the entire discipline (punchline form) |
| *"Ask for the missing witness."* | field-guide / meeting incantation register | The human-facing operational verb the laundering-detector framing collapses to — the audit unit is "what witness is missing" |
| *"Frankenstein Witness."* (field-guide name; Lean name is `AggregateWitnessRequiresJoin`) | `aggregate-witness-requires-join-candidate-2026-06-05.md` header / field-guide note | Workplace-demon name for the workflow-layer bundle-not-join failure. **Same object, two surfaces** — do not split into two candidates |
| *"Show the coupling witness, and show that the label isn't lying."* | `surface-deformation-requires-coupling-candidate-2026-06-05.md` short-form doctrine | The atomic-layer discipline for event-induced surface deformation — combines the indexed witness requirement with the well-typedness-of-labels requirement |
| *"No curvature without source."* | `anti-laundering-doctrine-map.md` § The conservation law / external-pitch headers | The brutal compression of the conservation-of-admissibility principle. GR analogy: a surface (predicate) cannot change without a traceable source term (event + witness) |
| *"Lawful backreaction has compact witnessed support."* | `anti-laundering-doctrine-map.md` § The conservation law | The formal compression — any modification to an admissibility surface is bounded by the coupling witness's envelope (after the event, inside scope, at or before horizon). Outside the envelope, admissibility is conserved |
| *"If the surface changed here, show the source term."* | field-guide / meeting incantation | The operational ask. Surface change is the curvature; the source term is the indexed coupling witness. Without the source, the change is laundering |
| *"Enum labels are testimony unless enforced by a well-typedness predicate."* | doctrine map § The master frame extension; type-design methodology | Sharper application of *"the label is not the witness"* to enum constructors. A `deformationType : ExpandAuthority` field is testimony about the transform until a `DeformationWellTyped` predicate threads it through the witness. Same disease as a self-asserted JSON field, one floor up |
| *"Behavioral equivalence, not intensional equality."* | doctrine map § The master frame extension; methodology docs | The corpus-wide rule for any kernel comparing admissibility predicates or surfaces: use `∀ c, left.admit c ↔ right.admit c`, not `left = right`. Intensional equality is a different question; the corpus refuses claims about *behavior*, not about *function objects* |
| *"Backreaction is managed insufficiency: the system permits bounded, witnessed loss of perfect recoverability so admitted events can lawfully deform the surface — charged gross, not net, because cancellation is not the same as never having spent."* | `surface-deformation-requires-coupling-candidate-2026-06-05.md` § Managed insufficiency; doctrine intros | The design discipline behind why deformation kernels need coupling witnesses at all. *Not* uncontrolled leakage, *not* perfect isolation — bounded, witnessed, temporary recoverability loss. The coupling witness is the licensed defect in perfect recoverability. The *charged gross, not net* clause carries the whole composition story: salami-slicing's signature is small net endpoint difference + large gross per-step spend, and net is fakeable by round-tripping verdicts while gross isn't |
| *"No fairy dust in the kernel."* | methodology / category-2 scratch headers | The anti-magic-cost discipline. Don't let undefined complexity / cost / budget primitives into the Lean until there is an actual model behind them. **Refined 2026-06-05:** flip-count IS an honest cost model (read off the transform's behavior, not asserted) — *visor comes off* once the witness carries `affordable : spend surface delta ≤ budget` over a derived count, not a stipulated value. Magic/complexity cost still isn't. The rule survives, but the line is *no asserted cost*, not *no cost* |
| *"Net is fakeable; gross isn't."* | `surface-deformation-requires-coupling-candidate-2026-06-05.md` § Composition Frontier; methodology | The salami-slicing signature: round-tripping a verdict (flip at step 1, flip back at step 7) makes net endpoint difference look like zero while the chain extended the effective horizon arbitrarily. Composition witnesses must be over the gross ledger; net is laundering-blind |
| *"A composite witness is a ledger you've proved closed."* | `surface-deformation-requires-coupling-candidate-2026-06-05.md` § Composition Frontier | The unifying observation: spend ledger and composite witness are not two paths but two compression levels of the same custody chain. Spend ledger = custody receipt; composite witness = claim receipt asserted over it |
| *"A lawful crossing must say what it does not change."* | `../bridge-obligation-lattice.md` § The doctrine line; external-pitch headers | The general unifier across the corpus's boundary-crossing families (Lift / Join / Convert / Delegate / Escalate / Project / Deform / Revoke / Except). The obligation set IS the list of what the crossing doesn't change. Surfaced 2026-06-06 in the bridge-taxonomy refinement round |
| *"A fog machine is a bridge with the empty obligation set."* | `../bridge-obligation-lattice.md` § The doctrine line | The brutal negative-compression form. A "crossing" that names no preservation obligations is not a bridge — it's atmospheric. Same disease as the v1 SurfaceDeformation `requiresAdditionalWitness` Boolean (vibes with a badge), generalized to the taxonomy level |
| *"The taxonomy must be admissible under its own NoSilentConversion."* | `../bridge-obligation-lattice.md` § The recursive scar; methodology docs | The recursion: classification claims are themselves claims. *"X is a specialization of Y"* must produce a ConversionWitness or get refused. ChatGPT's 2026-06-06 "four plus satellites" cut failed this gate on three of five reductions — the test catches its own architect. Self-applying refusal kernels prevents the taxonomy from becoming a fog machine |
| *"A specialization is admissible only if it inherits the parent's obligations without needing a new preservation invariant."* | `../bridge-obligation-lattice.md` § The NoSilentConversion gate | The honest test for child-of-parent reductions. If the child needs an extra preservation clause, it is a sibling wearing the parent's coat — not a child. Operationalizes the recursive-scar rule above |
| *"Together, the kernels suggest a calculus of admissible boundary crossings."* | `../bridge-obligation-lattice.md` § Static vs Dynamic; methodology / project intros | The sober doctrine sentence. *Suggest*, not *constitute* — the calculus is latent in what the kernels instantiate; it is not the project name. Safe-form version of the keeper below |
| *"Admissibility Kernels is the artifact name; calculus is the deeper pattern you keep rediscovering despite your best efforts, like mold in a Pittsburgh basement."* | methodology / `bridge-obligation-lattice.md` § Calculus stays in the basement | The discipline rule from the 2026-06-06 rename-still-holds round. *Kernels* = small refusal artifacts, bounded, buildable, citable; *calculus* = latent grammar (bridge witnesses, obligation sets, preservation invariants). Calculus as front-facing noun overpromises; kernels as artifact name keeps the universal-machine swagger in the footnotes |
| *"You tried to avoid building a theory of institutional spacetime and accidentally found the curvature tensor."* | `bridge-obligation-lattice.md` § Provenance; methodology footnotes | The goblin keeper for the SurfaceDeformation backreaction round. Same content as the sober line above, in the voice the user actually thinks in. Compresses the *we ran the audit, the audit caught itself, the catch is the point* arc. Don't quote in external pitch without translating |
| *"Cedar guards the door. This asks whether the door is where everyone says it is, whether the badge still counts, whether the emergency exit became the main entrance, and whether the map was rewritten by the person trying to get in."* | `../admissibility-as-pre-authorization-layer.md` § Cedar-relative positioning; external-pitch headers | The single strongest external-pitch keeper of the 2026-06-06 round. Locates the corpus precisely against Cedar / Verified Permissions without overclaiming it as a Cedar replacement. The four clauses map to the four most load-bearing dynamic refusal families: deformation (door location), revocation/freshness (badge), exception ≠ precedent (emergency exit), and projection / map-vs-territory |
| *"Cedar trusts the application to supply the witness facts. The hard problem moves outside Cedar."* | `../admissibility-as-pre-authorization-layer.md` § Cedar-relative positioning | The sharper one-line statement of the upstream/downstream relationship. Cedar's `permit` / `forbid` over principal/action/resource is honest authorization logic; the witness facts that get fed into Cedar are the corpus's territory. The corpus is not "better Cedar" — it's the missing notarization/governance/control layer under systems that use Cedar-like authorization |
| *"The more the Lean kernels line up with NQ gaps, the more dangerous they become to NQ's filing discipline."* | NQ filing-discipline docs / methodology / `bridge-obligation-lattice.md` § Artifact-discharge discipline | The danger rule. Similarity between Lean-refused conversions and NQ-named gaps creates temptation: *"this theorem proves the gap shape, therefore NQ can mark the gap handled"* — wrong. Different artifacts discharge different obligations. Surfaced 2026-06-06 in AG Claude's review of the bridge-obligation-lattice batch; preserved per ChatGPT's pocketing call |
| *"The doctrine caught its own architect."* | `bridge-obligation-lattice.md` § The NoSilentConversion gate; methodology footnotes | Sharper compression of the recursive scar — three of ChatGPT's five "four plus satellites" reductions failed NoSilentConversion against the cut itself. The corpus becoming self-hosting in the least embarrassing way: the discipline didn't merely classify external bullshit, it caught a corpus-internal taxonomy move trying to silently collapse distinct obligation sets. Surfaced 2026-06-06 in AG Claude's review |

## Placement rule

A keeper lands when:

1. The documentation pass that owns the canonical home runs, *and*
2. The keeper compresses better than what's currently there, *and*
3. The underlying claim is verified still in place.

If the underlying claim has moved or the kernel state has changed since the keeper was filed here, the keeper gets re-verified before placement.

## Anti-patterns this file refuses

- **Stockpiling keepers as if they were doctrine.** A keeper is a cosmetic upgrade on existing doctrine, not a substitute for it. If you find yourself wanting to *cite* a keeper from this file in active work, the keeper has not yet earned that citation — go cite the underlying claim instead.
- **Reading this file as a TODO list with priority.** It has no priority. Documentation-legibility passes are opportunistic; they happen when a docs surface is already being touched. Touch this file when that's happening; otherwise ignore it.
- **Promoting a keeper to a parked-lead because it sounds important.** If the keeper has no underlying claim, it's not a keeper — it's a candidate handle that should be evaluated against the [gate stack](../../../.claude/projects/-home-jbeck-git-papers/memory/feedback-gate-stack.md), not stockpiled here.

## Multi-clause doctrine blocks (added 2026-06-06)

Block-form keepers that don't compress to one line without losing structure. Preserve verbatim when quoted.

### The artifact-discharge discipline (per ChatGPT 2026-06-06)

> **Different artifacts discharge different obligations.**
>
> - **Lean kernels** may identify/refuse a formal conversion.
> - **NQ gaps** are discharged only by receipt, verdict, export, or runtime behavior.
> - **Related-work maps** record route signs and neighbors.
> - **External convergence** supplies pressure, not implementation authority.

**Underlying claim already in place at:** [[project-lean-custody-state]] (custody policy), [[project-witness-carrier-model]] (model ≠ schema ≠ Lean), the related-work map's *"route signs not territory"* status caveat, and the Cedar-relative positioning note (external convergence as forcing-case pressure rather than implementation authority). This block compresses that cross-cutting discipline into a single quotable unit.

**Operational firewall sentence (sharper compression of the above):**

> *Lean proves impossibility. NQ exports witnessed operational verdicts. The map records route signs. A consumer trigger spends implementation calories.*

**Companion danger rule** (filed above as single-line keeper): *"The more the Lean kernels line up with NQ gaps, the more dangerous they become to NQ's filing discipline."* Similarity creates temptation; the discipline above is what prevents the temptation from becoming a filing error.

## Cross-references

- `working/parked-leads.md` — deferred-build register (different artifact type)
- [[feedback-gate-stack]] — handle → predicate → fixture → kernel discipline
- `working/primitives/AUDIT.md` — per-primitive overclaim/non-case audit
