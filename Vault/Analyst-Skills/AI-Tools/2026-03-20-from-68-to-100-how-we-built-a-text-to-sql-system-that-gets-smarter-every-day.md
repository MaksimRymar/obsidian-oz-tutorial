---
title: 'From 68% to ~100%: How We Built a Text-to-SQL System That Gets Smarter Every
  Day'
date: '2026-03-20'
source: https://dev.to/alexchen31337/from-68-to-100-how-we-built-a-text-to-sql-system-that-gets-smarter-every-day-4dlp
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]'
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** A practical guide to moving beyond vanilla LLM prompting toward a self-improving pipeline for production text-to-SQL. The Problem with Vanilla LLM Text-to-SQL We had what seemed like a straightforward problem: let busine…

## What’s new and why it matters
A practical guide to moving beyond vanilla LLM prompting toward a self-improving pipeline for production text-to-SQL. The Problem with Vanilla LLM Text-to-SQL We had what seemed like a straightforward problem: let business users ask natural-language questions about a large domain-specific table — hundreds of millions of rows, 200+ columns, a mandatory date filter on every query — and get back correct SQL. We started where most teams start: a well-crafted prompt, GPT-4, and a schema dump. It worked. Sort of. Our initial accuracy was ~68% . That sounds decent until you realize it means one in th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alexchen31337/from-68-to-100-how-we-built-a-text-to-sql-system-that-gets-smarter-every-day-4dlp

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
