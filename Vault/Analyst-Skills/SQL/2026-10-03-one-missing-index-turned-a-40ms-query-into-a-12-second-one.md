---
title: One missing index turned a 40ms query into a 12-second one
date: '2026-10-03'
source: https://dev.to/kamenivanov/one-missing-index-turned-a-40ms-query-into-a-12-second-one-70l
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#career'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
status: unread
---

> **TL;DR:** The query had run fine for two years. It joined orders to customers on a foreign key, filtered by date range, and came back in under 40 milliseconds every time anyone checked it, which nobody had reason to do, because it…

## What’s new and why it matters
The query had run fine for two years. It joined orders to customers on a foreign key, filtered by date range, and came back in under 40 milliseconds every time anyone checked it, which nobody had reason to do, because it wasn't slow. Then a support ticket came in about a report timing out, and the same query, unchanged, was taking 12 seconds. Nothing about the query had changed. What had changed was the table it joined against, which had grown from a few hundred thousand rows to just over 2 million over those two years, gradually enough that no single deploy looked like the moment it broke. Th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kamenivanov/one-missing-index-turned-a-40ms-query-into-a-12-second-one-70l

## Related notes
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
