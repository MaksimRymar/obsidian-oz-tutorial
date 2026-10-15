---
title: On Windows, four processes appending to one file lost 37 of 200 lines
date: '2026-10-15'
source: https://dev.to/syntaxixr/on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines-3738
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-10-09-dont-let-a-new-signal-engine-write-fake-trades-a-warm-up-flag-for-trading-alert-bots]]'
- '[[2026-10-07-a-terminal-bench-task-frontier-agents-could-not-pass]]'
status: unread
---

> **TL;DR:** My CI failed with this, only on the Windows runner, on a commit that changed nothing but a few GIFs: receipts: Unexpected token '\', "\hostedtoo"... is not valid JSON The same test had passed on that runner a few hours e…

## What’s new and why it matters
My CI failed with this, only on the Windows runner, on a commit that changed nothing but a few GIFs: receipts: Unexpected token '\', "\hostedtoo"... is not valid JSON The same test had passed on that runner a few hours earlier. Here is what it was, because it is a small bug that is easy to ship. The setup Receipts runs the tests a change added or edited twice: with the change, and with the changed source files put back the way they were. For pytest it loads a tiny plugin that writes one JSON line per test result into a file, and the Node side reads that file afterwards. def _emit ( record ): o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/syntaxixr/on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines-3738

## Related notes
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-10-09-dont-let-a-new-signal-engine-write-fake-trades-a-warm-up-flag-for-trading-alert-bots]]
- [[2026-10-07-a-terminal-bench-task-frontier-agents-could-not-pass]]
