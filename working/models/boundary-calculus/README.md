# Boundary Calculus Examples

Status: toy corpus / non-doctrinal

These examples test notation and rule shapes for basis-indexed admissibility under boundary transition. They are intentionally small. Their purpose is to expose the moves of the calculus, not to define the final kernel.

## Core judgment

\[
\Gamma \vdash_{\kappa} \mathsf{Adm}(a)
\]

Read: action \(a\) is admissible in state/context \(\Gamma\) on basis \(\kappa\).

## Core invariant

Admissibility does not inherit across a boundary merely because the action was admissible before. A basis must either transport, degrade under an explicit rule or be freshly derived in the target state.

## Example ladder

- `example_000_visa_toy_model.md`  
  Binary transport and non-inheritance. A basis either survives the target-state recognition check or fails.

- `example_001_maintenance_window.md`  
  Degradation. A live authorization token dies as authority but survives as historical evidence.

- `example_002_cumulative_visa.md`  
  Mutable basis. A numeric basis transports while its value is consumed across repeated transitions.

- `example_003_deploy_across_staging.md`  
  Scope boundary. Promotion may transport an artifact, but it does not transport staging authority.

- `example_004_nq_witness.md`  
  Local derivation and anti-laundering. Observation survives ingest as evidence; testimony requires explicit coverage.

- `example_005_stale_cache_consequence_window.md`  
  Basis decay over time. Time passage is a boundary transition; a fresh cache entry transports as fresh within TTL, degrades into a stale-use basis through the grace horizon, and dies beyond it. Not a separate temporal calculus — instantiated within the existing preservation/degradation rule set.

- `example_006_belated_authorization.md`  
  Temporal non-overlap. Authorization may be procedurally valid while the consequence-viability window has already closed; the basis authorizes only an archival record, never the missed action. Distinct from TTL decay — the failure is non-overlap between basis validity and consequence viability, not basis expiry.

## Rule shapes under test

- Preservation: a basis survives a boundary and continues to support the same action.
- Degradation: a basis crosses a boundary as a weaker or different kind of support.
- Mutation: a basis survives while its internal value changes.
- Non-inheritance: failed transport does not prove inadmissibility, but it blocks reuse of the old basis.
- Local derivation: some admissibility judgments are constructed inside a state from already-admissible bases and verdicts, not transported across boundaries.
- Decay: a basis loses authority over time, possibly degrading into a weaker form before expiring entirely. A specific case of preservation + degradation under time-passage transitions.

## Corpus relation

Several examples instantiate failure modes already named in the Δt / admissibility corpus, including timing windows, scope boundaries, witness/testimony separation, resource-budgeted authority and consequence viability.

This is an **observation**, not a synthesis claim. The examples are toy models for testing whether a shared judgment form and rule vocabulary can express recurring transition failures. They should not be treated as proof that the corpus has a single formal substrate.

## Current evidence that the models are doing work

The toy models have already exposed rule-level errors — particularly cases where preservation would accidentally allow stale or belated authority to continue authorizing an action (Examples 5 and 6 both began as drafts with this bug, caught and corrected during review). Those failures are useful because they make implicit prose claims testable: a slogan like "stale evidence cannot authorize fresh use" looks self-evident in prose and turns out to be a non-trivial structural constraint on the transport / degradation split.

Three of chatty's four containment conditions for promoting toy notation into a named calculus appear to be met (shared judgment form; ≥3 examples; the toys catch errors). The fourth — **rules compose** — is not yet established. The examples *chain* but composition has not been tested directly. The discriminating question:

> If \(B_1\) transports/degrades \(\kappa\) into \(\kappa'\), and \(B_2\) transports/degrades \(\kappa'\) into \(\kappa''\), does \(B_2 \circ B_1\) produce the same admissibility result as the stepwise composition?

Until that test is run on a worked composition (e.g., fresh → stale → dead, or authorization → evidence → audit basis), the corpus is *synthesis-paper-adjacent*, not synthesis-paper-ready.

## Non-goals

- These examples are not the final calculus.
- They do not claim novelty for the phrase “boundary calculus.”
- They intentionally avoid full categorical/type-theoretic machinery.
- They should not be treated as production governance rules.
