---
title: The free plan searches exactly like the paid one and hides the results, and
  the blurred rows are fake on purpose
date: '2026-10-03'
source: https://dev.to/daniel_pertu/the-free-plan-searches-exactly-like-the-paid-one-and-hides-the-results-and-the-blurred-rows-are-145h
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
status: unread
---

> **TL;DR:** Nakodo ( nakodo.app ) searches YouTube, Instagram and TikTok for creators that fit a brand's brief, then emails the ones that fit. The Free plan shows the best 20 of them and hides the rest until you upgrade. You can see…

## What’s new and why it matters
Nakodo ( nakodo.app ) searches YouTube, Instagram and TikTok for creators that fit a brand's brief, then emails the ones that fit. The Free plan shows the best 20 of them and hides the rest until you upgrade. You can see that line in the comparison table on nakodo.app/pricing : creators shown per campaign, best 20 against all. The first implementation of that limit was wrong in an interesting way, and fixing it turned a product decision into one SQL expression and one deliberately dishonest-looking React component. Version one capped the work Originally a Free campaign stopped searching once i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/the-free-plan-searches-exactly-like-the-paid-one-and-hides-the-results-and-the-blurred-rows-are-145h

## Related notes
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
