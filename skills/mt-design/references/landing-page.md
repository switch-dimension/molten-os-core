# Surface Reference: Landing Page

Read this when the chosen **design surface** is a landing or marketing page. It layers surface-specific guidance on top of the shared spine in `SKILL.md`. The shared token core (colors, typography, radius, spacing, motion) is decided in `SKILL.md`; this file governs the **surface layer** — layout, density, component set, Pinterest angles, and the preview slice.

## What this surface optimizes for

A landing page has one job: convert a visitor on a single action. Prioritize a fast, emotional first impression and a clear path to one CTA.

- **Prioritize:** display type and hero hierarchy, section rhythm, CTA buttons, proof blocks (logos, testimonials, stats), generous marketing whitespace.
- **De-emphasize:** app chrome, data tables, dense settings UI, complex multi-level navigation.

## Layout & structure

- Full-width sections stacked vertically; one idea per section.
- Generous vertical rhythm — sections breathe (larger `spacing.xl` gaps between sections than within them).
- Content max-width for readable text (~640–760px for prose, wider for hero and feature grids).
- Single dominant CTA repeated down the page; secondary CTA is visually quieter.
- Strong type scale contrast — the display/headline step should be noticeably larger than on an app surface.

## Density

Low information density. Lean on whitespace and scale, not borders and dividers. Marketing pages can afford bigger type, bigger spacing, and bolder accent usage than product UI.

## Component set to define

Define only what a landing page needs:

- **Buttons:** primary (hero CTA), secondary, on a busy section consider an inverted/ghost variant.
- **Hero block:** headline, subhead, CTA, supporting visual.
- **Feature / benefit cards:** icon or label, heading, short body.
- **Proof block:** logo row, testimonial card, or stat strip.
- **Section headers:** eyebrow label + headline + optional subhead.
- **Footer:** links, legal, secondary CTA.

Skip app-only components (tables, sidebars, modals, settings rows) unless the page genuinely needs them.

## Pinterest search angles

Every term must read as a **landing / marketing page**. Anchor words: `landing page`, `marketing site`, `startup website`, `sales page`, `waitlist page`. Vary within landing-page patterns — hero, sections, CTA, social proof, full-page layout — not across unrelated domains. Add one brand modifier from `brand.md` (category, feel, B2B/B2C, dark/light).

Example (calm developer SaaS):

1. `saas landing page design`
2. `b2b startup landing page hero`
3. `minimal saas marketing website`
4. `landing page cta section design`
5. `developer tool landing page layout`

## Preview slice (`example.html`)

The realistic combined UI section should be a **hero + CTA + one proof/feature section** at desktop width, demonstrating the type scale contrast and the primary CTA in context.

## Surface do's and don'ts

- Do make the primary CTA unmistakable and repeat it.
- Do use scale and whitespace to create hierarchy before reaching for borders.
- Don't introduce app navigation patterns (sidebars, tab bars) on a marketing page.
- Don't define dense data components the page will never use.

## Accessibility notes

- Maintain WCAG AA contrast on hero text over imagery or gradients — add an overlay if needed.
- Tap/click target for the CTA is comfortably large; focus-visible ring is clearly defined.
