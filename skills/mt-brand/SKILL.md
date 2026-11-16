---
name: mt-brand
description: Molten Loop — guide brand, positioning, persona, messaging, and voice discovery, then produce `molten-docs/brand/brand.md`. Use for brand guide, brand.md, positioning brief, or product brand strategy. Do not use for visual design systems or `design.md`; use mt-design after brand.md exists.
metadata:
  author: switch-dimension
  version: "1.2.0"
  molten-suite: molten-os
  molten-category: product
  molten-tier: core
  molten-order: "2"
---

# Brand Brief

You help the user turn brand strategy into a practical brand brief that can guide the rest of an app build.

**Output path (canonical):** `molten-docs/brand/brand.md` at the repository root. Create the `molten-docs/brand/` directory if it does not exist.

Do not jump into visual design decisions. This skill creates the brand foundation only. The **mt-design** skill should later read `molten-docs/brand/brand.md` and create or update `molten-docs/design/design.md`.

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- Guide the user via an example of how to answer. Example: "For question 1, my answer is..."
- Ask concise questions in small batches.
- Ask every question as plain numbered text in chat so the user can answer by reference, especially when dictating in voice mode. Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).
- For multiple-choice questions, list the options as lettered sub-items under the numbered question (1a, 1b, 1c) so the user can reply with something like "1b, 2a". Use this for awareness level, persona archetype, personality dimensions, tone choices, and similar tradeoffs.
- Ask open-ended questions as numbered prose questions when the answer is free text (product name, one-liner, problem description, unique copy, references).
- Batch related questions into a single message when they belong to the same phase.
- If the user already provided an answer, do not ask for it again.
- Prefer specific tradeoffs over generic taste words.
- Push back on vague answers like "modern", "clean", "premium", or "for everyone".
- Separate facts, assumptions, and open questions.
- Do not generate app code while this skill is active.
- Do not define visual design details.
- If the user gives visual preferences, defer them to `molten-docs/design/design.md` instead of adding them to the brand brief.
- Create or update the brand brief only after the user has provided enough signal.
- If file writing is available, write `**molten-docs/brand/brand.md`** (create parent directories as needed). Otherwise, provide the full markdown contents and tell the user the target path.

## When To Use Multiple-Choice vs Open Questions

Ask a numbered question with lettered options when:

- The answer is naturally one or a few choices from a finite set.
- The user benefits from seeing the tradeoffs side-by-side.
- You're forcing a decision between competing brand directions.

Examples of good multiple-choice questions in this skill:

- Awareness level (unaware / problem-aware / solution-aware / product-aware / most-aware)
- Brand maturity (playful / polished / editorial / technical / utilitarian / luxury / expressive / calm)
- Voice axes (formal vs casual, expert vs friendly, bold vs reserved)
- Buyer vs user (same person / different person / committee)
- Pricing position (free / low-cost / mid-market / premium / enterprise)
- Persona archetype, narrative arc style, primary objection type

Ask an open numbered question (no options) when:

- The answer must be free text: product name, one-liner, problem description, customer quote, claim, anti-reference, custom CTA copy, microcopy rule.
- You're pushing back on a vague answer.
- You're confirming or summarizing before moving phases.

## Phase 1: Brand Foundation

Start by asking for the minimum viable brand context. Ask open numbered questions because these answers are free text.

Cover:

- Brand or product name
- One-sentence product description
- Category or market
- The painful problem the product solves
- The promised transformation or outcome
- Existing name, tagline, domain, customers, proof, or constraints

Useful questions:

- "What is the product called, and what does it do in one plain sentence?"
- "Who has the painful problem this solves?"
- "What do users currently do instead, and why is that not good enough?"
- "What outcome should a user believe is possible after using this?"
- "Are there any existing names, taglines, domains, customer quotes, claims, or market constraints I should respect?"

## Phase 2: Positioning And Market

Once the foundation is clear, clarify the market and positioning.

Ask as multiple-choice (lettered options) for:

- Buyer vs user (same person / different person / buying committee)
- Awareness level (unaware / problem-aware / solution-aware / product-aware / most-aware)
- Pricing position (free / freemium / low-cost / mid-market / premium / enterprise)
- Category stance (follow conventions / partially break / deliberately reframe the category)

Ask in chat (free text) for:

- Primary target market and narrowing context
- Competitive alternatives and workarounds
- Differentiation and unique mechanism
- Category expectations and credibility requirements

Push for crisp positioning:

- "For [audience] who struggle with [problem], [product] is a [category] that helps them [outcome], unlike [alternative], because [mechanism or proof]."

Do not accept "small businesses", "founders", or "creators" without narrowing by situation, urgency, budget, and sophistication.

## Phase 3: Persona And Use Context

Build one primary persona first. Add secondary personas only if they change product, message, trust, or buying decisions.

Ask as multiple-choice (lettered options) for:

- Skill level (novice / intermediate / expert / mixed)
- Primary device or environment (mobile / desktop / both / specialized hardware)
- Dominant emotional state (frustrated / overwhelmed / skeptical / curious / urgent / resigned)
- Primary objection type (price / trust / complexity / time / switching cost / not-a-priority)
- Buying trigger style (proactive search / referral / forced event / curiosity / regulation)

Ask in chat (free text) for:

- Role, context, and daily workflow
- Main jobs to be done in their own words
- Specific anxieties and trust requirements
- Accessibility or environment needs
- The exact success moment

Persona quality bar:

- A strong persona can explain what the brand should say, what proof is needed, what objections must be handled, and what friction must be removed.
- A weak persona is demographic trivia that does not change product decisions.

## Phase 4: Brand Personality And Messaging

Translate strategy into voice and copy rules.

Ask the voice axes as multiple-choice, all in one message, one answer per axis:

- Formality (very formal / professional / conversational / casual / playful)
- Authority (peer-to-peer / coach / expert / authority figure)
- Energy (calm and measured / steady / energetic / bold and intense)
- Warmth (warm and human / balanced / neutral / clinical)
- Humor (none / dry wit / light / playful / overt humor)
- Narrative arc style (problem-agitate-solve / before-after / hero's journey / contrarian thesis / quiet confidence)

Ask in chat (free text) for:

- Brand personality traits in paired form ("Confident, not arrogant")
- Traits the brand must avoid
- Specific words and phrases to use
- Specific words and phrases to avoid
- Proof points, claims, and credibility markers
- Tone variations in error, empty, onboarding, and success states

Use a paired-trait format:

- "Confident, not arrogant"
- "Simple, not simplistic"
- "Technical, not opaque"
- "Warm, not cute"

## Phase 5: Brand Strategy And Handoff

Clarify the brand-level guidance that a future `molten-docs/design/design.md` should use.

Ask as multiple-choice (lettered options) for:

- Brand maturity (playful / polished / editorial / technical / utilitarian / luxury / expressive / calm) — the user may pick more than one if they want a blend
- Risk posture (safe and conventional / confident / contrarian / disruptive)
- Trust strategy emphasis (social proof / credentials / transparency / track record / demos / guarantees) — the user may pick more than one

Ask in chat (free text) for:

- Desired first impression in words, not visuals
- Brand promises the product experience must prove
- Non-negotiable brand constraints
- Claims that need evidence before use
- Concepts, metaphors, or references that might inform future brand expression

If the user gives visual references like "Apple-like", "Stripe-like", or "Linear-like", ask which brand qualities they mean. Keep the brand qualities, but defer the visual interpretation to **mt-design** / `molten-docs/design/design.md`.

## Phase 6: Generate `molten-docs/brand/brand.md`

When enough information is gathered, write the file at `**molten-docs/brand/brand.md`** with this structure.

```markdown
# Brand Brief

## 1. Brand Snapshot

### Product Name
[Name]

### One-Sentence Description
[Plain-language description]

### Category
[Category and market context]

### Core Promise
[The transformation or outcome the brand promises]

### Strategic Summary
[Short paragraph connecting audience, problem, differentiation, and brand implications]

## 2. Positioning

### Target Market
[Specific market and qualifying context]

### Primary Audience
[Who this is for]

### Buyer And User
[Clarify whether buyer and daily user differ]

### Problem
[Painful, specific problem]

### Alternatives
[Current alternatives or workarounds]

### Differentiation
[Why this product should win]

### Positioning Statement
For [audience] who [problem], [product] is a [category] that helps them [outcome], unlike [alternative], because [mechanism/proof].

### Category Expectations
[What the market expects from this kind of product]

### Beliefs To Challenge
[Old assumptions the brand must replace]

## 3. Audience And Persona

### Primary Persona
- Name: [Persona label]
- Role: [Role]
- Context: [When and where they encounter the problem]
- Skill level: [Novice/intermediate/expert and relevant vocabulary]
- Motivation: [What they want]
- Anxiety: [What they fear]
- Objections: [Reasons they might hesitate]
- Success moment: [How they know it worked]
- Trust requirements: [What they need to believe before acting]

### Secondary Personas
- [Only include if meaningfully different from the primary persona]

### Jobs To Be Done
- Functional: [Task they need to complete]
- Emotional: [How they want to feel]
- Social: [How they want to be perceived]

### Awareness Level
[Unaware/problem-aware/solution-aware/product-aware/most-aware, plus implications]

## 4. Brand Personality

### Personality Traits
- [Trait], not [bad extreme]
- [Trait], not [bad extreme]
- [Trait], not [bad extreme]

### Voice Principles
- [Rule for headlines]
- [Rule for body copy]
- [Rule for CTAs]
- [Rule for errors and empty states]
- [Rule for sales or trust-building moments]

### Words To Use
- [Word or phrase]

### Words To Avoid
- [Word or phrase]

### Tone By Context
- First impression: [Tone]
- Onboarding: [Tone]
- Core workflow: [Tone]
- Error or failure: [Tone]
- Success moment: [Tone]
- Sales or conversion moment: [Tone]

## 5. Messaging System

### Primary Message
[Main message the product should lead with]

### Supporting Messages
- [Supporting point]
- [Supporting point]
- [Supporting point]

### Narrative Arc
- Before: [User's current state]
- Struggle: [Why current options fail]
- Breakthrough: [What new belief or mechanism changes things]
- After: [User's improved state]

### Proof Points
- [Evidence, credential, customer result, demo, data point, or mechanism]

### Objection Handling
- Objection: [Objection]
  Response: [How the brand answers it]

### Claims And Evidence

- Claim: [Claim the brand can make]
  Evidence needed: [Proof required before using it]

## 6. Brand Experience Principles

### Experience Promises
- [Promise the product experience must fulfill]
- [Promise the product experience must fulfill]
- [Promise the product experience must fulfill]

### Product Behavior Principles
- [How the product should behave]
- [How the product should explain itself]
- [How the product should handle user uncertainty]

### Trust And Credibility
- [Trust signal]
- [Risk reducer]
- [Proof requirement]

### Things The Brand Must Never Do
- [Anti-principle]
- [Anti-principle]
- [Anti-principle]

## 7. Market And Competitive Context

### Alternatives
- [Competitor, workaround, or status quo]

### Differentiation Map
- We are more: [Quality]
- We are less: [Quality]
- We are similar to: [Reference point]
- We are different from: [Reference point]

### Category Language
- Terms to use: [Terms]
- Terms to avoid: [Terms]
- Concepts that need explanation: [Concepts]

## 8. Content And Naming Rules

### Naming Conventions
- Product features: [Naming rule]
- Plans or tiers: [Naming rule, if relevant]
- Actions and CTAs: [Naming rule]
- Events or states: [Naming rule]

### CTA Patterns
- Primary CTA: [Pattern]
- Secondary CTA: [Pattern]
- Avoid: [Pattern]

### Microcopy Rules
- [Rule]
- [Rule]
- [Rule]

## 9. Design Handoff

This brand document does not define visual design details.

Create or consult `molten-docs/design/design.md` (via **mt-design**) for visual design decisions, interface design, and design-system implementation guidance.

## 10. Open Questions And Assumptions

### Open Questions
- [Question that still needs a user decision]

### Assumptions
- [Assumption made due to missing information]

### Next Step
Run **mt-design** to create or consult `molten-docs/design/design.md`.
```

## Quality Pass

Before finalizing `molten-docs/brand/brand.md`, verify:

- The target market is specific enough to exclude bad-fit users.
- The persona changes actual brand, copy, trust, and product decisions.
- The positioning statement names an alternative.
- The messaging system includes proof and objection handling.
- The voice guidance includes use and avoid rules.
- No visual design details are defined.
- Visual preferences are deferred to `molten-docs/design/design.md`, not included in the brand brief.
- The document includes clear "use" and "avoid" guidance.
- Remaining assumptions are explicitly listed.

If the brief feels generic, ask one more round of sharper questions before writing the final file.