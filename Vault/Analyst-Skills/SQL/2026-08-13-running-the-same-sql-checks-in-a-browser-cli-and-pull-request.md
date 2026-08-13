---
title: Running the same SQL checks in a browser, CLI and pull request
date: '2026-08-13'
source: https://dev.to/milekv/running-the-same-sql-checks-in-a-browser-cli-and-pull-request-52hk
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]'
status: unread
---

> **TL;DR:** I wanted one set of SQL checks to work in three places: while exploring a query, from a terminal and during code review. That became SQL Atlas. It is a local, deterministic SQL analyzer with a browser interface, a CLI an…

## What’s new and why it matters
I wanted one set of SQL checks to work in three places: while exploring a query, from a terminal and during code review. That became SQL Atlas. It is a local, deterministic SQL analyzer with a browser interface, a CLI and a GitHub Action. This article covers the interfaces, the CI contract and the limits of static SQL analysis. One analyzer, three interfaces The analyzer returns structured data instead of printing messages directly. Each interface decides how to present the same result: The browser explains findings and links them to learning material. The CLI returns text, JSON or Markdown an…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/milekv/running-the-same-sql-checks-in-a-browser-cli-and-pull-request-52hk

## Related notes
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]
