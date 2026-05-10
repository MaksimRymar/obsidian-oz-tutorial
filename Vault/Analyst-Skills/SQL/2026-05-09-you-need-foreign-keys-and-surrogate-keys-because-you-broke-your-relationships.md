---
title: You need foreign keys and surrogate keys because you broke your relationships
date: '2026-05-09'
source: https://dev.to/franckpachot/you-need-foreign-keys-and-surrogate-keys-because-you-broke-your-relationships-3b0j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
status: unread
---

> **TL;DR:** Many developers believe they need a relational database because their data has relationships. The reasoning usually goes: "My entities are related, therefore I need foreign keys, therefore I need an RDBMS." But the causa…

## What’s new and why it matters
Many developers believe they need a relational database because their data has relationships. The reasoning usually goes: "My entities are related, therefore I need foreign keys, therefore I need an RDBMS." But the causality is actually reversed. Normalization creates the need for foreign keys—not the other way around. This misunderstanding persists when the builders are agents, because LLMs operate on high-dimensional similarity (vectors), which may catch correlation better than causality. Normalisation and relations When you normalize your domain model into Normal Forms, you decompose aggreg…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/you-need-foreign-keys-and-surrogate-keys-because-you-broke-your-relationships-3b0j

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
