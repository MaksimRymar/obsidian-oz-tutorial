---
title: In information_schema, a generated column looks exactly like a plain one
date: '2026-06-29'
source: https://dev.to/hitoshi1964/in-informationschema-a-generated-column-looks-exactly-like-a-plain-one-499c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** I was rendering a \d -style column list — name, type, nullable, default — straight off information_schema.columns . Clean, portable, boring. Then I pointed it at a table with a generated column and the view was quietly,…

## What’s new and why it matters
I was rendering a \d -style column list — name, type, nullable, default — straight off information_schema.columns . Clean, portable, boring. Then I pointed it at a table with a generated column and the view was quietly, confidently wrong. The generated column showed up as a perfectly ordinary column. Type: fine. Nullable: fine. Default: NULL . No hint anywhere that the value is computed , not stored. If you trusted my panel, you'd think you could just write to it. CREATE TABLE orders ( qty int , price numeric , total numeric GENERATED ALWAYS AS ( qty * price ) STORED ); SELECT column_name , da…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hitoshi1964/in-informationschema-a-generated-column-looks-exactly-like-a-plain-one-499c

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
