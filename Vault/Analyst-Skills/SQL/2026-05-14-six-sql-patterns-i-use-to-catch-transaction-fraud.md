---
title: Six SQL patterns I use to catch transaction fraud
date: '2026-05-14'
source: https://dev.to/fixelsmith/six-sql-patterns-i-use-to-catch-transaction-fraud-coc
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
status: unread
---

> **TL;DR:** Quick disclaimer: I do data work on a program-integrity team. Examples below use generic transaction tables and made-up scenarios. Nothing here comes from anything I've actually worked on or seen. Views are mine, not my…

## What’s new and why it matters
Quick disclaimer: I do data work on a program-integrity team. Examples below use generic transaction tables and made-up scenarios. Nothing here comes from anything I've actually worked on or seen. Views are mine, not my employer's. Fraud detection in transaction data is mostly SQL. Not machine learning, not graph databases, not whatever Gartner is hyping this year. SQL, run against the right tables, with the right joins, looking for the right shapes. I work mostly with government-funded benefit programs, but the patterns below port over to anything with a transactions table: credit cards, heal…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fixelsmith/six-sql-patterns-i-use-to-catch-transaction-fraud-coc

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
