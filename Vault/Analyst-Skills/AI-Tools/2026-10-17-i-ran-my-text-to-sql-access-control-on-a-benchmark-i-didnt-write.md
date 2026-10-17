---
title: I ran my text-to-SQL access control on a benchmark I didn't write
date: '2026-10-17'
source: https://dev.to/ashish_sinha_5241c7673d93/i-ran-my-text-to-sql-access-control-on-a-benchmark-i-didnt-write-23n4
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-12-every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-22-how-i-cut-my-llm-api-bill-by-80-with-a-simple-router]]'
status: unread
---

> **TL;DR:** Every number I had published for schemagate came from my own tests. This month a SIGMOD'27 paper released a public benchmark for exactly the problem schemagate exists for: Benchmarking Text-to-SQL under Role-Based Access…

## What’s new and why it matters
Every number I had published for schemagate came from my own tests. This month a SIGMOD'27 paper released a public benchmark for exactly the problem schemagate exists for: Benchmarking Text-to-SQL under Role-Based Access Control . So I ran it. The test Each question comes with a role and a list of the columns that role may read. If the answer needs a column the role can't see, the right reply is "Sorry, I cannot answer." The authors score it with their own evaluator. I didn't change a line of it. Their main finding is uncomfortable for tools like mine. If you just hide the restricted columns,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashish_sinha_5241c7673d93/i-ran-my-text-to-sql-access-control-on-a-benchmark-i-didnt-write-23n4

## Related notes
- [[2026-09-12-every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-22-how-i-cut-my-llm-api-bill-by-80-with-a-simple-router]]
