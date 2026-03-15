# Paper 18: Entrainment Control Model — Working Notes

## Status
Spec exists in agent_gov (`specs/core/ENTRAINMENT_CONTROL_MODEL.md`). Paper not yet drafted. `paper.md` is the raw multi-model conversation that generated the idea.

## Thesis (one sentence)
The problem is not influence alone; the problem is illegitimate promotion of transient influence into durable governing structure.

### Upgraded thesis (from recursive governance insight)
The promotion ceremony is not an implementation detail. It is a scale-invariant governance primitive: **proposal → evaluation → attestation → application → audit.** The same rule that prevents prompt/context from silently becoming policy also prevents policy/config from silently becoming constitution. This makes the paper's claim not "here's an architecture that resists capture" but **"here's a composable governance primitive for controlling when lower-tier state may acquire higher-tier legitimacy."**

Caution (ChatGPT): don't oversell the recursion as mystical. It's not fractals. It's just that once you define governance in terms of write authority across layers, the same enforcement shape reappears whenever one layer governs another. That's the architecture telling on itself.

## Core Decomposition
- a(t) = attention / salience / phase state (fast)
- m(t) = meaning / interpretation / reference state (medium)
- p(t) = policy / prior / controller state (slow)
- o(t) = observer integrity / self-diagnostic capacity (slow, system-wide consequences)

Mapped to authority tiers L0 (runtime) → L1 (context) → L2 (durable policy) → L3 (constitutional).

## Core triad
- Feed entrains phase.
- Propaganda entrains reference.
- Inculcation entrains the controller.

## Key invariants
- INV-001: Lower layers must not silently mutate higher layers
- INV-002: Repetition is not authorization
- INV-003: Context is not constitution
- INV-004: Observer integrity must remain auditable

## Series position
- Paper 17: who controls the update rules for belief?
- Paper 18: how do transient signals become update rules in the first place?
- This is the mechanism-of-capture paper. It explains HOW capture propagates across authority tiers.

## Series connections
- Paper 12/15: NLAI ("language proposes, evidence commits") = INV-001 (L0 cannot silently mutate L2/L3)
- Paper 16: capture regime = cross-layer contamination where L0 signals acquire L2 force via low-fidelity correlator
- Paper 17: propaganda attacks the policy layer; paper 18 formalizes WHICH layer and defines write barriers
- Book Ch 6-7: training layer + subtraction-as-legitimization = worked examples of cross-layer contamination and hysteretic lock-in

## Review feedback (ChatGPT + Claude Code + Claude papers)

### Agreed actionable (spec-level, some already applied)
1. Narrow scope opening — "governed adaptive systems" first, human/institutional mapping as extension
2. Sharpen observer — needs operational definition (contradiction sensitivity, source discrimination, update-path auditability), not just a name
3. Add `proposed_persistence` / `durability_class` to receipt schema — if persistence is the battlefield, the receipt must carry the persistence claim
4. Note in open questions that threat taxonomy mixes capture modes with dynamic consequences (T1-T3 = where capture lands; T4 = audit impairment; T6 = persistence property)

### Deferred to paper
5. Worked metrics examples (cross-layer gain, promotion legitimacy ratio, observer integrity in practice)
6. Worked attack scenario end-to-end: prompt injection → repeated context recurrence → attempted durable memory promotion → denied by write barrier → receipt emitted
7. Formal promotion model: allowed transitions, denied transitions, attested transitions

### Design caution (ChatGPT)
- Paper must stand alone. Don't lean on the series map as a crutch. Reader shouldn't need the cinematic universe.

## Later feedback (Gemini + ChatGPT, not in paper.md)

### Neuro-symbolic governor framing (Gemini)
- The governor is not a symbolic AI subsystem — it's a **typed border crossing** between L1 (statistical/narrative) and L2 (symbolic/durable)
- Semantic ADC: analog (statistical interpretation) → digital (typed claim with predicates and evidence refs)
- Promotion ceremony: the claim must cross a gate with explicit rules, not just accumulate weight
- Key vulnerability: **ontological spoofing** — relabeling to evade barriers ("archive with zero retention" skating past "delete" policy)

### 8-axis entrainment model (ChatGPT)
- Three buckets: WHERE (target layer, scope), HOW (mechanism, repetition pattern, observer impact), WHAT HAPPENS (persistence, reversibility, legitimacy)
- Axes should feel discovered from the model, not assembled from a list
- The architecture should force the axes, not the other way around

### Substrate-invariance confirmation
- The model applies to LLM agents, human cognition, and institutional governance with the same structure
- This is the same control problem at different substrates, not metaphor

## Artifact design (concrete implementation path)

### The minimal artifact set
1. **Spec doc** (`GOV_PROMOTION_BOUNDARY_001.md`) — layer model, allowed/denied transitions, persistence classes, scope classes, required evidence, barrier outcomes
2. **Claim schema** (`promotion_claim_v1.json`) — the typed object emitted when anything wants to cross from interpretation into policy/durable state. Key fields: `source_layer`, `target_layer`, `claimed_predicates` (with evidence refs), `requested_persistence` (durability class + TTL), `requested_scope`, `authority_basis`, `ambiguities`
3. **Decision schema** (`promotion_decision_v1.json`) — what the governor decided. Can allow, deny, or **downgrade** (e.g., durable → session). Records barrier evaluations and matched rule IDs
4. **Application receipt** (`state_application_receipt_v1.json`) — only emitted if something actually mutates. Separates proposed/approved/applied
5. **Barrier policy file** (`promotion_barriers.yaml`) — explicit rules per transition (L0→L1, L1→L2, L2→L3), with required evidence and default deny
6. **Gate module** (`promotion_gate.py`) — validate claim, normalize predicates, check barriers, emit decision, emit receipt if allowed

### Symbolic-AI-aware additions
- **Predicate trace**: which predicate, from what evidence, into what ontology term, with what unresolved ambiguity
- **Ontology mapping version**: `ontology_id`, `ontology_version`, `mapping_confidence`, `alias_candidates` (ontological spoofing defense)
- **Effect class**: `requested_action`, `effect_class`, `destructive_capability`, `privilege_required` (prevents relabeling attacks)

### First vertical slice
**Durable memory / preference promotion gate.** The LLM proposes preference updates, saved memory, routing defaults — but via typed claim, and the governor can allow/deny/downgrade/attach TTL/constrain scope. Enough to prove the whole architecture.

### Repo layout
```
governor/
  docs/specs/          GOV_PROMOTION_BOUNDARY_001.md, GOV_OBSERVER_INTEGRITY_001.md, GOV_EFFECT_CLASS_001.md
  schemas/             promotion_claim_v1.json, promotion_decision_v1.json, state_application_receipt_v1.json
  policies/            promotion_barriers.yaml, persistence_classes.yaml, scope_classes.yaml, effect_classes.yaml
  src/governor/        promotion_gate.py, predicate_normalizer.py, effect_class_resolver.py, observer_monitor.py
  tests/               test_promotion_gate.py, test_scope_downgrade.py, test_repetition_not_authorization.py, test_ontology_spoofing.py
```

### Recursive governance (ChatGPT + Claude Code)
**"The border policy is itself a border crossing."**

The barrier policy files are not config — they are L3 constitutional objects. If the architecture carefully governs L1→L2 but leaves the definition of L1→L2 ungoverned, you get the standard industry failure: carefully governed at the border, hilariously ungoverned at the place that defines the border.

**Fix:** split the artifact stack into two tiers:

**Ordinary governed artifacts** (runtime promotion):
- `promotion_claim_v1.json`
- `promotion_decision_v1.json`
- `state_application_receipt_v1.json`

**Constitutional artifacts** (doctrine updates — same three-phase split):
- `policy_update_claim_v1.json`
- `policy_update_decision_v1.json`
- `policy_application_receipt_v1.json`

Constitutional policy files (`promotion_barriers.yaml`, `persistence_classes.yaml`, `scope_classes.yaml`, `effect_classes.yaml`) each carry: `policy_id`, `policy_version`, `constitutional_tier`, `effective_date`, `previous_hash`, `attestation`, `rollback_policy`.

Repo layout:
```
policies/
  constitutional/
    promotion_barriers.yaml
    persistence_classes.yaml
    scope_classes.yaml
    effect_classes.yaml
```

This gives: governed runtime promotion + governed doctrine updates + no magical exempt layer where the real power hides. The self-similarity (same pattern at two levels) is a good architectural sign.

## Follow-on: "The System Beside the System" (Paper 19?)
Paper 18 = the breach (how illegitimate promotion works). Follow-on = the settlement (what accumulates when illegitimate promotion becomes normalized and starts functioning as parallel governance).

Core thesis: Systems are often not captured by direct violation of formal rules, but by the accumulation of shadow rules that gain durability and authority without legitimate promotion.

Arc: transient exception → repeated shortcut → precedent → tacit rule → shadow doctrine → parallel constitution. Nobody signs anything. Nobody announces a rewrite. The system just starts acting like the workaround was always law.

Key concepts worth keeping:
- **Ghost permissions**: permissions that don't exist in formal policy but reliably work in practice
- **Normalization-of-deviance ratchet**: utility debt trap (shadow path is faster), dependency entrenchment (other systems build on the hack), semantic erasure (institutional memory of the formal rule decays)
- **Negative-space auditing**: don't ask "what rules exist?" — ask "where did authority appear without a matching authorized path?"

Audit ideas (from Gemini, stripped of theatrics):
- Clean room differential: compare fresh instance against live one to detect de facto drift
- Semantic stress test: probe for alias-based bypasses (ontology-spoofing test harness)
- Provenance exhaustion: force every allowed action to show its authorizing path

## Literature positioning (ChatGPT research, March 2026)
- NIST GenAI profile (AI.600-1): broad voluntary risk-management, limited initial scope, not a promotion-boundary theory
- OWASP LLM Top 10: threat listing and mitigation guidance, not formal theory of which signals may become durable state
- OWASP MCP Top 10 (beta): names context spoofing, prompt-state manipulation, insecure memory refs, privilege escalation, shadow MCP servers — same neighborhood, but as a list not a primitive
- AgentSys (arXiv 2602.07398): isolated contexts, schema-validated return values, deterministic parsing at boundaries — same direction (explicit, typed, narrow boundary crossing)
- Anthropic system cards: prompt injection in agentic systems is acknowledged unsolved, but framed as better defenses/detectors, not yet as promotion-boundary discipline
- **Novelty claim**: most safety regimes are content/perimeter/compliance regimes. This is a state-promotion regime. The layer where temporary interpretation becomes durable authority is just now becoming legible.

## Broader implications (ChatGPT synthesis, worth keeping)
- **Safety reframe**: shifts from behavior policing to state-promotion governance. "What is allowed to become durable, under what authority, and with what audit trail?"
- **Observer integrity is central**: one of the main attacks is on the observer-controller boundary itself. System can become compromised in a way that also compromises its ability to report compromise. Implies need for independent witnesses, baseline references, external verification.
- **Symbolic/statistical division of labor**: statistical systems for generation and interpretation, symbolic/typed systems for promotion and admissibility. Not a GOFAI revival — a practical handoff design.
- **Governance = controlling what gets to stick**: not what gets said or done, but what gets to persist, broaden, authorize itself, and become the basis for future decisions.

## Plain-English pitches (for non-specialists)
- "I accidentally built a theory of unauthorized durability — how temporary influence gets smuggled into durable governing structure — and it seems to cash out as an actual governor design."
- "Most safety systems focus on bad outputs. This focuses on bad promotions — how runtime/context pressure turns into durable memory, policy, or doctrine."
- Compressed: "I accidentally reinvented epistemology as a firewall rule."

## Next steps (when ready)
1. Make observer operational (spec + paper)
2. Add persistence/durability tier to receipt model (spec, may already be done)
3. Write one worked attack path (paper)
4. Draft the paper from the spec + conversation, not the other way around
5. Sketch exact `promotion_claim_v1.json` shape for one narrow lane (durable preferences or memory)
6. Build the vertical slice gate in agent_gov
