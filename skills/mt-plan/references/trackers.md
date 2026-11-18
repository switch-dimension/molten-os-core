# Issue trackers

How **mt-plan** finds the project's issue tracker, records it in `molten-docs/config.md`, and turns plan tasks into issues. Later skills (**mt-build**, **mt-verify**, **mt-review**, **mt-ship**, **mt-guide**) read only `molten-docs/config.md`, so everything they need must be written there.

Supported trackers: **GitHub Issues**, **Linear**, **Jira**, and **local** (the plan file itself).

## Task source (read this first)

Every project has exactly **one task source**: the single place where task details and status live. Every Molten skill reads and writes task status there and nowhere else.

| `molten-docs/config.md` | Task source | The plan file holds |
| --- | --- | --- |
| `issue_tracker: github`, `linear` or `jira`, with `tracker_sync: true` | **The tracker.** One issue per task under the feature's parent issue | Links to the issues, with no task details, checkboxes, or status |
| `issue_tracker: local`, or `tracker_sync: false`, or no config | **The plan file** | Full task blocks with checkboxes |

Rules that follow from this:
- **Never record status in both.** With the tracker as source, don't tick, annotate, or add `sync` notes to the plan. With the plan as source, don't create or update task issues.
- **Findings and new work go into the task source.** With a tracker, add a new issue under the parent; with the plan, add a new task or a "Noticed" note.
- **Switching sources** (for example, turning `tracker_sync` off, or adopting a tracker mid-feature) means moving every open task across in one step and then marking the old copy as retired. For issues, close them with a comment pointing to the plan. For the plan, reduce the tasks to links. Two live copies are never allowed.

## 1. Detect

Skip detection if `molten-docs/config.md` already exists. Otherwise check, in this order, and note every signal you find:

| Tracker | Signals |
| --- | --- |
| **Linear** | A Linear MCP connector is available (tools named like `linear` / `save_issue` / `list_issues`); `linear` CLI on PATH; Linear issue keys (e.g. `ENG-123`) in branch names or recent commit messages; `linear.app` links in README or PR templates |
| **Jira** | An Atlassian / Jira MCP connector is available; `jira` CLI on PATH (`jira me` works); Jira keys (e.g. `PROJ-123`) in branches or commits plus `atlassian.net` links |
| **GitHub Issues** | `git remote -v` points at github.com and `gh auth status` succeeds; issues are enabled (`gh repo view --json hasIssuesEnabled`) |
| **local** | None of the above, or the user prefers no tracker |

`ENG-123`-style keys alone are ambiguous between Linear and Jira; use the connector, CLI, or links to tell them apart. If several trackers show up, prefer the one the team's branches and commits reference.

## 2. Confirm once, then save

Present what you found and ask once, as numbered text:

```
I found these issue-tracker signals: <signals>.
1. Which tracker should Molten use for this project?
   - 1a. <detected tracker> (recommended)
   - 1b. <other detected tracker, if any>
   - 1c. None — keep tasks in the plan file
2. <tracker-specific details you could not detect: repo / team / project key>
```

Tracker sync is **on by default** when a tracker is chosen. Write `molten-docs/config.md`:

```markdown
---
issue_tracker: github | linear | jira | local
tracker_sync: true            # false = keep tasks in the plan only
github:
  repo: <owner/name>
linear:
  team: <team key or name>
  project: <project name, optional>
jira:
  site: <your-site.atlassian.net>
  project_key: <KEY>
  issue_type: Task            # parent uses Epic or Story if the project has it
statuses:                     # exact names in this tracker
  todo: <Todo>
  in_progress: <In Progress>
  done: <Done>
label: molten                 # applied to every issue Molten creates
---

# Molten config

## Tracker operations

<Copy the operations block for the chosen tracker from section 4, filled in
with this project's repo / team / project key and status names.>
```

Keep only the block for the chosen tracker. Look up real status names (Linear and Jira workflows differ per team) rather than guessing. If the user picks **local**, write `issue_tracker: local` and `tracker_sync: false` with no operations block.

## 3. Create issues (only after plan approval)

Creating issues writes to a shared, team-visible system. Show the user the list of issues you will create (parent + one per task, with blocking links) as part of the plan review, and create them only once the plan is approved.

- **Parent issue** per feature: title `<feature name>`, body links the spec and plan paths and lists the tasks.
- **One issue per task**: title `<task id> <task name>`, body contains the task's files, covered ACs, done-condition, verify step, and a link back to the plan.
- **Blocking links** from the task's `depends on` field: each dependency becomes a real "blocked by" relation where the tracker supports it.
- Apply the `label` from config to every issue.
- Once all issues exist, replace each task block in the plan with a one-line link (`- [#12](url) 1.1 <task> · wave 1`), add issue numbers to the waves table, and put the parent in the front matter (`tracker_parent: …`). The issue now holds the task's details; the plan keeps no copy of them.

If creation fails partway, report what was created. Reduce only those tasks to links, and keep full blocks for the rest so a re-run can finish the job without duplicates. Before creating, search for existing issues with the same title under the same parent to stay idempotent.

## 4. Operations by tracker

Each block lists the operations Molten skills need: **create**, **block**, **start**, **finish**, **comment**, **read status**. Copy the chosen one into `molten-docs/config.md`.

### GitHub Issues (via `gh`)

- **create:** `gh issue create --repo <repo> --title "<title>" --body-file <file> --label molten`
- **parent:** create the parent first; add each task as a sub-issue (`gh api` sub-issues endpoint) where available, otherwise list `- [ ] #<n>` task links in the parent body.
- **block:** add a "blocked by" issue dependency via `gh api` where the repo supports issue dependencies; otherwise add `Blocked by #<n>` to the task body.
- **start:** `gh issue edit <n> --add-label in-progress --add-assignee @me`
- **finish:** `gh issue close <n> --comment "Done in <commit sha or PR link>. Verify: <result>"`
- **comment:** `gh issue comment <n> --body "<text>"`
- **read status:** `gh issue view <n> --json state,labels,assignees`
- Commits reference the issue: `Refs #<n>` (or `Closes #<n>` when the commit finishes it).

### Linear (via the Linear MCP connector, or the `linear` CLI)

- **create:** create an issue in team `<team>` (project `<project>` if set) with the `molten` label; set the parent issue for task issues.
- **block:** add a "blocked by" relation from the task to each dependency.
- **start:** set state to `<statuses.in_progress>` and assign to the current user.
- **finish:** set state to `<statuses.done>` and comment with the commit or PR link and the verify result.
- **comment:** add a comment to the issue.
- **read status:** get the issue and read its state and assignee.
- Branch names and commits include the issue key (e.g. `ENG-123`) so Linear links them automatically.

### Jira (via an Atlassian / Jira MCP connector, or `jira` CLI)

- **create:** create an issue in project `<project_key>` with type `<issue_type>` and label `molten`; parent is an Epic or Story if the project uses them, and tasks are linked to it as children.
- **block:** add an issue link of type "Blocks" from each dependency to the task.
- **start:** transition to `<statuses.in_progress>` and assign to the current user.
- **finish:** transition to `<statuses.done>` and comment with the commit or PR link and the verify result.
- **comment:** add a comment to the issue.
- **read status:** get the issue and read its status and assignee.
- Commits include the issue key (e.g. `PROJ-123`) so Jira's dev panel links them.
- Jira workflows vary: confirm the transition names exist before relying on them, and record the real names in `statuses`.

### local

No external operations. The plan file is the tracker: tasks are checkboxes, `depends on` is the blocking link, and **mt-build** ticks tasks as they finish.

## 5. Source of truth

Tasks live in exactly **one** place: the task source (see the top of this file).

- **With a tracker and `tracker_sync: true`, the tracker is the single source of truth** for each task's details (files, ACs, done-condition, verify, blockers) and its status. The plan has no task details, checkboxes, or status, only links to the issues. Skills read and update status in the tracker only.
- **Findings during the build** become new issues under the parent, not notes in the plan.
- **Without a tracker (`local`)**, the plan file is the single source of truth, with full task blocks and checkboxes.
- **The plan file always remains the map:** approach, architecture, setup, phase order, waves, checkpoints, risks, AC coverage, and the issue links.
- **If the tracker is unreachable**, keep working, but don't move status into the plan. Note the pending updates in the session, and push them to the tracker when it's back.
