---
title: Why I am scared of complex nested JSON
date: '2026-10-22'
source: https://dev.to/maksim-gr/why-i-am-scared-of-complex-nested-json-50bk
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-30-dataform-for-bigquery-google-native-transformation-assertions-cicd]]'
status: unread
---

> **TL;DR:** This post isn't about ClickHouse internals. It's about a part of my day-to-day work that kept eating my time. You want to build something great, and instead you sit there struggling to understand what is going on. We con…

## What’s new and why it matters
This post isn't about ClickHouse internals. It's about a part of my day-to-day work that kept eating my time. You want to build something great, and instead you sit there struggling to understand what is going on. We consume a lot of data straight from Kafka into ClickHouse, using ClickHouse's own Kafka consumer (the Kafka table engine) and materialized views. Data is constantly flowing, and the message format keeps changing. Every new topic meant the same job: find a message on the topic and check its fields, write several migrations that have to be applied in a particular order (we use golan…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/maksim-gr/why-i-am-scared-of-complex-nested-json-50bk

## Related notes
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-30-dataform-for-bigquery-google-native-transformation-assertions-cicd]]
