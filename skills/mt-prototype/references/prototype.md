# Prototype path — technical spike

Build the smallest thing that answers one risky technical question: can this API, library, integration, algorithm or performance target work the way the feature needs? A spike is for learning, not shipping.

## Rules

- State the **one question** the prototype answers before building anything, and confirm it with the user.
- Write success criteria up front: "we'll know X if Y" (e.g. "we'll know the payments API supports split payouts if a test-mode call returns two transfers").
- Time-box it. Agree the box with the user (an hour or two is typical) and stop when it runs out, even if the answer is "no" or "partially".
- Choose the cheapest medium: a script, a single API call, a minimal integration, or a benchmark. Hardcoded data, no auth, no tests, no UI unless the question is about UI behaviour.
- Use test or sandbox credentials only, and only if the user provides them. Never commit secrets; read them from environment variables.
- Keep the code in `molten-docs/prototype/<slug>/` or a throwaway branch. Never merge it in as-is.

## Workflow

1. Extract the riskiest technical unknown from the discovery doc.
2. Write the question, success criteria and time-box, and confirm them with the user.
3. Build the minimum spike.
4. Run it and show the user the result (output, logs, timings).
5. Iterate at most a couple of times, and stop once the question is answered.
6. Write the learnings doc.

## Extra sections for the learnings doc

Add these after **Decisions for the spec**:

```markdown
## Success criteria and evidence (what was run, what it returned)
## Constraints discovered (limits, quotas, costs, latency, gotchas)
## Recommended approach for the build
```

## Checklist

- [ ] One question, success criteria and time-box confirmed before building
- [ ] No secrets committed; sandbox or test credentials only
- [ ] Spike run and the result shown to the user
- [ ] Constraints and the recommended approach recorded for the spec
