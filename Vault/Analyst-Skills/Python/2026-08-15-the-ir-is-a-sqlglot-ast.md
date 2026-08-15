---
title: The IR Is a sqlglot AST
date: '2026-08-15'
source: https://dev.to/5c4989ca297ed/the-ir-is-a-sqlglot-ast-e40
domain: Python
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-04-apache-arrow-for-data-engineers-zero-copy-columnar-memory-across-the-whole-stack]]'
- '[[2026-08-05-decision-record-an-in-app-saas-chatbot-api-with-one-key-and-durable-transcripts]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
status: unread
---

> **TL;DR:** Every data tool has an intermediate representation, whether it admits to one or not. It is the thing a model becomes after parsing and before execution, and it quietly decides what the tool can do. dbt's IR is templated…

## What’s new and why it matters
Every data tool has an intermediate representation, whether it admits to one or not. It is the thing a model becomes after parsing and before execution, and it quietly decides what the tool can do. dbt's IR is templated text, which is why ref() is a string and why a macro can produce SQL no analyser can reason about. An earlier iteration of Interlace effectively had a pandas DataFrame as its IR — every model boundary ran an eager .execute() and fed the result back in — which cost us laziness, dialect portability and any hope of semantic change detection, all at once. Three properties, one root…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/5c4989ca297ed/the-ir-is-a-sqlglot-ast-e40

## Related notes
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-04-apache-arrow-for-data-engineers-zero-copy-columnar-memory-across-the-whole-stack]]
- [[2026-08-05-decision-record-an-in-app-saas-chatbot-api-with-one-key-and-durable-transcripts]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
