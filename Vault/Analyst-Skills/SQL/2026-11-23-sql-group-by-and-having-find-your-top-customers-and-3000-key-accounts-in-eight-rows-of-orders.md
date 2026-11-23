---
title: 'SQL GROUP BY and HAVING: Find Your Top Customers and $3,000 Key Accounts in
  Eight Rows of Orders'
date: '2026-11-23'
source: https://dev.to/robert_breen_d96e41ecd765/sql-group-by-and-having-find-your-top-customers-and-3000-key-accounts-in-eight-rows-of-orders-4jh
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-24-sql-the-monthly-revenue-report-in-five-lines-group-by-month-instead-of-a-spreadsheet-every-month-end]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-24-sql-find-the-customers-who-stopped-ordering-with-a-left-join-and-why-a-plain-join-hides-the-one-you-most-need-to-call]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** Before a quarterly review, someone usually gets asked two questions: who are our top three customers, and which accounts were worth $3,000 or more this quarter? The usual answer is a spreadsheet, a sort, and a lot of add…

## What’s new and why it matters
Before a quarterly review, someone usually gets asked two questions: who are our top three customers, and which accounts were worth $3,000 or more this quarter? The usual answer is a spreadsheet, a sort, and a lot of adding up by hand. Both questions are four SQL keywords: GROUP BY , ORDER BY , LIMIT and HAVING . This walkthrough uses a made-up shop, Lakeside Office Supply, with eight orders. You can type all of it into DB Fiddle (free, no account needed, MySQL v9 selected). Step 1: make the orders table DB Fiddle has two boxes. The left one, Schema SQL , holds the table. Click inside it and t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/robert_breen_d96e41ecd765/sql-group-by-and-having-find-your-top-customers-and-3000-key-accounts-in-eight-rows-of-orders-4jh

## Related notes
- [[2026-10-24-sql-the-monthly-revenue-report-in-five-lines-group-by-month-instead-of-a-spreadsheet-every-month-end]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-24-sql-find-the-customers-who-stopped-ordering-with-a-left-join-and-why-a-plain-join-hides-the-one-you-most-need-to-call]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
