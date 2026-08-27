---
title: I gave an LLM the keys to a multi-tenant database
date: '2026-08-27'
source: https://dev.to/arif_ismailov_6535c00c21c/i-gave-an-llm-the-keys-to-a-multi-tenant-database-5hjc
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Five things that had to be true before I would point it at data belonging to more than one customer. An agent that writes good SQL is a solved problem, near enough. The first half of this project was about that: pulling…

## What’s new and why it matters
Five things that had to be true before I would point it at data belonging to more than one customer. An agent that writes good SQL is a solved problem, near enough. The first half of this project was about that: pulling descriptions, join keys, real filter values and signed-off metric definitions out of dbt and handing them to the model, so the query it writes is the query a competent analyst would have written. None of it makes the query safe. A perfectly grounded query against exactly the right table will return every tenant's rows if nothing stops it, and it will do so without an error, bec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/arif_ismailov_6535c00c21c/i-gave-an-llm-the-keys-to-a-multi-tenant-database-5hjc

## Related notes
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
