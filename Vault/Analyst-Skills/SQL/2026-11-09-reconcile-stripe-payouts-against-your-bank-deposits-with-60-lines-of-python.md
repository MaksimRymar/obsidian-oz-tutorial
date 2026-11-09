---
title: Reconcile Stripe payouts against your bank deposits with 60 lines of Python
date: '2026-11-09'
source: https://dev.to/cryptomoneymakr/reconcile-stripe-payouts-against-your-bank-deposits-with-60-lines-of-python-1n9f
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]'
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** If you sell anything through Stripe, the bank statement shows one lump deposit every day or two, while Stripe shows dozens of charges, refunds and fees. Month-end means proving those two views agree. This post builds a s…

## What’s new and why it matters
If you sell anything through Stripe, the bank statement shows one lump deposit every day or two, while Stripe shows dozens of charges, refunds and fees. Month-end means proving those two views agree. This post builds a small script that does that from two CSV exports: no API keys and no dependencies. What Stripe actually pays out With automatic payouts, every balance transaction (a charge, a refund, a fee, a dispute) is assigned to a payout. The payout amount is the sum of the net values of its transactions, and net is gross minus fee , in major units (dollars, not cents). The export to use is…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cryptomoneymakr/reconcile-stripe-payouts-against-your-bank-deposits-with-60-lines-of-python-1n9f

## Related notes
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
