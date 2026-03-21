---
title: SQL triggers for blocking
date: '2026-03-20'
source: https://dev.to/faith_in_errors_/sql-triggers-for-blocking-2llo
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#zendesk'
related:
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-03-08-sql-queries-asked-in-interview]]'
- '[[2026-03-20-postgresqlaggregative-functions]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-23-8-sql-queries-that-catch-90-of-interview-candidates-off-guard]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** AFTER INSERT, UPDATE AS BEGIN SET NOCOUNT ON; -- Look for the modified InvoiceId in the list of invoices exceeding the limit IF (SELECT TOP 1 InvoiceId FROM Inserted) IN ( SELECT InvoiceId FROM ( SELECT IL.InvoiceId, COU…

## What’s new and why it matters
AFTER INSERT, UPDATE AS BEGIN SET NOCOUNT ON; -- Look for the modified InvoiceId in the list of invoices exceeding the limit IF (SELECT TOP 1 InvoiceId FROM Inserted) IN ( SELECT InvoiceId FROM ( SELECT IL.InvoiceId, COUNT(*) AS count FROM InvoiceLine IL JOIN Track T ON IL.TrackId = T.TrackId WHERE T.GenreId = 32 -- Genre GROUP BY IL.InvoiceId ) AS Summary WHERE count > 3 ) BEGIN RAISERROR ('Market Overload! Max 3 Anime items per invoice.', 16, 1); ROLLBACK TRANSACTION; END END;

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/faith_in_errors_/sql-triggers-for-blocking-2llo

## Related notes
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-03-08-sql-queries-asked-in-interview]]
- [[2026-03-20-postgresqlaggregative-functions]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-23-8-sql-queries-that-catch-90-of-interview-candidates-off-guard]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
