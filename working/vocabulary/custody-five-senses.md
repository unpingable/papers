# "Custody" — five senses in the corpus

**Filed:** 2026-06-05. **Status:** vocabulary disambiguation note. **NOT a primitive.** **NOT doctrine.** Records the highest-cardinality lexical fracture surfaced by the vector-mining pilots: the word "custody" carries at least five distinct relations across the corpus.

## Why this note exists

Same reason as [`standing-three-senses.md`](standing-three-senses.md): silent collapse across senses produces fake primitives. The relay-shape attack on "custody = preserve provenance metadata" would erase the per-sense semantics into a single binding obligation. The corpus separates the senses on purpose; this note records which sense lives where so future cross-cutting work does not relitigate from confusion.

Surfaced 2026-06-05 in [`../vector-mining/2026-06-05-batch-six-attacks.md`](../vector-mining/2026-06-05-batch-six-attacks.md) attack #4-batch (cumulative pilot #7 of the vector-mining method).

## The five senses

### 1. Custody-as-file-role

**Where it lives:** [`../custody-classes.md`](../custody-classes.md).

**What it names:** The role a `.lean` file plays in the institutional discharge of the admissibility corpus: PUBLIC-SHIPPED / ANNEX / SCRATCH / UNRATIFIED-CANDIDATE / DEPRECATED. Marker convention: `Custody-Class:` (grep target) + `Custody:` prose paragraph (explanatory receipt).

**What touches it:** the per-file marker convention; the regression checker `~/git/lean/scripts/check-custody-classes.sh`; the AdmissibilityKernels aggregator's ANNEX enumeration. Repo-level discipline only.

### 2. Custody-as-ratification-discipline

**Where it lives:** `~/.claude/CLAUDE.md` § Register discipline; [[project-lean-custody-state]] § Option C.

**What it names:** Whether a change is *custody-affecting* — i.e., touches canonical definitions, kernels, receipt formats, ratification rules, release/signing/CI gates, or public claims tied to canonical artifacts. Custody-affecting changes require explicit ratification language; routine implementation does not.

**What touches it:** the register-discipline rule; the Option C policy in [[project-lean-custody-state]]; the classify-before-escalating rubric from CLAUDE.md. Governance-level discipline, distinct from file-role.

### 3. Custody-as-independent-channel

**Where it lives:** [`../loop-capture.md`](../loop-capture.md) § Witness/defense concepts; [[project-refusals-need-receipts]] dual-list.

**What it names:** A channel — sensor, detector, witness, attestor — that is not co-captured by the transformation being evaluated. The Witness Necessity Claim: *"A loop whose detectors consume only captured reports cannot reliably detect capture. Detection requires at least one channel not co-captured by the same transformation."*

**What touches it:** loop-capture's five capture surfaces; WIF-composition's audited failure-surface orthogonality; the no-self-validating-loop rule. Adversarial-mechanism discipline.

### 4. Custody-as-substrate-binding

**Where it lives:** [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) § 3 Binding obligations.

**What it names:** The joint signature/authority coverage over `(identity, time, authority, substrate)` that a production-witness carrier owes to refuse the seven refusal cases (self-mint / replay / wrong-surface / stale / widened / post-hoc / wrong-attempt). *"Identity + time + authority must be jointly covered by substrate. None of the three can be detached, restated, or replayed independently."*

**What touches it:** the witness carrier model's binding obligations; SPKI / Biscuit / macaroons / token-binding substrate neighbors; the `MayMint` predicate shape. Cryptographic-carrier discipline.

### 5. Custody-as-refusal-independence

**Where it lives:** [[project-refusals-need-receipts]] (dual-list refusals); `~/git/lean/LeanProofs/Admissibility/Mandamus.lean` (sprint #2 deferred theorem `appellate_independence_via_same_custody_refusal`).

**What it names:** Whether an appellate or review action is genuinely independent of the original adjudicator. *"Same-custody appeal is not independent review."* The institutional-process version of sense 3 (independent channel), applied to refusals.

**What touches it:** the refusals-need-receipts dual-list; the deferred sprint-#2 theorem in Mandamus.lean; admin-law independence doctrine. Institutional-process discipline.

## Cross-sense observations

- **Senses 3 and 5 are structurally siblings:** non-co-captured channel (loop capture) and non-same-custody appeal (mandamus). Both are *independence requirements* at different altitudes — adversarial-mechanism vs institutional-process.
- **Senses 2 and 4 are structurally siblings:** ratification-discipline (which changes need explicit authority) and substrate-binding (which fields need joint signature coverage). Both are *binding-obligation requirements* at different altitudes — repo-governance vs cryptographic-carrier.
- **Sense 1 stands alone:** custody-as-file-role is repo discipline for the corpus's own artifacts; it does not directly map onto any of the other four. It is the institutional-discharge classification for the corpus's own .lean files, not a property of authority-bearing claims downstream.

The collapse the relay-shape attack would have performed: senses 3 + 4 (independent-channel + substrate-binding) into a single "BoundaryIntegrity / provenance preservation" primitive. The corpus refuses this collapse because the underlying disciplines run on different topologies (adversarial loop-graph vs cryptographic signature-coverage).

## The key non-rule

There is no "custody" primitive in the corpus. Each sense lives at its own altitude with its own discipline. A future cross-sense theorem (e.g., *senses 3 and 5 are dual at different scales*) would owe the bridge tax from [[project-no-unifier-without-laundering]] — five-element receipt naming source surface, target surface, witness, licensed claim, and residual scope. None is currently on offer.

## What this note is NOT

- **NOT a new primitive.** No new atom, kernel, or class.
- **NOT doctrine.** Glossary entry only.
- **NOT a Lean module.** No Lean target.
- **NOT authorization** to mint `Custody`, `CustodyDiscipline`, `BoundaryIntegrity`, or any cross-sense type.
- **NOT exhaustive.** Five senses are surfaced as of 2026-06-05; a sixth may surface in future work and would be added by the same process.

## Cross-references

- [`../custody-classes.md`](../custody-classes.md) — sense 1 (file role).
- [[project-lean-custody-state]] — sense 2 (ratification discipline); `~/.claude/CLAUDE.md` § Register discipline.
- [`../loop-capture.md`](../loop-capture.md) — sense 3 (independent channel).
- [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) — sense 4 (substrate binding).
- [[project-refusals-need-receipts]] — senses 3 and 5 (independent channel; refusal independence).
- [`standing-three-senses.md`](standing-three-senses.md) — sibling disambiguation note; three senses of "standing."
- [`receipt-and-witness-senses.md`](receipt-and-witness-senses.md) — sibling disambiguation note; three senses each of "receipt" and "witness."
- [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) — federation discipline; why senses must not collapse.
- [`../vector-mining/2026-06-05-batch-six-attacks.md`](../vector-mining/2026-06-05-batch-six-attacks.md) — attack #4-batch audit that surfaced the fracture.
