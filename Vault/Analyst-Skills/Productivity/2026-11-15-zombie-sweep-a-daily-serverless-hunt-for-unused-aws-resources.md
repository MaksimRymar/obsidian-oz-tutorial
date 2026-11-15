---
title: 'Zombie Sweep: A Daily Serverless Hunt for Unused AWS Resources'
date: '2026-11-15'
source: https://dev.to/aws-builders/zombie-sweep-a-daily-serverless-hunt-for-unused-aws-resources-1ph1
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-21-find-the-aws-resources-nobody-is-using-and-what-they-cost-you]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-21-which-sql-database-should-you-install]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
status: unread
---

> **TL;DR:** This article provides a step by step guide to building a daily sweep for unused AWS resources with AWS Step Functions, AWS Lambda, Amazon DynamoDB, Amazon S3 and Amazon CloudFront. Each region runs zombiescan's checks be…

## What’s new and why it matters
This article provides a step by step guide to building a daily sweep for unused AWS resources with AWS Step Functions, AWS Lambda, Amazon DynamoDB, Amazon S3 and Amazon CloudFront. Each region runs zombiescan's checks beside AWS Compute Optimizer's idle recommendations, and one report prices what both found. Repository: https://github.com/xbill9/zombie-sweep Live report: https://diomvue77lcq.cloudfront.net/ Demo video: youtu.be/pb8_4G7hu-M What Is a Zombie Resource? A zombie resource is something that still bills and no longer does any work. An Elastic IP attached to nothing, a container repos…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aws-builders/zombie-sweep-a-daily-serverless-hunt-for-unused-aws-resources-1ph1

## Related notes
- [[2026-09-21-find-the-aws-resources-nobody-is-using-and-what-they-cost-you]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-21-which-sql-database-should-you-install]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
