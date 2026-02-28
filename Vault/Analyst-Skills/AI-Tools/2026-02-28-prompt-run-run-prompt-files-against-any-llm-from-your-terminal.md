---
title: 'prompt-run: Run .prompt files against any LLM from your terminal'
date: '2026-02-28'
source: https://dev.to/maneesh_thakur_d16c2852fa/prompt-run-run-prompt-files-against-any-llm-from-your-terminal-1f7n
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-22-automate-signate-competition-submissions-with-a-cli-tool-signate-deploy]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
status: unread
---

> **TL;DR:** The post Prompts buried in Python strings. No git history. No way to diff two versions. No clean way to swap models. I got tired of it. So I built prompt-run — a CLI tool that treats .prompt files as first-class runnable…

## What’s new and why it matters
The post Prompts buried in Python strings. No git history. No way to diff two versions. No clean way to swap models. I got tired of it. So I built prompt-run — a CLI tool that treats .prompt files as first-class runnable artifacts. Quickstart (60 seconds) pip install "prompt-run[anthropic]" export ANTHROPIC_API_KEY = "sk-ant-..." prompt run examples/summarize.prompt --var text = "LLMs are changing software development." What a .prompt file looks like --- name : summarize description : Summarizes text into bullet points model : claude-sonnet-4-6 provider : anthropic temperature : 0.3 max_tokens…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/maneesh_thakur_d16c2852fa/prompt-run-run-prompt-files-against-any-llm-from-your-terminal-1f7n

## Related notes
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-22-automate-signate-competition-submissions-with-a-cli-tool-signate-deploy]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
