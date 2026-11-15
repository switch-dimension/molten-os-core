---
name: mt-plan
description: Molten OS Core — fourth step of the Agent Development Loop. Converts an approved spec into an ordered, agent-executable implementation plan — phases, small verifiable tasks, files to touch, tests, and checkpoints — written to `molten-docs/plan/<slug>.md`. Use when the user wants an implementation plan, task breakdown, build plan, or "how should we build this". Do not use to define requirements (use mt-spec).
metadata:
  author: switch-dimension
  version: "0.1.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-order: "4"
---

# Plan

Define **how** the spec gets built, in small steps an agent can execute and verify one at a time.

**Input path:** `molten-docs/spec/<slug>.md` from **mt-spec**. If missing or still `draft`, recommend finishing **mt-spec** first; proceed only if the user insists, and note the risk in the plan.

**Output path (canonical):** `molten-docs/plan/<slug>.md`. Create the directory if it does not exist.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- Read the codebase before planning. Name real files, modules, and patterns — not hypothetical ones.
- Break work into tasks that each fit in one focused agent session and end in a verifiable state (tests pass, page renders, endpoint responds).
- Every task maps back to one or more spec acceptance criteria.
- Order tasks so the riskiest or most foundational work comes first and the app stays runnable between tasks.
- Include a test or verification step for each task.
- Number every free-text question asked in chat; use the agent's structured question tool (`AskUserQuestion`, `AskQuestion`, `request_user_input`) for finite choices.
- Do not start implementing while this skill is active — hand off once the plan is approved.

## Workflow

1. Read the spec, prototype learnings, and the relevant code.
2. Identify architecture decisions and dependencies (new packages, migrations, env vars).
3. Group work into phases; break phases into checklist tasks.
4. Review with the user — sequencing, scope per task, anything missing.
5. Write the plan and point the user to the file.

## Output template

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
spec: molten-docs/spec/<slug>.md
status: draft | approved | in-progress | done
---

# Plan — <name>

## Approach
## Architecture decisions
## Dependencies & setup (packages, migrations, env vars)

## Phase 1 — <name>
- [ ] **1.1 <task>** — files: `…` · covers: AC-1 · verify: <test/command/check>
- [ ] **1.2 <task>** — …

## Phase 2 — <name>
- [ ] …

## Risks & mitigations
## Definition of done (all acceptance criteria verified)
```

## Done checklist

- [ ] Every spec acceptance criterion is covered by at least one task
- [ ] Each task names real files and a verification step
- [ ] Tasks ordered so the app stays runnable
- [ ] `molten-docs/plan/<slug>.md` written; status set to `approved` once the user signs off
