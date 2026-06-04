---
title: 'SQL DISTINCT + COUNT(DISTINCT): Deduplication, Approximate Counts, HyperLogLog'
date: '2026-06-04'
source: https://dev.to/gowthampotureddi/sql-distinct-countdistinct-deduplication-approximate-counts-hyperloglog-3p1h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
status: unread
---

> **TL;DR:** sql distinct looks like the simplest operator in the language — a one-word switch that strips duplicates from a result set — and that is exactly why it shows up in dozens of production incidents and interview rounds ever…

## What’s new and why it matters
sql distinct looks like the simplest operator in the language — a one-word switch that strips duplicates from a result set — and that is exactly why it shows up in dozens of production incidents and interview rounds every year. The catch is that sql distinct is not free. Behind every SELECT DISTINCT is a sort or a hash aggregation; behind every sql count distinct is a unique-set whose memory cost is O(distinct cardinality) ; behind every dedup pattern is a choice between DISTINCT , GROUP BY , ROW_NUMBER() , and DISTINCT ON that decides whether the query finishes in seconds or grinds the wareho…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/sql-distinct-countdistinct-deduplication-approximate-counts-hyperloglog-3p1h

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
