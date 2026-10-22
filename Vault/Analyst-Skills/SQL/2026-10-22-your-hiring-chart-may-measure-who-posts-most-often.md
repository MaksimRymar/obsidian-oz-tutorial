---
title: Your hiring chart may measure who posts most often
date: '2026-10-22'
source: https://dev.to/dataspryva/your-hiring-chart-may-measure-who-posts-most-often-4hhk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-04-03-prepared-statements-in-manticore-search]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-09-25-python-data-types-explained-with-practical-examples]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
status: unread
---

> **TL;DR:** Your Friday investigation needs an industry ranking. On Thursday evening, industry.value_counts() looks reassuringly tidy. The uncomfortable question is whether those bars measure hiring demand or visibility in a recent-…

## What’s new and why it matters
Your Friday investigation needs an industry ranking. On Thursday evening, industry.value_counts() looks reassuringly tidy. The uncomfortable question is whether those bars measure hiring demand or visibility in a recent-results feed. Totaljobs serves anonymous searches newest-first. Relevance ordering requires a signed-in session and can't be combined with the filters, so the Actor always returns newest-first results. A capped collection therefore selects through posting recency. Recently posted adverts can enter the collection while older vacancies remain open beyond its reach. A chart can de…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataspryva/your-hiring-chart-may-measure-who-posts-most-often-4hhk

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-04-03-prepared-statements-in-manticore-search]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-09-25-python-data-types-explained-with-practical-examples]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
