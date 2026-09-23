---
title: 'Secrets Stay Home: Splitting Agent Work Between Laptop and Server'
date: '2026-09-23'
source: https://dev.to/codepro_9661/secrets-stay-home-splitting-agent-work-between-laptop-and-server-1h50
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]'
- '[[2026-09-07-score-the-trace-not-the-final-payload]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-04-when-index-hit-stats-go-stale-two-positions-for-sql-review-agents]]'
status: unread
---

> **TL;DR:** On a Tuesday afternoon, a staff engineer watched a local coding agent chew through a refactor on a four-year-old payments service. The laptop stayed warm, the uncommitted tree stayed dirty, and the .env file never left t…

## What’s new and why it matters
On a Tuesday afternoon, a staff engineer watched a local coding agent chew through a refactor on a four-year-old payments service. The laptop stayed warm, the uncommitted tree stayed dirty, and the .env file never left the disk that already held it. Later that night a teammate queued a bulk fixture generator because the laptop could not finish the run before a standup demo. They rsynced the entire working copy to a borrowed cloud box, including the secret file that the daytime session had treated as immovable. The morning review blamed a missing split between work that must stay local and work…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepro_9661/secrets-stay-home-splitting-agent-work-between-laptop-and-server-1h50

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]
- [[2026-09-07-score-the-trace-not-the-final-payload]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-04-when-index-hit-stats-go-stale-two-positions-for-sql-review-agents]]
