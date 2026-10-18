---
title: Six tests that passed without testing what they claimed
date: '2026-10-18'
source: https://dev.to/azadhmhd/six-tests-that-passed-without-testing-what-they-claimed-4h1c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-16-three-sets-one-diff-a-write-set-glossary-a-four-leaf-tree-and-a-worked-example-at-every-leaf]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
status: unread
---

> **TL;DR:** I recently built a multi-tenant booking API (FastAPI, SQLAlchemy, Postgres, Redis, and a background worker) with Claude Code, as the running example for a book. Writing good tests was an explicit goal from the first comm…

## What’s new and why it matters
I recently built a multi-tenant booking API (FastAPI, SQLAlchemy, Postgres, Redis, and a background worker) with Claude Code, as the running example for a book. Writing good tests was an explicit goal from the first commit. The suite grew to 97 tests against real Postgres and Redis, with no mocked database. Six of those tests passed without testing what their names claimed. None was careless. Each was plausible, read well, and went green. A green run can't tell a test that checks the behaviour from one that checks nothing, and that's as true when you write the test as when an agent does. Here…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/azadhmhd/six-tests-that-passed-without-testing-what-they-claimed-4h1c

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-16-three-sets-one-diff-a-write-set-glossary-a-four-leaf-tree-and-a-worked-example-at-every-leaf]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
