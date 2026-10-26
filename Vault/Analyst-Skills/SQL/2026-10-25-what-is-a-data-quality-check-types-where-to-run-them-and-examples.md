---
title: What Is a Data Quality Check? Types, Where to Run Them, and Examples
date: '2026-10-25'
source: https://dev.to/bruin-data/what-is-a-data-quality-check-types-where-to-run-them-and-examples-39a9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#presentations'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]'
- '[[2026-09-27-bruin-sql-python-pipelines-in-one-framework-with-built-in-quality-checks]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** This article was first published on the Bruin blog . A data quality check is a rule that runs against a table, or a column in it, and fails when the data breaks the rule. "No nulls in order_id ", "every status is one of…

## What’s new and why it matters
This article was first published on the Bruin blog . A data quality check is a rule that runs against a table, or a column in it, and fails when the data breaks the rule. "No nulls in order_id ", "every status is one of four values", "the newest row is less than six hours old". The check either passes or it fails, and what happens on failure is the design decision that separates a useful check from a dashboard nobody reads: a blocking check stops the pipeline, so bad data never reaches the tables downstream. In Bruin , checks are declared on the column inside the asset that produces it and blo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bruin-data/what-is-a-data-quality-check-types-where-to-run-them-and-examples-39a9

## Related notes
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]
- [[2026-09-27-bruin-sql-python-pipelines-in-one-framework-with-built-in-quality-checks]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
