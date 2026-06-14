# Wiring is a promotion claim. Folder placement is not.

**Filed:** 2026-06-06 (Fri PM/eve). **Status:** repo-organization discipline. Custody discipline applied to the corpus's own repo, not to external claims. **Memory pointer:** `project-wiring-vs-folder-placement`.

This file exists to keep the *if/when* of reorg / public-wiring decisions answerable without re-derivation, and to preempt the failure mode where momentum impersonates maturity. The corpus has spent today catching its own category errors; reorganizing under that cover would launder custody by path.

## The headline

> **Wiring is a promotion claim. Folder placement is not.**

A file under `Admissibility/` can still be fenced scratch (Option C policy already allows this; the 13 fenced-Admissibility annexes are the precedent). What matters is *what the import surface says it stands behind.*

## The three concepts (currently visually tangled)

```text
1. Physical location  — where the file sits on disk
2. Build coverage     — what `lake build` exercises
3. Custody / public claim status — what the corpus stands behind
```

These are independent dimensions. Visual proximity (same folder) does not equal build coverage; build coverage does not equal public claim status. Conflating them is how you accidentally promote.

## Current state (2026-06-06 PM)

Not yet wired into the public surface (`LeanProofs.lean`):

- `Admissibility/Mandamus.lean` — fenced annex; same convention as `AmendmentFragment`, `ContractionHinge`, etc.
- `Scratch/BoundaryTransit.lean`
- `Scratch/AggregateWitnessRequiresJoin.lean`
- `Scratch/LogOnlyProvesEmission.lean`
- `Scratch/SurfaceDeformationRequiresCoupling.lean`

**Mandamus is the tempting one. Resist.** *Alive enough to bite, not ratified enough to speak for the house.*

## The scratch aggregator pattern (doable next, not tonight)

Per the discussion that produced this doctrine: build a scratch aggregator that separates *build coverage* from *public claim*. Concretely:

```text
LeanProofs/Scratch.lean         -- imports the 4 Scratch/* files
LeanProofs/AdmissibilityScratch.lean  -- imports the fenced Admissibility/* annexes
                                       -- (including Mandamus while it remains fenced)
```

Effect: `lake build LeanProofs.Scratch` and `lake build LeanProofs.AdmissibilityScratch` become valid build targets, *without pretending scratch is public doctrine.* The aggregators are import-only files; their existence is build-coverage hygiene, not promotion.

**Not tonight.** Per the sleep-cycle discipline below.

## The promotion gate (8 criteria for fenced → wired)

A file may move from fenced scratch to wired/promoted only when:

1. Green direct build.
2. Header declaring custody class (Option C compliance).
3. Doctrine note / paper anchor exists.
4. No known deferred obligation hidden as implemented.
5. **At least one consumer or public-facing reason to exist.** *(The big one. No consumer, no promotion. Otherwise the repo becomes a museum of elegant little knives.)*
6. No theorem names overclaiming their actual strength.
7. INDEX / custody ledger updated.
8. Clear import target chosen before wiring.

## The vocabulary-foundation subgate (a third act, not a third ladder)

**Added 2026-06-14**, following the observer scratch packet, which surfaced a gap: the 8-criterion gate governs *wiring an existing theorem/file*. It does not govern *minting shared vocabulary* — nouns (`Consumer`, `Force`, `Stamp`, `Root`, `Claim`, `Receipt`, `Authority`, …) that become substrate other modules are built on top of.

These are different ceremonies:

> **Wiring** says: *this theorem/file is mature enough to enter a public aggregation surface.*
> **Vocabulary-foundation promotion** says: *this naming scheme is now allowed to become substrate for future theorems.*

The second is more dangerous. Bad theorem names are annoying. Bad foundational nouns are a small indoor plumbing problem that eventually floods the house. **The nouns are where the bodies are buried.**

This is **not a third epistemic status / not a third ladder.** It is an *additional gate applied before Ladder A wiring* whenever the act would introduce shared primitives consumed by other modules. (Keeping it a subgate rather than a ladder is what stops the taxonomy from reproducing in captivity.)

### The subgate (8 questions, answered in the promotion record before minting)

Before minting shared cross-module vocabulary, the promotion record must answer:

1. **What downstream consumer needs the vocabulary now?** (Same load-bearing rule as wiring #5, at noun altitude. No consumer, no nouns.)
2. **What existing scratch/application files prove the abstraction is recurring**, not decorative? (Recurrence is evidence; a single elegant use is not.)
3. **What are the excluded meanings of each term?** (E.g. is `Consumer` an operator / verifier / catcher / jurisdiction / runtime / tenant / root / policy domain? Name what it is *not*.)
4. **What is the minimal nucleus being promoted?** (Smallest set of nouns + the one center theorem; everything else stays application.)
5. **Which application lemmas stay OUT of the foundation?** (Bridge-prices, positive exceptions, adapters — cited consumers of the nucleus, not members of it.)
6. **What claim-register or paper-facing claim, if any, depends on it?** (Ladder B linkage, if any.)
7. **What import target owns the vocabulary?** (One module owns the nouns; others import.)
8. **What compatibility / deprecation path exists** if the vocabulary is later split or renamed? (How does the house drain if a noun turns out wrong?)

### Not a promotion criterion

> **Agreement by ChatGPT / Claude / agent_governor is not a promotion criterion.**

The subgate requires an **artifact-level custody witness and a named consumer**, same standard as `promotion-claims-require-custody-witnesses.md`. Consensus among assistants is a dopamine receipt, not a custody witness. *Green theorem ⇏ blessed nouns.*

### Motivating example (cited, NOT promoted)

The observer scratch packet is the example that surfaced this subgate. Against it the subgate is unmet (no live forcing consumer for the shared vocabulary; no import target). Recorded only to anchor the gate, not to promote:

- **Candidate nucleus:** `Consumer`, `Artifact`, `Force`, `ConsumersAgree`, `HasGlobalSection` (+ center theorem `has_global_section_iff_consumers_agree`).
- **Excluded from nucleus:** `AbsoluteForceStamp` (bridge-price application), `UniversalRoot` (positive exception / single-root governance), clock mechanics (`ConsumerRelativeFreshness` adapter), receipt-specific semantics.
- **Current status:** pinned warrant-tier scratch, **not ratified** (see `docs/formalization-index.md` observer pin + `observer-foundation-promotion-preflight.md`).

## Practical rule (the dog leash)

```text
When the dog wants to reorganize:
  1. write the proposed promotion criteria
  2. write the deferral receipt
  3. build the scratch aggregator
  4. wait one sleep cycle
  5. only then touch public wiring
```

This is not bureaucracy. It is self-defense against the operator's own future enthusiasm, *which is apparently a highly capable adversary and is also the build engine.*

## The Table-Flip Override (sleep-cycle exception)

The sleep-cycle waiting period may be bypassed **only if** the new observation invalidates the current custody classification or proves the current layout is actively misleading.

**Invalid table-flippers (these are dopamine receipts; adorable, inadmissible):**

- *"This is promising."*
- *"This finally clicks."*
- *"Claude / ChatGPT / DeepSeek / AG all agree."*

**Valid table-flippers (the seven):**

1. A scratch file is already being imported transitively and you didn't realize it.
2. A public aggregator implies reliance on a fenced file.
3. A theorem name / header overclaims custody status.
4. A path location is causing agents / readers to treat scratch as promoted.
5. A build target no longer corresponds to the custody ledger.
6. A consumer now exists and current wiring blocks the actual bounded test.
7. A contradiction appears between INDEX, header, ledger, and import graph.

**Override action shape (not a license to reorg):**

```text
1. write the table-flip observation
2. patch only the violated boundary
3. update custody / header / ledger
4. stop
```

> *Emergency wiring fixes may bypass sleep. Architectural beautification may not.*

## Reorg shape (eventually, not now)

Possible future structure, *but only when import churn is worth the tax:*

```text
LeanProofs/Admissibility/
  Soundness/
  Liveness/
  Bridges/
  Scratch/
```

Or the bigger version:

```text
LeanProofs/
  Admissibility/
    Core/
    Soundness/
    Liveness/
    Bridges/
    Examples/
  Scratch/
  Deprecated/
```

**Reorg is a tax.** Pay it when the current layout is causing errors, not when the tree merely offends taste. Reorganizing 47 files to satisfy aesthetic cleanliness is how the SurfaceDeformation 2026-06-04 audit described what NOT to do (*"moving 13 files just to satisfy aesthetic cleanliness is how 'cleanup' becomes a land war in Asia"*). Same rule applies here, at higher altitude.

## Wire Mandamus publicly only when sprint #2 lands

Mandamus stays fenced until:

- `ReachableCure` with well-founded progress measure exists.
- Claimant-capability indexing is encoded.
- Blocking-predicate discipline is full (typed / versioned / witnessed / known-before-submission / clock-charged).
- Heterogeneous-appeal / appellate-independence theorem lands.

Until then it is **scratch-checked liveness spine**, not *"admissibility liveness module."*

## The doctrine pair

> **Scratch can be built. Public can be relied upon. Those are different predicates.**

> **Do not let momentum impersonate maturity.**

> **Enthusiasm gets a sandbox; promotion requires custody.**

> *Golden retriever can sprint around the yard. It does not get root.*

## What this is NOT (curdling guard)

- Not a refusal of reorg in principle. The corpus will outgrow its current layout. Reorg-when-it-causes-errors is fine; reorg-when-it-merely-offends-taste is the failure mode this file refuses.
- Not a refusal of public wiring in principle. Mandamus, BoundaryTransit, Aggregate, Log, SurfaceDeformation may all eventually be promoted. The promotion gate above names the eight conditions; the consumer requirement is the load-bearing one.
- Not a permanent moratorium on the scratch aggregator. The aggregator is the discussion's own logical next step; it sleeps until the next session, not forever.
- Not a permission slip. *"I followed the practical rule"* is necessary but not sufficient; the promotion gate is the actual condition for wiring.

## Cross-references

- [`tooltheory/lean-custody-ledger-2026-06-06.md`](tooltheory/lean-custody-ledger-2026-06-06.md) — the custody ledger this discipline guards.
- [`INDEX.md`](INDEX.md) — the working/ classification companion; same shape, different file.
- [`refusals-need-receipts.md`](refusals-need-receipts.md) — the discipline of typed deferral receipts; this file is itself a typed deferral receipt for the scratch aggregator + reorg + public-wiring decisions.
- [`frontier3-rule-change-deferral.md`](frontier3-rule-change-deferral.md) — companion deferral receipt at higher altitude (constitutional layer).
- [`observer-foundation-promotion-preflight.md`](observer-foundation-promotion-preflight.md) — the first worked instance of the vocabulary-foundation subgate (candidate nucleus + open taxonomy questions; unmet, parked).
- [`promotion-claims-require-custody-witnesses.md`](promotion-claims-require-custody-witnesses.md) — the custody-witness rule the subgate inherits ("agreement is not a witness").
- [[documentation-keepers]] — keeper phrases from this file.

## Provenance

Filed 2026-06-06 (Fri PM/eve) following the operator's *"if/when reorg/wire-up"* question after a long day of multiple compile probes, doctrine consolidations, and the Mandamus build-green moment that made the temptation acute. Multi-model exchange produced: the three-concept separation; the scratch aggregator pattern; the eight-criterion promotion gate; the dog-leash practical rule; the Table-Flip Override (sleep-cycle exception with seven valid bypass conditions and the *"emergency wiring fixes may bypass sleep; architectural beautification may not"* rule); the doctrine pair.

This file is itself dogfooded discipline. *I want to reorganize* triggered steps 1-3 of the practical rule (proposed criteria, deferral receipt, *would* build the scratch aggregator next) and explicit step 4 (wait one sleep cycle before public wiring). The scratch aggregator construction itself sleeps until tomorrow.

**Addendum 2026-06-14:** the *vocabulary-foundation subgate* was added after the observer scratch packet exposed that the 8-criterion gate covers wiring a file but not minting shared nouns. Multi-model exchange (operator / ChatGPT / Claude) produced the wiring-vs-vocabulary distinction, the eight subgate questions, and the "third act, not third ladder" framing. Doc-only: no Lean wired, no shared module created, observer not promoted — the subgate's first instance is itself unmet and parked.

## Definition of done

> *Future-me with a shovel can find the rule before reorganizing, and the rule's exceptions are typed clearly enough that the override cannot be invoked by enthusiasm alone.*
