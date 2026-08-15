---
title: The free plan wasn't actually "no registration required" — fixing a landing
  page claim that contradicted itself
date: '2026-08-15'
source: https://dev.to/susumun/the-free-plan-wasnt-actually-no-registration-required-fixing-a-landing-page-claim-that-2dfl
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-06-21-turso-a-rust-rewrite-of-sqlite-setup-guide-and-whether-its-worth-your-time]]'
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
- '[[2026-07-30-how-to-write-a-cohort-retention-query-in-sql-that-actually-runs]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-07-23-the-kernel-trick-why-you-never-build-x-kxyxy-computes-an-infinite-dimensional-dot-product-for-one-function-call]]'
status: unread
---

> **TL;DR:** Background An external marketing review flagged what looked like a contradiction in our landing page's FAQ. Checking it against the actual code confirmed the claim was accurate. Two statements coexisted on the same page:…

## What’s new and why it matters
Background An external marketing review flagged what looked like a contradiction in our landing page's FAQ. Checking it against the actual code confirmed the claim was accurate. Two statements coexisted on the same page: Quick Start, step 2: "Register with your email to start for free" The FAQ answer: "The Free plan requires no registration and allows up to 1 site, 3 runs per month — completely free." One says "please register." The other says "no registration needed." Checking the implementation confirmed that the Free plan requires an email address to be registered and verified on first laun…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/susumun/the-free-plan-wasnt-actually-no-registration-required-fixing-a-landing-page-claim-that-2dfl

## Related notes
- [[2026-06-21-turso-a-rust-rewrite-of-sqlite-setup-guide-and-whether-its-worth-your-time]]
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
- [[2026-07-30-how-to-write-a-cohort-retention-query-in-sql-that-actually-runs]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-07-23-the-kernel-trick-why-you-never-build-x-kxyxy-computes-an-infinite-dimensional-dot-product-for-one-function-call]]
