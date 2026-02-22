---
title: 🚨 Why Your SQL Window Functions Betray You in Cloud SSMS vs Snowflake
date: '2026-02-21'
source: https://dev.to/naveena_davay/why-your-sql-window-functions-betray-you-in-cloud-ssms-vs-snowflake-147l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
related:
- '[[2026-02-22-your-ml-model-isnt-wrong-your-sql-probably-is]]'
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]'
- '[[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
status: unread
---

> **TL;DR:** 🚨 Why Your SQL Window Functions Betray You in Cloud SSMS vs Snowflake You run the same query. Same data. Same logic. But your numbers don’t match. Welcome to the sneaky world of window functions — where defaults quietly…

## What’s new and why it matters
🚨 Why Your SQL Window Functions Betray You in Cloud SSMS vs Snowflake You run the same query. Same data. Same logic. But your numbers don’t match. Welcome to the sneaky world of window functions — where defaults quietly change your results between Microsoft SQL Server (Cloud SSMS) and Snowflake. Let’s break down the drama. 🎭 The Silent Villain: Default Window Frames Here’s a classic trap: LAST_VALUE(amount) OVER ( PARTITION BY customer_id ORDER BY order_date ) In Snowflake, the default frame is: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW Translation? LAST_VALUE() returns the current row…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/naveena_davay/why-your-sql-window-functions-betray-you-in-cloud-ssms-vs-snowflake-147l

## Related notes
- [[2026-02-22-your-ml-model-isnt-wrong-your-sql-probably-is]]
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-02-22-how-to-generate-business-leads-using-google-maps-ids-and-python]]
- [[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
