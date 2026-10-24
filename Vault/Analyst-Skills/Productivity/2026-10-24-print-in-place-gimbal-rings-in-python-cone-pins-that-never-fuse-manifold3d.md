---
title: 'Print-in-place gimbal rings in Python: cone pins that never fuse (manifold3d)'
date: '2026-10-24'
source: https://dev.to/blackspectre512/print-in-place-gimbal-rings-in-python-cone-pins-that-never-fuse-manifold3d-4ob1
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#support-analytics'
related:
- '[[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-10-24-generate-print-in-place-flexi-toys-with-python-and-manifold3d]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
status: unread
---

> **TL;DR:** Nested gimbal rings are a nice print-in-place test: every ring has to turn freely, and nothing may fuse. This post builds four rings and a globe in Python with manifold3d , and shows the three mistakes that fused my firs…

## What’s new and why it matters
Nested gimbal rings are a nice print-in-place test: every ring has to turn freely, and nothing may fuse. This post builds four rings and a globe in Python with manifold3d , and shows the three mistakes that fused my first attempts. 1. A ring is a revolved rectangle from manifold3d import Manifold as Mf , CrossSection as CS w , t = 4.4 , 4.0 # radial width, thickness def ring ( R ): return Mf . revolve ( CS . square ([ w , t ], True ). translate ([ R , 0 ]), 96 ) revolve spins the profile around Z, so the ring lies in the XY plane. Rotate it with .rotate([90,0,0]) and so on to get the other pla…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/blackspectre512/print-in-place-gimbal-rings-in-python-cone-pins-that-never-fuse-manifold3d-4ob1

## Related notes
- [[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-10-24-generate-print-in-place-flexi-toys-with-python-and-manifold3d]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
