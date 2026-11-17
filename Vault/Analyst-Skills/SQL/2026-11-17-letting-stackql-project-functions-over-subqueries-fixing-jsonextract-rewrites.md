---
title: 'Letting StackQL Project Functions Over Subqueries: Fixing JSON_EXTRACT Rewrites'
date: '2026-11-17'
source: https://dev.to/prilog/letting-stackql-project-functions-over-subqueries-fixing-jsonextract-rewrites-o51
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-11-17-when-isnt-a-format-verb-fixing-like-patterns-in-stackql-views]]'
- '[[2026-11-10-ensuring-type-safe-database-queries-and-migrations-with-node]]'
- '[[2026-06-25-oracle-ora-00998-error-causes-and-solutions-complete-guide]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-08-26-sql-taught-me-that-there-is-always-an-easier-way-to-do-things]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
status: unread
---

> **TL;DR:** A rewriter that tried to resolve every projection as a column, even when it was a function. Short answer Selecting an expression such as JSON_EXTRACT(contact_method, '$.html_url') from a subquery failed in StackQL with "…

## What’s new and why it matters
A rewriter that tried to resolve every projection as a column, even when it was a function. Short answer Selecting an expression such as JSON_EXTRACT(contact_method, '$.html_url') from a subquery failed in StackQL with "query rewriting for indirection: cannot find col". The rewriter only let through projections that looked like json_each values or OR expressions; everything else had to match a subquery column by name. The fix treats any projection that isn't a bare column reference as an expression and passes it to the SQL backend. Bare column names that don't exist still error as before. It w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/prilog/letting-stackql-project-functions-over-subqueries-fixing-jsonextract-rewrites-o51

## Related notes
- [[2026-11-17-when-isnt-a-format-verb-fixing-like-patterns-in-stackql-views]]
- [[2026-11-10-ensuring-type-safe-database-queries-and-migrations-with-node]]
- [[2026-06-25-oracle-ora-00998-error-causes-and-solutions-complete-guide]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-08-26-sql-taught-me-that-there-is-always-an-easier-way-to-do-things]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
