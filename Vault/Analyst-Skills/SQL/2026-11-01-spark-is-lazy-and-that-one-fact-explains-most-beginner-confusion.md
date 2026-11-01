---
title: Spark Is Lazy, and That One Fact Explains Most Beginner Confusion
date: '2026-11-01'
source: https://dev.to/k_hunnurjirao_7ea28e971f/spark-is-lazy-and-that-one-fact-explains-most-beginner-confusion-193a
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
status: unread
---

> **TL;DR:** You write five lines of PySpark. You hit run. It finishes in a blink. You think, "wow, that was fast." Then you add .show() at the end, and suddenly everything takes ten seconds. Or worse, an error appears on a line that…

## What’s new and why it matters
You write five lines of PySpark. You hit run. It finishes in a blink. You think, "wow, that was fast." Then you add .show() at the end, and suddenly everything takes ten seconds. Or worse, an error appears on a line that looks completely fine. If this has happened to you, the reason is one idea: Spark is lazy. It doesn't do work when you write a line. It does work when you ask for a result. Once this clicks, a lot of "weird" Spark behaviour stops being weird. Let's see it with real output. I ran everything below with PySpark 4.3.0 in local mode (Java 17, Python 3.14). Nothing fancy, just pip i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/k_hunnurjirao_7ea28e971f/spark-is-lazy-and-that-one-fact-explains-most-beginner-confusion-193a

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
