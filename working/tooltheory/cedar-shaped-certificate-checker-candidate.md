# Cedar-shaped certificate checker (design boundary, NOT authorized)

**SUPERSEDED 2026-06-09 by [[conversion-router-candidate]].** Forcing
consumer named: Nightshift (`~/git/scheduler/crates/nightshiftd/`), not
NQ V2. This file is preserved as analysis archive only — for the
diagnostic Cedar-comparison material. The live scoping artifact is
[[conversion-router-candidate]], which explicitly drops Cedar framing
except as disclaimer.

**Policy correction, 2026-07-14:** the archive's runtime-consumer-first build
tree is historical and not operative. A coherent formal contract may lead code;
runtime rollout and public promotion are separate, and conformance requires an
explicit mapping plus evidence or refinement. The live router note carries the
corrected policy.

**Status:** UNRATIFIED design seed, superseded. **NOT** authorized to
build.
**Originally gated on:** a real forcing consumer — originally
hypothesized as NQ `TESTIMONY_DEPENDENCY V2`. *Superseded:* Nightshift
materialized first, on a different surface (Wicket / WLP / freshness),
which inverts the build trigger and Nightshift-scopes the artifact.
**Date filed:** 2026-06-09.
**Provenance:** Fable (Anthropic web, 2026-06-09 release, common-mode
with Claude Code) + chatgpt synthesis. Two Claude-family models in
agreement; **common-mode caveat** applies
([[feedback-claude-common-mode-synthesis]]) — the framing is candidate,
the technical core is inspectable.
**Custody:** working note in `working/tooltheory/`. Not a Lean module,
not promoted, not authorized for implementation.

## What this note IS

A **design boundary**: it tells you exactly what the mathy core of the
seam-graph / router work could become **if** a forcing consumer
materializes, and exactly where the hallucination perimeter is. Per
[[feedback-forcing-case]] and the corpus's YAGNI/completeness composition
rule: name early, ratify lazily, build only when forced.

## What this note is NOT

- Not a build authorization.
- Not a promotion of the seam-graph candidate or `TopologyRouterCandidate`
  into kernel-adjacent status.
- Not a claim that the proposed core is the right design — it's the
  smallest design that would survive Cedar-analogy scrutiny.
- Not "Cedar for governance." That phrasing is explicitly refused below.

## The publishable phrase

The framings that survive harsh review:

> **A certificate-checking approach to admissible claim conversion.**

Or, more technically:

> **Receipt-labeled conversion graphs with machine-checkable
> non-reachability certificates.**

The framings that do NOT survive:
- "Cedar for governance" — collides with Cedar's actual domain
  (closed-world authorization), invites authorized→safe collapse by
  vocabulary capture. **Refused.**
- "Authorization language" — same problem.
- "Machine-checked governance" — Lean checks the map, not the
  governing.
- "Verified agent policy" — verification scope would be the routing
  algebra, not agent behavior.
- "Topology" — still cursed. The corpus's signature move is *refusing*
  closure; the artifact has no opens, no continuity, no closure axioms.
  The best sentence in `seam-graph-candidate.md` — "no closure
  operator" — is literally an anti-topology statement.
- "Semantic completeness" — the engine can only prove no route *in the
  inventory*; any phrasing implying no conversion *exists* would be the
  silent promotion the whole stack exists to refuse.

## Fable's eight answers (preserved)

### 1. Closest Cedar-like artifact

Not a DSL for claim conversion in general (no consumer, "claims" is
unbounded). Not a "policy language for evidence/authority routing"
(overclaims into Cedar's territory). The defensible target: **a
certificate format plus checker for conversion routing** — receipts,
cuts, and non-reachability certificates — with a small router engine
in front.

**Underappreciated observation:** the most Cedar-shaped artifacts the
repo already contains are not the graph — they are
`FiatAdmissibility.classify` and `NumericalAdmissibility.classify`.
Total, decidable, executable policy functions from `(kind, use) →
verdict`, with a closure property. Grep-verified at type level
(plain `def`, no `noncomputable`). That **is** a microscopic policy
language with mechanized semantics, today. A Cedar-like system here
would put those tables as the per-surface policy layer and the
router as the inter-surface layer.

### 2. Smallest mathematically real core

Strip prose, this survives:

- finite labeled digraph;
- reflexive-transitive closure;
- **non-reachability certificates as forward-closed sets** (A∈S, B∉S,
  S closed under edges);
- edge-monotonicity of reachability;
- conditional edges gated by discharged obligations (the
  `CorrectiveMonotone` / `SafetyEnv.preserves` / `MergeAdmissible`
  pattern — dependent records as gates).

**Clean metatheorem hiding in there:** closed-set certificates are not
just sound but **complete** — if ¬Reach A B, the reachable set from A
is itself a certificate. Every negative answer ships with an
independently checkable witness.

Everything else (custody labels, receipt URIs, the kernels themselves)
is metadata discipline and domain content, not reusable machinery.
The projection pattern (richer config → kernel config, per-step lemma,
inherited containment) is a standard simulation argument — reusable as
discipline, not novel as math.

### 3. Cedar-style semantics — coherent or fake?

The tri-valued query `route(A, B, receipts) → {path |
blocked-by-named-cut | open}` is **coherent with one honest
restriction and fake without it.**

- **Coherent version:** the answer is about the *inventory*, full stop.
  "Blocked" means a cut receipt is on file; "open" means neither edge
  nor cut; the engine checks graph facts and receipt *presence*, never
  receipt *truth*.
- **Fake version:** any phrasing where the engine's "no route" reads
  as a fact about the world, or even about the full repo.

Cedar doesn't have this gap because in authorization the policy *is*
the authority — closed world by construction. The corpus's domain is
**open-world** at the semantic layer; the only honest move is to make
the inventory the primary artifact (the thing tools consume and humans
author), rather than a hand-drawn map of Lean files. **That inversion
is the entire pivot from catalog to language** — and it's also what
kills the redshift problem hit twice this week: generated inventory
can't drift from encoded inventory.

### 4. What Lean could actually prove

Real targets:

- (a) correctness of a routing decision procedure against `Reach` —
  finite-graph BFS, soundness and completeness;
- (b) certificate-checker correctness — "checker accepts S ⟺ S certifies
  ¬Reach A B", plus the completeness fact from §2;
- (c) conservativity — `Reach E ⊆ Reach (E ∪ {e})`; bridges only add
  routes; cut-set corollary: "B unreachable in E∖Bridges ⟹ every A→B
  path crosses a bridge edge" — the precise content of *no route
  without bridge*;
- (d) countermodel non-vacuity (already done in the repo's
  witness-discharge style);
- (e) implementation/model equivalence by differential testing, if a
  checker is built — Cedar's actual technique.

**Not provable, ever**, and should be stated in the artifact's first
paragraph: that the encoded graph matches the repo (documentary
binding); that receipts are true; that surface names mean what a
consumer assumes. "Receipt label soundness" degrades to a linter fact —
every edge's receipt field resolves to an existing declaration — which
is useful CI but not a theorem. **Calling it one would be the
manufactured-receipt crime with extra steps.**

### 5. The smallest useful tool

- **Data model:** TOML/JSON — `surfaces`, `edges {src, dst, type ∈
  {preservation, projection, bridge, conditional, parametric},
  receipt-URI, custody}`, `cuts {src, dst, kind, receipt-URI}`.
- **Router:** BFS emitting either a path with its receipt chain or a
  closed-set certificate plus matching cut receipts.
- **Checker:** ~50 lines, verifies certificates independently of the
  router. **This is the piece to prove correct in Lean and port.**
- **Generator:** emits the inventory markdown from the data file — the
  hand-built document becomes build output.
- **CLI:** `convroute --from authorizedStep --to safe` →
  `BLOCKED — certificate: {authorizedStep, authorizedVerdict,
  standingToClaim}; cuts on file: K1 (authorized_step_not_safe, …)`.
- **Differential tests:** random graphs, Rust against Lean `decide`.

Rust because `standing` already establishes that production idiom. Total
size: a **weekend-scale core with a long curation tail** — the curation
*is* the product.

### 6. Where Cedar analogy holds and breaks

**Holds, narrowly and genuinely:** small finite language; decidable
executable semantics; mechanized model with proven kernel;
implementation checked against the model; certificate-producing;
decidable analyzability questions ("is this cut vacuous?", "does adding
edge e create a forbidden route?").

**Breaks, structurally:**

- Cedar adjudicates *permission* in a closed world where evaluation
  settles the question; the corpus adjudicates *epistemic conversion*
  in an open world where evaluation settles only the inventory.
- Cedar's analyzability is SMT over a rich term language; the corpus's
  is trivial until surfaces become indexed (per-env, per-claim — per
  the router's own refusal note 4), at which point **you're building a
  type system and should say that word instead of "language."**
- Cedar's negative results protect *resources*; the corpus's protect
  *vocabulary*. Blurring those would be the exact laundering the
  kernels block.

### 7. Forcing consumer

**Currently none — say it plainly.** Candidates in order of realism:

1. **NQ `TESTIMONY_DEPENDENCY V2`** — the repo's `RefusalPropagation`
   header explicitly names this as the deferred consumer. "Is this
   finding's basis chain refused upstream?" is literally a
   `DependsTrans` reachability query. If V2 lands wanting that answer
   at runtime, **forcing event with a paper trail.**
2. **agent_gov** wanting mechanical answers to "may this claim kind be
   used for this purpose" — but already served by the `classify`
   tables without any graph.
3. **Nobody**, in which case the harsh disposition stands: keep as
   Lean notes with unusually good custody hygiene, and stop there.
   That is a respectable answer.

Publishing follows the same gate: with a tool and a consumer, this is
a credible formal-methods experience-report in the Cedar-paper genre
(and the manufactured-receipts incident from this week is a genuinely
good motivating anecdote for mechanical receipt-checking in multi-model
workflows). Without them, it's a blog post.

### 8. The dangerous overclaims

Listed under "publishable phrase" above. Each one would commit the
corpus's founding crime in its own marketing.

## The build decision tree (if forced)

```text
No NQ V2 forcing consumer
→ keep as working note / paper material / design seed (CURRENT STATE)

NQ V2 wants dependency/refusal routing
→ build tiny certificate checker first
→ then maybe Lean model + Rust/Python implementation + differential tests
→ inventory becomes generated, not hand-maintained
```

The five-piece build shape (preserved from chatgpt synthesis):

1. **Data file** — `surfaces`, `edges`, `cuts`, `receipts`,
   `custody/status`, `commit/tree`.
2. **Router** — BFS for positive path; closed-set certificate for
   negative; open / missing-bridge result.
3. **Checker** — independently verifies path or closed-set certificate;
   does not trust router output.
4. **Lean model** — checker correctness over finite graphs; closed-set
   certificate soundness/completeness; bridge-addition monotonicity /
   conservativity.
5. **Generated markdown** — seam inventory becomes output, not
   hand-maintained scripture. **The inventory rot hit this week is the
   motivating bug report.**

## Why this is filed without authorization to build

- **Forcing-case discipline.** Per [[feedback-forcing-case]], naming
  the abstraction is how recurrence is discovered; building requires
  a current consumer or recurrence trigger. NQ V2 is named, not
  delivered.
- **No-unifier doctrine.** Per [[project-no-unifier-without-laundering]],
  the corpus refuses cross-kernel federation; the certificate checker
  is precisely the kind of unifier the doctrine refuses **unless** a
  consumer outside the corpus forces it. (NQ V2 would be such a
  consumer.)
- **Completeness over novelty.** Per the global CLAUDE.md's
  YAGNI/completeness composition rule, completeness gates already-open
  surfaces. This is a new surface, governed by forcing-case. The
  existing surfaces (CorrectiveBoundary, NoFreeStandingBridge,
  seam-graph-candidate) all have their own completeness obligations
  before any new surface gets opened.
- **Vocabulary mill risk.** Per Fable §7 of the genre diagnosis
  ([[genre-diagnosis-lean-admissibility]]), refusal kernels are cheap
  to mint and binding to consumers is expensive. Naming this design
  boundary commits no marginal kernel-production cost; building it
  without a consumer would be the vocabulary-mill failure mode.

## Cohesion with already-filed artifacts

This design boundary, if built, would:

- consume the typed-edge vocabulary already filed in
  [[seam-graph-candidate]] (PRESERVATION / PROJECTION / BRIDGE /
  CONDITIONAL / PARAMETRIC) as its data model;
- consume the cut vocabulary (BLOCKING / COUNTERMODEL / NO-LIFT /
  ISOLATION / MODEL-DEPENDENCE / DECLARED-MISSING) as its certificate
  taxonomy;
- subsume the `TopologyRouterCandidate.lean` probe as the in-Lean
  model of the routing algebra;
- inherit the genre-diagnosis self-limiting description
  ([[genre-diagnosis-lean-admissibility]]) as its README's first
  paragraph (specifically the "Lean checks the map, not the
  governing" framing).

The cohesion means: if the forcing event materializes, the design has
non-trivial scaffold already filed. If it doesn't, the scaffold stays
useful as documentation regardless.

## Local verification receipt

- `FiatAdmissibility.classify : ArtifactKind → UseKind → Classification`
  — confirmed plain `def`, total, executable (grep against
  `LeanProofs/Admissibility/FiatAdmissibility.lean:102`, 2026-06-09).
- `NumericalAdmissibility.classify : NumericalKind → NumericalUse →
  Classification` — confirmed plain `def`, total, executable
  (`NumericalAdmissibility.lean:207`).
- Both are decidable by `decide` at the value level (codomain is a
  small enum); both satisfy Fable's "microscopic policy language with
  mechanized semantics, today" characterization.

## Doctrine links

- [[seam-graph-candidate]] — the typed-edge / typed-cut vocabulary this
  design would consume.
- [[genre-diagnosis-lean-admissibility]] — the self-limiting genre
  description; "Lean adjudicates a vocabulary, not a system" framing
  belongs in this design's first paragraph if it is ever built.
- [[external-model-find-corrective-boundary]] — the prior external-model
  finding pattern; the manufactured-receipts incident this week is the
  motivating anecdote for the linter / generator / checker discipline
  in the build shape above.
- [[feedback-forcing-case]] — gates whether this design ever moves from
  candidate to build.
- [[project-no-unifier-without-laundering]] — explains why the certificate
  checker is the kind of unifier the doctrine refuses absent an
  external forcing consumer.
- [[feedback-claude-common-mode-synthesis]] — the framings here are two
  Anthropic models in agreement plus one non-Anthropic synthesis;
  treat as candidate single-vendor framing.
