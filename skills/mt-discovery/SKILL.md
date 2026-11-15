---
name: mt-discovery
description: Molten OS Core — first step of the Agent Development Loop. Explores a feature or product problem before any code is written — goals, users, constraints, existing codebase context, risks, and open questions — and writes `molten-docs/discovery/<slug>.md`. Use when the user wants to start a new feature, explore an idea for implementation, "figure out what we're building", or kick off the dev loop. Do not use for business-idea validation (use mt-validate) or for writing a spec when discovery is already done (use mt-spec).
metadata:
  author: switch-dimension
  version: "0.1.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-order: "1"
---

# Discovery

Understand the problem well enough to build the right thing. Discovery comes before any prototype, spec, or plan.

**Output path (canonical):** `molten-docs/discovery/<slug>.md` at the repository root, where `<slug>` is a short kebab-case name for the feature. Create the directory if it does not exist.

**Next skill:** **mt-prototype** (when the riskiest question is about UX or feasibility) or **mt-spec** (when the shape is already clear).

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- Number every free-text question asked in chat so the user can answer by reference.
- Use the agent's structured question tool for finite choices:
  - **Codex:** `request_user_input`
  - **Claude Code:** `AskUserQuestion`
  - **Cursor:** `AskQuestion`
- Ask in small batches. Do not re-ask anything already answered by the user or by existing `molten-docs/` artifacts.
- Separate **facts**, **assumptions**, and **open questions**.
- Do not write application code while this skill is active.

## Workflow

1. **Gather context first.** Read what already exists before asking:
   - `molten-docs/validate/`, `molten-docs/brand/brand.md`, `molten-docs/design/design.md` if present
   - `README`, agent config (`CLAUDE.md`, `AGENTS.md`), and the parts of the codebase the feature will touch
2. **Frame the problem.** Ask for (or confirm) the one-sentence problem statement and who it is for.
3. **Explore.** Cover, briefly:
   - Desired outcome and how success will be observed
   - Primary user flows (happy path first)
   - Constraints — tech stack, integrations, data, performance, security, deadlines
   - What is explicitly out of scope
   - Existing code, patterns, or services to reuse
4. **Surface risks.** Identify the riskiest unknown (UX, technical feasibility, data, third-party dependency).
5. **Recommend the next step.** If the riskiest unknown needs to be seen or tried, recommend **mt-prototype**; otherwise recommend **mt-spec**.
6. **Write the discovery doc** and point the user to the file.

## Output template

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
molten_next_skill: mt-prototype | mt-spec
---

# Discovery — <name>

## Problem
## Users & context
## Desired outcome / success signals
## Key flows
## Constraints
## Out of scope
## Codebase context (files, patterns, services to reuse)
## Facts / Assumptions / Open questions
## Riskiest unknown
## Recommended next step
```

## Done checklist

- [ ] Existing docs and relevant code read before asking questions
- [ ] Problem, users, outcome, constraints, and scope captured
- [ ] Riskiest unknown named
- [ ] `molten-docs/discovery/<slug>.md` written with `molten_next_skill` set
