---
title: The Empty SMALLINT Column That Led Me to Nine More Missing Types
date: '2026-10-05'
source: https://dev.to/caiderek/the-empty-smallint-column-that-led-me-to-nine-more-missing-types-22p4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** I had written a stock market analysis program before. One of its tables had a SMALLINT column. When I tested LogCarver against that table, every row through it came back empty. After finding that, I tested a batch of col…

## What’s new and why it matters
I had written a stock market analysis program before. One of its tables had a SMALLINT column. When I tested LogCarver against that table, every row through it came back empty. After finding that, I tested a batch of column types my own program rarely uses, plus a few types I had never specifically tested before. Turned out it wasn't just one missing type. Ten fixed-length types were missing: tinyint, smallint, bit, uniqueidentifier, money, smallmoney, datetime, smalldatetime, float, real. Any table using one of these lost that column's data, silently, no error, just nothing there. Adding them…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/caiderek/the-empty-smallint-column-that-led-me-to-nine-more-missing-types-22p4

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
