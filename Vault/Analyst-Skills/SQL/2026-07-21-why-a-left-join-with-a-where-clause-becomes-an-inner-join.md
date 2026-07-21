---
title: Why a LEFT JOIN With a WHERE Clause Becomes an Inner Join
date: '2026-07-21'
source: https://medium.com/@annxsa/why-a-left-join-with-a-where-clause-becomes-an-inner-join-7b8b3f3fca39?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-13-understanding-locks-in-mysql-why-your-queries-get-stuck-and-how-to-fix-it]]'
- '[[2026-06-19-sql-exists-a-quick-and-easy-guidesql-exists-a-quick-and-easy-guide]]'
- '[[2026-05-15-advanced-sql-joins-for-data-analysts-inner-left-right-full-cross-self-join]]'
- '[[2026-05-21-sql-semi-joins-with-match-checks]]'
- '[[2026-02-22-semi-join-anti-join-the-most-misunderstood-performance-tools-in-sql]]'
- '[[2026-03-08-snowflake-snowpipe-integration-with-amazon-s3-and-sqs-for-automated-data-ingestion-and-export-to-a]]'
status: unread
---

> **TL;DR:** The keyword LEFT stops working when WHERE mentions the right-hand table. 5 test users, 7 rows become 3. Verified in MariaDB. Continue reading on Medium »

## What’s new and why it matters
The keyword LEFT stops working when WHERE mentions the right-hand table. 5 test users, 7 rows become 3. Verified in MariaDB. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@annxsa/why-a-left-join-with-a-where-clause-becomes-an-inner-join-7b8b3f3fca39?source=rss------sql-5

## Related notes
- [[2026-03-13-understanding-locks-in-mysql-why-your-queries-get-stuck-and-how-to-fix-it]]
- [[2026-06-19-sql-exists-a-quick-and-easy-guidesql-exists-a-quick-and-easy-guide]]
- [[2026-05-15-advanced-sql-joins-for-data-analysts-inner-left-right-full-cross-self-join]]
- [[2026-05-21-sql-semi-joins-with-match-checks]]
- [[2026-02-22-semi-join-anti-join-the-most-misunderstood-performance-tools-in-sql]]
- [[2026-03-08-snowflake-snowpipe-integration-with-amazon-s3-and-sqs-for-automated-data-ingestion-and-export-to-a]]
