---
title: I built a self-hosted license key server because I didn't trust Gumroad's,
  and I didn't want to pay for someone else's
date: '2026-09-21'
source: https://dev.to/aranadedoros/i-built-a-self-hosted-license-key-server-because-i-didnt-trust-gumroads-and-i-didnt-want-to-pay-3im3
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-13-time-series-charts-in-sql-bucketing-gap-filling-and-time-zones-that-dont-lie]]'
status: unread
---

> **TL;DR:** I've been selling small things on Gumroad, and I plan to sell more software down the line. Somewhere along the way I heard enough stories about how easy Gumroad's built-in license keys are to work around that I stopped t…

## What’s new and why it matters
I've been selling small things on Gumroad, and I plan to sell more software down the line. Somewhere along the way I heard enough stories about how easy Gumroad's built-in license keys are to work around that I stopped trusting them as the only thing standing between "customer" and "person who downloaded it once and shared it in a Discord." I looked at the hosted alternatives (Keygen, Lemon Squeezy's license API, etc.) and they're fine, but paying a recurring fee to validate a string felt silly for what's fundamentally a lookup table with an expiration date. So I built my own: SnaKey — a small…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aranadedoros/i-built-a-self-hosted-license-key-server-because-i-didnt-trust-gumroads-and-i-didnt-want-to-pay-3im3

## Related notes
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-13-time-series-charts-in-sql-bucketing-gap-filling-and-time-zones-that-dont-lie]]
