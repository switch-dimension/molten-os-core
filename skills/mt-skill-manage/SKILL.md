---
name: mt-skill-manage
description: Molten OS Core — manage agent skills with the skills.sh CLI (`npx skills`). Use to install, add, update, upgrade, remove, list, or find skills, restore from a lockfile, or scaffold a new skill. Trigger when the user mentions skills.sh, the skills CLI, `npx skills`, or asks to add/install/update/remove/list skills.
metadata:
  author: switch-dimension
  version: "1.4.0"
  molten-suite: molten-os
  molten-category: utility
  molten-tier: core
---

# Managing Skills

This project manages agent skills with the **skills.sh** CLI, run via `npx skills`. Use it whenever the user wants to install, update, remove, list, or find skills. Do not hand-edit skill installs or symlinks; use the CLI so installs stay consistent across agents.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- Always run the CLI through `npx skills <command>` (no global install assumed).
- Default to **project** scope. Add `-g`/`--global` only when the user wants a skill available across all their projects.
- Use `-y`/`--yes` to skip interactive prompts when the intent is unambiguous; otherwise let prompts run so the user can choose.
- Number every free-text question asked in chat so the user can answer by reference, especially when dictating in voice mode.
- When you need choices from the user (scope, agents, which skills), ask them as numbered questions with lettered options (1a, 1b, …). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).
- Confirm before removing skills unless the user clearly named what to remove.
- After installing or updating, run `npx skills ls` to confirm the result.

## Common Commands

**Install a skill package** (a GitHub repo or URL):

```bash
npx skills add switch-dimension/molten-os-core
```

Install specific skills or target specific agents:

```bash
npx skills add switch-dimension/molten-os-core --skill mt-brand mt-design
npx skills add switch-dimension/molten-os-core --agent claude-code cursor
npx skills add switch-dimension/molten-os-core --all   # all skills, all agents, no prompts
```

Preview what a repo offers without installing:

```bash
npx skills add switch-dimension/molten-os-core --list
```

**Update skills** to their latest versions:

```bash
npx skills update                 # update all
npx skills update mt-landing  # update one
npx skills update -p              # project skills only
npx skills update -g              # global skills only
```

**Remove skills:**

```bash
npx skills remove                 # interactive picker
npx skills remove mt-design
npx skills remove --all           # remove all, all agents, no prompts
```

**List installed skills:**

```bash
npx skills ls            # project scope (default)
npx skills ls -g         # global scope
npx skills ls --json     # machine-readable
```

**Find skills** to install, interactively:

```bash
npx skills find
npx skills find landing
```

**Scaffold a new skill** in this repo:

```bash
npx skills init mt-<name>   # creates mt-<name>/SKILL.md
```

**Restore from the lockfile** (`skills-lock.json`):

```bash
npx skills experimental_install
```

## Scope Flags Reference

| Flag | Meaning |
| --- | --- |
| `-g`, `--global` | User-level install (all projects) |
| `-p`, `--project` | Project scope only (update) |
| `-a`, `--agent <agents>` | Target specific agents (`*` for all) |
| `-s`, `--skill <skills>` | Target specific skills (`*` for all) |
| `-y`, `--yes` | Skip confirmation prompts |
| `--all` | Shorthand for `--skill '*' --agent '*' -y` |

## Naming Convention

Skills in this suite use the **`mt-<name>`** convention so they are easy to distinguish from third-party skills in `npx skills ls`. When scaffolding a new Molten skill, follow that prefix.

## Skill taxonomy

Molten OS Core skills fall into three categories. Set `molten-category` in skill front matter when adding or editing a skill.

| Category | Skills | `molten-order` | Purpose |
| --- | --- | --- | --- |
| **product** | mt-validate, mt-brand, mt-design, mt-landing | Required (`"1"`–`"4"`) | Sequential pipeline; writes artifacts to `molten-docs/` |
| **dev-loop** | mt-discovery, mt-spec, mt-plan, mt-build, mt-verify, mt-review, mt-ship (core); mt-prototype, mt-mockup (optional) | Core: required (`"1"`–`"7"`). Optional: omit, set `molten-optional: "true"` | Agent Development Loop; discovery → spec → plan → build → verify → review → ship, with optional prototype/mockup detours between discovery and spec; writes artifacts to `molten-docs/` |
| **utility** | mt-guide, mt-search, mt-skill-manage | Omit | Cross-cutting helpers; use anytime, not part of the product workflow |

**Product skills** and **dev-loop skills** each run in order and build on each other. **Utility skills** are optional — install only what you need.

**mt-guide** routes users across all three categories. When you add, rename or reorder a skill, update mt-guide's Skill map, State map and Shortcuts too.

When scaffolding a new skill:

- Product skill → `molten-category: product`, assign the next `molten-order`
- Dev-loop skill → `molten-category: dev-loop`, assign the next `molten-order` (core step) or omit it and set `molten-optional: "true"` (optional detour)
- Utility skill → `molten-category: utility`, no `molten-order`

Keep all skills in flat `skills/mt-<name>/` paths so `npx skills add` discovers them correctly.
