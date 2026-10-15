---
title: 'pdfkit says "No wkhtmltopdf executable found" on Debian 13: HTML to PDF without
  the binary'
date: '2026-10-15'
source: https://dev.to/hiver/pdfkit-says-no-wkhtmltopdf-executable-found-on-debian-13-html-to-pdf-without-the-binary-541o
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-07-17-how-to-use-the-google-flights-api-in-2026-python-mcp-and-a-no-code-shortcut]]'
- '[[2026-07-25-google-images-scraper-how-to-bulk-export-image-search-results-as-json-in-2026]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
status: unread
---

> **TL;DR:** If you rebuilt a Python image on python:3.13-slim recently and your invoice or report PDFs stopped, this is probably the error: OSError: No wkhtmltopdf executable found pdfkit (about 3 million downloads a month on PyPI)…

## What’s new and why it matters
If you rebuilt a Python image on python:3.13-slim recently and your invoice or report PDFs stopped, this is probably the error: OSError: No wkhtmltopdf executable found pdfkit (about 3 million downloads a month on PyPI) and imgkit are thin wrappers around the wkhtmltopdf binary. That binary's repository was archived after its last push in November 2022, and Debian removed the package from testing on 2025-02-05. Debian 13 is the base of the current python:3.13-slim image, so apt-get install wkhtmltopdf finds nothing. We checked this on Debian 13 on 2026-10-12 with pdfkit 1.0.0: pdfkit.from_url(…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/hiver/pdfkit-says-no-wkhtmltopdf-executable-found-on-debian-13-html-to-pdf-without-the-binary-541o

## Related notes
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-07-17-how-to-use-the-google-flights-api-in-2026-python-mcp-and-a-no-code-shortcut]]
- [[2026-07-25-google-images-scraper-how-to-bulk-export-image-search-results-as-json-in-2026]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
