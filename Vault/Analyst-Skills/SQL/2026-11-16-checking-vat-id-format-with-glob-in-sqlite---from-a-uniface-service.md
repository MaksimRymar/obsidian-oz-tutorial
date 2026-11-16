---
title: Checking VAT ID format with GLOB in SQLite - from a Uniface service
date: '2026-11-16'
source: https://dev.to/f345345dfg/checking-vat-id-format-with-glob-in-sqlite-from-a-uniface-service-5d3l
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-11-16-validating-free-form-field-values-in-sqlite---glob-patterns-and-a-date-surprise]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-11-16-customer-hierarchies-with-with-recursive---finding-cycles-and-group-totals-in-a-uniface-service]]'
- '[[2026-10-20-sqlazy-find-strings-with-5-or-more-consecutive-alphabetical-letters]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-11-16-oracle-fusion-rest-api-returns-only-25-invoices-page-through-with-limit-offset-and-hasmore]]'
status: unread
---

> **TL;DR:** A customer app built in Uniface 10 stores a VAT ID per business customer. A tax check module should list IDs that are obviously wrong: too short, no country prefix, odd characters, or a prefix that does not fit the billi…

## What’s new and why it matters
A customer app built in Uniface 10 stores a VAT ID per business customer. A tax check module should list IDs that are obviously wrong: too short, no country prefix, odd characters, or a prefix that does not fit the billing address. This is not a full validation with checksums per country, only a plausibility check that catches typos before an invoice goes out. Tested with Rocket Uniface 10.4.03 Community Edition (10.4.03.021) on Windows, November 2026. The app uses SQLite through the SLE driver (SQLite 3.50.2). Normalising first Users type DE 123 456 789 , de123456789 or DE123456789 . All thre…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/f345345dfg/checking-vat-id-format-with-glob-in-sqlite-from-a-uniface-service-5d3l

## Related notes
- [[2026-11-16-validating-free-form-field-values-in-sqlite---glob-patterns-and-a-date-surprise]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-11-16-customer-hierarchies-with-with-recursive---finding-cycles-and-group-totals-in-a-uniface-service]]
- [[2026-10-20-sqlazy-find-strings-with-5-or-more-consecutive-alphabetical-letters]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-11-16-oracle-fusion-rest-api-returns-only-25-invoices-page-through-with-limit-offset-and-hasmore]]
