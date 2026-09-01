---
title: Paginating hybrid search on Postgres, and why the obvious fix is worse
date: '2026-08-31'
source: https://dev.to/pavangupta352/paginating-hybrid-search-on-postgres-and-why-the-obvious-fix-is-worse-2kmd
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** If you have built hybrid search on Postgres, your query probably looks close to this. One CTE ranks by vector distance, one ranks by ts_rank_cd , and Reciprocal Rank Fusion combines the two rankings. with vector_candidat…

## What’s new and why it matters
If you have built hybrid search on Postgres, your query probably looks close to this. One CTE ranks by vector distance, one ranks by ts_rank_cd , and Reciprocal Rank Fusion combines the two rankings. with vector_candidates as ( select id , row_number () over ( order by embedding <=> $ 1 ) as rank from documents order by embedding <=> $ 1 limit 50 ), text_candidates as ( select id , row_number () over ( order by ts_rank_cd ( fts , query ) desc ) as rank from documents , websearch_to_tsquery ( 'english' , $ 2 ) query where fts @@ query order by ts_rank_cd ( fts , query ) desc limit 50 ) select c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pavangupta352/paginating-hybrid-search-on-postgres-and-why-the-obvious-fix-is-worse-2kmd

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
