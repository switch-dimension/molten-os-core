---
name: mt-spec
description: Molten OS Core — third step of the Agent Development Loop. Turns discovery and prototype learnings into a clear, testable feature spec — requirements, user stories, acceptance criteria, data and API shape, edge cases, and non-goals — written to `molten-docs/spec/<slug>.md`. Use when the user wants a spec, PRD, requirements doc, or acceptance criteria for a feature. Do not use for task breakdown (use mt-plan).
metadata:
  author: switch-dimension
  version: "0.1.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-order: "3"
---

# Spec

Define **what** will be built and how we'll know it works. The spec is the contract between the human and the agent doing the implementation.

**Input paths:** `molten-docs/discovery/<slug>.md` (from **mt-discovery**) and `molten-docs/prototype/<slug>.md` (from **mt-prototype**) when present. If neither exists, gather the essentials directly or offer to run **mt-discovery** first.

**Output path (canonical):** `molten-docs/spec/<slug>.md`. Create the directory if it does not exist.

**Next skill:** **mt-plan**.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- Describe behaviour, not implementation. Leave file-level and task-level decisions to **mt-plan**.
- Every requirement must be testable. Rewrite vague requirements ("fast", "intuitive") into observable criteria.
- Carry forward prototype decisions; flag any spec item that contradicts them.
- Keep open questions visible — do not silently resolve them with guesses.
- Ask every question as plain numbered text in chat; for finite choices, list lettered options under the question (1a, 1b, 1c). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).
- Do not write application code while this skill is active.

## Workflow

1. Read discovery, prototype learnings, and relevant code.
2. Draft the spec using the template below.
3. Review gaps with the user: missing edge cases, unclear acceptance criteria, unresolved questions.
4. Finalise and write the spec; point the user to the file.

## Output template

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
status: draft | approved
discovery: molten-docs/discovery/<slug>.md
prototype: molten-docs/prototype/<slug>.md | null
molten_next_skill: mt-plan
---

# Spec — <name>

## Summary
## Goals
## Non-goals
## User stories
## Functional requirements
## Acceptance criteria (Given / When / Then)
## Data model & API shape
## UX notes (link design.md / prototype where relevant)
## Edge cases & error states
## Non-functional requirements (performance, security, accessibility)
## Open questions
```

## Done checklist

- [ ] Every requirement has at least one acceptance criterion
- [ ] Non-goals listed
- [ ] Edge cases and error states covered
- [ ] Open questions visible, not guessed
- [ ] `molten-docs/spec/<slug>.md` written; status set to `approved` once the user signs off
