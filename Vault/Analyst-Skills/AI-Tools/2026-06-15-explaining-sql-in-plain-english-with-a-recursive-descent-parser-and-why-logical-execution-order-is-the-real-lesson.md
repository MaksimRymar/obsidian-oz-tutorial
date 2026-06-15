---
title: Explaining SQL in Plain English with a Recursive-Descent Parser — and Why Logical
  Execution Order Is the Real Lesson
date: '2026-06-15'
source: https://dev.to/sendotltd/explaining-sql-in-plain-english-with-a-recursive-descent-parser-and-why-logical-execution-order-35lg
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]'
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
status: unread
---

> **TL;DR:** "What does this SQL actually do?" — you could paste it into an LLM, but then it won't work offline, it ships your schema to a third party, and it drifts between runs. I wrote a deterministic explainer instead: a hand-wri…

## What’s new and why it matters
"What does this SQL actually do?" — you could paste it into an LLM, but then it won't work offline, it ships your schema to a third party, and it drifts between runs. I wrote a deterministic explainer instead: a hand-written tokenizer + recursive-descent parser for a subset of SQL SELECT , turning the AST into a plain-language, step-by-step explanation (Japanese or English). Two implementation hinges: (1) expressing operator precedence — AND binds tighter than OR — through the recursive-descent call hierarchy , and (2) narrating the explanation in logical execution order (FROM → WHERE → GROUP…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sendotltd/explaining-sql-in-plain-english-with-a-recursive-descent-parser-and-why-logical-execution-order-35lg

## Related notes
- [[2026-03-12-sql-join-tutorial-inner-left-right-full-outer-explained]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
