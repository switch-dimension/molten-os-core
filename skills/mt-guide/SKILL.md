---
name: mt-guide
description: Molten OS Core — the "start here" router for Molten skills. Reads `molten-docs/` to show where a project is and what comes next, or asks a few short questions and recommends the right Molten skill. Use when the user asks which Molten skill to use, "what's next", "where am I", "where do I start", "help me use these skills", or mentions mt-guide. Do not use when the user has already named the skill they want; run that skill directly.
metadata:
  author: switch-dimension
  version: "0.2.0"
  molten-suite: molten-os
  molten-category: utility
  molten-tier: core
---

# Molten Guide

Router only. Work out where the user is, recommend **one** next skill, say why, then hand off. Do not do the work of the skill you recommend.

**Input path:** `molten-docs/` at the repository root (read-only).

**Output:** a short recommendation in chat. This skill writes no files.

## Operating Rules

- **Read before you describe.** The summaries below are for orientation only. Before telling the user what a skill does, or recommending that a step be skipped, read that skill's `SKILL.md`.
- **Only route to installed skills.** Check which `mt-*` skills are available. If the best fit is not installed, say so and give the install command: `npx skills add switch-dimension/molten-os-core --skill <name>`.
- **State first, questions second.** If `molten-docs/` answers the question, do not ask.
- Ask at most three questions, as plain numbered text in chat; for finite choices, list lettered options under the question (1a, 1b, 1c). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).
- Recommend one next skill. Mention an optional step only when it clearly earns its cost.
- Do not recap whole documents. Point to the file paths.

## Workflow

1. **Read the project state.** Scan `molten-docs/` (see State map). For each feature slug, find the furthest step that exists and read its front matter (`status`, `verdict`, `recommendation`, `molten_next_skill`). If `molten-docs/config.md` has `tracker_sync: true`, read task status from the tracker using the operations listed there (the plan checkboxes are only a cache) and mention which tasks are in progress, done, and ready in the current wave.
2. **If there is state, report it and recommend.** Give a short status per active feature, then the next skill. Example:
   > **checkout** — spec approved, plan 3 of 7 tasks done.
   > **Next:** mt-build, starting at task 1.4. It reads `molten-docs/plan/checkout.md`.
   If several features are in flight, list each in one line and ask which one to continue.
3. **If there is no state (or the user wants something new), ask.** Pick only the questions you need:
   1. What are you trying to do?
      - 1a. Test whether an idea is worth building
      - 1b. Build a feature or product
      - 1c. Fix something that's broken
      - 1d. Review a change before it merges
      - 1e. Something else (search, manage skills)
   2. Is there an existing codebase?
   3. How big is it? (a. tiny, under an hour · b. a feature · c. a whole product)
4. **Route** using the Skill map and Shortcuts.
5. **Hand off.** Use the Recommendation format, then offer to start the recommended skill.

## Skill map

### Product flow — idea to a testable landing page

Run in order. For testing an idea with real people before building.

1. **mt-validate** — adversarially score the idea; name the riskiest assumption. → `molten-docs/validate/product-score-N.md`
2. **mt-brand** — audience, pain, positioning, message, voice. → `molten-docs/brand/brand.md`
3. **mt-design** — design system for one surface (landing, web, mobile, desktop). → `molten-docs/design/design.md`
4. **mt-landing** — build or audit a landing page from brand and design.

### Agent Development Loop — feature to merged code

Run in order, once per feature.

1. **mt-discovery** — interview before code; find the riskiest unknown. → `molten-docs/discovery/<slug>.md`
2. **mt-spec** — testable spec with acceptance criteria. → `molten-docs/spec/<slug>.md`
3. **mt-plan** — vertical-slice tasks with checkpoints. → `molten-docs/plan/<slug>.md`
4. **mt-build** — implement one slice at a time, test first; ticks off plan tasks.
5. **mt-verify** — prove every acceptance criterion with evidence; debug failures. → `molten-docs/verify/<slug>.md`
6. **mt-review** — pre-merge review with severity-labelled findings. → `molten-docs/review/<slug>.md`

**Optional detours between discovery and spec.** Skip both when the shape is already clear.

- **mt-prototype** — one risky question, usually technical feasibility or a single tricky interaction. → `molten-docs/prototype/<slug>.md`
- **mt-mockup** — the user needs to see and click through the whole UX with fake data before backend work. → `molten-docs/mockup/<slug>.md`

### Where the flows meet

The product flow feeds the dev loop. mt-discovery, mt-prototype, mt-mockup and mt-spec pick up `brand.md` and `design.md` when they exist. Neither flow requires the other: the dev loop works on its own in any codebase.

### Utility — any time

- **mt-search** — route a search or research query (competitors, prior art, recent discussion).
- **mt-skill-manage** — install, update, remove or find skills.
- **mt-guide** — this skill.

## State map

| Found in `molten-docs/` | Means | Recommend |
| --- | --- | --- |
| Nothing | Fresh start | Ask (Workflow step 3) |
| `validate/` only | Idea scored | Read the latest score's verdict. Promising → **mt-brand**. Weak → re-run the experiment, then **mt-validate** (re-validate mode) |
| `brand/brand.md`, no `design/` | Brand done | **mt-design** |
| `design/design.md` | Design system done | **mt-landing**, or **mt-discovery** if they're ready to build |
| `discovery/<slug>.md` only | Feature explored | Its `molten_next_skill` (default **mt-spec**) |
| `prototype/` or `mockup/<slug>.md`, no spec | Detour done | **mt-spec** |
| `spec/<slug>.md` `status: draft` | Spec unfinished | **mt-spec** to finish and approve |
| `spec/<slug>.md` `status: approved`, no plan | Ready to plan | **mt-plan** |
| `plan/<slug>.md` `draft` | Plan unfinished | **mt-plan** to finish and approve |
| `plan/<slug>.md` `approved` / `in-progress` | Building | **mt-build**, from the next ready task (lowest wave, not claimed). With a tracker, check issue status first |
| `plan/<slug>.md` `done`, no verify | Built | **mt-verify** |
| `verify/<slug>.md` `verdict: fail` / `partial` | Not proven | **mt-build** to fix, then **mt-verify** again |
| `verify/<slug>.md` `verdict: pass`, no review | Proven | **mt-review** |
| `review/<slug>.md` `request-changes` | Changes needed | **mt-build** for the fixes, then **mt-verify** and **mt-review** |
| `review/<slug>.md` `approve` / `approve-with-suggestions` | Ready to merge | Merge, then **mt-discovery** for the next feature |

If an artifact's front matter has `molten_next_skill`, prefer it over this table unless its status says the step is unfinished.

## Shortcuts

Not every job needs the whole loop. Use these when they fit:

| Situation | Route |
| --- | --- |
| Tiny, obvious change | **mt-build** with a one-line plan in chat |
| Something is broken | **mt-verify** (debugs from root cause) → **mt-build** for the fix → **mt-review** |
| A diff or PR to check | **mt-review** |
| Spec already written elsewhere | **mt-plan** (point it at that spec) |
| Turn a spec into tickets or issues | **mt-plan** (creates issues in GitHub, Linear or Jira on approval) |
| Clear feature, no unknowns | **mt-discovery** → **mt-spec**, skip both detours |
| Existing landing page to improve | **mt-landing** (audit mode) |
| Only need research | **mt-search** |

## Recommendation format

```markdown
**Where you are:** <one line, or "Fresh start">
**Next:** <skill> — <why, in one sentence>
**It reads:** <input paths, or "nothing yet">
**It writes:** <output path>
**Optional:** <one detour worth considering, or omit this line>
```

Then ask: "Want me to start **<skill>** now?"

## Checklist

- [ ] Read `molten-docs/` before asking anything
- [ ] Read the recommended skill's `SKILL.md` before describing it or suggesting a step be skipped
- [ ] Checked the recommended skill is installed (or gave the install command)
- [ ] One clear next skill, in the recommendation format
- [ ] No files written
