---
name: molten-skill-manage
description: Molten OS Core — manage agent skills with the skills.sh CLI (`npx skills`). Use to install, add, update, upgrade, remove, list, or find skills, restore from a lockfile, or scaffold a new skill. Trigger when the user mentions skills.sh, the skills CLI, `npx skills`, or asks to add/install/update/remove/list skills.
metadata:
  author: switch-dimension
  version: "1.0.0"
  molten-suite: molten-os
  molten-tier: core
  molten-order: "1"
---

# Managing Skills

This project manages agent skills with the **skills.sh** CLI, run via `npx skills`. Use it whenever the user wants to install, update, remove, list, or find skills. Do not hand-edit skill installs or symlinks; use the CLI so installs stay consistent across agents.

## Operating Rules

- Always run the CLI through `npx skills <command>` (no global install assumed).
- Default to **project** scope. Add `-g`/`--global` only when the user wants a skill available across all their projects.
- Use `-y`/`--yes` to skip interactive prompts when the intent is unambiguous; otherwise let prompts run so the user can choose.
- Confirm before removing skills unless the user clearly named what to remove.
- After installing or updating, run `npx skills ls` to confirm the result.

## Common Commands

**Install a skill package** (a GitHub repo or URL):

```bash
npx skills add switch-dimension/molten-os-core
```

Install specific skills or target specific agents:

```bash
npx skills add switch-dimension/molten-os-core --skill molten-brand molten-design
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
npx skills update molten-landing  # update one
npx skills update -p              # project skills only
npx skills update -g              # global skills only
```

**Remove skills:**

```bash
npx skills remove                 # interactive picker
npx skills remove molten-design
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
npx skills init molten-<name>   # creates molten-<name>/SKILL.md
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

Skills in this suite use the **`molten-<name>`** convention so they are easy to distinguish from third-party skills in `npx skills ls`. When scaffolding a new Molten skill, follow that prefix.
