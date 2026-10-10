---
title: Your eBay sold-price data is 14.9% too high and the response looks fine
date: '2026-10-10'
source: https://dev.to/sam_compsapi/your-ebay-sold-price-data-is-149-too-high-and-the-response-looks-fine-2b92
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-10-01-how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
status: unread
---

> **TL;DR:** If your code reads eBay sold prices, it has a bug you cannot see. Not a parsing bug. The number comes back well formed, plausible, in the right currency, and wrong. I run CompsAPI, so I hold both the asking price and the…

## What’s new and why it matters
If your code reads eBay sold prices, it has a bug you cannot see. Not a parsing bug. The number comes back well formed, plausible, in the right currency, and wrong. I run CompsAPI, so I hold both the asking price and the accepted price on the same sale. That let me measure the gap instead of guessing at it. Here is what came out, and why no amount of better scraping fixes it. The failure mode When an eBay listing sells through an accepted Best Offer, eBay's public sold page shows the asking price . The amount the buyer actually paid is not on that page. There is no field holding it, no query p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sam_compsapi/your-ebay-sold-price-data-is-149-too-high-and-the-response-looks-fine-2b92

## Related notes
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-10-01-how-i-close-a-monthly-dataset-and-the-month-i-found-out-mine-had-been-lying]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
