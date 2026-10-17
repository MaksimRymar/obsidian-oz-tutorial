---
title: How much GPU energy does fp16 save? Measured on a Tesla T4
date: '2026-10-17'
source: https://dev.to/bsharma173860oss/how-much-gpu-energy-does-fp16-save-measured-on-a-tesla-t4-4e08
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-14-google-jobs-results-as-json-for-1-per-1000-jobs-no-proxies-no-browser]]'
- '[[2026-10-17-batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives]]'
- '[[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]'
- '[[2026-10-16-i-read-a-cuda-inference-engines-symbols-with-ghidra-then-made-it-12-faster-on-my-3090]]'
status: unread
---

> **TL;DR:** How much GPU energy does fp16 actually save over fp32? Spec sheets give TDP and peak FLOPS, not joules per job, so I measured it on a Tesla T4 using the GPU's own NVML energy counter. The job import sys , torch dtype = {…

## What’s new and why it matters
How much GPU energy does fp16 actually save over fp32? Spec sheets give TDP and peak FLOPS, not joules per job, so I measured it on a Tesla T4 using the GPU's own NVML energy counter. The job import sys , torch dtype = { " fp16 " : torch . float16 , " fp32 " : torch . float32 }[ sys . argv [ 1 ]] a = torch . randn ( 8192 , 8192 , device = " cuda " , dtype = dtype ) for _ in range ( 100 ): b = a @ a torch . cuda . synchronize () fp16 and fp32 runs alternate (so temperature and clock drift hit both sides), 5 measured runs each, medians reported, Mann-Whitney test between the two. Results: the wh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bsharma173860oss/how-much-gpu-energy-does-fp16-save-measured-on-a-tesla-t4-4e08

## Related notes
- [[2026-08-08-how-full-text-search-works-in-pure-python-a-tour-with-whoosh]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-14-google-jobs-results-as-json-for-1-per-1000-jobs-no-proxies-no-browser]]
- [[2026-10-17-batch-converting-500-pngs-to-jpg-i-timed-my-pillow-script-against-the-alternatives]]
- [[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]
- [[2026-10-16-i-read-a-cuda-inference-engines-symbols-with-ghidra-then-made-it-12-faster-on-my-3090]]
