---
title: Don't put an LLM in charge of your production database
date: '2026-09-04'
source: https://dev.to/aniketsoni/dont-put-an-llm-in-charge-of-your-production-database-1o9e
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-13-text-to-sql-is-only-as-safe-as-the-layer-underneath-it]]'
- '[[2026-07-31-why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
status: unread
---

> **TL;DR:** Last June, a junior analyst pushed a "helpful" GenAI assistant to our internal Tableau-connected lakehouse. Within forty minutes, the agent generated a SELECT * across a 40-terabyte partitioned table joined against a cro…

## What’s new and why it matters
Last June, a junior analyst pushed a "helpful" GenAI assistant to our internal Tableau-connected lakehouse. Within forty minutes, the agent generated a SELECT * across a 40-terabyte partitioned table joined against a cross-region S3 bucket. The query didn't just fail; it locked the Databricks SQL Warehouse, blew our monthly compute budget in a single afternoon, and triggered a PagerDuty incident that ruined my kid’s birthday dinner. That query cost us $4,200 in DBU burn and an hour of downtime for our actual business stakeholders. Why I chose this topic: I’m tired of seeing engineers treat Tex…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aniketsoni/dont-put-an-llm-in-charge-of-your-production-database-1o9e

## Related notes
- [[2026-08-13-text-to-sql-is-only-as-safe-as-the-layer-underneath-it]]
- [[2026-07-31-why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
