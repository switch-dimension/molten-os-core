# Changelog

All notable changes to [Molten OS Core](https://github.com/switch-dimension/molten-os-core) are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Version guidance

| Tag | When to use |
| --- | --- |
| **`v1.3.1`** (recommended) | Tag `main` today — README product/utility split and `molten-category` metadata. |
| **`v1.3.0`** | Adds `molten-search` search router skill. |
| **`v1.2.0`** | Adds `molten-validate`, surface-routed `molten-design`, README/changelog updates, and the full public skill pack. |
| **`v1.1.0`** | Includes the full initial skill pack, `molten-skill-manage`, MIT license, and the conversion-focused README with install prompts. |
| **`v1.0.0`** | Retroactive baseline if you prefer the first public tag to stop at 2026-05-29 (skills + MIT + banner/workflow only, before the June README pass). |

Per-skill versions in skill front matter (independent of repo tags):

| Skill | Version in `SKILL.md` |
| --- | --- |
| mt-brand | 1.2.0 |
| mt-design | 1.8.0 |
| mt-build | 0.1.0 |
| mt-discovery | 0.3.0 |
| mt-landing | 1.2.0 |
| mt-mockup | 0.1.1 |
| mt-plan | 0.2.0 |
| mt-prototype | 0.2.0 |
| mt-review | 0.1.0 |
| mt-search | 1.0.0 |
| mt-skill-manage | 1.2.0 |
| mt-spec | 0.3.0 |
| mt-validate | 1.2.0 |
| mt-verify | 0.1.0 |

## [Unreleased]

### Added

- **Agent Development Loop** — new `dev-loop` skill category. Six core steps run in order (`molten-order` 1–6):
  - **mt-discovery** — explore a feature before code; writes `molten-docs/discovery/<slug>.md`.
  - **mt-spec** — testable feature spec with acceptance criteria; writes `molten-docs/spec/<slug>.md`.
  - **mt-plan** — agent-executable implementation plan; writes `molten-docs/plan/<slug>.md`.
  - **mt-build** — implements the plan one slice at a time with red-green-refactor.
  - **mt-verify** — proves every acceptance criterion with evidence; writes `molten-docs/verify/<slug>.md`.
  - **mt-review** — pre-merge review with severity-labelled findings; writes `molten-docs/review/<slug>.md`.
- **Optional dev-loop steps** between discovery and spec, marked with `molten-optional: "true"` and no `molten-order`:
  - **mt-prototype** — throwaway prototype to answer one risky question; writes `molten-docs/prototype/<slug>.md`.
  - **mt-mockup** — frontend-only, clickable mockup with mocked JSON and a fake API layer so the UX can be iterated on before real integrations. Asks whether to build a throwaway mockup in `molten-docs/mockup/<slug>/` or scaffold real pages in the project's frontend; decisions go to `molten-docs/mockup/<slug>.md`.

### Changed

- **Breaking:** renamed all skills from `molten-<name>` to `mt-<name>` for brevity (`mt-validate`, `mt-brand`, `mt-design`, `mt-landing`, `mt-search`, `mt-skill-manage`). Re-install with the new names; `molten-docs/` output paths and `molten-*` metadata keys are unchanged.
- **README** rewritten to lead with the Agent Development Loop alongside the product skills, with a loop diagram, core vs optional steps, and how the two groups hand off through `molten-docs/`.
- **mt-discovery** and **mt-spec** treat mt-prototype and mt-mockup as optional detours; mt-spec reads mockup learnings and the implied data contract.
- **mt-skill-manage:** taxonomy documents core vs optional dev-loop skills.
- **All skills:** ask questions as plain numbered text, with multiple-choice options as lettered sub-items (1a, 1b, 1c). Removed instructions to use agent-specific question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).

## [1.3.1] - 2026-08-25

Product vs utility skill taxonomy.

### Added

- **`molten-category` metadata** — `product` for pipeline skills (validate → brand → design → landing); `utility` for cross-cutting helpers (search, skill-manage).
- **molten-skill-manage:** Skill taxonomy section documenting product vs utility conventions.

### Changed

- README split into **Product skills** and **Utility skills** sections; workflow diagram covers product pipeline only.
- README install examples for product-only and utility-only installs.
- Utility skills no longer carry `molten-order` in front matter.

## [1.3.0] - 2026-08-25

Search routing for live web and social research during product work.

### Added

- **molten-search** — routes search and research queries to Cursor WebSearch, last30days, agent-reach, or parallel-cli web search.

## [1.2.0] - 2026-06-02

Validation-first workflow and surface-specific design-system guidance.

### Added

- **molten-validate** — adversarial product-idea validation skill with quick score, full 5-round interview, and re-validation modes. Outputs reports to `molten-docs/validate/product-score-N.md`.
- **molten-design:** Surface reference files for landing page, web product, mobile product, and desktop product design systems.

### Changed

- README workflow now starts with **molten-validate** before brand, design, and landing page creation.
- README skill table now lists all five discovered skills.
- **molten-design:** Restructured into a shared routing spine plus surface-specific references, with one canonical `design.md` model using shared core tokens and a surface layer.

## [1.1.1] - 2026-06-02

Skill portability and design-reference workflow polish.

### Changed

- **molten-brand:** Document agent-specific structured question tools (`AskQuestion`, `AskUserQuestion`, `request_user_input`) and microphone/dictation hint for discovery intake.
- **molten-design:** Added Pinterest visual-reference discovery, a design-surface first ask, and focused surface-specific Pinterest search terms.

## [1.1.0] - 2026-06-01

Documentation and onboarding polish after the initial public skill pack.

### Added

- README install prompt with full GitHub repo URL for agent-assisted setup.
- README “tag” / release callout line for discoverability.

### Changed

- README restructured as a conversion-focused product page (value prop, why landing pages, skill table, workflow).
- Simplified install instructions and intro copy.
- Clarified agent-assisted vs manual `npx skills` installation paths.

## [1.0.0] - 2026-05-29

First public Molten OS Core skill pack — brand → design → landing workflow for idea validation.

### Added

- **molten-brand** — brand discovery workflow; outputs `molten-docs/brand/brand.md`.
- **molten-design** — design system workflow; outputs `molten-docs/design/design.md` and `molten-docs/design/example.html` preview.
- **molten-landing** — landing page build and 22-point audit workflows with references and `audit_metrics.py`.
- **molten-skill-manage** — skills.sh CLI management (`npx skills` install, update, list, remove).
- README with banner (`molten-os-banner.png`) and workflow diagram (`molten-workflow.png`).
- Agent-assisted install hint in README.
- [MIT License](LICENSE).

### Changed

- Renamed skills from `brand` / `design` / `landing` to **`molten-brand`**, **`molten-design`**, **`molten-landing`** for clarity in `npx skills ls`.
- Relicensed project to MIT (from prior license in initial commit).

### Fixed

- **molten-design:** Prompt user to choose fast vs guided design workflow.
- **molten-design:** Quote YAML front matter `description` for valid parsing.
- **molten-design:** Reduced design intake question count.

---

## Commit history (reference)

| Date | Commit | Summary |
| --- | --- | --- |
| 2026-06-01 | `10aba51` | added readme tag |
| 2026-06-01 | `074fe60` | docs: include repo URL in agent install prompt |
| 2026-06-01 | `7884ce5` | docs: restructure README as conversion-focused product page |
| 2026-06-01 | `7b5cf99` | docs: simplify README install instructions and intro copy |
| 2026-05-29 | `b938f31` | docs: clarify agent vs manual install in README |
| 2026-05-29 | `b087222` | docs: add agent-assisted install hint to README |
| 2026-05-29 | `ddb34d5` | docs: add workflow diagram to README |
| 2026-05-29 | `9729f93` | docs: refine README and relicense to MIT |
| 2026-05-29 | `b2d12f0` | docs: add README banner |
| 2026-05-29 | `eefbf71` | feat(molten-skill-manage): add skills.sh management skill |
| 2026-05-29 | `727f839` | fix(molten-design): ask for design workflow choice |
| 2026-05-29 | `75afab5` | fix(molten-design): quote front matter description |
| 2026-05-29 | `c4e0ba0` | fix(molten-design): reduce design intake questions |
| 2026-05-29 | `992b89d` | feat(molten-design): add design preview output |
| 2026-05-29 | `65cdbdf` | feat(molten-design): write design brief to molten-docs/design/design.md |
| 2026-05-29 | `4f32572` | feat(molten-brand): write brand brief to molten-docs/brand/brand.md |
| 2026-05-29 | `f79a58d` | refactor(skills): rename to molten-brand, molten-design, molten-landing |
| 2026-05-29 | `908f33c` | feat: add Molten OS Core lifecycle skill pack |
