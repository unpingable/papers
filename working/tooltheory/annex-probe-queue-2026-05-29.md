# Annex-probe queue — projection-erases-distinction family (2026-05-29)

**Status:** Park-state / next-steps capture for the bounded-Lean-annex queue. Filed end-of-session so a future session can pick up cold without re-deriving the calibration.

**Trigger:** `ConsequencePartition.lean` landed as scratch annex 2026-05-29 (green, ~410ms, not in `LeanProofs.lean`). Operator override of an over-conservative paper-Lean Claude read produced the calibration that this queue documents. Companion notes: [consequence-partition-candidate-2026-05-29.md](consequence-partition-candidate-2026-05-29.md), [projection-laundering.md](projection-laundering.md), [control-path-independence-candidate-2026-05-29.md](control-path-independence-candidate-2026-05-29.md). Memory: [[feedback-forcing-case]] §"Layer-of-application refinement (2026-05-29, ChatGPT pass)".

---

## The annex-probe test (the calibration)

A bounded scratch Lean annex is licensed — without a paper-side forcing case — when *all five* hold:

```text
compile probe is licensed when:
  audit exists                             (kernel-overlap audit, sibling family identified)
  shape is bounded                         (no Mathlib, no public surface, no new infrastructure)
  sketch is near-Lean                      (not vibes; multi-pass refined)
  build answers a real question            (does this have independent shape beyond known siblings?)
  public-surface promotion remains gated   (no `LeanProofs.lean` import, no preprint claim, no doctrine mint)
```

The compile is *contact*, not publication. Green says "the shape is coherent enough that future arguments don't have to be built from chat vapor and vibes." It does not say "this is doctrine now."

## The two-gate doctrine ladder

(Crystallized from chatty's read on the consequence-partition close.)

```text
candidate note   ≠ module
module           ≠ public surface
public surface   ≠ paper claim
paper claim      ≠ platform verdict
```

Each `≠` is a separate gate. Stops both failure modes seen this session:

- **Paper-Lean Claude over-braking:** "no forcing case, no build" — collapses `candidate note → module` even when the build is bounded and the audit is done.
- **Gemini theater:** "filled holes, therefore theorem / title / doctrine" — collapses `module → public surface → paper claim` by laundering an unused-hypothesis proof into a titled boundary theorem.

Hold the ladder. Each rung needs its own gate.

## The cross-altitude rhyme (the real keeper)

Labelwatch caught it; chatty generalized it:

> **Existence claim isn't evidence; the constructor has to carry the pair.**

Same geometry at every altitude:

| Altitude | Bad form (existence-only) | Good form (constructor carries the witness) |
|---|---|---|
| Lean kernel | `ObservedNonRefinement : Prop` | `ObservedNonRefinement` as `structure ... where` |
| Labelwatch metric | raw drop count (says how hard) | unique-DID count (says what failed to learn) |
| Storage telemetry | `wal_truncate_busy_events_since_apply: 0` ("drops solved") | actual discharged-event audit |
| Doctrine | "the platform collapsed a distinction" (assertion) | actual (left, right) pair the platform collapsed |

Evidence that cannot carry its own discriminating fields is a rumor with a schema. Apply this lens whenever a refusal artifact gets proposed.

## Queue order

### First probe: ProjectionLaundering — BUILT 2026-05-30

**Status:** `LeanProofs/Admissibility/ProjectionLaundering.lean` green, ~270ms, not in `LeanProofs.lean`. Two paired theorems plus four predicates, namespaced under `Admissibility.ProjectionLaundering`. Scratch posture preserved: no public-surface promotion, no doctrine mint, no preprint citation. Companion note [projection-laundering.md](projection-laundering.md) updated with §"Lean annex — built status (2026-05-30)" and amended park state.

The compile was contact, not publication. CBA still owns the public name; PL owns the kernel slot. PL/UC composition stays prose-only until a downstream consumer forces the citation.

**Position (original audit, preserved):** Confirmed by all three readers (me, labelwatch, chatty). Cleanest match to the annex-probe test.

- **Audit:** done in [projection-laundering.md](projection-laundering.md) §Overlap audit. CBA at vocabulary level, FiatAdmissibility at routing, sibling to SurfaceAuthorization / WitnessInvariance. PL/UC composition partner ([uncertainty-custody.md](uncertainty-custody.md)) named but not built.
- **Shape:** paired negative + positive theorems over abstract variable bindings (`Belief / Artifact / Action / MustDefer / Consequential / ArtifactSignalsDefer`). One-line proofs each. Both sketches in the note ready to drop into Lean.
- **Real question the build answers:** is the paired neg+pos a kernel, or prose wearing a lab coat? Green confirms the structure; red surfaces the gap.
- **Public-surface gating:** unchanged. PL/UC composition stays prose-only until a downstream consumer (NQ / Wicket / Governor) demands a citation.
- **Filename per the note:** `LeanProofs/Admissibility/ProjectionLaundering.lean`.

**Recommended pass:** same shape as CP — drop the two sketches in, run `lake build`, file an annex addendum if green, leave scratch (no `LeanProofs.lean` import). Update [projection-laundering.md](projection-laundering.md) §Lean reserve to point at the built annex; the note can still hold the doctrine.

### Conditional probe: ControlPathIndependence

**Position:** Valid candidate, different shape, gated on a scope-statement pass first.

- **Audit:** done in [control-path-independence-candidate-2026-05-29.md](control-path-independence-candidate-2026-05-29.md). Three-axis decomposition (independence / standing / coupling); only independence is decidable from architecture alone.
- **Shape:** larger than PL or CP. `Principal / Component / PathKind / Arch / ReachableBy / IndependentAt / InterlockBasis` — substantive inductive types, multiple definitions, an incompleteness-certificate discipline built into the kernel structure.
- **Real question the build answers:** does the path-reachability + InterlockBasis shape hold together? (Yes, plausibly.) It does **not** answer the harder question — whether the discharge boundary is set correctly (only `independent` discharged; `standing` and `coupled` deliberately undischarged with explicit obligations on the consumer).
- **Why scope-first:** without a written scope statement, a CPI compile probe risks drifting into "architecture linter with a proof core," which is a different artifact than a refusal-kernel slice. The annex-probe test passes only if the build answers a bounded question; here the bounded question needs articulation before the build.

**Recommended pass:** before any compile, write a one-page scope statement at the head of the CPI candidate note answering:
- What is the bounded question the compile probe answers?
- What is deliberately undischarged, and what carries the obligation?
- Where does this annex stop being a slice probe and start being an architecture linter (and is that boundary intentional)?

Once the scope statement holds, the compile probe is licensed. Same five-criterion test, same posture (scratch, not public surface).

### Third candidate (added 2026-05-30): Conductance hygiene fragment — BUILT 2026-05-30

**Status:** `LeanProofs/Admissibility/Conductance.lean` green, ~262ms, not in `LeanProofs.lean`. One `class Protocol` with five fields (one — `coordinationSignal` — declared but unused as load-bearing absence), three definitions, two paired theorems. Companion note [desynchronized-horizons-candidate-2026-05-30.md](desynchronized-horizons-candidate-2026-05-30.md) updated with §"Lean annex — built status (2026-05-30, same day)" and §"Build-surfaced finding: `failureSignal` cannot infer `Subsystem`."

**Build-surfaced finding (worth filing in the queue, not just the candidate note):** the relay's sketch called `Protocol.failureSignal sig` directly. Lean rejected — `failureSignal`'s signature only mentions `Signal`, so instance synthesis on `Protocol Subsystem Signal` can't determine `Subsystem` from arguments. Fix was local: explicit `@Protocol.failureSignal Subsystem Signal _ sig` at the two callsites. The honest structural fix is to **split the class** into a signal-side and a transport-side. Deferred per [[feedback-forcing-case]]; flagged so a future session does not re-derive.

This finding is a worked example of the queue's cross-altitude rhyme: *the constructor has to carry the pair.* Class field projections that don't reference both class parameters silently fail to carry the second one, making instance synthesis ambiguous. Same shape, new altitude. Filed.

**Position (original audit, preserved):** post-PL, post-CPI. Smaller than both. Audit partially done by relay. Bug pre-flagged.

- **Parent candidate:** [desynchronized-horizons-candidate-2026-05-30.md](desynchronized-horizons-candidate-2026-05-30.md). The Conductance fragment is the one Lean-ready residue from a broader prose stack (Local Carryability primitive + Recovery Graph machinery + Conductance operator layer + 5 candidate theorems). Overlap audit run 2026-05-30 confirms Conductance is the bounded first cut; reachability-insufficiency is candidate-after (gated on a CPI-shaped scope statement for bounded `Recoverable` definition); lock/articulation is no-op (graph-theoretic tautology); governor non-sovereignty is downstream-consumer-gated (build when `agent_gov` forces it).
- **Audit:** partial. Multi-model relay (DeepSeek + Claude-web + operator 2026-05-30) confirmed scope: this is the *contagion-hygiene lemma*, **not** the coordination/contagion separability theorem (`coordinationSignal` is declared but unused — load-bearing absence). Kernel-overlap audit against the existing safety-bridge / WitnessInvariance / SurfaceAuthorization family not yet run; relay's read suggests recovery-graph axis is distinct from projection-erases-distinction family.
- **Shape:** one `class Protocol` with five fields, three definitions, two theorems. **Smaller than CP.** No Mathlib.
- **Sketch is near-Lean:** literally a Lean file in the candidate note. **Bug pre-flagged:** `{src dst : Subsystem sig : Signal}` parses `Subsystem sig` as application; fix is `{src dst : Subsystem} {sig : Signal}`. Already applied in the candidate-note version.
- **Real question the build answers:** does the relay's pull-gated/passive-contagion shape hold up under Lean type-checking? Green confirms the hygiene lemma is a real artifact; red surfaces the gap.
- **Public-surface gating preserved:** unchanged. Doctrine promotion (separability, recovery-graph model, governor non-sovereignty) stays in prose.
- **Filename when built:** `~/git/lean/LeanProofs/Admissibility/Conductance.lean`.

**Why third, not second:** operator explicitly said PL/CPI is tomorrow's queue. Conductance joins behind. Smaller-than-CPI does not jump the line — explicit ordering wins.

### Fourth candidate (scope-pass spin-out, 2026-05-30): Reachability insufficiency

**Status:** Scope statement filed at [reachability-insufficiency-candidate-2026-05-30.md](reachability-insufficiency-candidate-2026-05-30.md). Compile probe **gated** on operator endorsement of the scope statement AND on resolution of four open shape questions surfaced during the pass (bridge axiom vs. hypothesis; per-source vs. per-pair quantification; per-clause negation split; conjunction vs. structure form). Per the audit, the candidate is the more *interesting* residue from desynchronized-horizons but the larger blast radius — same scope-first discipline as CPI, with more open shape decisions.

The candidate was spun out from [desynchronized-horizons-candidate-2026-05-30.md](desynchronized-horizons-candidate-2026-05-30.md) §Q2(b) / §Q7 into its own note so the per-candidate audit gate is honored; the doctrine source remains the desynchronized note.

Posture: same as CPI. The scope statement is the gate, not authorization to build.

### Fifth candidate (deferred): Governor non-sovereignty

**Status:** Per the desynchronized-horizons audit §Q3, the cleanest formal hook of the five candidate theorems, but **downstream-consumer-gated**. Build only when `agent_gov` ([[project-governor-doctrine]]) forces a citation. Graph theory does the structural work; admissibility-side content is the "admissible recovery paths" predicate which would be reused from the reachability-insufficiency annex once that one builds. No pre-emptive scope pass; the forcing case has to come from `agent_gov`.

Filed in the queue so a future session does not re-derive the deferral logic. Memory pointer: [[project-governor-doctrine]] *cite, don't extract*.

### Everything else: per-candidate audit, no sweep

The override fired for one specific shape (bounded probe, audit done, multi-pass refined, sketches near-Lean-ready). It does **not** license a sweep through tooltheory compiling everything sketched.

**Meta-warning** (chatty's phrasing, worth preserving verbatim):

> Don't let "green annex worked once" become "quick, formalize every raccoon footprint in tooltheory/." That's how annex becomes shadow-public-surface and then everyone pretends they don't know why the basement has governance.

Per-candidate posture for the rest of `working/tooltheory/`:

- **Most material is doctrine, registry, or substrate scouting** — not kernel-candidate shape. (Refusal-rebar-status, refusal-kernel-to-refusal-receipt-seam, internet-substrate-failure-map, regulatory-substrate-spike, register-capture-admissibility, etc.)
- **Already-built kernels stay built.** ConsolidationDenial.lean is public. No re-annex.
- **First-pass sketches are not eligible.** The criterion is *multi-pass refined* — single-model first pass doesn't earn the build. Annex-probe license depends on the audit having already done the work.

If a future session is tempted to compile something not on this queue, the right move is to write its own annex-probe test result against the five criteria, not to assume the calibration generalizes.

## Labelwatch's emitter-finding (relevant to ConsequencePartition, parked here for the queue)

Labelwatch reports `boundary_edges` table (schema v18) is **half-built as `ObservedNonRefinement`**:

```text
boundary_edges row    →  candidate ObservedNonRefinement
─────────────────────    ─────────────────────────────────
target_uri (shared)   →  collapsed (p left = p right)
divergent verdict     →  split (policy left ≠ policy right)
two edge observations →  left / right (S-valued, observed)
family version        →  (audit/versioning metadata)
```

**Chatty's tiny-but-load-bearing gap:** to become a *true* `ObservedNonRefinement`, the row has to bind:
- the exact projection `p` being tested (which platform projection, where it collapses)
- the exact policy/control being tested (user intent or comparison frame, not "different labels")

Otherwise the schema risks becoming "same post, different labels" — interesting, but not automatically "platform collapsed a distinction the policy needed." The mapping is probably one page, not a subsystem. Retrofit cost near-zero; name-early is paid.

**Cross-pointer Labelwatch identified:** the three trip-distinctions in the CP candidate note (state identity / effective consequence / collapse-point location) match the spine of Labelwatch's `BOUNDARY_PHASE2_SPEC.md` — "domain taxonomy" + "polarity model" + "JSD orthogonality filter." Same structural questions under different vocabulary. If/when the CP Lean wants a worked example, that spec is the bridge already partly walked. *Do not over-extract before the consumer asks.*

**Promotion forcing case (parked):** "any consumer wants `ObservedNonRefinement` as a structured deliverable." Until that arrives, the schema stays in `boundary_edges`, the typed handle stays in the Lean annex, the mapping page stays unwritten.

## Provenance

- **Session date:** 2026-05-29.
- **Three-reader convergence on queue ordering:**
  - Me (paper-Lean Claude this session): "PL clean match, CPI different-shape candidate, no sweep."
  - Labelwatch: "PL passes the same annex-probe test; CPI maybe passes but with more blast radius."
  - Chatty: "PL next if you want another bounded hit; CPI only after scope statement; everything else stays per-candidate."
- **Override origin:** [[feedback-forcing-case]] §"Layer-of-application refinement (2026-05-29, ChatGPT pass)" — codifies the public-doctrine-vs-scratch-annex split that licensed CP's compile and licenses this queue.

## Park state

> The audit was the gate. The compile was the receipt. The forcing case is still upstream.

Soak holds. Park state respected.

**2026-05-30 update:** PL annex built (green, scratch). CPI scope statement filed at head of candidate; compile probe gated on operator endorsement of the scope statement. Conductance annex built (green, scratch) with one build-surfaced shape finding (`failureSignal` cannot infer `Subsystem`; explicit `@` form used; class-split refactor deferred). Reachability-insufficiency scope pass pending (CPI-shaped, needs bounded `Recoverable` definition). Governor non-sovereignty deferred until `agent_gov` forces it. Everything else stays per-candidate.

PL ✓ · CPI scope ✓ (compile gated) · Conductance ✓ · Reachability-insufficiency scope ✓ (spun out, compile gated) · governor non-sovereignty deferred.

**Successor plan filed:** [recovery-topology-build-ladder-2026-05-30.md](recovery-topology-build-ladder-2026-05-30.md) — staged build ladder around `AdmissibleRecoveryPath`. Frames recovery topology as composition over existing admissibility under failure pressure, not a new sovereign primitive. Ladder gates each step on its own forcing case; reachability-insufficiency now sits as Artifact-1-prep-work inside that ladder. **Next session's right first move is the ladder's Step 7 Artifact 1 (the candidate note), not this queue's pending items.**

Anti-sweep posture honored: three compiles + one scope statement + one deferred is the *queue*, not a sweep. Each one passed its own annex-probe test or scope gate. The remaining items have their own gates upstream. The dangerous-amount-of-momentum kind, unfortunately. 🍻
