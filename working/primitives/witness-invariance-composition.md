# Witness Invariance — Composition (probe)

**Status:** probe / extension note. **Not a new primitive.** Extends the parent primitive [Witness Invariance Failure](witness-invariance-failure.md) from single-witness qualification to multi-witness composition. Does not promote WIF; does not enter the Active primitive notes table; does not claim a general aggregation theory.
**Originated:** 2026-05-09 (multi-model: ChatGPT composition skeleton + four-lemma sketch + operator-override on audit-paralysis; claude-code-papers tightening; user emphasis on *audited* as load-bearing word).
**Parent:** WIF establishes the single-witness boundary — *sensitivity is not independence; encapsulation is invariance under declared excluded perturbations.* This file asks the next question.

## Scope

**Question.** When does a set of individually limited witnesses compose into admissible testimony?

**Answer (the seed claim, two-route form).** Sometimes — but only at the aggregate boundary, and through one of two distinct routes:

- **Corroborative composition.** Witnesses' agreement counts as evidence only when their failure surfaces have been independently audited. *Agreement is not corroboration unless the witnesses fail independently.*
- **Aggregate-invariance composition.** The aggregate $A \circ (w_1, \ldots, w_n)$ is admissible when *the aggregator itself* is invariant under admitted perturbations — through cancellation, thresholding, or insensitivity to component movement — even if no individual witness is clean. *A passed aggregate proves the aggregate. It does not promote its components.*

The two routes have different requirements. Corroboration requires audited failure-surface orthogonality. Aggregate-invariance does not. Both share Lemma 4: cleanliness belongs to the composition, never retroactively to the components.

**Out of scope.** This is not a general theory of aggregation, ensemble methods, or Bayesian combination. It does not specify *how* the audit step is performed. It does not extend to witnesses with different target signals (the *target-alignment map* is named below as future bridge, not built). It does not promote WIF.

## Formal-ish shape

Following the WIF parent's typed form: each witness sees a target signal and a contamination basis.

Let each witness be:

$$w_i : B \times D_i \to O_i$$

where:

- $B$ = admitted basis (the target signal the witness is sensitive to)
- $D_i$ = contamination basis (the excluded perturbation surface witness $i$ is supposed to be invariant under)
- $O_i$ = witness output

Let an aggregator be:

$$A : O_1 \times \cdots \times O_n \to Y$$

The aggregate witness is:

$$W_A(b, d_1, \ldots, d_n) = A\bigl(w_1(b, d_1), \ldots, w_n(b, d_n)\bigr)$$

Aggregate encapsulation under relation $R$ (the admissibility-relevant perturbation) holds iff:

$$\forall b, \mathbf{d}_1, \mathbf{d}_2.\ R(\mathbf{d}_1, \mathbf{d}_2) \Rightarrow W_A(b, \mathbf{d}_1) = W_A(b, \mathbf{d}_2)$$

The **load-bearing object** is therefore $A \circ (w_1, \ldots, w_n)$, not any individual $w_i$.

### Common-environment refinement

Set-disjointness $D_i \cap D_j = \emptyset$ is awkward when contamination bases live in different spaces. To compare witnesses under shared perturbations — required for the audit step — introduce a latent environmental perturbation space $E$ with projections $\pi_i : E \to D_i$. Each witness becomes $w_i(b, \pi_i(e))$, the aggregate becomes:

$$W_A(b, e) = A\bigl(w_1(b, \pi_1 e), \ldots, w_n(b, \pi_n e)\bigr)$$

and aggregate encapsulation under a relation $R$ on $E$ is:

$$\forall b, e, e'.\ R(e, e') \Rightarrow W_A(b, e) = W_A(b, e')$$

This is the form that drops cleanly into the parent WIF's relation-bounded encapsulation (`EncapsulatedWrt`) and regime-bounded encapsulation (`EncapsulatedWithinRegime`) — the aggregate is just a witness on $B \times E \to Y$ in the parent's typed shape.

Define per-witness movement under a perturbation step:

$$M_i(b, e, e') \;\equiv\; w_i(b, \pi_i e) \neq w_i(b, \pi_i e')$$

Then **audited failure-surface orthogonality** of $w_i$ and $w_j$ — the right operationalization of "disjoint contamination" — is:

$$\forall b, e, e'.\ R_{\text{atomic}}(e, e') \;\Rightarrow\; \neg\bigl(M_i(b, e, e') \wedge M_j(b, e, e')\bigr)$$

The **atomic** restriction matters. A coarse $R$ that flips many environmental variables at once can move two genuinely independent witnesses simultaneously; that proves the perturbation relation was too chunky, not that the witnesses share contamination. The audit asks: *under the smallest meaningful admitted perturbations, do the witnesses share a movement surface?* — not *can a mega-perturbation be constructed that moves everything?*

This also exposes the symmetric failure: orthogonality under atomic perturbations does not entail orthogonality under composite ones, since correlated atomic perturbations can be assembled into a movement neither witness sees alone. Audit at both atomic and the actually-admitted perturbation class.

## Four basic composition lemmas

**Lemma 1 — Clean witnesses compose.**
If every $w_i$ is encapsulated with respect to $R$, then any deterministic aggregator $A$ over their outputs is encapsulated with respect to $R$. *The "no surprise" direction.*

**Lemma 2 — One dirty witness does not automatically contaminate the aggregate.**
If $w_k$ moves under excluded perturbation, the aggregate fails only if $A$ is sensitive to the moved output in that context. A dirty witness can be harmless if (a) the aggregator ignores it, (b) another witness cancels its movement, (c) the movement does not cross the aggregate decision boundary, or (d) the dirty witness is only used in a regime where the movement is irrelevant. *Aggregate contamination is an empirical question, not an inheritance.*

**Lemma 3 — Agreement is not independence.**
If two witnesses move together under the same excluded perturbation, their agreement is not corroboration. It is shared contamination. *Matching outputs are not independent failure surfaces.*

**Lemma 4 — Cancellation earns aggregate standing, not component standing.** *(The sharp one.)*
If two contaminated witnesses move in opposite directions and the aggregator remains invariant, the aggregate may be qualified. The components are still unqualified individually. **Cleanliness belongs to the composition. It does not back-flow to the witnesses.**

## The audit requirement

The corroborative-route seed claim — *dirty witnesses can produce a clean aggregate when failure surfaces are orthogonal and the aggregator is invariant under admitted perturbations* — has a load-bearing word: **audited**.

Without the audit step, "orthogonal failure surfaces" is an assertion smuggled in as a premise. Lazy aggregation puts a blazer on shared contamination and calls it composition. The audit step is what gives the orthogonality claim its own standing.

The four conditions for a corroborative aggregate to earn admissibility:

1. **Contamination bases are declared.** Each witness's $D_i$ (or projection $\pi_i$ from common environment $E$) is on the table.
2. **Failure-surface orthogonality is audited, not assumed.** Independent verification that, under the smallest admitted atomic perturbations, no two witnesses share a movement surface — or that overlap regions do not cross the aggregate decision boundary. Set-disjointness $D_i \cap D_j = \emptyset$ is too literal; the right object is *orthogonality of induced movement under atomic perturbations.* The audit itself requires Standing — someone with the position to verify orthogonality — and the auditor must be **without a stake in the verdict**.
3. **Aggregation rule is invariant under admitted perturbations.** $A$ does not amplify the movement that any $w_i$ smuggles in. (And $A$'s own perturbation surface is declared — see *Aggregator contamination* below.)
4. **Aggregate standing is separate from component standing.** A passed aggregate does not retroactively cleanse the components; a failed aggregate does not retroactively certify them as honest.

Condition (4) is what prevents the inverse laundering — *"the aggregate passed, therefore the components are independent"* — which is the symmetric crime to lazy composition.

For the **aggregate-invariance route**, condition (2) drops out: orthogonality is not required when the aggregator's own invariance carries the weight. Conditions (1), (3), and (4) still hold — but (3) becomes the load-bearing condition rather than a side check.

## Additional composition hazards

The four lemmas, the two routes, and the audit conditions cover the basic geometry. There are at least five further hazards worth naming — none unpacked here, each a candidate door for separate work.

- **Aggregator contamination.** The aggregator $A$ is itself a witness/controller with its own excluded perturbation surface. Voting rule chosen after seeing outputs, weighted ensembles with stale weights, committee chairs who summarize selectively, dashboards with hidden thresholds, LLM "synthesis" introducing its own priors — all introduce a $D_A$. The full shape is $A : O_1 \times \cdots \times O_n \times D_A \to Y$. Cleanliness of components does not entail cleanliness of $A$. *Aggregation is not neutral merely because the inputs are named.*

- **Regime intersection.** Each witness $w_i$ is typically encapsulated only inside an operating regime $\Gamma_i$ (parent WIF's *regime leakage* failure class). The aggregate is qualified only inside $\Gamma_A \subseteq \bigcap_i \Gamma_i$. Component witnesses each qualified in their own regimes can be composed and used in a regime where their qualification overlap is empty. *Composed testimony inherits the intersection of its qualifications, not the union.*

- **Threshold accumulation.** Under weighted or soft aggregation, sub-threshold movement at every component can sum into threshold-crossing movement at the aggregate. Each witness is "harmless individually" while the composition crosses the aggregate decision boundary. This sharpens Lemma 2's "movement does not cross the aggregate decision boundary" clause: per-witness sub-threshold harmlessness is not an aggregate property. *Sub-threshold contamination can become threshold-crossing at the aggregate.*

- **Target mismatch (future bridge, not built).** When witnesses see different target signals $B_i$ that overlap rather than coincide, composition requires a declared **target-alignment map** $B_i \to B^*$. Without it, witnesses are not corroborating; they are adjacent. This probe restricts to shared $B$; the bridge is named for future work. *Witnesses cannot corroborate a target they are not mapped to.*

- **Agreement as anti-evidence.** Agreement among witnesses with shared contamination can be evidence of contamination, not corroboration — especially when the agreement appears exactly where independent perturbation should have produced diversity. The diagnostic split: *agreement under independent perturbations* is possible corroboration; *agreement under shared perturbation* is possible shared contamination; *suspiciously invariant agreement across known component weaknesses* is possible aggregator laundering. The paranoid-but-correct layer.

These are doors named, not opened. Each could earn its own probe; pursuing them all here would cross the probe boundary into a general aggregation theory.

## Failure predicate: Aggregate Witness Invariance Failure

Aggregate WIF occurs when:

1. Multiple witnesses are admitted as corroborating testimony for some target.
2. Their agreement is treated as evidence of independence rather than as a separately-auditable claim.
3. At least one excluded perturbation moves the witnesses jointly, *or* moves the aggregate output.
4. The aggregate continues to be used as if composition had established independence.

Compact form:

> *The ensemble was admitted over a perturbation boundary it did not survive.*

Distinct from single-witness WIF in the same way that aggregate encapsulation is distinct from component encapsulation: the failure lives at the *composition* surface, not at any individual witness.

## Diagnostic battery

For any ensemble / panel / committee / model ensemble / multi-source verification / witness bundle:

1. What is the **aggregate** claim?
2. Which **excluded variables** are the witnesses supposedly independent of?
3. Are the witnesses independent of those variables **individually**?
4. If not, does the **aggregate** remain invariant anyway? *(If yes: aggregate-invariance route; orthogonality not required.)*
5. Do the witnesses fail **independently** under atomic perturbations, or do they share a movement surface?
6. Does agreement survive **independent perturbation**, or only ordinary operating conditions?
7. Has the **failure-surface orthogonality** claim been audited by an actor with standing to evaluate the surfaces and **without a stake in the aggregate verdict**?
8. Does agreement appear **exactly where independent perturbation should have produced diversity**? *(Suspicious invariance is possible anti-evidence, not corroboration.)*
9. Has the **aggregator's own** excluded perturbation surface ($D_A$) been declared? Is the aggregation rule itself audited?
10. Are the **operating regimes** $\Gamma_i$ of the components declared, and is the aggregate's regime $\Gamma_A$ inside their intersection?

Operator rule:

> *Do not count agreement as corroboration until the agreement survives perturbation.*

## Keepers

> *Agreement is not corroboration unless the witnesses fail independently.*

> *Corroboration requires independent failure surfaces, not merely matching outputs.*

> *Cancellation can certify the verdict. It does not cleanse the witnesses.*

> *Dirty witnesses may compose into a clean verdict, but only if the cleanliness belongs to the composition, not retroactively to the witnesses.*

> *Aggregation is not neutral merely because the inputs are named.*

> *Composed testimony inherits the intersection of its qualifications, not the union.*

> *Sub-threshold contamination can become threshold-crossing at the aggregate.*

> *Witnesses cannot corroborate a target they are not mapped to.*

Sharpest single-line:

> *A passed aggregate proves the aggregate. It does not promote its components.*

Two-route summary:

> *Dirty witnesses may compose into admissible aggregate testimony only at the aggregate boundary. Corroborative standing requires audited orthogonal failure surfaces; aggregate standing requires the aggregation rule itself to be invariant under admitted perturbations. Neither route retroactively qualifies the component witnesses.*

## Anti-scope clauses

This probe **does not**:

- Promote WIF from candidate. Promotion still requires WIF's own working → ratified gate (formal stress on the four-step ladder selectivity → specialization → encapsulation → modularity).
- Define a general aggregation theory. The four lemmas are scoped to witness-and-aggregator structures of the form above; they do not extend to all ensemble methods, all Bayesian combinations, all sensor fusion, or all multi-agent agreement.
- Specify the audit step's mechanism. *Failure-surface orthogonality must be audited* is required; *how to audit* (independent perturbation tests, mechanism-orthogonality proofs, adversarial probing, etc.) is open. This is exactly where Lean / formal staging would land if the probe earns it.
- Generate composite primitives by combining with other notebook entries (anti-coordinate-combinatorics rule applies — see README).
- Enter the Active primitive notes table. The probe lives as an extension note, not as its own primitive.

## Open questions

- **Audit operationalization.** What does "audited orthogonality" reduce to in practice? Candidate forms: independent perturbation tests at the atomic-perturbation grain, theoretical proofs of mechanism orthogonality, cross-domain redundancy with declared mechanism separation, adversarial probing for shared failure modes. Each has its own admissibility profile. None is generic.
- **Heterogeneous targets / target-alignment map.** This probe assumes all witnesses see the same $B$. Real ensembles often have witnesses on different but overlapping target signals; the named-but-not-built bridge is a target-alignment map $B_i \to B^*$. Whether the composition lemmas extend cleanly through such a map is open.
- **Threshold geometry under weighted aggregation.** When $A$ is a weighted vote / soft aggregator, sub-threshold component movement can sum into threshold-crossing aggregate movement. Named in *Threshold accumulation* above; formal handling — what aggregation rules are threshold-stable, what bounds composite movement under per-component bounds — is open.
- **Aggregator contamination ($D_A$).** Named in *Additional composition hazards* but not formalized. The aggregator-as-witness shape $A : O_1 \times \cdots \times O_n \times D_A \to Y$ collapses cleanly into the parent WIF's typed form (the aggregator is just another witness on a richer basis); the open question is the right *audit composition* across components and aggregator simultaneously.
- **Atomic vs composite perturbations.** Audit at atomic perturbations does not entail orthogonality under composite/correlated perturbations; the converse can also fail. The right operational answer is probably "audit at both grains" but the formal characterization of when atomic-orthogonality lifts to composite-orthogonality is open.
- **Lean staging path.** WIF has a Lean module (`~/git/lean/LeanProofs/Admissibility/WitnessInvariance.lean`) with the typed-perturbation-relation form (`EncapsulatedWrt`) and regime-bounded form (`EncapsulatedWithinRegime`). The aggregate $W_A$ in common-environment form drops directly into these as a witness on $B \times E \to Y$. Two-witness scaffold — not n-ary, since dependent $O_i$ / $D_i$ / `Fin n` machinery turns into cathedral immediately — is the obvious starting shape. Three target theorems: (a) component encapsulation under $R$ ⇒ aggregate encapsulation under $R$ (Lemma 1, the boring foundational result); (b) Lemma 4 counterexample showing aggregate encapsulation without component encapsulation (cancellation case); (c) Lemma 3 counterexample showing agreement under shared perturbation. Held until a forcing case or paper home appears.
- **Connection to Simpson's paradox / aggregation paradoxes.** The Lemma 3 / Lemma 4 distinction is structurally close to standard aggregation paradoxes in statistics. The connection is real but not pursued here; pursuing it would expand scope past the probe boundary.
- **The audit's own Standing.** Condition (2) requires the auditor to be without stake in the verdict. That is itself a Standing claim, and Standing is its own load-bearing object in adjacent work. The recursive structure (audit-of-aggregate requires Standing, which may require its own audit) is noted but not unpacked.

## Provenance

- **2026-05-09 origin.** Multi-model exchange surfacing ChatGPT's four-type extension taxonomy (formal / operational / paper / composite); WIF composition identified as the deepest formal-upside candidate; operator override on audit-paralysis ("audit identified the sharp edges; now you're allowed to pick up a sharp object").
- **ChatGPT (origin pass):** four-lemma sketch, formal-ish setup, diagnostic battery, "agreement is not corroboration" keeper, "cancellation certifies the verdict, not the witnesses" sharpening.
- **claude-code-papers (initial pass):** identified the audit step as the load-bearing word in the seed claim ("disjoint *and audited*"); flagged contamination-base-disjointness-with-audit as the load-bearing form among ChatGPT's four candidate theorem shapes.
- **user (origin):** affirmed the audited-disjointness form as the theorem; emphasized that without the audit, the disjointness claim becomes a smuggled premise; affirmed Lemma 4 / cleanliness-belongs-to-composition as the doctrinal payload.
- **claude-code-papers (initial scope discipline):** probe not primitive; extension not promotion; bounded not general; aggregate-standing-separate-from-component-standing as Condition (4); explicit anti-scope clauses; "passed aggregate does not promote its components" symmetric guardrail.
- **2026-05-09 follow-up exchange (this revision).** ChatGPT caught that the original "only if" seed claim was overstrong against Lemma 4 (cancellation route does not need disjointness); proposed two-route split, common-perturbation-environment formalization with $E$ and $\pi_i$, atomic-perturbation refinement of audit, and the additional-hazards battery (aggregator contamination, regime intersection, threshold accumulation, target-alignment map, agreement-as-anti-evidence). Also fixed wording bug in diagnostic question 7: auditor needs Standing (the position to evaluate), what they must lack is *stake in the verdict* — not standing itself. claude-code-papers folded the revisions into the existing probe structure; resisted scope expansion into a general aggregation theory; named the additional doors without opening them. user affirmed the two-route reframe as the load-bearing fix.
- Filed as probe / extension note. Not promoted. Not registry-listed. No Lean staged. No paper home. Revised scope still bounded; new content is sharpening, not expansion.
