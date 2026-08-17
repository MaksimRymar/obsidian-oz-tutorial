---
title: 'Exactly-Once Semantics in Streaming: Idempotency, Transactions & Two-Phase-Commit
  Sinks'
date: '2026-08-16'
source: https://dev.to/gowthampotureddi/exactly-once-semantics-in-streaming-idempotency-transactions-two-phase-commit-sinks-3npa
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-08-16-windowing-in-stream-processing-tumbling-hopping-session-global-windows]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** exactly-once semantics is the phrase that ends more streaming design reviews in an argument than any other, because almost everyone repeats the marketing line ("this system gives you exactly-once!") and almost no one can…

## What’s new and why it matters
exactly-once semantics is the phrase that ends more streaming design reviews in an argument than any other, because almost everyone repeats the marketing line ("this system gives you exactly-once!") and almost no one can say what actually happens to a single record when a worker crashes halfway through processing it. The honest version is less magical and far more useful: a real streaming system still delivers a record more than once on failure — the network and the two-generals problem guarantee that — but it arranges for the duplicate delivery to have no duplicate effect . That is the whole…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/exactly-once-semantics-in-streaming-idempotency-transactions-two-phase-commit-sinks-3npa

## Related notes
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-08-16-windowing-in-stream-processing-tumbling-hopping-session-global-windows]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
