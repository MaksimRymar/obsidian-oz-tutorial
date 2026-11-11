---
title: Your UNIQUE constraint in PostgreSQL lets duplicates through. Here is how to
  find every one
date: '2026-11-11'
source: https://dev.to/_nedomolkov_ivan/your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one-99e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-29-one-long-select-one-alter-table-and-every-query-behind-them]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
status: unread
---

> **TL;DR:** The table has a UNIQUE constraint, and identical rows sit in it in pairs. If at least one column of the key is nullable, this is expected behaviour: following the SQL standard, PostgreSQL treats two NULL s as distinct, s…

## What’s new and why it matters
The table has a UNIQUE constraint, and identical rows sit in it in pairs. If at least one column of the key is nullable, this is expected behaviour: following the SQL standard, PostgreSQL treats two NULL s as distinct, so a row with an empty field never matches any other row, not even its own copy. No error, nothing in the log, the constraint is in place. We hit this in a service table next to a 1C:Enterprise database, caught by the final test of a migration. Below is the procedure we now run on every such table: find the keys, measure how many rows are actually protected, decide what the data…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_nedomolkov_ivan/your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one-99e

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-29-one-long-select-one-alter-table-and-every-query-behind-them]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
