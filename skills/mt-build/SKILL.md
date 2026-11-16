---
name: mt-build
description: Molten OS Core — fourth step of the Agent Development Loop. Implements an approved plan one thin slice at a time using a lightweight test-driven loop (red, green, refactor), keeping the app runnable and committing after each green task, and updates `molten-docs/plan/<slug>.md` as tasks complete. Use when the user wants to build, implement, or start coding a planned feature. Do not use without a plan or for exploratory spikes (use mt-prototype).
metadata:
  author: switch-dimension
  version: "0.1.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-order: "4"
---

# Build

Turn the plan into working, tested code — one small slice at a time. The loop is simple: write a failing test, make it pass, clean up, save progress, move on.

**Input path:** `molten-docs/plan/<slug>.md` (status `approved`) from **mt-plan**, and the spec it points to. If there is no approved plan, recommend **mt-plan** first. For a tiny, obvious change, a one-line plan in chat is enough — say so and proceed.

**Output:** working code, tests, small commits, and ticked-off tasks in the plan file. No separate doc.

**Next skill:** **mt-verify**.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- **One task at a time.** Pick the next unchecked task whose dependencies are done. Do not start a second task until the first is green and committed.
- **Tests first, where tests make sense.** For logic, APIs, and data handling: write a failing test, watch it fail for the right reason, write the minimum code to pass, then refactor with the tests green. For pure visual or config work where a test is not practical, state the verification you will use instead (screenshot, command output) and do it.
- **Bug fixes start with a reproducing test.** If it does not fail first, you have not found the bug.
- **Test behaviour, not implementation.** Assert what the spec's acceptance criteria say through public interfaces; avoid mocking what you can run for real. Prefer a few clear tests over clever shared helpers.
- **Keep the app runnable.** Every commit leaves tests passing and the app starting. Never leave a broken state to "fix next task".
- **Stay in scope.** Do only what the current task says. Note unrelated problems in the plan under a "Noticed" list rather than fixing them. If the plan or spec turns out to be wrong, stop, tell the user, and update the document before continuing.
- **Follow existing patterns.** Read the neighbouring code and match its conventions, naming, and structure before writing new code. Do not add dependencies that the plan did not approve.
- **Check the docs, don't guess.** For framework or library behaviour you are not certain of, consult the official documentation for the installed version instead of relying on memory.
- **Stop the line.** If a test fails unexpectedly, stop adding features, find the cause, fix it, then continue. Never skip, delete, or weaken a test to get green.
- Ask every question as plain numbered text in chat; for finite choices, list lettered options under the question (1a, 1b, 1c). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).

## The loop

For each task in the plan:

1. **Read** the task, the acceptance criteria it covers, and the files it names.
2. **Red** — write the smallest failing test that expresses the done-condition. Run it; confirm it fails for the expected reason.
3. **Green** — write the minimum code to pass. Run the test, then the wider suite.
4. **Refactor** — remove duplication and improve names while everything stays green. Do not change behaviour here.
5. **Check** — run the task's `verify` step from the plan (tests, lint, type-check, build, or a manual check).
6. **Save** — tick the task in the plan file and make one small commit with a message that says what and why. Only commit if the user has asked for commits in this project; otherwise leave changes staged and say so.
7. **Checkpoint** — at the end of each phase, run the full suite, summarise progress, and pause for the user before starting the next phase.

## Done checklist

- [ ] Every plan task is ticked and its verify step passed
- [ ] Tests exist for each acceptance criterion the plan assigned to the task
- [ ] Full suite, lint, type-check, and build pass
- [ ] No unrelated changes mixed in; "Noticed" items recorded in the plan
- [ ] Plan `status` updated (`in-progress` while building, `done` when all tasks complete)

## Extending

Common additions: a UI/frontend variant (component, accessibility, and responsive checks), an API-design pass before coding endpoints, a fresh-context "doubt" review of risky decisions mid-build, or a worktree-per-task flow for parallel agents.
