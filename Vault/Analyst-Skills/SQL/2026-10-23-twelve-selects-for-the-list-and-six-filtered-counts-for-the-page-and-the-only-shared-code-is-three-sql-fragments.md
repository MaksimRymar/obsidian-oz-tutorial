---
title: Twelve SELECTs for the list and six filtered counts for the page, and the only
  shared code is three SQL fragments
date: '2026-10-23'
source: https://dev.to/daniel_pertu/twelve-selects-for-the-list-and-six-filtered-counts-for-the-page-and-the-only-shared-code-is-three-1op9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
status: unread
---

> **TL;DR:** Nakodo has two screens that count the same rows. The campaigns list shows a card per campaign with found, fit, contacted and replied on it. A campaign's own page shows a funnel: found, fit, waiting, contacted, plus how m…

## What’s new and why it matters
Nakodo has two screens that count the same rows. The campaigns list shows a card per campaign with found, fit, contacted and replied on it. A campaign's own page shows a funnel: found, fit, waiting, contacted, plus how many results are still being checked and, on the free plan, how many are scored but hidden. Same words, same table, two completely different queries, because one needs a number per campaign in a list and the other needs six numbers for one campaign. That is the situation where a codebase grows two definitions of "fit" and nobody notices for a month. Our defence is that neither s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/twelve-selects-for-the-list-and-six-filtered-counts-for-the-page-and-the-only-shared-code-is-three-1op9

## Related notes
- [[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
