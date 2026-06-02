---
name: molten-validate
description: Molten OS Pro — adversarially validate a product or business idea (quick score, full 5-round interview, or re-validate). 10-criterion rubric (/50), red flags, falsifiable experiment; writes molten-docs/validate/product-score-N.md. Use when the user pitches an idea, asks if it is a good business/product, or wants a sanity check. Do NOT use when the idea is already validated and the user only needs implementation. Requires molten-os-core (molten-brand, molten-design, molten-landing) after a strong score.
metadata:
  author: switch-dimension
  version: "1.2.0"
  molten-suite: molten-os
  molten-tier: pro
  molten-order: "1"
  molten-requires: molten-os-core
---

# Validate a Product Idea

Adversarial idea evaluation (structured interview + 10-criterion rubric). Methodology is grounded in established startup practice — see `[references/research.md](references/research.md)` for **agent-internal** sources only. **Never end with "go build it."** Always end with a falsification experiment or an honest kill/pivot.

## Step 1 — Route to a mode

Pick **one** mode before loading other references. Do not load every reference file at once.


| Mode               | User signals                                                                              | Read next                                                      |
| ------------------ | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Quick score**    | One-liner pitch, "sanity check", "score this", pasted deck summary, no time for interview | `[references/quick-score.md](references/quick-score.md)`       |
| **Full interview** | "Validate my idea", "run the interview", first-time evaluation, ambiguous depth           | `[references/full-interview.md](references/full-interview.md)` |
| **Re-validate**    | Existing score in `molten-docs/validate/`, "I ran the experiment", "update my score"      | `[references/revalidate.md](references/revalidate.md)`         |


If ambiguous, ask once: *"Quick score from what you've shared, full 5 minute, 5-round interview , or re-validate against a previous product-score file?"*

After routing, also read when needed:

- **Glossary (user-facing language)** — before chat or `AskQuestion`: `[references/glossary.md](references/glossary.md)`
- **Scoring & caps** — before any score: `[references/scoring.md](references/scoring.md)`
- **Report file** — when writing output: `[references/report-template.md](references/report-template.md)`
- **Molten OS handoff** — after scoring: `[references/molten-handoff.md](references/molten-handoff.md)`
- **Deep research (agent-internal; never quote to user)** — only if anchors are unclear: `[references/research.md](references/research.md)`

## Operating principles (non-negotiable)

Before interactive validation, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."

1. **Past behaviour beats hypotheticals.**
2. **Compliments are not evidence** (friends, family, advisors, LinkedIn).
3. **Strangers + costly commitment = signal** (money, reputation, significant time).
4. **Bottom-up math only** — no "1% of a $50B market."
5. **Explain the check, not the guru** — user-facing text describes *what you tested and what you found*, not book titles, authors, or framework brands (Mom Test, Lean Startup, etc.). See `[references/glossary.md](references/glossary.md)`.
6. **End with falsification**, not a green light.
7. **Plain language with the user** — no unexplained jargon (CAC, LTV, GTM, TAM, LOI, etc.). Interviews and recommendations must stand alone (customer-discovery section in glossary).

## AskQuestion vs chat

- **Chat (free text):** Round 1 hypothesis, clarifications, pushback on vague answers.
- `**AskQuestion`:** Rounds 2–5 in full interview (one round per user turn unless they say "run the full interview now").
- **Numbered chat questions:** Number every free-text question asked in chat so the user can answer by reference, especially when dictating in voice mode.
- **Never** paste multiple-choice options as bullets in chat — use `AskQuestion`.
- **Do not re-ask** what the user already answered; confirm and move on.
- **One round per turn** in full interview (default).

## Progress checklist

```
- [ ] Mode selected (quick / full / re-validate)
- [ ] Hypothesis framed
- [ ] Evidence gathered (mode-appropriate)
- [ ] Scored with scoring.md anchors + cap rules applied
- [ ] Red-flag scan
- [ ] Riskiest-assumption experiment designed
- [ ] molten-docs/validate/product-score-N.md written (see report-template.md)
- [ ] User pointed to report file only — no chat summary (see molten-handoff.md)
```

## Hard rules

- **Cap total at 25/50** when the only evidence is friends, family, advisors, or LinkedIn — regardless of how good the idea sounds. Also **cap criterion 3 at 2/5** in that case (see scoring.md).
- **Never** recommend "go build it."
- **Never** accept vague customers ("everyone who…", "users").
- **Never** treat "I would use that" as evidence.
- **Never** recap the report in chat after writing — point to `molten-docs/validate/product-score-N.md` only.

## Additional resources (agent-only)

- Framework synthesis & bibliography: `[references/research.md](references/research.md)` 

