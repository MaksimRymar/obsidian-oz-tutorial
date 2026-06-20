---
title: Implementing Feature Flags Across Stack
date: '2026-06-20'
source: https://dev.to/leighfall/implementing-feature-flags-across-stack-29o2
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
status: unread
---

> **TL;DR:** Shipping an application that I didn't have access to was giving me heartburn. So I decided to create a lightweight feature flag tool. The Problem The team that I work on recently shipped a Vue 3, C#, and SQL application…

## What’s new and why it matters
Shipping an application that I didn't have access to was giving me heartburn. So I decided to create a lightweight feature flag tool. The Problem The team that I work on recently shipped a Vue 3, C#, and SQL application to a network that we do not have access to as engineers. We have a system admin that does the deployments, DBAs that handle the scripts, and stakeholders that test and monitor the application. But the engineers, the QA, the PM, and the BA have limited or no access to easily see what is and is not successful. I mean, could you imagine sending your application off into the nether…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/leighfall/implementing-feature-flags-across-stack-29o2

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
