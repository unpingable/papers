# Refusal algebra — prior art and application zones

**Status:** Companion reference to `refusal-kernel-to-refusal-receipt-seam.md`. Filed 2026-05-25 as park-state for tomorrow's planning pass. Not promoted; not yet authorized to grow into spec, draft, or kernel. Reference material — citations and application surface — kept here so the seam note stays focused on the layer structure.

**Purpose:** Capture the residue of the prior-art survey and the application-zone enumeration in a form that survives session-shutdown. So that *tomorrow's planning* doesn't have to re-derive what eight related fields cover, what's actually distinctive, and where the operator family shows up across domains.

---

## What this is not

- Not a literature review draft.
- Not a paper outline.
- Not authorization to cite, write, or scope a paper.
- Not a primitive.
- Not a kernel.
- Not a working specification.

It is **citation ballast plus an application catalog** — material to consult, not material to publish.

---

## Prior-art citation stack (foundations to cite when *refusal algebra* earns prose)

Eight neighboring fields. The pattern *surface predicate ⇏ substantive predicate* shows up across all of them; none packages the full seven-tuple `(claim, basis, witness, scope, time, use_kind, consequence)` aimed at *admissible use* rather than *truth*.

| Foundation | Anchor | Role in refusal algebra |
|---|---|---|
| **Dung argumentation frameworks** | Dung 1995, *On the acceptability of arguments* | Reasons attack/defeat other reasons; acceptability is computed structurally. Closest neighbor for **refusal composition** and **conflict handling**. |
| **AGM belief revision / TMS** | Alchourrón–Gärdenfors–Makinson 1985; Doyle 1979 *A truth maintenance system* | Rational belief revision under new information; dependency tracking when assumptions fail. Ancestor of **refusal propagation** through claim graphs. |
| **Database provenance semirings** | Green–Karvounarakis–Tannen 2007, *Provenance Semirings* | Algebraic account of how query answers depend on inputs; "why-not provenance" explains missing expected answers. Cleanest technical cousin — refusal algebra is **why-not provenance for authority-bearing claims** instead of tuple membership. |
| **Access-control calculi** | Abadi–Burrows–Lampson–Plotkin, *A Calculus for Access Control in Distributed Systems* | Principals, requests, delegation, authority as logical objects. Gives the **authorization spine** (who speaks for whom). |
| **Justification logic** | Artemov, *The Logic of Justification* (Stanford Encyclopedia of Philosophy entry) | Explicit reason terms `t : F` ("t justifies F"). Closest neighbor for **basis-witnesses-claim** structure. Refusal algebra tracks **reason failure modes**, not reasons. |
| **Input/output logic** | Makinson–van der Torre, *Input/Output Logic* / *Permission from an Input/Output Perspective* | Conditional norms, permissions, obligations; distinguishes kinds of permission (positive, negative, not-forbidden). Foundation for *allowed-to-observe ⇏ allowed-to-bind* and *no-prohibition ⇏ positive-standing*. |
| **Belnap four-valued / paraconsistent logics** | Belnap 1977 (and SEP entry on many-valued logic) | True / false / both / neither — explicit move away from binary truth. Foundation for **"runtime refusal cannot be pass/fail"** at the truth-status level. Refusal algebra extends this from truth-status to authority-status. |
| **Toulmin argument model** | Toulmin 1958, *The Uses of Argument* | Claim / grounds / warrant / backing / qualifier / rebuttal. Conceptual ancestor for separating claim, basis, warrant, qualifier, rebuttal. Rhetorical, not runtime — useful ancestor, not substrate. |

## What none of them quite package

The distinctive combination:

> **A typed refusal algebra over witness-bearing claims, where refusal is scoped by basis, witness, time, use-kind and downstream consequence.**

Most neighboring fields ask one of:

- Is the proposition true? *(many-valued, paraconsistent)*
- Is the argument acceptable? *(Dung argumentation)*
- Does the belief survive revision? *(AGM, TMS)*
- Why did this query result appear or not appear? *(provenance)*
- Is the principal authorized? *(access control)*
- Is the permission/obligation triggered? *(I/O logic, deontic)*
- What's the structure of the argument? *(Toulmin)*

Refusal algebra asks the different question:

> **Given this basis, what may this claim authorize, and what structured refusal follows when it cannot?**

That's *narrower than general logic, richer than access control, more operational than Toulmin, more authority-sensitive than database provenance, more typed than I/O logic.* The novelty isn't the ingredients. It's the packaging aimed at *admissible use* rather than *truth*.

### What to call it (and not yet)

**Current accurate term:** *the negative consequence algebra of admissibility.* Or: *the algebra of failed witness promotion.*

**NOT yet:** *formal dual of admissibility.* A dual requires earned mappings:

- ALLOW ↔ REFUSE?
- basis sufficiency ↔ basis failure?
- standing ↔ standing denial?
- scope expansion ↔ scope narrowing?
- authorization ↔ lockout?

That structure might exist. It hasn't been proved. The word "dual" stays unspent until earned.

**Best general line** (filed as a keeper):

> **Refusal calculus is how a system preserves weaker truth without letting it impersonate stronger authority.**

That subsumes the layer-split, the operator family, and the application story in one sentence. If only one survives long-term, it's this one.

---

## Application zones (where the operator family already lives)

The pattern *surface predicate ⇏ substantive predicate* is obnoxiously portable. Once recognized, it appears across at least nine domains (seven filed 2026-05-25; two added 2026-06-10 from relay residue). Listed as recognition vocabulary — NOT as project authorizations.

### LLM / agent safety
- Fluent output ⇏ settled learning *(this is `ConsolidationDenial`)*
- Tool-call proposal ⇏ authorized actuation
- Memory candidate ⇏ durable memory
- Summary ⇏ receipt
- "I checked" ⇏ admissible verification

Runtime outcome: advisory only, require revalidation, block actuation, force consolidation interrupt.

### NQ / claim preflight (home turf)
- SMART PASS ⇏ disk healthy
- NXDOMAIN from resolver ⇏ domain does not exist
- HTTP 200 ⇏ service recovered
- no alert ⇏ no incident
- fresh metric ⇏ valid conclusion

Runtime outcome: narrow scope, cannot testify, deny binding use, require different witness.

### Incident response / SRE
- service green ⇏ recovered
- workaround holds ⇏ fixed
- no recurrence ⇏ closed
- postmortem written ⇏ learning occurred
- rollback succeeded ⇏ cause understood

Runtime outcome: closure denied, recovery margin unknown, advisory status only.

### Law / governance (the spicy one)
- legal ⇏ legitimate
- signed ⇏ witnessed *(this is `signed_is_not_witnessed.md`)*
- procedurally valid ⇏ licit
- authority claimed ⇏ standing held
- emergency declared ⇏ unlimited scope

Runtime outcome: valid-but-illicit register, standing denied, scope narrowed, legitimacy unresolved.

### Bureaucracy / institutions
- form complete ⇏ case understood
- compliance passed ⇏ risk controlled
- metric met ⇏ mission served
- audit completed ⇏ accountability achieved
- stakeholder consulted ⇏ consent obtained

Runtime outcome: cannot bind, requires substantive witness, procedural success degraded to advisory.

### AI evaluation
- benchmark score ⇏ competence
- preference win ⇏ safe deployment
- no observed failure ⇏ capability absent
- red-team pass ⇏ robust
- explanation ⇏ reasoning trace

Runtime outcome: claim narrowed to tested scope, deny generalization, require coverage receipt.

### Social / media / politics
- virality ⇏ salience
- consensus appearance ⇏ legitimacy
- label applied ⇏ phenomenon understood
- outrage ⇏ harm model
- silence ⇏ consent

Runtime outcome: standing denied, conflict/ambiguity, cannot testify, requires independent witness.

### Supply chain / artifact deployment *(added 2026-06-10)*
- attestation present ⇏ artifact deployable
- signed provenance ⇏ build trustworthy
- SBOM complete ⇏ components vetted
- scan passed ⇏ vulnerability absent
- log inclusion ⇏ custody *(consume side of forbidden-inference register row 6)*

Runtime outcome: deployment refused with named missing attestation/bridge; receipt identifies which gate refused and what witness would discharge it. Note the register treats in-toto/CT/Sigstore as **substrate specimens** (where the pattern was discovered); this zone is the **consume side** (where refusal receipts would land). Source: 2026-06-10 relay, via [`guarded-lift-admission-overlap-audit-2026-06-10.md`](guarded-lift-admission-overlap-audit-2026-06-10.md).

### Regulated data flows *(added 2026-06-10)*
- lawful in zone A ⇏ lawful in zone B
- transfer agreement existed ⇏ agreement current *(SCC/DPA expiry — freshness axis)*
- consent collected ⇏ consent covers this purpose
- data classified ⇏ flow authorized

Runtime outcome: cross-boundary flow refused; receipt names the missing legal bridge artifact and its expiry/scope. Distinctive feature: the bridge here is a **human/legal artifact**, which makes the testimony-vs-consequence split unusually visible — legal/organizational testimony does not silently become technical consequence. Source: same relay/audit as above.

---

## Connection to laundering-move-watchlist (anti-laundering grammar)

Refusal algebra gives the laundering-move watchlist its *negative-space companion grammar*.

The watchlist generator says:

> *An artifact with limited standing crosses a boundary into a stronger operational role without earning the transition.*

Refusal algebra asks the inverse question:

> *Given that the artifact's standing is limited, what may the artifact still authorize, and what structured refusal follows when it cannot carry the stronger role?*

This means:
- Every laundering move (Section A of the watchlist) has a corresponding refusal-algebra entry — the algebra is what blocks the move at runtime.
- Every Section B handle (named-not-promoted) has a corresponding refusal pattern — the algebra is what the runtime would emit.
- The refusal-algebra outcomes (CANNOT_TESTIFY / INSUFFICIENT_BASIS / STALE / ALLOW_NARROWED / etc.) are what a system *says* when it refuses a laundering move.

> **Refusal calculus is the general grammar of anti-laundering: it lets a system preserve partial evidence without laundering it into permission.**

The two structures compose; they don't compete. Watchlist names the moves; algebra names the structured refusals.

---

## What this enables (the practical claim)

Without refusal algebra, systems are stuck with two failure modes:

1. **Bureaucratic paralysis** — partial evidence treated as worthless; nothing can authorize because nothing meets the perfect bar.
2. **Dashboard-civilization clowncraft** — partial evidence treated as good-enough; weak signals laundered into binding authority because the alternative is paralysis.

Refusal algebra lets a system say:

> *This basis is admissible for X, inadmissible for Y, stale for Z, and repairable by W.*

That's the **third option** between paralysis and laundering. The contract is worth formalizing when this distinction yields a precise, non-vacuous algebra or countermodel; that formalization may lead the runtime case that instantiates it.

---

## Cross-references

- [`refusal-kernel-to-refusal-receipt-seam.md`](refusal-kernel-to-refusal-receipt-seam.md) — primary seam note. Layer split, operator family, calculus-earns-its-shoes gate, P28 forcing-case candidate.
- [`consolidation-denial.md`](consolidation-denial.md) — the first instance landed today (Fluent ⇏ Settled).
- [`../../specifications/signed_is_not_witnessed.md`](../../specifications/signed_is_not_witnessed.md) — the second instance landed today (Signed ⇏ Witnessed).
- `~/git/lean/LeanProofs/Admissibility/RecoveryMargin.lean` — VisibleGreen ⇏ RecoveryMargin (pre-existing).
- `~/git/lean/LeanProofs/Admissibility/ClosureEligibility.lean` — Survival ⇏ ClosureEligibility (pre-existing).
- [`../laundering-move-watchlist.md`](../laundering-move-watchlist.md) — the positive-space companion: laundering moves blocked by refusal algebra outcomes.
- `[[project-laundering-move-watchlist]]` — memory pointer.

## Provenance

- Eight-foundation prior-art survey: ChatGPT 2026-05-25, after operator brought the multi-model relay forward with "what's actually new-ish here?"
- Application-zone enumeration: ChatGPT 2026-05-25, same session.
- "General grammar of anti-laundering" framing: ChatGPT, same session, connecting refusal algebra to the existing laundering-move watchlist.
- Filed as park-state by claude-code 2026-05-25, ahead of tomorrow's planning pass. The user's framing was *"rich vein,"* with the explicit intent to plan tomorrow.

## Park state

The work survives shutdown here. Tomorrow's planning can consult:
- The seam note for layer structure and the operator-family gate.
- This file for citations + application surface + the anti-laundering connection.
- `consolidation-denial.md` for the live LLM specimen.
- The Lean refusal kernels already in `~/git/lean/LeanProofs/Admissibility/`.

Nothing is built that wasn't already built. Nothing is promoted that wasn't already earned. The recognition vocabulary is preserved so the next composition theorem — when it arrives — lands with all the surrounding context intact.

> **Refusal calculus is how a system preserves weaker truth without letting it impersonate stronger authority.**
