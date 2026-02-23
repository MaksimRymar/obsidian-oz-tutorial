---
title: 8 SQL Queries That Catch 90% of Interview Candidates Off Guard
date: '2026-02-23'
source: https://dev.to/maxxmini/8-sql-queries-that-catch-90-of-interview-candidates-off-guard-4fae
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]'
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-02-21-sql-masterclass]]'
- '[[2026-02-22-building-an-ai-powered-natural-language-sql-interface-an-mvp-journey]]'
status: unread
---

> **TL;DR:** You know SELECT, JOIN, GROUP BY. You can write a basic subquery. But these 8 SQL patterns are where interviews separate the juniors from the seniors. I compiled 40 real SQL interview questions from FAANG+ companies. Here…

## What’s new and why it matters
You know SELECT, JOIN, GROUP BY. You can write a basic subquery. But these 8 SQL patterns are where interviews separate the juniors from the seniors. I compiled 40 real SQL interview questions from FAANG+ companies. Here are 8 that trip up even experienced developers — with explanations of why they work the way they do. 1. Running Totals with Window Functions The trap: Using a correlated subquery instead of a window function. -- ❌ Slow (O(n²) correlated subquery) SELECT date , amount , ( SELECT SUM ( amount ) FROM transactions t2 WHERE t2 . date <= t1 . date ) as running_total FROM transaction…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/maxxmini/8-sql-queries-that-catch-90-of-interview-candidates-off-guard-4fae

## Related notes
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-02-21-sql-masterclass]]
- [[2026-02-22-building-an-ai-powered-natural-language-sql-interface-an-mvp-journey]]
