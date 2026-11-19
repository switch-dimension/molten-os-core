# Molten Loop - Idea in, shipped feature out

![Molten Loop](assets/molten-loop-header.png)

### Validate the idea, give it a brand and a landing page, then build it with your coding agent using a disciplined loop: discovery, spec, plan, build, verify, review, ship.

Molten Loop is a set of AI agent skills from [Switch Dimension](https://switchdimension.com) and AI builder YouTuber [Rob Shocks](https://youtube.com/robshocks). It splits the work into two disciplines:

- **Product Engineering: are we building the right thing?** Challenge the idea, then give it a brand, a design system and a landing page to test with real people.
- **Software Engineering: are we building it well?** Run each feature through the Agent Development Loop. Your coding agent discovers and specs the feature, plans it, builds it in thin tested slices, proves every acceptance criterion, reviews the change, ships it as a clean, secret-scanned pull request, and runs a retro that improves the loop for next time.

Drop this prompt into your AI agent to get started:

```
install all the skills in this repo to my project - https://github.com/switch-dimension/molten-loop
```

Not sure where to start? Ask your agent to run **mt-guide**. It reads your `molten-docs/` folder, tells you where you are and recommends the next skill.

> Released under the MIT license — copy it, fork it, and use it as inspiration for your own evolving system. [Full install options below.](#installation)

## What you get

Every skill writes its output as Markdown under `molten-docs/`, so each step builds on the last and you (or another agent) can pick up where you left off.

| Discipline | Skills | You end up with |
| --- | --- | --- |
| **Product Engineering** (once per product) | mt-validate → mt-brand → mt-design → mt-landing | A validated idea and a landing page to test it |
| **Software Engineering** (once per feature) | mt-discovery → mt-spec → mt-plan → mt-build → mt-verify → mt-review → mt-ship, plus optional mt-prototype | A reviewed, secret-scanned pull request with evidence for every acceptance criterion |
| **Utility skills** | mt-guide, mt-search, mt-skill-manage | Routing, research and skill management. Start with **mt-guide** if you're unsure which skill to use |

You don't need both. Testing an idea? Use Product Engineering on its own. Working in an existing codebase? Run Software Engineering once per feature.

## Product Engineering

Most AI-built products fail by building the wrong thing. These skills turn a raw idea into a validated landing page you can test with real people — score, brand, design system and page — in an afternoon, not a quarter. Run them in order.

| Step | Skill | What it does for you |
| --- | --- | --- |
| 1 | **mt-validate** | Adversarially scores a product idea with quick, full-interview or re-validation modes and names the riskiest assumption to test. Writes `molten-docs/validate/product-score-N.md`. |
| 2 | **mt-brand** | Pins down who you're for, the pain you solve, your positioning, message and voice. Writes `molten-docs/brand/brand.md`. |
| 3 | **mt-design** | Turns that brand into a practical design system for one surface at a time (landing, web, mobile or desktop) plus a live visual preview. Writes `molten-docs/design/design.md`. |
| 4 | **mt-landing** | Creates (or audits) a high-converting landing page from your brand and design system, so you can test the idea with an audience fast. |

### Why validate before building?

A good validation pass and landing page force you to answer the questions that decide whether a product works: **who** is this for, **what** pain are they feeling, **why** does it matter to them right now, and **how** does your product remove it?

Add a waitlist or a paid pre-order and you get the only feedback that counts: will people act? You learn that **before** you commit months to building the wrong thing.

## Software Engineering

Your coding agent is the production line. The Agent Development Loop takes one feature from a vague request to a pull request you can trust, the same way every time. Run the steps in order. The early steps pick up `brand.md` and `design.md` when they exist, so what you build matches what you tested.

| Step | Skill | What it does for you |
| --- | --- | --- |
| 1 | **mt-discovery** | Interviews you before any code is written: goals, users, constraints, codebase context and the riskiest unknown. Writes `molten-docs/discovery/<slug>.md`. |
| optional | **mt-prototype** | See or test the feature before you spec it. Mainly a clickable UX mockup with mocked data and a fake API, either throwaway or as real pages in your app. When the risk is technical, it builds a time-boxed prototype that answers one feasibility question instead. Writes `molten-docs/prototype/<slug>.md`. |
| 2 | **mt-spec** | Turns discovery (and any prototype or mockup learnings) into a testable spec with acceptance criteria, data shape, edge cases and non-goals. Writes `molten-docs/spec/<slug>.md`. |
| 3 | **mt-plan** | Breaks the spec into ordered vertical-slice tasks with checkpoints, grouped into parallel waves so several agents or people can work at once. Says whether the feature needs a database branch. Writes `molten-docs/plan/<slug>.md`. |
| 4 | **mt-build** | Implements the plan one slice at a time on a feature branch with a lightweight red-green-refactor loop, keeping the app runnable. Creates a database branch only when the plan requires one, and gives parallel agents their own worktrees. |
| 5 | **mt-verify** | Checks every acceptance criterion against evidence (tests, the real app) and debugs failures from root cause. Writes `molten-docs/verify/<slug>.md`. |
| 6 | **mt-review** | Reviews the change with two fresh-context reviewers, Spec and Quality (correctness, readability, architecture, security, performance), and checks each finding against the code. Optional second opinion from another model. Writes `molten-docs/review/<slug>.md`. |
| 7 | **mt-ship** | Re-runs build, tests, lint and type-check, scans the branch for secrets with gitleaks, audits dependencies, tidies commits, updates docs and changelog, writes the PR with evidence and a "merge danger" call, and watches CI. It never merges. Writes `molten-docs/ship/<slug>.md`. |

Skip mt-prototype if the shape and feasibility are already clear. Already have a spec? Put it in `molten-docs/spec/<slug>.md` and start at **mt-plan**.

### The loop improves itself

Every **mt-ship** run ends with a retro (`molten-docs/retro/<slug>.md`). It looks at what slowed the feature down or slipped through (a missing check, an unclear doc, a skill step that misfired) and suggests concrete fixes, so each feature leaves the loop a little better than it found it.

### Issue trackers

The first time **mt-plan** runs, it looks for GitHub Issues, Linear or Jira, confirms the choice with you, and saves it in `molten-docs/config.md`. From then on, mt-plan creates one issue per task, mt-build closes them as tasks go green, mt-verify and mt-review post their verdicts, and mt-ship links the PR so the feature closes on merge.

No tracker? The plan file holds the tasks and they're ticked off as they're done.

## Utility skills

Cross-cutting helpers. Install and use as needed.

| Skill | What it does for you |
| --- | --- |
| **mt-guide** | The "start here" router. Reads `molten-docs/` to show where each feature is and what comes next, or asks a few questions and recommends the right skill, including shortcuts for small fixes, bugs and reviews. |
| **mt-search** | Routes search and research queries to the right backend: quick web lookup, recent social pulse, platform-specific fetch or cited web research. Handy during validation and discovery. |
| **mt-skill-manage** | Manages skills via the skills.sh CLI (`npx skills`): install, update, remove, list and find skills. |

## Installation

Paste this repo into your agent with the prompt above, or install manually with the [skills.sh](https://github.com/vercel-labs/skills) CLI.

Install all skills:

```bash
npx skills add switch-dimension/molten-loop
```

Install Software Engineering only, plus mt-guide. Drop `mt-prototype` if you don't want the optional step:

```bash
npx skills add switch-dimension/molten-loop --skill mt-guide mt-discovery mt-prototype mt-spec mt-plan mt-build mt-verify mt-review mt-ship
```

Install Product Engineering only, plus mt-guide:

```bash
npx skills add switch-dimension/molten-loop --skill mt-guide mt-validate mt-brand mt-design mt-landing
```

Install a single skill:

```bash
npx skills add switch-dimension/molten-loop --skill mt-landing
```

All skills use the **`mt-<name>`** convention so they are easy to distinguish from third-party skills in `npx skills ls`.

## Changelog

Release history and version notes: [CHANGELOG.md](CHANGELOG.md). Current release: **v1.3.1**.

## License

Released under the [MIT License](LICENSE). You may use, copy, modify, merge, publish, distribute, sublicense, and sell copies, provided the license and copyright notice are included in redistributions.
