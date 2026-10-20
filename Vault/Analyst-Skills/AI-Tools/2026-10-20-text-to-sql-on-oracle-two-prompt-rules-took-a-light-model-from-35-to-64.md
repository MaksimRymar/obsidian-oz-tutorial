---
title: 'Text-to-SQL on Oracle: two prompt rules took a light model from 35% to 64%'
date: '2026-10-20'
source: https://dev.to/ashish_sinha_5241c7673d93/text-to-sql-on-oracle-two-prompt-rules-took-a-light-model-from-35-to-64-3mpc
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
status: unread
---

> **TL;DR:** UniQL is a new benchmark that translates BIRD's 1,534 text-to-SQL questions into 16 SQL dialects. Its Oracle column is hard. The best published result is 49.61% (Claude Sonnet 4.5), and Gemini 2.5 Pro scores 26.14%. I ra…

## What’s new and why it matters
UniQL is a new benchmark that translates BIRD's 1,534 text-to-SQL questions into 16 SQL dialects. Its Oracle column is hard. The best published result is 49.61% (Claude Sonnet 4.5), and Gemini 2.5 Pro scores 26.14%. I ran schemagate on it with a light model, Gemini 2.5 Flash . The scores below come from UniQL's own evaluator, on Oracle Free 23ai. UniQL Oracle, 1,534 questions First try With error repair schemagate + Gemini 2.5 Flash 35.0 69.9 + two Oracle rules in the prompt 64.5 67.6 Best published (Claude Sonnet 4.5, single try) 49.6 — The first run looked good for the wrong reason. 69.9% wa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/text-to-sql-on-oracle-two-prompt-rules-took-a-light-model-from-35-to-64-3mpc

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
