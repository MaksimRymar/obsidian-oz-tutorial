---
title: my sigma scanner can't count, so i wrote that down instead of faking it
date: '2026-06-15'
source: https://dev.to/tiltedlunar123/my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it-2ci6
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** i've got a small python tool called SIEMForge. you point it at a log file and a folder of sigma rules and it tells you which rules fire on which events, no SIEM involved. it's at v3.1, 10 bundled rules, and the only runt…

## What’s new and why it matters
i've got a small python tool called SIEMForge. you point it at a log file and a folder of sigma rules and it tells you which rules fire on which events, no SIEM involved. it's at v3.1, 10 bundled rules, and the only runtime dependency is pyyaml. most of what it does is one-event-at-a-time matching. read an event, run every rule against it, print the ones that hit. that model is dead simple, and it's most of the reason the tool is useful for actually writing rules. you tweak a rule, rerun, see the result in under a second. that loop is the whole point. then i hit the one rule that doesn't fit t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tiltedlunar123/my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it-2ci6

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
