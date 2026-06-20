---
title: Green unit tests are a comfort blanket
date: '2026-06-20'
source: https://dev.to/golikovichev/green-unit-tests-are-a-comfort-blanket-40ag
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
status: unread
---

> **TL;DR:** My converter has a test suite. It was green. Every example I could think of went in, the right pytest file came out, and I shipped it to PyPI as 1.0. Weeks later it sits there marked Production/Stable. Then I pointed a f…

## What’s new and why it matters
My converter has a test suite. It was green. Every example I could think of went in, the right pytest file came out, and I shipped it to PyPI as 1.0. Weeks later it sits there marked Production/Stable. Then I pointed a fuzzer at it, and it stopped being so quiet. The blind spot in example tests Unit tests check the inputs you thought of. That is their whole nature: you sit down, you imagine how the code gets used, you write an example for each case. The cases you imagine tend to be the cases the code already handles, because you wrote the code and the test in the same afternoon, with the same…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/golikovichev/green-unit-tests-are-a-comfort-blanket-40ag

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
