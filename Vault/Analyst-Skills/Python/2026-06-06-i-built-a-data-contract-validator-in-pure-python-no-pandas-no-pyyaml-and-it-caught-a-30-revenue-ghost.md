---
title: I built a data-contract validator in pure Python (no pandas, no PyYAML) and
  it caught a 30% revenue ghost
date: '2026-06-06'
source: https://dev.to/hajirufai/i-built-a-data-contract-validator-in-pure-python-no-pandas-no-pyyaml-and-it-caught-a-30-revenue-hlm
domain: Python
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
status: unread
---

> **TL;DR:** A few months ago I spent the better part of a day chasing a bug that turned out not to be a bug at all. A downstream dashboard showed revenue had jumped 30% overnight. No deploys, no schema changes, nothing in the logs.…

## What’s new and why it matters
A few months ago I spent the better part of a day chasing a bug that turned out not to be a bug at all. A downstream dashboard showed revenue had jumped 30% overnight. No deploys, no schema changes, nothing in the logs. After far too long I found it: an upstream system had started sending a total column that no longer equaled subtotal + tax . The pipeline didn't crash. The data just lied, quietly, and everything downstream believed it. That's the thing about data bugs. They rarely throw exceptions. A status field grows a new typo'd value. A join key starts producing orphans. A nullable column…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/hajirufai/i-built-a-data-contract-validator-in-pure-python-no-pandas-no-pyyaml-and-it-caught-a-30-revenue-hlm

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
