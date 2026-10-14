---
title: Our free plan hides creators with a window function, and the locked count is
  the same predicate with a "not" in front
date: '2026-10-14'
source: https://dev.to/daniel_pertu/our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-42m6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-10-03-the-free-plan-searches-exactly-like-the-paid-one-and-hides-the-results-and-the-blurred-rows-are-fake-on-purpose]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]'
status: unread
---

> **TL;DR:** Nakodo's free plan runs a campaign exactly like a paid one. It searches the same way, checks the same creators, scores them the same way, and then shows you the best 20 of the ones it could write to. The rest are counted…

## What’s new and why it matters
Nakodo's free plan runs a campaign exactly like a paid one. It searches the same way, checks the same creators, scores them the same way, and then shows you the best 20 of the ones it could write to. The rest are counted, not thrown away, and they appear if you upgrade. The pricing page says "Best 20" on the free row and "All" on the others. The obvious implementation is LIMIT 20 on the results query. That was wrong, and the reason it was wrong is a decent lesson about where a product rule should live. Eight call sites need the same subset, and one of them is its complement "Which results can…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-42m6

## Related notes
- [[2026-10-03-the-free-plan-searches-exactly-like-the-paid-one-and-hides-the-results-and-the-blurred-rows-are-fake-on-purpose]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-10-06-a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]
