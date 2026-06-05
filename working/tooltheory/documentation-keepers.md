# Documentation Keepers — Fossil-Bed Pass

**Filed:** 2026-05-20 (separated from parked-leads register as a different artifact type).
**Shape:** documentation-legibility holding area, not a deferred-build register.
**Status:** TODO list for an external-reader-legibility pass on existing tool documentation (NQ, authority docs, related working notes).

## What this is

Keeper sentences that already capture existing doctrine but are sharper than what currently lives in the canonical docs. Filing them here keeps them visible until a documentation-housekeeping pass places them in their canonical homes.

**This is not new doctrine.** Every keeper here points to a load-bearing claim that already exists in code, working notes, or kernel modules. The work is *legibility*, not *invention*.

**This is not a deferred-build register.** A keeper that doesn't get placed during the next docs pass loses nothing structural; the underlying claim is already in place. The keepers exist to lower the cold-reader cost of entering the tool docs.

## Distinguishing from parked-leads

| Parked-leads | Documentation keepers |
| --- | --- |
| Deferred build candidates | Sentence-level filing work |
| Reopen triggers gate construction | Placement triggers gate documentation passes |
| Custody state: *preserved, non-binding, reopenable* | Custody state: *waiting for the next docs pass* |
| Lives at *handle* stage in gate stack | Doesn't live in the gate stack at all — it's downstream of already-earned doctrine |

If a keeper here turns out to *not* already be in place — i.e., the underlying claim is missing, not just unstated — it becomes a parked lead and migrates to `parked-leads.md`. Otherwise it stays here until the docs pass.

## Keeper inventory (seed)

Initial seed for the inventory. Add entries as they surface; trim as they land in canonical homes.

| Keeper sentence | Candidate canonical home | Underlying claim already in |
| --- | --- | --- |
| *"A log line is a witness statement, not substrate contact."* | NQ docs / witness-discipline section | NQ `cannot_testify` discipline + `WitnessInvariance` kernel |
| *"A cached answer is not fresh authority."* | Authority docs / freshness section | `Freshness.lean` + `working/primitives/stale-binding.md` |
| *"Claims are portable; authority is local unless a border-crossing substrate preserves it and a verifier honors it."* | Authority docs / serialization section (already present in `authority-observable-not-constructible.md`) | `working/authority-observable-not-constructible.md` |
| *"Once authority crosses serialization, it is no longer authority; it is a claim requiring verification/reminting."* | Authority docs / serialization section | Same — sharper compression of the gnat-lab finding |
| *"A collapsed surface may authorize inquiry. It may not authorize attribution."* | `SurfaceAuthorization.lean` docstring (already there) + downstream tool docs | `Admissibility/SurfaceAuthorization` |
| *"Narrative may route attention to receipts, but may not authorize mutation."* | Chronopolitics manuscript / authority docs | `FiatAdmissibility.classify` + `compression-becomes-authority-vocabulary.md` |
| *"Lucky is not authorized."* | Wicket / AG receipt documentation (when those land) | `working/primitives/post-hoc-authorization.md` + `SurfaceAuthorization` |
| *"Staleness says the map is old. Skew says which way it lies."* | `working/primitives/memory-skew.md` (already there) | `AxisSkew.lean` + `memory-skew.md` |
| *"A handle is not a predicate. A predicate is not a fixture. A fixture is not a kernel."* | Methodology docs / audit-procedure spec | Memory [[feedback-gate-stack]] |
| *"Not earned is a custody state, not a truth value."* | `working/parked-leads.md` framing section (already there) | `working/parked-leads.md` |
| *"People are naming the cliff; I'm formalizing the guardrail geometry."* | `admissibility-as-pre-authorization-layer.md` external-pitch section | `working/tooltheory/admissibility-related-work-map.md` § Overlap determination (Priority 0 synthesis) — the altitude-differentiation claim |
| *"The external world is converging on the problem statement. The corpus survives as a lower-altitude formal/refusal substrate, not as the first naming of the concern."* | `admissibility-as-pre-authorization-layer.md` external-pitch section | Same — the spike's strategic-result framing after codex + ChatGPT both pulled back the "first to name" overclaim |

## Placement rule

A keeper lands when:

1. The documentation pass that owns the canonical home runs, *and*
2. The keeper compresses better than what's currently there, *and*
3. The underlying claim is verified still in place.

If the underlying claim has moved or the kernel state has changed since the keeper was filed here, the keeper gets re-verified before placement.

## Anti-patterns this file refuses

- **Stockpiling keepers as if they were doctrine.** A keeper is a cosmetic upgrade on existing doctrine, not a substitute for it. If you find yourself wanting to *cite* a keeper from this file in active work, the keeper has not yet earned that citation — go cite the underlying claim instead.
- **Reading this file as a TODO list with priority.** It has no priority. Documentation-legibility passes are opportunistic; they happen when a docs surface is already being touched. Touch this file when that's happening; otherwise ignore it.
- **Promoting a keeper to a parked-lead because it sounds important.** If the keeper has no underlying claim, it's not a keeper — it's a candidate handle that should be evaluated against the [gate stack](../../../.claude/projects/-home-jbeck-git-papers/memory/feedback-gate-stack.md), not stockpiled here.

## Cross-references

- `working/parked-leads.md` — deferred-build register (different artifact type)
- [[feedback-gate-stack]] — handle → predicate → fixture → kernel discipline
- `working/primitives/AUDIT.md` — per-primitive overclaim/non-case audit
