# Molten Loop - Idea in, shipped feature out

![Molten Loop](assets/molten-loop-header.png)

### Validate the idea, give it a brand and a landing page, then build it with your coding agent using a disciplined loop: discovery, spec, plan, build, verify, review, ship.

Molten Loop is a set of AI agent skills from [Switch Dimension](https://switchdimension.com) and AI builder YouTuber [Rob Shocks](https://youtube.com/robshocks). It splits the work into two disciplines that meet at one document, the spec:

- **Product Engineering: are we building the right thing?** Challenge the idea, give it a brand, a design system and a landing page to test with real people, then pin each feature down in a testable spec.
- **Factory Engineering: are we building it well?** Treat your coding agent as a production line. It plans from the spec, builds in thin tested slices, proves every acceptance criterion, reviews the change, ships it as a clean, secret-scanned pull request, and runs a retro that improves the line for next time.

Drop this prompt into your AI agent to get started:

```
install all the skills in this repo to my project - https://github.com/switch-dimension/molten-loop
```

Not sure where to start? Ask your agent to run **mt-guide**. It reads your `molten-docs/` folder, tells you where you are and recommends the next skill.

> Released under the MIT license — copy it, fork it, and use it as inspiration for your own evolving system. [Full install options below.](#installation)

## What you get

Every skill writes its output as Markdown under `molten-docs/`, so each step builds on the last and you (or another agent) can pick up where you left off.

```
 PRODUCT ENGINEERING                              │  FACTORY ENGINEERING
 What are we building, and for whom?              │  How does a spec become shipped code, every time?
                                                  │
 idea ─► validate ─► brand ─► design ─► landing   │
                (once per product)                │
                                                  │
              ┌─ prototype ─┐                     │
 discovery ───┤  (optional) ├──► spec ════════════╪══► plan ─► build ─► verify ─► review ─► ship
              └─ mockup    ─┘                     │                                           │
                (once per feature)                │          retro ◄──────────────────────────┘
                                                  │   (improves your checks, docs and skills)
```

| Discipline | Skills | You end up with |
| --- | --- | --- |
| **Product Engineering** | mt-validate → mt-brand → mt-design → mt-landing, then per feature mt-discovery → mt-spec, plus optional mt-prototype and mt-mockup | A validated idea, a landing page to test it, and a testable spec for each feature |
| **Factory Engineering** | mt-plan → mt-build → mt-verify → mt-review → mt-ship | A reviewed, secret-scanned pull request with evidence for every acceptance criterion |
| **Utility skills** | mt-guide, mt-search, mt-skill-manage | Routing, research and skill management. Start with **mt-guide** if you're unsure which skill to use |

The **Agent Development Loop** is the full run for one feature, across both halves: mt-discovery → mt-spec → mt-plan → mt-build → mt-verify → mt-review → mt-ship.

## Product Engineering

Most AI-built products fail by building the wrong thing. These skills make you prove the idea, then pin down each feature before any code is written.

### The product (once)

Turn a raw idea into a validated landing page you can test with real people — score, brand, design system and page — in an afternoon, not a quarter. Run these in order.

| Step | Skill | What it does for you |
| --- | --- | --- |
| 1 | **mt-validate** | Adversarially scores a product idea with quick, full-interview or re-validation modes and names the riskiest assumption to test. Writes `molten-docs/validate/product-score-N.md`. |
| 2 | **mt-brand** | Pins down who you're for, the pain you solve, your positioning, message and voice. Writes `molten-docs/brand/brand.md`. |
| 3 | **mt-design** | Turns that brand into a practical design system for one surface at a time (landing, web, mobile or desktop) plus a live visual preview. Writes `molten-docs/design/design.md`. |
| 4 | **mt-landing** | Creates (or audits) a high-converting landing page from your brand and design system, so you can test the idea with an audience fast. |

#### Why validate before building?

A good validation pass and landing page are sharper tests than a pitch deck or a business plan, because they force you to answer the questions that decide whether a product works:

- **Who** is this for?
- **What** pain are they feeling?
- **Why** does that pain matter to them right now?
- **How** do the benefits of your product remove it?

Add a waitlist or a paid pre-order and you get the only feedback that counts: will people act? You learn that **before** you commit months to building the wrong thing.

### The feature (each time)

A vague request that goes straight to code produces the wrong thing quickly. These are the first steps of the Agent Development Loop: a few minutes of thinking that end in a spec the factory can build from. They pick up `brand.md` and `design.md` when they exist, so what you build matches what you tested.

| Loop step | Skill | What it does for you |
| --- | --- | --- |
| 1 | **mt-discovery** | Interviews you before any code is written: goals, users, constraints, codebase context and the riskiest unknown. Writes `molten-docs/discovery/<slug>.md`. |
| optional | **mt-prototype** | Use when one question is still risky, usually technical feasibility or a single tricky interaction. Builds the smallest throwaway thing that answers it, then records what was learned in `molten-docs/prototype/<slug>.md`. |
| optional | **mt-mockup** | Use when you want to see and click through the whole UX before paying for backend work. Builds a clickable, frontend-only mockup with mocked JSON and a fake API. Choose throwaway (`molten-docs/mockup/<slug>/`) or scaffold real pages in your app. |
| 2 | **mt-spec** | Turns discovery (and any prototype or mockup learnings) into a testable spec with acceptance criteria, data shape, edge cases and non-goals. Writes `molten-docs/spec/<slug>.md`. |

Use the optional steps only when they earn their cost. If the shape is already clear, go straight from discovery to **mt-spec**.

## Factory Engineering

Your coding agent is the production line. These skills make the line itself well built: they take an approved spec and turn it into a pull request you can trust, the same way every time. They are the second half of the Agent Development Loop. Run them in order.

| Loop step | Skill | What it does for you |
| --- | --- | --- |
| 3 | **mt-plan** | Breaks the approved spec into ordered vertical-slice tasks with checkpoints, grouped into parallel waves so several agents or people can work at once. Says whether the feature needs a database branch. Creates one issue per task in GitHub Issues, Linear or Jira when you use one. Writes `molten-docs/plan/<slug>.md`. |
| 4 | **mt-build** | Implements the plan one slice at a time on a feature branch with a lightweight red-green-refactor loop, keeping the app runnable. Creates a database branch only when the plan requires one. When several agents work a wave in parallel, it gives each task its own worktree and merges them back. Ticks tasks off in the plan, or moves their issues to done in your tracker. |
| 5 | **mt-verify** | Checks every acceptance criterion against evidence (tests, the real app) and debugs failures from root cause. Writes `molten-docs/verify/<slug>.md`. |
| 6 | **mt-review** | Reviews the change before it merges with two fresh-context reviewers, Spec and Quality (correctness, readability, architecture, security, performance). Checks each finding against the code and lists what it dismissed. Optional second opinion from another model. Writes `molten-docs/review/<slug>.md`. |
| 7 | **mt-ship** | Gets the approved change into a clean pull request: re-runs build, tests, lint and type-check, scans the branch for secrets with gitleaks, audits dependencies, tidies commits and debug leftovers, updates docs and changelog, writes the PR with evidence and a "merge danger" call, and watches CI. It never merges. Ends with a short retrospective that suggests improvements to your checks, docs and skills. Writes `molten-docs/ship/<slug>.md` and `molten-docs/retro/<slug>.md`. |

The factory takes a spec as input. Use **mt-spec** to write one, or bring your own in `molten-docs/spec/<slug>.md`.

### The factory improves itself

Every **mt-ship** run ends with a retro. It looks at what slowed the feature down or slipped through (a missing check, an unclear doc, a skill step that misfired) and suggests concrete fixes, so each feature leaves the line a little better than it found it.

### Issue trackers

The first time **mt-plan** runs, it looks for GitHub Issues, Linear or Jira (via your agent's connectors, CLIs such as `gh`, and repo signals), confirms the choice with you, and saves it in `molten-docs/config.md`. Sync is on by default:

- **mt-plan** shows you the issues it will create, then creates them when you approve the plan: one parent per feature and one issue per task, with blocking links.
- **mt-build** claims each task's issue when it starts, and closes it with the commit when the task is green.
- **mt-verify** and **mt-review** post their verdicts on the parent issue.
- **mt-ship** links the PR to the parent issue so it closes on merge.

No tracker? The plan file holds the tasks and they're ticked off as they're done.

## How the two fit together

The spec is the contract between the two halves. Product Engineering decides what goes in it; Factory Engineering builds exactly that and proves it.

You don't need both:

- **Testing an idea?** Use the product half on its own: validate, brand, design, landing.
- **Working in an existing codebase?** Run the Agent Development Loop once per feature: discovery and spec, then the factory.
- **Already have specs?** Hand them straight to the factory.

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

Install the Agent Development Loop (feature discovery and spec, plus the factory), plus mt-guide. Drop `mt-prototype` and `mt-mockup` if you don't want the optional steps:

```bash
npx skills add switch-dimension/molten-loop --skill mt-guide mt-discovery mt-prototype mt-mockup mt-spec mt-plan mt-build mt-verify mt-review mt-ship
```

Install Product Engineering only, plus mt-guide:

```bash
npx skills add switch-dimension/molten-loop --skill mt-guide mt-validate mt-brand mt-design mt-landing mt-discovery mt-prototype mt-mockup mt-spec
```

Install Factory Engineering only, plus mt-guide (for when you already write your own specs):

```bash
npx skills add switch-dimension/molten-loop --skill mt-guide mt-plan mt-build mt-verify mt-review mt-ship
```

Install utility skills only:

```bash
npx skills add switch-dimension/molten-loop --skill mt-guide mt-search mt-skill-manage
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
