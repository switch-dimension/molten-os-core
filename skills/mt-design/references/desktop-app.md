# Surface Reference: Desktop Product

Read this when the chosen **design surface** is a desktop application, Electron app, native tool, IDE-like workflow, or keyboard-heavy multi-pane product. It layers surface-specific guidance on top of the shared spine in `SKILL.md`. The shared token core (colors, typography, radius, spacing, motion) is decided in `SKILL.md`; this file governs the **surface layer** — layout, density, component set, Pinterest angles, and the preview slice.

## What this surface optimizes for

A desktop product supports repeated, often expert, workflows where speed, density, keyboard access, and persistent context matter. Prioritize multi-pane structure, discoverable commands, precise controls, and strong focus states.

- **Prioritize:** window chrome, menu/command patterns, sidebars, split panes, toolbars, dense lists/tables, keyboard shortcuts, resizable regions, durable focus states.
- **De-emphasize:** mobile tab bars, thumb-zone constraints, oversized marketing hero sections, touch-first spacing that wastes desktop real estate.

## Layout & structure

- Use a desktop-width canvas and define a durable app shell: title/menu area, toolbar, sidebar, primary content pane, optional inspector/detail pane.
- Support multi-pane workflows without losing hierarchy; each pane needs a clear job.
- Allow higher density than web product screens when the audience is expert, but preserve reading and scanning rhythm.
- Define resize behavior and minimum usable pane widths when relevant.
- Treat command palette, menus, shortcuts, and context menus as first-class interaction surfaces.

## Density

Medium-to-high density. Desktop products can carry more visible controls than mobile or marketing pages, but hierarchy must stay crisp. Use subtle dividers, grouped panels, and compact control spacing rather than large marketing whitespace.

## Component set to define

- **Buttons / controls:** primary, secondary, icon button, toolbar button, destructive.
- **Inputs:** text, select, checkbox/radio, toggle, search/command input, with focus/error/disabled states.
- **Navigation:** sidebar, menu bar, toolbar, breadcrumbs or tabs when useful.
- **Panes / panels:** resizable split pane, inspector panel, card/panel, empty state.
- **Tables / lists:** dense rows, selected row, hover/active, keyboard focus, grouped lists.
- **Overlays:** command palette, dropdown/context menu, modal/dialog, toast/notification.

Keyboard focus and shortcut discoverability are mandatory. Never hide critical actions behind hover-only controls.

## Pinterest search angles

Every term must read as a **desktop app UI**. Anchor words: `desktop app ui`, `electron app design`, `mac app interface`, `productivity app desktop`, `desktop dashboard ui`, `developer tool ui`. Vary within desktop patterns — command palette, sidebar, split pane, inspector, dense data view, settings — not landing-page or mobile terms. Add one brand modifier from `brand.md`.

Example (calm developer SaaS):

1. `developer tool desktop app ui`
2. `electron app sidebar design`
3. `desktop productivity app interface`
4. `command palette app ui`
5. `dark desktop dashboard ui`

## Preview slice (`example.html`)

The realistic combined UI section should be a **desktop app window** at a wide viewport, with a title/menu or toolbar area, sidebar or split pane, main content region, and one keyboard-oriented control such as search or command input. Show selected, hover, and focus-visible states.

## Surface do's and don'ts

- Do make keyboard navigation and focus order obvious.
- Do design persistent context with panes, sidebars, or inspectors when useful.
- Don't use mobile-only navigation patterns for a desktop tool.
- Don't let density erase hierarchy; group related controls clearly.

## Accessibility notes

- Focus-visible styles must work across menus, toolbar controls, panes, and tables.
- Text and icon-only controls need accessible names.
- Keyboard shortcuts should have discoverable labels or command-palette entries.
- Respect reduced motion for pane, menu, and modal transitions.
