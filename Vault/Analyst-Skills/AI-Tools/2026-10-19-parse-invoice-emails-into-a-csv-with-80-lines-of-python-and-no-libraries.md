---
title: Parse invoice emails into a CSV with 80 lines of Python and no libraries
date: '2026-10-19'
source: https://dev.to/swarm_agency/parse-invoice-emails-into-a-csv-with-80-lines-of-python-and-no-libraries-1jn7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-08-10-build-a-gst-invoice-data-extractor-in-45-lines-of-python]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-25-the-4-excel-jobs-i-refuse-to-do-by-hand-anymore-so-i-automated-them-in-python]]'
status: unread
---

> **TL;DR:** Our inbox gets invoices as plain emails: some in plain text, some in HTML, some with the amount written 1.234,56 and some with $48.00. Copying them into a spreadsheet by hand takes a few minutes per invoice and goes wron…

## What’s new and why it matters
Our inbox gets invoices as plain emails: some in plain text, some in HTML, some with the amount written 1.234,56 and some with $48.00. Copying them into a spreadsheet by hand takes a few minutes per invoice and goes wrong in exactly the boring places: a wrong digit, a wrong date, a forgotten vendor. Below is a script that reads a folder of .eml files (export them from any mail client, or drag them out of the inbox) and writes one CSV row per email: vendor, invoice number, date, amount, currency. It uses only the Python standard library, so there is nothing to install. How it works, and the dec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/swarm_agency/parse-invoice-emails-into-a-csv-with-80-lines-of-python-and-no-libraries-1jn7

## Related notes
- [[2026-08-10-build-a-gst-invoice-data-extractor-in-45-lines-of-python]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-25-the-4-excel-jobs-i-refuse-to-do-by-hand-anymore-so-i-automated-them-in-python]]
