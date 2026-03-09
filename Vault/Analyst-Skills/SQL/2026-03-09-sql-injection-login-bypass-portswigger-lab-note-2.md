---
title: 'SQL Injection – Login Bypass | PortSwigger Lab Note #2'
date: '2026-03-09'
source: https://dev.to/kenny-cipher/sql-injection-login-bypass-portswigger-lab-note-2-557e
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]'
- '[[2026-03-04-sqlite-as-an-mcp-context-saver-stop-cramming-raw-api-data-into-your-llm]]'
- '[[2026-03-04-bulletproof-data-pipelines-adding-schema-validation-to-nike-scrapers]]'
- '[[2026-02-28-say-goodbye-to-manual-refreshing-building-an-ai-medical-appointment-agent-with-playwright-and-llms]]'
- '[[2026-03-02-i-built-a-tool-to-find-your-h1b-wage-level-by-zip-code-openh1borg]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
status: unread
---

> **TL;DR:** target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-subverting-application-logic/sql-injection/lab-login-bypass Tools Used: browser Burp suite Vulnerability Summary： Type: SQL…

## What’s new and why it matters
target： Lab URL: https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-subverting-application-logic/sql-injection/lab-login-bypass Tools Used: browser Burp suite Vulnerability Summary： Type: SQL Injection Description: This lab contains a SQL injection vulnerability in the login function. To solve the lab, perform a SQL injection attack that logs in to the application as the administrator user. Steps to Exploit： 1.First of all, check the login interface. Then enter arbitrary values for the account and password. 2.Submit arbitrary values and use Burp to intercept the re…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kenny-cipher/sql-injection-login-bypass-portswigger-lab-note-2-557e

## Related notes
- [[2026-03-07-where-clause-allowing-retrieval-of-hidden-data-sql-injection-vulnerability]]
- [[2026-03-04-sqlite-as-an-mcp-context-saver-stop-cramming-raw-api-data-into-your-llm]]
- [[2026-03-04-bulletproof-data-pipelines-adding-schema-validation-to-nike-scrapers]]
- [[2026-02-28-say-goodbye-to-manual-refreshing-building-an-ai-medical-appointment-agent-with-playwright-and-llms]]
- [[2026-03-02-i-built-a-tool-to-find-your-h1b-wage-level-by-zip-code-openh1borg]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
