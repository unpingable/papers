# Attack #05 — Effect partial order vs. Bridge obligation-set inclusion

**Filed:** 2026-06-05. **Status:** vector-mining pilot output. **Vector ID:** attack-05. **Confidence:** high.

## Question

> Is the relay's "effect-indexed admissibility" partial order (Slice 1: `Effect : Type` with `[PartialOrder Effect]`, `Discharges : Artifact → Claim → Effect → Prop`, `MayUse a c requested discharged := Discharges a c discharged ∧ requested ≤ discharged`, `no_silent_escalation`) reducible to bridge-obligation-set inclusion already in the corpus?

## Sources audited

- `working/bridge-obligation-lattice.md` (2026-06-06): five obligation atoms, bridge families as points in obligation-space, NoSilentConversion gate, explicit kernel-to-obligation mapping table.
- `working/no-unifier-without-laundering.md` (2026-06-04): federation doctrine, bridge-admission decision rule, modal/dependent false-rescue closure (3-outcome partition).
- Relay claim source: this conversation, Slice 1 of the multi-agent effect-indexed admissibility proposal.

## Structural comparison

| Relay claim | Corpus structure | Verdict |
|---|---|---|
| `Effect : Type` (abstract) | Bridge family = subset of 5 obligation atoms | ALIAS-RISK: same role, different vocabulary |
| `[PartialOrder Effect]` (abstract) | Obligation-set inclusion (concrete, 5 named atoms) | DUPLICATE on shape; relay's lattice is abstract over the same shape |
| `Discharges a c F` | Bridge-admission decision rule (5-element tax) | ALIAS-RISK: relay collapses 5-element tax to single predicate |
| `MayUse := Discharges ∧ requested ≤ discharged` | Specialization admissibility = child obligation set ⊆ parent obligation set | DUPLICATE |
| `no_silent_escalation` theorem | NoSilentConversion gate (worked 2026-06-06, caught 3 of 5 reductions) | DUPLICATE; relay's theorem is the existing gate at a different altitude |
| Refusal as Effect / NoBurdenLaundering | `[[project-refusals-need-receipts]]`, Mandamus, liveness wing | DUPLICATE |
| BoundaryIntegrity / provenance preservation | `type-fidelity` atom + freshness atom + custody discipline | NEAR-DUPLICATE; relay sharpens the provenance-loss case but adds no new atom |
| Feedback quarantine / NoSelfValidatingLoop | freshness atom + `[[feedback-verdict-compression]]` freshness-window-on-relay-traffic | NEAR-DUPLICATE |
| Sacrifice-class floor / empty discharge region | Existing kernels' negative results (`no_basis_never_authorized` etc.) + `[[feedback-failed-factoring-as-honest-boundary]]` | DUPLICATE on structure; relay re-skins existing impossibility theorems as a single lattice region |
| ExceptionDebt / non-self-discharge | Exception family obligation set {temporal-bounding, anti-precedent} + receipt/standing kernels | NEAR-DUPLICATE; the "actor who acted cannot certify" separation is implicit in anti-precedent but not separately named — see Survivor 2 below |

## Verdict

**Three classifications fire, in this order:**

1. **DUPLICATE on shape.** The relay's effect-partial-order is bridge-obligation-set inclusion at a higher abstraction. The relay leaves `Effect` and `≤` opaque; the corpus instantiates them concretely as a 5-atom obligation set with subset-inclusion. Same lattice. The relay's NoSilentEscalation is the corpus's NoSilentConversion gate. The relay's theorem statement is the corpus's "a specialization is admissible only if it inherits the parent's obligations without needing a new preservation invariant" — *which was filed 2026-06-06, the day before this relay surfaced.*

2. **ALIAS-RISK on vocabulary.** The relay names: Effect / Discharge / MayUse / BoundaryIntegrity / RefusalEffect / ExceptionDebt / NoSelfValidatingLoop. The corpus names: bridge family / bridge admissibility / specialization admissibility / type-fidelity + freshness / refusals-need-receipts / Exception obligation set / freshness-window-on-relays. Five distinct relational vocabularies the [[project-no-unifier-without-laundering]] doctrine names as the *fracture* — not as something a single typed lattice unifies.

3. **LAUNDERING per the federation doctrine.** The relay proposes a *single* `Effect : Type` as the universal target of discharge across all kernels, with a single partial order and a single MayUse predicate. This is Outcome 2 (laundering) or Outcome 3 (unlicensed bridge structure) from `working/no-unifier-without-laundering.md` § Modal/dependent false rescue:

   > It erases those surfaces into a common judgment form. → **Laundering: forbidden.**
   > It permits cross-kernel implication without an explicit bridge theorem. → **Unlicensed bridge structure: forbidden.**

   The five relational vocabularies are erased into a single ordered type; the bridge tax (source surface / target surface / witness / licensed claim / residual scope) is not paid; the deliverable is a Lean module + paper, not a laundering receipt. Per the audit-vs-rescue distinction: **rescue, not audit.**

## Gate-firing trace

The pilot scope's gate (any BRIDGE-CANDIDATE must be auditable against [[project-paper-naming-stack]], [[project-bridge-obligation-lattice]], [[project-no-unifier-without-laundering]]) fired correctly. The relay's effect-partial-order does not survive classification as BRIDGE-CANDIDATE because:

- It does not bridge two named kernels (it proposes a universal type *over* them).
- It would erase the five relational vocabularies named in [[project-no-unifier-without-laundering]] § The relational-vocabulary fracture.
- It elevates "calculus" past the kernel surface — direct collision with the load-bearing naming-discipline line: *"Admissibility Kernels is the artifact name. Calculus is the deeper pattern... like mold in a Pittsburgh basement."*

Reclassification: BRIDGE-CANDIDATE → LAUNDERING-RECEIPT-SHAPED (with the receipt being this very note).

## Survivors

Two fragments survive review at prose altitude. Neither requires Lean. Neither requires a paper.

**Survivor 1: "Presentation may compress; authority carriers may not."** Not present in the corpus as a single sentence. Captures the type-fidelity atom's downstream consequence for UI/dashboard/summary layers. Candidate for `[[documentation-keepers]]` if it survives a slogan-blast-radius check; the corpus already has *"A fog machine is a bridge with the empty obligation set"* which is adjacent. May be duplicate at the keeper level — separate audit pass required, not done here.

**Survivor 2: separation-of-custody on exception discharge.** The relay's "actor who took the exceptional action cannot certify its discharge" is structurally implicit in the Exception family's `{temporal-bounding, anti-precedent}` obligation set + the receipt/standing kernel pattern, but is not separately named. Candidate sharpening of anti-precedent: *anti-precedent + separation-of-custody* may be two atoms or one with two faces. **Not authorized to file as new atom.** Filed here as a question for a future kernel-overlap audit when an Exception specimen forces the distinction.

## Lean polarity catch

The Slice 1 Lean draft had `¬(d.effect ≤ f')` where it should have `¬(f' ≤ d.effect)` (Claude-web caught it correctly mid-relay). This is an artifact-level correction to a Lean draft of the relay's claim. Since the relay's claim is itself DUPLICATE+LAUNDERING, the polarity catch does not survive into the corpus — there's no Lean target to apply it to. Recorded here for completeness; no action.

## Method validation

The vector-mining pilot earns its keep on attack-05. Specifically:

- **Output polarity is REFUSAL-shaped.** Three classifications fired (DUPLICATE / ALIAS-RISK / LAUNDERING); zero classifications fired in the "new theorem worth writing" direction.
- **Gate held.** The BRIDGE-CANDIDATE reclassification gate ([[project-no-unifier-without-laundering]] check) fired before any candidate could be promoted.
- **Bounded cost.** Two memory entries + two working notes + one comparison table + one verdict. ~10 minutes of file reads, not 30.
- **Auditable trace.** Every verdict cell cites a specific corpus location. No "I sense convergence" language.
- **Common-mode immunity confirmed.** The relay was Claude-web-shaped; the corpus check rejected it. The previous turn's refusal was not overfit — it was reading the same gate this audit reads.

**Method status:** ratified for next pilot. Recommended next attack: **#2 (BoundaryTransit × feedback quarantine)** — narrowest scope, tests whether the corpus's existing freshness/type-fidelity atoms already imply the feedback-loop quarantine claim, or whether a real provenance-preservation gap exists.

## Recommended next action

- **Do not** mint `LeanProofs/Scratch/EffectIndexedAdmissibility.lean`.
- **Do not** draft "No Silent Conversion: Effect-Indexed Admissibility" as a paper.
- **Do not** add Effect-as-PartialOrder to the corpus.
- **Do** file this note as a specimen under [[project-laundering-move-watchlist]] — a documented multi-agent relay-shape attack on a closed synthesis, caught by the vector-mining gate on its first run.
- **Do** consider whether Survivor 1 ("presentation may compress; authority carriers may not") earns keeper status — separate slogan-blast-radius audit.
- **Do** carry Survivor 2 (separation-of-custody on exception discharge) as a question for the next Exception specimen, NOT as a new atom.

## Cross-references

- [[project-bridge-obligation-lattice]] — the doctrine this audit reads against.
- [[project-no-unifier-without-laundering]] — the federation doctrine the relay would violate.
- [[project-calculus-vocabulary-retired]] — the 2026-06-03 retirement the relay would reverse.
- [[project-paper-naming-stack]] — the synthesis closure the relay would reopen.
- [[feedback-claude-common-mode-synthesis]] — the methodology check that flagged the relay shape.
- [[feedback-verdict-compression]] — the freshness-on-relays principle this audit instantiates.
- [[feedback-kernel-overlap-audit]] — the failure mode this audit caught: fresh chat re-derives existing kernel under new vocabulary.

## Provenance

Pilot run 2026-06-05 of the corpus-archaeology vector-mining method proposed earlier in this conversation. Attack #5 selected as smallest test of method polarity. Result: method polarity confirmed (refusal-biased), gate held, no laundering escaped.
