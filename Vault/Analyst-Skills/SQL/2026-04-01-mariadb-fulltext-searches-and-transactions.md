---
title: MariaDB FULLTEXT searches and transactions
date: '2026-04-01'
source: https://dev.to/fleetfootmike/mariadb-fulltext-searches-and-transactions-552o
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-27-postgresql-has-a-free-relational-database-json-full-text-search-and-extensions]]'
- '[[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
- '[[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-02-27-orms-are-a-lie-we-tell-junior-developers-so-they-dont-have-to-learn-sql]]'
status: unread
---

> **TL;DR:** Another in a series of "things I had to learn the hard way, and you shouldn't". The key takeaway from this is that MariaDB FULLTEXT search indices are not updated until a transaction is COMMIT'ed. Allow me to demonstrate…

## What’s new and why it matters
Another in a series of "things I had to learn the hard way, and you shouldn't". The key takeaway from this is that MariaDB FULLTEXT search indices are not updated until a transaction is COMMIT'ed. Allow me to demonstrate: MariaDB [ fulltext_demo ] > create table text_data ( -> id serial , info text ); Query OK , 0 rows affected ( 0 . 022 sec ) MariaDB [ fulltext_demo ] > CREATE FULLTEXT INDEX -> ft_idx on text_data ( info ); Now we have a table fulltext_demo with a row info indexed for a fulltext search. And just to prove it: MariaDB [ fulltext_demo ] > insert into text_data set info = "banana…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fleetfootmike/mariadb-fulltext-searches-and-transactions-552o

## Related notes
- [[2026-03-27-postgresql-has-a-free-relational-database-json-full-text-search-and-extensions]]
- [[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
- [[2026-03-09-the-sql-query-that-ruined-my-weekend-and-what-i-built-to-prevent-it]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-02-27-orms-are-a-lie-we-tell-junior-developers-so-they-dont-have-to-learn-sql]]
