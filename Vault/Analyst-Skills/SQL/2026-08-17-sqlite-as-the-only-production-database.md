---
title: SQLite as the only production database
date: '2026-08-17'
source: https://dev.to/floriang_dxb/sqlite-as-the-only-production-database-4gh4
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-04-23-from-0-to-100-github-stars-with-a-python-cli-spoiler-its-not-as-easy-as-they-say]]'
- '[[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]'
- '[[2026-06-04-redb-inside-part-1-the-13-tables-the-whole-engine-runs-on-with-the-actual-sql-and-why-its-not-eav]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
status: unread
---

> **TL;DR:** We built a local-first FF&E procurement tool on one Linux box. One writer at a time, 80–400 line items, money as integer cents. The production database is SQLite. There is no Postgres process. That is not a taste questio…

## What’s new and why it matters
We built a local-first FF&E procurement tool on one Linux box. One writer at a time, 80–400 line items, money as integer cents. The production database is SQLite. There is no Postgres process. That is not a taste question. For this profile the backup is a file copy and the restore case is one file. The expensive default is a second unit for PostgreSQL. I wrote the decision down as a short paid essay, from code that already exists. No invented GitHub stars, no invented incident. Essay ($12): https://gamefanatic2.gumroad.com/l/bzqtv The money helper we extracted is a one-file CLI: parse vendor s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/floriang_dxb/sqlite-as-the-only-production-database-4gh4

## Related notes
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-04-23-from-0-to-100-github-stars-with-a-python-cli-spoiler-its-not-as-easy-as-they-say]]
- [[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]
- [[2026-06-04-redb-inside-part-1-the-13-tables-the-whole-engine-runs-on-with-the-actual-sql-and-why-its-not-eav]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
