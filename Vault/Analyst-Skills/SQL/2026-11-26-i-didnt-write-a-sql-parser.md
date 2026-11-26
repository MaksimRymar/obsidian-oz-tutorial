---
title: I didn't write a SQL parser
date: '2026-11-26'
source: https://dev.to/kenhyou/i-didnt-write-a-sql-parser-3g2l
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]'
- '[[2026-10-03-build-a-knowledge-layer-for-sql-agents-with-okf-part-2]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
status: unread
---

> **TL;DR:** My first idea for the data side of Prism fit in one sentence: make a copy of the customer table with the personal columns masked, and let agents read only the copy. That sentence didn't survive the design. What replaced…

## What’s new and why it matters
My first idea for the data side of Prism fit in one sentence: make a copy of the customer table with the personal columns masked, and let agents read only the copy. That sentence didn't survive the design. What replaced it has no masking code in the gateway at all, and no SQL parser either. The gateway passes the agent's query to the database without changing a character. This is part 2 of a series on Prism , the gateway I built so my teammates' AI agents can read company data without seeing personal data. Part 1 covered why a read-only account isn't enough. This part is about the masking. Thr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenhyou/i-didnt-write-a-sql-parser-3g2l

## Related notes
- [[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]
- [[2026-10-03-build-a-knowledge-layer-for-sql-agents-with-okf-part-2]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-10-14-our-free-plan-hides-creators-with-a-window-function-and-the-locked-count-is-the-same-predicate-with-a-not-in-front]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
