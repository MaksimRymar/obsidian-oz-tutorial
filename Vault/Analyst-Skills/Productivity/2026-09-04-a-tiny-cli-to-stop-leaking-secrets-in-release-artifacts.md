---
title: A tiny CLI to stop leaking secrets in release artifacts
date: '2026-09-04'
source: https://dev.to/commonstudio/a-tiny-cli-to-stop-leaking-secrets-in-release-artifacts-396g
domain: Productivity
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]'
- '[[2026-06-18-how-i-built-a-local-tool-that-maps-any-codebase-in-55-seconds-no-cloud-no-uploads]]'
- '[[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
status: unread
---

> **TL;DR:** I ship a lot of small digital products. Every time I bundle a PDF, a zip, or a tar, I run the same paranoid check: did any of these files contain something that should never leave my workspace? API keys, internal hostnam…

## What’s new and why it matters
I ship a lot of small digital products. Every time I bundle a PDF, a zip, or a tar, I run the same paranoid check: did any of these files contain something that should never leave my workspace? API keys, internal hostnames, operator names, project codenames — the kind of things that slip into a draft PDF layer or a Markdown file and then get packed into a release. I automated that check into a single Python file called leakcheck . What it does leakcheck scans a directory of release artifacts for a configurable list of forbidden strings. It handles: plain text files PDF text layers (via PyPDF2…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/commonstudio/a-tiny-cli-to-stop-leaking-secrets-in-release-artifacts-396g

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]
- [[2026-06-18-how-i-built-a-local-tool-that-maps-any-codebase-in-55-seconds-no-cloud-no-uploads]]
- [[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
