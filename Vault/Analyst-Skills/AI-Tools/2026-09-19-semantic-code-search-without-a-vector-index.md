---
title: Semantic code search without a vector index
date: '2026-09-19'
source: https://dev.to/zaydmulani09/semantic-code-search-without-a-vector-index-3elj
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]'
- '[[2026-08-24-new-advancements-in-generative-ai]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** Every "AI code search" tool released this year does the same thing under the hood: chunk your repo, embed every chunk, stuff the vectors into an index, and keep that index in sync every time you commit. GitLab Duo does i…

## What’s new and why it matters
Every "AI code search" tool released this year does the same thing under the hood: chunk your repo, embed every chunk, stuff the vectors into an index, and keep that index in sync every time you commit. GitLab Duo does it. Sourcegraph does it. JetBrains shipped a whole RAG pipeline for it. It works, but it means you're maintaining a second copy of your codebase that can drift out of sync with the first one, and on a repo that changes fast, "rebuild the index" becomes its own chore. I wanted semantic search that didn't need that. So I built jevgrep, and it skips the index entirely. The actual m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/zaydmulani09/semantic-code-search-without-a-vector-index-3elj

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]
- [[2026-08-24-new-advancements-in-generative-ai]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
