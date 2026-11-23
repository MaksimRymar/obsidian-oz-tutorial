---
title: Odoo filestore too big? Find out what is filling it before you delete anything
date: '2026-11-23'
source: https://dev.to/atelier_rs_4b1759b9f9cdc1/odoo-filestore-too-big-find-out-what-is-filling-it-before-you-delete-anything-33me
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-11-23-5-mysql-explain-signals-that-tell-you-exactly-why-your-query-is-slow]]'
- '[[2026-10-30-your-model-archive-can-carry-a-program-check-members-by-their-bytes]]'
status: unread
---

> **TL;DR:** Your Odoo filestore keeps growing, backups take longer, and someone asks "can we just delete old attachments?". Before you compress, move or delete anything, answer one question: which records, which file types and which…

## What’s new and why it matters
Your Odoo filestore keeps growing, backups take longer, and someone asks "can we just delete old attachments?". Before you compress, move or delete anything, answer one question: which records, which file types and which years account for the space? Usually two or three sources explain most of it, and the right fix depends on which ones. This is read-only work. You only need psql access to the database (self-hosted, or the Odoo.sh shell). 1. How Odoo stores attachments (what you need to know) Each attachment is a row in ir_attachment . When type = 'binary' and the file is not in the database,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/atelier_rs_4b1759b9f9cdc1/odoo-filestore-too-big-find-out-what-is-filling-it-before-you-delete-anything-33me

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-11-23-5-mysql-explain-signals-that-tell-you-exactly-why-your-query-is-slow]]
- [[2026-10-30-your-model-archive-can-carry-a-program-check-members-by-their-bytes]]
