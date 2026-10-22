---
title: 77.1% on BIRD dev with one model call per question, and a test-set submission
  in
date: '2026-10-22'
source: https://dev.to/ashish_sinha_5241c7673d93/771-on-bird-dev-with-one-model-call-per-question-and-a-test-set-submission-in-5g6p
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
status: unread
---

> **TL;DR:** BIRD is the text-to-SQL benchmark the serious systems compete on: 1,534 dev questions over 11 real databases, scored by execution accuracy, with a hidden test set that only the BIRD team can run. I ran schemagate on the…

## What’s new and why it matters
BIRD is the text-to-SQL benchmark the serious systems compete on: 1,534 dev questions over 11 real databases, scored by execution accuracy, with a hidden test set that only the BIRD team can run. I ran schemagate on the full dev set this week and sent the test-set submission. Dev set, all 1,534 questions, BIRD's own evaluator: 77.12% execution accuracy (simple 80.97, moderate 71.34, challenging 71.03), with Claude Opus 5.5. What makes that number interesting is the cost. Per question: schemagate reflects the database and picks the tables the question needs; the model sees only those tables' DD…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/771-on-bird-dev-with-one-model-call-per-question-and-a-test-set-submission-in-5g6p

## Related notes
- [[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
