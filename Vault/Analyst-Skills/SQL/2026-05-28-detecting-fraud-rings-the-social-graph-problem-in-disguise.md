---
title: 'Detecting fraud rings: the social-graph problem in disguise'
date: '2026-05-28'
source: https://dev.to/fixelsmith/detecting-fraud-rings-the-social-graph-problem-in-disguise-24lm
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** Fraud at scale usually gives itself away through repetition. One phone number behind twelve identities. Same device fingerprint reused across signups. A shipping address that keeps showing up on accounts that supposedly…

## What’s new and why it matters
Fraud at scale usually gives itself away through repetition. One phone number behind twelve identities. Same device fingerprint reused across signups. A shipping address that keeps showing up on accounts that supposedly have nothing to do with each other. At some point the accounts stop looking independent. They're a ring. Finding rings is a graph problem. Nodes are accounts, edges are shared attributes, and what you want is connected components. The usual recommendation is to throw the data into Neo4j and solve it there with Cypher queries. That absolutely works. It's also a lot of infrastruc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/fixelsmith/detecting-fraud-rings-the-social-graph-problem-in-disguise-24lm

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
