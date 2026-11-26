---
title: The migration found the old dashboard had been counting everything twice
date: '2026-11-26'
source: https://dev.to/vijaykumar13/the-migration-found-the-old-dashboard-had-been-counting-everything-twice-3f3d
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-05-three-months-of-sales-vanished-and-every-dbt-run-was-green]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-11-02-7-sql-checks-i-run-before-uat-sign-off-with-queries-you-can-copy]]'
status: unread
---

> **TL;DR:** The first two posts in this series, about a delete+insert that wiped out three months of data and a merge that never deleted anything , were bugs in our own pipeline. This one went the other way. In this article I'll sho…

## What’s new and why it matters
The first two posts in this series, about a delete+insert that wiped out three months of data and a merge that never deleted anything , were bugs in our own pipeline. This one went the other way. In this article I'll show you how reconciling a new dbt build against an old dashboard proved the old dashboard wrong, how we confirmed it without touching the legacy system, and the cheap checks that would have caught it on day one. Some background I'm an analytics engineer at a leading North American housewares company. Part of our migration is a set of market-share reports that ran on an old on-pre…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vijaykumar13/the-migration-found-the-old-dashboard-had-been-counting-everything-twice-3f3d

## Related notes
- [[2026-10-05-three-months-of-sales-vanished-and-every-dbt-run-was-green]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-11-02-7-sql-checks-i-run-before-uat-sign-off-with-queries-you-can-copy]]
