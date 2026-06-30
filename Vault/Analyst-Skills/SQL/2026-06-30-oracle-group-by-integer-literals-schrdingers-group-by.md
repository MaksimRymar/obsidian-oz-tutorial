---
title: 'Oracle GROUP BY Integer Literals: Schrödinger''s GROUP BY'
date: '2026-06-30'
source: https://dev.to/pawsql/oracle-group-by-integer-literals-schrodingers-group-by-4oe
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-09-pandas-vs-sql-when-to-use-each]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** Recently, PawSQL's SQL parser stumbled on a bizarre edge case. The SQL below ran perfectly fine in an Oracle client — yet PawSQL threw an array-out-of-bounds error during parsing: SELECT category , count ( 1 ) FROM produ…

## What’s new and why it matters
Recently, PawSQL's SQL parser stumbled on a bizarre edge case. The SQL below ran perfectly fine in an Oracle client — yet PawSQL threw an array-out-of-bounds error during parsing: SELECT category , count ( 1 ) FROM products GROUP BY CATEGORY UNION ALL SELECT 23 as category , 100 FROM product_23 GROUP BY 23 The parser tried to map GROUP BY 23 to the 23rd column in the SELECT list — but the SELECT list only had 2 columns. Boom. This raises a deeper question: when you write an integer literal in GROUP BY , is it a column position or a plain constant value? The answer depends on which database — a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pawsql/oracle-group-by-integer-literals-schrodingers-group-by-4oe

## Related notes
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-09-pandas-vs-sql-when-to-use-each]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
