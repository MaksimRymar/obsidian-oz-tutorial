---
title: 'Building a construction WIP schedule in Python: percent complete, over and
  under billing, and the month-end entry'
date: '2026-10-18'
source: https://dev.to/zerabooks/building-a-construction-wip-schedule-in-python-percent-complete-over-and-under-billing-and-the-3kb6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]'
- '[[2026-08-10-build-a-gst-invoice-data-extractor-in-45-lines-of-python]]'
- '[[2026-10-12-monte-carlo-bid-estimating-price-a-construction-bid-at-p80-not-a-single-number]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]'
- '[[2026-09-22-a-retry-on-a-new-proxy-exit-can-double-submit-idempotency-for-scrapers-that-post]]'
status: unread
---

> **TL;DR:** A construction WIP schedule computes earned revenue for each open job as contract price times percent complete , where percent complete is cost to date divided by estimated total cost . Billed minus earned is overbilling…

## What’s new and why it matters
A construction WIP schedule computes earned revenue for each open job as contract price times percent complete , where percent complete is cost to date divided by estimated total cost . Billed minus earned is overbilling when positive and underbilling when negative. One journal entry a month moves the totals into the ledger, and debits must equal credits. I work on ZeraBooks, and contractors send us exactly this report each month. Here is the computation with the figures from our contractor guide. All jobs are fictional. What inputs does a WIP schedule need? from dataclasses import dataclass f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zerabooks/building-a-construction-wip-schedule-in-python-percent-complete-over-and-under-billing-and-the-3kb6

## Related notes
- [[2026-09-28-i-built-an-api-that-checks-whether-sec-financial-data-adds-up]]
- [[2026-08-10-build-a-gst-invoice-data-extractor-in-45-lines-of-python]]
- [[2026-10-12-monte-carlo-bid-estimating-price-a-construction-bid-at-p80-not-a-single-number]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]
- [[2026-09-22-a-retry-on-a-new-proxy-exit-can-double-submit-idempotency-for-scrapers-that-post]]
