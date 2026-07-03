# Show Me the Receipt
## Public register for No Silent Delta and the receipts corpus

**Filed:** 2026-07-03
**Status:** Candidate / public-language layer. This is the Substack/books register, NOT
the theorem layer — it owns the *doors*, not the claims. Every claim's custody stays
with `working/authority-conservation-candidate.md` and the Lean files. No venue
decision is made or implied by this file (see §9).
**Provenance:** multi-model session 2026-07-03 (Claude-lean + ChatGPT converged on
accounting/fraud; landmine audit by Claude-lean; AAA/ocap footing checked by ChatGPT
against Cisco AAA docs and the ocap literature).

**Top line:**

> **A log proves emission. A receipt proves standing.**

---

## 1. The folk move (why anything is legible)

A frame is legible when it attaches to an invariant people already carry AND hands them
an action they already know how to perform. Conservation laws are legible because "you
can't get something from nothing" is pre-installed. Double-entry is legible because
"where did this money go?" is pre-installed. The action this corpus hands people:

> When a system grants, refuses, delegates, revokes, or executes authority — **ask
> where the receipt is.** If it can't answer, that's the finding.

That's the Monday-morning audit move. Everything below is a door into it, tuned per
audience.

## 2. Civilian / auditor door: double-entry

Double-entry bookkeeping does NOT say money is conserved — money is created, spent,
destroyed, written off constantly. It says **every change must be entered**, with its
source and its destination, and a change without an entry is not a mistake, it's fraud.
That is exactly No Silent Delta. Pacioli got the "huh" in 1494; capitalism was built on
trusting it.

Pitch: *We keep books on power the way accountants keep books on money. If authority
appears, disappears, crosses scope, or changes hands, the system must show the receipt.*

Keeper: **The theorem is double-entry bookkeeping for authority; the code refuses any
entry that doesn't balance.**

The whole discipline in three lines anyone can carry out of the room:

> **No change without an entry.
> No entry without a receipt.
> No receipt without someone letting it in the door.**

(Internal form: no represented delta without a posting; no posting without support; no
support without admission.)

Fraud line: **Ambient authority is how control planes cook the books.** (`IsAdmin =
True` sitting in a database for six years is an unaudited ledger.) And the deepest cook:
pretending every account is the same currency — once coverage, standing, and custody all
spend as one denomination, every illegal translation becomes merely a low balance
instead of a type error.

## 3. Engineer door: the borrow checker

> **Ambient authority is untyped memory. No Silent Delta is the borrow checker.**

We already learned this lesson once: we stopped pretending arbitrary bytes were safe
just because they were addressable. Stop pretending authority is valid just because it
is reachable, signed, logged, or green. The mapping is tight, not decorative:
no-contraction on spendability is move semantics; the named-offender refusal is the
error-message-quality claim (*refusal never mislabels — the reported label is itself an
excess witness*, `forgery_offender_is_excess`).

Second panel (2026-07-03, `CrossingBalance.lean`): **a round trip across a privilege
boundary is not a refund — each traversal is priced.** The permissive layer literally
cannot see the double-spend (Cartesian membership is contraction-free); the linear layer
refuses it and names the receipt.

## 4. Preloaded rebuttal: the AAA collision (network/ops audience)

"Accounting" is already the third A — authentication, authorization, accounting
(RADIUS/TACACS+) — and it means **usage metering after access was granted**. Do not
pretend the word is clean; use the trap as the opener:

> *You already have accounting. It meters what happened after access was granted. It
> does not book where the authority came from, what scope it had, what it spent, or why
> a refusal counted.*

The cut: **a log proves emission; a receipt proves standing** (this is
`LogOnlyProvesEmission` in public clothes). The corpus is the fifth category adjacent to
authn/authz/accounting/attestation — admissibility — and this rebuttal is what keeps it
from being collapsed back into the third A.

## 5. Preloaded rebuttal: the ocap lawn (capability audience)

"Ambient authority" is established object-capability vocabulary (Miller et al.; confused
deputy, capability myths). **Cite as ancestor, never coin.** The split:

> *Capabilities make possession explicit. This work makes authority deltas receipted.*

Ocap solves minting-by-ambience. It does not give typed sinks, refusal receipts, expiry
accounting, or the admission boundary. Never title anything "Authority Is Not Ambient"
unless the goal is a lawn dispute with Mark Miller's ghost in the first question.

## 6. Preloaded rebuttal: blockchain (four words)

> **Consensus is not custody.**

Long form: blockchain records agreement about a sequence of entries; admissibility asks
whether an entry had standing to count. Consensus preserves counterfeit authority
exactly as faithfully as real authority. Expect this capture within thirty seconds of
saying "ledger" or "receipt" near funding.

## 7. Register correction: counterfeit vs inadmissible

Slides may say *counterfeit*. The precise claim is stronger and stranger:

> **Unreceipted ≠ false. Unreceipted = inadmissible.**

An unreceipted authority claim might be *true* and still cannot count — that is
signed-is-not-witnessed in courtroom English, and civilians already have it installed
from every cop show: inadmissible evidence can be completely true; the court still
refuses it. This is also the deepest cut against the consensus conflation (§6): truth
preservation is not standing.

## 8. The no-single-slogan result (why there is no brass ring)

There is no universal door, and that is the theorem operating at the rhetoric layer: a
one-slogan pitch would be a rhetorical global scalar, laundering exactly the
per-audience distinctions the rebuttals defend. The translation table IS the public form
of no-global-potential — uniform idea, per-audience doors, bridges priced per crossing.

| Audience | Door | Keeper |
|---|---|---|
| Civilians / auditors | double-entry, fraud | show me the receipt; cooked books |
| Ops / security | AAA trap | log proves emission, receipt proves standing |
| Ocap people | ancestor/delta split | possession-explicit ≠ delta-receipted |
| Blockchain people | standing vs agreement | consensus is not custody |
| Engineers | borrow checker | ambient authority is untyped memory |
| Lawyers / everyone | evidence law | true but inadmissible; chain of custody |

Parked title candidates: *Show Me the Receipt: Standing, Custody, and Authority Deltas*
/ *Receipts for Authority: Why Logs, Tokens, and Consensus Do Not Prove Standing*.

## 9. Venue fence (binding on this file)

Public language ≠ conference plan. The venue posture stays books + Zenodo unless
separately and explicitly re-decided; the USENIX/SAGE framing in the source session was
usable *language*, not a commitment — old venue ambition returns wearing whatever
mustache is nearest, and "the legibility work needs a conference" is a good one. If the
talk ambition comes back, it comes back as a named decision, not smuggled through this
register.
