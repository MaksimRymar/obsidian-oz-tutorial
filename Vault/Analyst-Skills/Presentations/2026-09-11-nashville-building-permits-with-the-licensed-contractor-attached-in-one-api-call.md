---
title: Nashville building permits with the licensed contractor attached, in one API
  call
date: '2026-09-11'
source: https://dev.to/perchpermits/nashville-building-permits-with-the-licensed-contractor-attached-in-one-api-call-4ki3
domain: Presentations
relevance: 🟡
tags:
- '#library'
- '#presentations'
- '#python'
- '#tool'
related:
- '[[2026-08-02-workdays-job-api-tells-you-there-are-2000-jobs-then-says-0-on-page-two]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Metro Nashville publishes every building permit as open data. It is a good dataset: address, parcel, declared cost, permit type, a free-text scope, updated daily. But it has three gaps that matter if you are building any…

## What’s new and why it matters
Metro Nashville publishes every building permit as open data. It is a good dataset: address, parcel, declared cost, permit type, a free-text scope, updated daily. But it has three gaps that matter if you are building anything on top of it. The "contact" field is whoever filed the paperwork. It is often the contractor, but often not. The licensed contractor, the license number, and the property owner are not in the dataset at all. Almost every residential permit says "not to add a second kitchen". Search for kitchen remodels and you get thousands of false hits. All three are fixable, and I pack…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/perchpermits/nashville-building-permits-with-the-licensed-contractor-attached-in-one-api-call-4ki3

## Related notes
- [[2026-08-02-workdays-job-api-tells-you-there-are-2000-jobs-then-says-0-on-page-two]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
