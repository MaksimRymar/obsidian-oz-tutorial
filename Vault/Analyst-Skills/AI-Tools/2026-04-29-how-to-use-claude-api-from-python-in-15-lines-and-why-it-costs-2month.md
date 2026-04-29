---
title: How to use Claude API from Python in 15 lines (and why it costs $2/month)
date: '2026-04-29'
source: https://dev.to/subprime2010/how-to-use-claude-api-from-python-in-15-lines-and-why-it-costs-2month-148d
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-04-06-summarize-1000-documents-with-python-for-under-1-pay-per-use-ai-api]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** How to use Claude API from Python in 15 lines You don't need a $20/month subscription to use Claude. You need 15 lines of Python and $2/month. Here's the complete working code: import anthropic client = anthropic . Anthr…

## What’s new and why it matters
How to use Claude API from Python in 15 lines You don't need a $20/month subscription to use Claude. You need 15 lines of Python and $2/month. Here's the complete working code: import anthropic client = anthropic . Anthropic ( api_key = " your-api-key-here " # get from simplylouie.com/developers ) message = client . messages . create ( model = " claude-opus-4-5 " , max_tokens = 1024 , messages = [ { " role " : " user " , " content " : " Explain async/await in Python in 3 sentences. " } ] ) print ( message . content [ 0 ]. text ) That's it. That's the whole API call. What you get back # The res…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/subprime2010/how-to-use-claude-api-from-python-in-15-lines-and-why-it-costs-2month-148d

## Related notes
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-04-06-summarize-1000-documents-with-python-for-under-1-pay-per-use-ai-api]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
