---
name: mt-plan
description: Molten Loop — third step of the Agent Development Loop. Breaks an approved spec into an ordered, agent-executable implementation plan — vertical-slice tasks with acceptance criteria, dependencies, files to touch, verification steps, checkpoints, and parallel waves showing which tasks can run at the same time — written to `molten-docs/plan/<slug>.md`. Detects the project's issue tracker (GitHub Issues, Linear, Jira), records it in `molten-docs/config.md`, and on approval creates one issue per task with blocking links. The tracker is then the single source of truth for tasks, and the plan only links to them. With no tracker, the plan file holds the tasks. Use when the user wants an implementation plan, task breakdown, build plan, tickets or issues for a feature, or "how should we build this". Do not use to define requirements (use mt-spec).
metadata:
  author: switch-dimension
  version: "0.4.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-order: "3"
---

# Plan

Define **how** the spec gets built, in small steps an agent can execute and verify one at a time. A good plan makes the build boring: every task is obvious, small, and checkable.

**Input paths:** `molten-docs/spec/<slug>.md` from **mt-spec**. If missing or still `draft`, recommend finishing **mt-spec** first; proceed only if the user insists, and note the risk in the plan. Also `molten-docs/config.md` if it exists.

**Output paths (canonical):**

- `molten-docs/plan/<slug>.md` — the plan. Create the directory if it does not exist.
- `molten-docs/config.md` — issue-tracker settings, written once per project (see Issue tracker).
- Issues in the project's tracker, when one is used.

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

## Parallel waves

The plan gives a safe order for one agent **and** shows which tasks can run at the same time, so several agents or people can work the same plan.

- Two tasks are **parallel-safe** only when neither depends on the other **and** their `files` lists do not overlap. Shared files (a router, a schema, a config file) cause merge conflicts: add a dependency or keep them in different waves.
- Group tasks into **waves**. Wave 1 holds tasks with no dependencies; each later wave holds tasks whose dependencies are all in earlier waves. Tasks in the same wave are parallel-safe with each other.
- Do not split work just to make it parallel. Two or three serial tasks are often right for a small feature; a single-task wave is fine.
- Checkpoints still close each phase. A wave never spans a checkpoint.
- When a wave is worked in parallel, each task usually gets its own worktree and task branch; **mt-build** covers how they merge back.

## Database branch

A code branch does not by itself need a database branch. Decide in the plan, and write the decision under Dependencies & setup.

- **Check before you assume.** Read the spec and the codebase. A database branch is required when this feature changes schema, migrations, or seed data **and** the project uses a branchable database (Neon, PlanetScale, Supabase branching, and similar). It is also required when tasks in one wave would write to the same database and collide.
- **Leave it out** when the work does not touch schema or data, or the project has no branchable database. A local database (SQLite, Docker Postgres) is isolated per worktree by **mt-build**, not by a hosted branch.
- **Schema changes share a database the way shared files share a merge.** Two tasks that both migrate are not parallel-safe on one database. Put them in different waves, or note that each task gets its own database branch.
- Name the provider the project already uses. **mt-build** creates the branch; **mt-ship** offers to delete it.

## Issue tracker

Read [references/trackers.md](references/trackers.md) before this step. In short:

1. **Find the tracker.** If `molten-docs/config.md` exists, use it. Otherwise detect GitHub Issues, Linear, or Jira from the available connectors, CLIs, and repo signals, confirm once with the user, and write `molten-docs/config.md`, including the exact operations and status names later skills will use.
2. **Sync is on by default** when a tracker is chosen (`tracker_sync: true`). The user can choose local instead, or set `tracker_sync: false` later.
3. **Show before you create.** Creating issues writes to a shared system, so the plan review includes the list of issues to be created: one parent per feature, one issue per task, with blocking links from `depends on`.
4. **Create on approval.** When the user approves the plan, create the issues with the full task details. Then replace each task block in the plan with a one-line link (`- [#12](url) 1.1 <task> · wave 1`), put the parent in the front matter, and add issue numbers to the waves table.
5. **No tracker, or `tracker_sync: false`:** the plan file is the task source. Tasks keep their full details and checkboxes, and **mt-build** ticks them off as they finish.

**One source of truth.** Tasks live in exactly one place, the **task source** (see [references/trackers.md](references/trackers.md) → Task source), so nobody has to wonder which copy is right:
- **With a tracker and `tracker_sync: true`**, each task's details (files, ACs, done-condition, verify, blockers) and its status live **only in its issue**. After issues are created, the plan has no task details, no checkboxes, and no status, only links. Things noticed during the build become new issues under the parent, not notes in the plan.
- **Without a tracker, or with `tracker_sync: false`**, the plan file is the only place, and no task issues are created.

Either way, the plan stays the map: approach, architecture, setup, phase order, waves, checkpoints, risks, and AC coverage.

## Workflow

1. Read the spec, prototype learnings, the relevant code, and `molten-docs/config.md` if it exists.
2. Identify architecture decisions and dependencies (new packages, migrations, env vars).
3. Draft the dependency order, then group work into phases and break phases into checklist tasks.
4. Group tasks into parallel waves (see Parallel waves).
5. Resolve the issue tracker (see Issue tracker). Skip if config already exists.
6. Review with the user — sequencing, scope per task, waves, anything missing, anything that can be cut, and the issues that will be created.
7. Write the plan. Set `status: approved` only on explicit sign-off.
8. On approval with tracker sync on, create the issues, then reduce the plan's task blocks to issue links (see Issue tracker, step 4). Point the user to the plan file and the parent issue.

## Output template

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
spec: molten-docs/spec/<slug>.md
status: draft | approved | in-progress | done
issue_tracker: github | linear | jira | local
tracker_parent: <parent issue key or URL> | null
molten_next_skill: mt-build
---

# Plan — <name>

## Approach
## Architecture decisions
## Dependencies & setup (packages, migrations, env vars)
Database branch: yes | no — <provider, or why not>

> With a tracker: "Tasks live in <tracker parent link>. This plan links to them and never tracks their status."

## Approach
…

<!-- While drafting and under review (any tracker), and permanently with no tracker: full task blocks -->
## Phase 1 — <name>
- [ ] **1.1 <task>** — files: `…` · covers: AC-1 · depends on: — · wave: 1 · verify: <test/command/check>
- [ ] **1.2 <task>** — files: `…` · covers: AC-2 · depends on: 1.1 · wave: 2 · verify: …
- [ ] **1.3 <task>** — files: `…` · covers: AC-3 · depends on: 1.1 · wave: 2 · verify: …
- **Checkpoint 1:** tests green, app runs, <manual check>

<!-- After issues are created: the same phase as links only. Details and status live in the issues. -->
## Phase 1 — <name>
- [#12](<url>) 1.1 <task> · wave 1
- [#13](<url>) 1.2 <task> · wave 2
- [#14](<url>) 1.3 <task> · wave 2
- **Checkpoint 1:** tests green, app runs, <manual check>

## Phase 2 — <name>
- …
- **Checkpoint 2:** …

## Parallel waves
| Wave | Tasks | Can start when |
| --- | --- | --- |
| 1 | 1.1 (#12 with a tracker) | Plan approved |
| 2 | 1.2, 1.3 | 1.1 done |
| 3 | 2.1 | Checkpoint 1 passed |

## Risks & mitigations
## Noticed during build
<!-- No tracker: notes go here. With a tracker: "File findings as issues under the parent", and nothing else. -->
## Definition of done (all acceptance criteria verified, with AC → task coverage)
```

## Done checklist

- [ ] Every spec acceptance criterion is covered by at least one task
- [ ] Each task names real files, a done-condition, and a verification step
- [ ] Tasks are vertical slices ordered by dependency so the app stays runnable
- [ ] Waves only group tasks that share no dependency and no files
- [ ] A checkpoint closes each phase
- [ ] Database branch marked yes or no, with the provider or the reason to skip it
- [ ] `molten-docs/config.md` exists with the chosen tracker (or `local`)
- [ ] `molten-docs/plan/<slug>.md` written; status set to `approved` once the user signs off
- [ ] With tracker sync on: issues created after approval with no duplicates, and the plan's task blocks reduced to issue links (no task details, checkboxes, or status left in the plan)

## Extending

Common additions: effort estimates per task, rollout or feature-flag steps, more trackers (add a block to `references/trackers.md`), or an orchestrator skill that runs one agent per task in the current wave.
