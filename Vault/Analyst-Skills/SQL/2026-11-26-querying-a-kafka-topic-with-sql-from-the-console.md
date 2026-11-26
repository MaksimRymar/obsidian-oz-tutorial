---
title: Querying a Kafka topic with SQL, from the console
date: '2026-11-26'
source: https://dev.to/alginte/querying-a-kafka-topic-with-sql-from-the-console-467m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-15-sql-joins-explained]]'
status: unread
---

> **TL;DR:** Sooner or later, everyone who works with Kafka asks a topic a question. How many orders came in for this customer? Which records have no match in the other topic? What did this partition receive in the last hour? A messa…

## What’s new and why it matters
Sooner or later, everyone who works with Kafka asks a topic a question. How many orders came in for this customer? Which records have no match in the other topic? What did this partition receive in the last hour? A message browser shows the records one by one. It does not count them, sum them or match them against anything. The usual answer is a consumer. You write a small program, point it at the topic, deserialize the records and add them up. Or you run a stream processor such as ksqlDB, on a server or a cluster of its own. There you declare a table over the topic before the first query. Eit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alginte/querying-a-kafka-topic-with-sql-from-the-console-467m

## Related notes
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-15-sql-joins-explained]]
