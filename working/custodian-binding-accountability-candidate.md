# Custodian-Binding Accountability — candidate refusal kernel

**Filed:** 2026-06-04. **Status:** name-early candidate; **not authorized to build** as a Lean kernel until a downstream consumer requires the distinction mechanically.

**Family:** custodian binding (see [`anti-laundering-doctrine-map.md`](anti-laundering-doctrine-map.md)).

## The bad inference

```text
ObservationEdgeExists(S)        -- a metric / log / probe / dashboard / alert rule exists for S
--------------------------------
AccountableCoverage(S)          -- ❌ promoted without proof of a binding edge
```

The corpus already refuses several adjacent forms (visible-green ⇏ recovery-margin; survival ⇏ closure; fluency ⇏ settlement). This candidate names the version where the visible-side artifact is **instrumentation** and the substantive-side claim is **accountability**. Observation without a conversion edge that can bind some custodian is surveillance, not accountability — and the bad inference quietly promotes the former to the latter.

## The refusal rule

> A witness regime with observation edges but no conversion edge that can bind a custodian cannot be promoted to accountable coverage.

Equivalently: *observation edges and binding edges are independent. Existence of one is not evidence for existence of the other. Coverage claims must witness both.*

## Failure modes that motivate the candidate

These are operational shapes — descriptive, not exhaustive — where the bad inference fires in practice:

1. **Instrumentation without an answerable owner.** Metrics scrape, dashboards exist, alert rules may even fire, but there is no oncall / escalation / ticket-owning custodian. The chain ends at the visual; no edge binds.
2. **Self-reporting custody.** The party being observed owns the exporter, the labels, the retention, and the silence rules. The "receipt" is generated and curated by the subject. No external custodian holds the receipt against the subject.
3. **Owner-configurable amnesia.** Alert exists, but suppression / silencing / retention is controlled by the same team being observed, with no external receipt of suppression. The observation can be silently discharged.
4. **Coverage scope mismatch.** The observation edge covers a coarser unit than the claim. (This is technically already a witness-identity / provenance issue, but it routinely co-occurs with the custodian-binding failure and is worth naming as a co-failure mode.)
5. **Provenance-stripped sample.** The observation arrived, but lineage was dropped en route, so even a willing custodian cannot bind a specific source. (Adjacent to witness-identity family; not the load-bearing case for this candidate.)

Cases 1, 2, and 3 are the load-bearing failure modes for this candidate. 4 and 5 are co-failure modes that already live in adjacent rows of the doctrine map but tend to surface together with custodian-binding failures.

## What a kernel would look like (if forced)

Sibling to `RecoveryMargin` / `ClosureEligibility` / `ConsolidationDenial` in the Lean repo's annex — same "visible X ⇏ substantive Y" pattern, same one-shot existential-countermodel shape. Likely a module name like `CustodianBinding.lean` or `InstrumentationNotAccountability.lean`, with:

- A small relational model (observation edges, binding edges, a custodian predicate).
- A theorem of the form: `∃ S, ObservationEdge S ∧ ¬ ∃ c, BindsCustodian c S` (an instrumented regime with no binding edge exists, by construction).
- A scope fence naming what the kernel doesn't claim (it doesn't define what counts as a binding edge in any concrete substrate; that lives in the consumer).

The verdict surface would naturally include states like `instrumented-only`, `no-custodian-binding`, and `admissible-with-scope`, but the exact verdict types belong to the consumer that forces the kernel, not to this candidate. Specifying them now would prejudge the forcing case.

## Forcing case

A consumer that needs to mechanically distinguish "this system is observed" from "this system is accountably covered." Candidate forcing consumers include any preflight / admissibility check that ingests instrumentation evidence and emits coverage claims. The first concrete one wins; the kernel earns construction the moment a downstream classifier needs to refuse the promotion.

Per the doctrine of [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md): the kernel, if built, would be a bridge-law specimen at exactly the kind of cross-surface seam the doctrine names. Observation surfaces and accountability surfaces are distinct refusal surfaces; bridges between them must name which one they pay.

## What this candidate is NOT

- **Not authorization to build.** Name-early per the corpus's standing discipline; ratify-lazily, implement-only-when-forced.
- **Not a paper.** Doctrine-shape at most. Operational shape until something forces the formalization.
- **Not a new family.** Lives in the custodian-binding row of the [doctrine map](anti-laundering-doctrine-map.md). The row exists; this is its first named candidate.
- **Not specific to any one consumer.** The candidate is portable; it names the refusal generically. Concrete verdict surfaces and binding-edge predicates belong to the consumer that forces it.

## Cross-references

- Parent doctrine map: [`anti-laundering-doctrine-map.md`](anti-laundering-doctrine-map.md).
- Composition discipline: [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md) (cross-surface promotion requires a paid bridge tax; this candidate, if built, would be such a bridge).
- Sibling refusal kernels (annex, Lean): `~/git/lean/LeanProofs/Admissibility/RecoveryMargin.lean`, `ClosureEligibility.lean`, `ConsolidationDenial.lean` — same structural pattern, different refusal surfaces.
- Adjacent doctrine map rows: witness-identity / provenance (sample lineage), declaration-completeness (coverage scope), freshness (sample staleness). Custodian-binding failures co-occur with these but are not identical to them.
- **Related face, not discharged here:** `NoFreeStandingReadout` (`~/git/lean/LeanProofs/Scratch/NoFreeStandingReadout.lean`, scratch; doctrine note [`standing-as-readout-no-free-standing-readout.md`](standing-as-readout-no-free-standing-readout.md)) models `CanRead ⊬ MayReadout` only as a **structural absence** (no capability constructor) while building the *readout regress*. The capability/authority countermodel itself remains part of THIS candidate and is **not** re-proved there — so the overlap doesn't get rediscovered later as a new seam, and this candidate stays unbuilt/undischarged until its own forcing case arrives. (The regress — non-root readout cannot self-ground — is the genuinely new piece and is NOT contained in custodian-binding.)
