# "Receipt" and "Witness" — distinct senses in the corpus

**Filed:** 2026-06-05. **Status:** vocabulary disambiguation note. **NOT a primitive.** **NOT doctrine.** Records the receipt/witness role boundary and the multiple senses each word carries.

## Why this note exists

Surfaced 2026-06-05 in [`../vector-mining/2026-06-05-batch-six-attacks.md`](../vector-mining/2026-06-05-batch-six-attacks.md) attack #3 (cumulative pilot #6 of the vector-mining method). Sibling to [`standing-three-senses.md`](standing-three-senses.md) and [`custody-five-senses.md`](custody-five-senses.md).

The receipt/witness boundary is structurally maintained where it matters — a witness *supports* an admissibility claim; a receipt *records* an act — but the words alias enough across registers that single-altitude review can confuse them.

## The genus boundary

> *A witness supports an admissibility claim.*
> *A receipt records an act.*

Two corpus-anchored sentences carry this boundary:

- **`ReceiptIsNotAuthority`** (static refusal kernel, [`../bridge-obligation-lattice.md`](../bridge-obligation-lattice.md)): the receipt of a transaction does not authorize the transaction.
- **"Label is not witness."** ([`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) § 7 guardrail): a field labeled `surface: prod` is testimony until the authenticity mechanism binds it.

When in doubt, run the relay claim against these two sentences and check whether the proposed object is being asked to *support* (witness shape) or *record* (receipt shape).

## Three senses of "receipt"

### (a) Submission record

**Where:** `~/git/lean/LeanProofs/Admissibility/Mandamus.lean`'s `Receipt` structure with `submittedAt : Nat`; `Matter.receipt`.

**What it names:** A timestamped artifact representing the claimant's submission. Used in matter-clock computations and horizon checks. Strictly an input-side artifact, authored by the claimant.

### (b) Verdict artifact

**Where:** [[project-refusals-need-receipts]] dual-list; refusal-receipt / reasoned-decision receipt as `Obligation DutyKind.discretionary` values in Mandamus.lean; `Violation` producing `EvidentiaryRecord`.

**What it names:** An artifact recording the institution's verdict on a matter — refusal, reasoned decision, exception debt, violation. The output side of the discharge, authored by the adjudicator. *"Refusal is an accountable act"* lives here.

### (c) Non-authorizing acknowledgment

**Where:** `ReceiptIsNotAuthority` static refusal kernel (bridge-obligation-lattice § "What this doctrine says about existing kernels").

**What it names:** The mere fact of having received something does not constitute authorization to act on it. Receipt-as-event, not receipt-as-license. The doctrinal refusal kernel that says: *the receipt is not the writ.*

## Three senses of "witness"

### (a) Lean proof object

**Where:** `~/git/lean/LeanProofs/Admissibility/BoundaryWitness.lean`'s `ForgetfulWitness`, `CouplingWitness`, `BridgeWitness`; dependent-type inhabitants throughout the Lean kernels.

**What it names:** A term whose existence proves a proposition in the Lean type theory. The substrate of formal admissibility claims inside the Lean repo.

### (b) Substrate carrier

**Where:** [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) § Non-claim.

**What it names:** Signed JSON, receipt rows, ledger entries, NQ testimony packets, WLP claims — production-level artifacts that carry admissibility evidence across boundaries. Distinct from sense (a): the substrate witness is the wire-format artifact that must satisfy the binding obligations; the Lean witness is the proof. The non-claim sentence is load-bearing: *"This sketch defines candidate production-witness carrier requirements; it does not establish correspondence between carrier validity and the Lean witness model."*

### (c) Testimonial admissibility object

**Where:** refusals-need-receipts; Mandamus's `EvidentiaryRecord`; [`../loop-capture.md`](../loop-capture.md)'s *"a witness need not be pure; it must fail differently."*

**What it names:** An artifact admissible as testimony about a fact. The testimonial sense is closest to the legal/evidentiary register; it carries the "fail differently" / non-co-captured requirement when used in adversarial settings. Composes with [[project-heterogeneous-turtles-not-witnesses]]: heterogeneity reduces correlation but does not change receipt type.

## Cross-word observations

- **Receipt (b) and witness (c) are nearest siblings:** the verdict-artifact records what the institution decided; the testimonial-admissibility object records what a witness reports. Both are *records of something*. The distinction is who authored: institution (b) vs witness (c).
- **Receipt (a) and witness (b) are distant cousins:** both are concrete artifacts at the substrate level, but the submission-record is one-shot (a single claimant submission) and the substrate-witness may be persistent, composable, or chained.
- **Receipt (c) and witness (a) are doctrinally orthogonal:** the non-authorizing-acknowledgment is a refusal kernel at the doctrine altitude; the Lean proof is a formal object at the substrate altitude. They live at incompatible altitudes; a claim that confuses them is altitude-conflated.

## Transversal meta-axis: production-mechanism type

Beyond the role classifications above, the corpus carries a **transversal meta-axis** for receipt evidence: *production-mechanism type*. From [`../heterogeneous-turtles-not-witnesses.md`](../heterogeneous-turtles-not-witnesses.md): receipts are classified by *what mechanism produced them* — model assessment vs compiler output vs sensor reading vs ledger entry vs signed external API response vs human observation with accountable standing vs reproducible experiment vs policy engine with typed authority input.

This is **not a fourth role sense.** It is an *orthogonal classification* that runs across the three role senses. A submission record (a) and a verdict artifact (b) can each carry any production-mechanism type. The heterogeneous-turtles doctrine uses this axis to refuse: even maximally heterogeneous channels that all share the same production-mechanism type (e.g., N model verifiers all producing `assessment`) cannot discharge witness-type predicates. Discharge requires a receipt of a *different* production-mechanism type, not just more channels of the same type.

Composes with the same-custody axis from [`../admissibility-vs-arms-control.md`](../admissibility-vs-arms-control.md): a witness must clear **both** axes — independent custody AND different production-mechanism type — to discharge. Either failure refuses. The two axes are orthogonal; neither subsumes the other.

## The key non-rule

The receipt/witness boundary is *role*, not *substrate*. A signed JSON can be either; a Lean term can be either; an `EvidentiaryRecord` can be either. The question is what work the artifact is doing in the discharge graph: supporting (witness role) or recording (receipt role). Some artifacts are both, in which case both roles must be discharged separately.

## What this note is NOT

- **NOT a new primitive.** No new atom, kernel, or class.
- **NOT doctrine.** Glossary entry only.
- **NOT a Lean module.** No Lean target.
- **NOT authorization** to mint `ReceiptWitness`, `WitnessReceipt`, or any cross-word type.

## Cross-references

- [`standing-three-senses.md`](standing-three-senses.md), [`custody-five-senses.md`](custody-five-senses.md) — sibling disambiguation notes.
- [`../bridge-obligation-lattice.md`](../bridge-obligation-lattice.md) — `ReceiptIsNotAuthority` static refusal kernel; the receipt-as-non-authorization sense.
- [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) — substrate-carrier sense of witness; the "label is not witness" guardrail.
- `~/git/lean/LeanProofs/Admissibility/Mandamus.lean` — submission-record and verdict-artifact senses of receipt.
- `~/git/lean/LeanProofs/Admissibility/BoundaryWitness.lean` — Lean proof-object sense of witness.
- [[project-refusals-need-receipts]] — verdict-artifact (receipt) and testimonial (witness) senses; "refusal is an accountable act."
- [`../loop-capture.md`](../loop-capture.md) — testimonial sense via *"a witness need not be pure; it must fail differently."*
- [[project-heterogeneous-turtles-not-witnesses]] — companion: heterogeneity does not change receipt type.
- [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) — federation discipline; why role-distinction must not collapse.
- [`../vector-mining/2026-06-05-batch-six-attacks.md`](../vector-mining/2026-06-05-batch-six-attacks.md) — attack #3 audit.
