---
title: Part 11 - Dimensions and Fact Table 📊
date: '2026-04-21'
source: https://dev.to/abdelrahman_adnan/part-11-dimensions-and-fact-table-9cn
domain: Tableau
relevance: 🟡
tags:
- '#sql'
- '#tableau'
- '#tutorial'
related:
- '[[2026-04-21-part-12---superset-seeding-and-dashboards]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-04-learning-how-to-use-windows-sql-functions-and-joins-in-relational-databases]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-20-postgresql-constraints]]'
- '[[2026-03-10-joins-window-functions]]'
status: unread
---

> **TL;DR:** Part 11 - Dimensions and Fact Table 📊 This part continues from the base model and explains the mart layer in dags/air_quality_dbt/models/marts/ . Why the mart layer exists The mart layer is where the analytics shape beco…

## What’s new and why it matters
Part 11 - Dimensions and Fact Table 📊 This part continues from the base model and explains the mart layer in dags/air_quality_dbt/models/marts/ . Why the mart layer exists The mart layer is where the analytics shape becomes obvious. Instead of keeping everything in one large staging table, the project splits the data into a star-schema-style layout. That makes downstream querying simpler and more efficient. The dimension tables The project creates two dimensions: dim_station from dim_station.sql , dim_sensor from dim_sensor.sql . These are deduplicated reference tables. Each one extracts the s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abdelrahman_adnan/part-11-dimensions-and-fact-table-9cn

## Related notes
- [[2026-04-21-part-12---superset-seeding-and-dashboards]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-04-learning-how-to-use-windows-sql-functions-and-joins-in-relational-databases]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-20-postgresql-constraints]]
- [[2026-03-10-joins-window-functions]]
