---
title: 'MAX()+1: The Invoice Number That Showed Up Twice'
date: '2026-10-03'
source: https://dev.to/hossam_assadallah_842151a/max1-the-invoice-number-that-showed-up-twice-3lb1
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-06-29-the-customerid-that-isnt-a-customer]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
status: unread
---

> **TL;DR:** 3 Oct 2026 · @hossam Assadallah Two invoices, one number Friday, 2 PM, and the restaurant is packed. Two cashiers hit "Save" at almost the same moment. Both get invoice number 10452. At month end, the accountant finds th…

## What’s new and why it matters
3 Oct 2026 · @hossam Assadallah Two invoices, one number Friday, 2 PM, and the restaurant is packed. Two cashiers hit "Save" at almost the same moment. Both get invoice number 10452. At month end, the accountant finds the duplicate. One of the two invoices drops out of the report; the other stays. The money gets counted once instead of twice. The system had run for years without a problem. The bug wasn't new. It was one line written on day one. The suspect Most of us have written this, or inherited it in someone else's code: SELECT NVL(MAX(invoice_no), 0) + 1 INTO v_new_no FROM invoices; INSER…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hossam_assadallah_842151a/max1-the-invoice-number-that-showed-up-twice-3lb1

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-06-29-the-customerid-that-isnt-a-customer]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
