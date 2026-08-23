---
title: I Got 28 TPS Out of Free Kaggle GPUs. Here's What It Took.
date: '2026-08-23'
source: https://dev.to/rautaditya2606/i-got-28-tps-out-of-free-kaggle-gpus-heres-what-it-took-5dpl
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-07-24-alpha-to-beta-bringing-in-qa]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
status: unread
---

> **TL;DR:** I want to be upfront about something: this whole project runs on free Kaggle T4 notebooks, an AWS EC2 t3.micro relay that costs almost nothing, and public internet. No A100s. No private datacenter network. No budget. And…

## What’s new and why it matters
I want to be upfront about something: this whole project runs on free Kaggle T4 notebooks, an AWS EC2 t3.micro relay that costs almost nothing, and public internet. No A100s. No private datacenter network. No budget. And yet, ShardFlow v2.1 hits 28.10 TPS peak on Qwen2.5-7B across two separate cloud regions over WAN. This is the story of how that happened, and specifically the one fix in v2.1 that I did not see coming. The Problem: Running a 7B Model When You Have No Money A 7B parameter model in FP16 needs roughly 15 GB of VRAM. A single Kaggle T4 has 16 GB. Technically it fits, barely, with…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/rautaditya2606/i-got-28-tps-out-of-free-kaggle-gpus-heres-what-it-took-5dpl

## Related notes
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-07-24-alpha-to-beta-bringing-in-qa]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
