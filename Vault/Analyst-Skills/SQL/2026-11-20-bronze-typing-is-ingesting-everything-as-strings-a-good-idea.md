---
title: 'Bronze Typing: Is Ingesting Everything as Strings a Good Idea?'
date: '2026-11-20'
source: https://dev.to/geekindata/bronze-typing-is-ingesting-everything-as-strings-a-good-idea-4ed0
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-29-teaching-yourself-sql-when-your-job-is-ops]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]'
- '[[2026-09-17-i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived]]'
status: unread
---

> **TL;DR:** I used AI tools to help draft and edit this post. I checked the facts and the wording, and the original lives at geekindata.com . The diagrams are on that page. Type each column once, as early as you dare Key takeaways P…

## What’s new and why it matters
I used AI tools to help draft and edit this post. I checked the facts and the wording, and the original lives at geekindata.com . The diagrams are on that page. Type each column once, as early as you dare Key takeaways Publish definitive types at bronze (or the earliest stable clean view). Ban ritual CAST on unchanged physical columns in silver and gold. Allow UNION alignment casts only when localized next to the UNION. Gold owns typed unknown-row literals that match relationship types. Lint CAST noise in CI; allowlist only with a written reason. Rematerialize dependents when the type contract…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/geekindata/bronze-typing-is-ingesting-everything-as-strings-a-good-idea-4ed0

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-29-teaching-yourself-sql-when-your-job-is-ops]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]
- [[2026-09-17-i-fact-checked-5-viral-my-ai-bot-made-money-posts-against-primary-data-none-survived]]
