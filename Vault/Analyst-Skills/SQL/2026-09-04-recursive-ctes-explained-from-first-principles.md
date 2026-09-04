---
title: Recursive CTEs, explained from first principles
date: '2026-09-04'
source: https://dev.to/sophiemwangi/recursive-ctes-explained-from-first-principles-295c
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-07-30-how-to-write-a-cohort-retention-query-in-sql-that-actually-runs]]'
status: unread
---

> **TL;DR:** Some data isn't flat. An employee has a manager, who has a manager, who has a manager, all the way up to the boss at the top. A comment can be a reply to a reply to a reply. A folder can sit inside a folder inside a fold…

## What’s new and why it matters
Some data isn't flat. An employee has a manager, who has a manager, who has a manager, all the way up to the boss at the top. A comment can be a reply to a reply to a reply. A folder can sit inside a folder inside a folder. This kind of data, where things are connected in layers or "levels," is called hierarchical data. Think of a family tree, or the folders on your computer. Each item points up (or down) to another item of the same kind. The tricky part: you never know ahead of time how many layers deep the chain goes. One employee might be 2 levels from the top, another might be 6. A recursi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sophiemwangi/recursive-ctes-explained-from-first-principles-295c

## Related notes
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-07-30-how-to-write-a-cohort-retention-query-in-sql-that-actually-runs]]
