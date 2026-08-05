---
title: 'Scythe: SQL as a first-class typed language (and where that leaves your ORM)'
date: '2026-08-05'
source: https://dev.to/nhirschfeld/scythe-sql-as-a-first-class-typed-language-and-where-that-leaves-your-orm-1fhh
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-08-01-sql-vs-nosql-a-simple-guide-to-picking-the-right-database]]'
- '[[2026-04-16-dominion-observatory-langchain-one-line-trust-telemetry-for-langchain-agents]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
status: unread
---

> **TL;DR:** I build and maintain scythe (MIT). This is the argument behind it: why I think SQL deserves to be treated as a typed language, what that replaces, and the one case where it doesn't. The glue code, and who already solved…

## What’s new and why it matters
I build and maintain scythe (MIT). This is the argument behind it: why I think SQL deserves to be treated as a typed language, what that replaces, and the one case where it doesn't. The glue code, and who already solved it Every application that talks to a database carries a layer of glue: map the parameters in, map the result rows out, keep the types on both sides aligned, and rewrite all of it every time a query or the schema changes. It is tedious, it is where a lot of quiet bugs live, and nobody enjoys maintaining it. sqlc solved this cleanly for Go. You write plain .sql files, it reads yo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/nhirschfeld/scythe-sql-as-a-first-class-typed-language-and-where-that-leaves-your-orm-1fhh

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-08-01-sql-vs-nosql-a-simple-guide-to-picking-the-right-database]]
- [[2026-04-16-dominion-observatory-langchain-one-line-trust-telemetry-for-langchain-agents]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
