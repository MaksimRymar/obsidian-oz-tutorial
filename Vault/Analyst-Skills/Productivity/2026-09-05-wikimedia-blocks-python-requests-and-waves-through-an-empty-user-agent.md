---
title: Wikimedia blocks python-requests and waves through an empty User-Agent
date: '2026-09-05'
source: https://dev.to/devil_scrapes/wikimedia-blocks-python-requests-and-waves-through-an-empty-user-agent-50p5
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** Quick answer Wikimedia's REST API returns 403 to python-requests/2.31.0 , 403 to Python-urllib/3.11 , and 200 to a completely empty User-Agent header . The 403 body politely asks you to "set a user-agent." Sending no use…

## What’s new and why it matters
Quick answer Wikimedia's REST API returns 403 to python-requests/2.31.0 , 403 to Python-urllib/3.11 , and 200 to a completely empty User-Agent header . The 403 body politely asks you to "set a user-agent." Sending no user-agent string at all satisfies it. Sending your HTTP library's honest default does not. It isn't a requirement — it's a denylist of library defaults , and the error message describes the wrong rule. The measurement 📏 Same URL, same machine, one variable changed. This is curl , so there's no impersonation layer quietly rewriting anything: U = "https://wikimedia.org/api/rest_v1/…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/wikimedia-blocks-python-requests-and-waves-through-an-empty-user-agent-50p5

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]
