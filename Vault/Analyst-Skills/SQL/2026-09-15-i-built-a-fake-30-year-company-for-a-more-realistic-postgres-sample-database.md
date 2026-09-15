---
title: I built a fake 30-year company for a more realistic Postgres sample database
date: '2026-09-15'
source: https://dev.to/ukhype1983_a92e7968657284/i-built-a-fake-30-year-company-for-a-more-realistic-postgres-sample-database-2p9h
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
status: unread
---

> **TL;DR:** Every sample database has the same problem: it's either too small to be interesting or too abstract to stick in your head. pagila and Chinook are lovely, but you'll never stress a query planner with a few thousand rows.…

## What’s new and why it matters
Every sample database has the same problem: it's either too small to be interesting or too abstract to stick in your head. pagila and Chinook are lovely, but you'll never stress a query planner with a few thousand rows. The StackOverflow dataset is genuinely great. But posts-and-votes only takes you so far, and I wanted data anyone could reason about on sight. So I did the sensible thing and invented an entire company. Meet Nick's Gaming Emporium NGE is a fictional video-game retailer, simulated across its whole life, from 1986 to 2016 . It opens in a strip mall, rides the dot-com wave, balloo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ukhype1983_a92e7968657284/i-built-a-fake-30-year-company-for-a-more-realistic-postgres-sample-database-2p9h

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
