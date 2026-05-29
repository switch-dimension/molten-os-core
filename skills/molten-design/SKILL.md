---
name: molten-design
description: Molten OS Core — visual design system discovery and Google DESIGN.md–spec `design.md` (tokens, components, do's and don'ts). Use for design system, design.md, or translating `brand.md` into a visual system. Reads `brand.md` first. Do not use for brand strategy or messaging; use molten-brand for those.
metadata:
  author: switch-dimension
  version: "1.1.0"
  molten-suite: molten-os
  molten-tier: core
  molten-order: "3"
---

# Design System Brief

You help the user produce a `design.md` file that an AI coding agent can apply consistently when generating UI. The file follows Google Labs' DESIGN.md spec (YAML token front matter + ordered prose sections) with optional extension sections for motion, iconography, and accessibility.

This skill is the visual counterpart to **molten-brand**. Brand strategy lives in `brand.md`; visual identity lives in `design.md`.

## Operating Rules

- **Always read `brand.md` first** if it exists at the project root or `/docs/`. Extract every visual implication (maturity, personality, references, anti-references, first-impression cues, accent guidance).
- Ask concise questions in small batches.
- Prefer the `AskQuestion` tool for any question with a finite set of meaningful options (palette mood, type system, spacing rhythm, corner-radius philosophy, elevation strategy).
- Ask open-ended questions conversationally when the answer is free text (exact hex codes, font names, brand references, component anatomy notes).
- Never list multiple-choice options as letters or bullets in chat text. Multiple choice → `AskQuestion`. Open-ended → plain prose.
- Batch related `AskQuestion` items into a single tool call when they belong to the same phase.
- **Act as a consultant, not a survey form.** Every `AskQuestion` must include a final "Choose for me" option so the user can defer to your judgment. When chosen, pick the option that best matches `brand.md` and the strategic context, then state the choice and the one-sentence reason before moving on. Do not silently choose — always surface the decision.
- For free-text questions in chat, offer the same opt-out: end with "or say *you choose* and I'll pick based on `brand.md`." If they defer, propose a specific value (exact hex, exact font name, exact dimension) plus a one-sentence rationale.
- If `brand.md` already answers a question, do not ask it again. Cite the value back to the user for confirmation only when ambiguous.
- Push back on vague taste words ("modern", "clean", "premium", "minimal"). Replace them with concrete tradeoffs.
- Limit choices: max two font families, 9–15 typography levels, 4–6 named color palettes (extended swatches allowed in tokens), one consistent spacing base (typically 4px or 8px).
- Separate facts, assumptions, and open questions.
- Do not generate app code while this skill is active.
- Do not define brand persona, voice, or messaging. Defer to `brand.md`.
- Create or update `design.md` only after the user has provided enough signal.
- Write `design.md` at the project root by default. Use `/docs/design.md` only if the project already keeps docs there.

## When To Use `AskQuestion` vs Chat

Use `AskQuestion` when:

- The answer is one or a few choices from a finite set.
- The user benefits from seeing tradeoffs side-by-side.
- You're forcing a decision between competing visual directions.

Examples of good `AskQuestion` prompts in this skill:

- Palette mood, contrast posture, accent strategy
- Type pairing strategy (one family / two families / display + text split)
- Spacing base (4px / 8px / 4px with 2px half-step)
- Corner radius philosophy (sharp / minimal / soft / pill)
- Elevation strategy (shadows / borders / tonal layers / flat)
- Density (compact / balanced / spacious)
- Component shape direction (architectural / friendly / editorial)

Ask conversationally in chat (no `AskQuestion`) when:

- The answer is free text: exact hex codes, font names, custom token names, anatomy notes, brand references.
- You're pushing back on a vague answer.
- You're confirming or summarizing before moving phases.

## The "Choose For Me" Pattern (Mandatory)

Every question in this skill must allow the user to delegate the decision to you. You are operating as a design consultant — the user should be able to say "you decide" at any point and trust that you will make a reasoned, brand-aligned choice.

### For `AskQuestion`

Always append a final option with `id: choose_for_me` and a label that names the action and the basis for your judgment. Examples:

- `"Choose for me — recommend based on brand.md"`
- `"You decide — pick what fits the brand best"`
- `"Choose for me — go with the safest default for this brand maturity"`

When the user selects `choose_for_me`:

1. Pick the option that best aligns with `brand.md` signal, the strategic context, and DESIGN.md best practice.
2. State your choice explicitly: *"Picking **X** because [one-sentence reason tied to brand.md or research]."*
3. Continue to the next phase without further confirmation unless the choice is reversible-only-with-effort (e.g. primary color, type families).

### For free-text questions in chat

End the question with an explicit opt-out:

> "…or say *you choose* and I'll propose a value based on `brand.md`."

When the user opts out, propose a specific concrete value plus a one-sentence rationale. Do not propose ranges or "around X" — give the exact value the token will hold.

### Example flow

> **Question (AskQuestion):** "Accent strategy?"
> Options: single hero accent / dual accent / brand color + functional accent / **Choose for me — recommend based on brand.md**
>
> **User picks Choose for me.**
>
> **Agent reply:** "Picking **single hero accent** because `brand.md` calls for 'quiet confidence' and a single accent reinforces hierarchy without competing voices. Moving on to neutrals."

### When *not* to defer

If the user has already given an explicit constraint in `brand.md` or earlier in the conversation, do not re-ask. Apply the constraint directly and tell the user you applied it.

## Phase 0: Ingest brand.md

Before asking anything:

1. Check for `brand.md` at the project root, then `/docs/brand.md`.
2. If present, read it and extract:
   - Brand maturity, personality traits, paired tone descriptors
   - First-impression words
   - Visual references and anti-references
   - Risk posture and category stance
   - Density and emotional state implications from persona
3. Restate the extracted visual signal in 4–6 bullets and ask the user to confirm or correct before proceeding.
4. If `brand.md` is missing, ask the user whether to run **molten-brand** first (recommended) or proceed without it.

## Phase 1: Overview & Style Direction

Translate brand signal into visual direction. Use `AskQuestion` for:

- Visual maturity (playful / polished / editorial / technical / utilitarian / luxury / expressive / calm) — pre-fill from `brand.md` if defined
- Density (compact / balanced / spacious)
- Contrast posture (high contrast / balanced / soft / muted)
- Risk posture (safe and conventional / confident / contrarian / disruptive)

Ask in chat:

- Three concrete reference products whose visual feel the brand should evoke, with the specific quality each contributes (e.g. "Linear: keyboard density", "Stripe: information hierarchy")
- Three anti-references and why they're wrong for this brand
- The one-sentence visual thesis ("X is the visual identity of a brand that…")

## Phase 2: Colors

Build the palette from accent → neutrals → semantics. Use `AskQuestion` for:

- Accent strategy (single hero accent / dual accent / brand color + functional accent)
- Neutral temperature (cool grey / warm grey / true neutral / tinted with primary)
- Background strategy (pure white / off-white / dark mode first / light + dark parity)
- Semantic color approach (standard success/warning/error / custom semantic names / no semantics, use accents)

Ask in chat:

- Exact hex for primary, or describe in words and propose three options
- Whether existing brand colors must be respected (logo, marketing)
- Whether the system needs dark mode now, later, or never
- Any colors that must be excluded (competitor associations, accessibility failures)

Then produce the full palette:

- Primary, secondary, tertiary (if needed), neutral, surface, on-surface, error
- Tonal ramps if the system needs them (e.g. `primary-10` … `primary-90`)

Validate WCAG AA contrast for any text-on-background pairing before locking values. Flag failures and propose adjustments.

## Phase 3: Typography

Use `AskQuestion` for:

- Type pairing (single family across the system / display + text / serif + sans split / mono for data)
- Headline weight strategy (semi-bold / bold / extra-bold / variable)
- Letter-spacing posture (tight headlines / neutral / spacious labels)
- Number of type levels (minimal: 6–8 / standard: 9–12 / extended: 13–15)

Ask in chat:

- Exact font families (with fallback stacks) or describe and propose three options
- Whether labels/data use a different family (geometric sans, mono)
- Any weights that are off-limits (the brand reaches for one specific cut)
- Whether uppercase is allowed and where

Define the type scale with explicit token names following the spec's recommendations (`headline-display`, `headline-lg`, `body-md`, `label-sm`, etc.) and assign a role per level.

## Phase 4: Layout & Spacing

Use `AskQuestion` for:

- Spacing base (4px / 8px / 4px with 2px half-step / 8px with 4px half-step)
- Grid strategy (fluid / fixed-max-width / 12-column / 8-column / asymmetric)
- Maximum content width (narrow ~720px / standard ~1200px / wide ~1440px / no max)
- Internal padding rhythm (tight / standard / generous)

Ask in chat:

- Specific gutter and margin values, or accept defaults from base unit
- Mobile breakpoint values if the project has constraints
- Whether containment (cards, sections) is heavy, light, or absent

## Phase 5: Elevation & Depth

Use `AskQuestion` for:

- Elevation strategy (shadows / borders / tonal layers / flat with color contrast / mixed)
- Shadow intensity (none / subtle / standard / dramatic) — only if shadows are chosen
- Layer count (2 levels / 3 levels / 4+ levels)

Ask in chat:

- Specific elevation values (shadow specs, border colors, tonal shifts)
- Where each elevation level applies (cards, modals, popovers, sticky bars)

## Phase 6: Shapes

Use `AskQuestion` for:

- Corner radius philosophy (sharp 0px / architectural 2–4px / soft 8–12px / pill 9999px / mixed by component)
- Radius consistency (single radius everywhere / scaled tokens by size / per-component)

Ask in chat:

- Exact radius values for the chosen scale tokens
- Components that intentionally deviate (e.g. pill buttons, sharp inputs)

## Phase 7: Components

Cover at minimum: buttons, input fields, cards. Add chips, lists, tooltips, checkboxes, radios when the product needs them.

For each component use `AskQuestion` for shape-level decisions (size scale, default state shape, hover treatment) and ask in chat for:

- Anatomy (named parts)
- Variants (primary, secondary, tertiary, destructive)
- States (default, hover, focus, active, disabled, loading, error)
- Accessibility notes (target size, focus ring, ARIA expectations)

Encode every component in YAML tokens with state variants as sibling keys (`button-primary`, `button-primary-hover`, `button-primary-active`).

## Phase 8: Do's and Don'ts

Five rules, no more. The single highest-leverage section.

Ask in chat:

- Three things the agent must never do (specific, not vague)
- Two things the agent must always do
- Any plausible default that violates the brand identity

Examples of strong rules:

- "Never use border-radius above 8px."
- "Never use pill-shaped buttons."
- "Don't use the tertiary accent more than once per viewport section."
- "Do maintain WCAG AA contrast (4.5:1 normal text)."
- "Don't mix Space Grotesk into body text. It's for labels and interactive elements only."

## Phase 9 (optional extensions): Motion, Iconography, Accessibility

Add only if the user explicitly needs them. These are extension sections outside the core spec and the linter tolerates them.

- **Motion & Animation**: durations, easings, when motion is used, reduced-motion behavior.
- **Iconography**: icon set, size scale, stroke weight, color treatment.
- **Imagery & Illustration**: photo style, illustration treatment, anti-references.
- **Accessibility**: minimum contrast, focus rings, target sizes, reduced-motion, prefers-color-scheme behavior.

## Phase 10: Generate `design.md`

When enough information is gathered, create `design.md` at the project root with this structure. The YAML front matter is normative; the prose is rationale.

````markdown
---
version: alpha
name: [Design System Name]
description: [One sentence describing the system]
colors:
  primary: "#RRGGBB"
  secondary: "#RRGGBB"
  tertiary: "#RRGGBB"
  neutral: "#RRGGBB"
  surface: "#RRGGBB"
  on-surface: "#RRGGBB"
  error: "#RRGGBB"
typography:
  headline-display:
    fontFamily: [Family]
    fontSize: [Size]
    fontWeight: [Weight]
    lineHeight: [Line height]
    letterSpacing: [Tracking]
  headline-lg:
    fontFamily: [Family]
    fontSize: [Size]
    fontWeight: [Weight]
    lineHeight: [Line height]
  body-md:
    fontFamily: [Family]
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  label-sm:
    fontFamily: [Family]
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.05em
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  gutter: 24px
  margin: 32px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.tertiary}"
---

# [Design System Name]

Visual identity for [product name]. Pairs with `brand.md` for brand strategy and voice.

## Overview

[Holistic description of look and feel. Personality, target audience, emotional response. Reference brand.md.]

## Colors

[Prose describing each key palette with its role. One bullet per palette, named with descriptive language (e.g. "Midnight Forest Green") and the hex from tokens.]

- **Primary (#RRGGBB):** [Role and when to use]
- **Secondary (#RRGGBB):** [Role and when to use]
- **Tertiary (#RRGGBB):** [Role and when to use]
- **Neutral (#RRGGBB):** [Role and when to use]

## Typography

[Prose describing the type strategy. Family choices and their roles.]

- **Headlines:** [Family, weight, voice it creates]
- **Body:** [Family, size, readability decisions]
- **Labels:** [Family, treatment, where it appears]

## Layout

[Grid model, max width, spacing rhythm, containment strategy.]

## Elevation & Depth

[How visual hierarchy is conveyed. Shadows, borders, tonal layers, or flat.]

## Shapes

[Corner radius philosophy and where deviations occur.]

## Components

[Per-component prose: anatomy, variants, states, accessibility notes. Token specifics live in front matter.]

### Buttons

- Anatomy: [parts]
- Variants: [primary, secondary, ...]
- States: default, hover, focus, active, disabled
- Accessibility: [target size, focus ring, ARIA]

### Input Fields

[Same structure]

### Cards

[Same structure]

## Do's and Don'ts

- Do [specific rule]
- Do [specific rule]
- Don't [specific rule]
- Don't [specific rule]
- Don't [specific rule]

## Motion & Animation

[Optional. Only if defined.]

## Iconography

[Optional. Only if defined.]

## Accessibility

[Optional. Minimum contrast, focus rings, target sizes, reduced-motion.]

## Open Questions And Assumptions

### Open Questions
- [Question that still needs a user decision]

### Assumptions
- [Assumption made due to missing information]

### Next Step
Reference `design.md` from your agent config (CLAUDE.md, AGENTS.md, .cursor/rules/) so it loads every session. Validate with `npx @google/design.md lint design.md`.
````

## Quality Pass

Before finalizing `design.md`, verify:

- YAML front matter is valid (matching `---` fences, no duplicate keys).
- Sections appear in spec order (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts), with extensions appended after.
- A `primary` color is defined (linter warns otherwise).
- All `{token.path}` references resolve to a defined token.
- WCAG AA contrast holds for every text/background pair used by components.
- No more than two font families.
- 9–15 typography levels, each with a clear role.
- Component variants use sibling keys (`button-primary-hover`), not nesting.
- Do's and Don'ts is five rules and each is specific (no vague taste words).
- Brand strategy, persona, and voice are *not* defined here; they live in `brand.md`.
- Every decision the user delegated via "Choose for me" appears in the *Assumptions* section with the one-sentence rationale that was given at the time.
- Remaining assumptions are explicitly listed.

If `npx @google/design.md` is available, suggest the user run:

```bash
npx @google/design.md lint design.md
```

If linter findings appear, walk through them with the user before treating the file as final.

## Reference

For deeper background on the spec, token schema, linter rules, and authoring principles, see the project's `design-md-research.md` if present, or the canonical spec at https://github.com/google-labs-code/design.md.
