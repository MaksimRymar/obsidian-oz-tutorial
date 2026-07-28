---
title: How I Made Sure You Can't Like and Dislike the Same Post at Once
date: '2026-07-28'
source: https://dev.to/kahenda/how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once-56io
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
status: unread
---

> **TL;DR:** Quick one today. While building the reactions feature for our team's forum project (Go + SQLite), I hit a question that sounds obvious until you actually have to implement it: what happens when a user likes a post, then…

## What’s new and why it matters
Quick one today. While building the reactions feature for our team's forum project (Go + SQLite), I hit a question that sounds obvious until you actually have to implement it: what happens when a user likes a post, then clicks dislike on the same post? Do they end up with both a like and a dislike registered? Because that would be a bug — a post shouldn't be simultaneously liked and disliked by the same person. The naive approach (don't do this) The tempting first instinct is: every click on Like or Dislike just inserts a new row into a reactions table. sql INSERT INTO reactions (user_id, targ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kahenda/how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once-56io

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
