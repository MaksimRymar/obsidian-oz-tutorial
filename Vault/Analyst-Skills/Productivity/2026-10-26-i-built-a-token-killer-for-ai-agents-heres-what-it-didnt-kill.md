---
title: I built a token killer for AI agents. Here's what it didn't kill.
date: '2026-10-26'
source: https://dev.to/shouvik12/i-built-a-token-killer-for-ai-agents-heres-what-it-didnt-kill-12o5
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-24-pdfua-the-verapdf-failures-you-can-fix-with-30-lines-of-pikepdf-measured-on-24-files]]'
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-05-15-build-a-rag-pipeline-that-actually-reads-the-web]]'
status: unread
---

> **TL;DR:** 🔪 I built a token killer for AI agents. Here's what it didn't kill. When an agent reads a web page, it pays for the whole page. On GitHub's page for psf/requests, that's 123,176 tokens. Only 519 of them are the README. 🤯…

## What’s new and why it matters
🔪 I built a token killer for AI agents. Here's what it didn't kill. When an agent reads a web page, it pays for the whole page. On GitHub's page for psf/requests, that's 123,176 tokens. Only 519 of them are the README. 🤯 The rest is navigation menus, sign-in banners, file lists and scripts. leantext is an open-source tool (Apache-2.0) that turns what an agent reads into lean Markdown. It strips page chrome, keeps the content, checks the result against the source, and reports tokens before and after. It handles HTML pages, Word, Excel and PowerPoint files, and PDFs, including scanned ones via O…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/shouvik12/i-built-a-token-killer-for-ai-agents-heres-what-it-didnt-kill-12o5

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-24-pdfua-the-verapdf-failures-you-can-fix-with-30-lines-of-pikepdf-measured-on-24-files]]
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-05-15-build-a-rag-pipeline-that-actually-reads-the-web]]
