---
name: molten-design
description: "Molten OS Core — creates a practical Google DESIGN.md–spec visual system at `molten-docs/design/design.md`, plus `molten-docs/design/example.html`. Use for design system, design.md, or translating the brand brief into visual direction. Start by choosing one design surface (landing page, web product, mobile product, or desktop product), then load the matching surface reference and ask whether the user wants a fast draft or detailed pass. Do not use for brand strategy or messaging; use molten-brand for those."
metadata:
  author: switch-dimension
  version: "1.8.0"
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

## First Ask: Design Surface

At the start of every run, establish **one design surface** for this session. Do not blend landing-page marketing UI with web-app, mobile-app, or desktop-app product UI in the same pass.

Skip this ask only when the user already named the surface clearly (e.g. "landing page design system", "mobile app UI", "SaaS dashboard").

Use the structured question tool:

**"What is this design system for?"**

Options:

- **Landing page** — marketing / conversion pages (hero, sections, CTAs); pairs with **molten-landing**
- **Web product** — browser-based app UI (dashboards, forms, nav, dense workflows)
- **Mobile product** — phone-first app UI (lists, tabs, thumb zones, native-like patterns)
- **Desktop product** — desktop app UI (window chrome, menus, multi-pane workflows, keyboard-heavy use)
- **Choose for me — infer from brand.md and context** (`id: choose_for_me`)

When the user picks **Choose for me**, infer from `brand.md` and their prompt:

- Marketing site, waitlist, launch, or single-page conversion → **Landing page**
- SaaS, admin, developer tool, internal tool, dashboard, or responsive browser app → **Web product**
- Consumer app, field tool, or on-the-go phone-first workflow → **Mobile product**
- Electron, native desktop app, menu bar, command palette, IDE/tooling, or keyboard-heavy multi-window app → **Desktop product**

State the choice and one-sentence reason before continuing.

## Surface Reference Routing

After the design surface is chosen, read exactly one surface reference before Pinterest, token, component, or preview decisions:

| Chosen surface | Required reference |
| --- | --- |
| Landing page | `references/landing-page.md` |
| Web product | `references/web-app.md` |
| Mobile product | `references/mobile-app.md` |
| Desktop product | `references/desktop-app.md` |

These references contain the surface-specific guidance: layout, density, component set, Pinterest search anchors, preview slice, and surface do's/don'ts. Keep `SKILL.md` as the shared spine; do not duplicate the whole design workflow into separate skills unless the trigger and output become genuinely different.

### One surface at a time

- Scope **every** decision in this run — tokens, components, Pinterest searches, `example.html`, and Do's and Don'ts — to the chosen surface only.
- Record the surface in the **Overview** and **Assumptions** sections of `design.md` (example: `Design surface: landing page`).
- If the user needs more than one surface (e.g. landing page **and** web app), finish this run for the chosen surface, then run **molten-design** again for the next surface. Do not expand scope mid-session.

## First Ask: Fast Or Detailed

Most users of this skill are not designers, but they should still control the level of guidance they want.

Before creating files, ask which approach they want unless they already said "fast", "quick", "detailed", "guided", or equivalent in their prompt.

Batch **Design surface** and **Fast vs Detailed** into one structured question tool call when both are still unknown.

Use the structured question tool with exactly these two choices for the workflow:

- **Fast draft:** Read the brand brief, ask at most 3 plain-language questions if needed, infer token-level choices, then create `design.md` and `example.html`.
- **Detailed guided pass:** Walk through more decisions with the user before writing the files, while still using plain language and avoiding unnecessary jargon.

If the user chooses **Fast draft**, use this flow:

1. Confirm **design surface** (landing page, web product, mobile product, or desktop product).
2. Read the matching surface reference from `references/`.
3. Read the brand brief, existing `design.md` if present, and any existing UI styles.
4. Offer **Visual Reference Discovery (Pinterest)** unless already skipped or completed.
5. Ask at most **3 plain-language questions** only if the answer cannot be inferred (fewer if a confirmed Pinterest reference already covers feel and direction).
6. Make the design decisions yourself — scoped to the chosen surface.
7. Write or update `molten-docs/design/design.md`.
8. Write `molten-docs/design/example.html`.
9. List assumptions so the user can react to a concrete draft.

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

- **Read the brand brief before design decisions:** `molten-docs/brand/brand.md`, then legacy `brand.md` at the project root or `/docs/brand.md`. Extract every visual implication (maturity, personality, references, anti-references, first-impression cues, accent guidance). Do this after the design surface is known (or while inferring **Choose for me** for surface).
- **Read the matching surface reference before design decisions:** `references/landing-page.md`, `references/web-app.md`, `references/mobile-app.md`, or `references/desktop-app.md`.
- Ask the **design surface** question at the start of every run unless already clear from the user's prompt.
- Ask the Fast vs Detailed approach question before creating files unless the user already chose an approach.
- Scope the entire run to **one** surface (landing page, web product, mobile product, or desktop product). Never mix surfaces in one pass.
- Ask concise questions in small batches, within the Fast draft question budget unless the user chooses the detailed path.
- Prefer inference over questions. Use the structured question tool only when choices are plain-language and genuinely reduce user effort.
- **Structured question tool by agent:**
  - **Codex:** `request_user_input`
  - **Claude Code:** `AskUserQuestion`
  - **Cursor:** `AskQuestion`
- Ask open-ended questions conversationally when the answer is free text, such as reference websites, existing assets, visual dislikes, or product context.
- Never list multiple-choice options as letters or bullets in chat text. Multiple choice → structured question tool. Open-ended → plain prose.
- Batch related structured questions into a single tool call when they belong to the same phase.
- **Act as a consultant, not a survey form.** Every structured question after the initial startup questions (design surface and fast vs detailed) must include a final "Choose for me" option so the user can defer to your judgment. When chosen, pick the option that best matches `brand.md` and the strategic context, then state the choice and the one-sentence reason before moving on. Do not silently choose — always surface the decision.
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

- Design surface: landing page / web product / mobile product / desktop product
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

After the **design surface** is chosen (or inferred), and before Pinterest or token work:

1. Check for **`molten-docs/brand/brand.md`** (canonical). If missing, fall back to `brand.md` at the project root or `/docs/brand.md` for older projects.
2. If present, read it and extract:
   - Brand maturity, personality traits, paired tone descriptors
   - First-impression words
   - Visual references and anti-references
   - Risk posture and category stance
   - Density and emotional state implications from persona
3. Use the extracted visual signal directly. Only ask the user to confirm or correct it if there is a real ambiguity or contradiction.
4. If `brand.md` is missing, ask the user whether to run **molten-brand** first (recommended) or proceed without it.

## Existing Design Briefs And Surface Layers

Use one canonical design brief at **`molten-docs/design/design.md`**. Do not create separate unrelated design systems for landing, web, mobile, and desktop unless the user explicitly asks for separate brands.

Structure the output as:

- **Shared core:** colors, semantic colors, typography families, base type scale, radius philosophy, spacing base, motion principles, iconography, accessibility defaults.
- **Surface layer:** layout, density, component set, navigation patterns, section patterns, interaction states, and preview slice for the chosen surface.

If `molten-docs/design/design.md` already exists:

1. Read it before making new token decisions.
2. Treat shared core tokens as locked unless the user explicitly asks to redesign the brand system.
3. Add or update only the chosen **surface layer**.
4. Record the inheritance in **Assumptions**: `Shared core inherited from existing design.md; updated surface layer: [surface]`.

If this is the first design run, create a complete `design.md` for the chosen surface and label which decisions are shared core vs. surface layer so future surface passes can inherit the core.

## Visual Reference Discovery (Pinterest)

After ingesting `brand.md`, curate Pinterest inspiration **before** locking design tokens or writing `design.md`. This gives non-designers concrete visual direction without asking them to articulate taste in design-system jargon.

Do not write `design.md` until this phase is complete (reference confirmed) or explicitly skipped.

### Generate 5 Pinterest search terms

Derive **exactly five** search terms from `brand.md`, the chosen **design surface**, any plain-language feel answers already given, and the **Pinterest search angles** in the selected surface reference. Do this **before** presenting the phase to the user.

Rules:

- Keep all five terms inside the chosen surface. Do not spread searches across unrelated concepts (palette-only, generic typography, abstract mood boards, editorial print, logo marks, etc.).
- Use the anchor words and example patterns from the selected surface reference.
- Add **one** brand/context modifier from `brand.md` where natural (category, feel, B2B/B2C, dark/light), but the surface anchor words stay mandatory in every term.
- Keep terms **3–6 words**, visual and Pinterest-friendly — not abstract strategy words ("modern", "premium", "aesthetic" alone).
- **Exclude** anti-references and things the user said to avoid.
- Do not duplicate the same pattern twice; vary within the chosen surface's patterns.
- If the five terms do not all clearly belong to the chosen surface, rewrite them before showing the list to the user.

### Offer the phase

Skip this subsection if the user already attached a reference image or explicitly said to skip references.

Do **not** ask whether they want to browse Pinterest. Present what you have already prepared, then offer to open it.

In chat, say something like:

> I've collected some visual inspiration for you on Pinterest that aligns with your brand. I can open those for you to take a look and pick one example as a favourite to aid design direction.
>
> Here are the five searches I put together:
>
> 1. …
> 2. …
> 3. …
> 4. …
> 5. …

Then use the structured question tool:

**"Shall I open these Pinterest searches for you?"**

Options:

- **Yes — open them so I can pick a favourite**
- **Skip — infer from brand.md alone**
- **Choose for me — recommend based on brand.md** (`id: choose_for_me`)

If they pick **Choose for me**: recommend **Skip** when `brand.md` already has strong visual references or a clear maturity/personality signal; recommend **Yes** when the brand brief is thin on visual cues or the user chose the detailed path. State the recommendation in one sentence, then follow it.

Only generate new search terms if the user asks for different angles; do not re-ask whether to use Pinterest at all.

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

> Take a look through the five tabs. Pick **one** pin as your favourite — the example that feels closest to the direction you want. Paste or attach **that single image** here (screenshot, saved image, or drag-and-drop). I'll describe what I take from it before we lock the design system.

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

Then:

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

The file should clearly separate:

- **Shared core:** reusable brand system tokens and principles that should remain stable across landing, web, mobile, and desktop surfaces.
- **Surface layer:** the chosen surface's layout, density, component priorities, and preview guidance.

```markdown
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

[Holistic description of look and feel. Personality, target audience, emotional response. Reference brand.md. State the design surface — landing page, web product, mobile product, or desktop product — and what this system optimizes for.]

## Shared Core

[Describe the stable cross-surface choices: color philosophy, type family pairing, radius philosophy, spacing base, motion posture, iconography posture, and accessibility defaults. If this file inherited an existing shared core, say so.]

## Colors

[Shared core. Prose describing each key palette with its role. One bullet per palette, named with descriptive language (e.g. "Midnight Forest Green") and the hex from tokens.]

- **Primary (#RRGGBB):** [Role and when to use]
- **Secondary (#RRGGBB):** [Role and when to use]
- **Tertiary (#RRGGBB):** [Role and when to use]
- **Neutral (#RRGGBB):** [Role and when to use]

## Typography

[Shared core. Prose describing the type strategy. Family choices and their roles.]

- **Headlines:** [Family, weight, voice it creates]
- **Body:** [Family, size, readability decisions]
- **Labels:** [Family, treatment, where it appears]

## Layout

[Surface layer. Grid model, max width, spacing rhythm, containment strategy for the chosen surface. Use the selected `references/*.md` file.]

## Elevation & Depth

[How visual hierarchy is conveyed. Shadows, borders, tonal layers, or flat.]

## Shapes

[Corner radius philosophy and where deviations occur.]

## Components

[Surface layer. Per-component prose: anatomy, variants, states, accessibility notes. Token specifics live in front matter. Include only components relevant to the chosen surface from the selected reference — e.g. hero/CTA/proof for landing page; nav/forms/tables for web product; tab bar/list rows/FAB for mobile product; window chrome/menus/panes for desktop product.]

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
- [Design surface: chosen surface]
- [Shared core: newly created or inherited from existing design.md]

### Next Step
Reference `molten-docs/design/design.md` from your agent config (CLAUDE.md, AGENTS.md, `.cursor/rules/`) so it loads every session. Validate with `npx @google/design.md lint molten-docs/design/design.md`.
```

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

- A short title and one-sentence design thesis (name the design surface).
- Color swatches with token names and hex values.
- Typography samples for display/headline, body, label, and caption styles.
- Button examples: primary, secondary, destructive, disabled, and focus-visible.
- Input examples: default, focused, error, and disabled (web and mobile product surfaces).
- Card examples showing spacing, radius, borders, shadows, and content hierarchy.
- One realistic combined UI section scoped to the chosen surface:
  - **Landing page:** hero + CTA + one proof/feature section
  - **Web product:** nav/sidebar slice with cards, form, or table
  - **Mobile product:** phone-width frame (~390px), status/header area, list or tab bar, thumb-friendly controls
  - **Desktop product:** desktop-width app window with title/menu area, sidebar or split pane, and keyboard-oriented control surface

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
- Sections appear in spec order (Overview, Shared Core, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts), with extensions appended after.
- A `primary` color is defined (linter warns otherwise).
- All `{token.path}` references resolve to a defined token.
- WCAG AA contrast holds for every text/background pair used by components.
- No more than two font families.
- 8-12 typography levels by default, each with a clear role.
- Component variants use sibling keys (`button-primary-hover`), not nesting.
- Do's and Don'ts is five rules and each is specific (no vague taste words).
- Brand strategy, persona, and voice are *not* defined here; they live in `molten-docs/brand/brand.md`.
- The chosen design surface (landing page, web product, mobile product, or desktop product) is stated in Overview and Assumptions; the current pass does not try to serve multiple surfaces at once.
- Shared core decisions are labeled and preserved when extending an existing `design.md`.
- Surface-layer decisions match the selected reference file.
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

For deeper background on the spec, token schema, linter rules, and authoring principles, see the project's `design-md-research.md` if present, or the canonical spec at [https://github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md).