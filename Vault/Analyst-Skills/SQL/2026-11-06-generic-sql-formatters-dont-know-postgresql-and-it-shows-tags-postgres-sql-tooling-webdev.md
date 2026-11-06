---
title: 'Generic SQL formatters don''t know PostgreSQL, and it shows Tags: postgres,
  sql, tooling, webdev'
date: '2026-11-06'
source: https://dev.to/webgaudi/generic-sql-formatters-dont-know-postgresql-and-it-shows-tags-postgres-sql-tooling-webdev-31op
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-23-following-foreign-keys-in-dbeaver-pgadmin-or-intellij-one-row-at-a-time]]'
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
status: unread
---

> **TL;DR:** Paste a Postgres query into a random online SQL formatter and most of the time it looks fine. Then you hit the one with a cast, a JSON operator or a function body, and the layout goes strange. There is rarely an error. Y…

## What’s new and why it matters
Paste a Postgres query into a random online SQL formatter and most of the time it looks fine. Then you hit the one with a cast, a JSON operator or a function body, and the layout goes strange. There is rarely an error. You just get id::text split across two lines, or meta ->> 'plan' laid out like three unrelated tokens. The reason is that a formatter doesn't understand SQL. It tokenises the text and lays out the tokens. PostgreSQL bends the token rules in more places than MySQL or SQL Server, so a tokeniser built for "SQL in general" trips over everyday Postgres. The constructs that break Thes…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/webgaudi/generic-sql-formatters-dont-know-postgresql-and-it-shows-tags-postgres-sql-tooling-webdev-31op

## Related notes
- [[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-23-following-foreign-keys-in-dbeaver-pgadmin-or-intellij-one-row-at-a-time]]
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
