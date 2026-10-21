---
title: 'Free SQL practice: why SUM(DISTINCT) doesn''t fix inflated payment totals'
date: '2026-10-21'
source: https://dev.to/antony502189max/free-sql-practice-why-sumdistinct-doesnt-fix-inflated-payment-totals-336g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** Free SQL practice, with the full data and solution below. No account, paid course, cloud service, or API key is needed. This is a SQLite exercise using synthetic payment data, with a Python standard-library runner if you…

## What’s new and why it matters
Free SQL practice, with the full data and solution below. No account, paid course, cloud service, or API key is needed. This is a SQLite exercise using synthetic payment data, with a Python standard-library runner if you do not have the SQLite CLI. Two distinct capture events are each worth 1000 USD cents. A report should show 2000 cents. After a join, one query reports 4000; adding DISTINCT reports 1000. Both are wrong. I maintain a free, MIT-licensed fintech data engineering roadmap. This article works through the class of bug explored in its C07 scenario: independent detail tables multiply…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/antony502189max/free-sql-practice-why-sumdistinct-doesnt-fix-inflated-payment-totals-336g

## Related notes
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
