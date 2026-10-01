---
title: 'A per-order margin ledger: reconciling what you quoted against what the carrier
  billed'
date: '2026-10-01'
source: https://dev.to/fulfillnexa/a-per-order-margin-ledger-reconciling-what-you-quoted-against-what-the-carrier-billed-34gg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]'
status: unread
---

> **TL;DR:** Shipping cost in most ecommerce backends is an estimate that nobody checks. At checkout you show a number from a rate table. The parcel ships. The carrier sends an invoice six weeks later with a different number on it. N…

## What’s new and why it matters
Shipping cost in most ecommerce backends is an estimate that nobody checks. At checkout you show a number from a rate table. The parcel ships. The carrier sends an invoice six weeks later with a different number on it. Nobody joins the two, because joining them means matching a carrier's line-item PDF against your order ids, and so the difference just disappears into cost of goods sold and the margin dashboard keeps lying. The fix is unglamorous and it pays for itself: a ledger that records the quote, the actual, and the variance per shipment, and a reconciliation step that fills in the actual…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fulfillnexa/a-per-order-margin-ledger-reconciling-what-you-quoted-against-what-the-carrier-billed-34gg

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]
