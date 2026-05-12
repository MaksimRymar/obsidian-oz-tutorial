---
title: I Built Rust-Style ADTs in 30 Lines of Python (Pattern Matching Works)
date: '2026-05-12'
source: https://dev.to/alexander_mia_9/i-built-rust-style-adts-in-30-lines-of-python-pattern-matching-works-41le
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-07-quarks-outlines-python-emulating-callable-objects]]'
- '[[2026-05-03-pandas-secret-mini-language]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
status: unread
---

> **TL;DR:** Sum types — also called tagged unions or algebraic data types — are the feature I miss most when I switch from Rust or Haskell back to Python. The match statement landed in 3.10, but the standard library still does not g…

## What’s new and why it matters
Sum types — also called tagged unions or algebraic data types — are the feature I miss most when I switch from Rust or Haskell back to Python. The match statement landed in 3.10, but the standard library still does not give you a clean way to declare a closed set of variants where each variant carries its own fields. Here is a 30-line metaclass that fixes that. The result first class Computation ( metaclass = EnumMeta ): Nothing = Case () To = Case ( target = int ) List = Case ( targets = list [ int ]) follower = Computation . List ([ 1 ]) match follower : case Computation . To ( target = p ):…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alexander_mia_9/i-built-rust-style-adts-in-30-lines-of-python-pattern-matching-works-41le

## Related notes
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-07-quarks-outlines-python-emulating-callable-objects]]
- [[2026-05-03-pandas-secret-mini-language]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
