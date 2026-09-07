---
title: 'When SQL Has Nothing to Say: Understanding NULLs'
date: '2026-09-06'
source: https://dev.to/rose_odiwuor/when-sql-has-nothing-to-say-understanding-nulls-4i2i
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-27-sql-select-null-a-complete-guide-to-handling-missing-data-in-sql]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** NULL in SQL carry different meanings; missing value unknown value no value inapplicable data customer_id customer_name contact 101 Alice 0712345678 102 Brian NULL 103 Carol 0798765432 You shouldn't interpret NULL as; 0 (…

## What’s new and why it matters
NULL in SQL carry different meanings; missing value unknown value no value inapplicable data customer_id customer_name contact 101 Alice 0712345678 102 Brian NULL 103 Carol 0798765432 You shouldn't interpret NULL as; 0 (zero) '' (empty string) blank space Using IS NULL, IS NOT NULL to find NULLs Since NULL is not equal to zero or an empty string, you cannot use = to compare it; you must use IS NULL or IS NOT NULL . select * from customers where contact = NULL ; This doesn't return 'Brian' = null returns 0 rows, always! SQL uses three-valued logic : TRUE , FALSE and UNKNOWN . The comparison whe…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rose_odiwuor/when-sql-has-nothing-to-say-understanding-nulls-4i2i

## Related notes
- [[2026-07-27-sql-select-null-a-complete-guide-to-handling-missing-data-in-sql]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
