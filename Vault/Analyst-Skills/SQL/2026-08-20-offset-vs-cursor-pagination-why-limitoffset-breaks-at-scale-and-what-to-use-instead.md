---
title: 'Offset vs Cursor Pagination: Why LIMIT/OFFSET Breaks at Scale (and What to
  Use Instead)'
date: '2026-08-20'
source: https://dev.to/vahid_aghajani_60ce9dbec9/offset-vs-cursor-pagination-why-limitoffset-breaks-at-scale-and-what-to-use-instead-3ho3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
status: unread
---

> **TL;DR:** 📺 Prefer to watch? 90-second YouTube Short · 💬 Telegram Originally published on software-engineer-blog.com . Everyone writes this on day one: SELECT * FROM orders ORDER BY created_at DESC LIMIT 20 OFFSET 40 ; Page three.…

## What’s new and why it matters
📺 Prefer to watch? 90-second YouTube Short · 💬 Telegram Originally published on software-engineer-blog.com . Everyone writes this on day one: SELECT * FROM orders ORDER BY created_at DESC LIMIT 20 OFFSET 40 ; Page three. Twenty rows. It works. Every ORM in existence will generate it for you from ?page=3 , and for a long time nothing goes wrong. That is exactly the problem. Page two is the one page that hides both of offset pagination's defects. The table is small, the data is sitting still, and you meet neither failure until you are in production with real traffic and a real table. What offset…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vahid_aghajani_60ce9dbec9/offset-vs-cursor-pagination-why-limitoffset-breaks-at-scale-and-what-to-use-instead-3ho3

## Related notes
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
