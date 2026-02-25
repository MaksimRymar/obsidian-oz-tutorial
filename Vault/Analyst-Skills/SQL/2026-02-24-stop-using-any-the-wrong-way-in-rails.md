---
title: Stop Using .any? the Wrong Way in Rails
date: '2026-02-24'
source: https://dev.to/pavelmyslik/stop-using-any-the-wrong-way-in-rails-429e
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-22-building-an-ai-powered-natural-language-sql-interface-an-mvp-journey]]'
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-02-23-why-your-ai-agent-forgets-everything-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** A single block passed to .any? can silently load thousands of records into memory. No warnings. No errors. Just unnecessary objects. And most Rails developers don’t notice it. You’ve probably used both .any? and .exists?…

## What’s new and why it matters
A single block passed to .any? can silently load thousands of records into memory. No warnings. No errors. Just unnecessary objects. And most Rails developers don’t notice it. You’ve probably used both .any? and .exists? in your Rails app without thinking twice. They both answer the same simple question: Is there at least one record? But under the hood, they can behave very differently. In this article, we’ll look at what actually happens when you call each method, when to use which, and how to avoid a common performance trap. The Basics: Same Query, Same Result If you just need to check wheth…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pavelmyslik/stop-using-any-the-wrong-way-in-rails-429e

## Related notes
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-22-building-an-ai-powered-natural-language-sql-interface-an-mvp-journey]]
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-02-23-why-your-ai-agent-forgets-everything-and-how-to-fix-it]]
