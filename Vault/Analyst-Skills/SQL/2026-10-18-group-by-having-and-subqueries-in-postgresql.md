---
title: GROUP BY, HAVING, and Subqueries in PostgreSQL
date: '2026-10-18'
source: https://dev.to/im_nishant/group-by-having-and-subqueries-in-postgresql-4mp2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]'
- '[[2026-10-12-where-vs-having-in-sql-a-simple-way-to-understand-the-difference]]'
- '[[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-09-28-group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes]]'
status: unread
---

> **TL;DR:** There's a point in almost every project where you stop just retrieving rows and start actually asking questions — how many venues per city, which cities have more than a handful, which venues are above average latitude.…

## What’s new and why it matters
There's a point in almost every project where you stop just retrieving rows and start actually asking questions — how many venues per city, which cities have more than a handful, which venues are above average latitude. That's the shift this article is about. The syntax for aggregation isn't complicated on its own. What takes a bit longer to get comfortable with is the order things actually happen in, especially once WHERE and HAVING are both in the same query and doing different jobs. Where it gets confusing Say you want cities with more than three venues. The instinct, especially early on, i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/im_nishant/group-by-having-and-subqueries-in-postgresql-4mp2

## Related notes
- [[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]
- [[2026-10-12-where-vs-having-in-sql-a-simple-way-to-understand-the-difference]]
- [[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-09-28-group-by-aggregate-functions-explained-the-where-vs-having-mistake-almost-everyone-makes]]
