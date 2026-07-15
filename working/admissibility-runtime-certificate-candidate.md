# Admissibility runtime product — the denial certificate (CANDIDATE)

**Status:** CANDIDATE / non-binding. Captured 2026-06-30 alongside
[[maximal-calculus-tech-tree-candidate]] (`working/maximal-calculus-tech-tree-candidate.md`).
This note is the **practical payoff / runtime-product** layer; the calculus
mechanics themselves live in the tech-tree note + the incoming codex work (not
inspected). Provenance: Gemini's "five doors" enthusiasm, **corrected** by operator
+ web-Claude.

**Policy correction (2026-07-14):** the formal contract leads the code. A coherent `Formula`, theorem, countermodel, or checker specification may be developed before certificate fields or runtime consumers exist. Runtime fields and executable code instantiate that contract; they are not permission to state it. The genuine implementation dependency remains: an executable checker needs a concrete schema to check. Citation or adoption identifies an intended contract but does not establish conformance; conformance requires an explicit mapping plus runtime evidence or a refinement proof. Scratch cannot testify for or pin production, and public promotion remains separate.

## The reframe (the whole thing in one line)

> The runtime product is NOT "a sequent calculus." It is **a denial/authorization
> certificate whose proof object cannot smuggle authority.**

It stops being philosophy the moment derivations become **machine-checkable
receipts**. The practical value is not that Lean proves the thing — it's that the
system can say, deterministically and without LLM jazz hands:

> *"This failed because the witness did not carry spend authority."*

## The clean altitude stack

```
Lean theorem      : ordinary reachability does NOT imply resource executability
Runtime cert      : ordinary_reachable: true / resource_executable: false
                    / reason: missing linear bridge token
Operator report   : "The path is valid, but this actor lacks the warrant to cross it."
```

The load-bearing phrase, the whole product in four words:
**`ordinary_reachable: true, resource_executable: false`** — `global_not_implied_by_local`
in a work vest.

## STATUS — steps 1–3 LANDED (2026-06-30, codex; reviewed green)

**UPDATE 2026-06-30 (later same day, post-review — SUPERSEDES the custody labels
in the bullets just below):** the resource layer was **promoted SCRATCH → public
ANNEX**, and the certificate metadata gap was **closed by removal**.
- The scratch files `WitnessedResourceSequent.lean` / `WitnessedResourceChecker.lean`
  are **deleted**; their content is now public
  `~/git/lean/LeanProofs/Witnessed/ResourceSequent.lean` + `Witnessed/ResourceChecker.lean`
  (imported by `LeanProofs.lean`, i.e. real ANNEX surface). **Uncommitted in the
  lean repo — James commits.** The `Witnessed/Sequent.lean` bullet below is still
  accurate (it was already ANNEX).
- **`ResourceCertificate` was REMOVED from the public surface.** The masquerade
  *"cert datatype exists + `Checks` valid ⇒ cert is witnessed"* is now impossible on
  the public API: the witnessed object is the **`Checks` relation**, not a datatype.
  The unchecked data shape survives only as
  `~/git/lean/LeanProofs/Scratch/UncheckedResourceCertificate.lean` (SCRATCH; thin;
  reuses the public `ResourceFormula`, not a stale calculus twin). Re-admit only as a
  proof-carrying `ValidatedResourceCertificate` (a `Checks` proof rides along) or as
  executable Bool-checker data with a soundness/adequacy theorem. **This resolves
  POCKETED TODO #2 — by removal, not by wiring.**
- **Cut correction (web-Claude/Chatty overcorrected, then ate it):** the reachability
  `Sequent.lean` carries cut-*admissibility* only, but public `Witnessed/Formula.lean`
  has a **genuine positive-fragment `cut_elimination`** that eliminates a real
  `Deriv.cut` over an `∧/∨/⊤` grammar — ND-style, *mild* (no left rules, no
  principal-cut Hauptsatz machinery, `∨` is intro-only / inert). **NOT full Gentzen.**
  Resource-cut (step 8 below) is still untouched. Full accounting: reachability layer
  = cut-admissibility; positive-formula layer = genuine-but-mild cut-elimination; the
  AG-native scalp remains `reachable ≠ executable`, not the cut trophy.
- Provenance of the catch: import-graph audit surfaced that the reviewed scratch
  files had *public twins* nobody had opened; the metadata gap was real on the public
  surface, caught pre-commit. All green, `propext`-only.

**Custody fence on this capture:** *steps 1–3 landed* — NOT "the runtime layer is
implemented." What exists:
- `~/git/lean/LeanProofs/Witnessed/Sequent.lean` — **ANNEX / ordinary shadow /
  imported into the Witnessed aggregator.** Conservative over WDC; weakening free
  here (correct — it's the non-resource shadow); `cut_admissible` (the *safe*
  ordinary cut, NOT resource cut).
- `~/git/lean/LeanProofs/Scratch/WitnessedResourceSequent.lean` — **SCRATCH /
  fenced / NOT authority-bearing.** Three formula forms (claim/bridge/residue);
  linear `Split`/`Consumes`.
- **Projection chain is now theorem-backed:**
  `ResourceSequent --erase--> Sequent --empty context--> WDC Lift`
  (`erases_to_sequent` + `empty_iff_lift`). "Every layer forgets safely" is a
  theorem.
- **Strictness theorem exists:** `ordinary_reachability_not_resource_executability_without_token`
  = `ordinary_reachable ∧ ¬ resource_executable_without_token` (non-vacuous; rules
  out floor/hyp/bridge for *any* residual Δ).
- **Frame preservation exists in the correct carried form:** `weaken_prefix_admissible`
  (`extra ++ Γ → extra ++ Δ`, zero-axiom, the *only* way to add resources). Minor
  naming-fence: still has `weaken` substring; rename `frame_*` if promoted.
- **Certificate datatype exists but is METADATA ONLY** — `ResourceCertificate`
  (`applied` / `bridgeSpendDenied`). Not a witness, not a checker, not an
  authorization object; does not construct a `Derives` proof.

All green, full root build exit 0, axiom-classified (`propext`/zero-axiom; no
`sorryAx`/`choice`/`native_decide`).

**Step 4 (checker_v0) LANDED 2026-06-30 (green, sorry-free, axiom-classified
`propext`):** now public `~/git/lean/LeanProofs/Witnessed/ResourceChecker.lean`
(ANNEX; was `Scratch/WitnessedResourceChecker.lean`, since promoted). The witnessed
object is the **`Checks` relation** — a **position-pinned** (deterministic)
validation relation — NOT the cert datatype (that stays unchecked scratch; see the
UPDATE block above). `Checks` is sound+complete against `Derives`:
- `checks_sound : Checks K B Γ c Δ → Derives K B Γ c Δ` (validated cert IS a real
  derivation),
- `checks_complete : Derives → Checks` (rejects nothing derivable),
- `checks_iff_derives` (accepts **exactly** the derivable),
- `validated_denial_sound` (the checker correctly REFUSES the token-less crossing —
  `ordinary_reachable ∧ ¬resource_executable` at the checker level).

This also **resolves the `Split` non-determinism** (web-Claude's catch): consumption
is pinned by index via `removeAt`, with `removeAt_sound` / `split_to_removeAt`
proving position-pinning refines `Split`. The gate **checks** the named occurrence,
it does not **search** for a split. Scope fence: this is a Prop-level checker spec +
soundness/completeness; a **Bool-executable** checker (needs `DecidablePred K` /
`DecidableRel B` / `DecidableEq`) is the deliberately-deferred next step.

Cut-elim and resource-cut remain at step 8 (the ordinary `cut_admissible` is the
safe one; resource cut, the spend/residue-preserving landmine, is untouched).

## The jewel (web-Claude, 2026-06-30) — needs a NON-CLAUDE check before promotion

web-Claude flags `ordinary_reachability_not_resource_executability_without_token` as
the load-bearing result, **mis-shelved under "no-contraction specimen"**: it isn't
about contraction, it's a **validity-vs-executability separation** — `B c c'` is
valid (persistent relation) but *crossing* spends a distinct linear `bridge c c'`
token, so bridge-validity ≠ permission-to-cross. That's signed-is-not-witnessed at
the calculus level.

**FENCE: this is a Claude-to-Claude synthesis claim — common-mode risk.** The
factual half (it's grouped with no-contraction but is a different phenomenon) is
verified. The *novelty* half ("non-standard linear logic / this is the
contribution") I would NOT promote on.

### Jewel UPDATE — the adversary got relocated (web-Claude self-correction, 2026-06-30)

A partial non-Claude-style check (web-Claude turning the corpus's own tools on its
own citation) **moved the gate to the right door**:

- **Wrong citation: Garg–Pfenning `says` (GP06, non-interference).** `says` is a
  strong monad / lax modality (constructive S4 necessitation in the single-principal
  case) — *intuitionistic, structural, reusable, never consumed.* It buys
  validity-vs-**attribution** (`A true` vs *who vouches for A*) and is **silent on
  consumption.** Checking the bridge-token seam against GP06 is "a clean acquittal
  that doesn't testify" — the linear axis was never in the dock. A denial cert that
  looks witnessed and isn't (the corpus's own distinction, self-applied).
- **Right citation [UNVERIFIED — confirm against the actual paper, do NOT rely on
  Claude memory, mine or web-Claude's]:** Garg, Bauer, Bowers, Pfenning, Reiter,
  *A Linear Logic of Affirmation and Knowledge* (ESORICS 2006, LNCS 4189) — a modal
  enrichment of LINEAR logic built specifically for **consumable authorizations and
  resources.** If real as described, that IS this axis, occupied in 2006.
- **Therefore the novelty claim "consumable / one-use authority decoupled from
  validity" is DEAD** (~20 years old), and web-Claude's original "non-standard linear
  logic" framing was too broad and partly wrong.
- **Codex's instinct was right; its reason was sharper than stated.** Not "two
  Claudes agree, stop" but "the citation pointed at the wrong axis." The relocation
  is the value.

**The gate STAYS UP — but the question is now tighter** (and deliberately NOT closed
into a fresh novelty claim, which would just relocate the overclaim again). Carry
THIS into the codex/ChatGPT check, *with GBBPR actually in hand*:

> Does anything survive past GBBPR in (a) the decoupling of the crossing relation
> `B` from the spendable token, PLUS (b) the move where erasure to the non-linear
> membership layer is what *exposes* the over-permission — i.e. the strictness
> receipt read as **a separation between a calculus and its forgetful shadow**, not
> as "no contraction"?

Whether that's a contribution or "GBBPR wearing our vocabulary" is **not answerable
from any model's memory.** Two non-negotiables before promotion: (1) get GBBPR in
hand and read it; (2) run the surviving question past a genuinely non-Claude
reasoner. Until both: gated.

## Cheap captures DONE + pocketed TODOs (2026-06-30)

Done (in `WitnessedResourceSequent.lean` scope-fence prose):
- `Split` non-determinism flagged (existence judgment, not canonical consumption).
- Prior art cited: dual-context split (DILL, Barber–Plotkin), input/output residual
  (Hodas–Miller), persistent floor = `!`-zone / exponential (cite-not-rename —
  `floor` is established corpus vocabulary).

**POCKETED TODO (historical operator priority — do not lose the thread):**
1. **Rename the jewel** to name it load-bearing (validity-vs-executability), out of
   the no-contraction section — GATED on the non-Claude check above.
2. **`WitnessedResourceSequent` SCRATCH→ANNEX promotion. — ✅ RESOLVED 2026-06-30**
   (see UPDATE block at top of STATUS). The resource layer + checker are now public
   ANNEX (`Witnessed/ResourceSequent.lean` + `ResourceChecker.lean`), and the
   **blocker was cleared by *removing* the `ResourceCertificate` metadata types from
   the public surface** (not by wiring them to `Checks`) — the datatype now lives as
   unchecked scratch (`Scratch/UncheckedResourceCertificate.lean`). The calculus +
   checker promoted alone, exactly the "cut the metadata types" branch. Original
   framing retained below for provenance:
   > It's closer than typical (the conservativity tie-back `erases_to_sequent`
   > already exists). Lighter than the 7-gate public-ship ceremony, but still
   > custody-affecting. Route if pursued: un-fence the `LeanProofs.lean` import,
   > freeze names (`Split`/`Consumes`/`Derives`), confirm `#print axioms` stays ≤
   > `[propext, Quot.sound]`. **Blocker:** the `ResourceCertificate` metadata types —
   > ANNEX shouldn't carry types whose docstrings say "not the thing it resembles."
   > Now that `Checks`/`checks_sound` exist, either re-base the certificate on
   > `Checks` (finish it) or cut the metadata types and promote the calculus+checker
   > alone.

## The product path — short-circuits the theory tree

The runtime stack is NOT the full proof-theory tech-tree. It branches off **tree 1's
strictness slice** and ships, deliberately skipping cut-elim / process calculus /
maximal calculus:

```
Lean scratch calculus (strictness slice)
  → certificate datatype
  → deterministic checker (the dumb customs officer)
  → English explainer
  → negative corpus / adversarial cases
  → runtime gate integration
```

NOT `full proof theory → cut-elim → process calculus → runtime someday` — *that
path goes to grad school and never comes home.* **Verification engine first,
downstream barrier second.**

## The practical artifact to aim at

A denial certificate:
```json
{ "verdict": "refused",
  "reason": "bridge_validity_without_spend_token",
  "from": "c", "to": "c'",
  "bridge_valid": true,
  "required_token": "bridge(c,c')",
  "token_present": false,
  "ordinary_reachable": true,
  "resource_executable": false }
```
…with deterministic English: *"The claim is reachable in the ordinary WDC shadow,
but not executable in the resource calculus. The bridge relation validates the
path from c to c', but no linear bridge token was available to authorize the
crossing."* That sentence **is** the product.

## Gemini's five doors — operator-corrected

1. **Proof-to-English explainer — YES, first near-term win.** But do NOT invert
   arbitrary Lean proofs (`Prop` proofs are good theorems, bad durable runtime
   artifacts). Define a **certificate/receipt datatype PARALLEL to the proof
   relation**: `input_tokens / consumed_tokens / residual_tokens / rule_trace /
   denial_point / erasure_summary`. English rendering is then deterministic. (=
   signed-is-not-witnessed; generator/validator split, [[project-doctrine-as-executable-architecture]].)
2. **Cut-elimination as optimization — LATER, landmine.** "Optimization" must NOT
   mean "remove bureaucracy until the proof is pretty" — it must mean *normalize
   while preserving spend, residue, refusal, witness custody.* Otherwise cut-elim
   is **laundering with a math hat.** Only after the resource layer has
   preservation theorems strong enough to survive normalization.
3. **Compositional security gating — YES, the big systems prize.** `Split` becomes
   infrastructure law: A⊕B compose only if their token stores compose **without
   double-spend** (`ΓA ⊕ ΓB ⊢ boundary_claim ▷ Δ`). Neither alone authorizes;
   joint derivation consumes the right warrants; residue stays visible. This is how
   you stop *"the dashboard was green"* from becoming authority. Distributed
   localized boundary enforcement, not a monolithic gatekeeper.
4. **Synthetic adversarial generation (fuzzing) — HELL YES, the sleeper hit,**
   probably most immediately useful. Once there are small negative theorems,
   generate malformed witnesses **with names**: valid bridge relation / missing
   token; duplicated claim token; residue omitted; stale freshness; revoked warrant
   still presented; floor claim used as spend authority; ordinary-derivable but
   resource-nonderivable. A normal fuzzer says "input broke parsing"; this says
   *"this input tried to launder validity into spend"* — a far better bug class.
   (= [[project-laundering-move-watchlist]] made executable.)
5. **Type-theoretic runtime enforcement — YES, but Lean is NOT in the hot path
   first.** Lean proves the calculus/metatheory; runtime emits compact certificate
   data; a **tiny dumb checker** validates ("token present? consumed once? residue
   preserved? rule trace valid? projection checks out?"); Lean proves the checker
   sound (or audits its shape). Do NOT embed Lean / build a "minimal Lean kernel
   variant" in the gate — *that's a cathedral with latency.* The gatekeeper is a
   dumb little customs officer. Boring wins.

## The certificate schema must not self-collapse (the goblin's badge)

The Lean can be clean and the discipline still leak **at the wire** if the schema
collapses the distinct facts into one bit. The certificate needs the SAME split the
Lean file has:
```
bridge_valid:          true       NOT:   bridge:   ok
bridge_token_present:  false             decision: allowed
bridge_token_consumed: false
decision:              refused
```
`bridge: ok` is where the goblin puts on a badge. This is the **runtime form of the
Collapsed-vs-Residue non-collapse discipline** (`~/git/lean/LeanProofs/Scratch/ResidueCustodyNoncollapse.lean`'s
`collapsed_launders` vs distinct-field residue; SeamEdges' `EdgeDiscipline`): one
`authorized: Bool` launders every conversion for free; distinct fields keep each
seam refutable. *The wire format is a representation choice, and the collapsed
representation is the laundering one.*

## Fences (so the payoff doesn't relaunder the discipline)

- **Certificate ∥ proof, not certificate = inverted-proof.** The receipt is a
  separate durable datatype, not a pretty-printed `Prop`. (validator-as-bounded-witness,
  cf. recent WDC commits.)
- **No collapsed verdict field** — keep `bridge_valid` / `bridge_token_present` /
  `bridge_token_consumed` / `decision` separate; never a single `ok`/`allowed` bit.
- **Relative-to-declared, not spiritually clean.** A valid certificate means the
  action satisfies *the boundary rule encoded by the declared calculus and evidence
  model* — NOT that the infrastructure is absolutely safe. It kills a class of
  laundering bugs; the machines remain haunted. (= validity-under-declared-order;
  don't let the certificate oversell into a legitimacy claim, cf.
  `working/governance-kernel-scope-correction.md` — anti-laundering engine, not a
  legitimacy engine.)
- **Cut-elim must preserve custody**, never "simplify" away spend/residue/refusal.
- **Lean establishes the contract; runtime emits+checks its mapped implementation.**
  The formal layer may lead the code. Deployment remains the **AG / NQ lane**
  ([[feedback-ag-claude-drives-constellation]]), which must supply the schema mapping,
  runtime evidence, and production custody; citing the Lean result is not conformance.
- The certificate "cannot smuggle authority" is the **runtime form of the
  conservation / no-free-X theorem** (no_free_lift, the seam money theorem
  `global_not_implied_by_local`). Same invariant, now an emittable artifact.
- The English explainer is the runtime form of **refusal legibility** (Frontier
  Register #5: sound refusal → receiver-*usable* refusal).

## The gate CHECKS, it does not SEARCH

Sharpen "decidability at the gate": the gate must check a **finite certificate**,
not discover a proof. The verifier does NOT ask *"can I prove this action
admissible?"* (search); it asks *"does this supplied receipt type-check under the
small checker?"* (customs). Keep verification cheap and finite (O(n) type-check);
the calculus can be as rich as it likes *under the hood* as long as the gate only
ever checks. Search at the gate is how the customs officer becomes a theorem prover
with latency.

## The immediate next structural property: frame preservation (NOT weakening)

After the strictness slice, the next target is **frame preservation / carried
weakening** — and it is more immediately practical than cut. Cut says "I can
compose derivations"; frame says "I can compose derivations *without losing
everyone else's wallet.*"

NOT ordinary weakening (silently drops `Ω`):
```
Γ ⊢ c ▷ Δ
──────────────         BAD
Γ, Ω ⊢ c ▷ Δ
```
The admissible, frame-carrying form:
```
Γ ⊢ c ▷ Δ
────────────────       irrelevant resources carried through UNCHANGED
Ω ++ Γ ⊢ c ▷ Ω ++ Δ
```
Meaning: extra tokens do not block a derivation, are not consumed by accident, are
not erased, are not converted into authority — and subsystems can compose stores
**without double-spend.** This is the distributed-systems prize hiding in boring
list lemmas (it's what `Split`/compositional gating, door 3, rests on).

Theorem target (codex's to prove; recorded here as the dependency):
```lean
theorem frame_preserved (h : Derives K B Γ c Δ) :
    Derives K B (Ω ++ Γ) c (Ω ++ Δ)
```
**Naming fence:** `frame_left` / `frame_right` / `frame_append` — NOT `weakening`.
Future automation will abuse a field literally named `weakening` (names are little
demons with IDE support; = [[feedback-enum-regression-tell]] energy). The name must
carry the frame, or it lies.

## Runtime implementation order from here (not formalization permission)

```
1. strictness theorem    ordinary reachable ≠ resource executable
2. frame preservation    irrelevant resources carry through unchanged
3. certificate datatype  proof-adjacent runtime receipt (model the shape only)
4. checker               finite validation, NO proof search
5. explainer             deterministic English
6. fuzz corpus           malformed receipts / laundering attempts
7. runtime time/freshness integration after token accounting is stable
8. cut / process         separate formal lane; currently lower priority than the certificate path
```
Runtime freshness integration is deferred to 7 (it's just another way to make the
goblin radioactive before the box exists). A coherent freshness `Formula` and its
theorems may be developed earlier once the resource assumptions are explicit, and
may lead the field/schema design. Cut/process is a priority choice, not something
that waits for runtime certificates as permission.

## Certificate v0 fields (after strictness + frame land)

```
input_context / frame_context / consumed_token / output_context / rule_trace
ordinary_reachable / resource_executable / verdict / denial_reason
```
Checker v0 is finite and dumb: (1) verify each rule step; (2) consumed token
appears exactly where claimed; (3) residue/frame preservation holds; (4) no bridge
crossing without bridge token; (5) emit deterministic allow/refuse. NOT a checker
until the datatype is modeled first.

## Stack placement: nq observes, WDC accounts, AG enforces

Anti-laundering correction to the obvious three-tier read (Gemini's map, the
poisonous phrase fixed):

```
nq                = witness acquisition / substrate seismograph
                    emits OBSERVED RECEIPTS — "collector X observed Y at T under
                    method M" — it does NOT manufacture facts
sequent calculus  = admissibility accounting kernel (decides if receipts can
                    support an admissible derivation)
AG                = finite certificate checker + enforcement gate
```
NOT `nq = fact factory / calculus = truth engine / AG = proof-believer` — *that's
how the goblin gets a clipboard.* `nq` emitting receipts-not-facts is the same
no-silent-conversion-of-moss-into-evidence / `cannot_testify` / *located ≠
authorized* doctrine the corpus already owns ([[project-governor-doctrine]],
[[feedback-outofscope-no-jurisdiction-over-moss]]). The paper/Lean lane may establish
the contract first and lead the **AG/NQ** implementation. Deployment ownership,
runtime evidence, and conformance remain in the AG/NQ lane.

## Witness decay (runtime step 7; formal contract may lead)

Freshness is runtime-integration **step 7**, deferred until token accounting is
stable in the checker/explainer/fuzz path. That runtime priority does not block a
bounded `Fresh` formula, countermodel, or theorem from being developed first and
shaping the implementation.

**Decay revokes SPENDABILITY, not truth.** A derived sequent must NOT "look
different" because evidence is old. Old evidence stays historical evidence; it just
may no longer be admissible as a *freshness-bearing warrant*. Ten-second-old and
ten-millisecond-old both support the historical claim "collector observed
service_up at t0"; only the fresh one supports the action warrant
"service_up_fresh_enough_for_restart_gate." *Evidence doesn't rot into falsehood.
It rots into residue.* (Connects to [[project-commitment-standing-decay]] and the
synchronic/diachronic Readout arc — decay is operational revocation, not truth
loss.)

**Model it as a freshness TOKEN, not temporal logic** ("too much wizard robe").
KEY REUSE: codex's resource layer already has `residue` + `residue_preserved` and
the `Split`/`Consumes` machinery — `Fresh(o, now, max_age)` becomes a **fourth
formula form reusing that exact machinery**, NOT a new calculus. A rule requires a
freshness token present-and-valid to spend (derive claim from observation only if
`Fresh` present; cross bridge only if bridge token AND freshness token). Stale →
the same `bridgeSpendDenied` shape: `reason: "freshness_token_expired"` with
`observed_at` / `checked_at` / `max_age_ms`. **SCOPE-FENCE NOTE:** adding `Fresh` to
the `Formula` inductive is a deliberate scope expansion, not an autocomplete
constructor add ([[feedback-enum-regression-tell]]). It requires an explicit model,
theorem shape, overlap check, and proof/axiom audit; it does not require a runtime
forcing case.

**Invariant — freshness must NOT be ambient.** Bad: *now is global, so all
recent-ish observations are usable.* Good: *this derivation carries a bounded
freshness warrant for THIS observation, checked against THIS clock/source/window.*
"It was green recently" is the ops equivalent of `bridge_valid: true` — useful, not
authorization by itself. This is exactly the **witnessed-clock candidate-2.0**
already filed ([[project-doctrine-as-executable-architecture]]: *a freshness bound
over a reported timestamp is not witnessed freshness; timestamp-signed ≠
timestamp-witnessed; t_gen attacker-controlled until witnessed*). Practical policy:
nq observations carry `observed_at / collector_clock / source / method / ttl /
cannot_testify`; AG certs carry `checked_at / required_freshness / freshness_verdict
/ ordinary_reachable / resource_executable / denial_reason`.

**Δt is temporal ACCOUNTING, not temporal logic** — and that's the point, not an
oversight. The Δt series already had the accounting primitive (`Δt = checked_at −
observed_at` vs `max_age`); what was deferred is the proof-theoretic distinction
*historical witness remains true / fresh warrant expires.* The dangerous version
`old(observation) ⇒ false(observation)` is bad ops metaphysics; the right version is
*observation stays residue/history, `fresh(o, window)` may be absent, therefore the
action warrant cannot be spent.* He built the Geiger counter (accounting) before
admitting radiation exists (the logic) — i.e. he built the part that **prevents time
from becoming authority** first. That IS the corpus thesis applied to time.

**Contract-led ordering:** state the bounded freshness contract at the formal layer
first when its model is coherent — for example `Formula.fresh observation_id
max_age` plus the non-conversion theorem below — and let that contract determine
the runtime fields (`observed_at / checked_at / max_age_ms / age_ms /
freshness_token_present`). A fields-only spike may still explore serialization, but
it cannot testify for or constrain the theorem merely because code exists. No
forcing case is required to develop the formal contract; runtime adoption requires
an explicit correspondence mapping. Named theorem target, same shape as
strictness/bridge-validity:
```
freshness_validity_does_not_grant_spend
  telemetry_path_reachable:  true
  freshness_warrant_spendable: false
```

**Why freshness is step 7 (the real reason, not convenience):** temporal logic came
late because time was *too dangerous to admit before spend/residue existed*, not
because it was missing. Without the resource layer, freshness almost inevitably
launders into `recent_enough ⇒ authorized` / `stale ⇒ false` — both laundering
moves. Only now is the clean shape available: *observed_at stays history; Δt
determines freshness-warrant availability; the warrant gates spend; stale evidence
becomes residue, not falsehood.* Same skeleton, different goblin:
```
bridge_validity_without_spend_token
freshness_validity_without_spend_token
ordinary_reachable_but_not_resource_executable
```

**The keeper sentence:**
> **Freshness is a spend warrant over historical evidence, not a truth predicate
> over evidence.**

And the canonical one-liner: **time is just another X that does not convert to
authority for free.**

**Symmetric caveat — `checked_at` must NOT be ambient authority either.** The checker
cannot just say "now says no"; "current time" becoming the unexamined floor is a
*time goblin with a badge.* The clock is its own laundering surface, so the check
carries a declared clock-source receipt:
```json
{ "observed_at": "...", "checked_at": "...",
  "clock_source": "checker_monotonic_clock_v0",
  "max_age_ms": 10000, "age_ms": 12400,
  "freshness_warrant_present": false,
  "historical_observation_preserved": true,
  "reason": "freshness_token_expired" }
```
This is the witnessed-clock doctrine applied to BOTH ends — the observation's
timestamp AND the checker's clock need provenance (timestamp-signed ≠
timestamp-witnessed, both directions).

## Generalized thesis + external horizon (SPITBALL — not our lane)

The abstract statement of what this whole certificate program *is*:

> **Make permission prove itself before mutation.** Anywhere an actor wants a state
> transition in a low-trust environment, require a finite admissibility certificate
> before the transition occurs.

**Necessary demotion (the fence that keeps it honest):** it is NOT a universal
"bullshit filter." It is a **state-transition admissibility filter.** It cannot
prove someone isn't a weasel; it proves *this transition is/isn't licensed by the
declared premises, witnesses, warrants, and residue rules.* = validity-under-declared-order
again (`working/governance-kernel-scope-correction.md`) — proves admissibility under
declared rules, NOT cosmic truth, moral righteousness, or that the CFO isn't doing
CFO things.

**The four external domains are HORIZON, not roadmap.** The corpus stays in its
AG/NQ agent-governance lane; these are illustrations that the *same certificate
object* re-aims, not four projects to start:
- **Smart contracts / funds movement — best fit.** "proof gates code" vs "code is
  law." Caveat: oracle inputs are the goblin — "price feed says X" is an observed
  receipt with custody/freshness/spend, not truth.
- **Institutional governance — most aligned + the one worth (narrowly) doing.**
  Killer app is NOT "strip the wiggle room" (some discretion is the job) but *make
  the wiggle room explicit and signed as discretion, not hidden as procedure* — =
  the governance kernel forcing arbitrary power to sign its own name.
- **Media provenance — good, overstated by Gemini.** "proof doesn't resolve ⇒
  treated as synthetic" is WRONG; correct is *not admissible under the claimed
  provenance class.* **`not proven authentic ≠ proven fake`** — the SAME
  null-laundering shape the corpus already owns (missing ACK ≠ NACK,
  [[project-signal-authority]]; silence ≠ denial, AuthenticatedDenial). Refuse the
  claim, don't invent the opposite.
- **Financial markets — apt, politically radioactive.** Firm-internal pre-trade
  compliance certs before order release, NOT "the exchange type-checks every trade."

**Why it's one object, not four domains:** Gemini's "new applications" aren't new
doctrine — they're the corpus's existing invariants (declared-order relativity,
null-laundering, no-free-X) pointed at four places where low-trust state transitions
happen to live. The same refusal certificate serves all four:
```json
{ "requested_transition": "...", "ordinary_reachable": true,
  "resource_executable": false, "missing_warrant": "...",
  "residue_preserved": true, "decision": "refused" }
```
Portable kernel = one thesis + one object. The four domains remain horizon examples,
not public-promotion or deployment claims. Coherent bounded formal contracts may be
explored in Scratch; no citation or domain analogy establishes implementation
conformance.

## What this note is NOT
- Not the calculus itself (that's [[maximal-calculus-tech-tree-candidate]] + codex).
- Not evidence that a certificate, checker, or gate is promoted or conformant merely
  because its contract compiles.
- Not a runtime deployment claim. The formal contract may lead the AG/NQ gate; AG/NQ
  still owns implementation mapping, runtime evidence, and production effects.
