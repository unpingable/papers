---
header-includes:
  - \usepackage{booktabs}
  - \usepackage{amsmath}
  - \usepackage{amssymb}
---

# Agreement on Partial Domains: Canonical Abstraction and a Δ-System Criterion

**James Beck**

Independent Researcher

**Date:** 2026-08-25

**Series:** Δt Framework, Paper 28

**Status:** v0.1 draft; not yet published

---

## Abstract

Systems with partial observations often compare two states by requiring equal
answers only to queries available in both. This common-domain relation is
reflexive and symmetric but can fail transitivity, preventing a canonical
quotient and permitting incomparable maximal coarsenings. We formalize two
repairs in Lean. Treating query availability as part of future behavior yields
an equivalence relation and a canonical quotient characterized by
observation-kernel refinement. If availability is intentionally ignored, we
characterize the domain families that restore transitivity uniformly over
arbitrary proposition-valued decision profiles: precisely the Δ-systems, whose
distinct domains share one common root and otherwise have private petals. A
mediator-hole labeling proves sharpness; explicit fixtures show that equal
domains are unnecessary, nested domains and nonempty overlap are insufficient,
and fixed labelings may be transitive accidentally outside the Δ-system regime.
The contribution is a machine-checked synthesis and design boundary built from
classical ingredients, not a claim that partial-function compatibility or
Δ-systems are new.

## 1. Introduction

The paper number places this self-contained note in the broader
[Δt Framework corpus](https://github.com/unpingable/papers/blob/main/docs/corpus.md),
a series on formal boundaries of observation, admissibility, and composition.
No result from Papers 1--27 is assumed here.

Many systems compare objects that do not expose the same information. A monitor
may have access to some predicates but not others. A policy engine may evaluate
only the clauses enabled for one request. A partial specification may leave some
input/output behavior undefined. A record may carry only a subset of a schema.
In each setting, a natural comparison is:

> two objects are compatible when they agree everywhere both are defined.

This comparison is useful and well established. It is also not generally an
equivalence relation. The failure is small enough to miss in an interface and
large enough to invalidate canonical quotienting.

Suppose states $a$ and $c$ can both answer a query $w$, while state $b$ cannot.
If $a$ and $c$ disagree on $w$, the disagreement is invisible when either is
compared with $b$. It is therefore possible to have

$$
aCb,\qquad bCc,\qquad \neg aCc.
$$

Compatibility is reflexive and symmetric, but the mediator $b$ hides an
endpoint disagreement by lacking the query that exposes it. Grouping states by
$C$ is not therefore a quotient construction.

This paper gives a precise account of two repairs.

The first is semantic: availability is included in what must be preserved. Two
states are equivalent only when they admit the same finite continuations and
make the same governed decision after every admitted continuation. The resulting
future relation is an equivalence and supports a canonical quotient. An
observation is future-sufficient exactly when its kernel refines that quotient
kernel.

The second repair retains the weaker semantics—availability differences remain
ignored—but constrains the geometry of availability domains. The relevant
condition is that every pair of distinct domains share one common root. Outside
the root, each state may have a private petal disjoint from every other petal:

$$
A_s=K\cup P_s,\qquad P_s\cap P_t=\varnothing\quad(s\ne t).
$$

This is a Δ-system/common-root family. In the static profile abstraction
formalized here, it is exactly the domain-only condition under which
common-domain compatibility is transitive for every proposition-valued decision
assignment.

The universal quantifier is essential. A fixed assignment can accidentally make
compatibility transitive even when the domain geometry is bad; constant
decisions are the simplest example. The theorem characterizes a structural
guarantee supplied by domains alone, not a necessary condition for every
particular system.

The formal contribution has five parts:

1. a common-domain compatibility relation and finite nontransitivity witnesses;
2. a characterization of compatible observation kernels and the distinction
   between maximal and greatest compatible equivalences;
3. an availability-sensitive future equivalence with a canonical quotient;
4. an equivalence between domain mediation, common-root geometry, and uniform
   transitivity of static profiles;
5. fixtures proving strictness, sharpness, and the fixed-versus-uniform boundary.

The mathematics uses classical objects. Partial functions agreeing on their
common domains, tolerance relations, compatible states in incomplete machines,
partial words, and Δ-systems all have substantial prior literatures [1–8]. The
claim here is narrower: these ingredients form a useful, machine-checked
architecture theorem about when a partial-observation comparison may be treated
as canonical.

## 2. Partial profiles and common-domain compatibility

Let $S$ be a type of states and $W$ a type of finite continuations or queries.
For each state $s\in S$, let

$$
A_s\subseteq W
$$

be its admissibility domain. Let a decision profile be a proposition-valued
function

$$
d:S\times W\to \mathsf{Prop}.
$$

Only the values $d(s,w)$ with $w\in A_s$ are semantically exposed. Writing
$d_s(w)$ for $d(s,w)$, define common-domain compatibility by

$$
s\,C_d\,t
\iff
\forall w\in A_s\cap A_t,
\bigl(d_s(w)\leftrightarrow d_t(w)\bigr).
$$

In the Lean source, the static definition is `ProfileCompatible admitted
decision left right`, with `admitted : S → W → Prop` and
`decision : S → W → Prop`. The proposition-valued presentation avoids adding
decidability hypotheses to the structural theorem. Boolean partial functions
provide the immediate finite intuition. The native finite-word continuation
model later uses the corresponding relation `CommonCompatible`; the static
profile isolates the arbitrary-labeling question used in the uniform
characterization.

For every fixed $d$, $C_d$ is reflexive and symmetric. It need not be
transitive. This makes it a tolerance or compatibility relation in the broad
relation-theoretic sense [2,3], not automatically an equivalence relation.

### 2.1 Observation kernels

An observation $O:S\to Y$ induces the kernel

$$
\ker O=\{(s,t)\mid O(s)=O(t)\}.
$$

The kernel is always an equivalence relation. The observation is sufficient for
the weaker partial-future semantics exactly when

$$
O(s)=O(t)\Longrightarrow sC_dt,
$$

or equivalently

$$
\ker O\subseteq C_d.
$$

Thus admissible observation kernels are equivalence subrelations contained in a
relation that may not itself be an equivalence.

This distinction generates two order-theoretic notions that must not be
conflated.

- A **maximal** compatible equivalence has no strictly larger compatible
  equivalence above it.
- A **greatest** compatible equivalence contains every compatible equivalence.

Finite systems always have maximal compatible equivalences: the identity
relation is compatible, and a finite inclusion order has maximal elements.
They need not have a greatest one. The formal three-state fixture admits two
distinct incomparable maximal choices, one merging $a$ with $b$ and another
merging $b$ with $c$.

### 2.2 Greatest compatibility exactly at transitivity

For any reflexive symmetric relation $C$, the formal development proves:

$$
\boxed{
\text{a greatest equivalence }E\subseteq C\text{ exists}
\iff
C\text{ is transitive}
}
$$

The forward direction is worth spelling out. Every compatible pair $(s,t)\in C$
generates a two-point equivalence—identity plus the pair in both directions.
If a greatest compatible equivalence $E$ exists, it must contain each such
two-point kernel. Hence $C\subseteq E$. By compatibility, $E\subseteq C$, so
$E=C$. Since $E$ is an equivalence, $C$ is transitive. Conversely, if the
reflexive symmetric relation $C$ is transitive, then $C$ itself is an
equivalence and trivially the greatest compatible one.

This theorem does not say that an arbitrary tolerance has a canonical “best
approximation” by equivalences. It says the opposite: the greatest candidate
exists only when the tolerance was already transitive.

## 3. The mediator-hole obstruction

The smallest obstruction has three states and one load-bearing query. Let
$a,b,c$ be pairwise distinct and choose $w\in W$ such that

$$
w\in A_a\cap A_c,\qquad w\notin A_b.
$$

Call this a **mediator hole**: the endpoints share a query that the proposed
middle state cannot answer.

Choose a decision profile for which $a$ and $c$ disagree at $w$. All other
jointly admitted decisions may be set equal. Then:

- $aC_db$, because $b$ does not admit $w$ and no shared query exposes a
  disagreement;
- $bC_dc$ for the same reason;
- $\neg aC_dc$, because both endpoints admit $w$ and disagree there.

The formal necessity proof uses an especially economical adversarial profile:

$$
d(s,u)\iff (s=c\land u=w).
$$

At the missing coordinate, only the right endpoint receives the distinguished
truth value. The profile is not claimed to arise from every operational
transition system. It witnesses the exact quantifier in the static theorem:
failure of the domain condition defeats transitivity for *some* permitted
decision assignment.

The obstruction also explains why generic overlap slogans are too weak. It may
remain present when:

- every two domains intersect;
- all domains have a nonempty global intersection;
- the domains are nested or laminar.

The `NestedFailure` fixture realizes all three conditions while retaining an
endpoint-shared query absent from the middle domain. Nonempty overlap does not
ensure mediation.

## 4. Semantic repair: preserve availability

The first repair treats future availability as part of the semantics rather
than discarding it.

The native formal model supplies a deterministic execution of finite words. Let
`Adm(s,w)` mean that word $w$ is admissible from state $s$, let $s\cdot w$ be
the resulting state, and let $D$ be the governed hazard or decision predicate.
Define

$$
s\sim_F t
\iff
\forall w,
\begin{cases}
\operatorname{Adm}(s,w)\leftrightarrow\operatorname{Adm}(t,w),\\
\operatorname{Adm}(s,w)\Longrightarrow
\bigl(D(s\cdot w)\leftrightarrow D(t\cdot w)\bigr).
\end{cases}
$$

Because admissibility domains are required to agree, the problematic asymmetric
middle case is unavailable. The relation is reflexive, symmetric, and
transitive. It therefore defines a quotient map

$$
q:S\to S/{\sim_F}.
$$

The formal definition is operational: an observation $O:S\to Y$ is
future-sufficient when any two states it identifies are future-equivalent,

$$
\operatorname{FutureSufficient}(O)
\;:\!\!\iff\;
\forall s,t,\; O(s)=O(t)\Longrightarrow s\sim_F t.
$$

Because equality in the quotient represents $\sim_F$, this definition has the
following quotient-kernel characterization:

$$
\operatorname{FutureSufficient}(O)
\iff
\ker O\subseteq\ker q
$$

This kernel-refinement property is the precise sense in which the quotient is
the coarsest available abstraction for the declared future semantics. The
formal result does not require a total factor map from arbitrary values outside
the range of $O$, and it does not state a cardinality-minimality theorem.

The construction is analogous in spirit to Myhill–Nerode future equivalence
[9], but the paper does not identify its deterministic hazard model with
language recognition, automata minimization, trace equivalence, or bisimulation.

## 5. Structural repair: domain mediation

Suppose instead that the architecture intentionally ignores differences in
availability. The relation remains $C_d$, and canonicality must come from a
property of the domains.

Define **distinct-domain mediation** by

$$
\forall a,b,c\in S,
\quad
\bigl(a,b,c\text{ pairwise distinct}\bigr)
\Longrightarrow
A_a\cap A_c\subseteq A_b.
$$

Repeated-state cases are excluded because transitivity is already immediate
when $a=b$, $b=c$, or $a=c$. The condition says that every query shared by two
distinct endpoints is visible to any third state that could serve as a genuine
middle element.

Under this hypothesis, the transitivity proof is direct. Assume $aC_db$ and
$bC_dc$. Take $w\in A_a\cap A_c$. Domain mediation gives $w\in A_b$. The first
compatibility premise yields

$$
d_a(w)\leftrightarrow d_b(w),
$$

and the second yields

$$
d_b(w)\leftrightarrow d_c(w).
$$

Therefore $d_a(w)\leftrightarrow d_c(w)$, so $aC_dc$.

The proof assumes no finiteness, decidable equality, quotient construction, or
choice principle.

## 6. Domain mediation is Δ-system geometry

Distinct-domain mediation has a standard set-family form. Define a
**common-root family** by the existence of a predicate $K\subseteq W$ such that

$$
A_s\cap A_t=K
\qquad\text{for every }s\ne t.
$$

This is exactly a Δ-system. Writing $P_s=A_s\setminus K$ gives the familiar
decomposition

$$
A_s=K\cup P_s,\qquad
P_s\cap P_t=\varnothing\quad(s\ne t).
$$

No finiteness assumption is present. “Sunflower” is common informal
terminology, but “Δ-system/common-root family” avoids suggesting that the
continuation languages are finite.

The formal development proves:

$$
\boxed{
\operatorname{DistinctDomainMediator}(A)
\iff
\operatorname{HasCommonCore}(A)
}
$$

One direction is immediate: if $A_a\cap A_c=K$ for distinct endpoints, then
$K\subseteq A_b$ for every state $b$, so each endpoint-common query is admitted
by the middle.

For the other direction, choose the common core

$$
K=\bigcap_{s\in S}A_s.
$$

The universal core is contained in every pairwise intersection. Conversely,
if $w\in A_a\cap A_c$ for distinct $a,c$, domain mediation places $w$ in every
other state domain; the endpoint memberships already cover $a$ and $c$. Hence
$w\in K$. All distinct pairwise intersections therefore equal $K$.

The statement remains well formed for small or empty state types. Its
distinct-pair clauses become appropriately vacuous rather than forcing all
domains equal through the identity $A_s\cap A_s=A_s$.

## 7. Main characterization

Let `UniformCompatibilityTransitive A` mean that for every proposition-valued
decision profile $d$, the relation $C_d$ is transitive. The main theorem is:

$$
\boxed{
\begin{aligned}
&\operatorname{UniformCompatibilityTransitive}(A)\\
&\quad\iff \operatorname{DistinctDomainMediator}(A)\\
&\quad\iff \operatorname{HasCommonCore}(A).
\end{aligned}
}
$$

The forward implication is the hostile-labeling argument from Section 3: if a
mediator hole exists, one decision profile exposes it and violates
transitivity. The reverse implication is the transport-through-the-middle
argument from Section 5. The equivalence with a common root is Section 6.

This locates a sharp boundary for a particular question:

> Which domain families guarantee transitivity independently of the static
> decision values assigned on those domains?

It does not answer the different fixed-model question:

> For this one domain family and this one decision profile, is compatibility
> transitive?

The fixed-model question may have a positive answer outside the Δ-system class.
For example, if every exposed decision is false, every pair is compatible no
matter how the domains overlap. The universal relation is then the greatest
compatible equivalence. Bad geometry creates the capacity for hidden endpoint
disagreement; a particular labeling may fail to activate that capacity.

We call the two cases:

- **structural canonicality:** the domains force transitivity for every profile;
- **accidental or fixed-profile canonicality:** one profile happens to be
  transitive despite a mediator hole.

The theorem characterizes only the first.

## 8. Strictness and hostile fixtures

The formal fixtures delimit what the theorem does and does not require.

### 8.1 Private petals: equal domains are unnecessary

Take three states and four queries:

$$
W=\{k,p_a,p_b,p_c\}.
$$

Let

$$
A_a=\{k,p_a\},\quad
A_b=\{k,p_b\},\quad
A_c=\{k,p_c\}.
$$

All distinct intersections equal $K=\{k\}$, but the domains are not equal. The
uniform theorem supplies transitivity for every decision profile, and the
common-domain relation itself is the greatest compatible equivalence.

In the native word model, the `PrivatePetals` fixture uses the empty word as the
common root and private self-loop controls as petals. It proves both that the
new condition is strictly weaker than globally equal continuation domains and
that two states may be common-domain compatible while failing the stronger
future equivalence because their availability domains differ.

Thus canonicality of the weaker decision relation does not require preservation
of complete future availability information.

### 8.2 Nested failure: pleasant overlap is insufficient

Let

$$
A_a=A_c=\{u,v\},\qquad A_b=\{u\}.
$$

The domains are nested. Every pair overlaps. The global intersection
$\{u\}$ is nonempty. Yet $v\in A_a\cap A_c$ and $v\notin A_b$. Give $a$ and
$c$ different decisions at $v$ while preserving agreement at $u$. Then

$$
aC_db,\qquad bC_dc,\qquad \neg aC_dc.
$$

Laminarity, pairwise nonempty overlap, and nonempty global intersection do not
remove mediator holes.

### 8.3 Constant decisions: geometry is not fixed-model necessity

Keep the nested domains but assign the same proposition at every admitted
query. Compatibility becomes universal and transitive. This fixture prevents a
misreading of the main theorem: common-root geometry is necessary for the
uniform domain-only guarantee, not for every individual assignment.

## 9. Architecture interpretation

The formal result supports the following bounded design rule:

> If an architecture defines compatibility as agreement on everything both
> sides can answer, varying answerability domains can make compatibility
> nontransitive. A canonical abstraction requires either preserving
> answerability in the semantics or enforcing domain geometry that prevents
> mediator holes.

The two repairs preserve different information.

| Architecture choice | Preserves | Canonicality basis | Cost |
|---|---|---|---|
| Availability-sensitive future equivalence | domain availability and governed decisions | equivalence by construction | distinguishes states whose answers match but capabilities differ |
| Common-domain compatibility under Δ-system domains | governed decisions on shared queries only | structural transitivity | restricts which queries may be shared outside the common core |

Neither route dominates the other without application semantics. If the fact
that a query is unavailable matters, suppressing that difference is already the
wrong model. If availability is intentionally outside the decision semantics,
the Δ-system condition identifies one exact way to retain canonicality without
forcing every domain to be equal.

### 9.1 A minimal monitor example

Consider a fleet health API that reports proposition-valued predicates. Every
agent reports the core predicate `service_ready`; optional hardware plugins
report additional predicates.

Three agent states have domains:

```text
A: {service_ready, disk_fault}
B: {service_ready}
C: {service_ready, disk_fault}
```

All three report `service_ready = true`. Agent A reports
`disk_fault = false`; agent C reports `disk_fault = true`. If the grouping rule
is “agree on all predicates both expose,” then A is compatible with B and B
with C, while A is incompatible with C.

There are two honest repairs.

1. Include the exposed-predicate set in the observation, so B is not equivalent
   to A or C merely because it lacks the disputed predicate.
2. If the architecture insists on ignoring capability differences, prevent two
   agents from sharing an optional predicate unless that predicate belongs to
   the common core exposed by every agent. All non-core predicates must be
   private to one domain.

The second policy is exact for the static model and often operationally
restrictive. The example is therefore an illustration, not a recommendation
that real monitoring fleets should adopt private-petal schemas. Dynamic
capabilities, noisy values, multivalued outputs, authorization checks, and
temporal sampling are outside the theorem.

## 10. Related work

### 10.1 Partial functions and compatibility

Borlido and McLean study algebras represented by partial functions and use the
relation “agree on the intersection of their domains” as the canonical
compatibility relation [1]. Their representation theorem demonstrates that this
is an established and general object. The present result does not compete with
their algebraic theory; it asks a narrower structural question about uniform
transitivity when domains are frozen and values vary.

### 10.2 Tolerance relations

Tolerance theory studies reflexive symmetric relations under many historical
names, including compatibility and similarity [2,3]. Its maximal blocks are
maximal cliques and need not form a quotient partition. This supplies the
general relation-theoretic background for the common-domain relation. The
paper's greatest-compatible result is an elementary kernel-order fact, not a
new theory of tolerances.

### 10.3 Incompletely specified machines

Paull and Unger's classical work on incompletely specified sequential machines
replaces complete-machine equivalence classes with compatibility classes and
covers [4]. Modern model-based testing continues to confront compatible states
in partial specifications [5]. This is the closest operational precedent:
partial behavior complicates state merging because compatibility need not be
an equivalence. Machine compatibility may impose transition closure or
implementation constraints not present in the static profile theorem, so the
two results should not be identified.

### 10.4 Partial words

In partial-word combinatorics, wildcard positions yield a compatibility
relation that is expressly not an equivalence relation [6]. A defined symbol,
a hole, and a conflicting defined symbol realize the same local shape as the
mediator-hole example. The domain-family uniform characterization is not the
object studied in that literature.

### 10.5 Δ-systems and partial-function amalgamation

Δ-systems are classical set families with a common pairwise intersection root
[7]. In forcing, the Δ-system lemma is routinely applied to domains of finite
partial functions; after restricting to functions that agree on the root,
their unions are compatible. Sánchez Terraf formalizes the Δ-system lemma and
its countable-chain-condition application in Isabelle/ZF [8]. Those arguments
use common-root domains to extract pairwise-compatible subfamilies. The theorem
here instead characterizes when the pairwise compatibility relation is
transitive under every labeling. The ingredients are the same; the quantifier
and architecture interpretation differ.

### 10.6 Future quotients and agreement testing

The availability-sensitive quotient follows a Myhill–Nerode-shaped pattern:
states are identified by their behavior under all future words [9]. The formal
result is limited to its declared deterministic continuation and hazard
semantics.

Agreement testing asks when local functions that agree on overlaps are close
to one global function [10]. That is a richer approximate local-to-global
problem. This paper asks neither for approximate decoding nor for a global
amalgam; it asks when pairwise agreement itself is transitive.

No exact prior publication of the uniformly quantified Δ-system
characterization was located in the bounded review that produced this draft.
Because the proof is an immediate mediator-hole argument from standard
definitions, the paper makes no claim of new combinatorics on that basis.

## 11. Lean formalization and artifact boundary

The formal development separates four layers:

1. static proposition-valued profiles and their domains;
2. a deterministic finite-word continuation model;
3. relation/kernel results about compatible observations;
4. finite hostile and strictness fixtures.

The central static declarations are:

```text
ProfileCompatible
DistinctDomainMediator
HasCommonCore
UniformCompatibilityTransitive
commonCore_iff_domainMediator
uniformCompatibilityTransitive_iff_domainMediator
```

The continuation and canonicality surface includes:

```text
CommonCompatible
PartialFutureSufficient
greatestCompatible_exists_iff_transitive
futureSufficient_iff_kernel_refines
commonCompatible_trans_of_domainMediator
greatestCommonCompatible_exists_of_domainMediator
```

The focused campaign gate compiled 40 declarations in the domain-overlap layer
and reran 31 partial-domain, 23 continuation-quotient, 16 continuation-hazard,
and 57 compositional-admissibility regression declarations. It found no
`sorry`, `sorryAx`, `admit`, or local axiom declarations. The principal
structural and sharpness theorems were axiom-free; inherited quotient and
finite-fixture declarations account for the broader reported footprint of
`Classical.choice`, `Quot.sound`, and `propext`.

The current paper directory is not yet a standalone formal artifact. The
verified development revision and toolchain are recorded in
`FORMAL-ARTIFACT.md`; a minimal portable extraction and fresh-clone replay are
release tasks. Until those are complete, this manuscript should be described as
a draft backed by verified development evidence, not as an independently
replayable package.

## 12. Limitations

The theorem has a deliberately narrow scope.

1. **Static profile quantifier.** Uniform sharpness ranges over arbitrary
   proposition-valued static profiles. It does not prove that every adversarial
   profile is realizable by a given transition system.
2. **Fixed-model necessity is false.** A particular decision assignment may be
   transitive outside the Δ-system class.
3. **No cardinality result.** Greatest equivalence under relation inclusion is
   not a theorem about the smallest observation codomain or minimum number of
   monitor states.
4. **No behavioral equivalence.** Common compatibility and the stronger future
   relation are not claimed to be bisimulation, trace equivalence, or complete
   operational semantics.
5. **No dynamic or probabilistic domains.** Availability is frozen, and
   decisions are proposition-valued. Noise, time variation, and partial trust
   are absent.
6. **No production validation.** The monitor example is an exact model
   illustration, not evidence about a deployed API.
7. **No novelty claim for the ingredients.** Partial-function compatibility,
   tolerance nontransitivity, incomplete-machine covers, and Δ-systems are
   established.
8. **No empirical promotion.** The theorem does not repair or validate any
   neural-representation experiment.

The nearest unpursued mathematical question is fixed-profile transitivity
outside the Δ-system class. Mediator holes create potential violations, but a
particular labeling may neutralize them. The present work does not establish
whether those exceptions admit a clean forbidden-pattern theory or only a
constraint catalog.

## 13. Conclusion

Agreement on common domains is a natural relation for partial observations. It
is not, by itself, a safe equality surrogate. A state that lacks the query on
which two endpoints disagree can mediate two compatible comparisons while the
endpoints remain incompatible.

There are two clean ways to recover canonical abstraction. The semantic repair
preserves availability and outcomes together, yielding a future equivalence and
a canonical quotient. The structural repair keeps the weaker, domain-ignoring
semantics but constrains the domains. Uniformly over static decision profiles,
the exact condition is Δ-system/common-root geometry.

The practical lesson is modest and precise:

> Pairwise agreement over shared answerability does not automatically compose.
> If answerability is erased, canonicality requires a structural reason.

## References

[1] C. Borlido and B. McLean, “Difference–restriction algebras of partial
functions with operators: discrete duality and completion,” *Journal of
Algebra*, vol. 604, pp. 760–789, 2022.
doi:[10.1016/j.jalgebra.2022.03.039](https://doi.org/10.1016/j.jalgebra.2022.03.039).

[2] M. J. Schroeder and M. H. Wright, “Tolerance and Weak Tolerance Relations,”
*Journal of Combinatorial Mathematics and Combinatorial Computing*, vol. 11,
pp. 123–160, 1992.
[Article and PDF](https://combinatorialpress.com/jcmcc-articles/volume-011/tolerance-and-weak-tolerance-relations/).

[3] W. Bartol, J. Miró, K. Pióro, and F. Rosselló, “On the coverings by tolerance classes,”
*Information Sciences*, vol. 166, pp. 193–211, 2004.
doi:[10.1016/j.ins.2003.12.002](https://doi.org/10.1016/j.ins.2003.12.002).

[4] M. C. Paull and S. H. Unger, “Minimizing the Number of States in
Incompletely Specified Sequential Switching Functions,” *IRE Transactions on
Electronic Computers*, vol. EC-8, no. 3, pp. 356–367, 1959.
doi:[10.1109/TEC.1959.5222697](https://doi.org/10.1109/TEC.1959.5222697).

[5] P. van den Bos, R. Janssen, and J. Moerman, “n-Complete Test Suites for
IOCO,” *Software Quality Journal*, vol. 27, no. 2, pp. 563–588, 2019.
doi:[10.1007/s11219-018-9422-x](https://doi.org/10.1007/s11219-018-9422-x).

[6] M. Crochemore, C. S. Iliopoulos, T. Kociumaka, M. Kubica, A. Langiu,
J. Radoszewski, W. Rytter, B. Szreder, and T. Waleń, “A Note on the Longest
Common Compatible Prefix Problem for Partial Words,” arXiv:1312.2381, 2013.
[arXiv](https://arxiv.org/abs/1312.2381).

[7] P. Erdős and R. Rado, “Intersection Theorems for Systems of Sets,”
*Journal of the London Mathematical Society*, vol. s1-35, no. 1, pp. 85–90,
1960.
doi:[10.1112/jlms/s1-35.1.85](https://doi.org/10.1112/jlms/s1-35.1.85).

[8] P. Sánchez Terraf, “Cofinality and the Delta System Lemma,” *Archive of
Formal Proofs*, 2020.
[AFP entry](https://isa-afp.org/entries/Delta_System_Lemma.html).

[9] A. Nerode, “Linear Automaton Transformations,” *Proceedings of the American
Mathematical Society*, vol. 9, no. 4, pp. 541–544, 1958.
doi:[10.1090/S0002-9939-1958-0135681-9](https://doi.org/10.1090/S0002-9939-1958-0135681-9).

[10] I. Dinur, Y. Filmus, and P. Harsha, “Agreement Tests on Graphs and
Hypergraphs,” *SIAM Journal on Computing*, vol. 54, no. 2, pp. 279–320, 2025.
doi:[10.1137/21M1397684](https://doi.org/10.1137/21M1397684).
