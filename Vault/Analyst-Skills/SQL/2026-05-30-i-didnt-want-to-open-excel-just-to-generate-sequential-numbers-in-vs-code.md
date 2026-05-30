---
title: I Didn't Want to Open Excel Just to Generate Sequential Numbers in VS Code
date: '2026-05-30'
source: https://dev.to/almiraj/i-didnt-want-to-open-excel-just-to-generate-sequential-numbers-in-vs-code-508h
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
status: unread
---

> **TL;DR:** While working in VS Code, I occasionally need sequential numbers. Something like this: user_001 user_002 user_003 Or test data for SQL: INSERT INTO users ( id , name , created_at ) VALUES ( 1 , 'testA' , '2026-05-28 10:0…

## What’s new and why it matters
While working in VS Code, I occasionally need sequential numbers. Something like this: user_001 user_002 user_003 Or test data for SQL: INSERT INTO users ( id , name , created_at ) VALUES ( 1 , 'testA' , '2026-05-28 10:00:00' ); INSERT INTO users ( id , name , created_at ) VALUES ( 2 , 'testB' , '2026-05-28 10:00:01' ); INSERT INTO users ( id , name , created_at ) VALUES ( 3 , 'testC' , '2026-05-28 10:00:02' ); Of course, I could open Excel and use formulas. But somehow that always felt wrong. I was already in VS Code. I wanted to stay in VS Code. VS Code Is Surprisingly Weak at Sequential Num…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/almiraj/i-didnt-want-to-open-excel-just-to-generate-sequential-numbers-in-vs-code-508h

## Related notes
- [[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-04-08-understanding-python-loops-a-beginner-friendly-guide]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
