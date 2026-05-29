# Auditing a landing page

You are auditing a landing page that already exists. Your job is to run it through 22 conversion and design checks, then return a structured report the user can act on. Be a frank reviewer — call out failures specifically, propose concrete fixes, and don't pad with praise.

The checks below operationalise the seven conversion principles in [`principles.md`](principles.md). Read that file if you need the underlying rationale for any check. When you propose copy rewrites, [`examples.md`](examples.md) shows the quality bar and copy formulas (PAS, AIDA, BAB, FAB, the 4 U's) plus a model audit entry to match.

## Contents

- Step 1 — Establish what you're reviewing
- Step 2 — Run all 22 checks (Strategy, Copy, Structure, Persuasion, Design, Mobile/A11y/Perf, Final cut)
- Step 3 — Deliver the report
- Tools you'll actually use
- What to avoid

## Step 1 — Establish what you're reviewing

Before checking anything, confirm two things:

1. **Where is the page?** File on disk (`index.html` + `styles.css`), a local dev server (e.g. `http://localhost:5173`), or a public URL? If unclear, ask once.
2. **Audience awareness level (if known)** — Problem-aware, Solution-aware, or Product-aware. This is needed for check #3. If the user didn't say, infer from the page copy and state your assumption in the report (don't block on this).

If the page is a local file or dev server, render it: start the preview server (or the existing one) and take a full-page screenshot for the visual checks. If only a URL is given, fetch the rendered HTML.

## Step 1.5 — Run the metrics script first (if Python is available)

Several checks are pure measurement (counting clickable elements, computing WCAG contrast ratios, finding off-scale spacing, flagging tiny fonts and heavy images). Doing these by hand from a screenshot is unreliable — the skill bundles [`scripts/audit_metrics.py`](../scripts/audit_metrics.py) to compute them deterministically. It is **standard-library only — no `pip install`** — and prints a JSON report.

```bash
python3 scripts/audit_metrics.py path/to/index.html --cta "Exact primary CTA text"
# or against a deployed page:
python3 scripts/audit_metrics.py https://example.com --cta "Start free trial"
```

Pass the primary CTA text with `--cta` so the attention-ratio count is exact; omit it and the script guesses the CTA from the most-repeated clickable label. You can pass extra `.css` files as additional arguments; local `<link rel="stylesheet">` files are auto-discovered.

Use the JSON to ground checks **2 (attention ratio), 4 (single H1), 15/19 (contrast), 17 (spacing rhythm), 18 (font size), 19 (alt text + form labels), 20 (image weight + typeface count)**. The script *measures*; you still assign the Pass/Weak/Fail verdict and write the fix — it has no opinion on copy, layout, or taste.

**This is a fallback accelerator, not a gate.** If Python isn't available, or the page only exists in a browser you can't export, fall back to inspecting computed styles / reading the CSS by hand as each check describes. Never block the audit on the script. Note in the report whether the metrics came from the script or manual inspection.

## Step 2 — Run all 22 checks

Work through every check below. For each one, output **one of three verdicts**:

- ✅ **Pass** — meets the standard. One short sentence on what's working. Worth **1 point**.
- ⚠️ **Weak** — partially meets it, with a specific gap. State the gap + the fix. Worth **0.5 points**.
- ❌ **Fail** — doesn't meet it. State what's missing + the fix. Worth **0 points**.

Sum the points across all 22 checks for the headline score, then round down to a whole number for the `N/22` figure (so 18.5 → "18/22", with a note that two checks were Weak). Report the raw total too if it helps (e.g. "18.5/22 raw").

Group your output by section (Strategy, Copy, Proof, Structure, Design, Mobile/A11y/Perf). Within each section, list every check with its verdict and one or two sentences. Don't skip checks even when they pass — the user is looking for a complete audit, not just flaws.

For each check, do the work the check describes — don't just read the criterion aloud. Methods are noted inline.

### Strategy & framing

1. **One-sentence test (5 seconds).** Read only the first viewport. In your own words, write a single sentence answering: *what is this, who is it for, what should I do next?* If you can't, the hero needs rewriting — say which of the three pieces is missing.
2. **Single goal (attention ratio).** Count every clickable element above the footer: nav links, logo link, social icons, "learn more" buttons, sticky bar links — everything. Then count appearances of the primary CTA. Report the ratio (e.g. "11 clickable elements : 3 primary CTAs = ratio 3.7"). Best landing pages run close to 1:1. Anything above 5:1 is a fail. (The metrics script reports `attention_ratio` directly — prefer it over hand-counting.)
3. **Awareness match.** State which awareness level you believe most visitors are at, then check the H1:
   - Problem-aware: names the pain and outcome (no product name yet).
   - Solution-aware: names the category + outcome.
   - Product-aware: can name the product + differentiator.
   Mismatched H1 = fail with a suggested rewrite.
4. **Outcome first.** Quote the H1 and subhead. Label each clause as either *feature* (what it is) or *outcome* (what changes for the visitor). If features outweigh outcomes, fail it and propose a rewrite that leads with outcome.

### Copy quality

5. **Voice of customer.** Scan the copy for jargon, marketing-speak, or category clichés ("all-in-one platform", "supercharge your workflow", "next-generation"). Flag at least 2 phrases and suggest plainer alternatives. If you have no source customer language to draw from, recommend the user collect 5 customer quotes before another rewrite.
6. **Proof before persuasion.** For every superlative or strong claim on the page (fast, easy, best, #1, the only, the smartest), check the nearby copy for a proof element: a number, screenshot, testimonial, case result, logo, or specific detail. List each unbacked claim.
7. **Specificity check.** Find vague phrases and propose specifics:
   - "Save time" → "Save 3 hours a week"
   - "Teams" → "5–50 person agencies"
   - "Easy" → "Set up in 10 minutes"
   List the top 3 worst offenders with concrete replacement candidates the user can verify.

### Structure & flow

8. **Scroll architecture.** Scrolling top to bottom, confirm this beat exists at least once (compressed is fine): **Hook → Value → Proof → Objection handling → CTA → repeat CTA after proof.** Name which beats are missing or out of order.
9. **CTA consistency.** Note the exact button text everywhere the primary CTA appears. Pass requires (a) identical wording each time, (b) at least 3 appearances, (c) no equally-prominent competing secondary CTA. Quote each variant if they diverge.
10. **Friction audit.** List every form field, step, and requirement on the path to conversion. Recommend removing at least one. If the CTA is "Book a demo", suggest a lower-friction secondary option (watch demo, see pricing) styled clearly as secondary.
11. **Objection checklist.** Confirm the page answers the top three novice doubts somewhere visible:
    - "Is this for someone like me?"
    - "Will it work for my case?"
    - "What does it cost / what's the catch?"
    Missing doubts = fail with a suggested section or FAQ entry.

### Persuasion craft

12. **Clarity scan (above the fold).** All four must be present before any scrolling:
    - Who it's for
    - What it helps them do
    - How it works (simple mechanism)
    - What to do next (CTA)
    List any missing piece.
13. **LIFT scan.** For each major section, ask:
    - Does this increase clarity or relevance?
    - Does this increase perceived value or urgency?
    - Does this add anxiety or distraction?
    Flag any section that's pure distraction and suggest cutting or moving it.
14. **Emotional resonance.** Find the one line that names the feeling behind the problem (frustrated, overwhelmed, stuck, embarrassed, tired). If there isn't one, suggest one — concrete and calm, not cheesy.

### Design

15. **One accent color rule.** Identify the accent color used on the primary CTA. Then scan: does any other button, link, or decorative element use the same color *unless* it's the same primary action? Pass requires accent reserved strictly for the primary CTA; everything else uses neutrals. Read the computed styles or the CSS source to verify exact colors — don't guess from a screenshot. (The metrics script's `contrast.pairs` lists each rule's exact fg/bg hexes and ratios to work from.)
16. **Hierarchy check.** Take a screenshot, blur it mentally (or describe what a 5-pixel blur would look like): does the CTA still read as the most important element on screen? Do headings cascade in a clear order, or are there random bold bits competing for attention?
17. **Spacing rhythm.** Inspect section padding and component spacing in the CSS. Pass requires a consistent step (e.g. 4 / 8 / 12 / 16 / 24 / 32 / 48, or a `clamp()`-based scale). Flag any "one-off" values (`padding: 27px`, `margin: 43px`) that look accidental.

### Mobile, accessibility, performance

18. **Mobile pass.** Resize the rendered page to ~390px wide and verify:
    - CTA visible early or sticky
    - Text readable without zooming (≥16px body)
    - No awkward line breaks in the headline (use `clamp()` or shorter copy)
    - Tap targets ≥44×44px
    Take a mobile screenshot for the report.
19. **Accessibility (WCAG AA).**
    - Text contrast ≥4.5:1 for body, ≥3:1 for large text — pay special attention to muted greys
    - Links visually distinguishable from body text (color alone is not enough — underline or weight)
    - Images have meaningful `alt` text (decorative images can be `alt=""`)
    - Form fields have real `<label>` elements (placeholder text is not a label)
    Read computed colors from the live page to verify contrast; check the HTML source for alts and labels.
20. **Performance sanity.** Run Lighthouse or inspect by hand:
    - LCP element identified and reasonable (hero image not 4MB)
    - Images compressed (WebP/AVIF where supported, not 8000px PNGs)
    - Web fonts subset or limited to 1–2 families
    Note Core Web Vitals if Lighthouse was run; otherwise list any obvious offenders from the network tab.

### Final cut

21. **"Remove one more thing" pass.** Identify the single weakest element on the page — the section, sentence, or component that's pulling the least weight. Recommend deleting or demoting it. If nothing obvious, name the weakest section and ask the user to consider cutting it.
22. **Overall verdict.** End the report with: a one-line summary, a top-3 prioritised fix list (highest-leverage first), and the score out of 22 using the points scheme above (Pass = 1, Weak = 0.5, Fail = 0; round down for the headline figure).

## Step 3 — Deliver the report

Format the output as a single markdown report the user can paste into a doc or PR. Structure:

```
# Landing page audit — [page name or URL]

**Awareness level assumed:** Problem / Solution / Product aware
**Score:** N/22 passed

## Top 3 fixes (do these first)
1. [highest-leverage fix with location]
2. ...
3. ...

## Detailed checks
### Strategy & framing
1. One-sentence test — ✅/⚠️/❌  — [finding + fix]
...

## Final verdict
[1–2 sentences]
```

Keep each check to 2–4 sentences. The user wants signal, not an essay. Quote the page's actual copy when calling out problems — generic feedback is useless.

## Capabilities you'll need

Use whatever tools your environment exposes for each capability below — don't assume a specific tool name. Discover what's available first (file read/edit, terminal, browser/preview MCP, web fetch), then map these capabilities onto it.

- **Read local files** — for HTML and CSS when reviewing a project on disk.
- **Fetch a public URL** — for pages already deployed; pull the rendered HTML/CSS.
- **Render + screenshot** — for any local file or dev server, render the page and capture a full-page shot for the visual checks. Any available browser/preview tool works.
- **Resize / mobile viewport** — drive the render to ~390px wide for the mobile pass and capture a second screenshot.
- **Inspect computed styles** — read exact colors, font sizes, spacing, and contrast ratios from the live DOM/CSS rather than guessing from a screenshot.
- **Evaluate in-page (optional)** — run a small script to count clickable elements programmatically for the attention-ratio check.
- **Inspect network (optional)** — check image weights and the LCP element for the performance check.

Prefer reading computed styles or the CSS source over eyeballing a screenshot for colors, font sizes, spacing, and contrast — screenshots are lossy and you'll be wrong.

## What to avoid

- Don't restate the checklist as your output without doing the work.
- Don't give every check a ✅ to be polite — if you can't find a problem in 30 seconds it's probably a pass; if you find one, say so plainly.
- Don't recommend rewrites in the abstract ("make the headline stronger") — write the alternative.
- Don't grade design taste. Grade the criteria. "I'd use a different font" is noise; "body text is 14px which fails AA at this contrast ratio" is signal.
- Don't review a page the user hasn't shown you. If you can't find the file, dev server, or URL, ask — don't invent.
