---
title: How to check your Rust port against the Python original (with five real bugs
  it caught)
date: '2026-11-18'
source: https://dev.to/neelagiri65/how-to-check-your-rust-port-against-the-python-original-with-five-real-bugs-it-caught-48g7
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-19-faq-five-myths-about-tests-the-agent-wrote-for-itself]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
status: unread
---

> **TL;DR:** You rewrote a Python library in Rust. The benchmarks look great and the test suite is green. One question is left, and it is the one your users care about: does it still do exactly what the old code did? Your tests can't…

## What’s new and why it matters
You rewrote a Python library in Rust. The benchmarks look great and the test suite is green. One question is left, and it is the one your users care about: does it still do exactly what the old code did? Your tests can't fully answer that. They check the inputs you thought of. The differences hide in the inputs nobody thought of. The good news is that a port comes with something most code never has: a complete specification. It's the old code. You don't need to read the Rust or reason about it. Run both versions on the same input and compare what comes back. Repeat until they disagree. Here is…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/neelagiri65/how-to-check-your-rust-port-against-the-python-original-with-five-real-bugs-it-caught-48g7

## Related notes
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-19-faq-five-myths-about-tests-the-agent-wrote-for-itself]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
