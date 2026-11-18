---
title: Where a fixed 90% interval misses by hour
date: '2026-11-18'
source: https://dev.to/widechaos/where-a-fixed-90-interval-misses-by-hour-6oh
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]'
- '[[2026-11-15-what-three-mae-values-on-one-fixed-split-support]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]'
- '[[2026-10-07-when-my-house-price-model-hit-100-accuracy-i-should-have-been-worried]]'
- '[[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]'
status: unread
---

> **TL;DR:** One overall number hides the hourly misses A fixed 90% prediction interval covered 3,894 of 4,258 test hours. The overall rate is 91.4514%, only 1.4514 percentage points from the nominal target. That single number reads…

## What’s new and why it matters
One overall number hides the hourly misses A fixed 90% prediction interval covered 3,894 of 4,258 test hours. The overall rate is 91.4514%, only 1.4514 percentage points from the nominal target. That single number reads as close enough. An operator using intervals makes hour-level decisions, and for staffing or dispatch the 08:00 to 09:00 window matters more than a six-month average. This article answers a descriptive question: where do the 364 missed hours sit in the day, and what can be read from that distribution. The data are the UCI Bike Sharing hourly system-wide rental totals from Washi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/widechaos/where-a-fixed-90-interval-misses-by-hour-6oh

## Related notes
- [[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]
- [[2026-11-15-what-three-mae-values-on-one-fixed-split-support]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]
- [[2026-10-07-when-my-house-price-model-hit-100-accuracy-i-should-have-been-worried]]
- [[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]
