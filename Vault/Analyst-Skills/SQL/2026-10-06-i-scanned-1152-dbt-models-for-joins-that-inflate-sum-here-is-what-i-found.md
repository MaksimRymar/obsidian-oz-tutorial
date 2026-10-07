---
title: I scanned 1,152 dbt models for joins that inflate SUM. Here is what I found.
date: '2026-10-06'
source: https://dev.to/rohit9007/i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found-1ea
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-09-20-window-functions-vs-aggregate-functions-in-sql-a-beginner-friendly-guide]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** There is a bug in analytics SQL that never throws an error. select o . customer_id , sum ( o . amount ) as revenue from orders o left join payments p on p . order_id = o . order_id group by o . customer_id Customer 1 has…

## What’s new and why it matters
There is a bug in analytics SQL that never throws an error. select o . customer_id , sum ( o . amount ) as revenue from orders o left join payments p on p . order_id = o . order_id group by o . customer_id Customer 1 has two orders worth ₹150 in total. They paid in five instalments. After the join, each order appears once per payment, and SUM adds it every time. The query says ₹400. This is called a fan out, or a fan trap. Its cousin is the chasm trap: one table joined to two one to many tables at once, where the two multiply each other. BI tools have some protection against it inside their se…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rohit9007/i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found-1ea

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-09-20-window-functions-vs-aggregate-functions-in-sql-a-beginner-friendly-guide]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
