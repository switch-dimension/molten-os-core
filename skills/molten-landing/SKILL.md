---
name: molten-landing
description: Molten OS Core — create or audit high-converting landing pages (build → index.html + styles.css, or 22-point audit). Use for landing page, waitlist, sales page, or conversion review. Reads `molten-docs/brand/brand.md` and `molten-docs/design/design.md` when present. Routes to build or audit workflow by intent.
metadata:
  author: switch-dimension
  version: "1.2.0"
  molten-suite: molten-os
  molten-tier: core
  molten-order: "4"
---

# Landing Page

This skill covers the full landing-page lifecycle: **building** a new page and **auditing** an existing one. A landing page has one job — convert a visitor on a single action. Not a homepage, not a brochure site.

## Operating Rules

- Ask concise questions in small batches. Group related questions together — don't drip them out one at a time.
- Prefer the agent's structured question tool for any question with a finite set of meaningful options (conversion goal, awareness level, output format, build vs audit).
- **Structured question tool by agent:**
  - **Codex:** `request_user_input`
  - **Claude Code:** `AskUserQuestion`
  - **Cursor:** `AskQuestion`
- Ask open-ended questions conversationally in chat when the answer is free text (transformation, mechanism, proof assets, objections, traffic source).
- Never list multiple-choice options as letters or bullets in chat text. Multiple choice → structured question tool. Open-ended → plain prose.
- Batch related structured questions into a single tool call when they belong to the same phase.
- If the user already provided an answer, or `molten-docs/brand/brand.md` / `molten-docs/design/design.md` already answers it, do not ask again.

## Step 1 — Route to the right workflow

Decide which mode the user is in, then read the matching reference file before doing anything else:

- **Build / create** a new page (build, design, draft, mock up, prototype, "make me a landing page") → read [`references/creating.md`](references/creating.md) and follow it.
- **Audit / review** an existing page (review, audit, critique, grade, QA, "is this good", "does this convert", "how do I improve this") → read [`references/auditing.md`](references/auditing.md) and follow it.

If the intent is ambiguous (e.g. "help me with my landing page"), use the structured question tool with one choice: build a new page vs review an existing one. Don't load both reference files.

After a build, offer an audit. After an audit that fails badly, offer a rewrite — the two workflows chain naturally.

## Shared foundation

Both workflows are graded against the same conversion principles. The full rubric lives in [`references/principles.md`](references/principles.md); read it when you need the detail. For calibration — what a great hero looks like, a model audit entry, and copy formulas (PAS, AIDA, BAB, FAB, the 4 U's) — see [`references/examples.md`](references/examples.md). The audit workflow also bundles a deterministic metrics helper, [`scripts/audit_metrics.py`](scripts/audit_metrics.py) (standard-library Python, no install), for the measurable checks — attention ratio, WCAG contrast, spacing rhythm, font sizes, image weight, form labels; `auditing.md` explains when to run it and how to fall back if Python isn't available. The one-line version of the rubric:

1. **One page, one goal** — a single primary CTA, repeated with identical copy; minimal attention ratio.
2. **Outcome before mechanism** — H1 is the transformation; sub-head is how it works, in plain language.
3. **Match message to awareness** — problem- / solution- / product-aware shapes how much to educate; mirror the traffic source.
4. **Proof, high and concrete** — real numbers, named testimonials, product screenshots beat vague claims.
5. **Scroll narrative** — Hook → Value → Proof → Objection → CTA, looped, not a flat "layout".
6. **Low-friction CTA** — specific outcome-focused button copy, anxiety-reducing microcopy, minimal form fields.
7. **Visual hierarchy** — one accent color reserved for the CTA, strong type scale, generous whitespace, mobile-first.
