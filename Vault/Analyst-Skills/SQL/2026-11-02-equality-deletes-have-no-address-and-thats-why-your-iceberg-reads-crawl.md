---
title: Equality deletes have no address, and that's why your Iceberg reads crawl
date: '2026-11-02'
source: https://dev.to/kyien/equality-deletes-have-no-address-and-thats-why-your-iceberg-reads-crawl-15h4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** Here's a failure I've watched happen more than once, and it always looks the same from the outside. A table is fed by CDC off a transactional database. Flink sink, upsert mode, a primary key, commits every minute. The wr…

## What’s new and why it matters
Here's a failure I've watched happen more than once, and it always looks the same from the outside. A table is fed by CDC off a transactional database. Flink sink, upsert mode, a primary key, commits every minute. The write path is healthy: no backpressure, no checkpoint failures, no small-file explosion because compaction runs nightly and does its job. Then over about three weeks, one dashboard query goes from roughly four seconds to roughly half a minute. The query didn't change. Row count is flat. The files look fine — a few hundred megabytes each, well above the target size. Somebody check…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kyien/equality-deletes-have-no-address-and-thats-why-your-iceberg-reads-crawl-15h4

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
