---
title: Automate Odoo Studio Views Migrations
date: '2026-11-05'
source: https://dev.to/kerbrose/automate-odoo-studio-views-migrations-32lo
domain: SQL
relevance: 🔴
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-11-postgresql-42710-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-24-handling-structured-output-with-openai-function-calling]]'
- '[[2026-09-15-how-to-extract-tables-from-word-documents-with-python]]'
- '[[2026-10-14-how-to-turn-google-maps-scraper-output-into-a-scored-local-seo-lead-list]]'
- '[[2026-07-12-the-developers-guide-to-multimodal-ai-apis-in-2026]]'
status: unread
---

> **TL;DR:** The odoo.sh platform doesn’t provide migrations to Odoo studio custom views. It also deactivate such views in the migration process. However a developer could benefit from the migrations directory during such process to…

## What’s new and why it matters
The odoo.sh platform doesn’t provide migrations to Odoo studio custom views. It also deactivate such views in the migration process. However a developer could benefit from the migrations directory during such process to update the views and reactivate it. The migrations directory informs Odoo run the migration scripts which located the matched version with the manifest. as you can see in the following addon directory my_module/ ├── __init__.py ├── __manifest__.py ├── README.rst ├── models/ │ ├── __init__.py │ ├── sale_order.py │ └── res_partner.py ├── security/ │ └── ir.model.access.csv ├── vi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kerbrose/automate-odoo-studio-views-migrations-32lo

## Related notes
- [[2026-07-11-postgresql-42710-error-causes-and-solutions-complete-guide]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-24-handling-structured-output-with-openai-function-calling]]
- [[2026-09-15-how-to-extract-tables-from-word-documents-with-python]]
- [[2026-10-14-how-to-turn-google-maps-scraper-output-into-a-scored-local-seo-lead-list]]
- [[2026-07-12-the-developers-guide-to-multimodal-ai-apis-in-2026]]
