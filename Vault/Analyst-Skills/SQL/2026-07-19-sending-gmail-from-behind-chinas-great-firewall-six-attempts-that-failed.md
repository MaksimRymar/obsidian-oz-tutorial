---
title: Sending Gmail from behind China's Great Firewall — six attempts that failed
date: '2026-07-19'
source: https://dev.to/baolin_tikool_43da6f2b56f/sending-gmail-from-behind-chinas-great-firewall-six-attempts-that-failed-1khf
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-05-i-automated-oauth-token-renewal-for-a-headless-ai-agent-it-was-harder-than-the-actual-work]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]'
- '[[2026-06-24-i-got-tired-of-cryptic-python-error-messages-so-i-built-a-vs-code-extension-that-fixes-them-automatically]]'
status: unread
---

> **TL;DR:** Last night I needed to send one email to support@creem.io from Guangzhou, China. Simple email — 15 minutes to draft. Sending it took over an hour. Here's what I learned about the six most common ways to send Gmail from m…

## What’s new and why it matters
Last night I needed to send one email to support@creem.io from Guangzhou, China. Simple email — 15 minutes to draft. Sending it took over an hour. Here's what I learned about the six most common ways to send Gmail from mainland China programmatically, and what finally worked. Everything starts with SMTP Habitual first try — Python smtplib with the Gmail app password: import smtplib , ssl s = smtplib . SMTP_SSL ( ' smtp.gmail.com ' , 465 , context = ssl . create_default_context ()) s . login ( user , app_password ) s . send_message ( msg ) ssl.SSLEOFError: EOF occurred in violation of protocol…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/baolin_tikool_43da6f2b56f/sending-gmail-from-behind-chinas-great-firewall-six-attempts-that-failed-1khf

## Related notes
- [[2026-03-05-i-automated-oauth-token-renewal-for-a-headless-ai-agent-it-was-harder-than-the-actual-work]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]
- [[2026-06-24-i-got-tired-of-cryptic-python-error-messages-so-i-built-a-vs-code-extension-that-fixes-them-automatically]]
