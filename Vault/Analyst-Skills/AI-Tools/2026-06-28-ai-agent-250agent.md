---
title: AI Agent 崩溃的根源与解法——从250个测试用例看Agent可靠性
date: '2026-06-28'
source: https://dev.to/wzg0911/ai-agent-beng-kui-de-gen-yuan-yu-jie-fa-cong-250ge-ce-shi-yong-li-kan-agentke-kao-xing-2j5e
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-03-25-actionlib-how-i-cut-my-agents-token-usage-by-97]]'
- '[[2026-04-24-started-giving-my-agents-my-credit-card]]'
- '[[2026-04-20-try-asqav-in-30-seconds]]'
- '[[2026-03-28-the-execution-guard-pattern-for-ai-agents]]'
- '[[2026-04-04-9-mcp-resilience-patterns-that-keep-ai-agents-alive-in-production-with-code]]'
- '[[2026-04-14-claude-api-tool-use-in-production-retry-logic-token-budgets-error-handling]]'
status: unread
---

> **TL;DR:** 根因一：工具调用的非确定性 Agent 的核心范式是"LLM 推理 → 选择工具 → 执行 → 观察结果 → 再推理"。这个链路里最脆弱的一环，是 LLM 选择工具这一步。 同样的 prompt，同样的上下文，你跑 10 次可能拿到 8 种不同的 function call 组合。有时候它调了正确的工具但传错参数，有时候它觉得"要不我再想想"然后死循环，有时候它直接跳过工具调用了——因为它"认为"自己知道答案。 我们在测试里见过一个典型…

## What’s new and why it matters
根因一：工具调用的非确定性 Agent 的核心范式是"LLM 推理 → 选择工具 → 执行 → 观察结果 → 再推理"。这个链路里最脆弱的一环，是 LLM 选择工具这一步。 同样的 prompt，同样的上下文，你跑 10 次可能拿到 8 种不同的 function call 组合。有时候它调了正确的工具但传错参数，有时候它觉得"要不我再想想"然后死循环，有时候它直接跳过工具调用了——因为它"认为"自己知道答案。 我们在测试里见过一个典型案例：Agent 被要求"检查所有服务器的磁盘使用率"，它正确地调了 list_servers ，拿到 42 台机器后， 只检查了前 3 台的磁盘，然后说"其余的都正常" 。它编的。 这是 LLM 的根本特性，不是 bug。你不可能靠 prompt engineering 完全消除。 解法：幂等守卫 (Idempotency Guard) ARK Trust 的做法是给每个工具调用加一层校验层： 参数校验 ：独立于 LLM 的 schema 校验，不依赖 prompt 里的"请确保参数正确" 调用去重 ：如果 LLM 连续两次发出完全相同的 function call，守卫会拦截并追问"你是认真的吗？" 关键操作拦截 ：标记为 destructive 的工具（delete、truncate、rm）强制走 approval 流程，绕不过去 这层校验跑在…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wzg0911/ai-agent-beng-kui-de-gen-yuan-yu-jie-fa-cong-250ge-ce-shi-yong-li-kan-agentke-kao-xing-2j5e

## Related notes
- [[2026-03-25-actionlib-how-i-cut-my-agents-token-usage-by-97]]
- [[2026-04-24-started-giving-my-agents-my-credit-card]]
- [[2026-04-20-try-asqav-in-30-seconds]]
- [[2026-03-28-the-execution-guard-pattern-for-ai-agents]]
- [[2026-04-04-9-mcp-resilience-patterns-that-keep-ai-agents-alive-in-production-with-code]]
- [[2026-04-14-claude-api-tool-use-in-production-retry-logic-token-budgets-error-handling]]
