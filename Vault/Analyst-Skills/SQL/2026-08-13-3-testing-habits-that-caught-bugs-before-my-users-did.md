---
title: 3 Testing Habits That Caught Bugs Before My Users Did
date: '2026-08-13'
source: https://dev.to/sirmax/3-testing-habits-that-caught-bugs-before-my-users-did-35eg
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
status: unread
---

> **TL;DR:** Last month a user reported that our checkout endpoint charged them twice. The code looked fine in review. Every test was green. The bug only appeared when two requests hit the same endpoint within the same millisecond —…

## What’s new and why it matters
Last month a user reported that our checkout endpoint charged them twice. The code looked fine in review. Every test was green. The bug only appeared when two requests hit the same endpoint within the same millisecond — a race condition between the "check if order exists" query and the "insert order" query. That single bug cost a refund, a support ticket, and an afternoon of my time. It also reminded me of something I already knew but kept ignoring: tests that only cover the happy path don't catch much. Since then I've adopted three habits that have caught bugs before my users did. They're not…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sirmax/3-testing-habits-that-caught-bugs-before-my-users-did-35eg

## Related notes
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
