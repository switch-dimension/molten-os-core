---
name: mt-build
description: Molten Loop — fourth step of the Agent Development Loop. Implements an approved plan one thin slice at a time using a lightweight test-driven loop (red, green, refactor), keeping the app runnable and committing after each green task, and updates `molten-docs/plan/<slug>.md` as tasks complete. When `molten-docs/config.md` names an issue tracker (GitHub Issues, Linear, Jira), moves each task's issue to in progress and done, and comments with the commit. Use when the user wants to build, implement, or start coding a planned feature. Do not use without a plan or for exploratory spikes (use mt-prototype).
metadata:
  author: switch-dimension
  version: "0.3.1"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-order: "4"
---

# Build

Turn the plan into working, tested code — one small slice at a time. The loop is simple: write a failing test, make it pass, clean up, save progress, move on.

**Input path:** `molten-docs/plan/<slug>.md` (status `approved`) from **mt-plan**, and the spec it points to. Also `molten-docs/config.md` for the issue tracker, if it exists. If there is no approved plan, recommend **mt-plan** first. For a tiny, obvious change, a one-line plan in chat is enough — say so and proceed.

**Output:** working code, tests, small commits, ticked-off tasks in the plan file, and (with a tracker) issues updated as tasks start and finish. No separate doc.

**Next skill:** **mt-verify**.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- **Work on a feature branch.** Before the first task, check the current branch. If it is the default branch (`main`, `master`, or the repo's default), create `feat/<slug>`, including the issue key when there is a tracker (e.g. `feat/ENG-123-checkout`) so Linear and Jira link it. Tell the user the branch name. Never build directly on the default branch.
- **Branch the database only when the plan says to.** Read Dependencies & setup in the plan. If it says a database branch is required, create one with the project's own tool before the first migration, name it after the feature branch, and point this checkout's env at it. Tell the user the database branch name. Never commit the connection string. If the plan says no, use the existing dev database and do not create one. If the plan forgot to decide and this task changes schema, stop and ask.
- **One task at a time.** Pick the next unchecked task whose dependencies are done, lowest wave first. Do not start a second task until the first is green and committed.
- **Respect parallel work.** Other agents or people may be working the same plan. With a tracker, re-read issue status before picking a task and skip any task that is already in progress or done; claim yours (start + assign) before writing code. Without a tracker, ask the user which task to take if several are ready in the same wave and others may be working.
- **Tests first, where tests make sense.** For logic, APIs, and data handling: write a failing test, watch it fail for the right reason, write the minimum code to pass, then refactor with the tests green. For pure visual or config work where a test is not practical, state the verification you will use instead (screenshot, command output) and do it.
- **Bug fixes start with a reproducing test.** If it does not fail first, you have not found the bug.
- **Test behaviour, not implementation.** Assert what the spec's acceptance criteria say through public interfaces; avoid mocking what you can run for real. Prefer a few clear tests over clever shared helpers.
- **Keep the app runnable.** Every commit leaves tests passing and the app starting. Never leave a broken state to "fix next task".
- **Stay in scope.** Do only what the current task says. Note unrelated problems in the plan under a "Noticed" list rather than fixing them. If the plan or spec turns out to be wrong, stop, tell the user, and update the document before continuing.
- **Follow existing patterns.** Read the neighbouring code and match its conventions, naming, and structure before writing new code. Do not add dependencies that the plan did not approve.
- **Check the docs, don't guess.** For framework or library behaviour you are not certain of, consult the official documentation for the installed version instead of relying on memory.
- **Stop the line.** If a test fails unexpectedly, stop adding features, find the cause, fix it, then continue. Never skip, delete, or weaken a test to get green.
- **Keep the tracker in step.** If `molten-docs/config.md` has `tracker_sync: true`, use the operations it lists: **start** the issue when you begin a task, **finish** it (with the commit or PR link and verify result) when the task is green and committed, and reference the issue key in commit messages. Status lives in the tracker; the plan checkbox is a cache, so update both. If the tracker is unreachable, keep going, mark the task line `sync: pending`, and sync when it is back. Never create, close, or edit issues outside the current plan.
- Ask every question as plain numbered text in chat; for finite choices, list lettered options under the question (1a, 1b, 1c). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).

## The loop

For each task in the plan:

1. **Pick and claim** — choose the next ready task (dependencies done, lowest wave, not claimed). With a tracker, **start** its issue.
2. **Read** the task, the acceptance criteria it covers, and the files it names.
3. **Red** — write the smallest failing test that expresses the done-condition. Run it; confirm it fails for the expected reason.
4. **Green** — write the minimum code to pass. Run the test, then the wider suite.
5. **Refactor** — remove duplication and improve names while everything stays green. Do not change behaviour here.
6. **Check** — run the task's `verify` step from the plan (tests, lint, type-check, build, or a manual check).
7. **Save** — tick the task in the plan file and make one small commit with a message that says what and why, including the issue key if there is one. Only commit if the user has asked for commits in this project; otherwise leave changes staged and say so. With a tracker, **finish** the issue with the commit (or "staged, not committed") and the verify result.
8. **Checkpoint** — at the end of each phase, run the full suite, summarise progress, and pause for the user before starting the next phase. With a tracker, post the checkpoint summary as a comment on the parent issue.

## Running a wave in parallel

Optional. A single agent working down the plan does not need any of this: stay on the feature branch. Use it only when several agents or people take tasks from the same wave at once.

- **One worktree per task.** Each parallel task gets its own git worktree and task branch, cut from the feature branch (e.g. `feat/<slug>--1.2`). If the agent host already creates worktrees per session (Claude Code, Codex, Orca, Conductor and others do), use what it provides instead of running `git worktree` yourself.
- **Set each worktree up to run.** Install dependencies, copy any `.env` files the app needs (never commit them), and use a different port if a dev server is needed, so worktrees do not clash.
- **Give writers their own database.** A worktree that runs migrations or writes data gets its own database branch, or its own local database file, with the URL only in that worktree's `.env`. Worktrees that only read can share the feature's database branch.
- **Merge back when green.** When a task is green and committed, merge its task branch into the feature branch, re-run the suite on the feature branch, then remove the worktree. Tasks in the same wave touch different files, so merges should be clean; a conflict means the plan's waves were wrong. Stop and tell the user.
- **Who ticks the plan.** Each worktree has its own copy of `molten-docs/`. With a tracker, each agent updates its issue and the tracker is the source of truth. Without a tracker, only the main session (on the feature branch) ticks the plan, after each task branch merges back; agents in worktrees do not edit the plan file.
- **Checkpoints still gate.** Do not start the next wave across a checkpoint until every task branch in the current phase has merged and the full suite passes on the feature branch.

## Done checklist

- [ ] Every plan task is ticked and its verify step passed
- [ ] Tests exist for each acceptance criterion the plan assigned to the task
- [ ] Full suite, lint, type-check, and build pass
- [ ] No unrelated changes mixed in; "Noticed" items recorded in the plan
- [ ] All work is on the feature branch; any task branches merged back and their worktrees removed
- [ ] A database branch exists only if the plan required one; connection strings stayed out of git
- [ ] Plan `status` updated (`in-progress` while building, `done` when all tasks complete)
- [ ] With a tracker: every finished task's issue is done with a commit link; no `sync: pending` left

## Extending

Common additions: a UI/frontend variant (component, accessibility, and responsive checks), an API-design pass before coding endpoints, a fresh-context "doubt" review of risky decisions mid-build, or an orchestrator that starts one agent per task in the current wave.
