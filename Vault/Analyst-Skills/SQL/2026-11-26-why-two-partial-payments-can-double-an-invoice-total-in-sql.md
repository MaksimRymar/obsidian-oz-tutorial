---
title: Why two partial payments can double an invoice total in SQL
date: '2026-11-26'
source: https://dev.to/stimul-education/why-two-partial-payments-can-double-an-invoice-total-in-sql-32k7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-11-25-how-to-find-duplicate-rows-in-mysql-before-they-break-your-app]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** A supplier invoice has two lines, one for 80 and one for 40. Accounts payable has recorded two payments against it, first 30 and then 20. The supplier is still owed 70. Suppose your ERP report shows an outstanding balanc…

## What’s new and why it matters
A supplier invoice has two lines, one for 80 and one for 40. Accounts payable has recorded two payments against it, first 30 and then 20. The supplier is still owed 70. Suppose your ERP report shows an outstanding balance of 140. Before you inspect the payment postings, count the rows going into your sums. Here is the entire example. Each amount is in the same currency, and each payment row records the amount applied to this invoice. Table Invoice ID Row ID Amount invoice_lines 101 L1 80 invoice_lines 101 L2 40 payments 101 P1 30 payments 101 P2 20 Joining the two tables on invoice ID gives ea…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/stimul-education/why-two-partial-payments-can-double-an-invoice-total-in-sql-32k7

## Related notes
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-11-25-how-to-find-duplicate-rows-in-mysql-before-they-break-your-app]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-03-08-understanding-group-by-in-sql]]
