---
title: 'One compaction, four actions, one block: compaction safety is a property of
  the pair'
date: '2026-07-18'
source: https://dev.to/alex_spinov/one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair-5a77
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-07-01-deduplicating-a-news-feed-the-boring-reliable-way-lexical-semantic-in-two-passes]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-09-how-do-i-answer-what-did-my-data-look-like-last-month-in-postgres]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
status: unread
---

> **TL;DR:** Context compaction is safe or unsafe only against a specific proposed action. Not in general. The compactor decides what your agent forgets before it knows what your agent will do, so at compaction time "did this lose an…

## What’s new and why it matters
Context compaction is safe or unsafe only against a specific proposed action. Not in general. The compactor decides what your agent forgets before it knows what your agent will do, so at compaction time "did this lose anything important?" has no answer yet. The lie, if there is one, comes into existence later, when the agent proposes to act. That sounds like philosophy. It has an exit code. AI disclosure. I wrote compaction_omission_gate.py with an AI assistant and ran it myself: Python 3.13.5, offline, standard library only, no network, no keys, no funds. Every verdict, exit code and hash bel…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alex_spinov/one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair-5a77

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-07-01-deduplicating-a-news-feed-the-boring-reliable-way-lexical-semantic-in-two-passes]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-09-how-do-i-answer-what-did-my-data-look-like-last-month-in-postgres]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
