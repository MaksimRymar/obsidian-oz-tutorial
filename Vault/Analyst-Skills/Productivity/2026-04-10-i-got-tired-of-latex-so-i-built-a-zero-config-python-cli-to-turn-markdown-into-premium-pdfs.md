---
title: I got tired of LaTeX, so I built a zero-config Python CLI to turn Markdown
  into premium PDFs
date: '2026-04-10'
source: https://dev.to/leonardosalasd/i-got-tired-of-latex-so-i-built-a-zero-config-python-cli-to-turn-markdown-into-premium-pdfs-oob
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-04-03-i-am-building-a-notebook-environment-for-sql-inside-a-database-client]]'
- '[[2026-04-01-i-built-a-portable-siem-detection-toolkit-that-converts-sigma-rules-to-splunk-elastic-and-kibana-queries]]'
- '[[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
- '[[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
status: unread
---

> **TL;DR:** Have you ever just wanted to turn your standard README.md into a nice, academic-looking PDF without having to install a 2GB LaTeX environment or write a 500-line config file? Same here. I was tired of dealing with comple…

## What’s new and why it matters
Have you ever just wanted to turn your standard README.md into a nice, academic-looking PDF without having to install a 2GB LaTeX environment or write a 500-line config file? Same here. I was tired of dealing with complex setups just to export some documentation, so I built a pure Python solution: doc-engine-cli . How it works under the hood I used mistune to parse the Markdown AST natively and safely in memory. Then, instead of hooking it up to a classic HTML-to-PDF engine (which usually misplaces margins and page breaks), I routed the parsed blocks directly into the lightning-fast Typst comp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/leonardosalasd/i-got-tired-of-latex-so-i-built-a-zero-config-python-cli-to-turn-markdown-into-premium-pdfs-oob

## Related notes
- [[2026-04-03-i-am-building-a-notebook-environment-for-sql-inside-a-database-client]]
- [[2026-04-01-i-built-a-portable-siem-detection-toolkit-that-converts-sigma-rules-to-splunk-elastic-and-kibana-queries]]
- [[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
- [[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
