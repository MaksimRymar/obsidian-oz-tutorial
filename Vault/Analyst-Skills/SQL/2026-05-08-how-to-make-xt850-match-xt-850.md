---
title: How to Make xt850 Match xt 850
date: '2026-05-08'
source: https://dev.to/sanikolaev/how-to-make-xt850-match-xt-850-o15
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-03-prepared-statements-in-manticore-search]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
status: unread
---

> **TL;DR:** TL;DR Since version 23.0.0 , Manticore can make searches like xt850 match xt 850 using bigram_delimiter together with digit-aware bigram_index modes. This solves a common tokenization mismatch in product search, where us…

## What’s new and why it matters
TL;DR Since version 23.0.0 , Manticore can make searches like xt850 match xt 850 using bigram_delimiter together with digit-aware bigram_index modes. This solves a common tokenization mismatch in product search, where users remove spaces from model names but the source data stores them as separate tokens. Assumptions and verification This article assumes: RT tables created with SQL examples exactly as shown default tokenization unless the example explicitly changes a setting ASCII digits in model names, because second_numeric and second_has_digit are digit-aware modes built around 0-9 All SQL…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sanikolaev/how-to-make-xt850-match-xt-850-o15

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-03-prepared-statements-in-manticore-search]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
