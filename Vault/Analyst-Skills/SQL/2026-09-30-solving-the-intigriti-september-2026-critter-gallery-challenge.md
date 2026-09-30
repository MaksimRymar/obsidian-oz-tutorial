---
title: Solving the Intigriti September 2026 Critter Gallery challenge
date: '2026-09-30'
source: https://dev.to/samikshashreya/solving-the-intigriti-september-2026-critter-gallery-challenge-37j5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
status: unread
---

> **TL;DR:** I found the flag by following the gallery's pic parameter from an ordinary animal page into a SQL query. The value looked opaque in the URL, but it was only base64 encoded. Once decoded, the animal name could change the…

## What’s new and why it matters
I found the flag by following the gallery's pic parameter from an ordinary animal page into a SQL query. The value looked opaque in the URL, but it was only base64 encoded. Once decoded, the animal name could change the database predicate and supply a result from another table. This writeup covers only the official challenge at https://challenge-0926.challenges.intigriti.io/challenge.php . The solve was accepted in submission INTIGRITI-T8Z07V6I . Start with one animal A gallery entry opened at this URL: https://challenge-0926.challenges.intigriti.io/challenge.php?pic=Zm94 Zm94 decodes to fox .…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/samikshashreya/solving-the-intigriti-september-2026-critter-gallery-challenge-37j5

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
