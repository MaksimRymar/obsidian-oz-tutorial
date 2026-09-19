---
title: A Nullable Column Cost Me Five Years of Branches
date: '2026-09-19'
source: https://dev.to/_66d02d0cc1ece7d1137c5f/a-nullable-column-cost-me-five-years-of-branches-3mbn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-18-rabbitmq-vs-kafka-for-data-engineering-queues-vs-logs-when-each-wins]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-13-recursive-ctes-how-sql-secretly-learned-to-loop]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-07-12-sql-null-semantics-three-valued-logic-the-traps-that-break-every-report]]'
status: unread
---

> **TL;DR:** A CSV export came back with blank locale cells for accounts that showed a locale in the UI. The export did SELECT * and wrote each column straight to a row. accounts.locale was NULL for some of them because a backfill jo…

## What’s new and why it matters
A CSV export came back with blank locale cells for accounts that showed a locale in the UI. The export did SELECT * and wrote each column straight to a row. accounts.locale was NULL for some of them because a backfill job never finished. That was the visible cost. The invisible one was that the column had been nullable for years, so every reader in the system had grown its own opinion about what NULL meant. A nullable column is a type change for everyone I added it the cheap way: ALTER TABLE accounts ADD COLUMN locale text ; No default, no backfill, no long lock. locale was text for about a we…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_66d02d0cc1ece7d1137c5f/a-nullable-column-cost-me-five-years-of-branches-3mbn

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-18-rabbitmq-vs-kafka-for-data-engineering-queues-vs-logs-when-each-wins]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-13-recursive-ctes-how-sql-secretly-learned-to-loop]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-07-12-sql-null-semantics-three-valued-logic-the-traps-that-break-every-report]]
