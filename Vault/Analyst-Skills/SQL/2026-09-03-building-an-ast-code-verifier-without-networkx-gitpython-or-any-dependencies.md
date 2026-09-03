---
title: Building an AST Code Verifier Without NetworkX, GitPython, or Any Dependencies
date: '2026-09-03'
source: https://dev.to/urjit_upadhyay/building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies-20dd
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]'
- '[[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]'
- '[[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]'
- '[[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-saves-you-money-in-2026]]'
status: unread
---

> **TL;DR:** You end up learning why those packages exist in the first place. For the Zero Dependency Hackathon 2026, I built Proofline, a pure Python static analysis tool that works as a verification gate for code changes. The main…

## What’s new and why it matters
You end up learning why those packages exist in the first place. For the Zero Dependency Hackathon 2026, I built Proofline, a pure Python static analysis tool that works as a verification gate for code changes. The main rule for the project was simple: No third-party dependencies. So there was no networkx, no GitPython, no pre-commit, no fastapi, and no watchdog. Everything had to be built using Python's standard library. What is Proofline? The idea behind Proofline came from working with AI-generated code. Most linters are great at finding things like syntax issues, formatting problems, unuse…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/urjit_upadhyay/building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies-20dd

## Related notes
- [[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-05-15-stop-passing-entire-chat-histories-to-ai-agents]]
- [[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]
- [[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]
- [[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-saves-you-money-in-2026]]
