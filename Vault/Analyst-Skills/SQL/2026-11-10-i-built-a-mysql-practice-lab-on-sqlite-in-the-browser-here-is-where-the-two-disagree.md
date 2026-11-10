---
title: I built a MySQL practice lab on SQLite in the browser. Here is where the two
  disagree
date: '2026-11-10'
source: https://dev.to/ghosh_srimanta/i-built-a-mysql-practice-lab-on-sqlite-in-the-browser-here-is-where-the-two-disagree-p29
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-11-08-sqlite-error-no-such-column-usually-missing-quotes-plus-4-other-causes]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]'
status: unread
---

> **TL;DR:** I run a small free study site for CBSE Class 11 and 12 students in India. SQL is part of their syllabus, and the syllabus is written around MySQL. The problem: most students practise on a phone or a locked school compute…

## What’s new and why it matters
I run a small free study site for CBSE Class 11 and 12 students in India. SQL is part of their syllabus, and the syllabus is written around MySQL. The problem: most students practise on a phone or a locked school computer, where installing MySQL is not an option. So I built a SQL lab that runs fully in the browser. It uses sql.js (SQLite compiled to WebAssembly) with a translation layer on top, so that students type MySQL and get MySQL-style answers. No server, no login. "SQLite is close enough to MySQL" turned out to be wrong in ways that matter to a beginner. Here are the gaps that cost me t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ghosh_srimanta/i-built-a-mysql-practice-lab-on-sqlite-in-the-browser-here-is-where-the-two-disagree-p29

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-11-08-sqlite-error-no-such-column-usually-missing-quotes-plus-4-other-causes]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]
