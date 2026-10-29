---
title: Your deletion tracker may be counting collection failures
date: '2026-10-29'
source: https://dev.to/dataspryva/your-deletion-tracker-may-be-counting-collection-failures-1cff
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-10-26-building-a-reliable-python-client-for-an-async-api]]'
- '[[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Your change log says a broadcast disappeared, and that count is heading into a report. Now you've to defend whether the broadcast was deleted or your collection failed. The suspicious line is usually innocent-looking: WH…

## What’s new and why it matters
Your change log says a broadcast disappeared, and that count is heading into a report. Now you've to defend whether the broadcast was deleted or your collection failed. The suspicious line is usually innocent-looking: WHERE type = 'broadcast' . It keeps the entities you want to analyse and removes the evidence you need to explain their absence. Our broadcast Actor emits status rows for invalid links, unsupported share links, Spaces, deleted broadcasts and rate limits. A missing broadcast row does not establish that the broadcast was deleted. The missing row has another explanation A broadcast-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataspryva/your-deletion-tracker-may-be-counting-collection-failures-1cff

## Related notes
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-10-26-building-a-reliable-python-client-for-an-async-api]]
- [[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
