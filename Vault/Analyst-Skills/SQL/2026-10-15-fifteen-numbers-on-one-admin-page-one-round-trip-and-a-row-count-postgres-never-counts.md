---
title: Fifteen numbers on one admin page, one round trip, and a row count Postgres
  never counts
date: '2026-10-15'
source: https://dev.to/daniel_pertu/fifteen-numbers-on-one-admin-page-one-round-trip-and-a-row-count-postgres-never-counts-50md
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-07-seventeen-subqueries-in-one-statement-because-our-connection-pool-has-five-slots]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-09-22-our-product-search-only-returns-rows-the-scanner-can-actually-answer-for]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** Munchable has an operator panel with an overview page on it. Accounts, premium accounts, new accounts this week, open tickets, tickets awaiting a reply, closed tickets, tickets this week, products in the catalogue, a cou…

## What’s new and why it matters
Munchable has an operator panel with an overview page on it. Accounts, premium accounts, new accounts this week, open tickets, tickets awaiting a reply, closed tickets, tickets this week, products in the catalogue, a couple of filtered catalogue states, active ingredient entries, the curation backlog, rewards earned, rewards applied. Fifteen numbers, one screen, and the only person who ever loads it is me. It is the most boring page in the product and it used to take unrelated requests down with it. Fifteen counts is fifteen connections The first version was the obvious one. Fifteen count(*) q…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/fifteen-numbers-on-one-admin-page-one-round-trip-and-a-row-count-postgres-never-counts-50md

## Related notes
- [[2026-10-07-seventeen-subqueries-in-one-statement-because-our-connection-pool-has-five-slots]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-09-22-our-product-search-only-returns-rows-the-scanner-can-actually-answer-for]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
