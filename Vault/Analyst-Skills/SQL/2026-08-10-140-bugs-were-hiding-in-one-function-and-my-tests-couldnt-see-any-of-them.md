---
title: 140 Bugs Were Hiding in One Function, and My Tests Couldn't See Any of Them
date: '2026-08-10'
source: https://dev.to/dannyamah/140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them-a0p
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
status: unread
---

> **TL;DR:** Anyone can port a library. Point a translator at the source, clean up the output, get it to compile, and you have something that looks like a port. The actual engineering problem is different and much harder: proving tha…

## What’s new and why it matters
Anyone can port a library. Point a translator at the source, clean up the output, get it to compile, and you have something that looks like a port. The actual engineering problem is different and much harder: proving that the new code means the same thing as the old code, across thirty algorithms, hundreds of edge cases, and a test suite written by people who were not thinking about you. This is the story of porting textdistance , a Python library for measuring string similarity, to Rust. The result is textdistance-rs . The porting took a fraction of the time. Everything else: the differential…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dannyamah/140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them-a0p

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
