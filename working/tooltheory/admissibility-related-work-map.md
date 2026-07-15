# Admissibility — related-work / representation-menu map

**Filed:** 2026-06-04 in `tooltheory/`. **Status:** prior-art map + representation menu. Not doctrine. Route signs for future "isn't this just X" review challenges.

## Why this exists

The corpus's work sits adjacent to a dense literature, much of it twenty-plus years old. Each middle rung between "Cedar policy decision" and "refusal kernel for forbidden conversions" already has a name, a representation, and a paper trail. This map names the rungs so that:

1. Future-you doesn't get blindsided in review by Aura / SecPAL / macaroons / Biscuit / linear credentials as "ah, beans" prior art.
2. The corpus's distinctive object (refusal kernels) is positioned by negation against the positive machinery the rungs supply.
3. The middle rungs become a **representation menu** — you don't have to invent how to represent attenuation, delegation, freshness, or consumability; the literature has worked answers worth stealing.

## The keeper

> **Use prior-art tokens / logics for representation. Use refusal kernels for forbidden conversions.**

The middle rungs mostly formalize *how authority may travel*: delegate, attenuate, prove, consume, relate. The refusal kernels formalize *where apparent authority-conversions must fail* regardless of what the positive machinery says is well-formed.

## The map

> **Status caveat (load-bearing — read this before the table).** The "What it does NOT refuse" column is **conjectured pending reading**. Each cell in that column is an absence claim about a literature the relay summarized but did not directly witness. By the corpus's own four-receipt discipline, an absence claim composed from relay-summary is a *claim-receipt formatted as an observation-receipt* — signed but not witnessed. The table is route-signs pointing at neighborhoods; the read-queue below ratifies each cell. If a future reading discovers that, e.g., SecPAL's negation handling or some corner of the says-logic tradition *does* treat failure-to-confer-standing, the corresponding cell loses its position and the map gets corrected, not defended.
>
> The "What it represents" and "Nearest kernel neighbor" columns are claim-shape and survive secondhand transmission. The third column is the one that needs witnessing.
>
> Two keepers from the audit that caught this:
>
> > **Absence claims require witnessing.**
> >
> > **The map is route signage, not territory.**
>
> Per-row confidence status uses these levels:
> - `[unread]` — named neighbor, no direct reading yet
> - `[skimmed]` — partial reading, conjectures unrevised
> - `[witnessed]` — read with summary added; conjectured cell updated to observed claim
> - `[ratified]` — distinction with refusal kernels confirmed against the literature
> - `[collision]` — the literature already covers what we thought was distinctive; reposition or retire
>
> Current status for buckets below: `[unread]` except where annotated. The map's conjectured column will turn into observed claims only as items get checked off in the read queue. **7th bucket (Agentic-systems authorization 2026 convergence) minted 2026-06-04 from Priority 0 readings — see § "Priority 0 readings (2026-06-04)" below for per-item witness paragraphs.**

| Bucket | What it represents | What it does NOT refuse | Nearest kernel neighbor |
|---|---|---|---|
| **Cedar / Cedar Analysis** `[unread]` | Policy semantics; SMT-backed analysis over modeled universe. | *Conjectured:* whether the facts that became modeled entities were laundered into the universe in the first place. | All — Cedar is the outer reference point and toolchain precedent. |
| **SPKI / SDSI, macaroons, Biscuit** `[unread]` | Capability/certificate/token attenuation; minting and provenance representation; offline attenuation; decentralized verification. | *Conjectured:* self-mint at the substrate boundary; replay across surfaces without explicit caveats; standing-laundering through chained delegation. | BoundaryTransit witness substrate; custodian-binding candidate. |
| **ABLP / says / speaks-for / SecPAL / DKAL / NAL** `[unread]` | Testimony, delegation, "A says φ" credential logics; positive entailment from logical assertions; distributed knowledge. | *Conjectured:* when testimony fails to confer standing; what assertions cannot bind regardless of who made them; post-hoc retroactive claims. | Standing kernel (currently named-not-coded in BoundaryTransit). |
| **Proof-carrying authentication (Appel/Felten 1999) / proof-carrying authorization (Bauer et al., later) / Aura** `[unread]` | Request-time proof objects; dependently-typed authorization with proof emission for audit. Aura is uncomfortably close to "receipts": dependent types + authorization logic + audit-proof generation. | *Conjectured:* what proofs cannot be valid — the negative space of what no proof should be allowed to discharge. PCA builds the gift shop; refusal kernels are the contrapositive. | Refusal kernels generally; closest neighbor by methodology. **The most dangerous unread literature.** |
| **Linear / consumable credentials** (Bauer et al., PCFS) `[unread]` | Credentials/authority that can be spent, not copied; use-once tokens with explicit consumption discipline; logic-based access control with linearity. | *Conjectured:* shared-budget-reused-as-multiple-premises through narrative duplication of consumed tokens. | Spendability / multiplicity gap (ContractionHinge sibling, currently informal). |
| **Zanzibar / ReBAC** `[unread]` | Relationship edges as authorization substrate; per-edge attribute storage; consistent global authorization. | *Conjectured:* provenance laundering on relationship edges; whether the edge-minting itself was admissible. | Provenance-typed edges as a candidate intermediate artifact. |
| **Agentic-systems authorization (2026 convergence)** `[witnessed: A,B,D,E; skimmed: C]` (minted 2026-06-04) | *Observed:* positive policy/standards/architectural-requirements machinery for multi-agent authorization: workflow-level authorization invariants (Tallam), deployment-record authorization profiles (WEF/ACAP), federal RFI scoping (NCCoE, CAISI), and umbrella standards programme (NIST). Common shape: structured *necessary* requirements / deployment-record artifacts / scoping questions for *how authority is granted, traced, scoped, and re-authorized* at the agentic-systems boundary. | *Observed (Priority 0 readings):* laundering of authority through delegation chains (Tallam explicitly names; ACAP non-additive rule blocks one specific shape); aggregation inference in the general case (Tallam disclaims solving; NCCoE asks the question); typed-provenance-without-minting-discipline (ACAP "agent passport" carries the label, leaves the cryptographic minting open); premise validity as a layer distinct from authorization (no item names admissibility-as-such). | Cross-cuts all kernel rows. Strongest convergence: ACAP non-additive multi-agent authority ≈ SurfaceAuthorization standing-upgrade-block. Strongest gap: ACAP "agent passport" + Tallam aggregation-inference-open status ≈ the BoundaryTransit substrate bridge and the ContractionHinge formalization. |

## Read queue (the actual prevention)

The map exists to prevent "ah, beans" review surprises — but the *actual* prevention is the week of reading, not the map. The map without a queue can eat the meal: filing a satisfying cross-referenced object that scratches the itch the reading was supposed to scratch. So:

**Priority 0 (active 2026 convergence — currently moving, most likely to surface in review):**

These are 2026 items where the field is actively converging on the corpus's problem space. Different in kind from the historical-prior-art reads below: those ask *"has this already been done?"*; these ask *"is the field currently being claimed by adjacent work, and is the corpus visibly absent from a convergence it should be part of?"* The arXiv item is the most direct overlap; the NIST/NCCoE/WEF items establish that the agentic-systems authorization neighborhood is having its standards moment in real time.

A. `[x]` **arXiv: "Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure"** (Tallam, May 2026). Names *transitive delegation*, *aggregation inference*, and *temporal validity* as the open problem triad. Direct overlap with the doctrine map's composition-axis row, spendability/multiplicity gap, and Freshness row respectively. **The most directly overlapping current literature.** Read first. *Witnessed 2026-06-04 — see § Priority 0 readings.*
B. `[x]` **NCCoE concept paper: "Accelerating the Adoption of Software and AI Agent Identity and Authorization"** (NIST, February 2026). Most likely to be in a reviewer's hands as NIST-stamped technical guidance. *Witnessed 2026-06-04 — see § Priority 0 readings.*
C. `[~]` **NIST CAISI RFI on security considerations for AI agents** (Federal Register, January 2026). First formal U.S. government initiative scoped to controls for autonomous AI agent systems; establishes regulatory framing for the problem space. *Skimmed 2026-06-04 via NIST press release + secondary summaries; Federal Register direct URL hit an anti-bot redirect. See § Priority 0 readings.*
D. `[x]` **WEF "AI Agents in Action" playbook** (May 2026). Industry-applied; introduces authorization-profile / enforceable-governance / auditability framing. Most likely to be cited by enterprise reviewers. *Witnessed 2026-06-04 (full 37-page read) — see § Priority 0 readings.*
E. `[x]` **NIST AI Agent Standards Initiative** (announced February 17, 2026). Programmatic rather than paper-shaped; tracks the broader standards trajectory. *Witnessed 2026-06-04 — see § Priority 0 readings.*

If a 7th bucket eventually earns its place in the map proper — *Agentic-systems authorization (2026 convergence)* — these are the seeds. Not minted yet because the reading hasn't happened; the bucket-creation gate is the same as for any kernel: read, find the genuine distinction (or collision), then file. **Update 2026-06-04:** Priority 0 readings completed; the 7th bucket earned its row in the table above. The corpus's distinctive object (refusal kernels for forbidden conversions) survives intact — no Priority 0 item claimed the negative-space territory. Per-item paragraphs in § Priority 0 readings.

**Priority 1 (most dangerous historical unread):**

1. **Aura** (Jia et al., ICFP 2008) — *AURA: A Programming Language for Authorization and Audit*. Dependent types + authorization logic + proof emission for audit. Closest methodological neighbor from the foundational period; if anyone built receipts-as-types already, it's here.
2. **Proof-Carrying Authentication** (Appel & Felten, CCS 1999) — the original PCA paper, higher-order logic for distributed authentication. Then trace forward to:
3. **Proof-carrying authorization** (Bauer et al., later CMU work) — the named-similarly successor that uses proof objects at the gate.

**Priority 2 (load-bearing for substrate candidates):**

4. **Macaroons** (Google, NDSS 2014) — chained-HMAC credentials with caveats. Concrete substrate candidate for BoundaryTransit witness production form.
5. **Biscuit** — Datalog-based authorization token with offline attenuation. Likely modern alternative to macaroons; check current state.
6. **SPKI/SDSI** (RFC 2693 / RFC 2692) — older capability/certificate theory; mostly for lineage.

**Priority 3 (testimony/delegation neighborhood):**

7. **ABLP** (Abadi, Burrows, Lampson, Plotkin, 1993) — the founding *says* / *speaks-for* paper. Need to know what it does refuse vs. enable.
8. **SecPAL** (Becker, Fournet, Gordon, MSR) — declarative authorization with delegation; check negation handling specifically.
9. **DKAL** / **NAL** — successors; lower priority unless SecPAL turns up gaps the successors filled.

**Priority 4 (consumption / relationship rungs):**

10. **Consumable credentials in logic-based access control** (Bauer, Garriss, Reiter at MPI-SWS / CMU; PCFS) — the linearity neighborhood for spendability.
11. **Zanzibar** (Pang et al., USENIX ATC 2019) — Google's global authz; mostly for the ReBAC representation choice, not because the paper is novel theory.

**Process discipline for the reading:**

- For each item, the output is a one-paragraph note added to this file specifying: *what it actually refuses* (replacing the conjectured cell), *what it doesn't*, and *where the refusal kernels do or don't have new ground left*.
- If a reading reveals that a refusal kernel's negative-space territory is already covered by existing positive machinery, that kernel deserves either retirement, repositioning, or a sharpened version of the distinction.
- Do NOT use the existence of this queue as evidence the reading is done. Mark each item explicitly: `[ ]` unread / `[~]` skimmed / `[x]` read with summary added.

Current state: **`[ ]` all sixteen items** (5 in Priority 0, 11 in Priorities 1–4). The map's conjectured column will turn into observed claims only as items get checked off.

## The distinctive object (negative space)

Each middle-rung formalism is **positive**: it specifies how to grant, delegate, attenuate, prove, consume, or relate correctly. The corpus's refusal kernels operate in the **negative space**: they prove certain conversions cannot be valid *regardless of what the positive machinery permits*.

> **Refusal kernels are the contrapositive discipline to proof-carrying authorization: they mechanize the conversions that no proof, credential, token, testimony, or policy context is allowed to launder into binding authority.**

That's a one-sentence positioning a PL/security reviewer parses instantly. ABLP and Aura built the gift shop; the corpus is building the museum of forbidden moves.

## Substrate guidance (the actionable part)

When the witness-substrate question comes up for any kernel earning promotion from category-2 (fenced scratch) to category-1 (wired/annex):

- **For witness substrate**: macaroons / Biscuit / SPKI are the live candidates — *not* "signed JSON" handwaved generically. The attenuation history IS the minting receipt; the verifier-side check is what makes the substrate non-launderable. The substrate gap named in BoundaryTransit's header has a worked answer here.
- **For testimony / delegation**: SecPAL / DKAL / NAL are the canonical neighbors. "A says φ" semantics with explicit speaks-for relations is the existing vocabulary.
- **For consumption**: linear-credentials / PCFS prior art. Don't reinvent linearity; the consumption discipline already exists in usable form.
- **For relationships**: Zanzibar / ReBAC + provenance-typed edges as a candidate intermediate artifact (DeepSeek named this; it's tractable).

### Candidate carrier sketch (added 2026-06-04 after Priority 0 spike; refreshed 2026-06-05 with name-TBD menu; relational model layer filed 2026-06-06 — see [`witness-carrier-model-candidate-2026-06-06.md`](witness-carrier-model-candidate-2026-06-06.md))

**Candidate name (TBD, NOT minted):** `BoundaryTicket` / `AdmissionClaim` / `WitnessPacket` — name deferred to the substrate this eventually lands on. Macaroons-style instantiation would call it a ticket; Biscuit-style would call it a packet; ABLP / says-logic-style would call it a claim. Minting the name in markdown before a substrate is chosen is exactly the typed-provenance failure mode the sketch refuses (see § DeepSeek typed-provenance warning below and guardrail #1).

**Non-claim sentence (load-bearing):**

> *This sketch defines candidate production-witness carrier requirements; it does not establish correspondence between carrier validity and the Lean witness model.*

**Why a sketch lives here at all.** Priority 0 readings surfaced two publicly-articulated instances of the same gap BoundaryTransit's header names — ACAP's "agent passport" (WEF/Capgemini May 2026) and Tallam R2 "explicit/bounded/auditable delegation" (arXiv 2605.05440, May 2026). The substrate gap is no longer purely internal observation; the WEF working group and Tallam have publicly asked for the carrier shape. This sketch is the name-early record of a candidate answer, lives in pre-ratified `tooltheory/`, and is NOT to be confused with a schema.

**Candidate neighbors (carry-forward):** macaroons / Biscuit / SPKI per the bullet above. These define the *actual* schema; the menu below names the *fields* a non-launderable carrier would have to carry regardless of which neighbor supplies the cryptographic minting discipline.

**Candidate carrier-field menu (NOT a schema):**

- attempt id
- surface
- issuer
- subject
- issued-at
- observed-at
- valid window
- evidence ref
- caveats
- standing basis
- signature / chain / digest

**Candidate refusal cases the carrier must support typed-refusal for:**

- self-minted witness
- replayed witness
- wrong attempt
- wrong surface
- stale (issued-at outside valid window)
- widened-after-issue (caveat-set growth post-issue)
- post-hoc authorization laundering (issued-at after observed-at on the consuming side)

**Hard guardrails on this sketch:**

1. **Field list = menu, not schema.** Writing field names in markdown does not specify a wire format, a cryptographic discipline, or a validator. Anyone with a keyboard can write `{"basis": "external"}` (see § DeepSeek typed-provenance warning below); the carrier is whatever macaroons / Biscuit / SPKI already define, with these fields carried in the substrate's native attenuation chain — not a new format invented here.
2. **No Lean ↔ runtime correspondence claim.** A Cedar-style differential-randomized-testing harness needs a concrete runtime target, an explicit mapping, and generated behavioral evidence (see § Adjacent methodological theft in `admissibility-as-pre-authorization-layer.md`). Until that work exists, *Lean witness ≠ production witness* and the bridge is empty. This does not block the formal contract from leading.
3. **No promotion path implied.** This sketch does NOT live in `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean`. The Lean file is in the repo's `Scratch/` (NOT imported by `LeanProofs.lean`, not part of any DOI surface); putting candidate carrier-shape material inside it would contaminate the file by promotion-by-proximity. The sketch stays here, pre-ratified, because its wire-format and cryptographic semantics are not fixed. A bounded Scratch model may explore a precise carrier contract before a consumer exists, but public promotion and runtime correspondence remain separate. The Lean file may later point back to this sketch as substrate guidance without implying either status.
4. **The label is not the witness.** See § DeepSeek typed-provenance warning below. The carrier-field menu is governed by that warning, not exempt from it. If a reader interprets the menu as "just add these fields to JSON," the sketch failed.
5. **Conversion witness must be typed to the conversion, not the destination.** Added 2026-06-05 after the laundering-detector side-quest surfaced the destination-only-witness trap. A witness that generically "supports authority" or "supports target kind" is the skeleton key the typed-provenance warning above refuses. A typed conversion witness must bind: source kind, target kind, surface/object, scope/time, issuer/authority. Destination-only witnesses re-introduce the laundering surface they're meant to refuse. The carrier-field menu above already enumerates most of these binders (attempt id = surface/scope; issuer + signature chain = issuer/authority; issued-at/observed-at/valid window = scope/time); guardrail #5 names *why* they're all required together rather than as à-la-carte fields. See [`anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) § The master frame for the doctrine-map-altitude version.

## The DeepSeek typed-provenance warning

DeepSeek's "attribute bags with provenance" suggestion is implementable but **unsafe if provenance is just typed data**. Anyone can write:

```json
{ "basis": "external" }
```

The clown has a keyboard. The minting discipline is the load-bearing part — verify the credential, not the label. Macaroons / Biscuit / SPKI exist precisely because the typed-data approach is laundering-prone: the attenuation chain and the cryptographic verifier are what convert a typed claim into a non-launderable witness. Typed-provenance-without-minting-discipline reintroduces exactly the failure mode the refusal kernels exist to refuse.

If you ever see an implementation that has a `"basis": "external"` field with no verifier hook, that's the smell. The label is not the witness.

## Non-promotion guard

This map is positioning + representation menu. It is NOT:

- A new security-stack taxonomy. The admissibility positioning is a route sign; this map is its prior-art context.
- A doctrine file. Refusal kernels are the doctrine; this map is the neighborhood.
- A commitment to build any of the represented substrates. Whichever consumer pulls a kernel into use picks its substrate from this menu.
- A "full admissibility calculus" cathedral. Cathedral is the cope direction; representation menu + refusal kernels + tested correspondence is the cathedral-avoiding shape.

## Cross-references

- [`../admissibility-as-pre-authorization-layer.md`](../admissibility-as-pre-authorization-layer.md) — positioning note that this map provides prior-art context for.
- [`../anti-laundering-doctrine-map.md`](../anti-laundering-doctrine-map.md) — family rows that the middle-rung machinery is positive-counterpart to.
- [`../no-unifier-without-laundering.md`](../no-unifier-without-laundering.md) — federation doctrine consistent with the "borrow representations, refuse conversions" stance.
- [`kerberos-lineage-boundary-transit.md`](kerberos-lineage-boundary-transit.md) — sibling tooltheory note; Kerberos is in the authn neighborhood; this map covers the authz/admissibility neighborhood.
- `~/git/lean/LeanProofs/Scratch/BoundaryTransit.lean` — scratch encoding whose witness-substrate gap macaroons/Biscuit are live candidates for.

## Provenance

Surfaced 2026-06-04 from a multi-model relay (ChatGPT + Claude-web + DeepSeek) digging into prior art adjacent to BoundaryTransit and Cedar. Claude-web flagged that "Cedar gives toolchain legitimacy but not object legitimacy" — and that the middle rungs (Aura, SecPAL, macaroons, etc.) constitute the actually-dangerous-in-review prior art. This map is the route-sign list that prevents future-session "ah, beans" surprises. The afternoon of reading just became a week — but better identified now than in review.

## Priority 0 readings (2026-06-04)

Per-item witness paragraphs from the first execution of the read queue. Format: *what it actually refuses* / *what it doesn't* / *where the refusal kernels do or don't have new ground left*. The conjectured-cell discipline applies — these paragraphs replace claim-receipts (relay summary) with observation-receipts (direct reads of source documents).

### A. Tallam, *Authorization Propagation in Multi-Agent AI Systems: Identity Governance as Infrastructure* (arXiv:2605.05440, May 2026) `[witnessed]`

**Source:** https://arxiv.org/abs/2605.05440 (full HTML read). **What it represents:** Formalizes authorization propagation as a workflow-level property and identifies a triad of sub-problems — transitive delegation, aggregation inference, temporal validity. Derives seven structural requirements R1–R7 for *any sufficient* authorization architecture (first-class agent principals; explicit/bounded/auditable delegation; per-boundary evaluation; expressible aggregation policies; workflow-scoped self-contained traces; temporal validity as a policy decision with three modes — initiation-time / access-time / completion-time; recovery traceable through synthesis graph). **What it actually refuses (revised after codex pass 2026-06-04):** authority accumulation through delegation chains (no privilege escalation); confused-deputy misuse; the bare positive-machinery framings of RBAC / ABAC / ReBAC ("not fully addressed" by classical models); *initiation-time-only authorization* (R3 forces per-boundary evaluation — this is a prose-level architectural refusal of "authorized at A ⇒ authorized at B"); *was-true-still-admissible* in the temporal-validity treatment (R6). Empirically observes that "Semantic Intent Fragmentation achieves 71% success rate across 14 enterprise scenarios by decomposing legitimate requests into individually benign subtasks" — the authority-laundering pattern the corpus's ContractionHinge refuses, observed but not theorem-formalized. **What it explicitly does NOT refuse:** the paper disclaims a complete architecture ("We do not propose a specific authorization architecture. We identify the structural requirements that any sufficient architecture must satisfy"), disclaims solving aggregation inference in the general case ("an open research question with roots in statistical disclosure control"), and disclaims a final policy language. **Codex correction (2026-06-04):** the original draft of this paragraph said Tallam "names it without formalizing the refusal" — that under-stated Tallam's negative-architectural-claim contribution. Tallam does NOT mechanize refusal kernels (no formal impossibility proof, no Lean), but it DOES make prose/architectural refusals for boundary transit (R3), temporal staleness (R6), and authority accumulation under delegation. The corpus's distinction is *formal-impossibility-proof altitude + substrate testing*, not *first to articulate the negative rule*. **Citations relevant to this map:** Biscuit (Prakash 2026), Zanzibar (Pang et al. 2019); does NOT cite Cedar, ABLP, SPKI/SDSI, PCA, Aura, SecPAL, DKAL, linear credentials, macaroons explicitly (mentions "attenuated authorization" and "append-only token chains" without macaroon citation). **Where the kernels have ground left (revised):** Tallam articulates several of the negative architectural rules the corpus's refusal kernels formalize; the corpus's surviving ground is the formal-impossibility-proof level + the substrate-correspondence testing level, not the level of "first to name." Convergence mapping (extended after codex pass): R2 (explicit/bounded/auditable delegation) ↔ BoundaryTransit substrate + macaroons/Biscuit menu; R3 (per-boundary evaluation) ↔ SurfaceAuthorization standing-upgrade refusal; R4 (expressible aggregation) ↔ ContractionHinge spendability/multiplicity slot; **R5 (workflow-scoped self-contained traces) ↔ AttestationLedger.lean / receipt-provenance row (added after codex pass);** R6 (temporal validity policy) ↔ Freshness.lean (kernel altitude); **R7 (recovery traceable through synthesis graph) ↔ CrossBoundaryCascade.lean / cascade-recovery family (added after codex pass).** **Triage:** Bucket B (strongly adjacent); strongest non-collision adjacency in the entire Priority 0 set. **Citation discipline:** Should be cited in `admissibility-as-pre-authorization-layer.md` as convergent contemporary literature articulating the negative architectural rules the corpus's refusal kernels formalize.

### B. NCCoE, *Accelerating the Adoption of Software and AI Agent Identity and Authorization Concept Paper* (NIST, February 2026) `[witnessed]`

**Source:** https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf (full 11-page PDF read). **What it represents:** Scoping document for a planned NCCoE demonstration project; not prescriptive guidance. Defines five areas of interest (Identification, Authorization, Access Delegation, Logging/Transparency, Tracking Data Flows) and six question groups (General/Use Case, Identification, Authentication, Authorization, Auditing/Non-repudiation, Prompt Injection prevention). Standards menu: Model Context Protocol (MCP); OAuth 2.0/2.1; OpenID Connect; SPIFFE/SPIRE; SCIM; Next Generation Access Control (NGAC); plus SP 800-207 (Zero Trust), SP 800-63-4 (Digital Identity), NISTIR 8587 (Token Forgery). **What it actually refuses:** Nothing — it is an RFI asking questions, not asserting refusals. **What it explicitly does NOT refuse:** explicit scope exclusions are RAG-only and LLM-only architectures (line 79–80), and "the challenge of identifying and managing access for external agents from untrusted sources" (line 152) — i.e., cross-organizational trust boundaries are explicitly deferred. **Direct overlap with corpus questions:** Section 4 asks verbatim "if an agent gets access to new tools and resources, how do we determine sensitivity levels of data when aggregated by an agent, and whether users are authorized to access the aggregated response?" — this is the corpus's ContractionHinge / aggregation-inference question, asked but not answered. Section 4 also asks "What are the mechanisms for an agent to prove its authority to perform a specific action?" — the BoundaryTransit / witness-substrate question. Section 5 asks "How can we ensure that agents log their actions and intent in a tamper-proof and verifiable manner?" — the receipt-format / attestation question. **Citations relevant to this map:** Does NOT cite Cedar, ABLP, PCA, Aura, macaroons, Biscuit, SPKI/SDSI. Names: MCP, OAuth 2.0, OIDC, SPIFFE/SPIRE, SCIM, NGAC. **Where the kernels have ground left:** The corpus's distinctive object survives wholly; NCCoE is at the scoping/standards-menu level and asks exactly the questions the corpus's refusal kernels answer. **Triage:** Bucket B (adjacent / sibling layer); a venue where the corpus's contribution could be cited as informing the questions NCCoE is asking. Not a collision.

### C. NIST CAISI, *Request for Information Regarding Security Considerations for Artificial Intelligence Agents* (Federal Register, January 8, 2026) `[skimmed]`

**Sources:** NIST press release (https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems) and YeshID secondary summary (https://www.yeshid.com/post/nist-just-opened-a-public-rfi-on-securing-ai-agents). **Direct Federal Register fetch (https://www.federalregister.gov/documents/2026/01/08/2026-00206/...) hit an anti-bot redirect to `unblock.federalregister.gov` and was not bypassed. Marker is `[skimmed]`, not `[witnessed]`, per the map's discipline.** **What it represents:** Federal RFI on four/five topic areas: unique threats affecting AI agent systems; security practices and controls (model-level, agent-system-level, human oversight including "approvals for consequential actions and network access permissions"); security measurement and assessment; deployment constraints and monitoring (rollbacks / undos for unwanted action trajectories). Scope: AI agents that affect external state. Framing vocabulary: "least privilege," "zero trust," "separation of untrusted inputs from privileged actions," Meta's "Rule of Two" pattern. **What it actually refuses:** Nothing directly — it's an RFI. The implicit policy posture refuses prompt-injection-induced action and unsupervised privileged access. **What it explicitly does NOT refuse:** Conventional software-system vulnerabilities (authentication, memory management) are noted as overlapping but not the RFI's focus. **Citations relevant to this map:** None of the historical authorization-logic literature is cited in the available summaries. **Where the kernels have ground left:** The RFI's "separation of untrusted inputs from privileged actions" is adjacent to the corpus's witness-identity/provenance row but framed as architectural separation, not premise validity. The corpus's refusal kernels operate at the inference-validity level; the RFI operates at the policy-posture level. Sibling. **Triage:** Bucket B (adjacent). Worth re-reading the Federal Register source directly if a future review surfaces it as the authoritative regulatory framing; the secondary summaries may have under-reported the sub-question structure.

### D. WEF + Capgemini, *AI Agents in Action: A Playbook for Trusted Adoption, Authorization and Scaling* (May 2026) `[witnessed]`

**Source:** https://reports.weforum.org/docs/WEF_AI_Agents_in_Action_A_Playbook_for_Trusted_Adoption_Authorization_and_Scaling_2026.pdf (full 37-page PDF read). **What it represents:** Practical organizational playbook centered on the Agent Capability and Authorization Profile (ACAP) — a deployment-level "living document" with seven sections (A: Identity/scope; B: Operating context; C: Authority and consequential events; D: Controls/enforcement; E: Evaluation evidence and promotion gates; F: Monitoring/incidents/change-log; G: Sign-offs and re-authorization cadence) — and a three-phase adoption life cycle (design+assessment → prepare+deploy → monitor+improve) with phase gates. Operates within ISO 42001 and NIST AI RMF; aligned with EU AI Act Article 14 (Human Oversight). Distinguishes deployment-context tiers: single-org / multi-org-single-platform / multi-platform-cross-boundary. **What it actually refuses:** (i) permitted / conditional / prohibited categorization of every agent action; (ii) **non-additive multi-agent authority** — *"a downstream agent operates under the intersection of its own ACAP permissions and those of the agent that invoked it. An orchestrating agent cannot delegate authority it does not itself hold"* (p11); (iii) AI-only safety verification — *"Verifying the system's safety does not depend solely on AI-based oversight for any critical boundary"* (p20); (iv) emergent-behavior dismissal — explicitly names *"a system that could have perfectly certified and guaranteed sub-components yet produce collective behaviour that breaches policies"*; (v) automatic update — *"Updates should be reviewed by a human and not applied automatically"* (p29); (vi) silent decommissioning — revocation of delegated authority is mandatory at retirement. **What it explicitly does NOT refuse:** The "agent passport" concept (p11) — *"verifiable, machine-readable claims of identity, authorization and jurisdiction-specific compliance that other systems or platforms can independently validate. The agent passport would act as a portable compliance credential, allowing trust and governance requirements to travel with the agent across organizational and geographic boundaries. Agent passports carry capability and authorization claims rather than personal data"* — is named as a requirement without specifying the cryptographic minting discipline. **This is the exact failure mode the corpus's DeepSeek typed-provenance warning anticipates: the label is not the witness.** **Citations relevant to this map:** ISO/IEC 42001, NIST AI RMF 1.0 (NIST AI 100-1), EU AI Act Article 14, Agentic AI Risk-Management Standards Profile (Berkeley CLTC), Agent Name Service (Huang et al., OWASP), MCP-I (DIF), IMDA/AI Verify Foundation Model AI Governance Framework, model/system/agent cards (Mitchell et al. 2019; Meta, Anthropic, OpenAI), Agent2Agent Protocol AgentCard, OWASP Agentic AI Threats and Mitigations. **Does NOT cite: Cedar, ABLP, macaroons, Biscuit, SPKI/SDSI, PCA, Aura, SecPAL, DKAL, Zanzibar, linear/consumable credentials, Tallam.** **Codex correction (2026-06-04):** the original draft framed ACAP's permitted/conditional/prohibited as "categorization schema" and said ACAP "does not claim the broader negative-space territory" — both under-stated the negative-rule content. ACAP's combination of (i) intersectional downstream authority, (ii) AI-only-oversight-refused, (iii) emergent-behavior-naming (the "perfectly certified sub-components yet collective breach" passage refuses *component-certified ⇒ system-safe*), (iv) automatic-update-refused, (v) silent-decommissioning-refused constitutes a *governance-altitude refusal set* — not kernel-altitude formal impossibility proofs, but more than "policy doc." The corpus's distinction is the formal-impossibility-proof altitude and the witness-substrate-correspondence testing methodology, not "first to articulate the negative rule." **Where the kernels have ground left (revised):** Strongest single-row convergence in Priority 0 — ACAP's non-additive rule ≈ SurfaceAuthorization standing-upgrade-block (governance-altitude refusal ↔ kernel-altitude formal proof). **ACAP deployment-context tiers** (single-org / multi-org-single-platform / multi-platform-cross-boundary) **map directly to the corpus's CrossBoundary family** as a deployment-topology taxonomy for boundary transit — convergence added after codex pass; the original draft surfaced only "agent passport" and missed the broader topology mapping. The "agent passport" is the substrate-gap subset of this convergence — labels without minting discipline. ACAP's "emergent behavior" passage adds a candidate component-composition-refusal slot (no current corpus row yet; sits at the doctrine map's composition row, formal-layer empty per [no-unifier-without-laundering]). The corpus's typed-provenance warning is now externally validated by ACAP's reach for "machine-readable" passport without specifying its cryptographic discipline. **Triage:** Bucket B (strongly adjacent — governance-altitude convergence on multiple rows). Not a collision; not a "first-to-name" claim either. **Citation discipline:** ACAP should be cited in `admissibility-as-pre-authorization-layer.md` as the practical/organizational sibling-layer that (a) articulates the non-additive multi-agent rule the corpus's SurfaceAuthorization formalizes, (b) maps the deployment-topology taxonomy the corpus's CrossBoundary family refines, and (c) names the witness-substrate gap the corpus's BoundaryTransit + macaroons/Biscuit menu fills.

### E. NIST CAISI, *AI Agent Standards Initiative* announcement (February 17, 2026) `[witnessed]`

**Source:** https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure. **What it represents:** Programmatic umbrella announcement; three pillars verbatim: (1) "Facilitating industry-led development of agent standards and U.S. leadership in international standards bodies"; (2) "Fostering community-led open source protocol development and maintenance for agents"; (3) "Advancing research in areas of AI agent security and identity to enable new use cases and to promote trusted adoption across sectors." Commits to: research, guidelines, RFIs (CAISI RFI = item C), concept papers (NCCoE = item B), listening sessions starting April 2026. **What it actually refuses:** Nothing technical — this is the umbrella that organizes items B and C and points to future work. **What it explicitly does NOT refuse:** No technical claims to overlap with. **Citations:** None relevant to this map's prior-art neighborhood. **Where the kernels have ground left:** Wholly intact; this item is meta-announcement, not technical content. **Triage:** Bucket A (already covered, in the trivial sense — it is the parent of B and C). Read primarily for completeness; provides no new constraint on the corpus's positioning. Worth tracking as a venue where future technical guidance will appear.

## Overlap determination (Priority 0 synthesis)

The user's question — *how much overlap exists?* — has a Priority 0 answer.

### Per-item overlap verdict

- **A. Tallam (arXiv).** Adjacent at requirements-altitude. Names what the corpus refuses as **open problems** (R4 aggregation, Section 9.4 aggregation-inference-open, Semantic Intent Fragmentation empirical observation). Not a collision. Strongest contemporary candidate for cross-citation.
- **B. NCCoE concept paper.** Scoping-altitude RFI. Asks the questions the corpus's refusal kernels answer (aggregation sensitivity, agent's authority proof, tamper-proof action logs). Not a collision.
- **C. CAISI RFI.** Policy-posture-altitude RFI. Adjacent to witness-identity row via "separation of untrusted inputs from privileged actions"; does not formalize. Not a collision.
- **D. WEF/ACAP.** Practical-organizational-altitude playbook. Strongest single point of convergence on a specific refusal (ACAP non-additive rule ≈ SurfaceAuthorization standing-upgrade-block). "Agent passport" concept is the witness-substrate gap the corpus's BoundaryTransit + macaroons/Biscuit menu addresses. Not a collision.
- **E. NIST AI Agent Standards Initiative.** Programmatic-umbrella-altitude announcement. No technical content. Not a collision.

### Aggregate verdict (revised after codex pass 2026-06-04)

**Original draft said:** "Corpus refusal kernels survive Priority 0 intact. All five items operate at *higher* altitudes than the corpus. No item claims the negative-space territory."

**Codex correction:** the "altitude" framing was too clean and risked Claude common-mode re-stating "they didn't formalize it as a Lean theorem" as "they didn't refuse the inference." The honest revision:

**Revised aggregate verdict.** No Priority 0 item supplies kernel-style formal impossibility proofs; *several articulate overlapping negative rules at requirements / governance / playbook altitudes.* Tallam states prose-architectural refusals for boundary transit (R3), temporal staleness (R6), and authority accumulation under delegation. ACAP states governance-altitude refusals for non-additive multi-agent authority, component-certified-yet-collective-breach, AI-only oversight on critical boundaries, automatic update, and silent decommissioning. The corpus's distinctive object — *formal impossibility proofs of authority-conversion inferences + tested correspondence between Lean witness and production substrate* — survives Priority 0 intact. What does NOT survive is the cleaner claim that the corpus is "first to name" these negative rules. It is not. The corpus's contribution is *formal-proof altitude + substrate-correspondence testing*, not articulation-priority.

**The 7th bucket** (*Agentic-systems authorization 2026 convergence*) **earned its row** with a more accurate what-it-doesn't-refuse column: not "doesn't refuse delegation laundering" (Tallam articulates it; ACAP refuses one shape of it) but "doesn't supply kernel-style formal impossibility proofs, doesn't test Lean-witness-to-substrate correspondence, and doesn't operate at the inference-validity layer where forbidden conversions are mechanized refusals rather than policy choices."

**Strongest external-pitch alignment surfaced by the spike (unchanged):** **ACAP's "agent passport" concept** — explicitly named in the WEF playbook as a requirement without a cryptographic minting discipline, matching exactly the DeepSeek typed-provenance warning the corpus's positioning note already carries. The corpus's BoundaryTransit substrate menu (macaroons / Biscuit / SPKI) and the doctrine map's witness-identity row are the answers to a question the WEF/Capgemini working group has now publicly asked. **Cite-back opportunity** added in revision: ACAP's deployment-context tiers map to the corpus's CrossBoundary family as a deployment-topology taxonomy — convergence missed in the original draft.

### Forcing cases surfaced

No bucket-E (forcing-case-for-revisit) findings fire from Priority 0. Two **candidate** forcing cases are noted for later consumer-driven promotion, NOT opened here:

- **ContractionHinge formalization** — Tallam's Semantic Intent Fragmentation observation (71% success rate decomposing legitimate requests into individually benign subtasks) is an empirical instance of the corpus's spendability/multiplicity refusal. A coherent kernel may be developed before any downstream consumer; Tallam's observation supplies citable external pressure and a later correspondence target, not permission. This prior-art pass does not itself schedule the work.
- **BoundaryTransit substrate bridge** — ACAP's "agent passport" + Tallam's R2 (explicit/bounded/auditable delegation) jointly name the substrate gap that the corpus's macaroons/Biscuit/SPKI menu + Cedar's differential-randomized-testing methodology already supply the template for. *If* a downstream consumer earns BoundaryTransit's promotion from category-2 fenced scratch to category-1 wired, this is the forcing-case shape. Not opened here.

Both remain candidate and unscheduled by this prior-art pass; both are *named-now-so-the-recurrence-is-traceable* per the name-early discipline. Formal admission is governed independently by theorem shape, semantics, overlap, anti-vacuity, and proof controls.

### Status caveat (preserved)

The Priority 0 readings cover one slice of one session. The bulk of the queue (Priorities 1–4: Aura, PCA, ABLP, SecPAL, macaroons, Biscuit, SPKI/SDSI, linear credentials, Zanzibar, DKAL/NAL) remains `[unread]`. The map's existing six-bucket rows above still carry their conjectured cells. The 2026 convergence findings here do not retroactively witness the historical-prior-art cells — those still need their own readings. **Most dangerous remaining unread:** Aura (Jia et al., ICFP 2008) and PCA (Appel/Felten 1999) + proof-carrying authorization (Bauer et al.), per the existing read-queue Priority 1.

---

# Demand-side / evidentiary prior art (second half — added 2026-06-15)

## Why a second half

Everything above is **representation-side / access-control** prior art — *who may do or see what*. The recent arc (readout regress, synchronic standing vs diachronic maintenance, cultivation fraud, confidence-exceeds-jurisdiction) rhymes with a **different cluster the map never covered**: *what may be relied on, by whom, under what custody / freshness / readout conditions.* That the original map was overweight on the first side is itself the gap.

## The spine

> **Related work now has two orthogonal halves: representation-side authority logics and demand-side evidentiary / provenance logics. The admissibility kernel lives at their boundary: it does not replace either; it forbids unlicensed conversion between them.**

## Discipline (carries the same load as the map's status caveat)

- **Rhymes are admissible as heuristic, inadmissible as proof.** (The rubber glove for handling the Gödel crystals below.)
- A rhyme is **never a reduction** (meta-bridge guard). Each is a good analogy and a bad reduction.
- **Self-application — read this.** Every bucket below is asserted from training knowledge, **not** from reading the literature this session. By this map's own rule that makes each one *signed but not witnessed* — a claim-receipt formatted as an observation-receipt. All are `[unread]`; the "rhyme" and "gap" columns are **conjectured pending reading**. The map's discipline applied to its own second half.

## The map

| Bucket | What it represents | The rhyme (what's the SAME) — *conjectured* | Gap to find / port / divergence — *conjectured* |
|---|---|---|---|
| **Evidence law (US FRE + common-law evidence)** `[unread]` | Centuries-worked procedure for *what may be relied on*: relevance (401), authentication / "laying a foundation" (901), hearsay (802), chain of custody, best-evidence (1002), Article III standing, jurisdiction, forum-shopping, statute of limitations. | A fully-worked instance of the whole kernel: judge ≈ `MayReadout`, court's jurisdiction ≈ the root, **"laying a foundation"** ≈ *may be relied on*, hearsay ≈ testimony ⊬ fact, chain of custody ≈ custody, forum-shopping / limitations ≈ the cultivation / cliff layer. | **Vocabulary home + citation goldmine.** Divergence: FRE is *adversarial-procedural* (judge, trial, discretion, prejudice-balancing); the kernel is *mechanical / receipt-driven* — good analogy, **bad reduction** (no "legal realism cosplay in a compiler hat"). And do NOT let "`MayRely` = relevance+authentication+hearsay gate" *shrink* the kernel — `MayRely` also carries authority, clock basis, custody, consumer scope. |
| **Robust declassification / IFC** `[unread]` | Who may downgrade a label, and *robustness* (attacker can't influence what is declassified). Zdancewic–Myers "Robust Declassification"; Sabelfeld–Sands "Dimensions and Principles of Declassification" (what / who / where / **when**); qualified robustness; Goguen–Meseguer noninterference. | `MayReadout` ≈ declassification authority; the diachronic cultivation layer ≈ **robust declassification** (attacker shaping what becomes visible); the *when* dimension ≈ the Δt layer. | **Formal danger zone — most likely "you reinvented X" landmine.** Audit before any readout-paper. `CanRead ⊬ MayReadout` + cultivation = who may convert latent/substrate state into admissible public reliance, and whether an attacker shaped what becomes visible — i.e. qualified robustness. |
| **Supply-chain integrity / transparency logs** `[unread]` | Provenance attestation chains: SLSA levels, in-toto layouts, Sigstore (Fulcio / Rekor), TUF; transparency logs / Certificate Transparency (Laurie). | **Tightest operational rhyme, already shipping:** CT/Rekor's *signature ≠ inclusion-proof ≠ trust* = `signed ≠ witnessed ≠ relied-upon`; "trust the build, not the artifact" = cultivation / provenance-over-provenance. | Closest neighbor to the actual repo machinery. Port the attestation-chain structure for the diachronic fraud layer (`LocallyAdmissibleDoesNotDischargeTrajectory`). |
| **Argumentation & defeasible reasoning** `[unread]` | Dung abstract argumentation frameworks (attack graphs; **"admissible extension"** is Dung's technical term — near-namesake, check for `[collision]`); Pollock rebutting/undercutting defeaters; Reiter default logic; Toulmin model (claim / data / **warrant** / **backing** / rebuttal). | Contradiction-pressure + disqualifiers ≈ defeaters; "source graph lacks adversarial nodes" ≈ argumentation-framework completeness; Toulmin's **warrant / backing** = the corpus's exact words for what licenses an inference. | Non-monotonic machinery for "fresh fact revokes prior standing" already exists — **port, don't rebuild.** Flag the "admissible" namesake for a collision read. |
| **Jurisprudence + philosophy of authority** `[unread]` | Hart's *rule of recognition*; Kelsen's *Grundnorm* (presupposed basic norm); Raz's service conception — *theoretical (epistemic) vs practical authority*. | Root stipulation = rule of recognition / Grundnorm (accepted / socially recognized, **not derived**); "epistemic ≠ authority / confidence exceeds jurisdiction" = **Raz's theoretical-vs-practical authority, named**. | **The root-stipulation shelter** — the safe, non-physics home for *valid-under-a-declared-order*. Cite Hart / Kelsen / Raz; retire the Gödel temptation. The kernel refuses laundering *inside* a declared order; it does not adjudicate metaphysical legitimacy. Raz is the citation most needed. |
| **Foundations / epistemic regress** `[unread]` **`[NON-CLAUDE FLAG]`** | Agrippa's / Münchhausen trilemma (regress / circularity / dogmatic stop); Gödel 2nd incompleteness; Tarski undefinability of truth. | The readout regress is **Agrippa-level** (any chain needs a base case) — clean and safe. | **Radioactive. Negative-control ONLY:** *"this may superficially resemble incompleteness / self-certification, but our claim is a local admissibility / refusal result under a declared order, NOT Gödelian."* **Never** "Just as Gödel showed…". The honest level is **Agrippa, not Gödel** — Gödel is about what a formal system proves about its own consistency; the regress is "no base case ⇒ empty inductive." Claiming Gödel claims precision the result lacks. **The non-Claude flag is on the *characterization* (Agrippa-not-Gödel), and it survives co-signature:** Code + web Claudes both declined the overclaim, but that is two correlated emitters, not a witness. The flag survives any Claude blessing, including the one that wrote this row. |
| **Capability security (DIVERGENCE, not a rhyme)** `[unread]` | Object-capability model (Dennis–Van Horn; Mark Miller / E); *possession = authority by construction*; confused-deputy prevention. | — (this is where the corpus goes *against* the grain). | ocap deliberately **fuses** capability and authority; `CanRead ⊬ MayReadout` deliberately **keeps them separate**. Needs an explicit *divergence paragraph* in any readout write-up: "we model readout / reliance / admissibility, not invocation permission; ocap collapses a distinction our domain must keep." Pre-empts the "reinvented confused-deputy badly" objection. |
| **Epistemic & justification logics** `[unread]` | Hintikka `K_a` (factivity = the **T axiom** `Kφ→φ`, *not* the field; S5; doxastic = fallible belief); Artemov justification logic `t:φ` (explicit evidence terms — the signature made visible); dynamic epistemic logic (updates/announcements); AGM belief revision; **BAN authentication logics** (belief / freshness / jurisdiction / provenance); Halpern–Moses common knowledge. Plus the **warrant lattice**: analytic/synthetic (+ Quine), necessary/contingent, a priori/a posteriori, Kripke's necessary-a-posteriori. | The vocabulary home for `Claim<T>` typing — but each models an *attitude* toward φ (knows/believes/revises/justifies), the **believer's side of the door**. BAN's belief/freshness/jurisdiction/provenance triad is the tightest rhyme to the admission gate's fields. | **The field is the country; the gate is the border** — epistemic logic operates *after* admission, the gate *is* admission, and **none of it has a Refusal operator** (it assumes the problem away). **Halpern–Moses common-knowledge-unattainable is a ceiling theorem** (the Agrippa floor with a citation), not a tool. *Found the shelf ≠ handed the artifact:* registering a field is signed-not-witnessed re: whether the gate runs. Donates vocabulary (`K_a`, `t:φ`, freshness/jurisdiction); the missing verbs (admit/refuse/downgrade/scope/expire/supersede/quarantine/promote) are the build. See `admission-gate-claim-conversion-normal-form.md`. |

## Three to chase first (gap-closing priority)

1. **Robust declassification** — closest *formal* neighbor; the landmine most likely to contain a "you reinvented X."
2. **Supply-chain attestation** — closest *operational* neighbor; already half-built in the repo (`signed ≠ witnessed`).
3. **Evidence law** — closest *vocabulary* neighbor + highest citation value; cheapest to audit.

## Already mapped elsewhere (do not re-derive)

Access-control logics (the seven buckets above); sheaf / descent / global-section (the noncommutativity arc — descent is observer's house, home A only); Goodhart / Campbell (`negative-inclusivity` — cultivation *is* Goodhart at the evidence layer); quorum / BFT (`QuorumCustody`).

## Read queue addition (Priority 0b — evidentiary half)

Same posture as the existing queue: the map is route signage; the reading is the prevention. Order = Robust declassification → Supply-chain attestation → Evidence law → Argumentation/Toulmin → Hart/Kelsen/Raz. Foundations bucket is **not** a reading target — it is a refusal to import; its only "read" is a non-Claude check of the Agrippa-not-Gödel characterization before it appears in any paper.

## Provenance

Multi-model exchange, 2026-06-15, downstream of the readout / standing / cultivation arc. ChatGPT supplied the spine sentence and the don't-shrink-the-kernel / don't-overfit-FRE / Gödel-as-negative-control caveats; a Claude-web pass co-signed and contributed the Agrippa-not-Gödel refinement *and* the observation that its own co-signature does not discharge the non-Claude flag (two correlated emitters declining one overclaim ≠ a witness); Claude-Code assembled the rhyme map and flagged the Gödel reflex for a non-Claude in the first place. The discipline propagating to the Code instance — quarantining an item *for* a non-Claude — is itself the corpus's readout doctrine eating its own tail correctly: *signed is not witnessed*, applied to the act of recording.
