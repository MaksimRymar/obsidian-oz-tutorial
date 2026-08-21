---
title: We caught a SQL injection with an offline AI security scanner — here's the
  exact query it found
date: '2026-08-20'
source: https://dev.to/jomynn/we-caught-a-sql-injection-with-an-offline-ai-security-scanner-heres-the-exact-query-it-found-4187
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#productivity'
- '#sql'
- '#tool'
related:
- '[[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-04-30-acacia-db-for-vs-code-map-your-database-usage-in-source-code-100-120]]'
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-06-06-i-built-a-free-sql-practice-game-where-you-work-at-a-fictional-singapore-bank]]'
status: unread
---

> **TL;DR:** The bug Here's a login endpoint from a small Express demo app ( scan-target-demo-apps/apps/01-sql-injection ): app . post ( ' /login ' , ( req , res ) => { const { username = '' , password = '' } = req . body ; const que…

## What’s new and why it matters
The bug Here's a login endpoint from a small Express demo app ( scan-target-demo-apps/apps/01-sql-injection ): app . post ( ' /login ' , ( req , res ) => { const { username = '' , password = '' } = req . body ; const query = `SELECT id, username, email, is_admin FROM users WHERE username = ' ${ username } ' AND password = ' ${ password } '` ; const result = db . exec ( query ); // ... }); You've seen this shape before. username and password go straight into the SQL string — no parameter binding, no escaping. Submit admin' -- as the username and anything as the password, and the query becomes:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/jomynn/we-caught-a-sql-injection-with-an-offline-ai-security-scanner-heres-the-exact-query-it-found-4187

## Related notes
- [[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-04-30-acacia-db-for-vs-code-map-your-database-usage-in-source-code-100-120]]
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-06-06-i-built-a-free-sql-practice-game-where-you-work-at-a-fictional-singapore-bank]]
