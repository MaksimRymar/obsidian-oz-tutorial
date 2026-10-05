---
title: The ALTER TABLE statement conflicted with the FOREIGN KEY constraint
date: '2026-10-05'
source: https://dev.to/woodfiresam/the-alter-table-statement-conflicted-with-the-foreign-key-constraint-4h3b
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
status: unread
---

> **TL;DR:** You add a foreign key to a table that has been live for years, and SQL Server refuses: ALTER TABLE dbo . SalesOrder ADD CONSTRAINT FK_SalesOrder_Customer FOREIGN KEY ( CustomerId ) REFERENCES dbo . Customer ( CustomerId…

## What’s new and why it matters
You add a foreign key to a table that has been live for years, and SQL Server refuses: ALTER TABLE dbo . SalesOrder ADD CONSTRAINT FK_SalesOrder_Customer FOREIGN KEY ( CustomerId ) REFERENCES dbo . Customer ( CustomerId ); Msg 547, Level 16, State 1, Line 1 The ALTER TABLE statement conflicted with the FOREIGN KEY constraint "FK_SalesOrder_Customer". The conflict occurred in database "erd_article_test", table "dbo.Customer", column 'CustomerId'. Read that message carefully, because it sends most people to the wrong table. It names dbo.Customer and column CustomerId — the table being pointed at…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/woodfiresam/the-alter-table-statement-conflicted-with-the-foreign-key-constraint-4h3b

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
