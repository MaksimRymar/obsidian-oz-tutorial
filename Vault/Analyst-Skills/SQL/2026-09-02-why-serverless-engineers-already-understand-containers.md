---
title: Why Serverless Engineers Already Understand Containers
date: '2026-09-02'
source: https://dev.to/umairrafi/why-serverless-engineers-already-understand-containers-2mb1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-14-serverless-python-deploying-fastapi-to-google-cloud-run-with-docker]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
status: unread
---

> **TL;DR:** The outage that teaches you deployment A service passes every test locally. It fails in staging because the API calls localhost:5432 for Postgres — but Postgres is in another container, reachable only as db:5432 . This i…

## What’s new and why it matters
The outage that teaches you deployment A service passes every test locally. It fails in staging because the API calls localhost:5432 for Postgres — but Postgres is in another container, reachable only as db:5432 . This is not a Docker problem. It is a boundary problem: your code assumed an environment it does not own. Engineers who have shipped on AWS Lambda already avoid a class of these mistakes. They never SSH into a function to hot-fix. They inject config at deploy time. They treat each invocation as disposable. Containers reward the same discipline with different vocabulary. This article…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/umairrafi/why-serverless-engineers-already-understand-containers-2mb1

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-14-serverless-python-deploying-fastapi-to-google-cloud-run-with-docker]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
