# Chart-of-Accounts Lens
## Account / Posting / Support as a meta-handle over resident structures

**Filed:** 2026-07-03
**Status:** Candidate / **handle-stage only** (gate stack: handle → predicate → fixture
→ kernel; this file earns rung one and claims nothing above it). Prose-only lens. NOT a
new primitive. NOT a new refusal. No Lean. No global `Account : Type`. No shared
interface across calculi. No promotion.
**Provenance:** operator question 2026-07-03 ("are we missing any primitives, lifted out
of the application vocabulary?"), ChatGPT lift, Claude-lean overlap audit, operator
ratification same day. Companion: `working/authority-conservation-candidate.md` (§0
ladder, §9 hazards), `working/public-register-authority-receipts.md`.

**The ratified classification:**

> **Account/Basis is not a new primitive. It is a meta-level handle for resident
> per-calculus structures.**

The constellation kept answering "no missing primitives" because inside each calculus
the answer IS no: every calculus already has its chart of accounts. What was missing was
the *name for the pattern the residents share* — a kind, per the primitive ontology, not
a refusal primitive.

---

## 1. The kernel thought

Double-entry's primitive is not money and not the transaction — it is the **chart of
accounts**: the declared structure that says what kinds of entries exist and where a
delta may be posted. The corpus's version: coverage, standing, custody, bridge
eligibility, obligation discharge, refusal, revocation, residue, freshness, admission —
these were never values of one `Auth`. They are **accounts**, and the corpus's refusals
are all instances of one move:

> **Receipt discipline was never only about receipts. It was about refusing untyped
> postings.**

"Coverage does not spend as standing" is not a failed inequality — the comparison is not
well-typed. That was always the content of non-fungibility; the lens just names where
the typing lives.

## 2. Residents map (the lens is citation, not construction)

| Lens term | Resident object(s) | Where |
|---|---|---|
| **Account / Basis** | jurisdiction scope (declared, opt-in, per-vocabulary); basis kind (kind-matched discharge, *no universal/top basis*); obligation atom; declared vocabulary | `JurisdictionScreen.lean` (v7); `BestEffortCompleteness.lean`; bridge obligation lattice |
| **Posting** | the booked delta: trace entry (position, label, polarity-in-context); occurrence consumption record | `OccurrenceTrace.lean` (`linearizeT` trace); `CrossingBalance.lean` (which occurrence paid which leg) |
| **Support** | the evidence making a posting admissible: `Consumes`/`Split` proof, derivation, receipt | v5/v6 normalization stack; = locked term **Receipt** in the authority-observable vocabulary (see §3) |
| **Admission** | the governed world→ledger boundary | admission gate (claim-conversion normal form); NQ/observatories |
| **Bridge / Conversion** | typed, paid, per-pair relation between accounts, **no default exchange rate** | `ArtifactProfiles.lean`, `CrossingBalance.lean`; `unmatched_context_cannot_convert` |
| **Projection / View** | lossy representation that must not become authority | `PredicateWitnessSeparation.lean` ("findability is not legitimacy") |
| **Settlement / Refusal** | closure of an obligation, including negative closure, receipted | `CheckpointSettlement.lean`; mandamus (`refusals-need-receipts.md`); relaxation valve |
| **Custody / Handoff** | path-sensitive preservation across carriers | custody spine (`chainOf`); transport hazard |

Nothing in the right columns is new. The lens's entire formal content is this table.

## 3. Vocabulary reconciliation (extend the lock, don't fork it)

`working/authority-observable-not-constructible.md` locks six terms: Observation,
Testimony, Receipt, Claim, Authority, Token. This lens **extends** that table; it does
not compete with it:

- **Support** = locked **Receipt** (copyable audit artifact; evidence for what was
  decided). Same object, ledger-register name.
- **Posting** = new handle, naming a distinction the formalism already implements but
  the prose conflated: the *booked ledger item* (trace entry) versus its *support*
  (the `Consumes` proof). `linearizeT` returns both, separately, and always has. The
  ladder below is why the split matters.
- **Account** = new handle for the resident scope/basis/atom structures (§2).
- Locked **Authority** (spendable capability, minted not constructed) is untouched —
  see §6 for how it re-enters as a *derived* object.

## 4. The ladder (the least-pidgin form of No Silent Delta)

> **No represented delta without a posting.
> No posting without support.
> No support without admission.**

Three rungs, each a resident discipline: rung one is No Silent Delta (totality of the
receipted classification), rung two is receipt adequacy (support discharges the posting,
never merely labels it), rung three is the read boundary (Lean polices the books, NQ
polices the door). Folded into the theorem note (§0) and the public register (§2).

## 5. The transport correction, at primitive altitude

Bad model: *network transit reduces authority* (decay-laundering). Ledger model:

> **Transit is not decay. Transit is an unbooked custody delta unless witnessed.**

A witnessed handoff posts custody-preserving flux; an unwitnessed hop cannot be posted
as preserved custody — not "authority leaked," but "the books have no entry, so the
ledger cannot represent survival." Domain-independent form of hazard §9.1.

## 6. The readout clause (load-bearing, and it cuts both ways)

The lift's sharpest consequence: **authority disappears as a primitive** — it becomes a
derived balance/standing over posted, typed entries. Admissible ONLY with this bolted
on:

> **Authority may be a derived balance, but reading that balance is itself a governed,
> receipted act.**

A derived balance is a *view*, and views do not authorize (`PredicateWitnessSeparation`)
— without the clause, Franklin returns as a dashboard: he no longer needs one account,
just one query. The corpus already proved the blocking theorem
(`NoFreeStandingReadout.lean`, zero-axiom: no free-standing readout of standing;
readout is a governed act).

**Seam surfaced by the resident-note check:** `authority-observable-not-constructible.md`
(2026-05-07) grants consumers casual query rights (`is_authorized`, `why_denied`),
predating the readout arc (2026-06-15) that governs exactly those reads. The lens adopts
the governed version; the older note's query clause should be read as
*observable-through-a-governed-readout*, not free consultation. (Noted here as a seam,
not silently patched there — that note has its own custody.)

## 7. The Franklin quarantine

**Formal hazard name:** Single-Account Collapse (alias: Degenerate Chart of Accounts).
**Hostile nickname:** Franklin. Nickname lives in hazard sections and scratch
quarantine only — never in a title, never in Lean.

> **Franklin is the model where `Account` has exactly one inhabitant.** Every posting is
> denominated in the same fake unit, so everything becomes comparable, and illegal
> translations become merely low-ranked instead of ill-typed.

This is the precise definition of the scalar collapse (`GlobalScalarTrap`, theorem note
§9.2): the global μ is Franklin's balance; the global `Auth : Type` is Franklin's
currency; the ungoverned dashboard (§6) is Franklin's teller window. Codex finding #4
named the interface form; this names the degenerate-chart form. Same collapse, three
disguises.

## 8. Fences (binding)

- **Charts are per-calculus and declared, or it is Franklin.** No global
  `Account : Type`; a cross-calculus `Bridge : Account A → Account B → Type` requires
  all accounts to inhabit one type, and that type is the forbidden unifier by
  denomination instead of scalar.
- No Lean from this note. A "chart of accounts" typeclass is codex finding #4 verbatim.
- The lens reorganizes **prose**, not the formalism. Where the lens and a resident
  theorem disagree, the theorem wins and the lens is wrong.
- Accounting vocabulary here is the *internal* register; the public-facing accounting
  language lives in the public register note with its own fences (AAA collision, venue).

## 9. Falsifier

This lens is **empty** if it adds nothing beyond relabeling the residents. Its claimed
earnings, each checkable: (a) the Posting/Support split names a distinction the Lean
already implements but the prose blurred; (b) the Franklin definition gives the scalar
hazard a precise degenerate-model form; (c) the transit correction restates hazard §9.1
domain-independently; (d) the readout composition surfaced a real seam between two
resident notes (§6). If those four reduce to zero on inspection, retire the lens; the
residents lose nothing.

**Keeper:** *Receipt discipline was never only about receipts. It was about refusing
untyped postings.*
