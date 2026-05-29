# Building a landing page

You are generating a landing page whose only job is to convert a visitor. Not a homepage. Not a brochure site. A focused, scroll-narrative page built around one action.

The rubric you write against is the seven conversion principles in [`principles.md`](principles.md). Read that file if you don't already have it in context — it is the standard every section below is measured by.

## Step 0 — Reuse existing brand and design foundations

Before asking anything, check for Molten OS Core artifacts:

- **Brand:** `molten-docs/brand/brand.md` (canonical from **molten-brand**). Fall back to `brand.md` at the project root or in `.docs/` on older projects.
- **Design:** `design.md` at the project root or in `.docs/` (from **molten-design**).

When present, these are the source of truth — don't re-ask what they already answer.

- **`molten-docs/brand/brand.md`** (or legacy root `brand.md`) typically supplies: positioning, target persona, the transformation/outcome, voice and tone, key messaging, and objections. Pull the H1 outcome, sub-head mechanism, and the objection list straight from it.
- **`design.md`** typically supplies: accent color, neutrals, type scale, font stack, spacing scale, and component conventions. Use these verbatim as your CSS variables instead of inventing a palette.

If both exist and are complete, you may be able to skip most of Step 1 — confirm only the conversion goal, traffic source, and output preference. If they're partial, ask only for the gaps. State which file you pulled from so the user can see the lineage. If neither exists, proceed to Step 1 in full (and you may offer **molten-brand** / **molten-design** first if the project would benefit).

## Step 1 — Ask the questions before you write anything

Collect the brief up front, before writing any markup. If your environment has a structured question/multiple-choice tool, use it; otherwise ask in plain text. Either way, group related questions and present them together — don't drip them out one at a time. Skip any question the user already answered in their initial prompt, or that `brand.md` / `design.md` already answers (see Step 0).

Gather these inputs (adapt phrasing to the user, but cover the substance):

1. **Primary conversion goal** — What is the *one* thing a visitor should do? (email signup, book a demo, start a free trial, purchase, join waitlist, download). If they list more than one, push back: pick the primary, the rest become secondary at best.
2. **Product / offer** — What are they selling or giving away? One sentence.
3. **Target audience and awareness level** — Who is this for, and how aware are they of the problem/solution? Problem-aware (knows the pain, not the solution), solution-aware (knows category, comparing options), or product-aware (knows your product, needs a final nudge). This shapes how much education the page needs.
4. **The transformation / outcome** — What does the visitor's life look like *after* they use this? This becomes the headline. Push for a concrete, desirable end-state, not a feature list.
5. **The mechanism** — *How* does the product deliver that outcome, in plain language? This becomes the sub-headline.
6. **Traffic source** — Where is the visitor coming from (Google search, paid ad, a specific tweet, a podcast)? The opening of the page should echo that source's language and promise.
7. **Proof assets** — What credibility do they actually have? Customer logos, testimonials with names, hard numbers (users, revenue, results), press mentions, screenshots, case studies, founder credentials. If they have none, say so — you'll work around it but the page will be weaker.
8. **Top objections** — What are the 2–4 reasons a qualified visitor would hesitate? ("too expensive", "I don't have time to learn it", "we tried something like this and it didn't work", "I'm worried about my data"). Each objection becomes copy on the page.
9. **Brand / style** — Brand name, any existing colors (or vibe: corporate / playful / minimal / bold / luxury / techy), font preference if any, and any assets/URLs they want included.
10. **Output preference** — Single self-contained `index.html` with embedded CSS, or separate `index.html` + `styles.css`? Default to separate files unless they say otherwise.

If the user is vague on any high-leverage field (especially transformation, mechanism, or proof), ask a tighter follow-up. A landing page lives or dies on specificity — generic inputs produce a generic page.

## Step 2 — Write against the seven principles

Apply every principle in [`principles.md`](principles.md). For calibration on quality and for copy formulas (PAS, AIDA, BAB, FAB, the 4 U's), see [`examples.md`](examples.md) — it shows a model hero block and the difference between strong and weak copy. After drafting, re-read the page against each principle and revise. The highest-leverage moves while drafting:

- Lead the hero with the **outcome** (principle 2), not the product category.
- Tune page length and opening to **awareness level** (principle 3) and mirror the traffic source.
- Place **concrete proof high** (principle 4) — directly under the hero.
- Build the page as a **scroll narrative** (principle 5), not a flat stack of sections.
- Reserve the **accent color** for the single primary CTA (principles 1 and 7).

## Step 3 — Produce the files

Default output: two files in the working directory.

- `index.html` — semantic HTML5. Use `<header>`, `<section>` with descriptive class names tied to the section's job (`hero`, `proof-strip`, `how-it-works`, `testimonials`, `faq`, `final-cta`), `<footer>`. Real, written copy throughout — never placeholder `Lorem ipsum`. If the user didn't give you a specific testimonial, write a realistic-*sounding* quote (right length, right tone, real objection answered) but make the **attribution obviously a placeholder** — `— [Name], [Role] at [Company]`, never a real-looking fake name. Add an HTML comment flagging it for swap. The rule: the *shape* can be invented, the *identity* must read as a stand-in.
- `styles.css` — vanilla CSS, no framework. Use CSS variables at `:root` for the accent color, neutrals, spacing scale, and font stack so the user can rebrand in one place. Mobile-first with one or two `min-width` media queries. Smooth, modern, but unfussy — no unnecessary animations, no carousels, no parallax.

### Accessibility & performance baseline (non-negotiable)

A page this skill builds must pass its own audit. Bake these in while writing, don't bolt them on later:

- **Contrast:** body text ≥ 4.5:1 against its background, large text and the CTA label ≥ 3:1. Check the accent-on-background and any muted-grey-on-white pairs before committing the palette — pick the accent and neutrals so they pass.
- **Semantic forms:** every input has a real `<label>` (visible or visually-hidden), not just a `placeholder`. Buttons are `<button>`/`<a>`, not styled `<div>`s.
- **Images:** meaningful `alt` text on content images, `alt=""` on decorative ones. Don't ship an uncompressed multi-MB hero — note the expected format (WebP/AVIF) and rough budget in a comment if you stub an image slot.
- **Type & tap:** body ≥ 16px so mobile doesn't zoom; interactive targets ≥ 44×44px.
- **Focus:** keep visible focus styles for keyboard users (don't blanket `outline: none`).
- **Fonts:** 1–2 families max; prefer `system-ui`/a single web font to keep LCP fast.

After writing, do a final pass against the seven principles **and** this baseline, and note any deliberate trade-offs to the user (e.g., "I left out a pricing section because you said the goal is waitlist signup — pricing would distract from that.").

## Step 4 — Hand off cleanly

In your closing message:

- Tell the user the two file paths.
- List the 2–4 places where you used placeholder content they should replace (testimonial quotes without real attribution, stand-in metrics, a hero image slot).
- Mention the single CSS variable they'd change to rebrand the accent color.
- Offer to iterate or to run an audit: "Want me to tighten the copy, try a different hero angle, or run the 22-point audit on what we just built?"
- **Optionally** offer to close the loop on measurement: a page only converts if you can see whether it converts. If the environment supports it, offer to instrument the primary CTA (a click/conversion event) and to set up a headline-vs-variant A/B test so the next iteration is data-driven, not guesswork. Keep this as an offer, not a default — don't add tracking the user didn't ask for.

## What to avoid

- Generic SaaS-page openers like "Welcome to [Product]" or "The all-in-one platform for…". Always open with the visitor's outcome.
- Feature lists masquerading as benefits. "Real-time dashboard" is a feature. "See today's revenue without opening five tabs" is a benefit.
- Two equally-weighted CTAs in the hero ("Start free trial" + "Book a demo" same size, same color). Pick one as primary.
- Carousels of testimonials that auto-rotate. Static, scannable proof converts better.
- Stock-photo "diverse team smiling at laptop" hero images. Prefer a real product screenshot, a clean illustration, or strong typography over a hero image.
- Long forms above the fold. If you need more than email, defer the rest.
- Inventing fake company logos or fake customer names that look real (e.g., "Acme Corp", "TechFlow Inc"). Use clearly-labeled placeholders like `[CUSTOMER LOGO]` or `[Name], [Role] at [Company]` that the user can obviously see are stand-ins. (Inventing the *wording* of a placeholder testimonial is fine — see Step 3 — but its attribution must never read as a real person or company.)
