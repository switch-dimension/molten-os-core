# Molten OS Core

An agentic product lifecycle skill pack for [skills.sh](https://skills.sh)—reusable capabilities for AI coding agents (Cursor, Claude Code, Windsurf, and more).

All skills use the **`molten-<name>`** convention so they are easy to distinguish from third-party skills in `npx skills ls`.

## Installation

```bash
npx skills add switch-dimension/molten-os-core
```

Install a single skill:

```bash
npx skills add switch-dimension/molten-os-core --skill molten-landing
npx skills add switch-dimension/molten-os-core --skill molten-brand
npx skills add switch-dimension/molten-os-core --skill molten-design
```

## Available Skills

| Skill | Description |
|-------|-------------|
| **molten-brand** | Guide brand, positioning, persona, messaging, and voice discovery, then write `molten-docs/brand/brand.md` for downstream app and design work. |
| **molten-design** | Translate `molten-docs/brand/brand.md` into a Google DESIGN.md–spec `design.md` (tokens, components, do's and don'ts). Reads brand first; defers strategy to the brand brief. |
| **molten-landing** | Create or audit high-converting landing pages. Routes to a build workflow (outputs `index.html` + `styles.css`) or a 22-point conversion audit, both graded against a shared set of conversion principles. |

## Lifecycle order

```
molten-validate (pro) → molten-brand → molten-design → molten-landing
```

Install [molten-os-pro](https://github.com/switch-dimension/molten-os-pro) for **molten-validate** and other pro skills.

## Repository layout

```
skills/
├── molten-brand/
│   └── SKILL.md              # Phased discovery → molten-docs/brand/brand.md
├── molten-design/
│   └── SKILL.md              # Visual system → design.md (reads molten-docs/brand/brand.md)
└── molten-landing/
    ├── SKILL.md              # Router: build vs audit + principles summary
    └── references/
        ├── principles.md     # Shared 7 conversion principles
        ├── creating.md       # Build workflow
        └── auditing.md       # 22-point audit checklist
```

Each skill is one folder under `skills/` with a required `SKILL.md`. The folder name matches the skill `name` in frontmatter. Detailed workflows live in `references/` and load on demand (progressive disclosure). Optional `scripts/` and `assets/` are also supported (see the [Agent Skills spec](https://agentskills.io/)).

## Status

Early development. More lifecycle skills will be added over time.

## License

TBD
