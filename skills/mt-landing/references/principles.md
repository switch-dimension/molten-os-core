# The seven conversion principles

Shared rubric for both building and auditing landing pages. Treat these as the standard the page is measured against.

## 1. One page, one goal (attention ratio)

- Exactly one primary CTA action. Repeat it 3–5 times down the page using the *same* button copy.
- No top navigation links that lead away from the conversion. A logo in the top-left is fine; a sticky nav with "Pricing / Features / About / Blog / Login" is not. If a login link is required, make it small, top-right, single link.
- Footer can have legal links (Privacy, Terms) and that's about it.
- Every section must justify itself by moving the visitor toward the CTA. If you can't say what job a section is doing, cut it.

## 2. Lead with the outcome, then the mechanism

- **H1 = the transformation the visitor wants**, in their words. Not "AI-powered analytics platform" — "Know which marketing actually made you money, by Friday."
- **Sub-head (one to two sentences) = the mechanism**, plain language. "We connect to your ad accounts and your Stripe, and show you the dollars-in / dollars-out per channel."
- The first screen (above the fold) must answer: *what is this, who is it for, why now*. Include the primary CTA in the hero.

## 3. Match the message to visitor awareness

Eugene Schwartz's five stages run from coldest to warmest. This skill works in three primary stages day-to-day, but know the bookends so you can handle cold and hot traffic:

- **Unaware** (cold): doesn't know they have the problem. Rare for paid landing pages — lead with a story, a surprising stat, or a relatable scenario before you can even name the pain. If you find yourself here, question whether a landing page is the right format at all.
- **Problem-aware**: open by naming the pain sharply. Educate on the category before pitching the product. Longer page.
- **Solution-aware**: open with positioning — why this product over the alternatives they're already considering. Comparison-friendly.
- **Product-aware**: open with the offer and a reason to act now. Shorter page. Heavier on social proof and risk reversal.
- **Most-aware** (hot): already wants it, just needs the deal and a nudge. Shortest page — offer, price/terms, risk reversal, CTA. Don't re-sell what they've already decided.
- Mirror the traffic source's language in the H1 and opening lines (message match). If the ad said "stop guessing which ads work," the page should not open with "welcome to AcmeAnalytics."

## 4. Earn trust fast with concrete proof

- Put proof *high* on the page — directly under the hero is a good spot for a logo strip or a single strong testimonial.
- Prefer concrete over vague: "$2.3M in tracked revenue across 412 stores" beats "trusted by leading brands." Real names with roles and companies beat anonymous quotes. Screenshots of the actual product beat illustrations.
- Pre-empt skepticism. If the claim sounds too good, the next line should address the obvious "yeah but…".

## 5. Scroll narrative, not a "layout"

- Structure as a repeating beat: **Hook → Value → Proof → Objection → CTA** — then loop with a new angle.
- A workable default outline (cut sections you don't need; don't pad):
  1. **Hero** — H1 outcome, sub-head mechanism, primary CTA, one supporting visual or short proof line.
  2. **Proof strip** — logos, headline metric, or one strong testimonial.
  3. **Problem / stakes** — name the pain. (Skip if product-aware audience.)
  4. **How it works** — 3 steps or 3 pillars showing the mechanism delivering the outcome.
  5. **Outcome details / features-as-benefits** — 2–4 blocks, each framed as a result, not a spec.
  6. **Deeper proof** — testimonial(s) with names/companies, case study snippet, or a metrics block.
  7. **Objection handling / FAQ** — answer the top 2–4 hesitations directly. Use the user's own objection list.
  8. **Final CTA block** — restate the transformation, repeat the same CTA, add risk reversal microcopy.
  9. **Footer** — minimal: small logo, legal links, copyright.
- Use progressive disclosure: don't dump pricing or detailed specs above the fold. Earn the scroll first.

## 6. Low-friction CTA, clear offer

- CTA button copy is specific and outcome-focused. "Start tracking my ad ROI" beats "Submit." "Get my free audit" beats "Get started." "Reserve my spot" beats "Sign up."
- Microcopy under the CTA reduces anxiety: "No credit card required.", "Takes 30 seconds.", "We'll never share your email.", "Cancel any time." Pick the ones that match the real friction.
- If there's a form, ask only for what's truly needed to fulfill the next step. Email-only for waitlists. Email + name maximum for most lead magnets. Defer everything else to a follow-up step.

## 7. Visual hierarchy steers attention

- **One accent color, reserved for the primary CTA.** Everything else is neutral (one near-black for text, one or two greys, white/off-white background). No secondary buttons in the same accent color — use a ghost/outline style if a secondary action is unavoidable.
- **Strong type scale.** H1 should feel almost uncomfortably large on desktop (e.g., `clamp(2.5rem, 5vw, 4.5rem)`). H2s clearly smaller but still confident. Body around 18px. Line-height generous (1.5–1.7 for body, 1.1–1.2 for big headlines).
- **Generous whitespace.** Section padding `clamp(4rem, 8vw, 8rem)` top/bottom is a sane default. Don't cram.
- **Max content width** around 1100–1200px for sections; narrower (600–700px) for prose-heavy blocks so lines don't get hard to read.
- **One typeface is fine.** A modern sans (Inter, Geist, system-ui) is the safe default. Two max: one display, one body.
- Mobile-first: stack on small screens, hero text shrinks fluidly with `clamp()`, tap targets at least 44px tall.
