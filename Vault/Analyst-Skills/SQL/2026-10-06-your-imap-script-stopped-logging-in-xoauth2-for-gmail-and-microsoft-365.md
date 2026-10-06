---
title: 'Your IMAP script stopped logging in: XOAUTH2 for Gmail and Microsoft 365'
date: '2026-10-06'
source: https://dev.to/mahirhir/your-imap-script-stopped-logging-in-xoauth2-for-gmail-and-microsoft-365-5480
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-09-send-emails-with-python-automate-notifications-reports-and-alerts-beginner-guide]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
status: unread
---

> **TL;DR:** If you have a small Python script that logs in to Gmail or Microsoft 365 over IMAP with a username and password, there's a good chance it already gets AUTHENTICATE failed or Invalid credentials back, even with the right…

## What’s new and why it matters
If you have a small Python script that logs in to Gmail or Microsoft 365 over IMAP with a username and password, there's a good chance it already gets AUTHENTICATE failed or Invalid credentials back, even with the right password. Both providers have moved IMAP to OAuth 2.0, and the IMAP side of that is a SASL mechanism called XOAUTH2 . This post covers why the password path closed, what XOAUTH2 actually sends over the wire, where the access token comes from, and how long it lives. The worked example uses mail-rule-digest , a stdlib-only Python CLI I wrote that filters a mailbox with a TOML rul…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/mahirhir/your-imap-script-stopped-logging-in-xoauth2-for-gmail-and-microsoft-365-5480

## Related notes
- [[2026-08-09-send-emails-with-python-automate-notifications-reports-and-alerts-beginner-guide]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
