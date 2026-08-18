---
title: Your verifier is probably lying to you about floats
date: '2026-08-18'
source: https://dev.to/gowrishankar-dev/your-verifier-is-probably-lying-to-you-about-floats-3m0d
domain: Productivity
relevance: 🔴
tags:
- '#feature'
- '#productivity'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** Here is a promise that looks obviously true: fn add_twice(x: Float) -> Float ensures result == x + 0.2 { return x + 0.1 + 0.1 } Adding a tenth twice is the same as adding two tenths. Every algebra teacher you have ever h…

## What’s new and why it matters
Here is a promise that looks obviously true: fn add_twice(x: Float) -> Float ensures result == x + 0.2 { return x + 0.1 + 0.1 } Adding a tenth twice is the same as adding two tenths. Every algebra teacher you have ever had agrees. Most program verifiers agree too. They are wrong, and so is the promise. Velaris — a language I have been building — refuses to prove it, and hands back the number that breaks it: error[E700] promise cannot be kept: 'add_twice' ensures result == x + 0.2 proven without running the program: x = -1.207290298954004637010939404717646539211273193359375 gives result = -1.00…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gowrishankar-dev/your-verifier-is-probably-lying-to-you-about-floats-3m0d

## Related notes
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
