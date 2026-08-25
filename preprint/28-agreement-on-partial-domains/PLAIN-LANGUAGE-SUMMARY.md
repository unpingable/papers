# Plain-language summary

**Companion to:** *Agreement on Partial Domains: Canonical Abstraction and a
Δ-System Criterion* (Paper 28)

**Version/status:** v0.1 draft; not yet published

**Reading status:** This is an explanatory companion to the manuscript. It is
not the canonical artifact and introduces no new claims.

Suppose a system compares two states by asking whether they give the same
answers to every question both states are able to answer. That sounds like a
reasonable notion of “these states are equivalent enough.” It is not always an
equivalence.

Imagine three monitors. The first and third can both answer a disk-health
question, but the middle monitor cannot. The first and middle agree on every
question they share. The middle and third also agree on every question they
share. Yet the first and third disagree about disk health. Compatibility holds
across both adjacent comparisons and fails across the endpoints.

That failure matters whenever a system wants to replace states with canonical
classes. Equality of classes must be transitive; common-answer compatibility
need not be.

The paper develops two precise repairs.

1. **Preserve answerability.** Two states count as equivalent only when the same
   future questions are available and their answers agree. This stronger
   relation supports a canonical quotient.
2. **Constrain answerability geometry.** If answerability differences are
   intentionally ignored, require every two distinct answerability domains to
   share exactly one common core. Everything outside that core belongs to
   private, nonoverlapping petals. Mathematicians call this a Δ-system.

In the paper's static formal model, Δ-system geometry is exactly the domain-only
condition that makes common-answer compatibility transitive for every possible
decision labeling. It is weaker than requiring every state to answer the same
questions. But it is stronger than merely requiring domains to overlap, share a
global question, or be nested.

The theorem does not say every practical monitor should be redesigned as a
Δ-system. Often the better repair is to retain answerability as part of the
state. The result is a design boundary: if an architecture discards
answerability differences, it must not assume that pairwise common-answer
agreement will compose without an additional structural guarantee.

## Claim boundary

Compatibility of partial functions, nontransitive tolerance relations,
incompletely specified machines, and Δ-systems are established mathematics.
The contribution is the Lean-checked synthesis of these ideas into one narrow
canonical-abstraction result. The draft does not prove runtime safety,
bisimulation, minimum state count, or a general distributed-monitoring theory.

## Read the draft

- [Main manuscript](agreement_on_partial_domains.md)
- [Draft PDF](agreement_on_partial_domains.pdf)
- [Directory guide](README.md)
- [Formal artifact status](FORMAL-ARTIFACT.md)
