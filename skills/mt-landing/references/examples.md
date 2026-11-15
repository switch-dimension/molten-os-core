# Examples & copy formulas

Calibration material for both workflows. The golden examples show the quality bar; the formulas help you generate copy that hits it. None of this is meant to be pasted verbatim — it's a target, not a template.

## Golden example — a strong hero block

Context: a marketing-attribution tool, solution-aware traffic from a "stop guessing which ads work" ad.

```html
<section class="hero">
  <h1>Know which ads actually made you money — by Friday.</h1>
  <p class="subhead">
    We connect to your ad accounts and your Stripe, then show you dollars-in /
    dollars-out per channel. No spreadsheets, no attribution guesswork.
  </p>
  <a class="cta" href="#start">Show me my real ad ROI</a>
  <p class="cta-microcopy">Connects in 2 minutes. No credit card.</p>
</section>
```

Why it works:

- **H1 is the outcome in the visitor's words** ("know which ads made you money"), with a concrete time anchor ("by Friday") — not "AI-powered marketing analytics."
- **Sub-head is the mechanism in plain language** — what it connects to and what you get, no jargon.
- **CTA is outcome-focused and first-person** ("Show me my real ad ROI"), not "Get started."
- **Microcopy kills the two biggest frictions** (setup effort, payment risk) in one line.
- Message-matches the ad's "stop guessing" promise.

Contrast with a weak version (do not ship this):

> **H1:** Welcome to AcmeAnalytics — the all-in-one marketing intelligence platform.
> **Sub-head:** Supercharge your workflow with next-generation, AI-powered insights.
> **CTA:** Get started

Every line is category cliché, feature-first, and message-mismatched.

## Golden example — one audit check, done right

This is the level of specificity the audit should produce — quote real copy, give the verdict, write the fix:

> **2. Single goal (attention ratio) — ❌ Fail.** Counted 14 clickable elements above the footer (7 nav links, logo, 2 "Learn more", 3 social icons, 1 login) against 2 primary CTAs → ratio 7:1. The sticky nav ("Features / Pricing / Docs / Blog / About / Login") is the worst offender. **Fix:** drop the nav to just the logo + a single small top-right "Log in", and let the page route everything toward "Show me my real ad ROI." Target ratio under 3:1.

Weak version (don't do this): *"There are too many links, consider simplifying the navigation."* — no count, no quote, no concrete target.

## Copy formulas

Reach for these when a section's copy feels flat. Pick the one that fits the job; don't stack them.

### Headlines — the 4 U's

A strong H1/H2 hits as many as fit without straining: **Useful** (clear benefit), **Urgent** (why now), **Unique** (only-here angle), **Ultra-specific** (numbers, names, timeframes). "Know which ads made you money by Friday" = useful + ultra-specific.

### PAS — Problem, Agitate, Solve

Best for problem-aware audiences and the "problem / stakes" section. Name the pain → make the cost of it vivid → present the product as the relief.

> You're spending $40k/month on ads and you genuinely can't say which ones work. Every budget meeting is a guess dressed up as a decision — and the channel you're about to cut might be your best one. AcmeAnalytics ties every dollar of spend to every dollar of revenue, so you cut with evidence.

### AIDA — Attention, Interest, Desire, Action

A whole-page arc: a hook that stops the scroll → interest via the mechanism → desire via proof and outcomes → a single clear action. Maps cleanly onto the scroll narrative in `principles.md` §5.

### BAB — Before, After, Bridge

Great for the hero or a "how it works" framing. Paint the current painful state → the desired state → the product as the bridge between them.

> **Before:** monthly attribution arguments and gut-feel budget cuts. **After:** a single screen showing profit per channel. **Bridge:** connect your ad accounts and Stripe once.

### FAB — Features → Advantages → Benefits

Use this to convert any feature list into benefit copy: *feature* (what it is) → *advantage* (what that lets you do) → *benefit* (why you care). "Real-time dashboard" → "see today's numbers instantly" → "walk into the budget meeting already knowing the answer."

### CTA microcopy

Pair an outcome-focused button with a one-line anxiety reducer that names the *real* friction: "No credit card required.", "Takes 30 seconds.", "Cancel anytime.", "We'll never share your email." Don't use all four — use the one that matches the objection that actually blocks this audience.
