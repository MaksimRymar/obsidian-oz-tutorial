---
title: Why Templating Engines' Auto-Escaping Breaks the Moment You Bypass It
date: '2026-08-03'
source: https://dev.to/137foundry/why-templating-engines-auto-escaping-breaks-the-moment-you-bypass-it-1129
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
- '[[2026-05-16-i-taught-sql-to-complete-beginners-heres-what-actually-happened]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** Most developers today have never had to write an HTML escaping function by hand, and that's a genuine improvement. React escapes interpolated values before rendering. Jinja2 and Django templates auto-escape by default. V…

## What’s new and why it matters
Most developers today have never had to write an HTML escaping function by hand, and that's a genuine improvement. React escapes interpolated values before rendering. Jinja2 and Django templates auto-escape by default. Vue and Angular do the same. This is why XSS in modern frameworks usually isn't a "the framework failed" story. It's a "someone explicitly turned the safety off for one specific value" story. The three ways teams bypass auto-escaping dangerouslySetInnerHTML in React. The name is honest about what it does, but that honesty doesn't stop it from getting used. It usually shows up wh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/137foundry/why-templating-engines-auto-escaping-breaks-the-moment-you-bypass-it-1129

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
- [[2026-05-16-i-taught-sql-to-complete-beginners-heres-what-actually-happened]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
