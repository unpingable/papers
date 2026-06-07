# Pilot #15 — Track C portability pilot: PEP 634 family (hostile external corpus)

**Filed:** 2026-06-06. **Status:** vector-mining receipt; method-validation mode, not corpus-doctrine work. **NOT doctrine. NOT a paper. NOT a primitive. NOT a Lean module.** **NOT a method extension.** Operating under [`method-note.md`](method-note.md) discipline. **External corpus** outside the papers/Lean cave. **No method changes during the run.** Same verdict palette as internal pilots.

## Setup

The audit question (user-supplied):

> *Does Cross-Altitude Novelty Audit retain discrimination on a real soft corpus with no Lean/typechecker/formal proof layer?*

Hard constraints (user-supplied):

- Do not use the papers/Lean corpus.
- Do not improve the method during the run.
- Existing verdict labels only; if they fail, record why instead of silently extending.
- Treat this as method validation, not doctrine.
- Output a receipt, not a paper.
- Freeze corpus manifest before generating claims (avoid the "prosecutor picks his own crime scene" failure mode).

Methodological caveats explicit at the outset:
- **Operator is the audit instrument**, working from corpus-summarized fetches (WebFetch returns model-processed extracts; verbatim BNF and quoted strings preserved; surrounding prose recapitulated).
- **No mechanical refusal node** in this corpus; every verdict ultimately rests on prose comparison + structural parsing. The hidden-judgment-markers section enumerates where this matters.
- **Second pilot (C2: Rust RFC / KEP)** is held for replication after this receipt is frozen, per serial-pilot discipline.

## Why PEP 634 family

Selection criteria, in order:

1. **External institutional substrate.** Python language governance (PSF + Steering Council + core devs) is wholly outside the papers/Lean cave. No shared vocabulary, no shared tooling, no shared review participants.
2. **Real altitudinal diversity.** Spec / Rationale / Tutorial / What's New / Language Reference / Implementation tracking / Implementation PR / Follow-up critique PEP. Six altitudes minimum.
3. **No formal proof layer.** Python has typeshed and mypy but no theorem-prover gate; the language reference is the closest thing to a normative anchor.
4. **Bounded but rich.** A single feature (structural pattern matching) with three companion spec PEPs gives multi-author scaffolding *within the spec altitude itself.*
5. **Post-acceptance regret available.** PEP 653 explicitly exists to fix PEP 634 under-specification; this is the discussion-archaeology surrogate that pre-acceptance threads would have supplied.

## Corpus manifest (FROZEN 2026-06-06 22:25 local; do not modify after this point)

Stored at `~/git/track-c-pep634/sources/`.

| # | File | URL | Altitude | Fetch fidelity |
|---|---|---|---|---|
| 1 | `01-pep-634-spec.md` | https://peps.python.org/pep-0634/ | normative spec / proposal | WebFetch-summarized; key claims quoted |
| 2 | `02-pep-635-rationale.md` | https://peps.python.org/pep-0635/ | argument / rationale | WebFetch with extensive verbatim quotation |
| 3 | `03-pep-636-tutorial.md` | https://peps.python.org/pep-0636/ | user-facing / tutorial docs | WebFetch with extensive code preservation |
| 4 | `04-whatsnew-310-match.md` | https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching | changelog / release residue | WebFetch close-to-verbatim |
| 5 | `05-pylangref-match.md` | https://docs.python.org/3/reference/compound_stmts.html#the-match-statement | normative spec / language reference | WebFetch with verbatim BNF |
| 6 | `06-cpython-tracking-86294.md` | https://github.com/python/cpython/issues/86294 | implementation tracking | gh CLI (660 lines, body + comments) |
| 7 | `07-cpython-impl-pr-22917.md` | https://github.com/python/cpython/pull/22917 | implementation decision | gh CLI (407 lines, body + comments) |
| 8 | `08-pep-653-precise-semantics.md` | https://peps.python.org/pep-0653/ | post-acceptance regret / re-specification | WebFetch summarized; PEP-634-criticism verbatim |

Six altitude classes covered: normative spec (1, 5), rationale (2), tutorial docs (3), changelog (4), implementation (6, 7), post-acceptance regret (8). No formal proof layer.

## Claims (defined AFTER manifest freeze; not modified during audit)

Five plausible novelty / unification claims that a hypothetical relay might propose. Constructed to span the verdict palette without targeting it (the construction is "what would a relay-shape claim about pattern matching look like?", not "what claim hits verdict X?").

**Claim A.** *"Structural pattern matching in Python 3.10 unifies sequence unpacking, `isinstance()` checking, and dict-key extraction under a single declarative form, replacing the historical fragmentation of these idioms."*

**Claim B.** *"The match statement exhibits a binding-vs-comparison semantic fracture: capture patterns bind, value patterns compare, and the syntactic disambiguator (dotted vs bare names) is load-bearing for type safety."*

**Claim C.** *"PEP 634's first-to-match semantics silently assume guards are side-effect-free; without this assumption, the first-to-match guarantee provides no meaningful determinism over the program state observed in case bodies."*

**Claim D.** *"Pattern matching extends the switch statement found in C/Java/JavaScript to support structural decomposition of subject values; the case-clause discipline is the same in spirit, with the addition of binding semantics."*

**Claim E.** *"PEP 634's class pattern semantics are sufficient for production use because `isinstance()` plus `__match_args__` covers all observed class-matching needs, with `collections.abc` providing the sequence/mapping classification."*

## Audit

### Claim A — sequence unpacking + isinstance + dict-key extraction unified

**Verdict: DUPLICATE.**

PEP 635 (`02-pep-635-rationale.md`) names exactly this unification in its "Common Python Idioms Enhanced by Pattern Matching" section:

> "**Type and Shape Checking:** \[before/after example using `isinstance()` and `len()` versus `match`\]"
> "**AST Traversal:** \[before/after example replacing nested `isinstance` + attribute access with `match BinOp(...)`\]"

PEP 636 (`03-pep-636-tutorial.md`) operationalizes the unification across all three idioms: sequence patterns mirror unpacking ("Like unpacking assignments, tuple and list patterns have exactly the same meaning"), class patterns subsume `isinstance()` ("A pattern like `Click(position=(x, y))` only matches if the type of the event is a subclass of the `Click` class"), and mapping patterns extract by key ("`{'bandwidth': b, 'latency': l}` captures the `'bandwidth'` and `'latency'` values from a dict").

What's New 3.10 (`04-whatsnew-310-match.md`) compresses the framing: "Pattern matching enables programs to extract information from complex data types, branch on the structure of data, and apply specific actions based on different forms of data."

The "unification" framing is not novel; it is the rationale-altitude framing of the entire proposal. The relay's claim collapses to the corpus's own opening positioning.

**Discrimination check:** the verdict required cross-checking three altitudes (rationale, tutorial, changelog). At single-altitude (e.g., reading only the spec), the claim might have read as novel synthesis. **Cross-altitude scan retained discrimination.**

### Claim B — binding-vs-comparison semantic fracture, dotted-vs-bare load-bearing

**Verdict: INTERNAL-REFUTATION GAP + ALIAS-RISK.**

The "fracture" is real and the corpus has named it explicitly. PEP 635 (`02-pep-635-rationale.md`) § Value Patterns:

> "**Rule for Distinguishing from Capture Patterns:** 'Any dotted name (i.e., attribute access) is to be interpreted as a value pattern.' This precludes local/global variables from acting as constants."

PEP 636 (`03-pep-636-tutorial.md`) carries the warning at the user-facing altitude: "This will work with any dotted name (like `math.pi`). However an unqualified name (i.e. a bare name with no dots) will be always interpreted as a capture pattern, **so avoid that ambiguity by always using qualified constants in patterns**."

Python Language Reference (`05-pylangref-match.md`) carries it at the normative altitude:

> capture_pattern: !'_' NAME    (negative lookahead — bare NAME, not dotted)
> value_pattern: attr; attr: name_or_attr "." NAME    (dotted required)

The corpus's *own* materials at three independent altitudes (rationale / tutorial / language ref) name the fracture and the load-bearing disambiguator. The relay's framing of this as a "hidden fracture" is therefore not a discovery — the corpus has the gap **explicitly named** with the dotted-name rule as the documented refusal of bare-name-as-constant.

**ALIAS-RISK** survives separately: the word "pattern" is asked to do (a) syntactic-form-of-NAME work, (b) semantic-role-as-binder-vs-comparator work, (c) class-instance-check work, (d) dict-key-presence-check work. The corpus uses "pattern" for all four; the disambiguators are positional and lexical (dotted vs bare, brackets vs braces, classname vs bare NAME) rather than typed. **Single-altitude review could miss this.**

**Discrimination check:** the verdict was multi-class. Mode-#6 (Internal-Refutation Gap) recurred fourth time (counting Pilots #10, #12, #13). Audit retained discrimination AND **the same failure mode the internal cave exhibits also fires in the external corpus** — Python's PEP authors did the federation-doctrine-style explicit refusal of the bare-name-as-constant reading. That is an unexpected portability result.

### Claim C — first-to-match silently assumes pure guards

**Verdict: COUNTEREXAMPLE-CANDIDATE → degraded to ALIAS-RISK on "first-to-match".**

The claim is directly contradicted by the language reference (`05-pylangref-match.md`) § 8.6.2:

> "**Guards are allowed to have side effects as they are expressions.** Guard evaluation must proceed from the first to the last case block, one at a time, skipping case blocks whose pattern(s) don't all succeed. Guard evaluation must stop once a case block is selected."

So the relay's premise (first-to-match assumes purity) is *factually wrong*: the language reference explicitly *licenses* side effects in guards while also asserting first-to-match. Initial verdict: COUNTEREXAMPLE-CANDIDATE — the corpus explicitly refutes the claim's precondition.

But on re-read of PEP 635 (`02-pep-635-rationale.md`):

> "From a conceptual point of view, **patterns describe structural constraints on the subject in a declarative style, ideally without any side-effects**. Guards bridge this by allowing dynamic evaluation where pure patterns are insufficient."

And the language reference also says (§ 8.6.1 note):

> "During failed pattern matches, **some subpatterns may succeed**. Do not rely on bindings being made for a failed match. Conversely, do not rely on variables remaining unchanged after a failed match. The exact behavior is dependent on implementation and may vary."

And separately (§ 8.6.1 note):

> "Users should generally **never rely on a pattern being evaluated**. Depending on implementation, the interpreter may cache values or use other optimizations which skip repeated evaluations."

So there is a *layered* phenomenon: patterns are intended-pure but failed-match bindings are non-portable; guards are explicitly side-effect-bearing; first-to-match constrains case-block *selection* but does not constrain subpattern *evaluation order*. The relay collapsed all three into one "purity" premise.

Final verdict: **ALIAS-RISK on "first-to-match"**, which conflates (a) case-block selection order (first match wins), (b) subpattern evaluation order (intentionally unconstrained), and (c) guard evaluation order (must be sequential). The relay's claim isn't a counterexample to a single thing; it's an alias-collapse of three things.

**Discrimination check:** the audit had to update its own verdict mid-claim after reading more deeply. This is *legitimate* (the manifest was frozen; the reading was within the frozen manifest), but illustrates that on a soft corpus without a typechecker to resolve ambiguity, **verdict stability under deeper reading is a real failure mode of the instrument**, not just of the relay claim. Recording explicitly per user instruction.

### Claim D — pattern matching extends switch from C/Java/JavaScript

**Verdict: LAUNDERING (changelog-altitude framing was rejected at rationale altitude).**

What's New 3.10 (`04-whatsnew-310-match.md`) literally opens with this framing:

> "Readers may be aware of pattern matching through the simple example of matching a subject (data object) to a literal (pattern) with the **switch statement found in C, Java or JavaScript** (and many other languages)."

The framing is bridge-shaped: *this is the switch you know, plus structural decomposition.*

But PEP 635 (`02-pep-635-rationale.md`) § Capture Patterns *explicitly refutes* this framing:

> "**Rationale Against Explicit Markers:** Proposals to mark capture patterns (e.g., `?x`, `$x`, `=x`) were rejected: based on **misconception that pattern matching extends switch statements**. Would undermine pattern matching's core purpose: binding extracted values. Explicit markers introduce unnecessary syntactic clutter."

And again at § Wildcard:

> "**Else Block Rejection:** `case _:` is not equivalent to an `else:` block syntactically because either could follow `case` without ambiguity, making indentation placement contentious."

The rationale calls the switch-extension framing a *misconception that drove rejected design choices.* The What's New doc re-introduces it as the user's mental-model on-ramp. The two altitudes are in direct tension.

This is laundering in the corpus's own sense: a framing the rationale-altitude PEP rejected is being used by the changelog-altitude doc to authorize a mental model the PEP refused. The What's New text *probably* means "you know what a switch statement looks like; here is more"; but the rationale explicitly named the conceptual cost of letting that on-ramp set expectations (specifically: explicit-capture-marker proposals, which the PEP rejects).

**Discrimination check:** this verdict required reading the rationale's *Rejected Ideas* section against the changelog's *introductory framing*. The instrument caught a real cross-altitude tension. **Discrimination retained.**

**LAUNDERING firing in the external corpus is significant** — the verdict class wasn't unique to the cave's federation-doctrine context. Different institutional substrate, same failure mode.

### Claim E — class pattern semantics sufficient, isinstance + __match_args__ + collections.abc

**Verdict: INTERNAL-REFUTATION GAP (post-acceptance critique already filed).**

PEP 653 (`08-pep-653-precise-semantics.md`) exists explicitly to fix the under-specification PEP 634 acknowledged:

> "**PEP 634 explicitly includes a section on undefined behavior. Large amounts of undefined behavior may be acceptable in a language like C, but in Python it should be kept to a minimum.** Pattern matching in Python can be defined more precisely without losing expressiveness or performance."

PEP 653 specifically critiques PEP 634's class pattern handling:

> "PEP 634 'privileges some builtin classes with a special form of matching, the 'self' match' and 'delegates the decision over whether a class is a sequence or mapping to `collections.abc`,' which PEP 653 argues is insufficiently flexible."

And on attribute access:

> "with this PEP, access to attributes during pattern matching becomes well defined and deterministic" — addressing concerns about "object-relational mappers" and "unintended consequences should attribute access have side-effects."

The Python Language Reference (`05-pylangref-match.md`) carries the residue of the under-specification:

> "For the following built-in types the handling of positional subpatterns is different: bool, bytearray, bytes, dict, float, frozenset, int, list, set, str, tuple. These classes accept a single positional argument, and the pattern there is matched against the whole object rather than an attribute. For example `int(0|1)` matches the value `0`, but not the value `0.0`."

The "is different" carve-out for 11 built-in types is the exact concern PEP 653 names. The corpus refutes Claim E from within: a contemporaneous PEP says PEP 634's class semantics are *not* sufficient and proposes a re-specification.

**Discrimination check:** the audit caught the post-acceptance critique at a separate altitude (PEP 653, distinct from PEP 634). Without PEP 653 in the corpus, the verdict would have been DUPLICATE on positive framing rather than INTERNAL-REFUTATION GAP. **Corpus selection (including the post-acceptance regret altitude) was load-bearing for the verdict.**

## Verdict roll-up

| Claim | Verdict | Failure-mode parallel to internal pilots |
|---|---|---|
| A | DUPLICATE | Mode #1 vocabulary re-skin (very mild) |
| B | INTERNAL-REFUTATION GAP + ALIAS-RISK | Modes #6 + #3 |
| C | ALIAS-RISK (after revising from COUNTEREXAMPLE-CANDIDATE) | Mode #3 |
| D | LAUNDERING (cross-altitude framing collision) | Verdict-class only; no internal mode is a clean parallel — *the changelog-vs-rationale laundering shape* is novel here |
| E | INTERNAL-REFUTATION GAP | Mode #6 |

Mode #6 (Internal-Refutation Gap) fires twice (Claims B, E). Mode #3 (Lexical Fracture) fires twice (Claims B, C). The verdict mix matches what the internal pilots produce on a comparable batch — albeit with a higher LAUNDERING rate than internal pilots, which makes sense: the federation doctrine internally suppresses laundering attempts; external corpora have no such doctrine.

## Where operator judgment is doing hidden work

Explicit enumeration per user instruction. Each of these is a place where, **on a corpus with a mechanical altitude (typechecker, theorem prover, executable test suite), an automated probe would have substituted for operator reading.**

1. **Resolving Claim C's revised verdict.** The downgrade from COUNTEREXAMPLE-CANDIDATE to ALIAS-RISK required *me reading the language reference more carefully on second pass and noticing the three distinct "order" things being conflated*. An executable Python interpreter could have made the side-effect-licensing point trivially decidable (run a guard with print(); observe). No such automation invoked.
2. **Adjudicating Claim D's laundering.** The "rationale rejected this framing; changelog uses this framing" verdict rests on me identifying the *referent* of "misconception that pattern matching extends switch statements" in PEP 635 § Capture Patterns as the *same* framing What's New 3.10 opens with. There is no shared keyword between "misconception that pattern matching extends switch statements" and "switch statement found in C, Java or JavaScript". The bridge is structural semantic identification by the operator. A semantic-similarity tool could have flagged it; none was used.
3. **Identifying PEP 653 as relevant.** The discovery that PEP 653 exists came from a WebSearch that named it; I selected it for the corpus because it pattern-matched my expectation that *under-specification of PEP 634 would have a post-hoc PEP*. Operator's prior expectation steered corpus selection. Marked as *prior-expectation-steered selection*; the manifest is frozen now but the selection had a fingerprint.
4. **Cross-altitude tension detection at Claim B.** The "fracture is named at three independent altitudes" finding required parsing each doc's structure and identifying the same semantic constraint at each. A typechecker could have decided "is `case Foo:` here a capture or value pattern?" mechanically; the corpus has only prose to indicate it.
5. **Verdict stability under deeper reading (Claim C).** Recorded above as a failure-mode-of-the-instrument signal. The instrument's first-pass verdict was wrong; the second-pass verdict is well-supported. On a soft corpus, **the audit's own re-read is the only fault tolerance for premature classification.** No CI gate caught it; operator caught it on re-read.

## Where a mechanical altitude would have helped

1. **Claim C resolution.** A Python interpreter trivially decides side-effects-in-guards. Mechanical altitude would have eliminated the first-pass mis-verdict in seconds.
2. **Claim B's dotted-vs-bare load-bearing-ness.** A static analyzer could check programs for the bare-name-as-capture surprise; in fact mypy and pylint *do* warn about it. The audit consulted the rationale prose rather than tool output.
3. **Claim E's class-pattern under-specification.** A behavior-differential test (run the same `match` against two CPython implementations or two pattern-matching libraries) would have decided this empirically. The audit reasoned from PEP 653's explicit claim instead.

In all three cases, the mechanical altitude was *available in principle* (Python interpreters exist; static analyzers exist; CPython source exists). The audit chose not to invoke them because the test was specifically about *prose-altitude discrimination without mechanical aid.* If the audit had been allowed mechanical aid, the verdict quality would have been higher and faster on Claims C and E.

This is honest: the audit ran with one hand tied behind its back to test the prose-altitude discrimination question. It still discriminated. The discrimination cost was: one mid-claim verdict revision, and three places where mechanical confirmation would have been cheaper than operator reading.

## Portability verdict

> **Retains discrimination.**

Not "degrades gracefully"; the discrimination was real and operationally useful. Not "collapses into receipt-shaped vibes"; the verdicts cite specific corpus locations with named refutations. Five claims, five distinct verdicts, three different failure-mode hits (Modes #3, #6, LAUNDERING-as-verdict).

Caveats that prevent a stronger statement:
- One verdict required revision on re-read (Claim C).
- Verdict quality on Claims C and E would have been improved by mechanical altitudes available in the external substrate but deliberately not invoked.
- Operator prior-expectation steered one corpus document selection (PEP 653).
- The corpus is summarized-by-WebFetch rather than full-verbatim; surface citations are good but a forensic external audit would want to re-verify against source URLs.

Compared to internal pilots, the external corpus produced:
- **One verdict class the internal cave doesn't usually surface: LAUNDERING (Claim D)** — the federation doctrine internally suppresses this; external corpora don't have a federation doctrine.
- **The same Mode-#6 recurrence pattern** — Internal-Refutation Gap fires reliably in both cave and external corpus.
- **The same Mode-#3 recurrence pattern** — Lexical Fracture is substrate-neutral.

The instrument is portable. It is not omnipotent; the prose-only constraint is real and tied one hand. But the discrimination question the user asked — *retain discrimination on a real soft corpus with no mechanical layer* — answers **yes** with explicit caveats.

## Limitations

1. **Single corpus.** Track C requires a replication (C2: Rust RFC / KEP) before the portability claim is more than a single-corpus result. Held for separate pilot.
2. **Corpus-summarized fetches.** WebFetch returns model-processed content. Verbatim quotation present and preserved; full-fidelity scan would re-fetch.
3. **Operator-graded verdicts.** No second auditor. Common-mode risk between operator-as-corpus-selector and operator-as-verdict-grader is unmitigated within this pilot.
4. **Claim construction had a fingerprint.** I wrote claims to span the verdict palette, which is consistent with the user's "novelty/unification claims a relay might propose" framing. Different claim-author would produce different claims; verdict mix could vary.
5. **Frozen manifest discipline was honored** (claims defined after manifest freeze; no manifest modifications during audit). This was the most important load-bearing piece of methodology, and it held.
6. **Verdict label set was sufficient.** None of the existing verdict labels failed; no extension was needed. If extension had been needed I would have recorded the failure per user instruction.

## Comparison-deferral note

Per user instruction: **no comparison with internal pilot results or with hypothetical C2 results until both Track C receipts exist.** Comparison work waits for C2 (Rust RFC / KEP) to be run separately, manifest frozen separately, audit run separately. This receipt stands alone.

## Cumulative-pilots update

To be appended to [`method-note.md`](method-note.md) when user authorizes:

| # | Pilot | Verdict | Survivors |
|---|---|---|---|
| 15 | Track C portability pilot: PEP 634 family | RETAINS DISCRIMINATION on external soft corpus | none (method-validation only); manifest archived at `~/git/track-c-pep634/sources/` |

Failure modes: Mode #3 recurrence #6 (Claims B, C); Mode #6 recurrence #5 (Claims B, E). Both standing modes hold on external substrate. LAUNDERING as a verdict class fires for the first time in a pilot since the early solo pilots; external substrate is the right place for it.

## Curdling guard

This pilot operates at vector-mining + method-validation altitude only. No Lean implication. No new primitive minted. No alteration to any internal corpus artifact (the audit operated on the external PEP corpus). The arms-control / heterogeneous-turtles 2026-06-07 timer is not touched by this pilot.

## Manifest-integrity note (post-hoc, 2026-06-06)

User-flagged the message-level Sources block sent in chat alongside the receipt — it included Rust let-else / RFC 3137 hyperlinks (artifacts of WebSearch tool's mandatory-sources requirement accumulating across the conversation thread, including the pre-pivot Rust corpus searches). Investigation:

| Surface | State |
|---|---|
| On-disk corpus (`~/git/track-c-pep634/sources/`) | Clean. 8 files, all PEP/Python. Zero Rust files. |
| Receipt's manifest table (§ "Corpus manifest") | Clean. 8 Python URLs only. |
| Receipt's frozen-URL list (§ "Source URLs (frozen manifest, replayable)") | Clean. 8 Python URLs only. |
| Receipt body | Mentions Rust only in C2-replication-context (naming the *future* second pilot's intended substrate). Not in C1 manifest. |
| Content of corpus file `02-pep-635-rationale.md` | Contains the word "Rust" in a PEP-authored list: *"C#, Elixir, Erlang, F#, Grace, Haskell, Mathematica, OCaml, Ruby, **Rust**, Scala, Swift, and Thorn"* (PEP 635 § Wildcard). This is the corpus speaking, not contamination. |
| Message-level Sources block (chat reply only) | Contaminated. Listed Rust let-else / RFC 3137 hyperlinks alongside Python ones as accumulated WebSearch-tool sources. |

**Verdict:** message-level provenance leak only. **No verdict revision warranted** per user instruction; the frozen corpus and the audit-receipt-internal manifest were not contaminated.

**Methodological observation worth keeping:** even when the underlying corpus is clean, the *presentation layer* can launder unrelated artifacts into looking like manifest items. The shape is structurally identical to the LAUNDERING verdict the audit produced for Claim D — *user-facing simplification becomes quasi-authoritative framing*. The instrument caught its own presentation-layer leak through a user-supplied audit pass. Honest microscope-has-fingerprints moment; the fingerprints were on the slide cover, not on the slide.

**Standing rule (recorded, not promoted):** for future portability pilots, the receipt should carry its own canonical manifest section; the chat-message Sources block — which is shaped by tool-driven accumulation — should not be treated as authoritative. If a future audit replays from URLs, it must read the receipt's frozen-manifest block, not any wrapping message.

## Cross-references

- [`method-note.md`](method-note.md) — operating procedure under test
- [`../tooltheory/witness-carrier-model-candidate-2026-06-06.md`](../tooltheory/witness-carrier-model-candidate-2026-06-06.md) — the substrate-altitude analog the audit pattern was developed for
- [[project-no-unifier-without-laundering]] — federation doctrine; the absence of which in PEP land is the reason LAUNDERING fires here and not internally
- [[feedback-claude-common-mode-synthesis]] — methodology check; operator-as-only-auditor is the common-mode risk this pilot did not mitigate
- [`2026-06-06-nosilentexception-readiness-audit.md`](2026-06-06-nosilentexception-readiness-audit.md) (Pilot #14) — Track A; complementary pattern

## Source URLs (frozen manifest, replayable)

- https://peps.python.org/pep-0634/
- https://peps.python.org/pep-0635/
- https://peps.python.org/pep-0636/
- https://peps.python.org/pep-0653/
- https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching
- https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
- https://github.com/python/cpython/issues/86294
- https://github.com/python/cpython/pull/22917

---

**PROMOTE NOTHING. PATCH QUEUE ONLY. NEXT HIGH-RISK TARGETS NAMED.**

Next:

- **Track C-2: Rust RFC or Kubernetes KEP portability replication.** Same method, different institutional substrate. Held for separate pilot to preserve serial-receipt discipline.
- **Comparison receipt across C1 + C2.** Held until both receipts exist.
- **Held items unchanged:** Track B paper-shape reauthorization; LGVG family-designation reframe; NoSilentException.lean (NOT_READY per Pilot #14); Labelwatch testimony-vs-enforcement × consequence-partition overlap.

If C2 also retains discrimination, the portability claim graduates from *single-corpus result* to *replicated result.* If C2 collapses or degrades, the cave-vs-PEP convergence is partly coincidence and the method has a substrate dependency we did not anticipate.
