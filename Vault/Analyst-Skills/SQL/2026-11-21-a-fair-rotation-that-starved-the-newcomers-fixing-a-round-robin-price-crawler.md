---
title: 'A fair rotation that starved the newcomers: fixing a round-robin price crawler'
date: '2026-11-21'
source: https://dev.to/2cstudio/a-fair-rotation-that-starved-the-newcomers-fixing-a-round-robin-price-crawler-pkh
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-10-10-from-35-seconds-to-half-a-second-70-faster-dashboards-in-plain-postgres]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-08-07-my-comment-reply-script-asked-devto-for-my-articles-leaving-off-one-query-param-silently-dropped-the-newest-two]]'
- '[[2026-10-25-pagination-that-skips-rows-is-an-off-by-one-in-the-data-model]]'
status: unread
---

> **TL;DR:** Steam Inventory Value prices a Steam inventory from a cache of market prices. A crawler inside Postgres keeps that cache fresh: every minute it may fetch two pages of a game's market catalogue, 100 items a page. The budg…

## What’s new and why it matters
Steam Inventory Value prices a Steam inventory from a cache of market prices. A crawler inside Postgres keeps that cache fresh: every minute it may fetch two pages of a game's market catalogue, 100 items a page. The budget is small on purpose, because Steam rations requests. Two pages a minute has to be shared between every game we support. This post is about how we shared it, why that quietly failed for new games, and the small rule that fixed it. The rotation Each game has a refresh interval: 6 hours for Dota 2 and CS2, 12 for TF2 and Rust, 24 for Steam trading cards. The crawler picks the g…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/2cstudio/a-fair-rotation-that-starved-the-newcomers-fixing-a-round-robin-price-crawler-pkh

## Related notes
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-10-10-from-35-seconds-to-half-a-second-70-faster-dashboards-in-plain-postgres]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-08-07-my-comment-reply-script-asked-devto-for-my-articles-leaving-off-one-query-param-silently-dropped-the-newest-two]]
- [[2026-10-25-pagination-that-skips-rows-is-an-off-by-one-in-the-data-model]]
