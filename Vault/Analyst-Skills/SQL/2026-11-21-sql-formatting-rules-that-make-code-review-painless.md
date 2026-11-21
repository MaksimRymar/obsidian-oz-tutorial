---
title: SQL Formatting Rules That Make Code Review Painless
date: '2026-11-21'
source: https://dev.to/sanjucse/sql-formatting-rules-that-make-code-review-painless-3f6l
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-13-sql-filtering-the-five-operators-that-let-you-ask-smarter-questions]]'
- '[[2026-03-13-how-to-generate-sql-queries-with-ai-a-complete-guide-for-non-dbas]]'
- '[[2026-10-29-teaching-yourself-sql-when-your-job-is-ops]]'
- '[[2026-07-17-sql-for-real-projects-what-tutorials-dont-teach-you]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
status: unread
---

> **TL;DR:** Formatting SQL is not cosmetic. Unreadable queries hide bugs, bloat diffs and slow reviews. What I enforce on every team: 1. One clause per line SELECT , FROM , WHERE , GROUP BY start on their own lines, with columns ind…

## What’s new and why it matters
Formatting SQL is not cosmetic. Unreadable queries hide bugs, bloat diffs and slow reviews. What I enforce on every team: 1. One clause per line SELECT , FROM , WHERE , GROUP BY start on their own lines, with columns indented beneath. Diffs then show exactly which column changed. 2. Never SELECT * It breaks when columns are added, defeats covering indexes and ships data you don't need. List the columns. 3. Explicit JOIN syntax Write JOIN ... ON instead of comma joins. A forgotten condition in a comma join silently produces a cartesian product. 4. Uppercase keywords, consistent aliases Short me…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sanjucse/sql-formatting-rules-that-make-code-review-painless-3f6l

## Related notes
- [[2026-07-13-sql-filtering-the-five-operators-that-let-you-ask-smarter-questions]]
- [[2026-03-13-how-to-generate-sql-queries-with-ai-a-complete-guide-for-non-dbas]]
- [[2026-10-29-teaching-yourself-sql-when-your-job-is-ops]]
- [[2026-07-17-sql-for-real-projects-what-tutorials-dont-teach-you]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
