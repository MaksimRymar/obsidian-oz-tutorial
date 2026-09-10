---
title: UTC Offsets Are Not Integers — A Remote Job Feed With 5.75 In It
date: '2026-09-10'
source: https://dev.to/devil_scrapes/utc-offsets-are-not-integers-a-remote-job-feed-with-575-in-it-5537
domain: Python
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** Quick answer UTC offsets are not integers. If you model a remote job's timezone requirement as list[int] , you will crash or silently truncate on every role that accepts candidates in India (+5:30), Newfoundland (−3:30),…

## What’s new and why it matters
Quick answer UTC offsets are not integers. If you model a remote job's timezone requirement as list[int] , you will crash or silently truncate on every role that accepts candidates in India (+5:30), Newfoundland (−3:30), Nepal (+5:45), Adelaide (+9:30) or the Marquesas (−9:30). The Himalayas remote-jobs API returns these as JSON numbers in a timezoneRestrictions array, and a live pull right now shows 37 distinct offsets, six of them fractional : -9.5, -3.5, 3.5, 4.5, 5.5, 5.75 . The correct type is a float — and 5.75 is the one that catches people who "fixed" it by switching to half-hour steps…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/utc-offsets-are-not-integers-a-remote-job-feed-with-575-in-it-5537

## Related notes
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
