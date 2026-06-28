---
title: 'Testing fourpointo Against Malicious Uploads: Prompt Injection and Stored
  XSS'
date: '2026-06-28'
source: https://dev.to/zeyrian_faris/testing-fourpointo-against-malicious-uploads-prompt-injection-and-stored-xss-23a9
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-06-16-3-fastapi-patterns-i-use-in-every-project]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-05-08-how-i-built-an-api-that-cuts-llm-token-costs-by-11-22]]'
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** fourpointo is a self-hosted Flask app I built that generates AI-powered task checklists and rubric breakdowns from uploaded assignment PDFs. It uses Groq's LLaMA 3.3 70B for extraction, SQLite for storage and Gunicorn be…

## What’s new and why it matters
fourpointo is a self-hosted Flask app I built that generates AI-powered task checklists and rubric breakdowns from uploaded assignment PDFs. It uses Groq's LLaMA 3.3 70B for extraction, SQLite for storage and Gunicorn behind a Cloudflare Tunnel. After fixing a magic-byte validation bug found during normal use (a fake PDF was causing an unhandled crash in PyMuPDF), I wanted to go further and actually probe the upload pipeline the way an attacker might. This writeup documents that process: the setup, the test cases and the results. All testing was done locally in a Kali VM against a local copy o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/zeyrian_faris/testing-fourpointo-against-malicious-uploads-prompt-injection-and-stored-xss-23a9

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-06-16-3-fastapi-patterns-i-use-in-every-project]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-05-08-how-i-built-an-api-that-cuts-llm-token-costs-by-11-22]]
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
