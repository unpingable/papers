# Log-Only-Proves-Emission — candidate kernel

**Filed:** 2026-06-05. **Status:** named, unbuilt, awaiting consumer. Side-quest yield #4 per the 2026-06-04 NoLift / laundering-detector exchange.

## Claim

> **A log entry proves emission, not truth, authorization, causality, completeness, or fairness.**

## Why candidate, not built

The 2026-06-04 kernel-overlap audit on the multi-model NoLift / laundering-detector exchange found that nearly every candidate kernel ChatGPT/DeepSeek enumerated has an existing corpus artifact — see `admissibility-related-work-map.md` § kernel-overlap audit (in the audit-output paragraph attached to the side-quest discussion) and cross-check against `LeanProofs.lean`'s current import surface. Log-epistemology was the single exception: no existing module proves what a log entry *cannot* support.

## Family classification

Per [`anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md): would land in the **witness identity / provenance** row, sharpening it from "sample exists ⇒ trustworthy / provenanced witness" to "system emitted statement ⇒ truth / authorization / causality / completeness / fairness." The master frame applies: a log entry is a witness to emission; converting it into a witness for truth (or any of the four other targets) requires a conversion witness that the log itself cannot supply.

## Forcing case (absent)

No downstream consumer currently needs this. Build trigger would be one of:

- NQ receipt substrate needing log-vs-testimony separation at a layer the existing `WitnessInvariance.lean` doesn't address.
- An external pitch needing one concrete artifact at the audit-log layer (SIEM dashboards, observability claims, "the logs prove X" framing).
- A Labelwatch / driftwatch artifact requiring "log entry says X, but does not witness Y."
- Any reviewer surfacing the gap.

Until one of these fires, the kernel stays named-not-built per name-early discipline.

## Sketch shape (NOT a build spec — name-early only)

Inductive `LogClaim` with one True constructor (`emitted system statement time`) and five False constructors (`truthOf` / `authorizationOf` / `causalityOf` / `completenessOf` / `fairnessOf`). The `inferable` predicate returns True only for `emitted`; for the other five, unconditionally False. Core theorem: for any log entry and any claim, if the claim is inferable from the entry, the claim is an `emitted` constructor with matching fields. Stronger: even collections of log entries don't lift to truth (`multiple_logs_still_do_not_prove_truth`).

The sketch above is candidate shape only. The actual build, if it happens, will be reviewed against the existing `WitnessInvariance` / `RefusalPropagation` modules to avoid duplicating coverage already in place.

## Non-claims

- **Not a build spec.** The sketch is candidate shape; the actual module would be designed against the corpus's existing kernel conventions.
- **Not authorization to build.** Name-early per [[feedback-name-early]]; build only on forcing case.
- **Not a position** on whether this should ever join the Lean tree. Placeholder so the gap is traceable.
- **Not part of any `NoLift/` parallel directory.** The 2026-06-04 audit explicitly refused a parallel module surface as cathedral-by-rename; if this kernel is ever built, it joins `LeanProofs/Admissibility/` under its existing namespace, not under a new roof.

## Cross-references

- [`admissibility-related-work-map.md`](admissibility-related-work-map.md) § Priority 0 readings + kernel-overlap audit (the audit that surfaced this gap)
- [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) § The master frame (where this kernel would slot under the witness-identity/provenance row)
- [[documentation-keepers]] *"Lean as laundering detector"* keeper phrase
- `~/git/lean/LeanProofs.lean` — current import surface; verify gap before any build

## Provenance

Surfaced in multi-model exchange 2026-06-04 (ChatGPT extending the Lean-underexposed-lane idea → DeepSeek sketching 12 candidate kernels with code → ChatGPT hand-reviewing for errors and naming the master abstraction (typed conversion witness) → DeepSeek refining → ChatGPT correcting the destination-only-witness trap → Claude Code kernel-overlap audit confirming 11 of 12 candidates already covered, one gap remaining). Side-quest yield #4 per the 2026-06-05 closing ledger: *named, unbuilt, awaiting consumer.*
