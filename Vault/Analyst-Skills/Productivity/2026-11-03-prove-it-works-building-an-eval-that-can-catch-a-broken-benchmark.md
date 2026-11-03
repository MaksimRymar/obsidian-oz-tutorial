---
title: 'Prove It Works: Building an Eval That Can Catch a Broken Benchmark'
date: '2026-11-03'
source: https://dev.to/ranadhir19/prove-it-works-building-an-eval-that-can-catch-a-broken-benchmark-2c4
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
related:
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-09-12-your-login-tests-are-green-what-did-cursorexecute-actually-receive]]'
- '[[2026-09-19-faq-five-myths-about-tests-the-agent-wrote-for-itself]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
status: unread
---

> **TL;DR:** A benchmark with flawed tests measures the tests. So I built two suites — one clean, one with 12 flaws planted in the tests — and watched a do-nothing agent start scoring points while my reference agent lost 8.3 points t…

## What’s new and why it matters
A benchmark with flawed tests measures the tests. So I built two suites — one clean, one with 12 flaws planted in the tests — and watched a do-nothing agent start scoring points while my reference agent lost 8.3 points to the tests themselves. This is the full experiment: calibrating the graders first, pre-registering the audit bar, catching 11 of 12 flaws — and being honest about the one that got away. The setup Local, deterministic, no API keys — a lab for auditing your eval before your eval audits your agent. The setup is a clean 60-task suite (arithmetic, extraction and classification; gol…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ranadhir19/prove-it-works-building-an-eval-that-can-catch-a-broken-benchmark-2c4

## Related notes
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-09-12-your-login-tests-are-green-what-did-cursorexecute-actually-receive]]
- [[2026-09-19-faq-five-myths-about-tests-the-agent-wrote-for-itself]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
