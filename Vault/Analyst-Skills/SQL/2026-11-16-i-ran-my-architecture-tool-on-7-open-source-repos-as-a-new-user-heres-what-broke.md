---
title: I ran my architecture tool on 7 open-source repos as a new user. Here's what
  broke.
date: '2026-11-16'
source: https://dev.to/sauvast/i-ran-my-architecture-tool-on-7-open-source-repos-as-a-new-user-heres-what-broke-1c4n
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-10-14-43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]'
status: unread
---

> **TL;DR:** ArchiLens reads a Git repository, builds a module dependency graph from real imports, draws C4-style diagrams, checks architecture rules, and posts an architecture diff on pull requests. I had tested it on its own codeba…

## What’s new and why it matters
ArchiLens reads a Git repository, builds a module dependency graph from real imports, draws C4-style diagrams, checks architecture rules, and posts an architecture diff on pull requests. I had tested it on its own codebase for months. Then I installed it from PyPI as a stranger would and pointed it at seven projects I didn't write: Flask, FastAPI, Django, Express, NestJS, Spring PetClinic and gin. Each run was the same four commands: archilens init archilens analyze --repo . archilens check --repo . archilens diff --base < previous release > --head < latest release > --ai Nothing I'd call an e…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sauvast/i-ran-my-architecture-tool-on-7-open-source-repos-as-a-new-user-heres-what-broke-1c4n

## Related notes
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-10-14-43-days-17040-ai-signals-four-things-the-data-says-that-trend-lists-wont-tell-you]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]
