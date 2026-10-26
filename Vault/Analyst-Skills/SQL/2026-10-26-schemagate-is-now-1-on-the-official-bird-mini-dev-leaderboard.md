---
title: 'schemagate is now #1 on the official BIRD Mini-Dev leaderboard'
date: '2026-10-26'
source: https://dev.to/ashish_sinha_5241c7673d93/schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard-4cec
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]'
- '[[2026-10-22-771-on-bird-dev-with-one-model-call-per-question-and-a-test-set-submission-in]]'
- '[[2026-10-24-what-one-month-of-public-benchmarks-says-about-my-text-to-sql-access-layer]]'
- '[[2026-10-07-strands-decider-2b-vs-llm-as-a-judge-a-keyword-regex-tied-the-2b]]'
- '[[2026-10-23-twelve-selects-for-the-list-and-six-filtered-counts-for-the-page-and-the-only-shared-code-is-three-sql-fragments]]'
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
status: unread
---

> **TL;DR:** The BIRD team merged our entry, so it is official: schemagate + Claude Opus 5.5 is #1 on the BIRD Mini-Dev leaderboard in all three dialects, and schemagate + Gemini 2.5 Flash is #2. SQLite MySQL PostgreSQL schemagate +…

## What’s new and why it matters
The BIRD team merged our entry, so it is official: schemagate + Claude Opus 5.5 is #1 on the BIRD Mini-Dev leaderboard in all three dialects, and schemagate + Gemini 2.5 Flash is #2. SQLite MySQL PostgreSQL schemagate + Claude Opus 5.5 81.00 72.40 72.60 schemagate + Gemini 2.5 Flash 63.60 54.80 55.60 Execution accuracy on BIRD's 500 Mini-Dev questions, scored by BIRD's own evaluator. What schemagate does: before the model writes SQL, it picks only the tables and columns the question needs (and only ones that caller is allowed to read), and refuses generated SQL that reaches past them. One mode…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard-4cec

## Related notes
- [[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]
- [[2026-10-22-771-on-bird-dev-with-one-model-call-per-question-and-a-test-set-submission-in]]
- [[2026-10-24-what-one-month-of-public-benchmarks-says-about-my-text-to-sql-access-layer]]
- [[2026-10-07-strands-decider-2b-vs-llm-as-a-judge-a-keyword-regex-tied-the-2b]]
- [[2026-10-23-twelve-selects-for-the-list-and-six-filtered-counts-for-the-page-and-the-only-shared-code-is-three-sql-fragments]]
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
