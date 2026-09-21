---
title: Find the AWS Resources Nobody Is Using, and What They Cost You
date: '2026-09-21'
source: https://dev.to/aws-builders/find-the-aws-resources-nobody-is-using-and-what-they-cost-you-35bj
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-08-05-decision-record-an-in-app-saas-chatbot-api-with-one-key-and-durable-transcripts]]'
status: unread
---

> **TL;DR:** This article provides a step by step guide to auditing an AWS account for resources nothing is using, pricing each finding from the AWS Price List API, and cleaning up the ones you choose. A suite of Python checks is bui…

## What’s new and why it matters
This article provides a step by step guide to auditing an AWS account for resources nothing is using, pricing each finding from the AWS Price List API, and cleaning up the ones you choose. A suite of Python checks is built to cover storage, compute, networking, data services and the account-wide services that sit outside any region. https://github.com/xbill9/zombiescan What Gets Left Behind A volume survives the instance it was attached to. An Elastic IP outlives the migration that freed it. A NAT gateway keeps running in a VPC whose workload was torn down last year. Each one bills every hour…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aws-builders/find-the-aws-resources-nobody-is-using-and-what-they-cost-you-35bj

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-08-05-decision-record-an-in-app-saas-chatbot-api-with-one-key-and-durable-transcripts]]
