# Idea Evaluation Research

> Foundation document for the `molten-validate` skill (Molten OS Pro).
> Goal: distill how the most cited operators, investors, and authors decide whether a product / business idea is worth pursuing — and turn that into a defensible evaluation framework.

> **AGENT-INTERNAL ONLY.** Do not quote expert names, book titles, or framework brands in chat, `AskQuestion`, or `product-score-*.md`. User-facing copy: [`glossary.md`](glossary.md) (plain language + standalone customer-discovery guidance).

User-facing definitions for jargon (CAC, LTV, GTM, TAM, etc.): [`glossary.md`](glossary.md).

---

## 1. The expert panel

The frameworks below were selected because they (a) are widely cited, (b) have been pressure-tested across thousands of startups, and (c) cover complementary lenses (problem, market, solution, business, distribution, founder).

| # | Expert | Primary work | Lens |
|---|--------|--------------|------|
| 1 | **Paul Graham** | *How to Get Startup Ideas* (essay), YC essays | Idea origination, "live in the future" |
| 2 | **Sam Altman / Jessica Livingston / Michael Seibel** | YC Startup Playbook, *How to Start a Startup* | Execution, "make something people want", default alive/dead |
| 3 | **Eric Ries** | *The Lean Startup* | Validated learning, Build-Measure-Learn, MVP |
| 4 | **Steve Blank** | *The Four Steps to the Epiphany* | Customer development, "get out of the building" |
| 5 | **Rob Fitzpatrick** | *The Mom Test* | Customer interviews that don't lie |
| 6 | **Alex Hormozi** | *$100M Offers*, *$100M Leads* | Value equation, offer-driven evaluation |
| 7 | **Peter Thiel** | *Zero to One* | Monopoly, 10x, secrets, durability |
| 8 | **Marty Cagan** | *Inspired* (SVPG) | Four product risks |
| 9 | **Clayton Christensen** (+ Bob Moesta, Tony Ulwick) | *Competing Against Luck* | Jobs to Be Done |
| 10 | **Ash Maurya** | *Running Lean*, Lean Canvas | Business-model-as-product, problem/solution fit |
| 11 | **Dan Olsen** | *The Lean Product Playbook* | Product-Market Fit Pyramid |
| 12 | **Bill Aulet** | *Disciplined Entrepreneurship* (MIT) | 24-step framework, beachhead market |
| 13 | **Teresa Torres** | *Continuous Discovery Habits* | Opportunity Solution Tree, assumption testing |
| 14 | **April Dunford** | *Obviously Awesome* | Positioning relative to alternatives |
| 15 | **Seth Godin** | *Purple Cow*, *This Is Marketing* | Remarkability, smallest viable audience |

---

## 2. Each framework, condensed

### 2.1 Paul Graham — "Notice, don't think up"

PG's central claim: **the best ideas are noticed, not invented.** Trying to brainstorm startup ideas produces "plausible-sounding but bad" ideas.

The best ideas share three traits:

1. **The founders themselves want it.**
2. **They can build it.**
3. **Few others realise it's worth doing.** (The third is where most "tarpit" ideas die — many have tried, few succeeded.)

Operating questions:
- "What's missing or broken in your daily life?"
- "What do you wish someone would make for you?"
- Are you **living in the future** in some domain? The gap between that future and the present is the idea.
- Is this **organic** (grew out of your life) or **made up** (something you've decided other people must need)? Organic is preferred, especially for young founders.

### 2.2 YC playbook — "Make something people want"

The whole YC stack reduces to four ingredients (Altman): **great idea + great market + great team + great execution.**

Core operating rules:

- **Write code. Talk to users. Iterate.** Everything else is "fake work".
- **Do things that don't scale.** Recruit users one at a time.
- **Launch fast.** Simplicity beats scope.
- **Default alive vs. default dead** (Graham): at current expenses and revenue growth, will you reach profitability before running out of cash? If yes, you can choose to raise; if no, cut, accelerate, or raise *now*.
- **Better to have 100 users who love you than 1M who sort of like you.**

### 2.3 Eric Ries — Lean Startup

Treat the startup as **a series of experiments**, each testing one assumption. The unit of progress is **validated learning**, not features or money.

The Build-Measure-Learn loop:

1. **Build** the smallest thing that tests the riskiest assumption (the MVP — *not* the cheapest version of the full product; it's a learning tool).
2. **Measure** with actionable metrics (not vanity metrics like signups or pageviews).
3. **Learn** — either *persevere* (the data supports the hypothesis) or *pivot* (change one element of the business model while keeping what's been validated).

Modern (2026) adaptation: the *principles* are unchanged, but cycle times collapsed from weeks/months to days thanks to no-code, AI scaffolding, and landing-page-as-test. The discipline of measuring honestly is what still kills most teams.

### 2.4 Steve Blank — Customer Development

Blank's premise: **a startup is not a small big company; it's a search for a repeatable business model.** Search precedes execution.

The 4 steps:

1. **Customer Discovery** — turn the founders' vision into testable hypotheses about who the customer is and what problem they have. *Get out of the building*. Confirm a problem exists.
2. **Customer Validation** — confirm you can sell the solution (paying customers, repeatable sales motion). If you can't, loop back to Discovery.
3. **Customer Creation** — drive demand into the channel.
4. **Company Building** — transition from search to scale.

The three founder questions:
1. Do we *really* understand the customer's problem?
2. Do enough people care to deliver a huge business?
3. Will they care enough to *tell their friends*?

### 2.5 Rob Fitzpatrick — The Mom Test

The deepest tactical layer for evaluating an idea: **how to talk to humans without polluting the data.** Three rules:

1. **Talk about their life, not your idea.** (Don't pitch — your idea shouldn't even come up.)
2. **Ask about specific past events, not hypotheticals about the future.** ("Tell me about the last time you…" beats "Would you use a tool that…").
3. **Talk less, listen more.** ~80% customer / 20% you.

Anti-patterns to detect in your own interviews:

- **Compliments** — "That sounds like a great idea." Worthless.
- **Fluff** — generic claims, opinions about the future ("I would definitely use that").
- **Ideas** — feature requests. The motivation behind the request is what matters, not the request itself.

Good questions:
- *"Why do you bother?"* (uncovers goals)
- *"What else have you tried?"* (uncovers existing alternatives & willingness to pay)
- *"Talk me through the last time that happened."* (uncovers actual workflow & friction)
- *"What does it cost you when this goes wrong?"* (uncovers pain magnitude)
- *"Who else should I be talking to?"* (commitment + network)

Look for **commitment & advancement**: time, intros, money, public statements. Anything else is noise.

### 2.6 Alex Hormozi — The Value Equation

Hormozi's contribution is making "is this a good offer?" tractable with an equation:

```
                Dream Outcome  ×  Perceived Likelihood of Achievement
Value  =  ─────────────────────────────────────────────────────────────
                       Time Delay  ×  Effort & Sacrifice
```

To evaluate an idea, rate each variable 1–10 and attack the lowest-scoring one first:

1. **Dream Outcome** — the transformation, not the feature. Specific, emotional.
2. **Perceived Likelihood** — testimonials, guarantees, demonstrated mechanism.
3. **Time Delay** — how fast they see *first* value.
4. **Effort & Sacrifice** — how much of their behaviour, time, money, and willpower the solution consumes.

Reinforce with **scarcity, urgency, guarantees, bonuses** during commercialisation. But these are amplifiers, not substitutes — without a real Dream Outcome they accelerate a bad idea.

### 2.7 Peter Thiel — Seven Questions

If you can't answer all seven well, expect to "have bad luck":

1. **Engineering** — Can you build something 10× better than alternatives? (Not 20% better — that loses to inertia.)
2. **Timing** — Is *now* the right moment? What just changed?
3. **Monopoly** — Are you starting with a big share of a *small* market? (Not "1% of a huge market".)
4. **People** — Do you have the right team?
5. **Distribution** — Can you actually *deliver* the product? (Most underrated risk.)
6. **Durability** — Will your position hold 10–20 years out?
7. **Secret** — Have you spotted a non-obvious truth others don't see / believe?

### 2.8 Marty Cagan (SVPG) — Four Big Risks

The four risks every product must survive — discovery exists to kill them all before delivery starts:

1. **Value risk** — will customers buy / choose to use it? *(Usually the biggest.)*
2. **Usability risk** — can users figure out how to use it?
3. **Feasibility risk** — can engineers build it with the time, skill, tech available?
4. **Business viability risk** — does it work for *our* business — legal, sales channel, go-to-market, brand, monetisation, and whether **cost to acquire a customer** is sustainable vs **what that customer is worth over time**?

Cagan's strong opinion: most teams under-weight viability and over-weight feasibility.

### 2.9 Christensen / Moesta / Ulwick — Jobs to Be Done

**Customers don't buy products; they hire them to make progress.** The unit of analysis is the *job*, not the customer demographic or the product category.

Every job has three dimensions:

- **Functional** — what they need to accomplish
- **Emotional** — how they want to feel
- **Social** — how they want to be perceived

Competitors are *everything the customer considers* when the job arises — including spreadsheets, doing nothing, and category-foreign alternatives.

**Switch interviews** (Moesta): reconstruct the timeline of a real recent purchase to surface the **four forces**:

- **Push** of current frustrations
- **Pull** of the new solution
- **Anxiety** about switching
- **Habit / inertia** of the status quo

Demand only exists when push + pull > anxiety + habit.

### 2.10 Ash Maurya — Running Lean / Lean Canvas

**Your business model is the product.** Deconstruct the idea on a one-page Lean Canvas in ≤20 minutes:

```
Problem        | Solution        | UVP             | Unfair Advantage | Customer Segments
(top 3 pains   | (top 3 features | (single clear   | (can't be easily | (who exactly)
+ existing     |  that test core | compelling      |  copied)         |
alternatives)  |  value)         | message)        |                  |
─────────────────────────────────────────────────────────────────────────────────────────
Key Metrics                              | Channels
─────────────────────────────────────────────────────────────────────────────────────────
Cost Structure                           | Revenue Streams
```

Three sequential fits:

1. **Problem/Customer fit** — evidence-based case that a big-enough problem exists.
2. **Problem/Solution fit** — demonstrate *demand* for the solution (often via *demo-sell-build*, e.g. a paid pre-sale) *before* you build.
3. **Product/Market fit** — traction sufficient to justify scaling.

The crucial mindset: **demo, sell, build** — not the other way around. You don't need a product to test demand; you need an offer.

### 2.11 Dan Olsen — Product-Market Fit Pyramid

Five layers, hierarchical (each depends on the one below):

```
                 ┌──────────────┐
                 │     UX       │   ← solution
                 ├──────────────┤
                 │ Feature Set  │   ← solution
                 ├──────────────┤
                 │   Value      │   ← solution
                 │ Proposition  │
═════════════════╪══════════════╪═══════ product / market fit boundary
                 │ Underserved  │   ← market (you can't change it)
                 │   Needs      │
                 ├──────────────┤
                 │   Target     │   ← market
                 │  Customer    │
                 └──────────────┘
```

You **choose** which market you serve; you **don't change it**. PMF is the measure of how well the top three layers (under your control) serve the bottom two.

The Lean Product Process: target customer → underserved needs → value prop → MVP feature set → MVP prototype → test with customers → iterate. Use the **Kano model** to classify features (must-have / performance / delighter) — and remember delighters become must-haves over time.

### 2.12 Bill Aulet — Disciplined Entrepreneurship (MIT)

A 24-step linear-ish framework. For the evaluation phase, the **first six steps** are what matter most:

1. Market Segmentation
2. **Select a Beachhead Market** (the most-cited concept)
3. Build an End User Profile
4. TAM for the Beachhead
5. Persona for the Beachhead
6. Full Life Cycle Use Case

A valid **beachhead** passes all three tests:

1. Customers buy the **same product** (you don't have to customise per buyer).
2. They have a **similar sales cycle** and value-recognition pattern.
3. There is **word-of-mouth density** between customers — they talk to each other.

Strategic premise: dominate a small specific market first, then attack adjacent ones from a position of strength. The opposite of "we'll go after the $50B TAM."

### 2.13 Teresa Torres — Continuous Discovery / OST

The **Opportunity Solution Tree** structures discovery so the team always knows what they're learning and why:

```
                    ┌── Desired Outcome ──┐
                    │  (one, measurable)   │
                    └──────────┬───────────┘
                               │
                  ┌────────────┼────────────┐
              Opportunity  Opportunity  Opportunity
              (customer    (need, pain,  …
               need)        desire)
                  │            │
              Solution     Solution
                  │            │
              Experiment   Experiment
              (assumption test)
```

Cadence: **at least one customer interview per week per product trio (PM + Designer + Eng)**. Update the tree weekly. Test the **riskiest assumptions** first — categorised as *desirability*, *usability*, *feasibility*, *viability*, and *ethical*.

The unit of test is the **assumption**, not the idea. Rank assumptions on a 2×2: high-uncertainty × high-importance → test first.

### 2.14 April Dunford — Positioning

Positioning isn't a tagline; it's the **context** you place yourself in so your value becomes obvious. Default positioning ("we're a CRM") often hides your real strength. The 5-step exercise:

1. **Competitive alternatives** — what would the customer do if you didn't exist? (Includes spreadsheets, status quo, in-house tools.)
2. **Unique attributes** — what do you have that the alternatives don't?
3. **Differentiated value** — translate those attributes into customer benefits ("so what?").
4. **Best-fit customers** — the segment that cares most about that value.
5. **Market category** — the frame of reference that makes your strengths obviously central, not peripheral.

The strongest evaluation question: *if a buyer compares this against [competitive alternative], can they articulate within 30 seconds why they'd pick this?*

### 2.15 Seth Godin — Purple Cow & Smallest Viable Audience

In a saturated market, **"adequate" is invisible.** Only **remarkable** products earn organic distribution. Remarkability is built *into the product*, not bolted onto marketing.

Evaluation questions:
- Is this idea **worth making a remark about**?
- Would a stranger naturally tell another stranger about it?
- Who is the **smallest viable audience** that will love it so much they evangelise? (Better 1,000 true fans than 1M tepid users.)
- Is the product engineered for **idea spread** (a "remarkability vector"), or are you relying on paid acquisition to manufacture interest?

---

## 3. Synthesis — where everybody agrees

Despite different vocabularies, **eight themes** appear across nearly every framework. These form the spine of any defensible evaluation:

### Theme 1 — A real problem, felt by a specific person

> *Blank: customer discovery. Olsen: target customer + underserved needs. Christensen: the Job. Maurya: top-3 problems. Aulet: persona + beachhead. Fitzpatrick: talk about their life.*

**Test:** Can you name the person, the painful moment, and what they currently do to cope — in their own words, not yours?

### Theme 2 — Severity & frequency of the pain

> *Hormozi: dream outcome. Christensen: push of current frustration. PG: "missing or broken in your daily life."*

**Test:** Is this a "hair-on-fire" problem (painkiller) or a "nice-to-have" (vitamin)? Are they already paying for inferior solutions, or hacking workarounds with spreadsheets/manual labour?

### Theme 3 — Demand evidence from strangers, not friends

> *Fitzpatrick: commitment & advancement. YC: do things that don't scale. Maurya: demo-sell-build. Modern validation: smoke test, LOI sprint, concierge MVP.*

**Test:** Have ≥10 strangers in the target segment described the problem **without your prompting**? Have ≥3 taken a costly action (LOI, deposit, pre-order, time commitment)?

### Theme 4 — Differentiated, defensible value

> *Thiel: 10× & monopoly & durability. Dunford: differentiation vs. alternatives. Godin: purple cow. Maurya: unfair advantage. Cagan: value risk.*

**Test:** Compared to the best existing alternative (including "do nothing" and spreadsheets), is your value at least an order of magnitude better on the axis customers actually care about? What can't be easily copied?

### Theme 5 — A reachable beachhead, not a TAM dream

> *Aulet: beachhead 3 tests. Olsen: target customer first. Godin: smallest viable audience. Thiel: big share of a small market.*

**Test:** Can you name a segment small enough to dominate in 12–18 months, where buyers share a product, a sales cycle, and a word-of-mouth network?

### Theme 6 — A working business model (not just a working product)

> *Cagan: viability risk. Hormozi: value equation amplifiers. YC: default alive/dead. Bottom-up unit economics.*

**Test:** Bottom-up math — # of customers × realistic price × realistic capture rate. Compare **lifetime value** (what one customer is worth over time) to **cost to acquire a customer** (ads, sales, outbound). Is lifetime value at least ~3× acquisition cost at a realistic price? Can you afford to acquire them? (See [`glossary.md`](glossary.md).)

### Theme 7 — Distribution, not just product

> *Thiel: distribution question. Godin: remarkability as built-in distribution. PG: "live in the future" includes seeing how people will discover it.*

**Test:** Can you name *one* channel where you can repeatably reach this customer for less than they're worth? Is the product engineered to spread, or does it depend entirely on paid acquisition?

### Theme 8 — Founder–market–timing fit

> *Thiel: timing + people. PG: founders want it & can build it. YC: great team. Aulet: founder competence.*

**Test:** Why you? Why now? Name a recent technological, regulatory, behavioural, or cultural shift that makes this possible *now* in a way it wasn't 2–3 years ago. What's your unfair domain insight?

---

## 4. Where the experts diverge (and what to do about it)

| Dimension | Camp A | Camp B | How to reconcile |
|---|---|---|---|
| Origin of ideas | **PG, YC** — notice, don't think up; organic > engineered | **Aulet, Maurya** — disciplined process can produce great ideas | Most ideas the agent will be asked to evaluate already exist. Don't litigate origin; evaluate substance. |
| Talk-to-customers first | **Blank, Fitzpatrick, Torres** — interview before anything | **PG, YC** — talk to users *while* building; just ship | Reconcile via stage: pre-MVP → interviews; once shippable, *interview + ship* in parallel weekly. |
| Market size framing | **Aulet, Thiel** — small market first, dominate it | **Generic VC** — show a $1B+ TAM | Always do **bottom-up** TAM for the beachhead first; top-down only as sanity check. |
| Build vs. demo | **Ries** — MVP that tests the riskiest assumption | **Maurya** — demo-sell-build, don't build until you've sold | Both agree: don't build the full product. The "MVP" can be a landing page, video, LOI, concierge service. |
| 10× better | **Thiel** — must be 10× to dethrone incumbents | **Christensen** — better-on-the-job, not necessarily 10× on every axis | Be 10× better *on the axis the job rewards*, not 10× across the board. |
| Differentiation | **Dunford** — frame yourself against alternatives | **Godin** — be so remarkable you create your own frame | Use Dunford to defend, Godin to attack. Both are forms of "be obviously different on something that matters." |

---

## 5. Common failure modes (red flags) to detect

Pulled from the modern startup-failure literature, cross-referenced with the frameworks above:

1. **"Validation" is friends, advisors, or LinkedIn likes.** Compliments are not commitment.
2. **Hypotheticals beat behaviour.** "I would buy that" with no past action is noise — see glossary § Customer discovery.
3. **No competitors / no existing alternatives.** Usually a sign that others tried and the market said no, not that you've found a hidden goldmine.
4. **Top-down TAM only.** "1% of a $50B market" is a planning fiction. Bottom-up or it didn't happen.
5. **Solution-first thinking.** The pitch starts with the product, not the customer's painful moment.
6. **Requires significant behaviour change** with no proportional payoff. Habit + anxiety > push + pull.
7. **Free, good-enough incumbent.** If Notion / Sheets / a free tool already covers the workflow for 80% of users, you need the free option to be visibly inadequate.
8. **Can't articulate the customer in one sentence.** Vague targeting → vague product → no traction.
9. **Distribution is "we'll do content marketing and ads".** Channel is undefined or assumes paid acquisition is cheaper than customer lifetime value without evidence.
10. **The only person excited is the founder.** Lukewarm co-founder + polite interviewees + unresponsive waitlist = the market is telling you no.
11. **Tarpit ideas** (PG): seemingly obvious ideas (e.g. "Yelp for X", "social network for Y") where dozens have tried and quietly failed. *Few realising it's worth doing* is a feature, not a coincidence.
12. **Mid-funnel storytelling without unit economics.** Engagement metrics without revenue intent is a vanity metric.

> **Rule of thumb:** any three of these flags co-occurring is "stop and reassess." Five or more is "kill or pivot."

---

## 6. A unified evaluation framework

Combining all of the above into a single rubric. Each criterion is scored 0–5, with explicit anchors. Total = 50.

| # | Criterion | Lens(es) | 0 — fatal | 5 — strong |
|---|-----------|----------|-----------|------------|
| 1 | **Problem clarity** | Blank, Olsen, Christensen | Vague "people struggle with X" | Specific person, specific trigger moment, in their own words |
| 2 | **Pain severity** | Hormozi, Christensen, Fitzpatrick | Nice-to-have; no workaround in use | Existing workarounds / spend / pain visible; "hair on fire" |
| 3 | **Demand evidence** | Ries, Maurya, YC, Fitzpatrick | Compliments from friends only | ≥3 strangers gave costly commitment (LOI / pre-pay / time) |
| 4 | **Differentiation** | Thiel, Dunford, Godin | "Like X but cheaper / nicer" | 10× better on the axis the job rewards; not easily copyable |
| 5 | **Beachhead viability** | Aulet, Olsen, Godin | "Everyone who…" | Same product, same sales cycle, word-of-mouth network |
| 6 | **Business viability** | Cagan, YC | Lifetime value < cost to acquire at realistic price | Bottom-up math works at ≥~3:1 (lifetime value : acquisition cost) with credible channel |
| 7 | **Distribution path** | Thiel, Godin | "We'll do content + ads" | One channel identified with credible unit economics or built-in virality |
| 8 | **Timing / "why now"** | Thiel, PG | "It's always been a problem" | Specific recent shift (tech, regulation, behaviour) unlocks this |
| 9 | **Founder–market fit** | PG, YC, Thiel | No domain advantage; built because it sounded cool | Founders live the problem, can build, see something others don't |
| 10 | **Riskiest-assumption testability** | Ries, Torres, Maurya | Can't articulate what would prove it wrong | Riskiest assumption named + cheapest experiment designed |

Interpretation (rough heuristic):

- **40–50** — pursue aggressively; design the riskiest-assumption test.
- **30–39** — pursue cautiously; named gaps must be closed before building.
- **20–29** — pivot one or two pyramid layers (usually customer or value prop).
- **<20** — kill or radically reframe; the idea as stated is structurally weak.

---

## 7. The evaluation workflow (turning rubric into action)

A repeatable seven-step flow that the future skill will operationalise:

1. **State the idea as a one-sentence hypothesis** in the form:
   *"We believe [target customer] struggles with [problem] in [context], and would adopt [solution] because [unique value]."*

2. **Map the Lean Canvas** (Maurya) — 20 minutes, by hand. Force every block.

3. **Run customer-discovery conversations** (glossary) — ≥10 strangers in the segment, no pitching. Look for commitment + past behaviour. Confirm problem clarity and pain severity before solution fit.

4. **Score against the 10-criterion rubric** (Section 6). Identify the three weakest criteria.

5. **For each weak criterion, name the riskiest assumption** behind it and design the cheapest experiment that could falsify it (Torres / Ries). Build an Opportunity Solution Tree if there are competing solution paths.

6. **Run the 7-question / 4-risks check** (Thiel + Cagan) as a "would this survive contact with reality?" gate. Specifically pressure-test value, viability, distribution, durability.

7. **Decide: pursue / refine / pivot / kill.** Document the assumptions you're betting on and the evidence required to disconfirm them. Re-evaluate at the next milestone.

---

## 8. What this gives the skill (agent behaviour)

The live skill should:

- **Trigger** when a user describes an idea, asks "is this a good business?", drops a one-liner pitch, or wants to validate a concept.
- **Ask structured questions** per [`full-interview.md`](full-interview.md) and glossary § Customer discovery — past behaviour, not hypotheticals; force clarity on customer, problem, alternative, evidence.
- **Score** on the 10-criterion rubric using [`scoring.md`](scoring.md); in user output, explain *what was checked*, not which author said it.
- **Flag red flags** from Section 5 in plain language.
- **Recommend the next action** — almost always an experiment to falsify the weakest assumption, never "go build the thing."
- **Refuse to validate** ideas with only friends-and-family evidence.

---

## 9. Reading list (agent-only bibliography)

Do **not** add this section to `product-score-*.md` or chat unless the user explicitly asks for book recommendations.

Tiered roughly by where to start.

**Tier 1 — start here**
- Rob Fitzpatrick, *The Mom Test*
- Paul Graham, *How to Get Startup Ideas* (free essay)
- Eric Ries, *The Lean Startup*

**Tier 2 — go deeper**
- Steve Blank, *The Four Steps to the Epiphany*
- Ash Maurya, *Running Lean* (3rd ed.)
- Dan Olsen, *The Lean Product Playbook*
- Teresa Torres, *Continuous Discovery Habits*
- Marty Cagan, *Inspired*

**Tier 3 — strategic lenses**
- Peter Thiel, *Zero to One*
- Bill Aulet, *Disciplined Entrepreneurship*
- April Dunford, *Obviously Awesome*
- Clayton Christensen, *Competing Against Luck*
- Alex Hormozi, *$100M Offers*
- Seth Godin, *Purple Cow* (and *This Is Marketing*)
