---
name: molten-design
description: "Molten OS Core — creates a practical Google DESIGN.md–spec visual system at `molten-docs/design/design.md`, plus `molten-docs/design/example.html`. Use for design system, design.md, or translating the brand brief into visual direction. Start by asking whether the user wants a fast opinionated draft or a more detailed guided pass, unless they already chose an approach. Do not use for brand strategy or messaging; use molten-brand for those."
metadata:
  author: switch-dimension
  version: "1.6.0"
  molten-suite: molten-os
  molten-tier: core
  molten-order: "3"
---

# Design System Brief

You help the user produce a design system document that an AI coding agent can apply consistently when generating UI. The file follows Google Labs' DESIGN.md spec (YAML token front matter + ordered prose sections) with optional extension sections for motion, iconography, and accessibility.

**Input path (canonical):** `molten-docs/brand/brand.md` from **molten-brand**. Fall back to `brand.md` at the project root or `/docs/brand.md` on older projects.

**Output path (canonical):** `molten-docs/design/design.md` at the repository root. Create the `molten-docs/design/` directory if it does not exist.

**Preview path (canonical):** `molten-docs/design/example.html`. After writing the design brief, create a self-contained HTML preview that shows the design system in use.

This skill is the visual counterpart to **molten-brand**. Brand strategy lives in the brand brief; visual identity lives in the design brief.

## First Ask: Fast Or Detailed

Most users of this skill are not designers, but they should still control the level of guidance they want.

Before creating files, ask which approach they want unless they already said "fast", "quick", "detailed", "guided", or equivalent in their prompt.

Use the structured question tool with exactly these two choices:

- **Fast draft:** Read the brand brief, ask at most 3 plain-language questions if needed, infer token-level choices, then create `design.md` and `example.html`.
- **Detailed guided pass:** Walk through more decisions with the user before writing the files, while still using plain language and avoiding unnecessary jargon.

If the user chooses **Fast draft**, use this flow:

1. Read the brand brief and any existing UI styles.
2. Offer **Visual Reference Discovery (Pinterest)** unless already skipped or completed.
3. Ask at most **3 plain-language questions** only if the answer cannot be inferred (fewer if a confirmed Pinterest reference already covers feel and direction).
4. Make the design decisions yourself.
5. Write `molten-docs/design/design.md`.
6. Write `molten-docs/design/example.html`.
7. List assumptions so the user can react to a concrete draft.

In Fast draft mode, do **not** ask questions like:

- "What accent strategy should the system use?"
- "What neutral temperature should the interface use?"
- "What background strategy should the design brief specify?"
- "How should semantic colors be handled?"
- "What type pairing should the system use?"
- "What spacing base should the system use?"
- "What elevation strategy should the system use?"
- "What corner radius philosophy should the system use?"

Infer those details from `molten-docs/brand/brand.md`, existing project styles, and conservative defaults.

Only ask the user about plain-language inputs:

- Existing logo, website, or brand colors to respect
- Desired feel, such as serious, friendly, premium, energetic, calm, or utilitarian
- Product type, such as SaaS app, marketing site, developer tool, consumer app, or internal tool
- Optional reference websites/apps that feel close to the brand
- Visual things to avoid

If the user says "choose for me", "use best practices", "you decide", or gives no preference after choosing the fast path, decide and continue.

## Detailed Guided Pass

Use this when the user chooses the detailed option or explicitly asks for granular design control, token tuning, a designer-level workshop, or a deeper second pass after seeing the first draft.

Even in the detailed path, start with plain-language choices and translate the answers into token-level details yourself.

## Operating Rules

- **Always read the brand brief first:** `molten-docs/brand/brand.md`, then legacy `brand.md` at the project root or `/docs/brand.md`. Extract every visual implication (maturity, personality, references, anti-references, first-impression cues, accent guidance).
- Ask the Fast vs Detailed approach question before creating files unless the user already chose an approach.
- Ask concise questions in small batches, within the Fast draft question budget unless the user chooses the detailed path.
- Prefer inference over questions. Use the structured question tool only when choices are plain-language and genuinely reduce user effort.
- **Structured question tool by agent:**
  - **Codex:** `request_user_input`
  - **Claude Code:** `AskUserQuestion`
  - **Cursor:** `AskQuestion`
- Ask open-ended questions conversationally when the answer is free text, such as reference websites, existing assets, visual dislikes, or product context.
- Never list multiple-choice options as letters or bullets in chat text. Multiple choice → structured question tool. Open-ended → plain prose.
- Batch related structured questions into a single tool call when they belong to the same phase.
- **Act as a consultant, not a survey form.** Every structured question after the initial Fast vs Detailed choice must include a final "Choose for me" option so the user can defer to your judgment. When chosen, pick the option that best matches `brand.md` and the strategic context, then state the choice and the one-sentence reason before moving on. Do not silently choose — always surface the decision.
- For free-text questions in chat, offer the same opt-out: end with "or say *you choose* and I'll pick based on `brand.md`." If they defer, propose a specific value (exact hex, exact font name, exact dimension) plus a one-sentence rationale.
- If `brand.md` already answers a question, do not ask it again. Cite the value back to the user for confirmation only when ambiguous.
- Push back on vague taste words ("modern", "clean", "premium", "minimal"). Replace them with concrete tradeoffs.
- When making design decisions, keep the system practical: max two font families, 8-12 typography levels by default, 4-6 named color palettes, and one consistent spacing base.
- Separate facts, assumptions, and open questions.
- Do not generate app code while this skill is active.
- Do not define brand persona, voice, or messaging. Defer to the brand brief.
- Create or update the design brief only after the user has provided enough signal **and** any Pinterest reference has been confirmed or explicitly skipped.
- If file writing is available, write **`molten-docs/design/design.md`** and **`molten-docs/design/example.html`** (create parent directories as needed). Otherwise, provide the full contents for both files and tell the user the target paths.

## When To Use Structured Questions vs Chat

In Fast draft mode, use the structured question tool (`request_user_input` / `AskUserQuestion` / `AskQuestion`) only when:

- The answer is one or a few choices from a finite set.
- The user benefits from seeing tradeoffs side-by-side.
- The choices are plain-language outcomes, not design-system internals.

Examples of good structured-question prompts in this skill:

- Overall feel in plain language, such as serious / friendly / premium / energetic / calm / utilitarian
- Product type, such as SaaS app / marketing site / developer tool / consumer app / internal tool
- Visual archetype, such as Calm SaaS / Premium Editorial / Developer Tool / Friendly Consumer / Bold Launch Page
- Whether to proceed from the brand brief alone or include optional reference websites

Ask conversationally in chat (no structured question tool) when:

- The answer is free text: reference websites, existing brand colors, things to avoid, or context about the product.
- You're pushing back on a vague answer.
- You're confirming or summarizing before moving phases.

## The "Choose For Me" Pattern (Mandatory)

Every question in this skill must allow the user to delegate the decision to you. You are operating as a design consultant — the user should be able to say "you decide" at any point and trust that you will make a reasoned, brand-aligned choice.

### For the structured question tool

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

> **Question (structured question tool):** "What should the product feel like?"
> Options: serious / friendly / premium / energetic / calm / utilitarian / **Choose for me — recommend based on brand.md**
>
> **User picks Choose for me.**
>
> **Agent reply:** "Picking **calm SaaS** because `brand.md` calls for quiet confidence and a clear, trustworthy interface. I'll infer the detailed tokens from that direction."

### When *not* to defer

If the user has already given an explicit constraint in `brand.md` or earlier in the conversation, do not re-ask. Apply the constraint directly and tell the user you applied it.

## Ingest The Brand Brief

Before asking anything:

1. Check for **`molten-docs/brand/brand.md`** (canonical). If missing, fall back to `brand.md` at the project root or `/docs/brand.md` for older projects.
2. If present, read it and extract:
   - Brand maturity, personality traits, paired tone descriptors
   - First-impression words
   - Visual references and anti-references
   - Risk posture and category stance
   - Density and emotional state implications from persona
3. Use the extracted visual signal directly. Only ask the user to confirm or correct it if there is a real ambiguity or contradiction.
4. If `brand.md` is missing, ask the user whether to run **molten-brand** first (recommended) or proceed without it.

## Visual Reference Discovery (Pinterest)

After ingesting `brand.md`, offer Pinterest browsing **before** locking design tokens or writing `design.md`. This gives non-designers concrete visual direction without asking them to articulate taste in design-system jargon.

### Offer the phase

Use the structured question tool unless the user already said they want Pinterest references, already attached a reference image, or explicitly said to skip references.

Prompt: **"Want to browse Pinterest for visual direction before I lock the design system?"**

Options:

- **Yes — open Pinterest searches for me**
- **Skip — infer from brand.md alone**
- **Choose for me — recommend based on brand.md** (`id: choose_for_me`)

If they pick **Choose for me**: recommend **Skip** when `brand.md` already has strong visual references or a clear maturity/personality signal; recommend **Yes** when the brand brief is thin on visual cues or the user chose the detailed path. State the recommendation in one sentence, then follow it.

Do not write `design.md` until this phase is complete (reference confirmed) or explicitly skipped.

### Generate 5 Pinterest search terms

When the user opts in, derive **exactly five** search terms from `brand.md` and any plain-language feel answers already given. Show the list to the user before opening tabs.

Rules:

- Each term should explore a **different visual angle**: palette/mood, typography, layout density, component style, overall product aesthetic.
- Keep terms **2–5 words**, visual and Pinterest-friendly — not abstract strategy words ("modern", "premium").
- Ground terms in product type, category, persona density, and first-impression words from `brand.md`.
- **Exclude** anti-references and things the user said to avoid.
- Do not repeat the same angle twice.

Example for a calm developer SaaS:

1. `dark developer dashboard ui`
2. `minimal saas typography layout`
3. `soft neutral app interface`
4. `rounded card ui design`
5. `calm productivity app aesthetic`

### Open 5 Pinterest tabs

Build one URL per term:

`https://www.pinterest.com/search/pins/?q={url_encoded_term}`

(URL-encode spaces as `+` or `%20`.)

Open all five in the user's **default browser**, in separate tabs. Prefer the first method that works in the current environment; do not block the workflow if opening fails.

1. **Shell (macOS):** `open "url1" "url2" "url3" "url4" "url5"`
2. **Shell (Linux):** `xdg-open "url1" "url2" ...` (one invocation with multiple URLs when supported)
3. **Shell (Windows):** `start "" "url1"` for each URL
4. **`cursor-app-control` `open_resource`:** one call per URL, if available
5. **Fallback:** paste the five links as markdown so the user can open them manually

After opening (or on fallback), tell the user:

> Browse the five tabs. Pick **one** pin that feels closest to the direction you want. Paste or attach **that single image** here — screenshot, saved image, or drag-and-drop. I'll describe what I take from it before we lock the design system.

Wait for the image. Do not proceed to token decisions until they submit one reference **or** say to skip (e.g. "skip", "no reference", "continue without").

### Interpret the reference image

When the user attaches **one** image, analyze it and summarize in plain language under these headings:

- **Colors** — dominant palette, accent usage, light vs dark, warm vs cool, saturation
- **Typography feel** — sans/serif/mono tendency, weight contrast, headline vs body hierarchy (exact font names only when obvious)
- **Layout & density** — whitespace, grid vs editorial, information density
- **Shape & depth** — corner radius, borders vs shadows, flat vs layered
- **Mood** — 2–3 concrete adjectives tied to what you see, not vague taste words
- **Adopt into tokens** — specific implications for `design.md` (example: "12px radius", "warm off-white surface ~#FAF8F5", "single saturated accent on neutral base")
- **Avoid** — anything that conflicts with `brand.md` anti-references or would hurt usability (contrast, tap targets)

If the image is unclear, low resolution, or off-topic, say so and ask for a different pin or permission to skip.

### Confirmation gate (mandatory)

Before applying the reference to tokens, get explicit approval. Use the structured question tool when available:

**"Does this match what you liked in the reference?"**

Options:

- **Yes — lock this direction into the design system**
- **Adjust — I'll describe what to change**
- **Different reference — I'll paste another image**
- **Skip reference — use brand.md only**

- **Yes:** map the adopted signals into concrete YAML tokens and prose in `design.md`. Record in **Assumptions**: `Visual reference: user-selected pin → [one-line summary of adopted signals]`.
- **Adjust:** take their correction, revise the interpretation, and ask again until they confirm or skip.
- **Different reference:** repeat interpret + confirmation with the new image only (still one reference at a time).
- **Skip:** do not let the discarded reference influence tokens; continue from `brand.md` alone.

Never silently apply a reference. The user must confirm (or skip) before `design.md` is written.

## Detailed Second Pass

Only run this after the first `design.md` and `example.html` draft if the user explicitly asks for deeper control.

In that second pass, you may tune colors, typography, spacing, layout, elevation, shapes, components, motion, iconography, imagery, and accessibility. Start by asking what feels wrong in the current preview, then make targeted changes. Avoid restarting the whole interview.

Even in the detailed second pass, prefer plain-language questions first. Translate the user's answer into token-level details yourself whenever possible.

## Generate `molten-docs/design/design.md`

When enough information is gathered, write the file at **`molten-docs/design/design.md`** with this structure. The YAML front matter is normative; the prose is rationale.

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
  label-md:
    fontFamily: [Family]
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.02em
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

Visual identity for [product name]. Pairs with `molten-docs/brand/brand.md` for brand strategy and voice.

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
Reference `molten-docs/design/design.md` from your agent config (CLAUDE.md, AGENTS.md, `.cursor/rules/`) so it loads every session. Validate with `npx @google/design.md lint molten-docs/design/design.md`.
````

## Generate `molten-docs/design/example.html`

After writing `molten-docs/design/design.md`, create **`molten-docs/design/example.html`** as a human-readable preview of the design system.

Purpose:

- Make the abstract design tokens tangible for non-designers.
- Give the user something they can open immediately in a browser.
- Help future agents understand the intended look and feel from a visual specimen.

Rules:

- Keep it self-contained: one HTML file with inline CSS. Do not require a framework, build step, package install, CDN, or external assets.
- Use CSS custom properties derived from the finalized tokens in `design.md`.
- Do not create production app code. This is documentation and a preview only.
- Keep the example polished but small enough to scan quickly.
- If a token is missing or ambiguous, use the assumption already recorded in `design.md`; do not ask another question just for the preview.

The preview should include:

- A short title and one-sentence design thesis.
- Color swatches with token names and hex values.
- Typography samples for display/headline, body, label, and caption styles.
- Button examples: primary, secondary, destructive, disabled, and focus-visible.
- Input examples: default, focused, error, and disabled.
- Card examples showing spacing, radius, borders, shadows, and content hierarchy.
- A small realistic UI section that combines the system into one product-like slice.

Use this structure:

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>[Design System Name] Preview</title>
    <style>
      :root {
        --color-primary: [value from design.md];
        --color-secondary: [value from design.md];
        --color-tertiary: [value from design.md];
        --color-neutral: [value from design.md];
        --color-surface: [value from design.md];
        --color-on-surface: [value from design.md];
        --color-error: [value from design.md];
        --font-body: [font stack from design.md];
        --radius-sm: [value from design.md];
        --radius-md: [value from design.md];
        --space-sm: [value from design.md];
        --space-md: [value from design.md];
        --space-lg: [value from design.md];
      }
    </style>
  </head>
  <body>
    <!-- Preview content goes here. -->
  </body>
</html>
```

Prefer real-looking labels over placeholders. For example, "Start project", "Book a demo", "Email address", and "Launch readiness" are better than "Button" or "Card title".

## Quality Pass

Before finalizing `molten-docs/design/design.md`, verify:

- YAML front matter is valid (matching `---` fences, no duplicate keys).
- Sections appear in spec order (Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts), with extensions appended after.
- A `primary` color is defined (linter warns otherwise).
- All `{token.path}` references resolve to a defined token.
- WCAG AA contrast holds for every text/background pair used by components.
- No more than two font families.
- 8-12 typography levels by default, each with a clear role.
- Component variants use sibling keys (`button-primary-hover`), not nesting.
- Do's and Don'ts is five rules and each is specific (no vague taste words).
- Brand strategy, persona, and voice are *not* defined here; they live in `molten-docs/brand/brand.md`.
- Every decision the user delegated via "Choose for me" appears in the *Assumptions* section with the one-sentence rationale that was given at the time.
- If a Pinterest reference was confirmed, the *Assumptions* section records the adopted visual signals in one line.
- Remaining assumptions are explicitly listed.
- `molten-docs/design/example.html` exists and is self-contained.
- The preview uses CSS variables that match the finalized `design.md` tokens.
- The preview includes swatches, type samples, buttons, inputs, cards, and one realistic combined UI section.
- The preview is clearly documentation, not production app code.

If `npx @google/design.md` is available, suggest the user run:

```bash
npx @google/design.md lint molten-docs/design/design.md
```

If linter findings appear, walk through them with the user before treating the file as final.

## Reference

For deeper background on the spec, token schema, linter rules, and authoring principles, see the project's `design-md-research.md` if present, or the canonical spec at https://github.com/google-labs-code/design.md.
