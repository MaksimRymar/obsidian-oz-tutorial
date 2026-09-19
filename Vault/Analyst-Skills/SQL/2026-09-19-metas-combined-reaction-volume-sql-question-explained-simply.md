---
title: Meta's "Combined Reaction Volume" SQL Question, Explained Simply
date: '2026-09-19'
source: https://dev.to/rahmanfrr/metas-combined-reaction-volume-sql-question-explained-simply-25o6
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]'
status: unread
---

> **TL;DR:** Your Feed post gets turned into a Reel. Somebody watches it and taps like. Does the database record that as one like, or two? That messy little detail is the whole point of a Meta SQL interview question called Combined R…

## What’s new and why it matters
Your Feed post gets turned into a Reel. Somebody watches it and taps like. Does the database record that as one like, or two? That messy little detail is the whole point of a Meta SQL interview question called Combined Reaction Volume. It looks like a basic counting problem. It isn't. And if you rush it, you'll get a number that's technically correct and completely wrong at the same time. The setup Meta keeps reactions to Feed posts and Reels in two separate tables, because the two products are built by separate teams: post_reactions — likes, loves, and other reactions on regular Feed posts re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rahmanfrr/metas-combined-reaction-volume-sql-question-explained-simply-25o6

## Related notes
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-08-13-cohort-retention-analysis-in-sql-the-query-that-tells-you-if-your-product-is-actually-sticky]]
