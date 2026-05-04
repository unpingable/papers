# Finder-Generator Inversion

**Status:** candidate
**Kind:** transition
**Originated:** 2026-05-03 (chatty surfaced during a session-internal self-audit — the primitive-detector was running hot enough that "what we are doing right now" became a load-bearing instance)
**Primary home:** no current paper home — cross-cutting meta-discipline; the ontology layer over the rest of the field notebook

## Settled status

> Finder-Generator Inversion is a specialized transition primitive: a detector / recognition system crosses into production when detection increases the supply, salience, or legitimacy of the thing detected. It descends from misplaced-concreteness / map–territory warnings and sits beside Goodhart-style measurement capture and Scott-style legibility failures, but differs by mechanism: **role transition rather than target substitution or administrative simplification.**

## Aphorisms (keepers)

> *A detector becomes dangerous when detection becomes a production function.*
>
> *The map starts charging rent to the territory.*
>
> *Don't mistake every address on the map for a new country.*

## Formal-ish shape

Two configurations of the same recognition system:

- **Detector mode.** A function $D : \text{Phenomenon} \to \{0, 1\}$ classifies whether each candidate instance exhibits the pattern. $D$'s operation does not change the rate, salience, or institutional legitimacy of the underlying phenomenon; it merely records.
- **Generator mode (post-inversion).** $D$ continues to classify, but its operation now feeds back into the supply: detected instances acquire visibility, status, taxonomic real estate, or budgetary affordance, raising the rate at which similar instances are produced (or labeled, or pursued, or proposed).

The inversion occurs when the institutional, incentive, or interpretive context around $D$ converts detection into a production function. The classifier's signature is unchanged; the system's role for it has flipped.

## Failure predicate

If the detector's continued operation increases the supply, salience, or legitimacy of the thing it was built to detect — as a *consequence* of detection rather than as feedback through an independent causal channel — the finder has become part of the generator.

Tighter operational form: *If removing the detector would decrease the rate, visibility, or institutional weight of the phenomenon (as opposed to merely reducing measurement of it), the inversion has occurred.*

## Non-case

A detector that passively identifies independently occurring events without increasing their production, institutional reward, or interpretive availability. Example: a thermometer in a sealed room. The reading exists; the room temperature does not respond to being measured. (This is also the limit case the older measurement-paradox literature was reasoning about.)

## Distinctness from neighboring failure modes

| Neighbor | Mechanism | F-G-I differs because |
|---|---|---|
| **Goodhart / Campbell** | Measurement becomes target; optimization pressure gamesthe measure | Goodhart is an **attractor** on the measurement axis (the measure was always a measure; pressure shifts incentives). F-G-I is a **transition** on the role axis (the detector becomes a producer). |
| **Whitehead — fallacy of misplaced concreteness** | Abstractions taken as concrete reality | Whitehead is the **parent shape**. F-G-I is a specialized child: the abstraction in question is specifically a *coordinate in a recognition system*, and the failure produces *more of the named thing*. |
| **Scott / legibility** | Administrative simplifications imposed back on the world | Scott is the political-power cousin: legibility-becomes-power. F-G-I narrows to the recognition→production mechanic without requiring administrative authority. |
| **Korzybski / map–territory** | Confusing representation with reality | Too general. F-G-I is finer-grained: not "map vs territory" but "address on a map vs new country." |
| **Newell & Simon — problem-space search** | Search through a representation can dominate the phenomenon | Cognitive-science precursor; F-G-I extends to institutional and taxonomic settings, not just individual cognition. |
| **Ashby / Beer — requisite variety** | Controller needs sufficient variety to regulate | The trap is reading "model enough states" as a warrant for control authority. F-G-I names a specific way that warrant fails: the modeler starts producing what they were modeling. |

## Symptoms

- Every clever phrase becomes a candidate primitive / category / KPI / vulnerability class.
- Distinctness arguments thin out; new entries quote-back existing axes with new labels.
- The directory / metric / benchmark / category-system grows faster than its diagnostic capacity.
- Removing the detector would visibly reduce the supply of detected things, not just measurement of them.

## Cross-domain instances

- **Metrics:** KPI tracking starts shaping work to produce KPI-friendly behavior (Goodhart-adjacent attractor following the F-G-I transition).
- **Moderation:** category creation gives users a new identity / game surface; the moderation taxonomy generates the genres it was built to regulate.
- **Academia:** "gap in the literature" detection becomes gap manufacturing.
- **Consulting:** diagnostic frameworks generate demand for their own remediation.
- **Security:** vulnerability classes become bounty-hunting genres.
- **AI evals:** benchmark discovery becomes benchmark overfitting; evaluation surfaces become production targets.
- **AI / proof economy** (Bessis): theorem-production benchmark crosses into producing-mathematics-the-benchmark-rewards.
- **Self-application (this directory):** the primitive-detector starts producing candidate primitives because every axis combination becomes nameable. Discovered the pattern in itself; the discovery itself is a (modest) instance.

## Architectural rules

- **Diagnostic, not generative.** The state-space view that surfaced F-G-I is an audit surface, not a production engine. Use it to *explain* candidates, not *manufacture* them.
- **Ratification gate** (`feedback-primitive-ratification-gate.md` in project memory) governs the immune system. F-G-I is the named mechanism the gate is designed against.
- **Phase-mode discipline:** exploration / ratification / canon / quarantine. The madness starts when exploration artifacts get legislative authority.

## Do not confuse with

- **Goodhart's Law.** Different kind (attractor vs transition). Goodhart describes the *pressure on a measure once it is a target*; F-G-I describes the *role flip from detector to producer*. The two compose: F-G-I is often the upstream transition that creates the target Goodhart then captures.
- **Performativity** (Austin / MacKenzie). Performative speech-acts make their referent true. F-G-I is narrower: the recognition system *increases the supply* of the referent; it does not necessarily make new instances *true* in a speech-act sense.
- **Self-fulfilling prophecy.** SFP is about belief → behavior → confirmation. F-G-I is about detection-as-production via institutional / incentive / interpretive context, not necessarily via belief.

## Minimal example

A taxonomy is created to classify failure modes. The taxonomy is useful: it prevents duplicate vocabulary, surfaces shared structure, gives orientation. Once the taxonomy is present, every clever observation becomes a candidate entry. The taxonomy's operation now produces taxonomy entries, including ones that are merely coordinates produced by combining existing axes. The detector has become a generator. The cure is not destroying the taxonomy; it is *not running its combinatorics unless a real case forces it*.

(This is the example that produced the primitive. Yes, the dragon is eating its tail. That's the point.)
