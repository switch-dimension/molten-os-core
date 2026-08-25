---
name: molten-search
description: Molten OS Core — routes search and research queries to Cursor WebSearch, last30days, agent-reach, or parallel-cli web search. Use when the user asks to search, look up, research, google, find recent discussion, check a social platform, fetch current web info, or mentions molten-search.
metadata:
  author: switch-dimension
  version: "1.0.0"
  molten-suite: molten-os
  molten-category: utility
  molten-tier: core
---

# Molten Search

Router only. Classify the query, name the route in one sentence, then hand off. Do not invent a search workflow of your own.

## Operating Rules

1. Honor an explicit backend name over inference.
2. Pick **one** primary route. Add a second only when the user clearly needs two kinds of evidence (for example recent social sentiment **and** a cited web brief).
3. After routing, **read the target `SKILL.md` and follow it**. Do not summarize or improvise last30days, agent-reach, or parallel-web-search.
4. Local codebase lookup is not this skill. Use Grep, Glob, and Read instead.
5. Do not post, comment, like, or otherwise write to platforms. Agent-reach is fetch-only here.

## Routes

| Route | When | How |
| --- | --- | --- |
| **cursor** | Quick facts, definitions, docs, a specific public URL, "just search it", simple current-event lookup | Cursor `WebSearch` / `WebFetch`. No extra skill file. |
| **last30days** | What people are saying *recently*: last 30 days, sentiment, Reddit / X / YouTube / TikTok / HN pulse, "what's the reaction" | Read and follow the `last30days` skill |
| **agent-reach** | A named platform, a platform URL, Chinese-web / 全网调研, GitHub code search, YouTube/Bilibili transcripts, RSS, LinkedIn | Read and follow the `agent-reach` skill |
| **parallel** | Broader web research that needs current sources and citations; default when the query is research-shaped but not social-recency or platform-specific | Read and follow the `parallel-web-search` skill |

## Classification

Apply in this order. Stop at the first match.

### 1. Explicit override

User named a backend or close synonym:

- `cursor`, `websearch`, `just google`, `quick search` → **cursor**
- `last30days`, `last 30 days`, `what people are saying`, `recent discussion` → **last30days**
- `agent-reach`, `agent reach`, or a platform from its list (小红书/xhs, Twitter/X, B站/bilibili, Reddit, Facebook, Instagram, V2EX, LinkedIn, YouTube, GitHub code search, 小宇宙, 雪球) → **agent-reach**
- `parallel`, `parallel-cli`, `parallel web search` → **parallel**

### 2. Intent

**last30days** if the goal is recent *community* evidence: reaction, sentiment, discourse, "what are people saying", last month / last 30 days, social-platform pulse across Reddit/X/YouTube/TikTok/HN.

**agent-reach** if the goal is a **specific platform or URL** (including 调研/全网调研 and the platforms in that skill's description). Prefer this over last30days when they name one platform rather than a 30-day multi-source pulse.

**cursor** if the goal is cheap and fast: a fact, a definition, official docs, "what is X", "open this URL", a yes/no current check.

**parallel** for everything else that still needs the live web: compare tools, market/context brief, "research X", current info with citations, multi-source synthesis that is not a 30-day social pulse.

### 3. Default

If still ambiguous, use **parallel**.

## Handoff

1. State the route: `Routing to last30days` (or cursor / agent-reach / parallel).
2. **cursor:** run `WebSearch` and/or `WebFetch`. Cite sources. Stop.
3. **last30days / agent-reach / parallel:** Resolve that skill's `SKILL.md`, read it immediately, then execute it as if the user had invoked it directly. Pass the user's query through unchanged unless the target skill requires a rewritten objective.

If `parallel-cli` is missing when the parallel route is chosen, resolve `parallel-cli-setup` and follow it, then continue.

Deep / exhaustive / comprehensive report requests are **not** parallel-web-search. Resolve and follow `parallel-deep-research` instead.

## Resolve a backend skill

Look for `<name>/SKILL.md` in this order and use the first hit:

1. `.agents/skills/<name>/`
2. `.cursor/skills/<name>/`
3. `.claude/skills/<name>/`
4. `skills/<name>/`
5. `~/.agents/skills/<name>/`
6. `~/.cursor/skills/<name>/`
7. `~/.claude/skills/<name>/`
8. `~/.codex/skills/<name>/`

If the chosen backend is not installed, say so, keep the cursor route as a fallback for simple lookups, and tell the user how to install the missing skill (`last30days`, `agent-reach`, or `parallel-web-search`). Do not improvise that backend's workflow.

## Examples

| User | Route |
| --- | --- |
| "What is Zod?" | cursor |
| "Look up the Next.js caching docs" | cursor |
| "What's the reaction to the Claude release in the last 30 days?" | last30days |
| "What are people saying about Cursor vs Claude Code?" | last30days |
| "Search Twitter for comments on the GPT-5 launch" | agent-reach |
| "帮我调研一下小红书上大家怎么评价这个产品" | agent-reach |
| "Search GitHub for repos that do local-first sync" | agent-reach |
| "Research current AI video tools and cite sources" | parallel |
| "Compare v0, Bolt, and Lovable for shipping Next apps" | parallel |
| "last30days nvidia earnings reaction" | last30days (explicit) |
| "Just google the release date, don't do a whole research pass" | cursor (explicit) |
