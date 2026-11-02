---
title: 'From a GraphQL monorepo to FastAPI and React: the coupling changed'
date: '2026-11-02'
source: https://dev.to/marusyaganza/from-a-graphql-monorepo-to-fastapi-and-react-the-coupling-changed-49eo
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
- '[[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** Language Power is a vocabulary trainer I've built three times. The current version is a Python backend, FastAPI with PostgreSQL and Redis, and a React client, kept in two separate repositories and talking over REST. It r…

## What’s new and why it matters
Language Power is a vocabulary trainer I've built three times. The current version is a Python backend, FastAPI with PostgreSQL and Redis, and a React client, kept in two separate repositories and talking over REST. It runs as a private deployment I use every day and a public demo with strict limits. The version before it was a TypeScript monorepo with a GraphQL API and a shared schema. I built the app for my own language learning, so what follows is about maintaining one developer's project over several years, not about a team or about traffic. Between the two versions I changed more than the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/marusyaganza/from-a-graphql-monorepo-to-fastapi-and-react-the-coupling-changed-49eo

## Related notes
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
- [[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
