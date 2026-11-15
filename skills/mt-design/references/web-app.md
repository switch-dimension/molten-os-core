# Surface Reference: Web Product

Read this when the chosen **design surface** is a browser-based application UI (dashboards, SaaS, admin, internal tools). It layers surface-specific guidance on top of the shared spine in `SKILL.md`. The shared token core (colors, typography, radius, spacing, motion) is decided in `SKILL.md`; this file governs the **surface layer** — layout, density, component set, Pinterest angles, and the preview slice.

## What this surface optimizes for

A web product is used repeatedly to get work done. Prioritize clarity, scanability, consistent navigation, and comfortable information density.

- **Prioritize:** app layout (nav/sidebar/topbar), forms, cards, tables, modals, clear focus states, dense-but-readable information UI.
- **De-emphasize:** long-scroll marketing sections, oversized campaign hero patterns, decorative whitespace that wastes screen space.

## Layout & structure

- Persistent app shell: top bar and/or left sidebar, with a primary content region.
- Content uses a responsive grid; tables and lists handle overflow gracefully.
- Tighter vertical rhythm than a landing page — more content per viewport, but never cramped.
- Define max content width for reading-heavy views; allow full-width for data tables and dashboards.
- Clear z-index/elevation story for menus, popovers, modals, and toasts.

## Density

Medium-to-high information density. Use the spacing scale's smaller steps for in-component spacing and reserve larger steps for separating regions. Borders, dividers, and subtle surfaces carry hierarchy where whitespace alone is too expensive.

## Component set to define

- **Buttons:** primary, secondary, tertiary/ghost, destructive, plus icon buttons.
- **Inputs:** text, select, checkbox/radio, toggle — with default, focus, error, disabled states.
- **Navigation:** sidebar item, top-bar item, breadcrumbs, tabs.
- **Cards / panels:** content containers with header, body, optional footer.
- **Tables / lists:** row, header, selected, hover, empty state.
- **Overlays:** modal/dialog, dropdown menu, toast/notification.

Focus states are mandatory on every interactive element (keyboard users).

## Pinterest search angles

Every term must read as a **web app / dashboard UI**. Anchor words: `web app ui`, `dashboard ui`, `saas interface`, `admin panel`, `app dashboard`. Vary within app UI patterns — nav/shell, cards, forms, data views, settings — not marketing or mobile terms. Add one brand modifier from `brand.md`.

Example (calm developer SaaS):

1. `minimal saas dashboard ui`
2. `developer web app interface`
3. `clean admin panel design`
4. `saas app sidebar navigation ui`
5. `dark mode web app dashboard`

## Preview slice (`example.html`)

The realistic combined UI section should be an **app-shell slice**: sidebar or top nav plus a content area containing cards, a form, or a table. Show focus-visible states on at least one input and one button.

## Surface do's and don'ts

- Do keep navigation consistent and predictable across views.
- Do define explicit focus, hover, active, and disabled states for every interactive component.
- Don't rely on hover-only affordances for critical actions.
- Don't borrow marketing hero scale for in-app headings; keep the type scale working at app density.

## Accessibility notes

- WCAG AA contrast for text and for UI state changes (focus rings, selected rows).
- Keyboard navigability and visible focus order; min 24–32px click targets for dense controls, larger for primary actions.
- Respect reduced-motion for transitions on menus, modals, and toasts.
