# Validator as bounded witness — the doctrine as executable architecture (CANDIDATE)

**Status: CANDIDATE working note. Named, not started. Mints nothing.** Records the
*find* and sorts it by the session's non-collapse rule; does not build a validator,
mint a kernel, or authorize a runtime. The runtime / NQ / AG instantiation is
**AG-claude / NQ-claude's lane** — cite, don't extract.

**Provenance:** 2026-06-27 multi-model pass after the WDC **1.4.0** release. Sorted, not
transcribed. (The nameplate "ChatGPT + Gemini + Claude" is the one *unwitnessed* claim in
a note about unwitnessed claims: this session repeatedly proved the relay can't reliably
say which instrument said what — model-attribution-signed is not model-attribution-
witnessed, the sibling of timestamp-signed-is-not-witnessed. Nothing here load-bears on the
attribution; the structure stands witnessed-against-the-surface regardless of who signed.) The version-attractor showed up cross-vendor
(Gemini wrote a 1.5/1.6/1.7 roadmap convinced it was a 2.0 roadmap), so everything below
is sorted by *does it change the calculus or carry it to the world*, not by enthusiasm.

## The find

**The generator/validator split is the corpus doctrine expressed as an executable
architecture** — not an application of it; the same object viewed from the other side.

- an **untrusted generator** (outside the TCB) emits a **certificate** = a *signed claim*
- a small **deterministic checker** performs the *witnessing*
- the checker's pass is the *receipt*; it **fails closed** on anything it cannot witness
- the generator stays outside the TCB because **proof-search is not authority** (a proof
  is evidence *into* a gate, never the receipt the gate emits)

Line them up: generator = signing party; checker = witness; no-negative-clearance =
fail-closed; proof-is-evidence-not-receipt = *why* the generator lives outside the TCB.
`validate : Policy → RuntimeFacts → WitnessCert → Except Error Derivation` with
`validate_sound` is DeferredWitness's lawful-completion crossed with the
proof-is-evidence fence, instantiated at the wire. The framework eats its own use case
again because it was *extracted from* these situations (27y ops; the dark-witness fossil
re-fire) and sharpened past intuition — so it recognizes them. Keep it grounded, not
myth: **production taught the failure mode; Lean forced the boundary to become checkable.**

## The tool-theory law

A validator is **not** an oracle, judge, agent, or operator. It is a **bounded witness
over a declared surface** — the *anti-agentic component*: a deliberate reduction of
agency at the boundary. It exists to stop a tool from laundering capability into authority.

```
Generators may be clever.
Checkers must be stupid.
Enforcers must be brutal.
Custody must be pedantic.
```

> A tool may propose transitions, but may not spend its own interpretation of authority.
> It must carry a bounded, replayable, witnessed derivation to a verifier whose authority
> is narrower than the generator's intelligence.

## The non-collapse table (the architecture in one table)

```
receipt exists        ≠ admissible
proof parses          ≠ proof checks
proof checks          ≠ action executed
action executed       ≠ action authorized
authorization passed  ≠ outcome witnessed
t_gen asserted        ≠ freshness witnessed
validator hash        ≠ validator authority
rule name             ≠ rule identity
deny                  ≠ predicate false
cannot_testify        ≠ pass
```

`cannot_testify` is the load-bearing verdict: failure-to-prove-P is not proof-of-¬P
(Γ⊬P **and** Γ⊬¬P). Enforcement may spend one bit (pass→allow, everything-else→deny);
custody must **not** collapse the reasons (malformed / stale / missing_witness /
wrong_rule / wrong_scope / predicate_false). Green dashboards are where evidence becomes
PowerPoint. This is **already NQ doctrine** (`located ≠ authorized`, the masking axis,
`cannot_testify`) — cite, don't re-mint.

## The runtime correction (don't hand the goblin root)

Do **not** put Lean-the-prover in the enforcement loop. Put a small **total compiled
checker**. Build-time: Lean proves the checker. Runtime: the checker validates a bounded
certificate against pinned rules. This is **Proof-Carrying Authorization** (Appel /
Felten / Bauer lineage). Enforcement = checking, not theorem-proving. FFI / line-rate /
Envoy / PAM is a *non-authoritative feasibility spike*, **not** a 2.0 gate — "compile to
C and link into prod" may move the mess closer to the blast radius, not shrink the TCB.

Immutable coordinates only (commit / content / artifact / image / rule-set digest).
Mutable pointers (`main`, `latest`, `v2-candidate`) are *reported context* with their own
resolution witness, never the target. **Rule name ≠ rule identity**: bind verdicts to
`(rule_set_digest, schema_digest, checker_digest, validator_id + signature)` — a hash
preserves bytes; a signature under declared authority establishes *who testified*.

## The frontier: witnessed clocks / temporal custody (candidate 2.0-class)

The gold, in one sentence:

> A freshness bound over a reported timestamp is not witnessed freshness; timestamp
> authority must itself be witnessed, or Δt validation launders time through assertion.

`t_gen` is attacker-controlled until witnessed ("born five seconds ago, Your Honor,"
over a fossil). The hard version isn't `t_eval − t_gen ≤ Δt_max` — it is *what does it
mean for a timestamp to carry witness authority rather than assertion, and what refuses
when it doesn't*: trusted clock? who supplied t_gen? monotonic vs wall? skew? replay?
does staleness **refuse / degrade / require re-witnessing**? Is the timestamp itself
witnessed or merely reported? **Timestamp-signed is not timestamp-witnessed.**

This connects the **Δt paper series** to the witnessed-derivation work at the seam
circled for months. It is **candidate 2.0-class** (per the frontier register's "What
Would Make This 2.0" gate): *if* solving it forces the derivation judgment to carry clock
authority as a first-class term, that is a breaking change to the calculus forced by
stronger math — a real 2.0. Filed in the Lean register next to confluence + cut.

## Sorted roadmap (named-not-started; each needs a coherent bounded claim and intrinsic scope/proof review)

Runtime forcing cases may prioritize an item, test its instantiation, or support public promotion. They are not admission tickets for formal development; a checked model or specification may lead the implementation.

> Operationalization is how the calculus meets the world; 2.0 is what changes the calculus.

- **1.5 — certificate validator.** Doctrine as executable boundary (`validate` +
  `validate_sound`). Frame as *the doctrine instantiated at the boundary*, **not**
  "serialize a Lean proof." The trusted thing is a small checker over a closed witness
  format, not "whatever proof-ish thing an agent invented."
- **1.6 — freshness-bound validation.** Δt policy / freshness-witness instance, as a
  *policy layer* over existing Freshness machinery, **not** a core-calculus rewrite.
- **1.7 — runtime adapter spike.** CLI / daemon / FFI, explicitly *non-authoritative*,
  no line-rate claims without measured receipts.
- **2.0 candidate** — witnessed clock / temporal custody (above), **or** structural
  normalization + cut-elimination, **or** resource-sensitive non-suppression. Reserved
  for a diff that changes what the calculus proves.

## Stress-test ordering (which domain breaks the schema first)

**Moderation breaks `ValidationTarget` first** — not noisy evidence but *ontological
instability*: subject, predicate, observer-standing, and rule-jurisdiction all disputed
at once. Cold-chain only stresses *observation* (is there a continuous witness?);
moderation stresses *ontology* (what would count as a witness, who may provide it, what
predicate it supports, what action it authorizes).

```
noisy evidence  breaks validators operationally
unstable predicates breaks validators ontologically
```

Honest scope: the validator does **not** make hard domains objective. It prevents systems
from laundering *contested* claims into *uncontested operational facts*. The math verifies
receipt structure + admissibility rules; it cannot make a predicate socially uncontested.

## The essay reframe (books layer — NOT a Lean claim)

Not "I formalized trust discourse." Rather: *here is what a trust boundary looks like when
someone who has had to enforce one by hand builds it precise enough to hand to a machine.*
DeferredWitness is the lede; the certificate architecture is the proof the doctrine *runs*;
the witnessed-clock theorem is where it gets harder. The intersection (ops scars + formal
chops) is empty because almost nobody stands in both — that is the moat, not the gap. Keep
grounded; resist the myth register.

## Fences

- **No build authorized here.** Names the finds; sorts them; mints nothing.
- The validator runtime + the non-collapse wiring is **NQ-claude / AG-claude's lane** —
  this corpus already owns `cannot_testify` / `located ≠ authorized` / masking. Cite the
  Governor doctrine; do not extract a new kernel.
- 1.5 / 1.6 / 1.7 are named-not-started *adapter* releases; **2.0 stays owed** until a
  frontier changes what the calculus *proves*.
