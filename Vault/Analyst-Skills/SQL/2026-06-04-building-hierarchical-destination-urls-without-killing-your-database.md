---
title: Building Hierarchical Destination URLs Without Killing Your Database
date: '2026-06-04'
source: https://dev.to/lji/building-hierarchical-destination-urls-without-killing-your-database-3n1g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]'
- '[[2026-05-13-we-built-an-enterprise-integration-stack-for-net-from-scratch-eav-dsl-runtime]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
status: unread
---

> **TL;DR:** One of the more challenging engineering problems we encountered while building our travel portal, was figuring out a decent URL structure for destination hubs. On the face of it, this one looks relatively easy to crack.…

## What’s new and why it matters
One of the more challenging engineering problems we encountered while building our travel portal, was figuring out a decent URL structure for destination hubs. On the face of it, this one looks relatively easy to crack. You've got a geographically based hierarchy: Global Region, Subregion, Country, Local Region, Local Subregion & City - & it would be nice to have URLs that make sense with that structure. Something that's clean, readable, semantically meaningful, and also SEO-friendly sounds pretty great. The problem is, turning that into a system that doesn't grind your application to a halt.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lji/building-hierarchical-destination-urls-without-killing-your-database-3n1g

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-24-database-decoded-navigating-queries-in-fastapi-django-orm-vs-raw-sql]]
- [[2026-05-13-we-built-an-enterprise-integration-stack-for-net-from-scratch-eav-dsl-runtime]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
