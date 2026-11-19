---
name: mt-discovery
description: Molten Loop — first step of the Agent Development Loop. Interviews the user about a feature or product problem before any code is written — what they actually want, who it is for, constraints, existing codebase context, risks, and open questions — then writes `molten-docs/discovery/<slug>.md`. Use when the user wants to start a new feature, explore an idea for implementation, "figure out what we're building", "interview me", or kick off the dev loop. Do not use for business-idea validation (use mt-validate) or for writing a spec when discovery is already done (use mt-spec).
metadata:
  author: switch-dimension
  version: "0.3.0"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-order: "1"
---

# Discovery

Interview the user until you understand what they actually want. Discovery comes before any prototype, spec, or plan. A vague request that goes straight to code produces the wrong thing quickly — this skill spends a few minutes of questions to avoid that.

**Output path (canonical):** `molten-docs/discovery/<slug>.md` at the repository root, where `<slug>` is a short kebab-case name for the feature. Create the directory if it does not exist.

**Next skill:** **mt-spec** by default. Optionally run **mt-prototype** first, to click through the UX as a mockup with fake data or to test a risky technical question.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- This is an **interview**, not a form. Ask **one numbered question at a time**, wait for the answer, and let each answer shape the next question. Number questions continuously (1, 2, 3 …) so the user can refer back.
- For finite choices, list lettered options under the question (1a, 1b, 1c) and mark your recommended option. Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).
- Never ask what the code or existing `molten-docs/` artifacts already answer — read first, then ask about what is genuinely unknown.
- Probe vague answers ("it should be easy", "like Notion") by asking for a concrete example or observable outcome.
- Separate **facts**, **assumptions**, and **open questions**. Do not silently turn a guess into a fact.
- Do not propose solutions or write application code while this skill is active. Reflecting back understanding is fine.

## Workflow

1. **Gather context first.** Read what already exists before asking:
   - `molten-docs/validate/`, `molten-docs/brand/brand.md`, `molten-docs/design/design.md` if present
   - `README`, agent config (`CLAUDE.md`, `AGENTS.md`), and the parts of the codebase the feature will touch
2. **Open with the problem.** Ask for the one-sentence problem and who feels it. If the user arrives with a solution ("add a dashboard"), ask what problem it solves.
3. **Interview through these themes**, in whatever order the conversation calls for, skipping what is already clear:
   - Outcome — what changes for the user, and how success will be observed
   - Users and the trigger — who, when, and what they do today instead
   - Key flows — happy path first, then the most likely failure
   - Constraints — stack, integrations, data, performance, security, deadline
   - Existing code, patterns, or services to reuse
   - Out of scope — what this explicitly is *not*
4. **Surface risks.** Ask what would make this fail or what the user is least sure about. Name the **riskiest unknown** (UX, technical feasibility, data, third-party dependency).
5. **Play it back.** Summarise your understanding in 5–8 lines and ask the user to correct it. Stop interviewing when corrections stop — do not pad.
6. **Recommend the next step.** Default to **mt-spec**. Recommend an optional detour only when it earns its cost: **mt-prototype** if the user needs to see and iterate on the UX before committing (mockup path), or if the riskiest unknown is technical feasibility (prototype path).
7. **Write the discovery doc** and point the user to the file.

## Output template

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
molten_next_skill: mt-spec | mt-prototype
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
- [ ] Interview played back to the user and corrected
- [ ] Problem, users, outcome, constraints, and scope captured
- [ ] Facts, assumptions, and open questions kept separate
- [ ] Riskiest unknown named
- [ ] `molten-docs/discovery/<slug>.md` written with `molten_next_skill` set

## Extending

Common additions: a research step that calls **mt-search** for competitors or prior art, a stakeholder-interview variant, or an idea-refinement pass (diverge on options, then converge) before the playback.
