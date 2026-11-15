# Quick score

Use when the user wants a **fast sanity check** without the full 5-round interview.

Use [`glossary.md`](glossary.md) in chat and reports: plain language, no jargon, **no book/framework/author names** in scorecard or red flags.

## Workflow

1. **Extract or ask for** the one-sentence hypothesis (Round 1 template). One chat turn max if missing.
2. **Infer** answers to rounds 2–5 only from what the user already said. List **explicit gaps** — do not invent evidence.
3. Read [`scoring.md`](scoring.md). Score each criterion; use **1–2** on criteria where data is missing (not 4–5). Note `evidence: stated | inferred | missing` per row in the report.
4. Apply cap rules if friends-only / no stranger evidence.
5. Red-flag scan.
6. Design the **single** highest-priority experiment (same rigour as full mode).
7. Write `molten-docs/validate/product-score-N.md` via [`report-template.md`](report-template.md) with:
   - `mode: quick`
   - `interview_complete: false`
   - Section **Gaps to close** listing which full-interview rounds would change the score most.
8. Recommend **full interview** if total is 30–39 and gaps are material, or if the user plans to pursue.
9. Close per [`report-template.md`](report-template.md) § After writing — pointer to the file only, no summary in chat.

## Do not

- Run five `AskQuestion` rounds unless the user upgrades to full interview mid-session.
- Give high scores on criteria 3, 6, or 7 without user-stated evidence.
- Skip writing the file.

## Upgrade path

If the user says "let's do the full interview", switch to [`full-interview.md`](full-interview.md) from the next unanswered round; keep the same `product-score-N.md` series (new file on completion).
