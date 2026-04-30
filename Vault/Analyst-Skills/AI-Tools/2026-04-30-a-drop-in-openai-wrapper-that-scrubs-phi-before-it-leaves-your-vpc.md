---
title: A drop-in OpenAI wrapper that scrubs PHI before it leaves your VPC
date: '2026-04-30'
source: https://dev.to/tiamatenity/a-drop-in-openai-wrapper-that-scrubs-phi-before-it-leaves-your-vpc-2nk4
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-04-10-using-llms-with-patient-data-de-identifying-clinical-text-before-api-calls]]'
- '[[2026-03-11-promptlab-test-and-compare-llm-prompts-from-your-terminal-open-source]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-04-07-the-missing-infrastructure-for-agent-commerce]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
status: unread
---

> **TL;DR:** Healthcare AI builders keep tripping the same wire. You ship a chatbot. Someone pastes a patient note into it. The note hits OpenAI. OpenAI hasn't signed your BAA. You now have a HIPAA breach and a compliance officer wit…

## What’s new and why it matters
Healthcare AI builders keep tripping the same wire. You ship a chatbot. Someone pastes a patient note into it. The note hits OpenAI. OpenAI hasn't signed your BAA. You now have a HIPAA breach and a compliance officer with a clipboard. The fix everyone reaches for is "just write a regex" and then six months later they discover their regex didn't catch the DEA number, or treated 1234567890 as a phone instead of an NPI, or missed the email because someone wrote it as john [at] example.com . I spent today building the version I wish existed. The drop-in from scrubbed_openai import ScrubbedOpenAI c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tiamatenity/a-drop-in-openai-wrapper-that-scrubs-phi-before-it-leaves-your-vpc-2nk4

## Related notes
- [[2026-04-10-using-llms-with-patient-data-de-identifying-clinical-text-before-api-calls]]
- [[2026-03-11-promptlab-test-and-compare-llm-prompts-from-your-terminal-open-source]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-04-07-the-missing-infrastructure-for-agent-commerce]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
