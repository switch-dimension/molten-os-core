# Re-validate

Use when a prior **`product-score-*.md`** exists or the user reports new evidence from an experiment.

## Workflow

1. **Find the latest score file** in `molten-docs/validate/` (create the folder when writing if missing). If the user points to an older path, read that file for context but write the new report under `molten-docs/validate/`. Read the prior file fully.
2. Ask in chat (or one `AskQuestion`):
   - What changed since the last evaluation? (new interviews, LOIs, revenue, pivot, failed experiment)
   - Did they run the **riskiest-assumption test** from the prior report? Outcome vs threshold?
3. **Re-run only rounds that new evidence affects** — do not repeat unchanged rounds; record "unchanged from prior" in raw answers.
4. Re-score with [`scoring.md`](scoring.md); cite **new** evidence in the Why column.
5. Write a **new** `product-score-N.md` (never overwrite). Include:
   - `mode: revalidate`
   - `prior_score_file: molten-docs/validate/product-score-(N-1).md`
   - **Score delta** table (criterion, old, new, reason)
6. Apply [`molten-handoff.md`](molten-handoff.md).

## Experiment outcomes

| Outcome | Action |
|---------|--------|
| Hypothesis **falsified** | Lower relevant scores; verdict likely Pivot or Kill; new experiment or stop |
| **Inconclusive** | Hold or slight adjust; prescribe narrower retest with tighter threshold |
| **Supported** | Raise criterion 3 (and related) only if stranger + costly commitment is documented; still no "go build" without addressing weakest criteria |

## If no prior file exists

Treat as **full interview** ([`full-interview.md`](full-interview.md)) and note in the report that this is a baseline evaluation.
