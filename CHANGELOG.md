# Changelog

All notable changes to [Molten OS Core](https://github.com/switch-dimension/molten-os-core) are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Version guidance

| Tag | When to use |
| --- | --- |
| **`v1.2.0`** (recommended) | Tag `main` today — adds `molten-validate`, surface-routed `molten-design`, README/changelog updates, and the full public skill pack. |
| **`v1.1.0`** | Includes the full initial skill pack, `molten-skill-manage`, MIT license, and the conversion-focused README with install prompts. |
| **`v1.0.0`** | Retroactive baseline if you prefer the first public tag to stop at 2026-05-29 (skills + MIT + banner/workflow only, before the June README pass). |

Per-skill versions in skill front matter (independent of repo tags):

| Skill | Version in `SKILL.md` |
| --- | --- |
| molten-brand | 1.2.0 |
| molten-design | 1.8.0 |
| molten-landing | 1.2.0 |
| molten-skill-manage | 1.0.0 |
| molten-validate | 1.2.0 |

## [Unreleased]

Nothing yet.

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
