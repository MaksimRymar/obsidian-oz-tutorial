---
title: How a LEFT JOIN Lost a $1,000 Invoice at Month-End
date: '2026-11-11'
source: https://dev.to/noreply_utaxes_f57b6771a0/how-a-left-join-lost-a-1000-invoice-at-month-end-502c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-11-11-i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables]]'
- '[[2026-08-17-from-30-minutes-to-5-seconds-testing-agent-memory-with-pytest-sqlite]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]'
status: unread
---

> **TL;DR:** An invoice for $1,000 is open on September 30. On October 1 the customer pays $400. Run the September report again and the invoice disappears. A customer who paid nothing still shows up just fine. You can reproduce this…

## What’s new and why it matters
An invoice for $1,000 is open on September 30. On October 1 the customer pays $400. Run the September report again and the invoice disappears. A customer who paid nothing still shows up just fine. You can reproduce this with three invoices and one payment in SQLite. Amounts are in US cents. The dates are fixed-width YYYY-MM-DD business dates. applied_on is the day a receipt was applied to this particular invoice. CREATE TABLE invoices ( id TEXT PRIMARY KEY , issued_on TEXT NOT NULL , total_cents INTEGER NOT NULL ) ; CREATE TABLE applications ( invoice_id TEXT NOT NULL REFERENCES invoices ( id…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/noreply_utaxes_f57b6771a0/how-a-left-join-lost-a-1000-invoice-at-month-end-502c

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-11-11-i-built-generaterealdata-a-test-data-generator-where-keys-totals-and-rules-hold-across-tables]]
- [[2026-08-17-from-30-minutes-to-5-seconds-testing-agent-memory-with-pytest-sqlite]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-11-05-sql-inner-join-vs-left-join-vs-right-join-vs-full-outer-join-differences-with-examples-tested-in-mysql-84-and-sqlite]]
