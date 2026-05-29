# Molten OS Core

An agentic product lifecycle skill pack for [skills.sh](https://skills.sh)—reusable capabilities for AI coding agents (Cursor, Claude Code, Windsurf, and more).

## Installation

```bash
npx skills add switch-dimension/molten-os-core
```

Install a single skill:

```bash
npx skills add switch-dimension/molten-os-core --skill landing
npx skills add switch-dimension/molten-os-core --skill brand
npx skills add switch-dimension/molten-os-core --skill design
```

## Available Skills

| Skill | Description |
|-------|-------------|
| **brand** | Guide brand, positioning, persona, messaging, and voice discovery, then produce a project-root `brand.md` for downstream app and design work. |
| **design** | Translate `brand.md` into a Google DESIGN.md–spec `design.md` (tokens, components, do's and don'ts). Reads brand first; defers strategy to `brand.md`. |
| **landing** | Create or audit high-converting landing pages. Routes to a build workflow (outputs `index.html` + `styles.css`) or a 22-point conversion audit, both graded against a shared set of conversion principles. |

## Repository layout

```
skills/
├── brand/
│   └── SKILL.md              # Phased discovery → brand.md
├── design/
│   └── SKILL.md              # Visual system → design.md (reads brand.md)
└── landing/
    ├── SKILL.md              # Router: build vs audit + principles summary
    └── references/
        ├── principles.md     # Shared 7 conversion principles
        ├── creating.md       # Build workflow
        └── auditing.md       # 22-point audit checklist
```

Each skill is one folder under `skills/` with a required `SKILL.md`. Detailed
workflows live in `references/` and load on demand (progressive disclosure).
Optional `scripts/` and `assets/` are also supported (see the
[Agent Skills spec](https://agentskills.io/)).

## Status

Early development. More lifecycle skills will be added over time.

## License

TBD
