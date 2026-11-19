---
name: mt-prototype
description: Molten Loop — optional step in the Agent Development Loop, between discovery and spec. Builds something fast to see or test before speccing a feature, on one of two paths. Mockup path (the default) — a frontend-only, clickable UX mockup with mocked JSON and a fake API layer, either throwaway or scaffolded as real pages in the project. Prototype path — a time-boxed technical spike that answers one risky feasibility question. Records decisions in `molten-docs/prototype/<slug>.md`. Use when the user wants to mock up, wireframe in code, preview or iterate on the UX with fake data, prototype, spike, try out, test whether something is feasible, or de-risk a feature before speccing it. Skip it when the shape and feasibility are already clear. Do not use for production implementation or backend work (use mt-build).
metadata:
  author: switch-dimension
  version: "0.4.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-optional: "true"
---

# Prototype

Build the cheapest thing that lets the user see or test the feature before anyone pays for production code. The output is learning, not shippable software.

**Optional step.** Run this only when discovery leaves a real unknown. If the shape and feasibility are already clear, skip straight to **mt-spec**.

**Input paths (all optional):** `molten-docs/discovery/<slug>.md` from **mt-discovery**, `molten-docs/design/design.md` from **mt-design**, `molten-docs/brand/brand.md` from **mt-brand**. If no discovery doc exists, ask what the user wants to see or test (or offer to run **mt-discovery** first).

**Output paths (canonical):**

- Throwaway code: `molten-docs/prototype/<slug>/` (or a clearly named throwaway branch or folder the user chooses)
- Scaffolded mockup pages: the project's own frontend, on a branch
- Decisions and learnings: `molten-docs/prototype/<slug>.md`

**Next skill:** **mt-spec**.

## Choose the path

Read the discovery doc and name the riskiest unknown. Then pick the path, confirming with the user unless it is obvious:

| Path | Use when | The question it answers | Read |
| --- | --- | --- | --- |
| **Mockup** (default) | The risk is the user experience: screens, flows, states, copy, layout | "Is this the right experience?" | `references/mockup.md` |
| **Prototype** | The risk is technical: an API, library, integration, performance or algorithm that might not work | "Can this be built the way we think?" | `references/prototype.md` |

If both are risky, do the prototype first: a mockup of something that can't be built wastes the user's time. Read only the reference file for the chosen path.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- Confirm what you are building and what "done" looks like before writing code.
- Use the cheapest medium that works. No auth, no real credentials, no polish beyond what the question needs.
- Keep throwaway code isolated from production code and never merge it in as-is. Its lasting outputs are the decisions, not the code.
- If `molten-docs/design/design.md` exists, use its tokens for any UI.
- Stop once the question is answered or the user is happy with the experience.
- Ask every question as plain numbered text in chat; for finite choices, list lettered options under the question (1a, 1b, 1c). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).

## Workflow

1. Read the inputs, name the riskiest unknown, and choose the path.
2. Follow the workflow in the chosen reference file.
3. Show it to the user (or run it with them) and iterate.
4. Write `molten-docs/prototype/<slug>.md` using the template below, and point the user to it and to **mt-spec**.

## Output template

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
type: mockup | prototype
discovery: molten-docs/discovery/<slug>.md | null
design: molten-docs/design/design.md | null
mode: throwaway | scaffold            # mockup only
location: <path, routes, or branch>
branch: <branch name> | null
molten_next_skill: mt-spec
---

# Prototype — <name>

## Question (what this set out to show or test)
## How to run it
## What was built (medium, shortcuts taken, what was deliberately faked)
## Result — answered? yes / partially / no
## Decisions for the spec
<!-- Path-specific sections from the reference file go here -->
## Open questions for the spec
```

## Done checklist

- [ ] Path (mockup or prototype) and the question confirmed before building
- [ ] Throwaway code isolated from production code; scaffolded code on a branch
- [ ] User has seen, clicked through, or run it, and feedback has been applied
- [ ] Path-specific checklist in the reference file is complete
- [ ] `molten-docs/prototype/<slug>.md` written with decisions for the spec
