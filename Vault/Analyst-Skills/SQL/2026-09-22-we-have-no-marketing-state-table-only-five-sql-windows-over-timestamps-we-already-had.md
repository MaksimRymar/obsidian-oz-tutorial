---
title: We have no marketing state table, only five SQL windows over timestamps we
  already had
date: '2026-09-22'
source: https://dev.to/daniel_pertu/we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had-3p75
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-14-my-migration-generator-shuffled-itself-for-two-days-pythonhashseed-was-the-coin-flip]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** CogniPrep sends five lifecycle emails. Somebody tries an assessment-centre exercise and does not unlock it. Somebody plays a practice test but has not bought feedback. Somebody signs up and owns nothing an hour later. Th…

## What’s new and why it matters
CogniPrep sends five lifecycle emails. Somebody tries an assessment-centre exercise and does not unlock it. Somebody plays a practice test but has not bought feedback. Somebody signs up and owns nothing an hour later. The normal way to build this is a marketing state machine: a table per user holding which campaigns they are enrolled in, which step they are on, when they last received something. That table then has to be written by every part of your app that changes a user's situation, and it goes wrong the first time somebody buys a thing through a path that forgot to update it. We have none…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had-3p75

## Related notes
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-14-my-migration-generator-shuffled-itself-for-two-days-pythonhashseed-was-the-coin-flip]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
