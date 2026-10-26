---
title: One Annotation Cut Our SQL Write Amplification by 90%
date: '2026-10-25'
source: https://dev.to/algopro/one-annotation-cut-our-sql-write-amplification-by-90-35jp
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-05-29-part-11-indexes-and-performance]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** I added one annotation to a Java entity class. Two lines of code. The PR diff was so small that our reviewer almost skipped it. That change cut the bytes written to our SQL transaction log on every UPDATE by roughly 90%,…

## What’s new and why it matters
I added one annotation to a Java entity class. Two lines of code. The PR diff was so small that our reviewer almost skipped it. That change cut the bytes written to our SQL transaction log on every UPDATE by roughly 90%, eliminated unnecessary index maintenance on 17 nonclustered indexes, and brought our peak database wait times from minutes down to near zero during the busiest job of the day. Here's what happened, why it happened, and how you can check whether the same thing is quietly hurting your service right now. The setup We run a Spring Boot service backed by Azure SQL (SQL Server). One…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/algopro/one-annotation-cut-our-sql-write-amplification-by-90-35jp

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-05-29-part-11-indexes-and-performance]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
