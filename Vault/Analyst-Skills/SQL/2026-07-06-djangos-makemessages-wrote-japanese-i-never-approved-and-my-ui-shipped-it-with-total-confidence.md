---
title: Django's makemessages wrote Japanese I never approved — and my UI shipped it
  with total confidence
date: '2026-07-06'
source: https://dev.to/hitoshi1964/djangos-makemessages-wrote-japanese-i-never-approved-and-my-ui-shipped-it-with-total-confidence-dle
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
status: unread
---

> **TL;DR:** I added a drift-history model to my Django app, gave its fields the usual verbose_name s, and ran the one command you always run: django-admin makemessages -l ja It found the new strings, dropped them into the .po file,…

## What’s new and why it matters
I added a drift-history model to my Django app, gave its fields the usual verbose_name s, and ran the one command you always run: django-admin makemessages -l ja It found the new strings, dropped them into the .po file, I recompiled, and moved on. A while later I opened the app in Japanese and a column header read 取得日時 — "fetch time." I never wrote "fetch time." The field is Detected At . Where did a translation I never typed come from? makemessages wrote it. And it was confidently, specifically wrong. What makemessages actually did When you add a new msgid that looks similar to one you've alr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hitoshi1964/djangos-makemessages-wrote-japanese-i-never-approved-and-my-ui-shipped-it-with-total-confidence-dle

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
