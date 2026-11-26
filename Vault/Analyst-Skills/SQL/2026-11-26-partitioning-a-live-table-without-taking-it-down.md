---
title: Partitioning a Live Table Without Taking It Down
date: '2026-11-26'
source: https://blog.devgenius.io/partitioning-a-live-table-without-taking-it-down-6106181ba623?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-11-19-how-to-delete-or-update-millions-of-rows-in-sql-server-safely-batching]]'
- '[[2026-08-02-9104-rows-in-5000-out-the-silent-cap-that-made-my-dashboard-lie]]'
- '[[2026-10-13-using-claude-to-write-a-safe-bulk-delete-for-a-large-postgres-table]]'
- '[[2026-10-13-postgres-18-can-enforce-no-two-bookings-overlap-for-you]]'
- '[[2026-07-26-advanced-sql-server-series-part-10-table-partitioning-splitting-billions-of-rows-without]]'
- '[[2026-02-25-partition-and-organize-data-for-performance]]'
status: unread
---

> **TL;DR:** Copying 20 million rows into partitions froze writes for 49 seconds. Attaching the live table as one partition held its lock for 14 ms… Continue reading on Dev Genius »

## What’s new and why it matters
Copying 20 million rows into partitions froze writes for 49 seconds. Attaching the live table as one partition held its lock for 14 ms… Continue reading on Dev Genius »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://blog.devgenius.io/partitioning-a-live-table-without-taking-it-down-6106181ba623?source=rss------sql-5

## Related notes
- [[2026-11-19-how-to-delete-or-update-millions-of-rows-in-sql-server-safely-batching]]
- [[2026-08-02-9104-rows-in-5000-out-the-silent-cap-that-made-my-dashboard-lie]]
- [[2026-10-13-using-claude-to-write-a-safe-bulk-delete-for-a-large-postgres-table]]
- [[2026-10-13-postgres-18-can-enforce-no-two-bookings-overlap-for-you]]
- [[2026-07-26-advanced-sql-server-series-part-10-table-partitioning-splitting-billions-of-rows-without]]
- [[2026-02-25-partition-and-organize-data-for-performance]]
