---
title: 'Exit code 0 is a lie: 7 ways my unattended automation silently did nothing'
date: '2026-09-06'
source: https://dev.to/youfuhsu/exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing-501j
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
- '[[2026-09-02-the-48-hour-verdict-sort-your-ai-failures-before-you-fix-them]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-08-10-my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet]]'
status: unread
---

> **TL;DR:** I run about thirty scheduled jobs on a single Windows box. Some are scrapers, some generate content, some are trading bots, some just check that the other jobs are alive. Most of them were written and are maintained by a…

## What’s new and why it matters
I run about thirty scheduled jobs on a single Windows box. Some are scrapers, some generate content, some are trading bots, some just check that the other jobs are alive. Most of them were written and are maintained by an AI coding agent that I let run unattended. Over three months, every one of the failures below reported success . The scheduler said LastTaskResult = 0 . The logs looked fine or didn't exist. And nothing had happened. If you only take one thing from this post: stop checking exit codes, start checking artifacts. I'll get to why at the end. First, the seven ways I got lied to. 1…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/youfuhsu/exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing-501j

## Related notes
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
- [[2026-09-02-the-48-hour-verdict-sort-your-ai-failures-before-you-fix-them]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-08-10-my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet]]
