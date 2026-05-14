---
title: 'We built an enterprise integration stack for .NET from scratch: EAV + DSL
  + runtime'
date: '2026-05-13'
source: https://dev.to/rinat_kozin_d0a2ef43e7824/we-built-an-enterprise-integration-stack-for-net-from-scratch-eav-dsl-runtime-2l16
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-13-typescript-knows-your-sql-is-broken-before-your-tests-even-run]]'
- '[[2026-04-12-postgresql-jsonb-a-complete-guide-to-storing-and-querying-json-data]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]'
- '[[2026-03-28-kysely-has-a-free-api-type-safe-sql-query-builder-for-typescript]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
status: unread
---

> **TL;DR:** Three open-source libraries. One coherent stack. All Apache 2.0. This is the story of what we built, why, and how the three pieces fit together in a way that surprised even us. The problem Enterprise .NET integration in…

## What’s new and why it matters
Three open-source libraries. One coherent stack. All Apache 2.0. This is the story of what we built, why, and how the three pieces fit together in a way that surprised even us. The problem Enterprise .NET integration in 2026 still looks like this: EF Core for data — plus a migration file every time a field changes MassTransit or NServiceBus for messaging — great if you only need message brokers, but IBM MQ, SFTP, MQTT, SQL polling? Custom adapters, every time Kubernetes + etcd for clustering — because "that's just how you do it" We needed all three. We built all three. And then we noticed they…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rinat_kozin_d0a2ef43e7824/we-built-an-enterprise-integration-stack-for-net-from-scratch-eav-dsl-runtime-2l16

## Related notes
- [[2026-04-13-typescript-knows-your-sql-is-broken-before-your-tests-even-run]]
- [[2026-04-12-postgresql-jsonb-a-complete-guide-to-storing-and-querying-json-data]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]
- [[2026-03-28-kysely-has-a-free-api-type-safe-sql-query-builder-for-typescript]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
