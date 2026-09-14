---
title: Building a file-sharing service with Rails 8 and SQLite
date: '2026-09-14'
source: https://dev.to/bakimosadi/building-a-file-sharing-service-with-rails-8-and-sqlite-5bih
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
status: unread
---

> **TL;DR:** Campsend sends finished work to one person, tells you when they opened it and lets you keep the files in a bucket you own. It runs on one server. I don't work on this full time, and Campsend is meant to be self-hostable.…

## What’s new and why it matters
Campsend sends finished work to one person, tells you when they opened it and lets you keep the files in a bucket you own. It runs on one server. I don't work on this full time, and Campsend is meant to be self-hostable. Fewer services helps both. Here's what's running, and where it stops being enough. Why Rails 8 Start with what isn't there. Authentication is the clearest example. Rails 8 generates it. There's no Devise and no password to store. A sign-in link goes to an email address, and the session holds a user id and a timestamp: module Authentication extend ActiveSupport :: Concern SESSI…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bakimosadi/building-a-file-sharing-service-with-rails-8-and-sqlite-5bih

## Related notes
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
