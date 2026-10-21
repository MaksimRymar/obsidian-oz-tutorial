---
title: Same SQL, Fast for One Value, Slow for Another
date: '2026-10-21'
source: https://dev.to/uptimearchitect/same-sql-fast-for-one-value-slow-for-another-22he
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** The order-history screen is fast for every customer except one. Or it's fast all morning and crawls all afternoon. Or it was fine for months and became slow the night after a restart, with nobody deploying anything. You…

## What’s new and why it matters
The order-history screen is fast for every customer except one. Or it's fast all morning and crawls all afternoon. Or it was fine for months and became slow the night after a restart, with nobody deploying anything. You pull the statement and run it yourself with the problem value, and it comes back instantly. The SQL is identical. The data hasn't changed. The plan in the execution history is the same plan it always uses. That last sentence is the clue. The statement uses a bind variable , which is the right thing to do, and the cursor for it holds one plan . That plan was chosen for whichever…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/uptimearchitect/same-sql-fast-for-one-value-slow-for-another-22he

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
