---
title: Building a local video search CLI with ffmpeg and OpenCLIP
date: '2026-08-25'
source: https://dev.to/harry_xu_74d04f7a971995d5/building-a-local-video-search-cli-with-ffmpeg-and-openclip-3a5g
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
- '[[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]'
- '[[2026-06-22-build-a-profitable-ai-agent-with-langchain-a-step-by-step-tutorial]]'
status: unread
---

> **TL;DR:** I often remember the shot I want before I remember its filename. That gap is what binquery is for. It is a local Python CLI that indexes video clips and turns a sentence into a ranked shortlist for a human to review. It…

## What’s new and why it matters
I often remember the shot I want before I remember its filename. That gap is what binquery is for. It is a local Python CLI that indexes video clips and turns a sentence into a ranked shortlist for a human to review. It deliberately stops before editing: no timeline generation, no automatic cut, and no render. The smallest reproducible trial You can test the complete installed command path without supplying footage: python3 -m venv .venv .venv/bin/pip install binquery .venv/bin/binquery demo --out /tmp/binquery-demo The demo generates a synthetic 30-second video locally, then exercises splitti…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/harry_xu_74d04f7a971995d5/building-a-local-video-search-cli-with-ffmpeg-and-openclip-3a5g

## Related notes
- [[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
- [[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-08-17-test-the-ai-generated-test-in-a-throwaway-two-version-server]]
- [[2026-06-22-build-a-profitable-ai-agent-with-langchain-a-step-by-step-tutorial]]
