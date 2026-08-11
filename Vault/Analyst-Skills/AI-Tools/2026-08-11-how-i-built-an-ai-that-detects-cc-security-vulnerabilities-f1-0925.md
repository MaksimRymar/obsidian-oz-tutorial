---
title: How I Built an AI That Detects C/C++ Security Vulnerabilities (F1 0.925)
date: '2026-08-11'
source: https://dev.to/alyabbas11/how-i-built-an-ai-that-detects-cc-security-vulnerabilities-f1-0925-4ifp
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
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-03-30-i-couldnt-afford-an-a100-so-i-built-a-surgical-weight-editor-in-rust]]'
- '[[2026-04-30-how-to-serve-mistral-medium-35-128b-without-running-out-of-gpu-memory]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** Finder of one bug in a million lines is still sleeping, but the models have started watching. Static analysis tools like Flawfinder and Cppcheck have been the industry standard for years, but they work on predefined rule…

## What’s new and why it matters
Finder of one bug in a million lines is still sleeping, but the models have started watching. Static analysis tools like Flawfinder and Cppcheck have been the industry standard for years, but they work on predefined rules. They miss what they were never told to look for. This is the story of SecureScan AI — a deep learning model that reads C/C++ source code like a language model reads text, and flags vulnerabilities the way a code reviewer would. We built it for our Deep Learning lab at Air University Lahore, and it runs as a free web demo at securescan-ai.vercel.app . Why CodeBERT instead of…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/alyabbas11/how-i-built-an-ai-that-detects-cc-security-vulnerabilities-f1-0925-4ifp

## Related notes
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-03-30-i-couldnt-afford-an-a100-so-i-built-a-surgical-weight-editor-in-rust]]
- [[2026-04-30-how-to-serve-mistral-medium-35-128b-without-running-out-of-gpu-memory]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
