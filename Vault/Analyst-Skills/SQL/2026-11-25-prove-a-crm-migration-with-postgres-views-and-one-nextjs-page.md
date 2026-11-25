---
title: Prove a CRM migration with Postgres views and one Next.js page
date: '2026-11-25'
source: https://dev.to/hasnan_khan_dev_0/prove-a-crm-migration-with-postgres-views-and-one-nextjs-page-3f62
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-11-24-how-to-get-jobs-from-the-greenhouse-job-board-api]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** This article was drafted with AI help and reviewed by the author. The import finished. HubSpot shows a green "completed" banner. Someone asks "did everything come across?" and the honest answer is "probably". "Probably"…

## What’s new and why it matters
This article was drafted with AI help and reviewed by the author. The import finished. HubSpot shows a green "completed" banner. Someone asks "did everything come across?" and the honest answer is "probably". "Probably" isn't good enough when the next step is switching off the old CRM. Once it's gone, a missing deal or a broken company link has no source to recover from. This post describes a small check you can rerun as often as you like. It has three parts: Two tables in Supabase Postgres. One holds the old CRM export. The other holds what HubSpot has right now. Five views that compare them:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hasnan_khan_dev_0/prove-a-crm-migration-with-postgres-views-and-one-nextjs-page-3f62

## Related notes
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-11-24-how-to-get-jobs-from-the-greenhouse-job-board-api]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
