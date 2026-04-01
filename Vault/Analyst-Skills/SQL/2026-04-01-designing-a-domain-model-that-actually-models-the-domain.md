---
title: Designing a Domain Model That Actually Models the Domain
date: '2026-04-01'
source: https://dev.to/elpic/designing-a-domain-model-that-actually-models-the-domain-4e7a
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]'
- '[[2026-03-25-stop-googling-dax-formulas-here-are-the-5-i-actually-use-to-solve-business-problems]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
status: unread
---

> **TL;DR:** Ports and adapters only work if you have a domain worth protecting. If your domain objects are just bags of getters and setters no behavior, no rules, no real logic the boundaries don't buy you much. You've built a clean…

## What’s new and why it matters
Ports and adapters only work if you have a domain worth protecting. If your domain objects are just bags of getters and setters no behavior, no rules, no real logic the boundaries don't buy you much. You've built a clean fence around an empty lot. This post is about filling the lot. The Anemic Domain Model Here's the Order and Customer you see in most codebases even the "clean" ones: from dataclasses import dataclass from typing import List , Optional @dataclass class OrderItem : product_id : str price : float quantity : int @dataclass class Customer : id : str loyalty_points : int @dataclass…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/elpic/designing-a-domain-model-that-actually-models-the-domain-4e7a

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-03-26-i-built-an-ai-that-reads-your-pets-mood-heres-the-python-behind-it]]
- [[2026-03-25-stop-googling-dax-formulas-here-are-the-5-i-actually-use-to-solve-business-problems]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
