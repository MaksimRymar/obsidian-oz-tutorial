---
title: Why GitHub Cannot Paginate Through Millions of Repositories - Deep Pagination
  Explained
date: '2026-08-03'
source: https://dev.to/mayank7924/why-github-silently-caps-your-search-at-1000-results-and-whats-actually-happening-underneath-1oik
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]'
status: unread
---

> **TL;DR:** You've paginated through a big result set before. Page 2 loads fine. Page 200 takes a beat. Nobody stops to ask why — until something like this shows up instead of a slow page: { "message" : "Only the first 1000 search r…

## What’s new and why it matters
You've paginated through a big result set before. Page 2 loads fine. Page 200 takes a beat. Nobody stops to ask why — until something like this shows up instead of a slow page: { "message" : "Only the first 1000 search results are available." , "documentation_url" : "https://docs.github.com/v3/search/" , "status" : "422" } That's GitHub's own search API. Ask it for page 9 or page 10 of a search and you get real results. Ask for page 11 and you get that, on purpose, every time. I went and looked at why. Full video below, written breakdown after it for anyone who'd rather read. Reproducing it No…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mayank7924/why-github-silently-caps-your-search-at-1000-results-and-whats-actually-happening-underneath-1oik

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]
