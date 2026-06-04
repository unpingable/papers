# Multiplicity/resource register — seed note

**Status:** bounded register seed, 2026-06-03. NOT an open register. NOT
active work. NOT a theorem. NOT a build plan.
**Discipline:** file-now-work-never per
[`maximal-calculus-forcing-cases.md`](maximal-calculus-forcing-cases.md).
A specimen candidate is named here; the register is not opened until the
promotion gate's second concrete example surfaces.

## Keeper line

> **A shared safety budget is not a reusable premise.**

## 1. Specimen name candidates

- `BlastRadiusBudgetDoubleSpend` (preferred — ops-legible)
- `DeploymentBudgetContraction` (Lean-shaped sibling phrasing)

Both refer to the same candidate. Pick one when promoted; until then,
either is acceptable.

## 2. Failure shape

A deployment system enforces a shared safety budget:

- no more than N hosts may mutate at once;
- no more than N racks / cells / POPs may be in rollout;
- no more than N concurrent risky operations may consume the same
  maintenance window or blast-radius budget.

Multiple admissible actors or jobs observe the same valid remaining
budget. Each treats that observation as reusable authority. Independent
schedulers, parallel rollout waves, or concurrent jobs each consume the
*same* premise as if exclusively held.

Concrete instances of the same shape (deployment-at-scale, not
generalized further):
- canary cohort budget reused by parallel rollout jobs
- maintenance window capacity double-booked
- rack / POP / cell blast-radius cap exceeded by independent schedulers
- error-budget "available" snapshot consumed by multiple releases
- database migration lock treated as advisory evidence instead of
  exclusive lease
- rate-limit / API quota checked before fanout but not consumed atomically

## 3. Why this is multiplicity/resource, not source/temporal

The premise is:

- **valid** — the budget reading is correct;
- **fresh** — the reading is current at the moment of each check;
- **correctly sourced** — no actor is self-authorizing, no laundering,
  no retroactivity;
- **standing-clean** — every actor has legitimate authority to invoke
  the operation.

What fails is none of the source/temporal failure modes. The failure is
that the same valid premise is **duplicated into more operational
authority than it carries.**

The forcing discriminator (operator-issued):

> If the fix is "better provenance / freshness / revocation," it is
> source/temporal.
>
> If the fix is "reservation, lease, token consumption, accounting,
> uniqueness of use," it is multiplicity/resource.

This candidate fixes with reservation / lease / token consumption —
never with provenance or revocation. Clean multiplicity/resource.

## 4. Allowed shape

```
budget / reservation / token / lease is consumed once
total mutation remains within capacity
each admissible actor obtains its own consumption record before acting
the consumption is atomic with the check
```

## 5. Blocked shape

```
the same observed budget authorizes multiple independent mutations
total consumption exceeds the premise's capacity
multiple actors share a single check-result as independent authority
observation is treated as a lease when it was only a snapshot
```

## 6. Fix family

- **reservation** — claim N units up front against a counter
- **lease** — bounded-time exclusive hold on a portion of the budget
- **token consumption** — issue token at check, retire at use
- **accounting** — track outstanding commitments alongside availability
- **uniqueness of use** — each premise produces at most one consumption
- **atomic claim/check/use boundary** — check-and-consume is one
  operation, not two

The family is operationally diverse but structurally one: a single
admissible premise yields a single use-right.

## 7. Relation to ContractionHinge

Same species. Different substrate, different application altitude.

| Aspect          | ContractionHinge                       | BlastRadiusBudgetDoubleSpend            |
|-----------------|----------------------------------------|------------------------------------------|
| Altitude        | substructural sequent calculus         | deployment-at-scale ops                   |
| Substrate       | weight measure `v`, soundness `T2`     | budget counter, atomic consumption       |
| Allowed unit    | `[A] ⊢ A` (one occurrence licenses one) | budget N permits N-bounded mutation       |
| Blocked unit    | `¬ [A] ⊢ A ⊗ A` (one cannot license two) | one budget reading cannot license two consumptions |
| Quarantine      | `contr` lives only in `DerivableC`     | "shared observation as advisory" is an explicit override, not default |
| Refusal proof   | counting argument (`v A + v A ≤ v A` → ⊥) | atomic-reservation invariant (sum-of-claims ≤ capacity) |

Same species. The structural shape transfers; the substrate does not.
Lean specimen mirroring would need its own apparatus (atomic
reservation counters, capacity invariant) distinct from ContractionHinge's
sequent calculus.

## 8. Non-goals

- No Lean specimen yet. ContractionHinge.lean is the species's kernel
  reference; a deployment-side Lean specimen waits for promotion.
- No NQ implementation yet. The seed names the pattern; it does not
  authorize building reservation/lease primitives in the operator's
  systems.
- No new taxonomy. This is the second species, already named. Adding a
  third would require a specimen that refuses classification under both
  source/temporal and multiplicity/resource.
- No source/temporal rewrite. The amendment-cut register stays
  source/temporal-specific (per the substrate lint). Do not import
  Int / counts / ≤ / budgets into amendment-cut work.

## 9. Promotion gate

Open the register only when **all three** hit:

1. A second concrete operational example surfaces — a real incident,
   failing test, or implementation consumer the operator can name (not
   a theoretical case).
2. The example passes the forcing discriminator (fix is
   reservation/lease/consumption, not provenance/revocation).
3. The example refuses reduction to source/temporal discipline under
   the substrate lint.

When all three hit: this note becomes the seed for the register, the
chosen specimen name becomes specimen zero's first entry, and a
ContractionHinge-style Lean specimen at the deployment altitude becomes
candidate work.

Until then: the seed sits. Pre-built registers grow features they don't
need; forcing-driven registers grow features they earned.

## Cross-references

- Taxonomy classification (the source/temporal-side classifier pass
  the second species mirrors):
  [`maximal-calculus-taxonomy-classification.md`](maximal-calculus-taxonomy-classification.md)
- Synthesis closure (the two-species split that made room for this
  register):
  [`source-basis-discipline-synthesis.md`](source-basis-discipline-synthesis.md)
- First species's kernel reference:
  `~/git/lean/LeanProofs/Admissibility/ContractionHinge.lean`
- Alloy substrate-shape diagnostic for this species:
  [`contraction-hinge-probe-result.md`](contraction-hinge-probe-result.md)
- Sibling forcing-case register (source/temporal side):
  [`maximal-calculus-forcing-cases.md`](maximal-calculus-forcing-cases.md)
- Arc index:
  [`maximal-calculus-refused-map.md`](maximal-calculus-refused-map.md) §
  "Arc closure 2026-06-03"
- Case-work classifications (the source/temporal side under closed
  taxonomy):
  [`amendment-cut-case-classification.md`](amendment-cut-case-classification.md)
- Standing-upgrade Alloy probe (sibling Alloy artifact in the arc):
  [`alloy-spike-standing-upgrade-result.md`](alloy-spike-standing-upgrade-result.md)
