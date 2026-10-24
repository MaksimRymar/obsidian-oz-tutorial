---
title: What one month of public benchmarks says about my text-to-SQL access layer
date: '2026-10-24'
source: https://dev.to/ashish_sinha_5241c7673d93/what-one-month-of-public-benchmarks-says-about-my-text-to-sql-access-layer-4n91
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
related:
- '[[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]'
- '[[2026-10-22-771-on-bird-dev-with-one-model-call-per-question-and-a-test-set-submission-in]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-10-17-i-ran-my-text-to-sql-access-control-on-a-benchmark-i-didnt-write]]'
- '[[2026-09-12-every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** schemagate is an open-source layer for text-to-SQL that starts from one question: what is this caller allowed to see? It shows the model only the tables the current user may read, before any SQL is written, reads the per…

## What’s new and why it matters
schemagate is an open-source layer for text-to-SQL that starts from one question: what is this caller allowed to see? It shows the model only the tables the current user may read, before any SQL is written, reads the permissions from your database's own grants, and refuses a query that touches anything else before it reaches the database. This month I ran it on public benchmarks. Every number below comes from that benchmark's own evaluator, and the predictions are in the repo. Access control RBAC Text-to-SQL (SIGMOD '27): 90.1 AC-F1 , against 88.1 for the paper's best setup with the same model…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/what-one-month-of-public-benchmarks-says-about-my-text-to-sql-access-layer-4n91

## Related notes
- [[2026-10-19-schemagate-tops-bird-mini-dev-in-sqlite-postgresql-and-mysql]]
- [[2026-10-22-771-on-bird-dev-with-one-model-call-per-question-and-a-test-set-submission-in]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-10-17-i-ran-my-text-to-sql-access-control-on-a-benchmark-i-didnt-write]]
- [[2026-09-12-every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
