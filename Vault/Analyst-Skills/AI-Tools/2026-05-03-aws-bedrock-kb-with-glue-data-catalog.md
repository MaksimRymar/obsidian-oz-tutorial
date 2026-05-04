---
title: AWS Bedrock KB with Glue data catalog
date: '2026-05-03'
source: https://dev.to/aws-builders/aws-bedrock-kb-with-glue-data-catalog-1j9g
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-13-understanding-sql-ddldmlfiltering-and-dcl]]'
- '[[2026-04-20-how-my-journey-has-been-into-understanding-sql]]'
- '[[2026-03-02-sql-joins-explained-case-example]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
status: unread
---

> **TL;DR:** Hi 👋, In this post we shall explore Bedrock's structured KB with this architecture: Upload CSVs to S3 > SNS Queue > Crawl data with Glue > Query with Redshift > Bedrock KB > Query with LLM . Setup Let's do some of this w…

## What’s new and why it matters
Hi 👋, In this post we shall explore Bedrock's structured KB with this architecture: Upload CSVs to S3 > SNS Queue > Crawl data with Glue > Query with Redshift > Bedrock KB > Query with LLM . Setup Let's do some of this with code. Let's get started. Clone the repo and switch to the project directory. git clone git@github.com:networkandcode/networkandcode.github.io.git cd structured-kb-demo/ Do a uv sync. uv sync Setup environment variables. $ cat .env AWS_ACCOUNT_ID = AWS_ACCESS_KEY_ID = AWS_REGION = ap-south-1 AWS_SECRET_ACCESS_KEY = BEDROCK_KB = StructKb BEDROCK_KB_IAM_POLICY = StructKbIamPol…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aws-builders/aws-bedrock-kb-with-glue-data-catalog-1j9g

## Related notes
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-13-understanding-sql-ddldmlfiltering-and-dcl]]
- [[2026-04-20-how-my-journey-has-been-into-understanding-sql]]
- [[2026-03-02-sql-joins-explained-case-example]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
