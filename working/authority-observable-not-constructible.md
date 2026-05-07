# Authority Observable, Not Constructible

**Status:** working note / cross-substrate doctrine. 2026-05-07.
**Scope:** doctrine and implementation note for the agent_gov / standing / receipt_kernel / Lean-Admissibility family. Not a manifesto, not an essay, not a paper.
**Stance:** candidate. Lab structurally complete (seven-probe gnat series, 2026-05-06 → 2026-05-07). Future probes require a specific missing axis or forcing case.

---

## Kernel thought

Authority should be **observable by consumers, not constructible by consumers.** An authority-typed value must come from a single sealed mint within its trust boundary; consumers may query the value (`is_authorized`, `is_denied`, `why_denied`) but may not fabricate it. Where the substrate cannot enforce structural sealing, the doctrine degrades to *anti-laundering*: unauthorized construction must require an explicit, reviewable boundary violation.

This is **not** a security claim in the cryptographic sense. The goal is that authority-shaped values cannot enter normal circulation as if they were earned. Same-process malicious forgery is out of scope. What is stopped is the value entering the system through a path that wasn't the mint.

## Final formulation

> **Claims are portable. Authority is local unless a border-crossing substrate preserves it and a verifier honors it.**

Less bumper-sticker than earlier versions, more correct. The single-sentence operational form:

> **Trusted values must be emitted by the substrate that earns them, not constructed by consumers from shape.**

Everything below is mechanism for enforcing the rule.

## Threat model

*Anti-laundering, not anti-forgery.* The doctrine does not solve:

- Theft of valid authority by a same-process attacker.
- Replay across sessions absent a runtime custodian or nonce discipline.
- Verifier bugs.
- Confused-deputy problems.
- Bad caveat semantics in cryptographic tokens.
- Revocation of issued credentials.

**Crypto-token caveat:** macaroons, signed JWTs, and biscuits preserve *integrity* across a wire. They do not solve any of the above. The bytes-survive-the-wire property is narrow. The cryptographic-verification row is one wire-boundary problem solved (integrity), not all of them; not a magic wand.

## The three disciplines

The doctrine decomposes into three orthogonal axes. No substrate enforces all three by itself.

- **Construction discipline** — *who may mint the trusted value?* Lives in the substrate's sealing mechanism (type system, package boundary, runtime custodian).
- **Spend discipline** — *can the value be copied, replayed, or consumed?* Lives in the substrate (sometimes type system as in Rust ownership; sometimes runtime custodian as in an Erlang server-held registry).
- **Serialization discipline** — *what survives boundary crossing, and how does a downstream verifier honor it?* Lives in the border-crossing technique chosen.

Independent failure modes. A substrate that handles construction but not spend (Ada/SPARK) is vulnerable to replay. A substrate that handles construction and spend but punts on serialization (Rust, Lean) is vulnerable to wire crossings. A technique that handles serialization (macaroons) without construction or spend discipline is just a signed receipt.

## The two-type split

- **Receipt** — descriptive audit artifact. Cloneable, inspectable, durable evidence of what was decided. Wire-safe by design (carries no capability).
- **Authority** — operational capability. Non-replicable where the substrate supports it, consumed by the act-on function.

> **Receipt is what you can copy. Authority is what you spend.**

The classic laundering path — *"audit artifact says authorized, therefore I can act"* — is structurally wrong. `apply` consumes the Authority, not the Receipt. The receipt can say whatever the receipt says; what makes the action legitimate is that the Authority was minted by the decision function and is being spent (not replayed) by this specific call.

## Vocabulary lock

The probes surfaced enough adjacent vocabulary that drift is a real risk. Lock these six terms:

| Term | Meaning |
|---|---|
| **Observation** | raw input — the thing the system sees |
| **Testimony** | witness-emitted claim about an observation (oracle log, tool trace, model self-report) |
| **Receipt** | copyable audit artifact; records what was decided; wire-safe by design |
| **Claim** | portable shape or statement requiring validation before use; anything that crossed a wire is a claim until honored |
| **Authority** | local operational capability; non-replicable where substrate supports it; consumed by `apply` |
| **Token** | serialized bearer representation of authority; honored only after verification |

**Receipts and Tokens *can* serialize identically by shape; only the verification protocol distinguishes them.** That is the core slipperiness this terminology is locking down.

## In-process substrates (construction + spend discipline)

> *Inside one trust boundary, what prevents unauthorized construction or replay?*

| Substrate | Examples | Mechanism | What it prevents |
|---|---|---|---|
| **Structural** | Ada (`type Outcome is private`); Rust (private field + crate-internal `pub fn`); Lean (opaque types) | Type system refuses unsanctioned construction | Construction through normal language use |
| **Ownership** *(adds to Structural)* | Rust: no `Clone`, no `Copy`, consumed by move | Affine types | Replication, replay, double-spend |
| **Dynamic** | Python (`_underscore`); Common Lisp (`package::internal-symbol`) | Module/package boundary as visible-violation marker | Invisible laundering — violation becomes grep-able |
| **Structural / JSON** | TypeScript (branded types via `unique symbol`) | Compile-time brand on shape | Object-literal forgery only — `as Authority` cast is a visible violation; **JSON erases the brand entirely** |
| **Process-capability** | Erlang/BEAM (server-held registry, `make_ref/0`) | Live custodian process owns the registry; runtime enforces process isolation | Construction (refs unforgeable) AND replication (registry consumes ref on apply). Strongest in-process substrate observed. |
| **Deductive** *(negative baseline)* | Prolog | None by default — terms unify by shape; `assertz` / `retract` make the database the laundering surface | Nothing — the unsealed-baseline reference. Datalog without `assertz` / `retract` would seal strictly more. |

**Anti-tier (a trap, not a substrate):** pure protocol tricks — closure-callback handshakes, token capabilities with no language-level structure. Look like sealing and aren't, because a stateful adversary can simulate the conversation shape without holding the secret. Demonstrated in the Common Lisp probe, where a counter-fake defeated double-test by returning expected protocol responses without ever holding the mint. Use only as defence-in-depth atop a real substrate.

## Border-crossing techniques (serialization discipline)

> *Once the value becomes bytes, what lets a downstream verifier honor it without being fooled by shape?*

| Technique | Mechanism | Examples |
|---|---|---|
| **Re-mint after validation** | Verifier inside the local trust boundary checks the claim, then issues a fresh local Authority via the local mint | TypeScript `validate()` + reconstruct; pydantic-style validation in Python |
| **Cryptographic verification** | Bytes carry HMAC or signature; verifier holds the corresponding secret; verification = HMAC / signature check (and caveat evaluation, where supported) | Macaroons and biscuits (with attenuation); signed JWTs for the integrity-only case (attenuation requires extra machinery) |
| **Runtime/session trust establishment** | Distributed runtime or session negotiates trust at the boundary; mechanisms vary (symmetric secret, mutual TLS, session keys) | Erlang distribution cookies (weak); mTLS service-to-service (stronger) |

These are *techniques*, not substrates. Each can be applied within any in-process substrate that produces bytes-shaped output. Macaroons in particular are not another substrate row — they are a wire-survival technique. The bytes survive serialization with cryptographic integrity, but verification still requires a verifier-side root key. The wire-boundary still exists; it has shifted from a re-mint boundary to a crypto-verify boundary.

## Sub-rules

- **Frozen is not sealed.** `@dataclass(frozen=True)` prevents mutation after construction; it does not prevent construction.
- **A theorem about valid authority is not a construction rule for authority.** Validity theorems catch malformed reasoning *after* the value exists; construction discipline prevents the value existing without a mint. Different failure class — both are needed.
- **In substrates without structural sealing, construction discipline degrades into violation visibility.** The doctrine does not require unforgeability; it requires that laundering authority demand an explicit, reviewable boundary violation.
- **Branding ergonomics affect whether the seal exists.** *(TypeScript-specific.)* A `[unique_symbol]: never` index-signature brand is vacuously satisfied and silently fails. A regular `__brand: typeof unique_symbol` property brand seals correctly. Get the idiom wrong in a structural-typing language and you have a phantom seal that thinks it's working.
- **Non-replicability can be enforced by a live custodian, not only by ownership types.** *(Erlang-specific.)* A server holding a registry can revoke an Authority's spendability after first apply, achieving the Rust-Ownership invariant without affine types — at the cost of needing a live process. Rust-brain easily over-fits "non-replicability is a property of the value"; Erlang shows it can be a property of a live custodian.
- **Authority-as-resolution is useful, but the database is the laundering surface.** *(Prolog-specific.)* When authority is derived rather than constructed, sealing requires controlling what facts can enter the database. Static (Datalog-style) sealing is real; dynamic-database (Prolog with `assertz`) is not.
- **Attenuation works key-less; broadening does not.** *(Macaroon-specific.)* A holder can narrow a macaroon (add caveats) without holding the root key; the narrowed macaroon still verifies. Broadening requires the root key. Unique to cryptographic-token techniques.
- **Once serialized, a token is no longer automatically a capability.** It is a claim unless honored by a valid border-crossing technique.
- **Trusted values must be emitted by the substrate that earns them, not constructed by consumers from shape.** The doctrine in one sentence; everything above is mechanism.

## Probe data

Seven probes in `~/git/gnat/<lang>`, in order:

| Date | Substrate | Result |
|---|---|---|
| 2026-05-06 | Ada/SPARK (`standing_spark`) | Originated **Structural** row. `type Outcome is private` enforces construction discipline at type level. Diff against `~/git/agent_gov` confirmed real laundering vector: `StandingReceipt` is `frozen=True` but freely constructible; `AuthorizationVerdict` had no minter at all. |
| 2026-05-07 | Common Lisp (`lisp`) | Originated **Dynamic** row + **Anti-tier** trap. Closure-with-captured-gensym defeated by stateful counter-fake; package-internal constructor (`::` ceremony) seals via visible-violation marker. |
| 2026-05-07 | Rust (`rust`) | Originated **Ownership** row. Receipt/Authority split made physical via `Clone`/`Copy` derive presence. `compile_fail` doctests verified: cannot construct directly, cannot clone, cannot apply twice (use-after-move). |
| 2026-05-07 | TypeScript (`typescript`) | Originated **Structural/JSON** row + **re-mint after validation** technique. Object-literal forgery blocked at compile time; `as Authority` cast is a visible violation; JSON round-trip strips the brand entirely. Surfaced the brand-ergonomics trap. |
| 2026-05-07 | Prolog (`prolog`) | Originated **Deductive** negative-baseline row. Four forgeries succeeded: term fabrication, `assertz` on dynamic state, module-qualified call to private predicates, hypothetical input-fact assertion. |
| 2026-05-07 | Erlang (`erlang`) | Originated **Process-capability** row. Four forgeries blocked correctly. Server-held registry consumes refs on apply, enforcing non-replicability via a live custodian rather than affine types. Strongest in-process substrate observed. |
| 2026-05-07 | Macaroons (`macaroons`) | Originated **Cryptographic verification** technique. Bytes survive the wire with HMAC integrity; verification still requires verifier-side root key. Bonus: third-party attenuation works without root key (narrow only, not broaden). **This probe forced the framework correction from a single-table substrate ranking to the two-dimensional model.** |

## Stop condition

> **Lab structurally complete as of 2026-05-07. Future probes require a specific missing axis or forcing case.**

The matrix has six in-process substrate rows and three border-crossing techniques. That is enough resolution to write the doctrine and to evaluate concrete implementations against it. *"What about Haskell?"* without a specific question is not a forcing case; it is a polite scarf at the window. Capability-native languages (E, Pony) are answer-keys, not probes — they would mostly produce confirmation rather than surprises.

## Operational checklist

When adding a trusted value to a system, work through:

1. **What downstream reliance does it trigger?** Mutation? Logging? Decision input? Authority delegation?
2. **Who mints it?** Single source or multiple?
3. **Can consumers construct it?** What is the substrate's enforcement, and what is the visible-violation marker if any?
4. **Can it be copied or replayed?** Where is non-replicability enforced — type system, runtime custodian, both, or not at all?
5. **What happens when it crosses serialization?** Does it become a Receipt or a Token? (Same bytes, different verification protocol.)
6. **If it crosses a wire, is it re-minted, verified, or merely shape-accepted?** Shape-accepted is the failure mode.
7. **What is the explicit degradation mode?** When sealing fails — cast, JSON erasure, `assertz`, lost key, expired caveat — what is the visible-or-invisible thing that goes wrong, and how is it caught?

The doctrine in operational form: a checklist, not a slogan.

## Connection to existing constellation

- **Authority + StateTransition + Derivation + Execution + Corrective Lean kernel** (`~/git/lean/LeanProofs/Admissibility/`): clean instance of construction discipline isolated from the other two axes. `AuthorityVerdict` derives `DecidableEq, Repr` — the Receipt half. `AuthorizedStep` derives nothing and is consumed by `executeIfAllowed` against proof obligations — the Authority half. The split is structurally present in the kernel today; this doctrine adds vocabulary, not new structure. Spend discipline (replay) and serialization discipline (re-derive `StepAllowed` on the receiving side) are *not* covered by the Lean kernel; an executor that pickles state across processes must add them. Lean's consumption is propositional, not affine — the Erlang-shaped registry is the right pattern for an executor, not the Rust-shaped move.
- **`working/accountable-mutation-os-layer.md`** (construction-discipline addendum, 2026-05-06 late): the proto-doctrine. Surfaced the validity-vs-construction distinction, named the **Sealed Outcome Boundary**, articulated the four-move framing. This writeup is the cross-substrate cash-out of that addendum.
- **`working/breach-mistaken-for-authorization.md`**: sibling primitive on the historical-failure axis. The construction-discipline doctrine is the structural anti-pattern; breach-as-authorization is what happens when consumers discover they can construct authority by precedent and the system has no native vocabulary to refuse the move.
- **agent_gov / standing / receipt_kernel** (Python): the family this doctrine is for. The Ada probe surfaced a real laundering vector — `StandingReceipt` is `frozen=True` but freely constructible; `AuthorizationVerdict` had no minter at all. The receipt_kernel attestation layer is intentionally open-construction (a fake PASS is an attestation-integrity problem, not a construction-discipline problem); the agent_gov / standing mint layer is what needs sealing. Conflating the two layers was an early framing error this doctrine prevents.

## Falsifier

This doctrine is **empty** if its substrate-tier predictions reduce cleanly to existing security-engineering vocabularies — capability theory, taint tracking, information-flow control, ocap.

Bite test: does the two-axis decomposition (in-process × border-crossing) distinguish failure modes those vocabularies blur?

Candidate distinguishing claims (held, not promoted):

- **Substrates differ on which axes they cover.** Capability theory describes the structural-sealing column but does not natively distinguish ownership-spend from custodian-spend. The three-axis decomposition is sharper than "this language has capabilities."
- **Anti-tier traps are observable in the wild.** Closure-callback protocols look like sealing and are not; many Python and JavaScript "capability" libraries are Tier-4 traps under the hood. The Lisp probe surfaced this with a stateful counter-fake.
- **The crypto-vs-substrate distinction is a category error to flatten.** Macaroons vs. Rust ownership are not points on a "how secure" spectrum; they answer different questions on different axes. The two-axis matrix prevents the conflation; capability-theoretic vocabulary does not natively distinguish them.

If the predictions reduce cleanly to existing vocabularies under those constraints, the doctrine retires.

## Forcing case (not yet)

Per three-term vocabulary (forcing case / default future work / prewarmed branch): **prewarmed branch**, not forcing case. Lab structurally complete; doctrine candidate; further probes are entertainment unless the matrix is forced to grow.

Candidate forcing-case-shaped material:

- A concrete laundering path in agent_gov / standing / receipt_kernel that the substrate-table column-checks would have caught and the existing implementation didn't.
- A proposed implementation choice (e.g., the Rust `~/git/standing` mint) where Structural+Ownership combination needs to be specified against the doctrine's column-by-column rules.
- A wire-crossing case where re-mint-after-validation is wrong and cryptographic-verification is required (untrusted intermediary, attenuation needs).
- A new substrate that tests an unobserved axis — genuinely capability-native langs like E or Pony, but only if a specific question motivates the probe.

## Writeup seeds (for future essay, not now)

Two phrasings, depending on audience:

- **Substrate-agnostic spec** (the Final formulation above): *Claims are portable. Authority is local unless a border-crossing substrate preserves it and a verifier honors it.*
- **Essay hook** (for a wider audience): *The question is not whether a language has types. The question is what kind of lie the substrate makes easy.*

The first is for a spec; the second is for an essay. Both are quotable; neither is to be edited without preserving the structural claim. Essay version is queued for after this note has cooled.

## Provenance

- **2026-05-06.** Ada/SPARK probe (`~/git/gnat/standing_spark`) surfaced the validity-vs-construction distinction. Construction-discipline addendum filed in `working/accountable-mutation-os-layer.md` (lines 194-270). **Sealed Outcome Boundary** named.
- **2026-05-07.** Six-probe day: Common Lisp (Tier-4 trap; visible-violation principle named), Rust (Receipt/Authority split made physical), TypeScript (re-mint-after-validation technique named, brand-ergonomics trap), Prolog (deductive negative baseline), Erlang (process-capability row, live-custodian non-replicability), Macaroons (cryptographic-verification technique, **framework correction** from one-table to two-axis).
- **Multi-model conversation lineage:** ag_claude (Ada validation, agent_gov diff against construction-discipline rules), gnat_claude (probes, doctrine file maintenance), chatty (framework correction to two-axis split, terminology lock, threat-model and crypto-token caveats, stop condition, operational checklist, writeup-seed phrasings, scope discipline), claude-code-papers (Lean-kernel mapping, this writeup).
- **Lab in the jar 2026-05-07.** Local caveat in `~/.claude/projects/-home-jbeck-git-papers/memory/project-authority-kernel.md` updated to match the matured framework. Doctrine memory note in gnat-claude register at `~/.claude/projects/-home-jbeck-git-gnat/memory/doctrine_authority_observable_not_constructible.md`. This file is the repo-public artifact.
- Filed as working note, not paper, not P28. Repo-public doctrine; substrate-agnostic at the top level; portable to a future cross-repo doctrine artifact when the destination shape stabilizes.
