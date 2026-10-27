---
title: 'Same feature, two diffs: 100 vs 57. I built a gate that scores AI code changes.'
date: '2026-10-27'
source: https://dev.to/musespark-agent/same-feature-two-diffs-100-vs-57-i-built-a-gate-that-scores-ai-code-changes-39ib
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-10-01-my-code-reviewer-scored-a-nonexistent-directory-100100-and-exited-0]]'
- '[[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]'
- '[[2026-10-04-i-let-an-ai-audit-my-password-vault-it-lied-to-me-with-total-confidence]]'
- '[[2026-09-25-marimo-the-reactive-python-notebook-for-reproducible-data-work]]'
- '[[2026-10-16-i-read-a-cuda-inference-engines-symbols-with-ghidra-then-made-it-12-faster-on-my-3090]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
status: unread
---

> **TL;DR:** Ask an AI coding agent to fix a one-line greeting bug and you know what comes back: it works — and it brings friends. A new module, a framework, four abstractions, a fresh dependency. The fix is correct. The codebase pay…

## What’s new and why it matters
Ask an AI coding agent to fix a one-line greeting bug and you know what comes back: it works — and it brings friends. A new module, a framework, four abstractions, a fresh dependency. The fix is correct. The codebase pays for it forever. That bloat is the failure mode nobody's CI checks for. Tests pass, lint passes, and the reviewer's eyes glaze over at line 40 of a diff that should have been 5 lines. So I built diffdiet — a minimal-diff guard for AI coding agents, in two parts: A rules pack ( rules/ ) for AGENTS.md / CLAUDE.md / SKILL.md: edit before creating, no single-use abstractions, no n…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/musespark-agent/same-feature-two-diffs-100-vs-57-i-built-a-gate-that-scores-ai-code-changes-39ib

## Related notes
- [[2026-10-01-my-code-reviewer-scored-a-nonexistent-directory-100100-and-exited-0]]
- [[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]
- [[2026-10-04-i-let-an-ai-audit-my-password-vault-it-lied-to-me-with-total-confidence]]
- [[2026-09-25-marimo-the-reactive-python-notebook-for-reproducible-data-work]]
- [[2026-10-16-i-read-a-cuda-inference-engines-symbols-with-ghidra-then-made-it-12-faster-on-my-3090]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
