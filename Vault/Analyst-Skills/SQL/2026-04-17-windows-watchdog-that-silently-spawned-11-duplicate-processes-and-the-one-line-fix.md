---
title: Windows watchdog that silently spawned 11 duplicate processes — and the one-line
  fix
date: '2026-04-17'
source: https://dev.to/lucas_gragg_9ca9e7f95852f/windows-watchdog-that-silently-spawned-11-duplicate-processes-and-the-one-line-fix-5958
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-03-12-my-first-public-project-on-python]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
- '[[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
status: unread
---

> **TL;DR:** I came back to my desk and counted 11 cmd windows instead of the 6 I expected. All running Python, all for the same project, all spawned by my own watchdog. This post is the diagnostic trail and the fix, in case anyone e…

## What’s new and why it matters
I came back to my desk and counted 11 cmd windows instead of the 6 I expected. All running Python, all for the same project, all spawned by my own watchdog. This post is the diagnostic trail and the fix, in case anyone else is using tasklist /FI "WINDOWTITLE" as a process-liveness check on Windows. The setup I run ~6 Python daemons on a Windows 11 box. Each is launched via: start "Agent" cmd /c "cd /d C:\path && python -m agent.main" Task Scheduler fires watchdog.bat every 5 minutes. The watchdog is supposed to: Check if each daemon is alive If not, relaunch it For daemons with HTTP ports, liv…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/lucas_gragg_9ca9e7f95852f/windows-watchdog-that-silently-spawned-11-duplicate-processes-and-the-one-line-fix-5958

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-03-12-my-first-public-project-on-python]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
- [[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
