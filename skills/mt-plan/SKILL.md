---
name: mt-plan
description: Molten OS Core — third step of the Agent Development Loop. Breaks an approved spec into an ordered, agent-executable implementation plan — vertical-slice tasks with acceptance criteria, dependencies, files to touch, verification steps, and checkpoints — written to `molten-docs/plan/<slug>.md`. Use when the user wants an implementation plan, task breakdown, build plan, or "how should we build this". Do not use to define requirements (use mt-spec).
metadata:
  author: switch-dimension
  version: "0.2.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-order: "3"
---

# Plan

Define **how** the spec gets built, in small steps an agent can execute and verify one at a time. A good plan makes the build boring: every task is obvious, small, and checkable.

**Input path:** `molten-docs/spec/<slug>.md` from **mt-spec**. If missing or still `draft`, recommend finishing **mt-spec** first; proceed only if the user insists, and note the risk in the plan.

**Output path (canonical):** `molten-docs/plan/<slug>.md`. Create the directory if it does not exist.

**Next skill:** **mt-build**.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- Read the codebase before planning. Name real files, modules, and patterns — not hypothetical ones.
- Plan in **read-only mode**: no edits to application code while planning.
- Slice **vertically**, not horizontally. Each task delivers one thin working path through the stack (UI → logic → data), not "all the database, then all the API, then all the UI".
- Size tasks to fit one focused agent session, touch roughly 1–5 files, and end in a verifiable state (tests pass, page renders, endpoint responds). If a task needs "and" to describe it, split it. If you cannot state its done-condition in one sentence, it is too big.
- Every task maps back to one or more spec acceptance criteria (AC-n). Every AC is covered by at least one task.
- Map dependencies, then order so foundations and the riskiest work come first and the app stays runnable between tasks.
- Put a **checkpoint** after each phase: full test run, manual smoke check, and a chance for the human to redirect.
- Include a test or verification step for each task.
- Ask every question as plain numbered text in chat; for finite choices, list lettered options under the question (1a, 1b, 1c). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).
- Do not start implementing while this skill is active — hand off once the plan is approved.

## Workflow

1. Read the spec, prototype learnings, and the relevant code.
2. Identify architecture decisions and dependencies (new packages, migrations, env vars).
3. Draft the dependency order, then group work into phases and break phases into checklist tasks.
4. Review with the user — sequencing, scope per task, anything missing, anything that can be cut.
5. Write the plan and point the user to the file. Set `status: approved` only on explicit sign-off.

## Output template

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
spec: molten-docs/spec/<slug>.md
status: draft | approved | in-progress | done
molten_next_skill: mt-build
---

# Plan — <name>

## Approach
## Architecture decisions
## Dependencies & setup (packages, migrations, env vars)

## Phase 1 — <name>
- [ ] **1.1 <task>** — files: `…` · covers: AC-1 · depends on: — · verify: <test/command/check>
- [ ] **1.2 <task>** — …
- **Checkpoint 1:** tests green, app runs, <manual check>

## Phase 2 — <name>
- [ ] …
- **Checkpoint 2:** …

## Risks & mitigations
## Definition of done (all acceptance criteria verified)
```

## Done checklist

- [ ] Every spec acceptance criterion is covered by at least one task
- [ ] Each task names real files, a done-condition, and a verification step
- [ ] Tasks are vertical slices ordered by dependency so the app stays runnable
- [ ] A checkpoint closes each phase
- [ ] `molten-docs/plan/<slug>.md` written; status set to `approved` once the user signs off

## Extending

Common additions: effort estimates per task, parallelisable-task markers for multi-agent builds, rollout/feature-flag steps, or exporting tasks to Linear or GitHub issues.
