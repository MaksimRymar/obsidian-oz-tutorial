---
title: 'The FETCH FIRST story: from ROW_NUMBER() in 12c back to ROWNUM in 23ai, and
  a LIMIT equivalent for PostgreSQL'
date: '2026-10-04'
source: https://dev.to/franckpachot/the-oracle-fetch-first-story-from-rownumber-in-12c-back-to-rownum-in-23ai-525e
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-29-sql-assertions-ansi-join-and-ora-08697]]'
status: unread
---

> **TL;DR:** The FETCH FIRST ... ROWS ONLY clause arrived in the SQL standard with SQL:2008, and Oracle Database implemented it in 12cR1, released in June 2013. Before that, there were two common ways to write a Top-N query, both req…

## What’s new and why it matters
The FETCH FIRST ... ROWS ONLY clause arrived in the SQL standard with SQL:2008, and Oracle Database implemented it in 12cR1, released in June 2013. Before that, there were two common ways to write a Top-N query, both requiring a subquery: Order the rows first, then apply ROWNUM outside: SELECT * FROM ( SELECT ... FROM ... ORDER BY ... ) WHERE ROWNUM <= 42 ; Calculate an analytic ROW_NUMBER() , then filter its result outside: SELECT * FROM ( SELECT ..., ROW_NUMBER () OVER ( ORDER BY ...) AS rn FROM ... ) WHERE rn <= 42 ; The first subquery is necessary because the ordering must happen before th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/franckpachot/the-oracle-fetch-first-story-from-rownumber-in-12c-back-to-rownum-in-23ai-525e

## Related notes
- [[2026-09-07-sql-for-beginners-window-functions-vs-group-by]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-29-sql-assertions-ansi-join-and-ora-08697]]
