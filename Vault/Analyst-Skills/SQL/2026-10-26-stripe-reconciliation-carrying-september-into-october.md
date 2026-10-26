---
title: 'Stripe reconciliation: carrying September into October'
date: '2026-10-26'
source: https://dev.to/akarazhev/stripe-reconciliation-carrying-september-into-october-2743
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-10-08-the-refund-arrived-after-the-payout-so-the-fix-was-two-nullable-columns-and-no-code]]'
- '[[2026-10-19-why-stripe-payouts-dont-match-your-books]]'
- '[[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** In the first article , I used SQL to explain a €3,496.99 gap between the ledger and the bank for a fictional EU shop. A reader pointed out that some of the harder cases cross the month boundary. A payout arrives after th…

## What’s new and why it matters
In the first article , I used SQL to explain a €3,496.99 gap between the ledger and the bank for a fictional EU shop. A reader pointed out that some of the harder cases cross the month boundary. A payout arrives after the close, a dispute is resolved the following month, or a USD payment is refunded after the exchange rate has changed. So I added October to the demo. It has 620 charges, 21 refunds and a payout every weekday. I left September's data as it was and added those three cases. Apart from the two entries tied to September, October's operations match. What carries over from September L…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/akarazhev/stripe-reconciliation-carrying-september-into-october-2743

## Related notes
- [[2026-10-08-the-refund-arrived-after-the-payout-so-the-fix-was-two-nullable-columns-and-no-code]]
- [[2026-10-19-why-stripe-payouts-dont-match-your-books]]
- [[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
