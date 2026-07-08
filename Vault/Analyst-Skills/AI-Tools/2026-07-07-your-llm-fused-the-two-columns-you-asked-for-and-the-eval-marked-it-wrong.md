---
title: Your LLM fused the two columns you asked for — and the eval marked it wrong
date: '2026-07-07'
source: https://dev.to/omer_hochman/your-llm-fused-the-two-columns-you-asked-for-and-the-eval-marked-it-wrong-5gge
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** You ask a text-to-SQL model to "list the members' names". The benchmark's gold query returns first_name, last_name — two columns. The model returns one: a helpfully assembled full name. Read side by side, the model's ans…

## What’s new and why it matters
You ask a text-to-SQL model to "list the members' names". The benchmark's gold query returns first_name, last_name — two columns. The model returns one: a helpfully assembled full name. Read side by side, the model's answer is arguably the better one. The scorer marks it wrong, every single time, and your engine number reads lower than the engine is. -- gold: two columns SELECT first_name , last_name FROM member WHERE ...; -- model: one column, same information SELECT first_name || ' ' || last_name FROM member WHERE ...; Why every execution-accuracy scorer does this Execution accuracy — the me…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/omer_hochman/your-llm-fused-the-two-columns-you-asked-for-and-the-eval-marked-it-wrong-5gge

## Related notes
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
