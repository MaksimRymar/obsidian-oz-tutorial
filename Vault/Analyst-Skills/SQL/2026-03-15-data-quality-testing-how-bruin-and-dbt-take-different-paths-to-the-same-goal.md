---
title: 'Data quality testing: how Bruin and dbt take different paths to the same goal'
date: '2026-03-15'
source: https://dev.to/terzioglub/data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal-3b5f
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** If you've built data pipelines for any length of time, you know the drill: the pipeline runs fine, the table gets created, and three days later someone discovers that half the rows have null IDs. The transformation was c…

## What’s new and why it matters
If you've built data pipelines for any length of time, you know the drill: the pipeline runs fine, the table gets created, and three days later someone discovers that half the rows have null IDs. The transformation was correct, the data just wasn't what you assumed. Both Bruin and dbt have built-in systems for catching these problems. They solve the same problem, but in genuinely different ways. dbt treats tests as separate nodes in the DAG. Bruin embeds quality checks directly into asset definitions. Both approaches work, and the trade-offs between them are worth understanding regardless of w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/terzioglub/data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal-3b5f

## Related notes
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
