---
title: Tattoo data taught me to delete every third-party script — and build analytics
  from a SQLite table
date: '2026-08-18'
source: https://dev.to/sike_ren_f38951df83469817/tattoo-data-taught-me-to-delete-every-third-party-script-and-build-analytics-from-a-sqlite-table-7ng
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-14-funnel-analysis-in-sql-find-exactly-where-users-drop-off]]'
- '[[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]'
- '[[2026-06-20-customer-facing-analytics-what-your-saas-app-is-missing-and-how-to-add-it]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** The post is a casual chain, not a product pitch. Blackwork is only the evidence. A tattoo booking is one of the most sensitive payloads a web app can touch. Not in the "payment card" sense — in the body sense. The bookin…

## What’s new and why it matters
The post is a casual chain, not a product pitch. Blackwork is only the evidence. A tattoo booking is one of the most sensitive payloads a web app can touch. Not in the "payment card" sense — in the body sense. The booking form asks for placement (which arm, which rib), size, reference photos, a deposit amount, and a phone number. That's more personally identifying than a bank transfer: it describes a body and a plan to permanently modify it. I built Blackwork , a booking/deposit/CRM system for tattoo studios. The studio's clients submit that data. And the default SaaS stack would have handed a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sike_ren_f38951df83469817/tattoo-data-taught-me-to-delete-every-third-party-script-and-build-analytics-from-a-sqlite-table-7ng

## Related notes
- [[2026-08-14-funnel-analysis-in-sql-find-exactly-where-users-drop-off]]
- [[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]
- [[2026-06-20-customer-facing-analytics-what-your-saas-app-is-missing-and-how-to-add-it]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
