---
title: Your Login Tests Are Green. What Did cursor.execute Actually Receive?
date: '2026-09-12'
source: https://dev.to/yuan_ming_3549dae7e400994/your-login-tests-are-green-what-did-cursorexecute-actually-receive-5a92
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-06-09-pandas-vs-sql-when-to-use-each]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]'
status: unread
---

> **TL;DR:** A reader on my earlier Dev.to post made the useful point directly: Assert that the query is parameterized before it reaches cursor.execute . That sounds simple. It also exposes a blind spot in many test suites. A respons…

## What’s new and why it matters
A reader on my earlier Dev.to post made the useful point directly: Assert that the query is parameterized before it reaches cursor.execute . That sounds simple. It also exposes a blind spot in many test suites. A response assertion can prove that login behaves correctly. It cannot prove what SQL and parameters reached the database executor. So I built a small experiment with two login implementations. Both passed the same two behavior tests. Only one passed the parameterization contract test. The two implementations The first implementation builds SQL with an f-string: def login ( db , usernam…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yuan_ming_3549dae7e400994/your-login-tests-are-green-what-did-cursorexecute-actually-receive-5a92

## Related notes
- [[2026-09-06-put-a-write-boundary-between-the-agent-patch-and-the-oracle]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-06-09-pandas-vs-sql-when-to-use-each]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]
