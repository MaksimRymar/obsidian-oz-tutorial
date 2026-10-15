---
title: You Deleted 99% of the Rows. The Full Scan Didn't Get Any Faster.
date: '2026-10-14'
source: https://dev.to/uptimearchitect/you-deleted-99-of-the-rows-the-full-scan-didnt-get-any-faster-40mb
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]'
status: unread
---

> **TL;DR:** The audit table had grown to 200 million rows, so the team finally ran the purge: everything older than 90 days, gone. Ninety-nine percent of the rows deleted, committed, celebrated. The next morning the nightly report t…

## What’s new and why it matters
The audit table had grown to 200 million rows, so the team finally ran the purge: everything older than 90 days, gone. Ninety-nine percent of the rows deleted, committed, celebrated. The next morning the nightly report that full-scans that table ran exactly as long as it always had. Same I/O, same elapsed time, same line in the AWR report. The data was gone. The work wasn't. Nothing is broken here, and the delete did what it was told. The full scan simply doesn't read rows — it reads blocks , every block up to a boundary called the high-water mark , and DELETE never moves that boundary. This p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/uptimearchitect/you-deleted-99-of-the-rows-the-full-scan-didnt-get-any-faster-40mb

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]
