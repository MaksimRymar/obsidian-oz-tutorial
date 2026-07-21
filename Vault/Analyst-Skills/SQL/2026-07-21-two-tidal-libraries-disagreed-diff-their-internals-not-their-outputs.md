---
title: 'Two tidal libraries disagreed: diff their internals, not their outputs'
date: '2026-07-21'
source: https://dev.to/clarkbw--/two-tidal-libraries-disagreed-diff-their-internals-not-their-outputs-klg
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
status: unread
---

> **TL;DR:** Two tide libraries gave different answers and bisecting by ablation found nothing, because the difference was spread thin across a dozen small terms. Both libraries expose their own per-constituent astronomical argument…

## What’s new and why it matters
Two tide libraries gave different answers and bisecting by ablation found nothing, because the difference was spread thin across a dozen small terms. Both libraries expose their own per-constituent astronomical argument and nodal factors — comparing those instead of the predictions localized it in one probe. Jump to the fix. Second lesson, nearly as valuable: ask which regime your discrepancy was measured in. Ours was measured without re-fitting, and the shipped pipeline re-fits, which made the headline number 4x too scary. I have a small tool, chs-constituents , that fits tidal- current harmo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/clarkbw--/two-tidal-libraries-disagreed-diff-their-internals-not-their-outputs-klg

## Related notes
- [[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
