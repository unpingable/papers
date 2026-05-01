# Preemptive Naming

**Status:** meta-doctrine (not active primitive — design-governance level, per chatty's level call 2026-05-01)
**Originated:** 2026-05-01 (user identification mid-session; multi-model synthesis with chatty + claude-code)
**Primary home:** no paper home — meta-discipline / design-governance
**Shelf:** sibling to `design-basis-erasure.md` (design-governance lane), not a system primitive like standing / continuity / basis / directness

## Keeper

> Deferred naming is not neutral when retrofit cost is high.

Adjacent line:

> If you wait too long to name a surface, implementation will name it badly for you.

## Pointer-shape, not doctrine restatement

This file *names* a discipline that already lives in two canonical places. It does not restate the doctrine — it indexes the surface so the discipline has a referent.

**Canonical statements:**

- `~/.claude/CLAUDE.md` ("YAGNI scope" section): "for architectural surfaces where retrofit cost rises with usage spread — APIs, schemas, permission boundaries, provider interfaces, wire formats, cross-module vocabulary — name the candidate early in a lightweight record... A record is not authorization to build. It is a handle for review. Name early. Ratify lazily. Implement only when the current task, failure mode or acceptance criteria justify it."
- `memory/feedback-name-early.md`: in theory work, the abstraction is *how* you discover the recurrence; naming-after-the-fact has asymptotic, not constant, cost.

This file is the operational *positive form* of those principles — the working law extracted from the YAGNI exception clause.

## Failure shape

The pattern Preemptive Naming guards against:

1. A surface exists in practice (load-bearing, used across modules / agents / docs).
2. Nobody wants to "prematurely abstract" it.
3. It stays unnamed.
4. Implementation pressure arrives.
5. The wrong layer names the surface first — usually the layer with the loudest bug.
6. Semantics get accidentally baked in at that wrong layer.
7. Cleanup later is more expensive than early naming would have been; the surface is now load-bearing in two places, and one of them is wrong.

The cost asymmetry is the load-bearing part. If the surface is *not* load-bearing across spread, deferred naming is cheap. If it is, deferred naming is silently capitalizing future debt.

## Three-term placement (and the third term is this primitive)

From `feedback-forcing-case.md`'s three-term vocabulary:

- **Forcing case.** Reality made the abstraction non-optional. (Disaster ratifies.)
- **Default future work.** Obvious next ladder step. Not forced, just next.
- **Preemptive naming.** No catastrophe yet, but the surface is load-bearing enough that waiting is *actively* unsafe. (Retrofit cost ratifies.)

The first two are already named in `feedback-forcing-case.md`. This file names the third explicitly so it stops being "the unnamed thing in the gap between forcing case and default future work."

## Operational corollary

The discriminating question, when an unnamed surface appears:

> Is the retrofit cost high enough that waiting is actively unsafe — even without a forcing case?

If yes, file the lightweight record now (gap-spec, candidate note, doctrine stub, working primitive, memory pointer, working/ note — whichever fits). The record is *not* implementation. It is a handle.

If no, default future work.

## Promotion gate

Held at meta-doctrine, not active primitive. Promote to active primitive only if the failure shape recurs as an *object-level* failure across multiple contexts in a way the existing CLAUDE.md / feedback-name-early statements miss. Until then, this file indexes the surface and lets the canonical statements carry the doctrine.

## Open

- The keeper line *deferred naming is not neutral when retrofit cost is high* is the candidate epigraph if this ever earns a paper home; otherwise it stays as the working-doctrine handle.
- Whether this graduates from meta-doctrine to active primitive is a separate decision and should *not* happen automatically just because someone (this file's author included) finds the framing satisfying.
