# Molten OS handoff

After scoring, set **`molten_next_skill`** in the report frontmatter only — do not duplicate handoff guidance in chat (see **Chat closing** below).

Requires [molten-os-core](https://github.com/switch-dimension/molten-os-core) installed for `molten-brand`, `molten-design`, `molten-landing`.

## Decision table

| Total (after caps) | Verdict | `molten_next_skill` | Guidance |
|--------------------|---------|---------------------|----------|
| 40–50 | Pursue | `molten-brand` | Run riskiest-assumption test **in parallel** with early **molten-brand** only if experiment is under 2 weeks; otherwise experiment first, then `molten-brand` |
| 30–39 | Pursue cautiously | `molten-validate` | Close gaps from **Gaps to close** or full interview; re-validate before `molten-brand` |
| 20–29 | Pivot | `molten-validate` | Use pivot hints; re-validate after pivot — not `molten-brand` yet |
| <20 | Kill | `none` | Do not invoke molten-brand / molten-design / molten-landing unless user explicitly reframes |

## Core skill chain (when pursuing)

```
molten-validate (pro) → molten-brand → molten-design → molten-landing
```

- **molten-brand** — reads nothing from molten-validate automatically; user should attach or point to latest `molten-docs/validate/product-score-N.md`.
- **molten-design** — requires `brand.md`.
- **molten-landing** — can use `brand.md` + `design.md` when building a page.

## Output path (required)

Write and read score files **only** under `molten-docs/validate/`. Create the directory if missing. See [`report-template.md`](report-template.md).

## Chat closing (always)

Point the user to the markdown report. **No supplementary summary** (no verdict recap, score breakdown, red flags, experiment, or `molten_next_skill` in chat).

Example:

> Review your evaluation in **`molten-docs/validate/product-score-3.md`**.

Follow [`report-template.md`](report-template.md) § After writing.
