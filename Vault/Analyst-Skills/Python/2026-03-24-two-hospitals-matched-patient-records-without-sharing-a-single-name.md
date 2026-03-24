---
title: Two Hospitals Matched Patient Records Without Sharing a Single Name
date: '2026-03-24'
source: https://dev.to/benzsevern/two-hospitals-matched-patient-records-without-sharing-a-single-name-4op4
domain: Python
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-02-a-maze-to-solve-when-youre-bored]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-28-mastering-dcl-the-ultimate-guide-to-grant-and-revoke-in-sql]]'
- '[[2026-03-21-snowflake-vs-redshift-vs-bigquery-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** Hospital A has 50,000 patient records. Hospital B has 40,000. Some patients visit both. Nobody knows which ones. They need to find the overlap — for care coordination, billing reconciliation, research. But HIPAA says nei…

## What’s new and why it matters
Hospital A has 50,000 patient records. Hospital B has 40,000. Some patients visit both. Nobody knows which ones. They need to find the overlap — for care coordination, billing reconciliation, research. But HIPAA says neither hospital can share raw patient data with the other. No names. No SSNs. No dates of birth. Nothing identifiable. So how do you match records you're not allowed to see? Bloom Filters A bloom filter is a bit array. You take a name like "John Smith," break it into character pairs ("jo", "oh", "hn", "n ", " s", "sm", "mi", "it", "th"), hash each pair into positions in the bit a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/benzsevern/two-hospitals-matched-patient-records-without-sharing-a-single-name-4op4

## Related notes
- [[2026-03-02-a-maze-to-solve-when-youre-bored]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-28-mastering-dcl-the-ultimate-guide-to-grant-and-revoke-in-sql]]
- [[2026-03-21-snowflake-vs-redshift-vs-bigquery-which-one-should-you-use]]
