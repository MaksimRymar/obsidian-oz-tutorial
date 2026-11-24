---
title: 'CUR 2.0 in AWS Data Exports: the bucket, the export from the CLI, the SQL
  query, and where the files land'
date: '2026-11-24'
source: https://dev.to/gonzalogjuka/cur-20-in-aws-data-exports-the-bucket-the-export-from-the-cli-the-sql-query-and-where-the-6mk
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-11-23-sql-group-by-and-having-find-your-top-customers-and-3000-key-accounts-in-eight-rows-of-orders]]'
- '[[2026-10-24-sql-the-monthly-revenue-report-in-five-lines-group-by-month-instead-of-a-spreadsheet-every-month-end]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** The short answer: CUR 2.0 is not created on the old Cost and Usage Reports screen but in AWS Data Exports, as a "Standard data export" on the COST_AND_USAGE_REPORT table. You can do it from the console (Billing and Cost…

## What’s new and why it matters
The short answer: CUR 2.0 is not created on the old Cost and Usage Reports screen but in AWS Data Exports, as a "Standard data export" on the COST_AND_USAGE_REPORT table. You can do it from the console (Billing and Cost Management → Data Exports → Create export) or with aws bcm-data-exports create-export , and the API has a single endpoint, in us-east-1 ( bcm-data-exports.us-east-1.api.aws , per the Billing endpoints list ). Before you create it, the S3 bucket has to let the bcm-data-exports.amazonaws.com service write to it. If what you want is what CUR is and how it compares with the Azure a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gonzalogjuka/cur-20-in-aws-data-exports-the-bucket-the-export-from-the-cli-the-sql-query-and-where-the-6mk

## Related notes
- [[2026-11-23-sql-group-by-and-having-find-your-top-customers-and-3000-key-accounts-in-eight-rows-of-orders]]
- [[2026-10-24-sql-the-monthly-revenue-report-in-five-lines-group-by-month-instead-of-a-spreadsheet-every-month-end]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
