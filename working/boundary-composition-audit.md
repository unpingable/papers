# Boundary Composition — Kernel Audit

**Logged:** 2026-05-05 (continuation of `boundary-composition-investigation.md`)
**Status:** First deliverable on the investigative branch. **Audit, not theorem.** No new Lean stated; no `BoundaryCompositionExperiments` opened. Outcome here decides whether targets are stated next.
**Lives near:** P28 candidate territory. Inputs the synthesis question for the P22→P27 spine.
**Repo state read:** `~/git/lean/LeanProofs/Admissibility/` (Authority, StateTransition, Derivation, Execution, Corrective) plus `~/git/lean/LeanProofs/Admissibility.lean` (P27 skeleton). All five kernel modules are `sorry`-free; axioms are exactly the documented opaque substrate (`PolicyStore`, `EvidenceStore`, `GapStore`, `RevocationStore`, `Receipt`, `Gap`, `Revocation`, `PolicyUpdate`, `Actor`, `AuthorityClaim`, four abstract store ops, four abstract `*Standing` predicates). README's warrant claim is honest against the code.

---

## Method, with caveats

This audit fills the table the investigation note posted. Two things were forced into the open during the walk and are recorded here rather than absorbed silently:

1. **The kernel uses *several* senses of "boundary."** Verdict dimensions (basis / precedence / standing), store-partition walls (policy / evidence / gap / revocation), Step classifications (corrective / forward / neutral), and the `WeaklyLessPermissive` preorder are all reasonably called "boundaries" in prose. They are *not* the same kind of object. The audit cannot answer "do boundaries compose?" until it names which sense composition is being asked about. Glossary below.
2. **"Action" splits across layers.** What gets authorized at the verdict / derivation layer is `AuthorityClaim`; what gets executed at the state-transition / execution layer is `Step`. They are bridged at Layer 4 by `claimForStep : GovState → Actor → Step → AuthorityClaim`. An honest action-indexing column has to track *which* notion of action the theorem is indexed against.

Neither caveat is a complaint about the kernel — both are findings. Synthesis vocabulary that does not respect these splits will produce a fake calculus.

---

## Boundary glossary (provisional, audit-only)

Numbering is local to this document. None of these are minted primitives; they are descriptive labels for senses already present in the code.

- **B1 — Verdict-dimension boundary.** `BasisVerdict`, `PrecedenceVerdict`, `StandingVerdict`. A verdict-dimension boundary fails when its dimension is not green. Authority refusal is the conjunction of three independent dimension states. *Layer 0.*
- **B2 — Store-partition boundary.** Wall between `PolicyStore` / `EvidenceStore` / `GapStore` / `RevocationStore`. A store-partition boundary fails when a `Step` mutates a store other than its own — by construction this cannot happen, since `applyStep` rewrites exactly one field. *Layer 3a.*
- **B3 — Mutation-permission boundary.** `StepAllowed` together with the four `*Standing` predicates. A mutation-permission boundary fails when a Step is applied without its corresponding standing witness. *Layer 3b.*
- **B4 — Claim-invocation boundary.** `decideAuthority`'s component derivations (`basisRevoked` so far; future `precedenceConflicting`, `standingRevoked`, etc.). A claim-invocation boundary fails when the derivation env recognizes a blocking condition for the specific claim. *Layer 2.*
- **B5 — Classification boundary.** `IsCorrective` / `IsForward` / `IsNeutral` (via `classify`). A classification boundary is the wall between authority-down-edges and authority-up-edges. Disjointness theorems (`corrective_not_forward` etc.) keep it from collapsing. *Layer 5.*
- **B6 — Authorization-set order.** `WeaklyLessPermissive env Γ' Γ`. Not a boundary in the refusal sense; a *direction* on the authorization surface. Corrective steps are below; forward steps are not constrained by it. *Layer 5.*

These are not equiplanar. B1 and B4 live at the verdict / derivation layer (read-side). B2 and B3 live at the mutation layer (write-side). B5 and B6 are an orthogonal gradient over both. The composition question for a Boundary Calculus has *different content* depending on which Bᵢ × Bⱼ pair it asks about.

---

## Per-object audit

Columns: kind (which Bᵢ does this object belong to or operate on?), composes (what does this combine?), blocks (what would prevent composing?), action-indexed (claim or Step?), derivation-indexed (does the conclusion mention the env / derivation that supplies the boundary?), state-indexed (does it reach into ambient `GovState`?), already-composition (single-step property vs theorem-of-theorems?), individuation (would collapsing the relevant split kill the proof?), generalizable (without redefining terms?).

### Layer 0 — `Authority.lean`

| Object | Kind | Composes | Blocks | Action-idx | Deriv-idx | State-idx | Already comp | Individuation | Generalizable |
|---|---|---|---|---|---|---|---|---|---|
| `authorityVerdict b p s` | B1×B1×B1 | three dimension verdicts → AuthorityVerdict | non-green dim | n/a (pure algebra) | n/a | no | gate, not theorem | yes — collapsing dims → vacuous gate | bounded: the gate shape *is* the algebra |
| `no_basis_never_authorized`, `advisory_basis_never_authorized`, `incomparable_precedence_never_authorized`, `conflicting_precedence_never_authorized`, `no_standing_never_authorized` | B1 | dimension-state → ¬authorized | — | n/a | n/a | no | single-dim properties | yes — proving them collectively gives `authorized_iff_all_green` | yes (each generalizes within its dim) |
| `authorized_iff_all_green` | B1×B1×B1 | the five negative invariants + positivity | — | n/a | n/a | no | **yes — first composition theorem in the kernel** | yes | bounded by gate shape |
| `authorized_requires_*` projections | B1 | iff-mp | — | n/a | n/a | no | corollaries | n/a | yes |

**Finding.** Layer 0 has one composition theorem, `authorized_iff_all_green`, but it is composition *across the three verdict dimensions of one boundary kind*, not composition across boundary kinds. It is the algebraic gate, not a calculus result. Action-indexing is `n/a` because the layer has no notion of action — verdicts are over abstract dimension states.

### Layer 3a + 3b — `StateTransition.lean`

| Object | Kind | Composes | Blocks | Action-idx | Deriv-idx | State-idx | Already comp | Individuation | Generalizable |
|---|---|---|---|---|---|---|---|---|---|
| `applyStep state step` (Layer 3a) | B2 | Step + GovState → GovState | — | Step | no | yes | no | yes — collapsing the four stores into one breaks the trapdoor theorems | yes within mutation algebra |
| `record_receipt_does_not_amend_policy` ×3 (per non-amend constructor) | B2 | partition discipline | — | specific Step constructor | no | yes | no — single-step | **yes load-bearing** — partition is the whole point | yes (one per non-amend Step kind) |
| `amend_policy_targets_policy_store` | B2 | positivity for amendment | — | `Step.amendPolicy` | no | yes | no — single-step | yes | yes |
| `StepAllowed`, `executeIfAllowed` (Layer 3b) | B3 | Step × `*Standing` predicate | absence of standing witness | Step | no (standing predicate is in env, but conclusion is `StepAllowed`, not derivation-keyed) | yes (predicates take state) | by construction — ctor requires the witness | yes — `*Standing` per-store individuation matches B2 partition | yes |
| `execute_*_does_not_amend_policy` ×3 | B2×B3 | wrapper trapdoor lifted through Layer 3b | — | Step | no | yes | **lifts a 3a property through 3b — first cross-layer composition** | yes | yes |
| `execute_amend_policy_targets_policy_store` | B2×B3 | wrapper positivity | — | Step | no | yes | lifted | yes | yes |

**Finding.** Layer 3 has *two* boundary kinds (B2 store-partition and B3 mutation-permission) and the wrapper trapdoor theorems compose them at the Step level: a `StepAllowed`-witnessed `Step.recordReceipt` is *both* permitted and constrained-not-to-amend-policy. This is real cross-boundary composition, action-indexed (on `Step`), state-indexed, but **not** derivation-indexed — Layer 3 has no derivation env yet.

### Layer 2 — `Derivation.lean`

| Object | Kind | Composes | Blocks | Action-idx | Deriv-idx | State-idx | Already comp | Individuation | Generalizable |
|---|---|---|---|---|---|---|---|---|---|
| `BasisDerivation` (struct) | B4 | function + `revoked_never_admissible` obligation | — | claim | yes (carries the law) | yes (deriveBasis takes state) | bundle, not theorem | yes — without the obligation, claim-invocation boundary is vacuous | bounded |
| `PrecedenceDerivation`, `StandingDerivation` | B4 | functions only | — | claim | yes | yes | bundle | symmetric obligations not yet stated; the slot is shaped right | yes (pending obligations) |
| `DerivationEnv` | B4×B4×B4 | three derivations | — | claim | yes | yes | composition shape | yes | bounded by env shape |
| `decideAuthority env state actor claim` | B4 → B1 | env + state + actor + claim → AuthorityVerdict | — | claim | yes | yes | function, not theorem | yes (relies on Layer 0 gate) | bounded |
| `decide_authorized_requires_all_green` | B4×B1 | bridge: env-derived verdicts ↔ Layer 0 algebra | — | claim | yes | yes | **yes — first vertical composition theorem (B4 read-side ↔ B1 verdict-shape)** | yes | direct corollary; tight |
| `revoked_basis_never_authorized` | B4 | `basisRevoked state claim` + bridge → ¬authorized | — | claim (same `claim` in hypothesis and conclusion) | yes (env carries the obligation) | yes | **yes — first action-indexed safety theorem in the kernel** | yes (basisRevoked is *of* the claim) | yes — symmetric ones for precedence/standing fit the same shape (deferred) |

**Finding.** Layer 2 introduces B4 (claim-invocation boundary) and bridges it vertically to B1 (verdict algebra). `revoked_basis_never_authorized` is the first action-indexed ¬authorized theorem and is correctly action-keyed: the claim recognized as revoked is the claim denied. It is also derivation-indexed in the kernel's idiom — the conclusion is keyed to the same `env` that supplies the revocation predicate, which is the shape of "this env cannot launder this claim." A different env with no revocation predicate could authorize, which is exactly DeepSeek's `¬ authorized_by d a` (rather than `¬ authorized a`) discipline expressed through env-parameterization.

### Layer 4 — `Execution.lean`

| Object | Kind | Composes | Blocks | Action-idx | Deriv-idx | State-idx | Already comp | Individuation | Generalizable |
|---|---|---|---|---|---|---|---|---|---|
| `ExecutionEnv` | B4 + claim-resolution | DerivationEnv + `claimForStep` | — | both (claim and Step, bridged) | yes | yes | bundle | the bridge is load-bearing; its absence is what kept the kernel from warranting "stale basis cannot bind" before this layer landed | bounded by shape of bridge |
| `stepAuthorityVerdict` | B4 routed via Step | `claimForStep` ∘ `decideAuthority` | — | both | yes | yes | function | yes | yes |
| `AuthorizedStep env state actor` (struct) | B3×B4 | `StepAllowed` ∧ `stepAuthorityVerdict = authorized` | one half missing | both, simultaneously | yes | yes | **structural composition: by construction you cannot get one without the other** | the *both* is the whole point | yes |
| `executeAuthorizedStep` | B3×B4 → mutation | `applyStep` parametric over the proofs | — | both | yes | yes | reduction to Layer 3a, mediated by the structure | yes | yes |
| `authorized_step_requires_authority` | B4 from struct | extraction | — | both | yes | yes | trivial projection | n/a | yes |
| `revoked_basis_cannot_be_authorized_step` | B4 → ¬B3∧B4 | revocation ⇒ no AuthorizedStep with that step | — | Step (bridged via `claimForStep` to the revoked claim) | yes (env supplies the revocation obligation) | yes | **yes — load-bearing horizontal composition: chains `revoked_basis_never_authorized` (Derivation) into the Execution structure** | yes (the same Step is denied) | yes — symmetric variants (revoked_standing, conflicting_precedence) fit the same shape; deferred |
| `authorized_record_receipt_does_not_amend_policy`, `..._declare_policy_gap_...`, `..._record_revocation_...` | B2×B3×B4 | lifts Layer 3a trapdoors through the AuthorizedStep structure | — | Step (constrained by hypothesis) | yes | yes | **lifts B2 partition theorems through B3+B4 wrapper — three-boundary composition** | yes | yes |
| `authorized_amend_policy_targets_policy_store` | B2×B3×B4 | positivity through three boundaries | — | Step | yes | yes | three-boundary composition | yes | yes |

**Finding.** Layer 4 is where the kernel *first does composition across heterogeneous boundary kinds* in a load-bearing way: `revoked_basis_cannot_be_authorized_step` chains a B4 fact (basis revoked) through the `claimForStep` bridge to a B3-shaped conclusion (no `AuthorizedStep`). The four lifted store-isolation theorems compose three boundaries (B2 + B3 + B4) on the same Step. This is the strongest evidence that *some* boundary composition is real in the kernel.

But: the composition is always a *projection* through the AuthorizedStep structure, not an arithmetic of independent boundary theorems. The structure carries both proofs by construction; the theorems do not assemble two free-standing boundaries into a third. That is a discriminator the audit must record honestly — see cross-cutting finding (3) below.

### Layer 5 — `Corrective.lean`

| Object | Kind | Composes | Blocks | Action-idx | Deriv-idx | State-idx | Already comp | Individuation | Generalizable |
|---|---|---|---|---|---|---|---|---|---|
| `StepClassification`, `classify : Step → StepClassification` | B5 | total classification | non-exhaustive match (compile error) | Step | no | no | enforcement surface, not theorem | yes — disjointness lemmas show collapse breaks the structure | yes (every future Step constructor must classify) |
| `IsCorrective`, `IsForward`, `IsNeutral` | B5 | predicates | — | Step | no | no | predicates | yes | yes |
| `corrective_not_forward`, `corrective_not_neutral` | B5 | classification disjointness | — | Step | no | no | single-step | **yes — these are exactly the "individuation load-bearing" check for B5** | yes |
| `WeaklyLessPermissive env Γ' Γ` | B6 | preorder over GovState authorizations | — | quantifies over claim universally | yes (env fixed) | yes (two states) | preorder, not theorem | env-fixed — environment mutation is a separate vector (open question §5) | yes |
| `weakly_less_permissive_refl/_trans` | B6 | preorder sanity | — | universal | yes | yes | sanity | n/a | yes |
| `CorrectiveMonotone env` (struct) | B5→B6 obligation | obligation: `IsCorrective` → `WeaklyLessPermissive (applyStep Γ s) Γ` | — | quantifies over Step and Γ | yes (env-keyed) | yes | bundle obligation, not theorem | yes — vacuous under current store axioms (open question §4); first non-vacuous case forces behavioral laws | bounded by current vacuity |
| `corrective_monotone` | B5→B6 | obligation under-discharge | — | Step | yes | yes | projects obligation | yes | yes |
| `corrective_no_authority_laundering` | B5→B6, same-K | corrective Step + ¬authorized at Γ ⇒ ¬authorized at applyStep Γ s, **same K** | — | claim K (same in hypothesis and conclusion) AND Step | yes | yes | **yes — same-K is load-bearing; documented as such** | yes — collapsing same-K into "any K" makes the theorem false (re-entry through fresh K' is exactly the legitimate path) | yes |
| `applySteps`, `corrective_sequence_monotone` | B5→B6 over List Step | sequence composition through `weakly_less_permissive_trans` | — | quantifies over claim | yes | yes | **yes — sequence composition theorem; same-class only (all corrective)** | yes | only stated for all-corrective sequences; mixed sequences not covered |
| `RecoveryEnv`, `applyCorrectiveRecovery`, `recovery_monotone` | B5→B6 + obligation gating | bundles env with discharged obligation; type-gates the recovery surface | — | quantifies | yes | yes | bundle + projection | yes — operational gate at the recovery boundary | yes |

**Finding.** Layer 5 introduces B5 (classification) and B6 (preorder direction) and proves a *same-class sequence-composition theorem* (`corrective_sequence_monotone`) plus a *single-step monotonicity-with-same-K* result (`corrective_no_authority_laundering`). These are real composition theorems. They are however only over **homogeneous** sequences (all corrective) and over **single-claim same-K** rather than across two genuinely different claim/action pairs.

The CorrectiveMonotone obligation is currently vacuous (open question §4 in `Corrective.lean`), waiting on the first concrete `BasisDerivation` that reads `RevocationStore`. That is a vocabulary-deficient region masquerading as a discharged obligation. **Audit flag.**

### `Admissibility.lean` (P27 skeleton, sibling)

| Object | Kind | Composes | Blocks | Action-idx | Deriv-idx | State-idx | Already comp | Individuation | Generalizable |
|---|---|---|---|---|---|---|---|---|---|
| `admissible Ω r` | post-transition obligation accounting (separate kind, not Bᵢ above) | accounting + durability | — | transition (via Receipt.transitionId) | no | no (no GovState) | conjunction over Ω | yes (Obligation enum) | bounded |
| `unaccounted_implies_inadmissible`, `short_receipt_horizon_inadmissible`, `open_finding_admissible_with_durability` | same | per-clause consequences | — | transition | no | no | three single-clause properties; no theorem-of-theorems | yes | yes |
| `masked_recovery_not_resolved`, `orphaned_causality_inadmissible` | same | placeholders (`True`) | — | n/a | n/a | n/a | not yet stated | n/a | vocabulary-deficient (substrate-accusation, causal-binding predicates not declared) |

**Finding.** P27 skeleton is post-action obligation accounting, separate from B1–B6. Its action-indexing is per-transition (via `Receipt.transitionId`). It is **not currently bridged** to the `Admissibility/` kernel — `claimForStep`, `AuthorizedStep`, and `obligations Ω` do not see each other. That is a cross-paper seam visible to the audit.

---

## Cross-cutting findings

### F1. The kernel's "boundary kind" pluralism is real and not a vocabulary failure

There are six distinguishable senses (B1–B6) used in load-bearing ways. They sit at different layers (read-side B1+B4 vs write-side B2+B3) or operate orthogonally (B5+B6). A Boundary Calculus that asks "do boundaries compose?" must specify which Bᵢ × Bⱼ pair, and the answer can differ per pair. This is a *kind separation* result of the audit — and it is exactly the locked-definitions discipline the working note demanded for question 7 (individuation).

### F2. Action-indexing is correctly maintained — modulo a claim/Step duality

DeepSeek's worry (theorem `¬ authorized a` from a bad-derivation `d` for arbitrary `a`) is structurally avoided here because the kernel uses *env-parameterization* in place of derivation-tagging. `decideAuthority env ... claim ≠ authorized` under `env.basis.basisRevoked state claim` is the action-and-derivation-indexed shape, expressed via `env`. A different env without that revocation predicate could authorize, which is the correct behavior.

The claim/Step duality is the only sharp edge:
- B1+B4 theorems action-index by `AuthorityClaim`.
- B2+B3 theorems action-index by `Step`.
- Layer 4 bridges via `claimForStep`. The bridge is **abstract** (no concrete resolver yet). When a concrete resolver lands, every theorem that bridges must verify that the same Step→claim mapping is consistent — otherwise the audit's action-indexing column becomes dishonest.

### F3. Composition theorems already in the kernel — by composition kind

Counted by what they actually compose. Single-direction projections through bundles are not counted as composition theorems (otherwise every record accessor would qualify).

| # | Theorem | Composition shape | Kinds |
|---|---|---|---|
| 1 | `authorized_iff_all_green` | three same-kind dimension states → gate verdict | B1×B1×B1 |
| 2 | `decide_authorized_requires_all_green` | env-derived verdicts ↔ Layer-0 gate | B4 ↔ B1 (vertical) |
| 3 | `revoked_basis_never_authorized` | per-claim revocation → ¬authorized | B4 → ¬B1 (action-indexed) |
| 4 | `execute_*_does_not_amend_policy` (×3) | Layer 3a partition lifted through Layer 3b wrapper | B2×B3 (cross-boundary) |
| 5 | `revoked_basis_cannot_be_authorized_step` | derivation-layer revocation → execution-layer impossibility | B4 → ¬(B3∧B4) (cross-layer, bridged by `claimForStep`) |
| 6 | `authorized_record_receipt_does_not_amend_policy` (×3) | Layer 3a partition lifted through Layer 4 AuthorizedStep | B2×B3×B4 (three-boundary lift) |
| 7 | `corrective_no_authority_laundering` | classification-down × preorder × same-K | B5→B6 (same-K, single-step) |
| 8 | `corrective_sequence_monotone` | sequence of corrective steps preserves preorder | B5→B6 (homogeneous sequence) |

Eight composition theorems, real. Most are vertical-lifts (a property at one layer survives wrapping at the next). Two — (5) and (8) — are sequencing/bridging theorems with non-trivial content. **None compose two heterogeneous action-level boundary theorems into a third action-level boundary theorem about a composite action.** The closest is (8), but it is homogeneous (all corrective) and does not yet handle (corrective ⨾ forward) — exactly the case the working note's question 5 ("what failure is allowed to block the whole composite?") was trying to formalize.

### F4. Vocabulary-deficient regions

Where targets *cannot* be honestly stated until vocabulary lands:

- **CorrectiveMonotone is vacuous** until the first concrete `BasisDerivation` consults `RevocationStore` — pending behavioral laws on `appendRevocation`. Without those laws, "corrective Step preserves preorder" is satisfiable trivially. (Captured in Corrective open question §4.)
- **Symmetric blocking-derivation obligations** for `PrecedenceDerivation` (no `conflicting_never_resolved`) and `StandingDerivation` (no `revoked_standing_never_standing`) — slots shaped right, content not yet committed. (Captured in Derivation TODO.)
- **`claimForStep` is abstract** — every Layer 4 bridge theorem is parametric over how Steps map to claims. Concrete resolution is deferred along with `AuthorityClaim`'s schema. Composition theorems that need to talk about *which* claim a composite Step refers to are blocked here.
- **No bridge between `deriveStanding` (Layer 2, claim invocation) and `*Standing` (Layer 3b, mutation)**. Distinct standing concepts; not yet bridged. (Captured in Derivation TODO.)
- **No bridge between `Admissibility/` kernel and `Admissibility.lean` (P27 skeleton)**. Pre-action authorization vs post-action obligation accounting are not yet glued.
- **Environment mutation is uncovered.** All B6 results fix `env`. Re-deriving authority by changing the env (replacing a `BasisDerivation`) is a separate laundering vector with no theorem yet. (Corrective open question §5.)
- **Composite-action vocabulary is absent.** The kernel has `applySteps : List Step` (sequence) and `Step` (atomic). It has no notion of `Step × Step → CompositeStep` with a derivable claim, no explicit "composite action whose claim is the composition of its parts." Question 5 of the working note needs this primitive to even be statable.

### F5. Individuation status

| Split | Status |
|---|---|
| Basis / Precedence / Standing (B1) | **Load-bearing.** Collapse → vacuous gate; the five negative-invariant theorems would have nothing to discriminate. |
| Policy / Evidence / Gap / Revocation (B2) | **Load-bearing.** Collapse → trapdoor theorems false. |
| `EvidenceWriteStanding` / `GapDeclareStanding` / etc. (B3) | **Load-bearing.** Collapse to one `Standing` predicate → `StepAllowed` becomes a single proposition; per-store individuation that mirrors B2 disappears. |
| Claim invocation derivation strategies (B4) | **Load-bearing.** Collapse → bundled obligations (`revoked_never_admissible`) cannot be hung off the relevant dimension; symmetric obligations for the other dimensions could not be added later without redesign. |
| Corrective / Forward / Neutral (B5) | **Load-bearing.** Collapse → `corrective_no_authority_laundering` becomes "any step preserves authorization," which is FALSE for forward steps. |
| `WeaklyLessPermissive` env-keyed (B6) | **Load-bearing for the recovery use.** Letting env vary silently would absorb environment-mutation laundering into the same predicate — exactly Corrective open question §5. |
| `AuthorityClaim` vs `Step` (claim/Step duality) | **Load-bearing.** Collapse → no `claimForStep` bridge needed, but the cost is losing the read/write split and the action-indexing-by-Step trapdoors. |

No load-bearing splits are decorative. The kernel pays for each one with at least one theorem that requires the split to discriminate.

---

## Mapping to the working note's candidate theorem shapes

From `boundary-composition-investigation.md` §"Candidate theorem shapes":

1. **`boundary_violation_blocks_authorization`** (action-indexed). **Already present** as `revoked_basis_never_authorized` (Derivation), specialized to "boundary kind = revocation of basis." General form (`crosses_boundary` × `required_for_action` × `¬ admissible_crossing` → `¬ authorized`) would generalize the *kind* of blocking condition; the slot is shaped correctly in the kernel via `BasisDerivation.basisRevoked` + symmetric obligations for the other dimensions. **Status: pattern proved for one boundary kind; symmetric statements vocabulary-deficient (F4, point 2).**

2. **`receipt_does_not_authorize_without_basis`** (action+derivation-indexed, conclusion `¬ authorized_by d a`). Kernel uses env-parameterization rather than derivation-tagging, but the shape is structurally equivalent. **Already present** in spirit as `revoked_basis_never_authorized` and at the execution layer as `revoked_basis_cannot_be_authorized_step`. The DeepSeek-correct conclusion (denial scoped to *this* derivation, not absolute) is preserved through `env`. **Status: ✓.**

3. **TTL / revocation breaks composition.** Already substantially present at `revoked_basis_cannot_be_authorized_step` (Execution). **Status: ✓ for revocation; TTL specifically requires durability/horizon vocabulary that lives in the P27 skeleton, currently unbridged. Bridge is the next slot if TTL gets concrete.**

4. **Kind separation: stores do not collapse into each other under transition.** Five-fold-decomposed in the kernel: B2 trapdoors (Layer 3a) + B3 standing predicates (Layer 3b) + their lifts through Layer 4. **Status: ✓ for the four stores; the *cross-kind* claim ("no Step kind launders into a different store kind") is provable for each non-amend constructor and is one direction of `applyStep`'s definitional behavior.**

5. **Possible null result: boundaries may not form a lattice or clean algebra.** **The audit's strongest finding is that this is the right framing for the current kernel.** B1–B6 are not equiplanar; composition theorems are layer-specific lifts and same-class sequence theorems, not heterogeneous action-level composition. The kernel currently expresses "Family with composition lemmas" rather than "Calculus." Mixed-class sequence composition (corrective ⨾ forward) is the first concrete obstruction whose absence is *load-bearing*: question 6 of the locked definitions ("what failure is allowed to block the whole composite?") has no kernel answer yet.

---

## Three-fork status (provisional, audit-only)

The investigation note posed three outcomes for what P28 honestly is. Reading the audit:

- **"Boundary Calculus."** Not warranted by the current kernel. There is no general action-level composition operator and no theorem of the form "two action-indexed boundary theorems → third action-indexed boundary theorem on a composite action."
- **"Admissibility Boundary Family."** Best fit. The kernel is a layered family with eight real composition theorems (F3) clustered as vertical lifts and same-class sequencing. Heterogeneous composition is reachable in a small number of pinned places (mixed corrective⨾forward sequences; cross-kind claim/Step bridges; env-mutation laundering) but vocabulary-deficient (F4) until specific store laws and a concrete `claimForStep` resolver land.
- **"Related refusals, not an algebra."** Not the worst-case reading. The eight theorems are not loosely related — they share an action-indexing discipline and a refusal grammar (the three promotion errors compress them honestly: evidence→authority via `revoked_basis_*`, mechanism→legitimacy via `AuthorizedStep`'s both-proofs-by-construction).

**Recommendation for the working note:** the synthesis target reads, after this audit, as **Admissibility Boundary Family with composition lemmas, working-name only**. P28's title would name the *family*, not the *calculus*. The "no calculus yet" finding is itself publishable content.

---

## Recommended next move

Reading the audit, here is what the work surface looks like ranked by *what would force kernel statements to fail honestly*:

1. **State (and `sorry` if needed) `corrective_then_forward_is_not_monotone`.** This is the load-bearing null statement for question 6 (what failure blocks the whole composite). It does not need new vocabulary — it can be stated against the existing `applySteps` and a witness-counterexample step list. **First investigative target.**
2. **State (and `sorry` if needed) `claim_step_action_consistency`.** With abstract `claimForStep`, the Layer-4 audit cannot rule out that a future concrete resolver returns inconsistent claims for "the same" action across two paths. The slot for the consistency obligation is right at the `ExecutionEnv` structure. **This is a vocabulary-pressure test, not a forward proof.**
3. **State (and `sorry` if needed) the symmetric blocking-derivation obligations** (`conflicting_never_resolved`, `revoked_standing_never_standing`) and their Execution-layer corollaries. **Lowest-friction kernel extension; mostly mechanical given the existing template.** This is where "extend the lean" earns its keep without designing the constitution off the sorrys.
4. **Do not yet open `BoundaryCompositionExperiments`.** Two of the three targets above can live in existing modules (Corrective.lean for #1; Derivation.lean / Execution.lean for #3). Opening a new module before #1 has run is the post-hoc-name failure mode the working note flagged.
5. **Do not yet bridge `Admissibility/` to `Admissibility.lean` (P27 skeleton).** The bridge is a real seam, but it is gated on substrate-accusation / causal-binding vocabulary that P27 has not declared. Premature bridging would import skeleton vocabulary into the kernel without a slot decision. (Same discipline the P27 file's own header invokes.)

Targets 1 and 3 are honest investigative theorems: they have a chance to fail. Target 2 is a vocabulary-pressure check on Layer 4. Together they exercise three of the audit's vocabulary-deficient regions (F4) without minting new operators. They are appropriate for the investigative branch.

Targets 1, 2, 3 are **candidate** investigative targets. Stating them is permitted under the working note's discipline. **Drafting P28 is not.**

---

## Pointers

- Investigation note: `boundary-composition-investigation.md`
- Lean kernel: `~/git/lean/LeanProofs/Admissibility/{Authority,StateTransition,Derivation,Execution,Corrective}.lean`
- Sibling kernel sketch: `~/git/lean/LeanProofs/Admissibility.lean` (P27 skeleton, unbridged)
- Recovery semantics companion (referenced from Corrective.lean docstring): `admissible-recovery-semantics.md`
- P25 substitution forcing: `preprint/25-epistemic-border-control/epistemic_border_control.md` (no kernel binding yet — flagged in F4)

---

## Shutdown / state capture (2026-05-05)

End of session. Audit + target #1 stated. Stopping, not closing.

### Current verdict

- **Boundary Calculus is still provisional.** Not warranted.
- **The honest current object is: Admissibility Boundary Family with composition lemmas.**
- **Target #1 (`corrective_then_forward_is_not_monotone`) was stateable using existing vocabulary.** No minted primitives, no broadened "boundary", no new namespace. Lives in `~/git/lean/LeanProofs/Admissibility/Corrective.lean` as a `sorry`-posture investigative theorem.
- **It failed at the warrant level, not the statement level.** The kernel can express the claim; it cannot warrant either direction.
- **The precise deficit is that abstract store operations (`applyUpdate`, `appendGap`, `appendRevocation`, `appendEvidence`) have no behavioral commitments.** Under an identity interpretation of all four ops, every Step is state-preserving and the existential is provably FALSE. The kernel is currently consistent with both the existential and its negation.
- **Therefore mixed-class sequence composition currently requires nondegenerate state-transition semantics, not a proof trick.** The deficit is a missing behavioral commitment, not a missing tactic.

### Guardrails (carry into next session)

- Do not add axioms to force the theorem.
- Do not create `Action.lean`, `Boundary.lean`, `Composition.lean`, or `Calculus.lean`.
- Do not ratify "Boundary Calculus."
- Do not draft P28 or public framing.
- Do not broaden "boundary" to make composition work.

### Next-session options (recorded, not executed)

1. **Concrete witness model.** Prove the existential in a tiny nondegenerate store model — e.g. instantiate `PolicyStore` etc. with concrete inhabited types and `applyUpdate` etc. with concrete non-identity functions, then discharge the existential against that model. Stays inside the kernel discipline by being a parallel concrete instantiation rather than an axiom.
2. **Typeclass/assumption route.** Define a minimal nondegenerate store-semantics assumption (e.g. `∃ Γ p, applyUpdate Γ.policyStore p ≠ Γ.policyStore`) and prove the theorem conditionally under it. Names the missing vocabulary precisely as a hypothesis without committing the kernel to a specific behavioral law.
3. **Null-result route.** Keep the finding as evidence that the abstract kernel alone yields **Family, not Calculus**. No further Lean work; the recorded `sorry` plus this audit *is* the result. Composition vocabulary remains a downstream concretization concern, not a kernel one.

End of state capture. Stop.

---

## DeepSeek harvest (recorded, not executed)

Outside-model proposed a Phase-0 hardening pass plus a `ProductClaim`-shaped obstruction test for mixed-class composition. Sorting before close.

### Keep

- **Phase 0 projection lemmas — valid low-risk kernel hardening if not already present.** Three Derivation-layer corollaries of `decide_authorized_requires_all_green`:
  - `basis_not_admissible_implies_not_authorized`
  - `precedence_not_resolved_implies_not_authorized`
  - `standing_not_stands_implies_not_authorized`

  Status check: `Authority.lean` already has the Layer-0 projections (`authorized_requires_admissible_basis`, `authorized_requires_resolved_precedence`, `authorized_requires_standing`) as iff-mp consequences. The Derivation-layer versions through `decideAuthority` are *not* currently present. Cheap to add; one-line proofs each. Naming nit if implementing: kernel uses `StandingVerdict.standing`, not `StandingVerdict.stands`.

- **Vertical vs horizontal split, correctly named.** Current all-green authorization (`authorized_iff_all_green`, `decide_authorized_requires_all_green`) is *vertical* composition — three same-layer dimension verdicts into one gate verdict. A calculus would require *horizontal/mixed-class* composition — combining two action-level boundary theorems into a third. This is consistent with the audit's F3 finding (eight kernel composition theorems, none horizontal-action-level).

- **Composite authorization requires a bridge from composite structure to basis/precedence/standing verdicts.** Correctly identified. The kernel currently has no such bridge for any composite-action notion; Layer-4 has `claimForStep : Step → AuthorityClaim` but that resolves a single Step to a single claim, not a composite of two claims to a derived verdict.

### Quarantine

- **Do not create `Action.lean`, `Boundary.lean`, `Composition.lean`, `Calculus.lean`.** Roadmap-flavored module proliferation; pre-empts the doctrine question.
- **Do not add `boundary_crossing_effect` as an axiom.** Same prohibition as "do not axiomatize `applyUpdate` to force the theorem" — would discharge the recorded null by smuggling in the missing vocabulary.
- **Do not use the `ProductClaim` obstruction as written.** It introduces a separate `ProductClaim` structure type where `decideAuthority` expects `AuthorityClaim`. With no embedding `ProductClaim → AuthorityClaim` defined, the goal `decideAuthority env s a1 { first := c1, second := c2 : ProductClaim } = …` fails at the *type* level, not the *semantic* level. That is a fake obstruction — the proof can't proceed because the types don't match, not because composite-verdict vocabulary is missing. The honest obstruction needs an embedding (or `ProductClaim` reified inside `AuthorityClaim`'s schema), which the kernel keeps abstract on purpose.
- **Treat the roadmap as future architecture only, not next-session implementation.** Phase 2/3 / "boundary effect axiom" / "this lemma becomes the boundary effect axiom" are doctrine-promotion shapes, not next-session work.

### Current priority (unchanged)

- **Preserve the actual AG result.** `corrective_then_forward_is_not_monotone` is stateable with existing vocabulary but unwarranted because abstract store ops lack behavioral commitments. Recorded `sorry` posture in `Corrective.lean`.
- **Next real fork remains:** concrete nondegenerate store witness (option 1) vs minimal typeclass/assumption (option 2) vs null-result documentation (option 3). DeepSeek's harvest does not change which fork is chosen.
- **No doctrine promotion. Family with composition lemmas, not Calculus.**

End of harvest. Stop.
