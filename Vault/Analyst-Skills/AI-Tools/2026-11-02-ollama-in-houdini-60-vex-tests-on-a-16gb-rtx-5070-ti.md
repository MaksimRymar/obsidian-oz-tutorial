---
title: 'Ollama in Houdini: 60 VEX Tests on a 16GB RTX 5070 Ti'
date: '2026-11-02'
source: https://dev.to/alicia_lu/ollama-in-houdini-60-vex-tests-on-a-16gb-rtx-5070-ti-32bf
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]'
- '[[2026-10-17-batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives]]'
status: unread
---

> **TL;DR:** Originally published by Alicia on 2 November 2026 at Digital Garden . Original measurements and limitations are retained. A local Ollama endpoint worked from Houdini 22, but fast VEX replies were often wrong. In 60 froze…

## What’s new and why it matters
Originally published by Alicia on 2 November 2026 at Digital Garden . Original measurements and limitations are retained. A local Ollama endpoint worked from Houdini 22, but fast VEX replies were often wrong. In 60 frozen trials on an RTX 5070 Ti, Qwen2.5-Coder 7B and 14B each passed 5/30 first attempts. With at most two compiler or semantic feedback repairs, they reached 8/30 and 11/30. I kept all 156 generated snippets unchanged. This is a controlled point-attribute study in headless Houdini 22.0.429 , using owned synthetic fixtures. It does not measure an open garden viewport, artist produc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/alicia_lu/ollama-in-houdini-60-vex-tests-on-a-16gb-rtx-5070-ti-32bf

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]
- [[2026-10-17-batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives]]
