# ATProto Provenance Instrument: Signal Intelligence for Content Ranking

**Date:** 2026-03-21
**Status:** Specification sketch (not a roadmap)
**Frame:** SIGINT, not trust. Radar, not tribunal.
**Related:** `atproto_governance_transfer_proof.md` (governance ontology), labelwatch, driftwatch

## The Reframe

The original question was "web of trust overlay for ATProto." The better question is "provenance instrument." The distinction matters:

| | Trust layer | Provenance instrument |
|---|---|---|
| Claim | "believe this" | "understand why this is in front of you" |
| Output | authority / endorsement | decomposed signals / audit trail |
| Risk | becomes governance surface | becomes intelligence apparatus |
| Moral object | soft normative authority | measurement with documented limits |

A trust system tells you who is good. A provenance instrument tells you where something came from, how it got to you, and who amplified it. The second is a lot easier to defend and a lot harder to abuse — though not immune (see Constitutional Constraints below).

## What ATProto Already Provides

The protocol gives you most of the plumbing:

- **Custom feeds** are first-class. A feed generator returns ranked post URIs via `getFeedSkeleton`; the AppView hydrates them. The generator can use any ranking logic it wants.
- **Public follows / relationships** are queryable via `app.bsky.graph.*` lexicons.
- **Lists and starter packs** are explicit trust/curation signals users have already created.
- **Labeler services** emit structured labels with metadata — positive, negative, or informational.
- **Firehose** provides real-time repo events for indexing.
- **DIDs / signed commits** provide cryptographic authorship.

What ATProto does *not* provide: any notion of why you're seeing something, what path it took to reach you, or how to decompose a post's ranking into auditable signals. That's the gap.

## Architecture: Three-Layer Scoring

The core design principle: **never collapse signals into a single trust number.** Keep three layers separate, auditable, and decomposable.

### Layer 1: Actor Signals

Per-account scoring based on the user's relationship to the author:

| Signal | Source | Weight direction |
|---|---|---|
| Direct follow | `app.bsky.graph.follow` | Positive |
| Mutual follow | Bidirectional follow check | Strong positive |
| Follow-graph distance | BFS/limited-depth traversal | Decays with distance |
| Shared list membership | `app.bsky.graph.list` | Positive (weighted by list trust) |
| Starter pack co-membership | `app.bsky.graph.starterpack` | Mild positive |
| Labeler output on account | `com.atproto.label.subscribeLabels` | Positive or negative by label value |
| Account age / activity pattern | Indexed from firehose | Mild signal; new accounts slightly discounted |

Actor signals answer: **who is this, and what is my relationship to them?**

### Layer 2: Relay Signals

Per-post scoring based on how the content reached the user:

| Signal | Source | Weight direction |
|---|---|---|
| Original post | Direct authorship | Full author score |
| Repost | `app.bsky.feed.repost` | Partial inheritance from reposter + original author |
| Quote post | `app.bsky.feed.post` with embed | Weighted by both quoter and quoted |
| Reply chain depth | Thread structure | Decays with depth from root |
| Amplification velocity | Firehose timing analysis | Informational — fast coordinated amplification is a signal, not necessarily negative |
| Relay path length | How many hops from origin to user's feed | Longer paths = more uncertainty about why it surfaced |

Relay signals answer: **how did this get here, and who touched it along the way?**

### Layer 3: Domain / Source Signals

Per-domain scoring based on linked external sources:

| Signal | Source | Weight direction |
|---|---|---|
| Known-quality domains | Curated list (ProPublica, AP, Reuters, etc.) | Positive |
| Domain recurrence in trusted clusters | Correlation analysis | Positive if correlated with high-actor-score posts |
| Domain recurrence in low-trust clusters | Correlation analysis | Informational / caution signal |
| Link density | Posts with vs without external links | Informational |
| Domain freshness | First appearance timing | Informational — new domains are neither good nor bad |

Domain signals answer: **what external sources are being referenced, and where do they cluster?**

## Feed Candidate Record

Every post considered for the feed gets a candidate record with decomposed signals — the hosting locus card pattern applied to content ranking:

```
{
  "uri": "at://did:plc:.../app.bsky.feed.post/...",
  "actor_score": 0.72,
  "actor_signals": {
    "mutual": true,
    "graph_distance": 1,
    "list_membership": ["trusted-journalists"],
    "labeler_flags": []
  },
  "relay_score": 0.85,
  "relay_signals": {
    "relay_type": "quote_post",
    "original_author_score": 0.68,
    "amplification_velocity": "normal",
    "path_length": 2
  },
  "domain_score": 0.90,
  "domain_signals": {
    "linked_domains": ["propublica.org"],
    "domain_cluster": "investigative-journalism",
    "domain_quality": "curated-high"
  },
  "composite_rank": null,
  "reasons_json": "mutual follow, quoted from known journalist, links propublica"
}
```

**`composite_rank` is deliberately nullable.** The system can rank without collapsing to a single number. The decomposed view is the primary output. If a composite is needed for feed ordering, it should be clearly documented as a lossy projection.

## Intelligence Modes

The same infrastructure supports multiple output modes beyond feed ranking:

### Provenance Explainer
"Show me the path, decomposition, and signals for why this post is in scope at all." This is the first artifact to build — it keeps the system in measurement land.

### Propagation Mapping
Consume driftwatch fingerprints to trace how claims propagate through the network. "This claim fingerprint appeared first in cluster A, then spread to clusters B and C within 4 hours." Not judgment — cartography.

### Labeler Overlay Analysis
Consume labelwatch outputs to correlate labeler behavior with content flow. "Posts in this topic cluster are labeled 3x more frequently by labeler X than by labeler Y." Again: measurement, not verdict.

### Timing Intelligence
Who was early, who was derivative, who synchronized suspiciously. Firehose timestamps make this directly observable. Coordinated posting (many accounts posting similar content within a narrow time window) is a signal worth surfacing without requiring a judgment about whether coordination is good or bad.

## Composability with Existing Systems

This is not greenfield. It's a joining layer across existing observatories:

| Existing system | What it provides | How this consumes it |
|---|---|---|
| **labelwatch** | Labeler behavior profiles, churn rates, regime shifts | Labeler flags as actor/relay signals; high-churn labelers as caution signal |
| **driftwatch** | Claim fingerprints, propagation traces, burst detection | Propagation geometry as relay signal; coordinated bursts as timing intelligence |
| **Feed generator (existing)** | Basic feed mechanics, firehose ingestion | Infrastructure reuse; this extends the ranking logic, doesn't replace the plumbing |

## Constitutional Constraints

The system must be designed so that even its successful outputs cannot fully naturalize themselves. This is Paper 18's thesis restated as a requirement:

1. **No single trust score.** Signals stay decomposed. Users can inspect why a post ranked where it did.
2. **Reasons are first-class.** Every ranking decision has a `reasons_json`. The system cannot rank without explaining.
3. **The system does not label content.** It maps provenance and flow. Labeling is a separate function with separate authority.
4. **Intelligence does not automatically become action.** The system can analyze influence paths but should be architecturally cautious about collapsing analysis into recommendation or sanction. The pressure to do so will be constant.
5. **The miss log exists.** Cases where the provenance signals pointed one way and reality went another are tracked, not buried. Without this, the instrument becomes a confirmation engine.
6. **No interdiction.** The system surfaces signals. It does not suppress, downrank-to-zero, or block. Feed ranking is always positive selection ("show me more of this"), not negative enforcement ("hide this from me").
7. **The operator is visible.** The feed generator's scoring logic is documented and auditable. "Algorithmic transparency" means the weights and signals are inspectable, not that they're published as a press release.

## The Slope

SIGINT has its own slope toward governance. Once you can map flows well, people immediately want: prioritization, interdiction, suppression, automated weighting, threat scoring, trust by implication.

The constitutional constraints above are the brakes. But brakes only work if someone maintains them. The system that resists becoming sovereign only stays non-sovereign if someone keeps reasserting the conditions under which it is merely instrumental.

This is the maintenance trap: the operational burden is not the code. It is the ongoing discipline of keeping an intelligence instrument from becoming a governance surface.

## Infrastructure Notes

- **Cannot cohabitate on the current VM.** Three observatory-weight projects on an 8GB Linode is how you get involuntary filesystem theology at 3am. This would need its own box or a serious rethink of the hosting architecture.
- **SQLite is fine for the prototype.** The feed generator pattern (firehose → index → serve) is well-documented in atproto starter kits. SQLite handles the indexing. Postgres if it grows.
- **The first artifact should be the provenance explainer, not the feed generator.** "Show me why this is here" before "rank this for me." That keeps it in radar-console territory longer.

## Open Questions

### Architecture

1. **How much transitive trust before it becomes six-degrees-of-crank?** Follow-graph distance decay needs a cutoff. Two hops? Three? The answer is empirical and probably domain-dependent.
2. **Protocol boundary breaks.** Bridgy Fed bridges Mastodon → ATProto. Content that crosses protocol boundaries loses provenance metadata. If a growing fraction of the network comes through bridges, the instrument has a blind spot that grows with federation success.
3. **The instrument's own temporal coherence.** The firehose has latency. The graph index goes stale. The domain list ages. This instrument is itself a controller with observation lag, actuation delay, and temporal contracts that can rot. The Δt framework applies to the instrument, not just the systems it observes. The spec should eat its own cooking.

### Adversarial Dynamics

4. **Explainability as attack surface.** Once provenance signals are visible and influence ranking, they become optimization targets (Paper 16's gain geometry predicts this). Actors learn what path geometry looks "normal," clusters shape amplification to evade timing flags, list curation becomes reputation laundering, `reasons_json` becomes SEO for legitimacy. This is not fraud prevention — it is co-evolutionary warfare with a legibility layer.
5. **The curated domain list is a governance decision hiding inside an intelligence system.** "Known-quality domains" like ProPublica get a boost. Who curates that list? That's an editorial judgment wearing an infrastructure costume. The constitutional constraints say "no interdiction" but a curated positive list is soft interdiction of everything not on it.

### Subject Rights and Decay

6. **Subject-side contestability.** The spec is operator-view. What rights does the subject of observation have? Can they inspect their own provenance profile? Can they see what signals are attached to them? Can they challenge stale or false inference? Without this, even a well-behaved instrument stays structurally one-sided.
7. **Forgetting policy for soft suspicion.** The instrument preserves path and history. But when do signals expire? How long do anomalous patterns haunt an account? What prevents old pathologies from becoming permanent aura? Without a serious decay policy, the system drifts toward inherited stigma.
8. **Measurement produces rank even when it refuses judgment.** Even if the instrument never labels content, users will treat certain path shapes as discrediting, infer guilt from anomaly, treat cluster association as contamination, and use decomposition as a proxy for moral standing. A non-sovereign instrument can still manufacture informal caste behavior.

### Governance of the Instrument

9. **Change control for the intelligence apparatus.** Who versions the weights? Who decides signal inclusion/exclusion? Who defines miss-log thresholds? What gets receipted when the instrument itself changes? The instrument needs its own provenance.
10. **Functional creep through adjacent utility.** Instruments don't become sovereign because someone declares it. They become sovereign because people keep asking one more "obvious" thing: can you rank? caution? suggest? auto-deprioritize? feed moderation triage? generate alerts? The actual constitutional failure path is boring product pressure, not evil intent.
11. **Observatory disagreement.** Multiple feed generators, labelers, and provenance instruments will coexist with conflicting operator constitutions. When one says "normal propagation" and another says "coordinated burst," what does the user infer? What prevents this from silently collapsing back into "who do you trust?" — which is exactly the thing the spec is trying to avoid.

### Identity

12. **The operator's information diet.** The first user is the operator. Running a radar changes the operator's perception of the network, not just the observed. This effect is unaudited.
13. **Interface as constitutional surface.** Same data, different UI: forensic console, trust badge, suspicion dashboard, journalistic provenance card, network observatory. The presentation layer decides what kind of epistemic object the instrument becomes. The interface is part of the constitution.
14. **Paper or project?** The same idea has two honest forms: a paper on provenance architecture and constitutional constraints for social-graph intelligence, or a working instrument that makes demands on its operator. Those are different obligations wearing the same outfit.
15. **Is this the causality control plane?** The overlap with the `causality-control-plane.md` working paper (ordering failure, admissibility, manufacture of necessity) is non-trivial. The provenance instrument is arguably the implementation-side expression of that paper's theory. Worth tracking but not forcing.

## Status

Specification sketch. Not committed to build. Filed as a precision instrument for evaluating the idea later — clear enough to assess, not so committed that it creates obligation.
