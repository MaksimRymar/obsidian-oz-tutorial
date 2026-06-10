---
title: Your schema validation passes and the agent still picks the wrong tool. The
  bug is semantic.
date: '2026-06-10'
source: https://dev.to/james_oconnor_dev/your-schema-validation-passes-and-the-agent-still-picks-the-wrong-tool-the-bug-is-semantic-2i41
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-wins-in-2026]]'
- '[[2026-05-26-from-screen-recording-to-test-cases-in-seconds-meet-clipcase]]'
- '[[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]'
status: unread
---

> **TL;DR:** Pydantic and JSON-schema guarantee the shape of a tool call. They say nothing about whether it was the right call for the user's intent. TL;DR: We put strict Pydantic validation on every tool call our agent makes, expect…

## What’s new and why it matters
Pydantic and JSON-schema guarantee the shape of a tool call. They say nothing about whether it was the right call for the user's intent. TL;DR: We put strict Pydantic validation on every tool call our agent makes, expecting tool-call failures to drop. They barely did. When I categorized 40 logged failures, 31 of them passed schema validation cleanly. They were well-formed calls to the wrong tool, or the right tool with arguments that were valid types but wrong values. Schema validation catches structural errors. Our actual problem was semantic, and the validator is blind to it. What schema val…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/james_oconnor_dev/your-schema-validation-passes-and-the-agent-still-picks-the-wrong-tool-the-bug-is-semantic-2i41

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-wins-in-2026]]
- [[2026-05-26-from-screen-recording-to-test-cases-in-seconds-meet-clipcase]]
- [[2026-03-17-a-3rd-year-cs-students-attempt-to-reduce-ais-water-footprint-ecocache-a-python-library]]
