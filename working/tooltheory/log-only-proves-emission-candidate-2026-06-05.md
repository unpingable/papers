# Log-Only-Proves-Emission — candidate kernel

**Filed:** 2026-06-05. **Status:** scratch-checked 2026-06-06 as a bounded tactic / custody probe (smaller-altitude than a type-design probe). **Lean source at `~/git/lean/LeanProofs/Scratch/LogOnlyProvesEmission.lean`** (~127 lines including category-2 prelude with the four bounded probe questions recorded). Not imported by `LeanProofs.lean`; not part of any 1.0 surface. Direct `lake env lean` check clean on first elaboration; only output is a non-fatal linter style suggestion (`simp at` vs `simpa using`). Side-quest yield #4 per the 2026-06-04 NoLift / laundering-detector exchange.

**Lean custody:** `extracted-to: ~/git/lean/LeanProofs/Scratch/LogOnlyProvesEmission.lean` (scratch-checked, tactic-probe). Markdown Lean block below is the explanatory mirror of the authoritative scratch source. See [`lean-custody-ledger-2026-06-06.md`](lean-custody-ledger-2026-06-06.md) § Checked Scratch.

## Claim

> **A log entry proves emission, not truth, authorization, causality, completeness, or fairness.**

## Why candidate, and what the Scratch build settled

The 2026-06-04 kernel-overlap audit on the multi-model NoLift / laundering-detector exchange found that nearly every candidate kernel ChatGPT/DeepSeek enumerated has an existing corpus artifact — see `admissibility-related-work-map.md` § kernel-overlap audit (in the audit-output paragraph attached to the side-quest discussion) and cross-check against `LeanProofs.lean`'s current import surface. Log-epistemology was the single exception: no existing module proves what a log entry *cannot* support.

## Family classification

Per [`anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md): would land in the **witness identity / provenance** row, sharpening it from "sample exists ⇒ trustworthy / provenanced witness" to "system emitted statement ⇒ truth / authorization / causality / completeness / fairness." The master frame applies: a log entry is a witness to emission; converting it into a witness for truth (or any of the four other targets) requires a conversion witness that the log itself cannot supply.

## Runtime correspondence targets

The Scratch formalization already exists; no downstream consumer was required to authorize it. Possible correspondence and later implementation targets include:

- NQ receipt substrate needing log-vs-testimony separation at a layer the existing `WitnessInvariance.lean` doesn't address.
- An external pitch needing one concrete artifact at the audit-log layer (SIEM dashboards, observability claims, "the logs prove X" framing).
- A Labelwatch / driftwatch artifact requiring "log entry says X, but does not witness Y."
- Any reviewer surfacing the gap.

These targets may supply mapping and conformance evidence. They do not control whether the formal proposition may be stated. The file remains Scratch because custody and public-surface promotion have not been granted.

## Source sketch shape (extracted; Scratch file is authoritative)

Inductive `LogClaim` with one True constructor (`emitted system statement time`) and five False constructors (`truthOf` / `authorizationOf` / `causalityOf` / `completenessOf` / `fairnessOf`). The `inferable` predicate returns True only for `emitted`; for the other five, unconditionally False. Core theorem: for any log entry and any claim, if the claim is inferable from the entry, the claim is an `emitted` constructor with matching fields. Stronger: even collections of log entries don't lift to truth (`multiple_logs_still_do_not_prove_truth`).

The Markdown block records the source shape. The checked Scratch file is authoritative and has already been reviewed against the existing `WitnessInvariance` / `RefusalPropagation` neighborhood. Any later promotion still requires a fresh overlap and custody review.

## Non-claims

- **Not the authoritative Lean source.** The Markdown sketch is an explanatory mirror; the checked Scratch file owns the formal details.
- **Not automatic promotion.** Scratch formalization is not an import, public-surface, doctrine, or conformance receipt.
- **Not a position** on whether this should ever join the imported Lean surface. The custody state stays explicit.
- **Not part of any `NoLift/` parallel directory.** The 2026-06-04 audit explicitly refused a parallel module surface as cathedral-by-rename; if this kernel is ever built, it joins `LeanProofs/Admissibility/` under its existing namespace, not under a new roof.

## Cross-references

- [`admissibility-related-work-map.md`](admissibility-related-work-map.md) § Priority 0 readings + kernel-overlap audit (the audit that surfaced this gap)
- [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) § The master frame (where this kernel would slot under the witness-identity/provenance row)
- [[documentation-keepers]] *"Lean as laundering detector"* keeper phrase
- `~/git/lean/LeanProofs.lean` — current import surface; verify gap before any build

## Lean sketch (candidate shape; hand-reviewed for compile-readiness 2026-06-05, NOT in any import surface)

```lean
namespace Admissibility

/-!
Candidate: LogOnlyProvesEmission

Doctrine:
A log entry proves emission, not truth, authorization, causality,
completeness, or fairness.

Atomic epistemology kernel. Layer tag: NoLift.
-/

structure LogEntry where
  system : String
  statement : String
  timestamp : Nat
deriving Repr

inductive LogClaim where
  | emitted (system : String) (statement : String) (timestamp : Nat)
  | truthOf (statement : String)
  | authorizationOf (actor : String) (action : String)
  | causalityOf (cause : String) (effect : String)
  | completenessOf (domain : String)
  | fairnessOf (process : String)
deriving DecidableEq, Repr

def inferableFromLog (entry : LogEntry) : LogClaim → Prop
  | .emitted sys stmt ts =>
      entry.system = sys ∧ entry.statement = stmt ∧ entry.timestamp = ts
  | .truthOf _ => False
  | .authorizationOf _ _ => False
  | .causalityOf _ _ => False
  | .completenessOf _ => False
  | .fairnessOf _ => False

theorem log_does_not_discharge_truth
  (entry : LogEntry) (stmt : String) :
  ¬ inferableFromLog entry (.truthOf stmt) := by
  simp [inferableFromLog]

theorem log_does_not_discharge_authorization
  (entry : LogEntry) (actor action : String) :
  ¬ inferableFromLog entry (.authorizationOf actor action) := by
  simp [inferableFromLog]

def inferableFromManyLogs
  (entries : List LogEntry) (claim : LogClaim) : Prop :=
  ∃ entry, entry ∈ entries ∧ inferableFromLog entry claim

theorem many_logs_still_do_not_discharge_truth
  (entries : List LogEntry) (stmt : String) :
  ¬ inferableFromManyLogs entries (.truthOf stmt) := by
  intro h
  rcases h with ⟨entry, _, hInfer⟩
  simpa [inferableFromLog] using hInfer

end Admissibility
```

**Phrasing note (load-bearing).** Theorem names use *"does not discharge"* (audit-unit form) rather than *"≠"* (equation-negation form). Per the doctrine map's audit-unit framing: *X ≠ Y* is a type joke; *X cannot discharge P without witness W* is a type accusation. The `LogClaim` inductive carries the predicates; `inferableFromLog` returns `False` for five of six constructors. The corpus does NOT prove that no truth witness exists anywhere — only that *this log entry does not discharge the truth predicate*. Produce the witness; the kernel will accept it under a different constructor.

## Provenance

Surfaced in multi-model exchange 2026-06-04 (ChatGPT extending the Lean-underexposed-lane idea → DeepSeek sketching 12 candidate kernels with code → ChatGPT hand-reviewing for errors and naming the master abstraction (typed conversion witness) → DeepSeek refining → ChatGPT correcting the destination-only-witness trap → Claude Code kernel-overlap audit confirming 11 of 12 candidates already covered, one gap remaining). Lean sketch attached 2026-06-05 in the field-guide-and-Lean-handoff round and extracted to checked Scratch on 2026-06-06. The original closing-ledger phrase *"named, unbuilt, awaiting consumer"* is historical and superseded: the formalization exists; runtime correspondence and public promotion remain separate.
