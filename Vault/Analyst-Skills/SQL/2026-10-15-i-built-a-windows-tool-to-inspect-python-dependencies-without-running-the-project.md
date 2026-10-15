---
title: I built a Windows tool to inspect Python dependencies without running the project
date: '2026-10-15'
source: https://dev.to/sage_melocik_2dd42c783db6/i-built-a-windows-tool-to-inspect-python-dependencies-without-running-the-project-3kcf
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-03-building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies]]'
- '[[2026-07-31-how-local-ai-became-my-247-python-tutor-without-doing-the-work-for-me]]'
- '[[2026-03-17-i-wrapped-my-free-npm-package-as-a-paid-rest-api-heres-the-architecture]]'
- '[[2026-10-13-i-built-a-local-windows-seo-audit-tool-for-freelancers-and-what-it-deliberately-doesnt-do]]'
- '[[2026-07-13-how-i-built-an-automated-web-vulnerability-scanner-with-python-and-owasp-zap]]'
- '[[2026-10-14-how-to-turn-google-maps-scraper-output-into-a-scored-local-seo-lead-list]]'
status: unread
---

> **TL;DR:** Ever inherited a Python project and wondered which third-party packages it actually uses? That's the problem behind ImportSmith 1.0 , a Windows desktop utility from RooTech. ImportSmith performs static inspection of Pyth…

## What’s new and why it matters
Ever inherited a Python project and wondered which third-party packages it actually uses? That's the problem behind ImportSmith 1.0 , a Windows desktop utility from RooTech. ImportSmith performs static inspection of Python source code. It identifies imports, helps map them to likely distributions, compares observed imports with declared dependencies, and exports reports for review. Crucially, it doesn't execute the project being inspected . Static analysis has limits: dynamic imports, optional dependencies, and ambiguous module names need human review. The results are a starting point for depe…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sage_melocik_2dd42c783db6/i-built-a-windows-tool-to-inspect-python-dependencies-without-running-the-project-3kcf

## Related notes
- [[2026-09-03-building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies]]
- [[2026-07-31-how-local-ai-became-my-247-python-tutor-without-doing-the-work-for-me]]
- [[2026-03-17-i-wrapped-my-free-npm-package-as-a-paid-rest-api-heres-the-architecture]]
- [[2026-10-13-i-built-a-local-windows-seo-audit-tool-for-freelancers-and-what-it-deliberately-doesnt-do]]
- [[2026-07-13-how-i-built-an-automated-web-vulnerability-scanner-with-python-and-owasp-zap]]
- [[2026-10-14-how-to-turn-google-maps-scraper-output-into-a-scored-local-seo-lead-list]]
