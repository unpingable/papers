# Anti-Laundering Doctrine Map

**Filed:** 2026-06-04. **Status:** family map. Names what's covered, what's candidate, what's adjacent. Prevents candidate-explosion from looking like orphaned doctrine acne.

## The family

Each row names one *bad inference* the corpus exists to refuse. The right-hand column points at the Lean modules or candidates that own the refusal at the formal layer; the left-hand column names the family so a new instance can be classified before being filed.

| Family                       | Bad inference refused                                            | Where it lives                                                                                       |
| ---------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Surface boundary**         | revoked / spendable / valid on A ⇒ same on B                     | `SurfaceAuthorization.lean` (collapsed-surface refusal); standing-upgrade-block specimen             |
| **Declaration completeness** | partial coverage ⇒ total coverage; survival ⇒ closure            | `ClosureEligibility.lean`; `RecoveryMargin.lean`                                                     |
| **Witness identity / provenance** | sample exists ⇒ trustworthy / provenanced witness           | `WitnessInvariance.lean` (encapsulation / regime axis); provenance is a candidate gap                |
| **Custodian binding**        | observed / instrumented ⇒ accountable                            | candidate, [`custodian-binding-accountability-candidate.md`](custodian-binding-accountability-candidate.md) |
| **Freshness / expiry**       | was true ⇒ still admissible                                      | `Freshness.lean` (metric-time axis)                                                                  |
| **Fluency / settlement**     | output reads coherent ⇒ settled                                  | `ConsolidationDenial.lean`                                                                           |
| **Cross-boundary mint**      | failure / exposure / degradation on A ⇒ same on B                | `CrossBoundary{Exposure,Degradation,FailureMint,Cascade}.lean`                                       |
| **Authorization vs safety**  | authorized ⇒ value-preserving                                    | safety-bridge family (`SafetyBridge.lean`, `SafetyTrajectory.lean`, `AttestationLedger.lean`)        |
| **Composition / unification**| local refusal composes ⇒ unified judgment form                   | doctrine: [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md); not a Lean theorem |

## How to use this map

Before filing a new candidate working note that names a refusal:

1. **Classify it against the family table.** If the bad inference matches an existing row, the candidate is either (a) a new specimen of an existing family (annex / specimen work), or (b) a sharper restatement of an existing refusal (rewrite the existing module's docstring, not a new file).
2. **If the inference doesn't match any row**, the candidate is opening a new family. That is a heavier move — name it, but do not build Lean until a downstream consumer requires the distinction mechanically (per the doctrine file's bridge-tax discipline).
3. **If the inference matches a row but the existing modules don't cover the specific operational failure mode the candidate names**, the candidate is a *forcing case* on an existing family. File it; the existing module may need to be extended, or a sibling kernel may need to be added.

## Meta-pattern: control-flow laundering

Some anti-laundering refusals can be reintroduced by the checker's *control flow* rather than by its *domain model*. This is an implementation-level preservation rule that applies to ALL refusal families above; it is not a separate row.

**The pattern.** Monadic short-circuiting (`Except.bind`, `do`-notation, first-failure-wins validators, early-return gate chains) collapses a multi-failure attempt into a single refusal. The domain model can be perfectly typed and the kernels can each return typed failures, and the *checker's evaluation strategy* still launders `[failure₁, failure₂, failure₃]` into `[failure₁]`. A complete diagnosis is converted into the first encountered failure, and independent refusal grounds are silently erased.

**The rule.** Boundary checkers that claim to preserve refusal structure must use validation/applicative-shaped accumulation: run all relevant kernels, preserve each typed failure, avoid netting failures into a scalar verdict. The idiomatic clean code (early return, monadic bind) is wrong here. The awkward accumulating form is correct, and the awkwardness is load-bearing.

**Where this came from.** Discovered structurally in `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` (a fenced scratch encoding of the boundary-checker pattern). The Lean type system rejected the obvious idiomatic shape — `Except`-based aggregation forced a confession that monadic structure would have eaten the multi-failure diagnosis. The 8-way exhaustive match in that file is intentionally ugly because the ugliness is what prevents the laundering. Any future kernel-abstraction layer must be validation/applicative-shaped, never plain `Monad`.

**Operational translations (non-Lean code).** The Lean scratch is *category 2* (fenced proof-of-encodability), but the four implementation idioms it rejected translate directly into design rules for NQ / AG / Rust / Python code without needing to ship any Lean:

1. **No caller-supplied admissibility.** Witnesses are output, never input. APIs that accept a "verified" or "trusted" flag from the caller are reintroducing self-mint.
2. **No early-return validators where all failures matter.** Short-circuiting aggregators (`Result::?`, `Either.bind`, `try` chains, gate-cascade returns) launder multi-failure cases into single-failure refusals. Where complete diagnosis is the point, use accumulating / validation-shaped aggregation.
3. **No boolean "valid" APIs for authority transitions.** Boolean returns convert "passed" into an uninspectable scalar. Authority-bearing checks should return typed verdicts carrying either the admissibility evidence or the typed refusal, not `bool`.
4. **No reusable witness unless explicitly versioned / scoped.** A witness should be tied to the specific attempt, time, and (if relevant) policy version it was minted under. "Trusted token" / "session" abstractions that elide the binding are replay laundering with better PR.

These translations are the bridge from "proof-shaped toy discovered something in Lean" to "non-Lean code that doesn't lie." Citable outside the formal context.

**Why this isn't a sixth row.** It is not a domain refusal (it doesn't refuse a class of bad inferences across surfaces). It is a preservation rule for the implementation of any domain refusal. Filing it as a row would dilute the family taxonomy; filing it here keeps the row structure clean and surfaces the meta-rule where checkers will actually consult it.

## Lean filing discipline (two admissible categories)

The earlier rule "no Lean without a downstream consumer" was too narrow. Two categories of Lean filings are admissible in the corpus, and conflating them is the failure mode to watch for:

1. **Public / promoted kernels** — wired into `LeanProofs.lean`, part of the 1.0 compatibility surface (or earned annex). Requires a downstream consumer that mechanically needs the distinction. Bridge-tax discipline per [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md) applies.
2. **Fenced scratch proof-of-encodability** — scratch annex labeled as such, NOT wired, NO promotion path, NOT used as discharge. Allowed when it demonstrates that a doctrine *can* be structurally encoded. Pays its rent by forcing the architecture to confess which implementation idioms are inadmissible (see meta-pattern above). The productive use of formal methods is not "prove the system correct" but "use the proof-shaped toy to discover which implementation idioms are inadmissible." Lean's role in category 2 is the compiler as adversarial reviewer, not as ratification authority.

The failure mode the original rule was guarding against — Lean masquerading as discharge — fires only when category-2 work is presented or used as category 1. Fenced scratch that stays fenced is genuinely productive. `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` is a category-2 filing: it structurally encodes three of the family rows above (custodian binding's self-attestation half, freshness, declaration completeness's zero-evidence degenerate case), explicitly names the standing-kernel gap, and surfaced the control-flow laundering meta-pattern as a side effect of refusing to be elegant.

## What this map is NOT

- Not a formal taxonomy. Rows are operational categories, not type-theoretic partitions.
- Not exhaustive. New families can be added; old families can be retired if their refusal turns out to be a special case of another row.
- Not a paper. This is internal navigation for the working-notes layer; if a paper ever needs to cite the family structure, it cites the individual kernel modules, not this map.
- Not a license to build. Files referenced here are the substrate; building a new kernel in any row still requires the per-row forcing-case discipline.

## Composes with

- The doctrine file [`no-unifier-without-laundering.md`](no-unifier-without-laundering.md) names the meta-rule: cross-family implications require an explicit bridge theorem stating which row's refusal condition is being preserved. This map names the rows; the doctrine file governs how they cross.
- The Lean repo's `LeanProofs/Admissibility/README.md` "Refusal kernel taxonomy" section is the formal-layer sibling of this map.

## Provenance

Filed 2026-06-04 after a candidate (`custodian-binding-accountability-candidate.md`) needed a parent to prevent it from looking orphaned. The retroactive realization that the corpus has been building a small family of refusal-kernel patterns prompted the map; the patterns predate this filing.
