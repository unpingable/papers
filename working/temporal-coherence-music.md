# Temporal Coherence in Music: Productive Incoherence and the Missing Control Architecture

**Status:** Working paper skeleton. NOT Paper 23. Standalone candidate.
**Origin:** Shower thought (2026-03-24), validated against music cognition literature.
**Decision:** Decide later whether this is a paper, a book appendix, or a conference talk.

### Working Title Options
- Productive Temporal Incoherence: A Δt Framework for Musical Timing
- Tension, Groove, and Delay: Toward a Multiscale Theory of Musical Δt
- Governed Drift: Musical Timing as Controlled Temporal Mismatch
- When Delay Is the Product: Δt and the Architecture of Musical Time

### Draft Abstract
Musical timing can be modeled as a multiscale system of temporal mismatch spanning pulse, meter, phrase, cadence, ensemble coordination, and form. Existing literatures treat pieces of this problem separately: dynamical entrainment models explain rhythmic coupling, generative and expectation-based models explain metrical and tonal structure, ensemble-cognition work explains interpersonal coordination, and groove research explains why moderate syncopation and complexity can increase pleasure and desire to move. What is missing is a unified architecture that distinguishes pathological delay from productive delay. We propose a Δt framework in which musical tension, groove, swing, rubato, and ensemble lag are analyzed as forms of governed temporal incoherence rather than mere deviation from an ideal grid. The contribution is not to replace existing theories, but to connect them: music becomes a domain in which temporal mismatch is not simply tolerated, but often cultivated as the source of expressive force. This also sharpens the broader Δt framework by forcing a formal account of positive deviation, not just failure.

---

## One-Sentence Thesis

Music is the domain where temporal mismatch is not a bug to be minimized but a resource to be shaped — and formalizing when mismatch is productive vs pathological forces the Δt framework to grow the limb it's currently missing.

## Why This Matters for the Framework

The Δt series treats temporal incoherence as a failure mode with occasional "signed" nuance (Paper 16). Music is the forcing function that demands a formal account of **productive temporal incoherence** — structured deviation that generates feel, tension, propulsion, and release rather than degradation. If the framework can't handle this, it's incomplete. If it can, it becomes sharper everywhere else too.

The claim is NOT "Δt explains music." The claim is:

> Δt gives you a way to distinguish musically productive delay from pathological delay across multiple layers: beat, groove, phrase, cadence, ensemble coordination.

## The Gap in the Literature

The music cognition literature has all the building blocks but no unified control architecture. The fragmentation is almost identical to the pre-Paper-22 state of temporal failure across engineering/distributed-systems/institutional theory:

- **Oscillator models** (Large) capture entrainment but not intentional deviation
- **Linear correction models** (Wing, Repp) capture pairwise synchronization but not hierarchy
- **Generative grammar** (Lerdahl & Jackendoff) describes metrical structure but not dynamics
- **Information theory** (Pearce/IDyOM) models pitch expectation but not timing control
- **Groove research** (Witek, Butterfield, Keil) measures what feels good but doesn't model the underlying control
- **Networked performance** (Chafe) solves delay problems without connecting to cognition

Nobody has assembled these into: here is the plant, here is the controller, here is the estimator, here is the reference signal, and here is how they compose across the ensemble.

## The Four Layers in Music

### Layer 1: Gauge Mismatch — "What is the beat?"

Shared temporal reference in music is constructed, not given. A conductor's downbeat is a gauge convention — different sections see it at different times. In a jazz combo, the shared "now" is negotiated continuously through listening. In polymetric music, the gauge is deliberately fractured.

- Lerdahl & Jackendoff's metrical well-formedness rules are gauge constraints
- Conductor–ensemble lag is measurable and dynamically variable (Frontiers, 2020)
- Polymeter and polyrhythm are intentional gauge multiplicity

### Layer 2: Clock Divergence — "One second here ≠ one second there"

Musicians' internal timekeepers drift. Tempo drift between players is the musical equivalent of clock skew.

- Rubato is intentional clock divergence: the soloist's clock decouples from the accompaniment's and must reconverge
- Hudson (1994) distinguishes "earlier" rubato (melody deviates, accompaniment keeps time — a two-layer timing system) from "later" rubato (entire texture deviates together)
- Swing ratio varies inversely with tempo (Friberg & Sundström, 2002) — a systematic constraint on clock deviation
- Tempo drift in ensembles is corrected by phase and period correction mechanisms (Repp, Keller)

### Layer 3: Retarded-State Estimation — "Playing to what you heard"

Every musician acts on stale observations. In a large ensemble or reverberant hall, acoustic delay is non-trivial (~30ms across a large orchestra stage). Musicians perform state estimation on delayed input.

- Goebl & Palmer (2009): disrupting auditory feedback degrades but doesn't destroy synchronization — internal models buffer against observation loss
- Chafe et al. (2010): critical threshold ~20-30ms for networked performance — below this, compensation works; above, strategy must change
- A 2024 dyadic tapping study found synchronization was actually *better* at intermediate delays (~40-160ms) than at 0ms — a non-monotonic relationship consistent with the inverted-U pattern in groove

### Layer 4: Delayed Actuation — "The instrument has physics"

Physical lag between musical intention and sound: hammer mechanics (piano), air column settling (brass), bow response (strings), breath onset (voice). The musician must anticipate — target a future beat, not the current one.

- Different instruments have different actuation latencies — ensemble roles have different delay tolerances
- Farner et al. (2009): rhythm section is more affected by delay than melodic instruments — consistent with different loop bandwidth requirements
- Smith predictor analogy: experienced musicians build internal models of their instrument's response, effectively running predictive compensation

## The Novel Contribution: Three Forms of Temporal Debt in Music

Not all temporal mismatch in music works the same way. Following Chatty's suggestion, the paper should formalize a three-way split:

### 1. Closure Debt

Tension created by withholding expected resolution. Harmonic cadences delayed, phrases extended, resolutions postponed. This is temporal debt in the Meyer/Huron sense — expectation is set up and satisfaction is deliberately deferred. The timing of resolution is the emotional content.

- Maps to: information-theoretic surprise (Pearce/IDyOM), but applied to temporal rather than pitch domain
- Productive when: the listener maintains prediction (knows resolution is coming) — bounded debt
- Pathological when: prediction collapses (the listener gives up expecting resolution) — debt exceeds coherence budget

### 2. Entrainment Debt

Deviation from the internalized metrical grid. Syncopation, swing, groove microtiming. The listener's oscillator expects an event at time t; it arrives at t ± δ. The deviation is productive when δ is within the entrainment bandwidth (the oscillator can absorb it and re-entrain) and pathological when δ exceeds it.

- Witek et al. (2014): inverted-U relationship — medium syncopation maximizes groove. This IS the coherence budget curve.
- The inverted-U is the empirical signature of a bounded coherence regime: too little deviation = no engagement (underdriven oscillator), too much = loss of entrainment (exceeded bandwidth), optimal = productive tension within the coupling range
- Keil's "participatory discrepancies" are entrainment debt that stays within budget

### 3. Coordination Debt

Timing mismatch between ensemble members. Phase offsets between instruments, tempo disagreements, leader-follower lag. Coordination debt is productive when it creates "pocket" (relational timing that generates feel) and pathological when the ensemble loses mutual entrainment.

- Butterfield (2010): the pocket is a *relational* timing property — specific instruments consistently ahead or behind
- Wing et al. (2014): string quartet timing shows asymmetric coupling with a virtual shared metronome
- The 20-30ms networked performance threshold (Chafe) is a stability boundary for coordination debt

## The Productive Incoherence Regime

The key theoretical contribution: formalizing the **regime** in which temporal mismatch is productive rather than pathological. This requires:

1. **A reference trajectory that is not the grid.** The target is not metronomic perfection but a specific deviation pattern (swing curve, groove template, rubato contour). The control system tracks this non-trivial reference, not the clock.

2. **A bounded coherence envelope.** Deviations from the reference trajectory are tolerated within a band. Inside the band = expressive. Outside the band = error. The inverted-U (Witek) is the empirical shape of this envelope.

3. **A multi-timescale coherence budget.** Beat-level deviations are absorbed by bar-level structure. Bar-level deviations are absorbed by phrase-level structure. The hierarchy provides cascading coherence buffers. When a deviation exceeds the buffer at one level, it propagates upward.

4. **A distinction between execution and retirement** (from the causality-control-plane working paper). Musicians can execute out of order (anticipate beats, play ahead, syncopate) as long as the phrase-level structure retires in order. The reorder buffer is the phrase. Undisciplined retirement — losing the phrase arc — is the pathological case.

## What This Forces the Δt Framework to Formalize

Paper 16 introduced signed Δt (mismatch can be positive, negative, or neutral in effect). This paper would force the framework to specify:

- **When is Δt productive?** When deviations remain within a bounded coherence envelope around a non-trivial reference trajectory, and the hierarchical absorption cascade is functioning.
- **When does productive Δt become pathological?** When the deviation exceeds the envelope, the hierarchy's absorption capacity is exhausted, or the reference trajectory itself becomes incoherent.
- **What governs the transition?** The ratio of deviation magnitude to coherence bandwidth at each hierarchical level.

This generalizes beyond music. Any system where some temporal incoherence is functional (democratic deliberation, market price discovery, scientific peer review, creative collaboration) could be analyzed using the same productive-incoherence regime concept.

## Key Literature to Cite

### Foundational
- Meyer (1956). *Emotion and Meaning in Music.* — expectation as the basis of musical meaning
- Huron (2006). *Sweet Anticipation.* — ITPRA framework for expectation response
- Lerdahl & Jackendoff (1983). *A Generative Theory of Tonal Music.* — hierarchical metrical structure
- London (2012). *Hearing in Time.* — meter as cognitive framework with constraints

### Groove and Productive Deviation
- Witek, Clarke & Wallentin (2014). *PLOS ONE.* — inverted-U for syncopation and groove
- Keil (1987). *Ethnomusicology.* — participatory discrepancies
- Butterfield (2010). *Music Theory Online.* — the pocket as relational timing
- Iyer (2002). *Music Perception.* — embodied microtiming in African-American music
- Benadon (2006). *Music Perception.* — swing ratio as tempo-dependent function

### Ensemble Coordination and Delay
- Keller (2014). *Psychonomic Bulletin & Review.* — anticipation, attention, adaptation
- Wing et al. (2014). *PNAS.* — string quartet as coupled dynamical system
- Chafe et al. (2010). *Computer Music Journal.* — latency thresholds in networked performance
- Goebl & Palmer (2009). *JASA.* — auditory feedback and internal models

### Oscillators and Dynamical Systems
- Large & Jones (1999). *Psychological Review.* — Dynamic Attending Theory
- Large & Palmer (2002). *Psychological Review.* — coupled production-perception oscillator

### Control and Timing Models
- Pressing (1998). *Psychological Research.* — error-correction models (closest to explicit control theory)
- van der Steen & Keller (2013). *Frontiers in Computational Neuroscience.* — ADAM model (feedback + feedforward)
- Jacoby & Repp (2012). *PLOS ONE.* — synchronization as delayed feedback control

### Information Theory
- Pearce (2018). *Frontiers in Psychology.* — IDyOM review
- Hansen & Pearce (2014). *Frontiers in Psychology.* — predictive uncertainty and groove

## Proposition Set

Explicit testable claims:

- **P1:** Musical systems are organized by nested temporal verification windows rather than a single clock.
- **P2:** The musical effect of timing deviation depends on scale, context, and recoverability, not magnitude alone.
- **P3:** Groove, swing, and rubato are not mere departures from ideal timing, but structured temporal targets.
- **P4:** Pathological and productive Δt can be distinguished by whether deviation preserves shared frame legibility.
- **P5:** Ensemble coordination requires anticipatory control under delayed perception and nonzero actuation lag.
- **P6:** A unified Δt architecture clarifies relationships among entrainment, expectation, closure, and coordination that are usually treated separately.

## Hinge Line

> **Time is universal; what varies is the regime by which a system samples, anticipates, and settles against it.**

## Section Outline

### 1. Introduction: Music as the Domain Where Delay Is Not a Bug
- Bureaucracies, networks, and institutions treat delay as failure. Music often treats delay as value.
- The problem is not whether temporal mismatch exists but what regime it belongs to.
- Four claims: tension = felt closure debt, groove = stabilized local mismatch, ensemble coordination = recoverable interpersonal lag, form = long-range governance of delayed resolution.
- This forces the Δt framework to formalize the productive/pathological boundary — that formalization generalizes beyond music.

### 2. The Existing Landscape: Rich Parts, No Assembly
- Oscillator models, correction models, generative grammars, information theory, groove research — all present, none connected
- The fragmentation mirrors pre-Paper-22 temporal failure literature
- Subsections: entrainment/oscillators (Large), meter/hierarchy (Lerdahl & Jackendoff), expectation/prediction (Pearce/IDyOM), ensemble coordination (Keller), groove/syncopation/microtiming (Witek, Keil, Butterfield), networked/delayed performance (Chafe)
- Transition: "The parts exist. The architecture does not."

### 3. The Δt Architecture for Musical Timing

Five layers, musically native rather than imported from engineering:

**L0 — Onset / Pulse.** The shortest horizon. When is the event? How much local offset is recoverable? Objects: onset alignment, microtiming, swing ratio, local jitter, attack/actuation lag.

**L1 — Beat / Meter.** The shared grid. What counts as "on time"? What deviations preserve metrical legibility? Objects: syncopation, meter confirmation, metrical ambiguity, phase alignment.

**L2 — Phrase / Cadence / Harmonic Closure.** Delay becomes semantic. What closure has been promised? What debt is being carried? When does delay produce yearning vs mere expiration? Objects: suspension, appoggiatura, dominant prolongation, deceptive cadence, phrase extension.

**L3 — Ensemble Coordination.** The social layer. How do multiple agents maintain recoverable alignment under stale perception and actuation delays? Objects: conductor lag, chamber anticipation, leader/follower drift, linked internal models, delay compensation.

**L4 — Formal / Stylistic / Genre Contract.** The long horizon. What kind of return, drop, climax, or sectional payoff has the piece trained the listener to expect? Objects: sonata return, EDM drop, breakdown/fakeout, chorus arrival, rubato release into tempo.

### 4. Three Forms of Temporal Debt in Music
- Closure debt (deferred resolution — the Meyer/Huron axis)
- Entrainment debt (grid deviation / syncopation / groove — the inverted-U)
- Coordination debt (inter-player mismatch / pocket — the Keil/Butterfield axis)
- The inverted-U as the empirical coherence budget curve

### 5. Productive vs Pathological Temporal Incoherence

Three regimes:

**Pathological Δt.** Mismatch destroys legibility or recoverability. Ensemble drift nobody can absorb. Expressive timing that no longer reads as shared. Phrase delay that outlasts memory of the promise.

**Neutral Δt.** Mismatch is present but musically inert. Tiny deviations with no perceptual or expressive consequence. Complexity tolerated but not generative.

**Productive Δt.** Mismatch intensifies expectation, embodiment, or social coordination while remaining legible. Groove. Swing. Rubato with reconvergence. Syncopation under preserved meter. Delayed cadence that heightens closure.

### 6. Failure Taxonomy

Six distinct failure kinds (not a single "bad timing" bucket):

- **Clock failure:** tempo or phase reference degrades
- **Estimation failure:** performer/listener misreads where others are in time
- **Actuation failure:** physical production cannot meet intended target
- **Propagation failure:** local deviation cascades upward across levels
- **Settlement failure:** harmonic or formal debt is not repaid in time
- **Visibility failure:** the shared frame is no longer perceptible enough to govern deviation

### 7. Case Studies
- Swing: structured local off-grid timing under stable meter
- Rubato: temporary clock divergence with planned reconvergence
- Deceptive cadence: promised closure rerouted into renewed debt
- Ensemble lag: real joint-control problem — conductor lag, networked performance
- Optional: groove in funk/D&B/EDM — genre-specific ways of governing local drift

### 8. Empirical Predictions
- The inverted-U should appear at every hierarchical level, with different bandwidth parameters
- Coordination debt tolerance should correlate with ensemble coupling architecture
- The 20-30ms threshold should vary with musical role (rhythm section tighter than melodic)
- Rubato should show convergence statistics consistent with clock divergence under resynchronization

### 9. Implications for the Δt Framework
- Productive incoherence forces the framework to specify regime boundaries, not just failure modes
- Generalizes to deliberation, price discovery, scientific discourse, creative collaboration
- The sharpened framework: Δt is pathological when it exceeds the coherence envelope, productive when it stays inside, and dead when it's zero

### 10. Limits and Anti-Imperial Guardrails
- Not "all music is secretly control theory." Not a replacement for music theory, ethnomusicology, or performance practice. Not a claim that groove can be computed from first principles. A diagnostic instrument, not a composition tool.
- Do not let governor/SAC language invade the paper. That's how Beethoven becomes a compliance daemon.
- Do not treat groove as just milliseconds. The empirical record supports productive mismatch but not a crude "more off-grid = more groove" law.
- This framework is strongest for groove-based, tonal, and ensemble contexts. It is weaker for musics whose aesthetics are less invested in closure, steady pulse, or shared meter. Do not explain free improv as packet loss.

## What Would Make It Strong
1. The inverted-U as the empirical coherence budget curve — if that mapping holds rigorously, the paper has a real contribution
2. The three-way debt taxonomy (closure, entrainment, coordination) — if these are genuinely orthogonal
3. The execution/retirement distinction applied to musical phrasing — if this clarifies something the existing literature doesn't
4. The generalization beyond music — if productive incoherence formalizes cleanly

## What Would Make It Weak
- Becoming "all vibes are tensors now" (Chatty's warning)
- Treating the four-layer mapping as deep rather than structural (it's a useful decomposition, not a revelation)
- Overclaiming that control theory "explains" groove (it provides a formal language; the musical knowledge is in the reference trajectories and envelope shapes, which are culturally determined)
- Ignoring the microtiming evidence mess (not all deviation is productive; quantized music is not automatically dead)

## The Hardest Question (from the falsification guardrails)

**Am I naming a real temporal structure, or am I translating musicology into control theory because it sounds cleaner?**

The test: does the four-layer decomposition + productive incoherence regime generate predictions that existing music theory doesn't? If yes, it earns its keep. If it merely re-describes known results in new vocabulary, it's translation, not contribution.

The best candidate for a genuine prediction: the inverted-U should appear at every hierarchical level with level-specific bandwidth parameters, and the bandwidth parameters should be predictable from the coupling architecture. If that's testable, the paper is real.
