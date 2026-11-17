---
title: 'When % Isn''t a Format Verb: Fixing LIKE Patterns in StackQL Views'
date: '2026-11-17'
source: https://dev.to/prilog/when-isnt-a-format-verb-fixing-like-patterns-in-stackql-views-ic5
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-11-15-the-one-line-sql-query-that-broke-code-review]]'
- '[[2026-04-14-how-i-built-a-real-world-automation-tool-in-python-step-by-step]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-03-the-batch-api-that-hid-its-failures-a-take-home-packet-for-ai-reviewers]]'
- '[[2026-06-02-the-data-engineering-take-home-assessment-how-to-turn-a-4-hour-test-into-a-job-offer]]'
status: unread
---

> **TL;DR:** User SQL passed through fmt.Sprintf , where every % means something. Short answer StackQL builds the final SQL for views and subqueries by substituting the inner query into a template with fmt.Sprintf . A LIKE '%TLS12%'…

## What’s new and why it matters
User SQL passed through fmt.Sprintf , where every % means something. Short answer StackQL builds the final SQL for views and subqueries by substituting the inner query into a template with fmt.Sprintf . A LIKE '%TLS12%' pattern in a query on a view therefore contained characters that Go read as format verbs, and the result failed with sql packet preparation error: near "(": syntax error . The fix replaces the printf-based substitution with explicit placeholder tokens and a literal-safe expander. It was merged as PR #723 and closed issue #472 . The problem Issue #472, opened in October 2024, sh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/prilog/when-isnt-a-format-verb-fixing-like-patterns-in-stackql-views-ic5

## Related notes
- [[2026-11-15-the-one-line-sql-query-that-broke-code-review]]
- [[2026-04-14-how-i-built-a-real-world-automation-tool-in-python-step-by-step]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-03-the-batch-api-that-hid-its-failures-a-take-home-packet-for-ai-reviewers]]
- [[2026-06-02-the-data-engineering-take-home-assessment-how-to-turn-a-4-hour-test-into-a-job-offer]]
