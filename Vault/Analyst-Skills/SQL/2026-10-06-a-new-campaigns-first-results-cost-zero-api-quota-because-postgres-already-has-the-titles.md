---
title: A new campaign's first results cost zero API quota, because Postgres already
  has the titles
date: '2026-10-06'
source: https://dev.to/daniel_pertu/a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles-4j96
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** Searching a platform API for a brand's keywords is the slow, expensive, rate-limited part of Nakodo . YouTube's Data API gives a project 10,000 quota units a day and charges 100 of them for a single search call, so a day…

## What’s new and why it matters
Searching a platform API for a brand's keywords is the slow, expensive, rate-limited part of Nakodo . YouTube's Data API gives a project 10,000 quota units a day and charges 100 of them for a single search call, so a day's quota is at most a hundred searches for the entire product, and we cap ours below that to leave room for everything else that spends units. Meanwhile, every creator any campaign has ever found is sitting in our own Postgres, with their recent video titles. Two brands selling slim wallets want substantially the same creators. The second one does not need to spend search quota…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/a-new-campaigns-first-results-cost-zero-api-quota-because-postgres-already-has-the-titles-4j96

## Related notes
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
