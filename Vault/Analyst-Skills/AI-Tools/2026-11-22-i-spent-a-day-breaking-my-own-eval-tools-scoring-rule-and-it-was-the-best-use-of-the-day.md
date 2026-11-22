---
title: I spent a day breaking my own eval tool's scoring rule, and it was the best
  use of the day
date: '2026-11-22'
source: https://dev.to/the_movie_9b1357e8c99cfaa/i-spent-a-day-breaking-my-own-eval-tools-scoring-rule-and-it-was-the-best-use-of-the-day-eak
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]'
- '[[2026-10-10-your-ebay-sold-price-data-is-149-too-high-and-the-response-looks-fine]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-10-22-ollama-run-llms-locally-and-swap-them-into-your-app-with-one-baseurl-change]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** This is the developer-facing version of a post I published on AI Stack Lab: Your Eval Suite Is Theater Until a Non-Zero Exit Code Stops the Merge . Same measurements, different angle — this one is about the scoring rule…

## What’s new and why it matters
This is the developer-facing version of a post I published on AI Stack Lab: Your Eval Suite Is Theater Until a Non-Zero Exit Code Stops the Merge . Same measurements, different angle — this one is about the scoring rule itself. I spent a day breaking my own eval tool's scoring rule, and it was the best use of the day Last week I shipped a $1 CLI called AIEval that does exactly one thing: read a JSONL of recorded model answers, compare each one to an expected string, and exit non-zero if accuracy falls under a threshold you wrote in a config file. Offline, stdlib only, 275 lines of Python. The…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/the_movie_9b1357e8c99cfaa/i-spent-a-day-breaking-my-own-eval-tools-scoring-rule-and-it-was-the-best-use-of-the-day-eak

## Related notes
- [[2026-10-17-i-added-a-fourth-shard-in-python-and-75-of-the-keys-moved]]
- [[2026-10-10-your-ebay-sold-price-data-is-149-too-high-and-the-response-looks-fine]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-10-22-ollama-run-llms-locally-and-swap-them-into-your-app-with-one-baseurl-change]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
