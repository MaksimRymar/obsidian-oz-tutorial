---
title: 'SnowLens: Free Snowflake Observability — 9 Detectors, Zero Data Egress'
date: '2026-07-30'
source: https://dev.to/abin_alex_863f65bd6a1a77f/snowlens-free-snowflake-observability-9-detectors-zero-data-egress-1dln
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-06-21-product-analytics-with-sql-tracking-what-actually-matters]]'
status: unread
---

> **TL;DR:** If you run Snowflake in production, you've probably asked yourself: which queries are burning credits? Why did costs spike last Tuesday? Are any warehouses just sitting there idle? Most observability tools answer these q…

## What’s new and why it matters
If you run Snowflake in production, you've probably asked yourself: which queries are burning credits? Why did costs spike last Tuesday? Are any warehouses just sitting there idle? Most observability tools answer these questions by shipping your query logs to an external SaaS — data egress, vendor lock-in, another subscription. SnowLens takes a different approach: it's a Streamlit app that installs directly into your Snowflake account and runs on your own compute. Your data never leaves your environment. And it's completely free. What It Detects — 9 Rules Performance: Slow queries — configurab…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abin_alex_863f65bd6a1a77f/snowlens-free-snowflake-observability-9-detectors-zero-data-egress-1dln

## Related notes
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-06-21-product-analytics-with-sql-tracking-what-actually-matters]]
