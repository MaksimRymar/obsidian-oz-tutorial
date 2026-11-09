---
title: My STL to CAD tool can now give you a rounded box you can edit with one number
date: '2026-11-09'
source: https://dev.to/emirmrkaljevic/my-stl-to-cad-tool-can-now-give-you-a-rounded-box-you-can-edit-with-one-number-2phf
domain: Productivity
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#productivity'
- '#tool'
related:
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-07-28-a-safety-gate-inside-a-face-swap-tool-or-how-the-nsfw-check-is-wired-into-the-pipeline]]'
- '[[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]'
status: unread
---

> **TL;DR:** When you download a rounded enclosure as an STL, every round corner is just hundreds of tiny triangles. If you want the corners a bit softer, or a hole 1 mm bigger, you usually redraw the whole part. I have been working…

## What’s new and why it matters
When you download a rounded enclosure as an STL, every round corner is just hundreds of tiny triangles. If you want the corners a bit softer, or a hole 1 mm bigger, you usually redraw the whole part. I have been working on mesh2cad , an open source tool that turns STL meshes of simple mechanical parts back into editable CAD. Over the last few releases (0.20.0 to 0.23.0) it learned to handle a box where every edge is rounded. What changed 0.20.0: a fully rounded box is rebuilt as an exact STEP solid: 6 planes, 12 cylinders and 8 sphere corners, instead of a triangle soup. 0.21.0: the same box i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/emirmrkaljevic/my-stl-to-cad-tool-can-now-give-you-a-rounded-box-you-can-edit-with-one-number-2phf

## Related notes
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-07-28-a-safety-gate-inside-a-face-swap-tool-or-how-the-nsfw-check-is-wired-into-the-pipeline]]
- [[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]
