# Full interview (5 rounds)

Use for **full** mode. One round per turn unless the user explicitly asks to run all rounds in one go.

**Language:** `AskQuestion` labels and chat must follow [`glossary.md`](glossary.md) — plain terms, no jargon, **no book/framework/author names**. Customer-discovery rules in glossary § Customer discovery.

## Skip logic

Before each round, check what the user already provided:

- If Round 1 hypothesis already states **customer + problem + alternative**, confirm in one sentence instead of re-asking Round 2.
- If they cited **stranger evidence** in the pitch, confirm Round 3 selections instead of repeating every option.
- If they named a **beachhead and channel**, confirm Round 4 instead of re-asking.
- Still run **scoring**, **red flags**, **experiment**, and **report** even when rounds are skipped.

---

### Round 1 — Frame the hypothesis

If the user hasn't stated the idea precisely, ask them to fill the blanks:

> "We believe **[target customer]** struggles with **[problem]** in **[context]**, and would adopt **[solution]** because **[unique value]**."

Echo it back verbatim. Do not editorialise yet. If they've already given a clear one-liner, restate it in this template and confirm.

---

### Round 2 — Customer, problem, current alternatives

Ask in one `AskQuestion` call. Questions mirror **customer discovery** (glossary): focus on their life today, not your pitch.

- **"How close are you to the customer?"**
  - "I am the customer myself"
  - "I know them well (work with them, family, etc.)"
  - "I've talked to them but don't live their problem"
  - "I haven't talked to one yet"
- **"How are they solving this today?"**
  - "Spreadsheet / manual / paper / WhatsApp"
  - "A paid competitor"
  - "A free good-enough alternative (Notion, Sheets, ChatGPT, etc.)"
  - "Doing nothing — accepting the pain"
  - "I don't know"
- **"How severe is the pain?"**
  - "Hair-on-fire — they already pay or hack around it"
  - "Painful but tolerated"
  - "Annoying, not urgent"
  - "Nice-to-have"
  - "Not sure"

After: restate **customer + problem + current alternative** in one sentence. If their evidence is weak, say **why in plain language** (e.g. "only compliments, no past behaviour described" / "hypothetical interest, no workaround today") — do not label it with a framework name.

---

### Round 3 — Demand evidence (most important)

Ask in one `AskQuestion` call. Both questions allow multi-select:

- **"What evidence do you have from STRANGERS (not friends, family, advisors)?"** (multi)
  - "Strangers have described this problem to me unprompted"
  - "≥10 strangers interviewed about their real workflow (past behaviour, not pitching my idea)"
  - "I've observed the workflow / pain in the wild"
  - "Strangers gave costly commitment (LOI, deposit, pre-pay, time)"
  - "Only friends / family / advisors / LinkedIn reactions"
  - "No evidence yet"
- **"What costly actions have prospects taken?"** (multi)
  - "Money — paid pre-order, deposit, paid pilot"
  - "Reputation — letter of intent, intros to others, public endorsement"
  - "Time — ≥30-min interview, repeat conversations, workflow walkthrough"
  - "Nothing yet"

**Hard rule:** if only "friends / advisors / LinkedIn" or "no evidence" is selected, name Red Flag #1 *now*, state the **25/50 total cap** and **criterion 3 max 2/5**, and design the experiment step to fix stranger evidence first.

---

### Round 4 — Differentiation, beachhead, distribution

Ask in one `AskQuestion` call:

- **"Compared to the BEST existing alternative (including 'do nothing' and spreadsheets), this is 10× better on:"** (single)
  - "Speed / time-to-first-value"
  - "Cost"
  - "Outcome quality"
  - "Effort required from the user"
  - "Trust / brand / data"
  - "It isn't 10× better — it's incrementally better"
- **"Name the SMALLEST segment you can dominate in 12–18 months."** (single)
  - "Specific role + industry + size (e.g. 'solo bookkeepers serving e-commerce in the UK')"
  - "A role across industries (e.g. 'all bookkeepers')"
  - "An industry without role specificity"
  - "'Everyone who…' / 'anyone with…'"
- **"Pick ONE repeatable distribution channel."** (single)
  - "Built-in virality / network effect inside the product"
  - "Existing community / audience I own"
  - "SEO / content with named search intent"
  - "Direct outbound to a known target list"
  - "Paid ads (checked: what you earn per customer exceeds what you spend to get them)"
  - "Partnerships / integrations"
  - "I don't know yet"

Flag in chat (plain language): only incrementally better than alternatives; target is "everyone who…"; distribution channel unknown; or paid ads chosen without unit-economics check.

---

### Round 5 — Business model + why-you-why-now

Ask in one `AskQuestion` call:

- **"Bottom-up unit economics: # customers × realistic price × capture rate. Is lifetime value at least ~3× cost to acquire each customer?"** *(Lifetime value = what one customer pays you over time; acquisition cost = what you spend to win them — ads, sales time, etc.)*
  - "Yes — modelled bottom-up; revenue per customer is ~3×+ what it costs to acquire them"
  - "Top-down only ('1% of a $X market')"
  - "Haven't done the math"
- **"Why YOU?"** (Founder–market fit)
  - "I live the problem / am the customer"
  - "Deep domain experience"
  - "I can build it uniquely well"
  - "I have unique distribution / audience"
  - "None of the above stand out"
- **"Why NOW? What changed in the last 1–3 years that unlocks this?"**
  - "Specific tech shift (LLMs, on-device ML, new API, hardware)"
  - "Regulatory / market change"
  - "Behavioural / cultural shift"
  - "Nothing specific — it's always been a problem"

"Top-down only" + "None of the above" + "Nothing specific" together is a strong kill signal.

---

## After Round 5

1. Read [`scoring.md`](scoring.md) and score all 10 criteria with cited evidence per row.
2. Run red-flag scan (scoring.md § Red flags).
3. Design the riskiest-assumption experiment.
4. Write `molten-docs/validate/product-score-N.md` per [`report-template.md`](report-template.md); apply [`molten-handoff.md`](molten-handoff.md) for chat closing (file pointer only — no summary).
