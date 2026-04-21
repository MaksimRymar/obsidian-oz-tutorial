---
title: Part 10 - Base Model and Data Quality ✅
date: '2026-04-21'
source: https://dev.to/abdelrahman_adnan/part-10-base-model-and-data-quality-54b9
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-04-21-part-11---dimensions-and-fact-table]]'
- '[[2026-04-21-part-12---superset-seeding-and-dashboards]]'
- '[[2026-03-16-how-to-extract-text-from-pdf-in-python-2026]]'
- '[[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-04-20-how-my-journey-has-been-into-understanding-sql]]'
status: unread
---

> **TL;DR:** Part 10 - Base Model and Data Quality ✅ This part continues from the dbt setup and looks at the base layer in dags/air_quality_dbt/models/base/base_air_quality.sql and dags/air_quality_dbt/models/base/schema.yml . The ba…

## What’s new and why it matters
Part 10 - Base Model and Data Quality ✅ This part continues from the dbt setup and looks at the base layer in dags/air_quality_dbt/models/base/base_air_quality.sql and dags/air_quality_dbt/models/base/schema.yml . The base model The base model is a view over the staging table. It selects the core fields needed by downstream models: station identifiers, sensor identifiers, measurement values, coordinates, weather context, and time partitions. This layer is the place where the project standardizes the source before turning it into marts. Why a view makes sense here A base view is a good fit beca…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abdelrahman_adnan/part-10-base-model-and-data-quality-54b9

## Related notes
- [[2026-04-21-part-11---dimensions-and-fact-table]]
- [[2026-04-21-part-12---superset-seeding-and-dashboards]]
- [[2026-03-16-how-to-extract-text-from-pdf-in-python-2026]]
- [[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-04-20-how-my-journey-has-been-into-understanding-sql]]
