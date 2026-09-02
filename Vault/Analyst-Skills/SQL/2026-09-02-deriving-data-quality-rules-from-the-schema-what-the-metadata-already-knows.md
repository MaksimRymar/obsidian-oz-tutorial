---
title: Deriving Data Quality Rules from the Schema — What the Metadata Already Knows
date: '2026-09-02'
source: https://dev.to/marcus1968/deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows-23p2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-16-checking-data-quality-with-sql-a-configurable-framework-for-spotting-bad-data-generically]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** The rule " country_code is mandatory" lives in your database twice: once as NOT NULL in the target table's schema, and once as a hand-typed row in the check configuration. On the next ALTER TABLE , only one of the two pl…

## What’s new and why it matters
The rule " country_code is mandatory" lives in your database twice: once as NOT NULL in the target table's schema, and once as a hand-typed row in the check configuration. On the next ALTER TABLE , only one of the two places changes, and the check silently goes wrong. With derived data quality rules you no longer type that repetition: the metadata already knows which columns are mandatory, which keys must be unique and which value ranges the types allow. And by pinning the derived state at deployment time, you detect schema drift instead of suffering it. The essentials up front: NOT NULL, key…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/marcus1968/deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows-23p2

## Related notes
- [[2026-07-16-checking-data-quality-with-sql-a-configurable-framework-for-spotting-bad-data-generically]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
