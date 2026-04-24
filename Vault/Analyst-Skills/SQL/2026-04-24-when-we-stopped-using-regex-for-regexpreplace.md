---
title: When we Stopped Using Regex for REGEXP_REPLACE
date: '2026-04-24'
source: https://medium.com/opteryx/when-we-stopped-using-regex-for-regexp-replace-cce38a358893?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-09-sql-is-the-new-regex-using-aiquery-for-real-world-data-cleaning]]'
- '[[2026-03-30-why-i-stopped-manually-masking-data-in-snowflake-and-how-i-used-dbt-to-automate-it-forever]]'
- '[[2026-04-05-sql-conversion-accelerator-ai-powered-ad-hoc-sql-conversion-to-snowflake-using-cortex]]'
- '[[2026-04-08-rethinking-rag-why-i-replaced-vector-databases-with-sql]]'
- '[[2026-03-31-comparing-current-vs-previous-year-values-in-sql-a-practical-guide-for-analysts]]'
- '[[2026-04-21-from-4s-to-400ms-fixing-a-performance-regression-in-code-we-didnt-write]]'
status: unread
---

> **TL;DR:** REGEXP_REPLACE dominated query time. Swapping regex engines didn’t help. We built a specialised DFA instead. Continue reading on Opteryx Engineering »

## What’s new and why it matters
REGEXP_REPLACE dominated query time. Swapping regex engines didn’t help. We built a specialised DFA instead. Continue reading on Opteryx Engineering »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/opteryx/when-we-stopped-using-regex-for-regexp-replace-cce38a358893?source=rss------sql-5

## Related notes
- [[2026-04-09-sql-is-the-new-regex-using-aiquery-for-real-world-data-cleaning]]
- [[2026-03-30-why-i-stopped-manually-masking-data-in-snowflake-and-how-i-used-dbt-to-automate-it-forever]]
- [[2026-04-05-sql-conversion-accelerator-ai-powered-ad-hoc-sql-conversion-to-snowflake-using-cortex]]
- [[2026-04-08-rethinking-rag-why-i-replaced-vector-databases-with-sql]]
- [[2026-03-31-comparing-current-vs-previous-year-values-in-sql-a-practical-guide-for-analysts]]
- [[2026-04-21-from-4s-to-400ms-fixing-a-performance-regression-in-code-we-didnt-write]]
