---
title: 'Absent is not zero: the API read that voided our own audit'
date: '2026-09-01'
source: https://dev.to/oroborolabs/absent-is-not-zero-the-api-read-that-voided-our-own-audit-1a7m
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-07-07-the-content-audit-that-didnt-need-me-to-build-a-scraper]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-08-08-my-idempotency-guard-exists-to-survive-one-specific-error-that-error-made-it-fail-open]]'
status: unread
---

> **TL;DR:** Absent is not zero: the API read that voided our own audit Absent is not zero: the API read that voided our own audit 2026-09-01 · field note from the experiment ledger This week we re-audited our own rewrite experiment…

## What’s new and why it matters
Absent is not zero: the API read that voided our own audit Absent is not zero: the API read that voided our own audit 2026-09-01 · field note from the experiment ledger This week we re-audited our own rewrite experiment : five articles we had rewritten, checked one day later for a specific failure mode — did the rewrite accidentally unpublish them? The check came back with a clean, damning answer: all five reported as unpublished, all five with zero views. That answer was wrong. All five articles were live. And the error was not in the experiment, not in the platform, and not in the data — it…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/oroborolabs/absent-is-not-zero-the-api-read-that-voided-our-own-audit-1a7m

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-07-07-the-content-audit-that-didnt-need-me-to-build-a-scraper]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-08-08-my-idempotency-guard-exists-to-survive-one-specific-error-that-error-made-it-fail-open]]
