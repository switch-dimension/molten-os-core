# Surface Reference: Mobile Product

Read this when the chosen **design surface** is a phone-first mobile application. It layers surface-specific guidance on top of the shared spine in `SKILL.md`. The shared token core (colors, typography, radius, spacing, motion) is decided in `SKILL.md`; this file governs the **surface layer** — layout, density, component set, Pinterest angles, and the preview slice.

## What this surface optimizes for

A mobile product is used in short sessions, often one-handed, with limited screen space and no hover state. Prioritize clarity, touch comfort, strong hierarchy, and focused single-screen flows.

- **Prioritize:** 44px minimum touch targets, single-column layout, bottom navigation or tab bars, list rows, cards, sheets, thumb reach, safe areas, concise labels.
- **De-emphasize:** hover-dependent affordances, dense multi-column dashboards, tiny table controls, wide desktop navigation, complex nested menus.

## Layout & structure

- Design around a narrow viewport (~360-430px) and scale up only if needed.
- Use a clear top app bar or header area, plus bottom navigation when there are 3-5 primary destinations.
- Favor one primary action per screen; secondary actions can move into overflow menus or sheets.
- Use cards and list rows for scanability, but avoid stacking too many nested surfaces.
- Respect safe areas and keep critical actions within comfortable thumb reach.

## Density

Medium density. Mobile can be compact, but not cramped. Preserve enough whitespace for tap accuracy and reading rhythm. Use short labels, progressive disclosure, and bottom sheets instead of trying to show every control at once.

## Component set to define

- **Buttons:** primary, secondary, destructive, icon button, floating action button only if the product needs it.
- **Inputs:** text, select-like picker, toggles, checkboxes/radios where appropriate, with focus/error/disabled states.
- **Navigation:** top app bar, bottom tab bar, segmented control, back affordance.
- **Lists / rows:** title, metadata, leading/trailing icon, selected/pressed/disabled states.
- **Cards:** compact content cards with clear tap behavior.
- **Sheets / dialogs:** bottom sheet, confirmation dialog, toast/snackbar.

Every interactive component must define touch target size and pressed/focus-visible state. Do not rely on hover.

## Pinterest search angles

Every term must read as a **mobile app UI**. Anchor words: `mobile app ui`, `ios app design`, `android app ui`, `mobile interface`, `app home screen`. Vary within mobile patterns — home, lists, tab bar, onboarding, profile, cards — not landing-page or desktop-dashboard terms. Add one brand modifier from `brand.md`.

Example (calm developer SaaS):

1. `minimal productivity mobile app ui`
2. `ios saas app home screen`
3. `mobile app dashboard design`
4. `clean mobile app list ui`
5. `dark mode mobile app interface`

## Preview slice (`example.html`)

The realistic combined UI section should be a **phone-width frame** (~390px) showing a top/header area, primary content list or cards, bottom navigation or primary action, and thumb-friendly controls. Demonstrate touch target sizing and pressed/focus-visible styling.

## Surface do's and don'ts

- Do design for one-handed use and clear tap targets.
- Do keep each screen focused on one main job.
- Don't use hover-only cues or tiny desktop-style controls.
- Don't squeeze wide tables or multi-column dashboards into a phone frame.

## Accessibility notes

- Minimum interactive target is 44x44px for primary touch controls.
- Body text should stay at or above 16px unless labels are clearly secondary.
- Support reduced motion for sheet, tab, and navigation transitions.
- Ensure focus-visible styles work for keyboard and switch-control users.
