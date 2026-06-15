---
title: SELECT MAX()+1 Is a Race Condition Waiting to Happen
date: '2026-06-15'
source: https://dev.to/mattia_armas/select-max1-is-a-race-condition-waiting-to-happen-22m2
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]'
- '[[2026-04-13-typescript-knows-your-sql-is-broken-before-your-tests-even-run]]'
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** This is a story in three acts about one of the most innocent-looking patterns in backend code: generating the next number in a sequence. It passed every test. It ran fine for months. Then a unique-index violation showed…

## What’s new and why it matters
This is a story in three acts about one of the most innocent-looking patterns in backend code: generating the next number in a sequence. It passed every test. It ran fine for months. Then a unique-index violation showed up in production logs, and the fix I reached for first didn't actually fix it. Act 1: The code that looks correct The requirement was a per-customer progressive number — ORD-1 , ORD-2 , and so on. The implementation read like plain English: var existing = await db . Orders . Where ( o => o . CustomerId == customerId ) . ToListAsync (); var next = existing . Select ( o => ParseP…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mattia_armas/select-max1-is-a-race-condition-waiting-to-happen-22m2

## Related notes
- [[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]
- [[2026-04-13-typescript-knows-your-sql-is-broken-before-your-tests-even-run]]
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
