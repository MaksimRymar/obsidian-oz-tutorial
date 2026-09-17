---
title: 'A 200 that isn''t reachability: SpareRoom''s soft-redirect and the empty run
  nobody notices'
date: '2026-09-17'
source: https://dev.to/devil_scrapes/a-200-that-isnt-reachability-sparerooms-soft-redirect-and-the-empty-run-nobody-notices-367e
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]'
- '[[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-06-14-the-billing-state-most-apis-get-wrong-unknown-is-not-no]]'
status: unread
---

> **TL;DR:** Quick answer: SpareRoom does not 404 an unknown location. It soft-redirects to the generic /flatshare/search.pl form page and returns HTTP 200 . A scraper that checks the status code sees success, parses a form, finds ze…

## What’s new and why it matters
Quick answer: SpareRoom does not 404 an unknown location. It soft-redirects to the generic /flatshare/search.pl form page and returns HTTP 200 . A scraper that checks the status code sees success, parses a form, finds zero cards, and reports a clean empty run. The fix is not a better selector — it's refusing to treat a status code as evidence that you landed where you asked to land. Why does a misspelled location return 200? Because the redirect is a product decision, not an error path. Ask SpareRoom for /flatshare/not-a-real-place-xyz and you end up at https://www.spareroom.co.uk/flatshare/se…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/a-200-that-isnt-reachability-sparerooms-soft-redirect-and-the-empty-run-nobody-notices-367e

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]
- [[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-06-14-the-billing-state-most-apis-get-wrong-unknown-is-not-no]]
