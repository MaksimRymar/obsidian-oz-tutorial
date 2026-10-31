---
title: 'My open-source text-to-SQL layer is #1 on BIRD Mini-Dev in all three dialects'
date: '2026-10-31'
source: https://dev.to/ashish_sinha_5241c7673d93/my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects-17a
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]'
- '[[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]'
- '[[2026-10-22-771-on-bird-dev-with-one-model-call-per-question-and-a-test-set-submission-in]]'
- '[[2026-10-24-what-one-month-of-public-benchmarks-says-about-my-text-to-sql-access-layer]]'
- '[[2026-10-17-transpile-or-re-ask-fixing-dialect-breaks-in-agent-written-sql]]'
- '[[2026-10-02-your-rls-policy-returns-zero-rows-the-view-next-to-it-returns-two]]'
status: unread
---

> **TL;DR:** BIRD Mini-Dev is 500 text-to-SQL questions over 11 databases, in SQLite, PostgreSQL and MySQL versions, scored by whether the query returns the right rows. BIRD keeps the leaderboard and checks the submissions. schemagat…

## What’s new and why it matters
BIRD Mini-Dev is 500 text-to-SQL questions over 11 databases, in SQLite, PostgreSQL and MySQL versions, scored by whether the query returns the right rows. BIRD keeps the leaderboard and checks the submissions. schemagate, the Apache-2.0 library I maintain, is now first in all three columns: schemagate Next entry SQLite 81.0 75.6 PostgreSQL 72.6 69.0 MySQL 72.4 49.2 The setup is plain: schemagate picks the tables a question needs, the prompt carries only those plus BIRD's column notes, and Claude Opus 5.5 writes one query. No candidate voting and no agent loop. If the query errors, the model s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/my-open-source-text-to-sql-layer-is-1-on-bird-mini-dev-in-all-three-dialects-17a

## Related notes
- [[2026-10-26-schemagate-is-now-1-on-the-official-bird-mini-dev-leaderboard]]
- [[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]
- [[2026-10-22-771-on-bird-dev-with-one-model-call-per-question-and-a-test-set-submission-in]]
- [[2026-10-24-what-one-month-of-public-benchmarks-says-about-my-text-to-sql-access-layer]]
- [[2026-10-17-transpile-or-re-ask-fixing-dialect-breaks-in-agent-written-sql]]
- [[2026-10-02-your-rls-policy-returns-zero-rows-the-view-next-to-it-returns-two]]
