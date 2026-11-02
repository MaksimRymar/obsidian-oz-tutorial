---
title: 'Cleaning a product CSV before import: encoding, image URLs, variant rows,
  and finding the line that broke'
date: '2026-11-02'
source: https://dev.to/aumcreate/cleaning-a-product-csv-before-import-encoding-image-urls-variant-rows-and-finding-the-line-that-521l
domain: SQL
relevance: 🔴
tags:
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-10-29-two-requests-one-rule-two-rows-fixing-the-insert-where-not-exists-race-in-postgresql]]'
- '[[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
status: unread
---

> **TL;DR:** An 800-row product sheet looks like a 20-minute import until the importer stops somewhere past the halfway mark and says the SKU is duplicated. It does not say which line. That is usually the moment people start deleting…

## What’s new and why it matters
An 800-row product sheet looks like a 20-minute import until the importer stops somewhere past the halfway mark and says the SKU is duplicated. It does not say which line. That is usually the moment people start deleting rows until something passes. Most of those failures come from the file, not the store. The encoding, the price column, the image URL column, the variation rows and the SKU column account for nearly all of them. Clean those in a script first and the import turns into a non-event. Everything below is plain Python 3 and works on any CSV you are about to feed into an admin importe…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aumcreate/cleaning-a-product-csv-before-import-encoding-image-urls-variant-rows-and-finding-the-line-that-521l

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-10-29-two-requests-one-rule-two-rows-fixing-the-insert-where-not-exists-race-in-postgresql]]
- [[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
