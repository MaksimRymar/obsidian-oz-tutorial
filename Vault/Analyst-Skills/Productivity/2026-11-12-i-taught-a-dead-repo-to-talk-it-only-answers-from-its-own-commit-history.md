---
title: I Taught a Dead Repo to Talk. It Only Answers From Its Own Commit History.
date: '2026-11-12'
source: https://dev.to/aheadkit/i-taught-a-dead-repo-to-talk-it-only-answers-from-its-own-commit-history-12ll
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#productivity'
- '#python'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
status: unread
---

> **TL;DR:** Every repo keeps a diary and almost nobody reads it. git log holds years of decisions — why a URL changed, which typos got fixed, who argued about what — but it only speaks when you grep it, and grep doesn't rank answers…

## What’s new and why it matters
Every repo keeps a diary and almost nobody reads it. git log holds years of decisions — why a URL changed, which typos got fixed, who argued about what — but it only speaks when you grep it, and grep doesn't rank answers. So I built a small ghost: a Python script that takes a question, matches its words against every commit message in a repo, and answers with the commits that fit best. No language model, no API key, no network. If nothing matches, it says so and stays quiet. A ghost that hallucinates would be worse than no ghost at all. The repo I woke up I needed a repo with a real history, s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aheadkit/i-taught-a-dead-repo-to-talk-it-only-answers-from-its-own-commit-history-12ll

## Related notes
- [[2026-09-14-keeping-strands-agents-honest-in-a-household-money-app]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
