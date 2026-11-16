---
title: 'Why Rails `dependent: :destroy` Gets Painfully Slow, with a Simple Example'
date: '2026-11-16'
source: https://dev.to/kaziusan/why-rails-dependent-destroy-gets-painfully-slow-with-a-simple-example-159o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
- '[[2026-11-04-sql-server-parameter-sniffing-what-it-is-and-how-to-fix-it]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** What happens dependent: :destroy (so-called cascade delete) is handy: delete the parent record, and its child records go with it. But if the children have callbacks , those callbacks fire on every single delete. class Au…

## What’s new and why it matters
What happens dependent: :destroy (so-called cascade delete) is handy: delete the parent record, and its child records go with it. But if the children have callbacks , those callbacks fire on every single delete. class Author < ApplicationRecord has_many :books , dependent : :destroy end class Book < ApplicationRecord belongs_to :author , touch : true # deleting it updates the parent's updated_at (a "touch") after_destroy :reindex_search # reindexes Elasticsearch on every single delete (synchronous, heavy) end When you call author.destroy … destroy 1 Author └─ if there are 1000 books, destroy t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kaziusan/why-rails-dependent-destroy-gets-painfully-slow-with-a-simple-example-159o

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
- [[2026-11-04-sql-server-parameter-sniffing-what-it-is-and-how-to-fix-it]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
