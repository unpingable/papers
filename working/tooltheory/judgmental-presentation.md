# Judgmental Presentation of the Admissibility Kernel

## Status

Explanatory / non-canonical.

Canonical semantics live in the Lean kernel (`~/git/lean/LeanProofs/Admissibility/`). This document introduces judgmental notation for reading the kernel. **It does not define a sequent calculus, process calculus, proof-theoretic admissibility logic, or independent proof system.** No claims are made about cut elimination, completeness, normalization, or structural-rule admissibility.

The Lean source is the proof system. This is a reading aid over it.

## Why this exists

Five readers benefit from sequent-flavored notation over the Lean source:

1. **Formal-methods-literate reader** who can parse judgments and rules but does not want to reverse-engineer 21 Lean modules from imports and theorem names.
2. **Future collaborator** deciding whether "calculus" is honest by inspecting the grammar.
3. **Implementer-reader** (NQ, Wicket, Agent Governor, Standing) mapping the kernel back to operational systems. They need the non-laundering boundaries (`evidence ≠ basis ≠ standing ≠ authority ≠ execution`) legible at a glance.
4. **Adversarial / skeptical reviewer** asking "is this a calculus or just named enums and theorems?"
5. **Future self / future agent** as a context bootloader — do not re-derive the grammar from theorem names every session.

Without a sanctioned grammar, readers and agents will mint unauthorized ones. The doc reduces hallucination pressure.

## Judgments

`Γ` stands for the governance context (state + actor + claim + derivation environment). Judgments are inhabited by Lean theorems and definitions in the kernel modules; this notation is a reading aid over those.

```
Γ ⊢ B ok       basis is admissible
Γ ⊢ P ok       precedence is active / non-conflicting
Γ ⊢ S ok       standing is present
Γ ⊢ A auth     action is authorized
Γ ⊢ A deny     action is refused / no authorization derivable
```

The shape of authorization is *three-dimensional admissibility plus refusal-on-any-dimension*. Authorization is not a primitive; it is the only case where all three component judgments succeed.

## Rules

### AUTH — three-dimensional admissibility

```
Γ ⊢ B ok    Γ ⊢ P ok    Γ ⊢ S ok
─────────────────────────────────  (AUTH)
Γ ⊢ A auth
```

Implemented as `Authority.authorityVerdict` (`LeanProofs/Admissibility/Authority.lean:64`); the bidirectional form is `authorized_iff_all_green` (line 107).

### BASIS-FAIL, PREC-FAIL, STAND-FAIL — refusal on any dimension

```
Γ ⊢ B fail                Γ ⊢ P fail                Γ ⊢ S fail
─────────── (BASIS-FAIL)   ─────────── (PREC-FAIL)   ─────────── (STAND-FAIL)
Γ ⊢ A deny                Γ ⊢ A deny                Γ ⊢ A deny
```

Implemented respectively as `no_basis_never_authorized` (`Authority.lean:80`), `conflicting_precedence_never_authorized` (line 95) / `incomparable_precedence_never_authorized` (line 90), and `no_standing_never_authorized` (line 100).

### NO-LAUNDER — advisory does not bind

```
Γ ⊢ X advisory-only
─────────────────────────  (NO-LAUNDER)
Γ ⊬ X authorizes mutation
```

An advisory basis short-circuits the verdict algebra to `advisory`, never to `authorized`. Implemented as `advisory_basis_never_authorized` (`Authority.lean:85`).

### REVOKED-NO-EXEC — revoked basis blocks execution

```
Γ ⊢ basisRevoked(K)
──────────────────────────────  (REVOKED-NO-EXEC)
Γ ⊬ AuthorizedStep(step(K))
```

A claim whose basis is revoked cannot be wrapped in an `AuthorizedStep` structure literal. Implemented as `revoked_basis_cannot_be_authorized_step` (`Execution.lean:124`).

### TRAPDOOR-RECEIPT — receipt does not move policy

```
Γ ⊢ apply(recordReceipt, r)
──────────────────────────────────  (TRAPDOOR-RECEIPT)
Γ ⊢ policyStore unchanged
```

Recording evidence into `EvidenceStore` cannot mutate `PolicyStore`. Implemented as `record_receipt_does_not_amend_policy` (`StateTransition.lean:112`). Symmetric trapdoor rules hold for `declarePolicyGap` and `recordRevocation`.

## Composition

The Lean kernel composes via structure literals (`AuthorizedStep`, `DerivationEnv`, `ExecutionEnv`, `RecoveryEnv`) and theorem application. This presentation does *not* introduce composition as a separate rule schema. Readers who need composition should read the Lean source — `Derivation.decideAuthority` (`Derivation.lean:106`) into `Execution.AuthorizedStep` (`Execution.lean:82`) is the canonical chain.

## What is not here

This document does not formalize:

- **Structural rules** (weakening, contraction, exchange).
- **Cut** as a primitive rule or schema. The kernel composes via Lean's type system; no cut-elimination meta-theorem is claimed.
- **Completeness.** The judgments above are exactly those the Lean kernel proves; there is no separate proof system whose completeness with respect to those judgments is asserted.
- **Subformula property, normalization, or admissibility-of-rules theorems** in the Iemhoff sense.
- **Process-calculus structure** (parallel composition, channels, bisimulation, scheduling).
- **Model theory.** No semantics for the judgments are offered beyond their Lean implementations.

This is grammar, not calculus.

## What would be required for a real sequent calculus

Surfaced by DeepSeek's analysis (with corrections); recorded here as future debt, not as a promise to build:

1. **A propositional language.** Atomic propositions for states, claims, evidence, standing; logical connectives; possibly modal operators for `Authorized`, `Fresh`, `Witnessed`. None of this exists today.
2. **Sequents proper**, with a context (`Γ`) on the left and conclusions on the right. The current judgments above embed the context implicitly; a real sequent calculus would name it explicitly and treat it as a syntactic object.
3. **Left and right rules** for each connective and each modal operator. Each kernel theorem would become a rule schema rather than a single proved instance.
4. **Structural rules**, and proofs that they are admissible (weakening, contraction, exchange — or principled non-admissibility, e.g., linear-logic-style resource sensitivity if standing is treated as consumable).
5. **Soundness against the Lean kernel.** Every derivable sequent should correspond to a provable Lean theorem. (Completeness — every Lean theorem corresponds to a derivable sequent — is a stronger claim and would typically be deferred or scoped.)
6. **Cut-elimination** as a meta-theorem. The interesting analogue: *any authorization derivation using an intermediate advisory or limited-standing judgment normalizes into one where the limited-standing artifact never authorizes mutation.* Useful but not trivial.

### Vocabulary correction

DeepSeek's exposition described "unwanted inferences are admissible" as the safety target. **This conflates two senses of "admissible":**

- **Proof-theoretic** *admissible rule*: adding the rule does not change the set of provable theorems. Used for cut, contraction, weakening.
- **Governance-kernel** *admissibility*: the artifact has standing to bind the next transition. Used throughout the Lean kernel.

For authority-laundering or boundary-upgrade rules, the safety claim should be that they are **not derivable** (or that any derivation attempting them blocks / normalizes to a non-authorizing form). It should *not* be that they are admissible in the proof-theoretic sense. Confusing the two is exactly the false-friend trap the scope-fence is designed to prevent; any future sequent-calculus work must be explicit about which sense is meant on each page.

## Pressures for expansion or promotion

Formal development does not require a downstream consumer: a precise normalization,
soundness, non-derivability, or countermodel question may lead later tooling. The
pressures below help choose between keeping the present judgmental notation, building a
real sequent calculus, or moving to operational semantics; public promotion remains a
separate decision.

If one of the following appears, the judgmental presentation may need to be promoted toward (or replaced by) something stronger:

- **Composition pressure** — a downstream consumer needs to compose admissibility judgments across NQ / Wicket / Governor / Standing with a shared formal grammar, or a formal composition theorem independently exposes that need.
- **Normalization pressure** — a need to prove that laundering paths can be reduced away or exposed structurally.
- **Protocol pressure** — concurrent/revoked/stale receipts across agents and services require operational semantics or transition-system reasoning.
- **Equivalence pressure** — two governance protocols need to be shown observationally equivalent with respect to admissible mutation.

The first two motivate moving toward a real sequent calculus. The latter two motivate operational semantics or (eventually) a process calculus, both of which are explicitly deferred.

## Cross-references

- Lean modules (1.0 public surface): `LeanProofs/Admissibility/{Authority, StateTransition, Derivation, Execution, Corrective, Freshness, SurfaceAuthorization, WitnessInvariance}.lean`
- Aggregator: `LeanProofs/Admissibility/CalculusOne.lean`
- Specimens: `LeanProofs/Admissibility/Examples.lean`
- Narrative walkthrough: `lean/docs/worked-examples/standing-upgrade-block.md`
- DOI (concept): `10.5281/zenodo.20369489`
- DOI (v1.0.1): `10.5281/zenodo.20369490`
- Related working note: [[truce-doctrine]]
