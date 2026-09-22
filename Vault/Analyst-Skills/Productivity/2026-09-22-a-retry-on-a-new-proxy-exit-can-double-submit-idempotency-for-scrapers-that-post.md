---
title: 'A Retry on a New Proxy Exit Can Double-Submit: Idempotency for Scrapers That
  POST'
date: '2026-09-22'
source: https://dev.to/thordata-flora/a-retry-on-a-new-proxy-exit-can-double-submit-idempotency-for-scrapers-that-post-3fih
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-07-30-how-to-batch-moderate-existing-posts-and-comments-with-an-llm-classification-api]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** Most scraping advice assumes you only ever GET. And for a lot of collection work, that is true: you fetch a page, you parse it, and if the request dies halfway you just fire it again. GET is idempotent by contract, so a…

## What’s new and why it matters
Most scraping advice assumes you only ever GET. And for a lot of collection work, that is true: you fetch a page, you parse it, and if the request dies halfway you just fire it again. GET is idempotent by contract, so a duplicate costs you nothing but bandwidth. Then one day your job has to POST. Maybe you are submitting a search form that a site only answers with JSON after a real POST body. Maybe you are driving an authenticated internal API where each call enqueues a task, files a claim, places a bid, or writes a row. Maybe you are posting to a moderation queue. The moment the request has a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thordata-flora/a-retry-on-a-new-proxy-exit-can-double-submit-idempotency-for-scrapers-that-post-3fih

## Related notes
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-07-30-how-to-batch-moderate-existing-posts-and-comments-with-an-llm-classification-api]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-04-21-what-happens-to-your-mutual-fund-between-9-am-and-9-pm]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
