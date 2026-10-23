---
title: Turning a messy payments export into a 2026 1099 vendor worksheet (without
  silently wrong totals)
date: '2026-10-23'
source: https://dev.to/trilliumcompany/turning-a-messy-payments-export-into-a-2026-1099-vendor-worksheet-without-silently-wrong-totals-1988
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-29-python-part-2]]'
- '[[2026-10-11-how-to-export-google-play-reviews-to-csv-for-any-app-and-country]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** For 2026 payments, the Form 1099-NEC reporting threshold goes from USD 600 to USD 2,000 (1099-MISC thresholds still vary by payment type, and backup withholding can require reporting below a threshold; see the IRS page )…

## What’s new and why it matters
For 2026 payments, the Form 1099-NEC reporting threshold goes from USD 600 to USD 2,000 (1099-MISC thresholds still vary by payment type, and backup withholding can require reporting below a threshold; see the IRS page ). If you keep the books for a small business, or write scripts for someone who does, this year's vendor list needs a fresh pass. The awkward part isn't the threshold; it's the export. Here's a small, defensive way to turn a messy payments export into a reviewable vendor worksheet. This is data preparation, not tax advice. The problems in a typical export The same vendor appears…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/trilliumcompany/turning-a-messy-payments-export-into-a-2026-1099-vendor-worksheet-without-silently-wrong-totals-1988

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-29-python-part-2]]
- [[2026-10-11-how-to-export-google-play-reviews-to-csv-for-any-app-and-country]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
