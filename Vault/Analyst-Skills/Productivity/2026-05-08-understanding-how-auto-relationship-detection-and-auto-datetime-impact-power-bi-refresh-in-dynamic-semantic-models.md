---
title: Understanding How Auto Relationship Detection and Auto Date/Time Impact Power
  BI Refresh in Dynamic Semantic Models
date: '2026-05-08'
source: https://dev.to/midhun_balakrishnan_7a34d/understanding-how-auto-relationship-detection-and-auto-datetime-impact-power-bi-refresh-in-dynamic-5elc
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#productivity'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-30-7-stripe-webhook-edge-cases-that-break-billing-and-how-to-handle-them]]'
- '[[2026-04-16-from-rpa-to-data-thinking-building-a-high-scale-payment-processing-system]]'
- '[[2026-04-21-mastering-sql-joins-a-practical-guide-for-beginners]]'
- '[[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]'
- '[[2026-03-03-sql-joins-and-window-functions-with-case-example]]'
status: unread
---

> **TL;DR:** While working on a Power BI automation platform using TOM/XMLA and multiple datasources, I faced refresh failures that were difficult to identify initially. Our system dynamically generates tables and relationships at ru…

## What’s new and why it matters
While working on a Power BI automation platform using TOM/XMLA and multiple datasources, I faced refresh failures that were difficult to identify initially. Our system dynamically generates tables and relationships at runtime using JSON metadata. However, the PBIX template already contained predefined relationships and Power BI automatic features such as: Auto relationship detection Auto date/time This created conflicts during refresh. Example: Initially, the PBIX template assumed: Table1 Col1 = relationship key But at runtime, the datasource generated: Table1 Col2 = relationship key Even afte…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/midhun_balakrishnan_7a34d/understanding-how-auto-relationship-detection-and-auto-datetime-impact-power-bi-refresh-in-dynamic-5elc

## Related notes
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-30-7-stripe-webhook-edge-cases-that-break-billing-and-how-to-handle-them]]
- [[2026-04-16-from-rpa-to-data-thinking-building-a-high-scale-payment-processing-system]]
- [[2026-04-21-mastering-sql-joins-a-practical-guide-for-beginners]]
- [[2026-03-08-data-engineers-what-if-your-bigquery-function-could-return-multiple-tables]]
- [[2026-03-03-sql-joins-and-window-functions-with-case-example]]
