---
title: An AI-generated login endpoint "works" - I still found SQL concatenation before
  launch
date: '2026-09-10'
source: https://dev.to/yuan_ming_3549dae7e400994/an-ai-generated-login-endpoint-works-i-still-found-sql-concatenation-before-launch-2om8
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-06-03-read-this-before-you-deploy-python-on-railway]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-05-29-build-dynamic-sql-filters-for-joget-reports-with-beanshell]]'
status: unread
---

> **TL;DR:** Functional tests passing is not the same as code being safe to ship. Here is a reproducible case: an AI-generated login endpoint that behaves correctly, the scan finding I checked before launch, and the fix that made the…

## What’s new and why it matters
Functional tests passing is not the same as code being safe to ship. Here is a reproducible case: an AI-generated login endpoint that behaves correctly, the scan finding I checked before launch, and the fix that made the pattern disappear. The code runs, but I would not ship it like this This is a local demo equivalent of a login endpoint, not live production code and not a client project: username = request . form . get ( " username " , "" ) password = request . form . get ( " password " , "" ) sql = f " SELECT id FROM users WHERE username = ' { username } ' AND password = ' { password } '" c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yuan_ming_3549dae7e400994/an-ai-generated-login-endpoint-works-i-still-found-sql-concatenation-before-launch-2om8

## Related notes
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-06-03-read-this-before-you-deploy-python-on-railway]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-05-29-build-dynamic-sql-filters-for-joget-reports-with-beanshell]]
