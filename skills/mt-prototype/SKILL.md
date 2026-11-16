---
name: mt-prototype
description: Molten OS Core — optional step in the Agent Development Loop, between discovery and spec. Builds a fast, throwaway prototype to answer the riskiest question from discovery (UX, flow, or technical feasibility), then records what was learned in `molten-docs/prototype/<slug>.md`. Use when the user wants to prototype, spike, try out, or de-risk a feature before speccing it. Skip it when the shape and feasibility are already clear. Do not use for production implementation, or for a clickable whole-feature UX mockup with fake data (use mt-mockup).
metadata:
  author: switch-dimension
  version: "0.2.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-optional: "true"
---

# Prototype

Build the smallest thing that answers the riskiest question. Prototypes are for learning, not shipping.

**Optional step.** Run this only when discovery leaves a real unknown — usually technical feasibility or one risky interaction. If the shape is already clear, skip straight to **mt-spec**.

**Input path:** `molten-docs/discovery/<slug>.md` from **mt-discovery**. If missing, ask for the question the prototype must answer (or offer to run **mt-discovery** first).

**Output paths (canonical):**

- Prototype code: `molten-docs/prototype/<slug>/` (or a clearly named throwaway branch/folder the user chooses)
- Learnings: `molten-docs/prototype/<slug>.md`

**Next skill:** **mt-spec**.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- State the **one question** the prototype answers before building anything. Confirm it with the user.
- Choose the cheapest medium that answers it:
  - **UX / flow question** → clickable HTML mock or minimal UI
  - **Feasibility question** → technical spike (script, API call, minimal integration)
- Time-box it. Prefer hardcoded data, no auth, no tests, no polish.
- Keep prototype code isolated from production code. Never merge it in as-is.
- If `molten-docs/design/design.md` exists, use its tokens for UI prototypes.
- Ask every question as plain numbered text in chat; for finite choices, list lettered options under the question (1a, 1b, 1c). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).

## Workflow

1. Read the discovery doc and extract the riskiest unknown.
2. Write the prototype question and success criteria ("we'll know X if Y").
3. Pick the medium and build the minimum prototype.
4. Run or show it to the user; collect reactions.
5. Iterate at most a couple of times — stop once the question is answered.
6. Write the learnings doc and point the user to it.

## Output template

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
discovery: molten-docs/discovery/<slug>.md
prototype_location: <path or branch>
molten_next_skill: mt-spec
---

# Prototype — <name>

## Question
## Approach (medium, what was built, shortcuts taken)
## Result — answered? yes / partially / no
## What we learned
## Decisions for the spec
## Remaining unknowns
```

## Done checklist

- [ ] Single prototype question confirmed before building
- [ ] Prototype isolated from production code
- [ ] User has seen or run the prototype
- [ ] `molten-docs/prototype/<slug>.md` written with decisions for the spec
