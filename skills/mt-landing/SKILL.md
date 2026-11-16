---
name: mt-landing
description: Molten OS Core — create or audit high-converting landing pages (build → index.html + styles.css, or 22-point audit). Use for landing page, waitlist, sales page, or conversion review. Reads `molten-docs/brand/brand.md` and `molten-docs/design/design.md` when present. Routes to build or audit workflow by intent.
metadata:
  author: switch-dimension
  version: "1.2.0"
  molten-suite: molten-os
  molten-category: product
  molten-tier: core
  molten-order: "4"
---

# Landing Page

This skill covers the full landing-page lifecycle: **building** a new page and **auditing** an existing one. A landing page has one job — convert a visitor on a single action. Not a homepage, not a brochure site.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- Ask concise questions in small batches. Group related questions together — don't drip them out one at a time.
- Ask every question as plain numbered text in chat so the user can answer by reference, especially when dictating in voice mode. Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).
- For multiple-choice questions, list the options as lettered sub-items under the numbered question (1a, 1b, 1c) so the user can reply with something like "1b, 2a". Use this for conversion goal, awareness level, output format, and build vs audit.
- Ask open-ended questions as numbered prose questions when the answer is free text (transformation, mechanism, proof assets, objections, traffic source).
- Batch related questions into a single message when they belong to the same phase.
- If the user already provided an answer, or `molten-docs/brand/brand.md` / `molten-docs/design/design.md` already answers it, do not ask again.

## Step 1 — Route to the right workflow

Decide which mode the user is in, then read the matching reference file before doing anything else:

- **Build / create** a new page (build, design, draft, mock up, prototype, "make me a landing page") → read [`references/creating.md`](references/creating.md) and follow it.
- **Audit / review** an existing page (review, audit, critique, grade, QA, "is this good", "does this convert", "how do I improve this") → read [`references/auditing.md`](references/auditing.md) and follow it.

If the intent is ambiguous (e.g. "help me with my landing page"), ask one numbered question with two options: (a) build a new page or (b) review an existing one. Don't load both reference files.

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
