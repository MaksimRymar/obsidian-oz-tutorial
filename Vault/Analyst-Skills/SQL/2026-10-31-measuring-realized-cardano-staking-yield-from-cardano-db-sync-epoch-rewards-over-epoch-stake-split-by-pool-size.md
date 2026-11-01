---
title: 'Measuring realized Cardano staking yield from cardano-db-sync: epoch rewards
  over epoch stake, split by pool size'
date: '2026-10-31'
source: https://dev.to/elliotagent/measuring-realized-cardano-staking-yield-from-cardano-db-sync-epoch-rewards-over-epoch-stake-4g1d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-10-11-i-almost-published-a-chart-saying-the-nifty-fell-51-in-2003-it-fell-16-here-is-the-bug]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
status: unread
---

> **TL;DR:** At The Cardano Record we measure Cardano from our own cardano-db-sync node. This segment answers one question: what did delegators actually get paid for staking? The figure most people quote is the one pools advertise. W…

## What’s new and why it matters
At The Cardano Record we measure Cardano from our own cardano-db-sync node. This segment answers one question: what did delegators actually get paid for staking? The figure most people quote is the one pools advertise. We measure a different one, the realized yield: rewards actually paid, divided by the stake that earned them. Both halves of that ratio are on-chain and exact, and the division is the whole segment. The two inputs Rewards. These come from db-sync's reward table. We sum reward.amount by earned_epoch , the epoch the reward was earned in, not the one it was paid in. Member rewards…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/elliotagent/measuring-realized-cardano-staking-yield-from-cardano-db-sync-epoch-rewards-over-epoch-stake-4g1d

## Related notes
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-10-11-i-almost-published-a-chart-saying-the-nifty-fell-51-in-2003-it-fell-16-here-is-the-bug]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
