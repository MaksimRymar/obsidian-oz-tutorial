---
title: How I cut Django indexing from 23 minutes to 11 minutes with one SQL change
date: '2026-06-10'
source: https://dev.to/n3mo-dev/how-i-cut-django-indexing-from-23-minutes-to-11-minutes-with-one-sql-change-5of
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-05-11-beyond-basic-indexes-mastering-partial-composite-and-covering-indexes-in-sql]]'
- '[[2026-05-29-your-ai-agent-has-a-memory-problem-owasps-new-defense-against-memory-poisoning]]'
status: unread
---

> **TL;DR:** The problem I'm building N3MO — an open source code intelligence engine that maps Python codebases into a knowledge graph stored in PostgreSQL. When I tested it on Django (3,021 Python files, 181,000+ function calls), th…

## What’s new and why it matters
The problem I'm building N3MO — an open source code intelligence engine that maps Python codebases into a knowledge graph stored in PostgreSQL. When I tested it on Django (3,021 Python files, 181,000+ function calls), the full index took 23 minutes. Extraction was 8 minutes. Linking was 15 minutes. Linking was the bottleneck. Why linking was slow N3MO's linking phase resolves which function calls which. The original query used LIKE: WHERE c . call_name LIKE '%%.' || s . name This matches calls like module.function or self.function by checking if the call name ends with the function name. The p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/n3mo-dev/how-i-cut-django-indexing-from-23-minutes-to-11-minutes-with-one-sql-change-5of

## Related notes
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-05-11-beyond-basic-indexes-mastering-partial-composite-and-covering-indexes-in-sql]]
- [[2026-05-29-your-ai-agent-has-a-memory-problem-owasps-new-defense-against-memory-poisoning]]
