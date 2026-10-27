---
title: 'The Free Server Slept Overnight: Four State Claims Your App Can''t Back Up'
date: '2026-10-27'
source: https://dev.to/gitlab_3188/the-free-server-slept-overnight-four-state-claims-your-app-cant-back-up-4l27
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-09-the-idle-gap-wore-a-model-badge]]'
- '[[2026-08-18-shadow-test-free-model-endpoint-changes-before-you-rely-on-them]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** Your app worked at 6pm. At 9am it half-worked. Nothing changed in git. So what changed? The process died and came back. That is the whole story. Most "free server" bugs are not code bugs. They are state bugs wearing a co…

## What’s new and why it matters
Your app worked at 6pm. At 9am it half-worked. Nothing changed in git. So what changed? The process died and came back. That is the whole story. Most "free server" bugs are not code bugs. They are state bugs wearing a costume. This post is not about portability. Portability asks "does it run there?" Durability asks "does it still run tomorrow?" Different question, different probe. Below is a small app, a restart probe, and four claims I keep hearing. Each claim gets a test you can run in about ten minutes. What this post does and does not claim I am not claiming your free server is unreliable.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gitlab_3188/the-free-server-slept-overnight-four-state-claims-your-app-cant-back-up-4l27

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-09-the-idle-gap-wore-a-model-badge]]
- [[2026-08-18-shadow-test-free-model-endpoint-changes-before-you-rely-on-them]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
