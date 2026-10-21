---
title: 'Day 17/90: Working with Processes -- Python Security'
date: '2026-10-21'
source: https://dev.to/thinkkun/day-1790-working-with-processes-python-security-4gnj
domain: Productivity
relevance: 🔴
tags:
- '#best-practice'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-29-python-part-2]]'
- '[[2026-09-28-detect-500-errors-in-server-logs-with-python-in-10-lines]]'
- '[[2026-08-27-design-functions-that-compound]]'
- '[[2026-07-20-learn-configuration-precedence-with-empty-missing-and-invalid-values]]'
- '[[2026-06-20-sql-pattern-series-7-the-running-total-pattern]]'
- '[[2026-07-20-3-lines-of-code-to-build-an-ai-team-the-10k-star-python-framework-most-people-dont-know-about]]'
status: unread
---

> **TL;DR:** Day 17/90: Working with Processes -- Python Security 90 Day Python Security Scripting Challenge Process analysis is core to incident response on any operating system. Today we use psutil to build practical triage tooling…

## What’s new and why it matters
Day 17/90: Working with Processes -- Python Security 90 Day Python Security Scripting Challenge Process analysis is core to incident response on any operating system. Today we use psutil to build practical triage tooling. Process Inventory with Security Context During triage you need more than just a process name. You need the owning user, the full command line, parent PID for process tree reconstruction, and the executable path to verify it is running from a legitimate location. import psutil from datetime import datetime def security_inventory (): """ Build a process inventory with fields re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/thinkkun/day-1790-working-with-processes-python-security-4gnj

## Related notes
- [[2026-07-29-python-part-2]]
- [[2026-09-28-detect-500-errors-in-server-logs-with-python-in-10-lines]]
- [[2026-08-27-design-functions-that-compound]]
- [[2026-07-20-learn-configuration-precedence-with-empty-missing-and-invalid-values]]
- [[2026-06-20-sql-pattern-series-7-the-running-total-pattern]]
- [[2026-07-20-3-lines-of-code-to-build-an-ai-team-the-10k-star-python-framework-most-people-dont-know-about]]
