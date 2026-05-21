---
title: 🐍 python global vs nonlocal keyword — when to use each?
date: '2026-05-21'
source: https://dev.to/ptp2308/python-global-vs-nonlocal-keyword-when-to-use-each-17df
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-14-title-how-to-stream-reasoning-tokens-from-an-llm-in-production-a-practical]]'
- '[[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-02-22-mutability-vs-immutability-in-python-memory-references-and-side-effects]]'
status: unread
---

> **TL;DR:** A variable can be modified inside a nested function without being passed as an argument — if Python’s scope resolution rules allow it through global or nonlocal . 📑 Table of Contents 🧠 Scopes in Python — How Names Are Re…

## What’s new and why it matters
A variable can be modified inside a nested function without being passed as an argument — if Python’s scope resolution rules allow it through global or nonlocal . 📑 Table of Contents 🧠 Scopes in Python — How Names Are Resolved 🌍 Global — Modifying Module-Level Names ⚙️ Mechanism — What Happens at Compile Time 📌 Practical Example — A Simple Call Counter ⚠️ Gotcha — Global Isn’t Always What You Want 🔐 Nonlocal — Accessing Enclosing Function Variables ⚙️ Mechanism — Cell Variables and Closure 📌 Practical Example — Maintaining State in a Closure 💡 Real-World Use Case — Retry Logic with Backoff 🔍 P…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ptp2308/python-global-vs-nonlocal-keyword-when-to-use-each-17df

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-14-title-how-to-stream-reasoning-tokens-from-an-llm-in-production-a-practical]]
- [[2026-02-26-choosing-an-agent-framework-in-2026-a-data-driven-decision-guide]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-02-22-mutability-vs-immutability-in-python-memory-references-and-side-effects]]
