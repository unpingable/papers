# Formal artifact and reproducibility standing

## Current standing

The theorem family was compiled and axiom-audited in the development
environment. This draft directory does **not** yet contain the minimal portable
Lean artifact, and the relevant development branch has not been converted into
a public release dependency for this paper.

Accordingly:

> The mathematics is Lean-verified in its development custody, but this draft is
> not yet independently replayable from the papers repository alone.

Because machine checking is part of the paper's contribution, a public release
should not describe the package as replayable—or freeze v1.0—until the minimum
extraction below has been shipped and tested from a fresh checkout.

## Principal declarations used by the paper

### Static profile and domain geometry

- `ProfileCompatible`
- `DistinctDomainMediator`
- `HasCommonCore`
- `UniformCompatibilityTransitive`
- `commonCore_iff_domainMediator`
- `uniformCompatibilityTransitive_iff_domainMediator`

### Native continuation specialization

- `CommonCompatible`
- `PartialFutureSufficient`
- `commonCompatible_trans_of_domainMediator`
- `greatestCommonCompatible_exists_of_domainMediator`
- `commonCompatible_isGreatest_of_domainMediator`
- `partialFutureSufficient_refines_canonical`

### Canonicality and full-future comparison

- `partialFutureSufficient_iff_kernel_compatible`
- `greatestCompatible_exists_iff_transitive`
- `futureSufficient_iff_kernel_refines`
- `futureEquivalent_implies_commonCompatible`
- `futureEquivalent_iff_commonCompatible_of_equalWordDomains`

### Fixtures

- `PrivatePetals.commonCore_strictly_weaker_than_equalDomains`
- `PrivatePetals.commonCompatible_strictly_coarser_than_futureEquivalent`
- `NestedFailure.weak_overlap_and_laminar_do_not_restore_transitivity`
- `fixedModel_domain_necessity_refuted`

## Verified scope

The authoritative development checks reported:

```text
domain-overlap transitivity: passed (40 declarations)
partial-domain compatibility: passed (31 declarations)
continuation-stable quotient: passed (23 declarations)
continuation-relative hazard: passed (16 declarations)
compositional admissibility: passed (57 declarations)
```

The principal mediator/common-core/transitivity/uniform-sharpness theorems were
reported axiom-free. The broader inherited and fixture footprint used only the
documented assumptions:

```text
Classical.choice
Quot.sound
propext
```

The source gate found no `sorry`, `sorryAx`, `admit`, or local axiom
declarations.

## Toolchain recorded by the development campaign

```text
Lean: 4.29.0
Lean toolchain revision: 98dc76e3c0a9b856c9b98726b713fb04fab16740
Mathlib revision: 6ef8cc2731780be866bf243afcb7732f4da5f406
Companion Lean repository revision: 2bb4ea1f97baadbc1477f58937a3fde84776f0f4
Development evidence revision: 45015037ac78650c29a74ca7a3558ad3b972d0e8
```

These identifiers are custody facts, not yet a portable reader-facing build
recipe.

## Minimum extraction target

The release artifact should contain only:

1. the deterministic finite-word model definitions needed by the paper;
2. common-domain and full-future equivalence definitions;
3. compatible-kernel and greatest-kernel results;
4. domain-mediator/common-root definitions and the uniform characterization;
5. the three explanatory fixture families;
6. one qualification module that prints the paper declarations and axioms;
7. one replay script with pinned revisions.

It should not import the empirical campaigns, governance records, or unrelated
formal theorem strands.

## Audit boundary

The latest narrow Kimi prior-art request timed out without a report. Earlier
formal gates were controller-audited but not independently certified. Neither
Lean compilation nor model review establishes external novelty, runtime
conformance, or applicability to a concrete monitoring system.
