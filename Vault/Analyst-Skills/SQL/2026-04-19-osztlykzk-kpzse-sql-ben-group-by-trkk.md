---
title: Osztályközök képzése SQL-ben (GROUP BY trükk)
date: '2026-04-19'
source: https://dev.to/kovoliver/osztalykozos-lekerdezes-sql-lel-36d
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]'
- '[[2026-03-15-sql-for-generating-test-data-in-mysql]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
- '[[2026-03-27-postgresql-has-a-free-relational-database-json-full-text-search-and-extensions]]'
- '[[2026-03-15-materialization-strategies-how-bruin-and-dbt-turn-select-queries-into-tables]]'
- '[[2026-03-27-cockroachdb-has-a-free-distributed-sql-database-with-postgresql-compatibility]]'
status: unread
---

> **TL;DR:** Ebben a rendkívül rövid blogbejegyzésben arról fogok értekezni, hogyan lehet osztályközös lekérdezést létrehozni SQL nyelven. A példához MSSQL-t használok majd, de mivel az SQL szintaxisok nagyon hasonlóak, így ezt bárme…

## What’s new and why it matters
Ebben a rendkívül rövid blogbejegyzésben arról fogok értekezni, hogyan lehet osztályközös lekérdezést létrehozni SQL nyelven. A példához MSSQL-t használok majd, de mivel az SQL szintaxisok nagyon hasonlóak, így ezt bármelyik SQL dialektusban meg lehet oldani. Itt is van a mérhetetlenül egyszerű lekérdezés: SELECT amount / 200000 * 200000 AS BinStart , amount / 200000 * 200000 + 199999 AS BinEnd , COUNT ( * ) AS Count FROM Salaries WHERE end_date IS NULL GROUP BY amount / 200000 ; A tábla maga így néz ki: CREATE TABLE Salaries ( salary_id int PRIMARY KEY IDENTITY ( 1 , 1 ), employee_id int , am…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kovoliver/osztalykozos-lekerdezes-sql-lel-36d

## Related notes
- [[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]
- [[2026-03-15-sql-for-generating-test-data-in-mysql]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
- [[2026-03-27-postgresql-has-a-free-relational-database-json-full-text-search-and-extensions]]
- [[2026-03-15-materialization-strategies-how-bruin-and-dbt-turn-select-queries-into-tables]]
- [[2026-03-27-cockroachdb-has-a-free-distributed-sql-database-with-postgresql-compatibility]]
