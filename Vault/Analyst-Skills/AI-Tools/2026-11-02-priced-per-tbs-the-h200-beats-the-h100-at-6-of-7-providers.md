---
title: Priced per TB/s, the H200 beats the H100 at 6 of 7 providers
date: '2026-11-02'
source: https://dev.to/sampop3/priced-per-tbs-the-h200-beats-the-h100-at-6-of-7-providers-1lia
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]'
- '[[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** An H200 has exactly as much compute as an SXM H100 and usually rents for more, so on a FLOPS spreadsheet it never makes sense. The H200 vs H100 cost per token question turns on a different column: the H200 moves 4.8 TB/s…

## What’s new and why it matters
An H200 has exactly as much compute as an SXM H100 and usually rents for more, so on a FLOPS spreadsheet it never makes sense. The H200 vs H100 cost per token question turns on a different column: the H200 moves 4.8 TB/s out of memory against the H100's 3.35, and decode spends its time waiting on memory. Memory is also what the industry is short of: TechCrunch reports that Samsung used its Q2 earnings call to say the shortage worsens in 2027 and stays tight until at least 2028. So we priced that column, using our GPU table for 2026-10-30. Decode waits on memory, even at large batches The Flash…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sampop3/priced-per-tbs-the-h200-beats-the-h100-at-6-of-7-providers-1lia

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]
- [[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
