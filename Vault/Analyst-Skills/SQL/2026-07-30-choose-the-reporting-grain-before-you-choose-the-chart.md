---
title: Choose the Reporting Grain Before You Choose the Chart
date: '2026-07-30'
source: https://dev.to/datplan/choose-the-reporting-grain-before-you-choose-the-chart-cp6
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-06-11-why-text-to-sql-needs-table-relationship-discovery-before-sql-generation]]'
- '[[2026-05-14-your-ai-database-agent-does-not-know-what-revenue-means]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
status: unread
---

> **TL;DR:** A chart can be perfectly formatted and still be wrong. In accounting and operational reporting, the most common cause is not the visual—it is the grain of the data underneath it . Grain means what one row represents. One…

## What’s new and why it matters
A chart can be perfectly formatted and still be wrong. In accounting and operational reporting, the most common cause is not the visual—it is the grain of the data underneath it . Grain means what one row represents. One row might be an invoice, an invoice line, a payment, an account balance at a reporting date, a CRM deal, or a single activity. Those are different business events. When they are treated as interchangeable, totals multiply, dates lose their meaning, and filters answer a different question from the one in the chart title. Start with the business question Before choosing a table…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datplan/choose-the-reporting-grain-before-you-choose-the-chart-cp6

## Related notes
- [[2026-06-11-why-text-to-sql-needs-table-relationship-discovery-before-sql-generation]]
- [[2026-05-14-your-ai-database-agent-does-not-know-what-revenue-means]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
