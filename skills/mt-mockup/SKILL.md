---
name: mt-mockup
description: Molten Loop — optional step in the Agent Development Loop, between discovery and spec. Builds a frontend-only, fully clickable mockup of a feature or app using mocked JSON data and a fake API layer — no backend, auth, database, or real integrations — so the user can see, click through, and iterate on the UX before any expensive code is written. Asks whether the mockup should be throwaway (in `molten-docs/mockup/<slug>/`) or scaffolded as real pages in the project's own frontend, and writes the decisions to `molten-docs/mockup/<slug>.md`. Use when the user wants to mock up, wireframe-in-code, preview the UX, or iterate on a feature's design with fake data. Do not use for backend or integration work, or for answering technical feasibility questions (use mt-prototype).
metadata:
  author: switch-dimension
  version: "0.1.1"
  molten-suite: molten-os
  molten-category: dev-loop
  molten-tier: core
  molten-optional: "true"
---

# Mockup

Build the UX of a feature or app with **only frontend code and mocked data**, so the user can see and click the real thing before anyone pays for integrations, backend work, or production code. The mockup is a conversation tool: the goal is fast design iteration, not shippable software.

**Input paths (all optional):** `molten-docs/discovery/<slug>.md` from **mt-discovery**, `molten-docs/design/design.md` from **mt-design**, `molten-docs/brand/brand.md` from **mt-brand**. If no discovery doc exists, gather the essentials directly (see Workflow, step 1).

**Output paths (canonical):**

- Mockup app: depends on the chosen mode (see Mockup Mode). Throwaway: `molten-docs/mockup/<slug>/`. Scaffold: real pages and components in the project's frontend.
- Decisions and learnings (both modes): `molten-docs/mockup/<slug>.md`

**Next skill:** **mt-spec** (carry forward the approved screens, flows, and the implied data contract).

**How it differs from mt-prototype:** **mt-prototype** answers one risky question, which may be technical. **mt-mockup** shows the whole user experience of a feature across screens, states, and flows, with realistic fake data, so the user can judge and reshape it. If the real risk is feasibility, use **mt-prototype** instead.

## Mockup Mode

Ask this first, before building anything, unless the user already said which they want. Ask as a numbered multiple-choice question:

**"Should this mockup be throwaway or scaffold real pages?"**

- a. **Throwaway** — a standalone mockup in `molten-docs/mockup/<slug>/`, isolated from the codebase. Fastest, zero risk to the app, deleted or archived once the design is settled. Best for early exploration and unfamiliar ideas.
- b. **Scaffold real pages** — build the pages, routes, and components in the project's actual frontend, using its stack, design system, and conventions, with mocked data behind a fake API layer. Costs more up front, but the approved screens become the real UI and only the data layer is swapped in later. Best when the stack is established and the design is fairly clear.
- c. **Choose for me** — recommend one with a one-sentence reason, based on whether a frontend already exists and how settled the design is.

If there is no existing frontend, scaffold mode is not possible; say so and use throwaway.

| | Throwaway | Scaffold real pages |
| --- | --- | --- |
| Location | `molten-docs/mockup/<slug>/` | Project's own routes and components |
| Stack | Zero-build static (default) | Project's existing stack, no new dependencies unless approved |
| Data | `data/*.js` fixtures + `api.js` | `mocks/<slug>/` fixtures + a mock implementation of the real data-access module |
| Fate of the code | Discarded; keep screens, flows, copy, data shape | Kept; only the mock data layer is replaced |
| Production risk | None | Must be flagged and removable (see Scaffold rules) |

### Scaffold rules

- Work on a branch, not directly on the default branch, and tell the user the branch name.
- Follow existing patterns: routing, component library, styling, state management, naming, and lint/type settings. Reuse existing components before writing new ones.
- Write UI as production-quality components. They must call a data-access module (hooks, services, or API client) that has a clear interface; only the implementation behind it is mocked.
- Keep all fixtures and the mock implementation together in one folder (e.g. `mocks/<slug>/`) so replacing them is a single, obvious step. No fixture imports inside UI components.
- Gate the mock behind one switch (a constant, env flag, or provider) so the real implementation can be dropped in without touching the screens. Never enable mocks in production builds.
- Keep the visible "Mockup — sample data" indicator in one removable component.
- Do not add backend routes, database schema, migrations, auth changes, or third-party services, even as stubs that look real.
- List every file added or changed in the decisions doc under "What to replace for production".

## Operating Rules

- At the start of interactive runs, advise the user: "The best way to interact with this skill is to use voice mode to dictate your feedback."
- **Frontend only.** No backend, database, auth, payments, email, third-party SDKs, or real network calls. Never ask for or store API keys or credentials.
- **All data is mocked.** Data lives in local JSON or JS fixtures. Use realistic, domain-appropriate names, numbers, dates, and copy. Never use real people's personal data, and avoid lorem ipsum.
- **Put a fake API layer between UI and data.** Screens must call small async functions (`api.listOrders()`, `api.createOrder(input)`) that read and write the fixtures, with a short artificial delay. Screens must never import fixtures directly. This keeps the swap to a real backend a one-file change and makes loading and error states testable.
- **Show every state, not just the happy path.** For each screen, cover populated, empty, loading, error, and (where relevant) permission-denied, long-content, and first-run states. Provide a visible way to switch scenarios (see Scenario switcher).
- **Make it clickable.** Navigation, forms, filters, modals, and primary actions must work against the fake API. Mutations update in-memory state; resetting the page restores the fixtures.
- **Mark it as a mockup.** Show a small, unobtrusive "Mockup — sample data" indicator so nobody mistakes it for the product.
- **Cheapest stack that works.** In throwaway mode, default to a zero-build static app (HTML, CSS, vanilla JS or ES modules) that opens by double-clicking `index.html`. In scaffold mode, use the project's own stack and still keep everything behind the fake API layer.
- If `molten-docs/design/design.md` exists, use its tokens, type, and components. Otherwise pick a neutral, clean style and say so; do not spend the session on visual polish.
- **Throwaway mode:** keep mockup code isolated from production code and never merge it in as-is. Its lasting outputs are the screens, flows, copy, and data shape, not the code.
- **Scaffold mode:** follow the Scaffold rules so the mock data layer can be replaced without rewriting the screens.
- Ask every question as plain numbered text in chat; for finite choices, list lettered options under the question (1a, 1b, 1c). Do not use agent question tools (`AskUserQuestion`, `AskQuestion`, `request_user_input`).

## Workflow

1. **Frame it.** Read any discovery, design, and brand docs. Then confirm with the user, as numbered questions, only what you cannot infer:
   1. Who is the primary user and what job are they doing?
   2. What are the 2–4 key flows to mock (e.g. "create a project", "review an invite")?
   3. What surface: web, mobile, or desktop (affects layout and interaction patterns)?
   4. Throwaway or scaffold real pages (see Mockup Mode)? In throwaway mode, zero-build static is the default stack.
2. **Plan the screens.** List screens, the flows that connect them, and the entities and fields they show. Share this as a short outline and get a go-ahead before building. Keep scope tight; mock the flows the user named, not the whole product.
3. **Design the data.** Write the fixtures and the fake API function signatures first. These become the implied data contract for **mt-spec**.
4. **Build the first pass.** Implement the screens and flows end to end, all states included. Prefer breadth over polish.
5. **Show it.** Tell the user exactly how to open it (see Running the mockup). If a browser tool is available, open it and check each flow and state yourself, and fix anything broken before handing it over.
6. **Iterate.** Collect feedback as numbered points, apply changes, and re-show. Each round, summarise what changed. Stop when the user says the experience feels right or further changes would be copy-level only.
7. **Capture decisions.** Write the decisions doc and point the user to it and to the next step (**mt-spec**). In scaffold mode, also state the branch and what must be replaced to go to production.

## Suggested structure (throwaway, zero-build default)

```
molten-docs/mockup/<slug>/
  index.html          # shell, nav, mockup banner, scenario switcher
  styles.css          # tokens from design.md (or neutral defaults)
  app.js              # router + screen rendering
  api.js              # fake API: async functions, artificial delay, in-memory writes
  data/
    <entity>.js       # fixtures, e.g. `export const orders = [...]`
  README.md           # how to open, scenarios, reset
```

Use ES modules and plain `.js` fixtures (not `fetch('x.json')`), because browsers block local JSON fetches on `file://`. If the user wants real `.json` files, serve the folder with `npx serve molten-docs/mockup/<slug>` instead and say so.

## Fake API layer

- Every function is `async`, waits roughly 200–600 ms, and returns plain data shaped like the real API would.
- Reads return copies of fixtures; writes mutate an in-memory store so flows feel real.
- Support a failure switch (`?scenario=error`, or the scenario switcher) so error states can be seen on demand.
- Name functions after user intent, not storage (`api.inviteMember`, not `api.insertRow`).

## Scenario switcher

Include a small, collapsible panel (or query-string parameters) that lets the user flip between scenarios without editing code:

- **Populated** (default, realistic volume)
- **Empty / first run**
- **Loading** (slow responses)
- **Error** (failed requests)
- **Edge cases** (very long text, many items, missing optional fields)

Add feature-specific scenarios when they matter (e.g. trial expired, over quota, read-only role).

## Running the mockup

Scaffold mode: use the project's normal dev command and give the user the route(s) to visit. The rest of this section is for throwaway mode.

- Zero-build: open `molten-docs/mockup/<slug>/index.html` in a browser.
- Served: `npx serve molten-docs/mockup/<slug>` (only if JSON files or routing require it).
- Reset: reload the page; in-memory changes are discarded.
- Include these instructions in the mockup's `README.md` and repeat them to the user.

## Output template (decisions doc)

```markdown
---
feature: <name>
slug: <slug>
created: <YYYY-MM-DD>
discovery: molten-docs/discovery/<slug>.md | null
design: molten-docs/design/design.md | null
mode: throwaway | scaffold
mockup_location: molten-docs/mockup/<slug>/ | <routes/folders in the project>
branch: <branch name> | null
molten_next_skill: mt-spec
---

# Mockup — <name>

## Goal (user, job to be done, flows mocked)
## How to run it
## Screens and flows (list, with the scenario that shows each state)
## Decisions made (what the user liked, changed, or rejected, and why)
## Implied data contract (entities, fields, and fake API functions the real backend must provide)
## Copy and content notes
## What to replace for production (scaffold mode: files, mock switch, fixtures folder; throwaway mode: n/a)
## Out of scope / deliberately faked (auth, payments, real-time, integrations, etc.)
## Open questions for the spec
```

## Done checklist

- [ ] Mode (throwaway or scaffold), flows, and surface confirmed before building
- [ ] Frontend only: no real network calls, secrets, or personal data
- [ ] UI reads and writes only through the fake API layer
- [ ] Populated, empty, loading, and error states visible via the scenario switcher
- [ ] Mockup labelled as sample data; throwaway code isolated, or scaffold code on a branch with the mock layer behind one switch and one folder
- [ ] User has opened and clicked through it, and feedback has been applied
- [ ] `molten-docs/mockup/<slug>.md` written, including the implied data contract
