---
title: 'S3 Select in 2026: Why New Accounts Get MethodNotAllowed, and What to Use
  Instead'
date: '2026-11-06'
source: https://dev.to/anshul_vaibhav_1f725e0621/s3-select-in-2026-why-new-accounts-get-methodnotallowed-and-what-to-use-instead-ckd
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-29-what-i-added-to-omni-sql-after-v025-local-analytics-s3-and-more]]'
- '[[2026-10-23-stop-giving-your-ai-blind-access-to-databases]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-06-25-duckdb-for-data-engineering-in-process-olap-local-etl-parquet-first-workflows]]'
- '[[2026-11-01-spark-is-lazy-and-that-one-fact-explains-most-beginner-confusion]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
status: unread
---

> **TL;DR:** SELECT * FROM S3Object s LIMIT 5 That was the query I expected to work. I had uploaded a tiny CSV to Amazon S3, checked its metadata, and previewed the contents. When I clicked Run Query in Buckets by Serverless Creed, I…

## What’s new and why it matters
SELECT * FROM S3Object s LIMIT 5 That was the query I expected to work. I had uploaded a tiny CSV to Amazon S3, checked its metadata, and previewed the contents. When I clicked Run Query in Buckets by Serverless Creed, I got this instead: The specified method is not allowed against this resource. Changing the SQL didn't resolve it. Running the equivalent operation through AWS CLI returned MethodNotAllowed too. This post follows that investigation across four scenarios in Buckets v2.8.7 and v2.8.9 . It also explains the S3 Select availability change behind a plausible diagnosis, and the alterna…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/anshul_vaibhav_1f725e0621/s3-select-in-2026-why-new-accounts-get-methodnotallowed-and-what-to-use-instead-ckd

## Related notes
- [[2026-09-29-what-i-added-to-omni-sql-after-v025-local-analytics-s3-and-more]]
- [[2026-10-23-stop-giving-your-ai-blind-access-to-databases]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-06-25-duckdb-for-data-engineering-in-process-olap-local-etl-parquet-first-workflows]]
- [[2026-11-01-spark-is-lazy-and-that-one-fact-explains-most-beginner-confusion]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
