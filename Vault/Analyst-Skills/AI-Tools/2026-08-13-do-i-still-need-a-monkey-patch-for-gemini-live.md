---
title: Do I Still Need a Monkey Patch for Gemini Live?
date: '2026-08-13'
source: https://dev.to/gde/do-i-still-need-a-monkey-patch-for-gemini-live-4c3e
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** No. And deleting 187 lines of it was the single biggest benefit of moving to ADK 2.x — but it was not the only one, and it was not the last thing that needed fixing. What Does This Agent Do? The project is a biometric se…

## What’s new and why it matters
No. And deleting 187 lines of it was the single biggest benefit of moving to ADK 2.x — but it was not the only one, and it was not the last thing that needed fixing. What Does This Agent Do? The project is a biometric security scanner, built to exercise the parts of the Gemini Live API that a text chatbot never touches. A browser captures webcam and microphone, streams both to a FastAPI backend over a single WebSocket, and the backend forwards them to Gemini 3.1 Flash Live through the Agent Development Kit. The model watches the video feed, counts the fingers being held up, and calls a tool. T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gde/do-i-still-need-a-monkey-patch-for-gemini-live-4c3e

## Related notes
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
