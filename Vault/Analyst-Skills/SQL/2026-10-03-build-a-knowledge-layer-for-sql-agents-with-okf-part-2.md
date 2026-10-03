---
title: Build a Knowledge Layer for SQL Agents with OKF (Part 2)
date: '2026-10-03'
source: https://dev.to/lakhan_malviya_09d3c6dbcb/build-a-knowledge-layer-for-sql-agents-with-okf-part-2-2c34
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-10-03-turn-database-docs-into-agent-ready-knowledge-okf-series-part-3]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** You connect an AI agent to your shop's database and ask a simple question: "How many active customers do we have?" The agent looks at the tables: customers (customer_id, name, status, created_at) orders (order_id, custom…

## What’s new and why it matters
You connect an AI agent to your shop's database and ask a simple question: "How many active customers do we have?" The agent looks at the tables: customers (customer_id, name, status, created_at) orders (order_id, customer_id, amount, paid, ordered_at) It spots a status column with the value 'active' , writes a query, and gives you a number in two seconds: SELECT COUNT ( * ) FROM customers WHERE status = 'active' ; The number is wrong. In your company, status = 'active' only means the account hasn't been closed. When finance says "active customer", they mean someone who placed a paid order in…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lakhan_malviya_09d3c6dbcb/build-a-knowledge-layer-for-sql-agents-with-okf-part-2-2c34

## Related notes
- [[2026-10-03-turn-database-docs-into-agent-ready-knowledge-okf-series-part-3]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
