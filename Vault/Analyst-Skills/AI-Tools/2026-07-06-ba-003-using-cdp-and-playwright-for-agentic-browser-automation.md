---
title: '[BA-003] Using CDP and Playwright for agentic browser automation'
date: '2026-07-06'
source: https://dev.to/isaias_velasquez_d2261770/ba-003-using-cdp-and-playwright-for-agentic-browser-automation-5eeo
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#tool'
related:
- '[[2026-07-06-ba-006-extracting-structured-data-with-browser-automation]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-07-06-ba-007-logins-sessions-and-authentication-in-browser-automation]]'
- '[[2026-05-04-day-3-prompting-techniques-in-ai-part-1]]'
- '[[2026-07-03-why-does-a-list-change-in-two-variables]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** So far we have seen what BA-001 and how to automate with BA-002 . Now we get to the interesting part: using these tools to build an AI agent that controls a browser. The core idea is simple: the agent sees what is on the…

## What’s new and why it matters
So far we have seen what BA-001 and how to automate with BA-002 . Now we get to the interesting part: using these tools to build an AI agent that controls a browser. The core idea is simple: the agent sees what is on the page, decides what to do, executes the action, and repeats. This is called the observation-action loop. Here is a minimal example using Playwright and an LLM: from playwright.sync_api import sync_playwright from openai import OpenAI client = OpenAI() with sync_playwright() as p: browser = p.chromium.launch(headless=False) page = browser.new_page() page.goto("https://example.co…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/isaias_velasquez_d2261770/ba-003-using-cdp-and-playwright-for-agentic-browser-automation-5eeo

## Related notes
- [[2026-07-06-ba-006-extracting-structured-data-with-browser-automation]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-07-06-ba-007-logins-sessions-and-authentication-in-browser-automation]]
- [[2026-05-04-day-3-prompting-techniques-in-ai-part-1]]
- [[2026-07-03-why-does-a-list-change-in-two-variables]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
