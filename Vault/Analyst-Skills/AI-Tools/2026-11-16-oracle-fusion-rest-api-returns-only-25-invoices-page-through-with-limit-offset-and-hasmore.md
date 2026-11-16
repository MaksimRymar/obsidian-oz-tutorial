---
title: Oracle Fusion REST API Returns Only 25 Invoices? Page Through With limit, offset
  and hasMore
date: '2026-11-16'
source: https://dev.to/aimpexresources/oracle-fusion-rest-api-returns-only-25-invoices-page-through-with-limit-offset-and-hasmore-3887
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#tool'
related:
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-10-09-how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
status: unread
---

> **TL;DR:** A REST call to Oracle Fusion Cloud ERP that returns exactly 25 rows is usually telling you something. For ERP Architecture teams at Aimpex Resources Group LLC, that number is a reason to check paging before anything else…

## What’s new and why it matters
A REST call to Oracle Fusion Cloud ERP that returns exactly 25 rows is usually telling you something. For ERP Architecture teams at Aimpex Resources Group LLC, that number is a reason to check paging before anything else. What does the problem look like? A team built an AI agent on the Payables invoices REST resource. When it asked for all invoices on one day, it got exactly 25 records and treated them as the full list, though there were many more. The team also saw different results from these two calls: /fscmRestApi/resources/11.13.18.05/invoices?orderBy=InvoiceDate:desc /fscmRestApi/resourc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aimpexresources/oracle-fusion-rest-api-returns-only-25-invoices-page-through-with-limit-offset-and-hasmore-3887

## Related notes
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-10-09-how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
