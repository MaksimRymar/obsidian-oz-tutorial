---
title: Your pytest retries are lying to you. The hidden cost of --reruns, and the
  plugin I wrote so I could actually see what my tests were doing.
date: '2026-04-22'
source: https://dev.to/michle/your-pytest-retries-are-lying-to-you-the-hidden-cost-of-reruns-and-the-plugin-i-wrote-so-i-27fh
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#productivity'
- '#tool'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-23-the-reason-your-live-ai-demo-spins-has-nothing-to-do-with-your-model]]'
- '[[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]'
- '[[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]'
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
status: unread
---

> **TL;DR:** Picture this. A test fails in CI. It's been flaky all week — fails on push, passes when you rerun. So you add --reruns 2 to the pytest command. Now the suite passes. Green build. Ship it. A week later, the same test fail…

## What’s new and why it matters
Picture this. A test fails in CI. It's been flaky all week — fails on push, passes when you rerun. So you add --reruns 2 to the pytest command. Now the suite passes. Green build. Ship it. A week later, the same test fails in production in a way that only happens under load. You go back to look at the build that passed, and the report says... "passed." One line. No context. No hint that the test ever failed before, let alone what it failed with. This is what pytest looks like to most of us: a final verdict. It's not wrong, exactly — the test did pass, eventually. But "eventually" is hiding the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michle/your-pytest-retries-are-lying-to-you-the-hidden-cost-of-reruns-and-the-plugin-i-wrote-so-i-27fh

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-23-the-reason-your-live-ai-demo-spins-has-nothing-to-do-with-your-model]]
- [[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]
- [[2026-04-02-how-i-stopped-paying-openai-to-run-my-test-suite]]
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
