---
title: 'Building a Chatbot API From Scratch: 13 PRs, a Lot of Broken Things, and a
  Context Window That Actually Works'
date: '2026-03-28'
source: https://dev.to/kris_k/building-a-chatbot-api-from-scratch-13-prs-a-lot-of-broken-things-and-a-context-window-that-3i73
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-07-why-i-rebuilt-my-first-api-from-scratch]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-17-surrealdb-why-joins-are-so-2010-and-how-graphs-change-everything-part-3]]'
- '[[2026-03-15-surrealdb-the-one-size-fits-all-database-for-lazy-developers-part-1]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
status: unread
---

> **TL;DR:** Part 3 of building a retail inventory API and then giving it a brain. In Part 1 I explained why I archived my first API and started over. In Part 2 I restructured it properly, migrated to Supabase, and got to 97% test co…

## What’s new and why it matters
Part 3 of building a retail inventory API and then giving it a brain. In Part 1 I explained why I archived my first API and started over. In Part 2 I restructured it properly, migrated to Supabase, and got to 97% test coverage. The retail API is solid now. Working in production. Tests passing. Architecture I can explain. So I started the next thing: a chatbot API. Same stack, new layer. The goal: a conversational AI service that remembers what you said, manages long conversations intelligently, and eventually connects to the retail inventory data. This is what the last few weeks looked like. W…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kris_k/building-a-chatbot-api-from-scratch-13-prs-a-lot-of-broken-things-and-a-context-window-that-3i73

## Related notes
- [[2026-03-07-why-i-rebuilt-my-first-api-from-scratch]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-17-surrealdb-why-joins-are-so-2010-and-how-graphs-change-everything-part-3]]
- [[2026-03-15-surrealdb-the-one-size-fits-all-database-for-lazy-developers-part-1]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
