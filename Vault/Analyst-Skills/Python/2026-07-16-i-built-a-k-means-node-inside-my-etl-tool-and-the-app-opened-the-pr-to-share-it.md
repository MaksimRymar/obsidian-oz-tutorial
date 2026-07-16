---
title: I built a k-means node inside my ETL tool — and the app opened the PR to share
  it
date: '2026-07-16'
source: https://dev.to/edwardvaneechoud/i-built-a-k-means-node-inside-my-etl-tool-and-the-app-opened-the-pr-to-share-it-28hj
domain: Python
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-05-28-how-i-added-dbt-cloud-to-coral-my-open-source-hackathon-journey]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
status: unread
---

> **TL;DR:** There's a k-means clustering node in Flowfile now, and it didn't come from a release. I built it inside the app — drew the settings form, wrote one process() function, tested it against sample data, hit publish — and Flo…

## What’s new and why it matters
There's a k-means clustering node in Flowfile now, and it didn't come from a release. I built it inside the app — drew the settings form, wrote one process() function, tested it against sample data, hit publish — and Flowfile opened the pull request that put it one click away for everyone else. Flowfile is an open-source, self-hosted analytics tool built on Polars: you build data pipelines on a visual canvas — where every node is also real Python — then explore, schedule, and chart the results, all on one machine you pip install . It ships with 40+ built-in nodes , and until now that was the c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/edwardvaneechoud/i-built-a-k-means-node-inside-my-etl-tool-and-the-app-opened-the-pr-to-share-it-28hj

## Related notes
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-05-28-how-i-added-dbt-cloud-to-coral-my-open-source-hackathon-journey]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
