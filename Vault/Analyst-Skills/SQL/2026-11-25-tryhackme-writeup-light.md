---
title: tryhackme-write_up-light-
date: '2026-11-25'
source: https://dev.to/maivermic_z/tryhackme-writeup-light--2o4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-28-sql-basics]]'
- '[[2026-10-03-hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column]]'
- '[[2026-10-06-can-we-build-an-ai-agent-thatll-kill-udemy]]'
- '[[2026-10-23-stop-giving-your-ai-blind-access-to-databases]]'
- '[[2026-10-14-how-to-open-a-sqlite-database-query-and-explore-your-data]]'
- '[[2026-09-08-column-must-appear-in-the-group-by-clause-why-sql-wont-let-you-do-that]]'
status: unread
---

> **TL;DR:** In this CTF, we explore a database application called "Light" reachable via a TCP socket. The main challenge is to perform an SQL Injection to retrieve the administrator's credentials and the flag. Connection First, we e…

## What’s new and why it matters
In this CTF, we explore a database application called "Light" reachable via a TCP socket. The main challenge is to perform an SQL Injection to retrieve the administrator's credentials and the flag. Connection First, we establish a TCP socket connection to the target service on port 1337: nc MACHINE_IP 1337 Once connected, we interact with the login prompt. Step 1: SQL Injection Discovery we write smokey the example in the THM and then after we see the password , We try to see if the application is vulnerable to SQL Injection by inputting a single quote ': Please enter your username: ' UniOn Se…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/maivermic_z/tryhackme-writeup-light--2o4

## Related notes
- [[2026-10-28-sql-basics]]
- [[2026-10-03-hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column]]
- [[2026-10-06-can-we-build-an-ai-agent-thatll-kill-udemy]]
- [[2026-10-23-stop-giving-your-ai-blind-access-to-databases]]
- [[2026-10-14-how-to-open-a-sqlite-database-query-and-explore-your-data]]
- [[2026-09-08-column-must-appear-in-the-group-by-clause-why-sql-wont-let-you-do-that]]
