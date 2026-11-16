---
title: datasette-llm 0.1a11：通过 OpenAI 兼容接口接入本地模型
date: '2026-11-15'
source: https://dev.to/arthur1988/datasette-llm-01a11tong-guo-openai-jian-rong-jie-kou-jie-ru-ben-di-mo-xing-4oj
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-09-07-gate-agent-success-on-closed-spans]]'
- '[[2026-11-06-reconcile-a-dashboard-number-with-the-source-table-in-sql]]'
- '[[2026-02-25-glue-ai-agents-to-enterprise-data-with-universal-sql]]'
- '[[2026-03-30-dataai-a-local-ai-database-client-from-plain-language-to-executable-sql]]'
- '[[2026-10-27-sqlcmd-scripting-variable-not-defined-why-breaks-your-script-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** 更新要点：支持 OpenAI 兼容接口 datasette-llm 是 Datasette 的大语言模型配置中间层插件，负责为其他 Datasette 插件配置模型。 0.1a11 版本新增了 OpenAI 兼容接口支持 。只要模型服务提供兼容接口，就可以接入 Datasette，不必限定模型的部署位置。对于通过 LM Studio、Ollama 或 llama.cpp 运行本地模型的开发者，这也提供了将本地模型与 Datasette…

## What’s new and why it matters
更新要点：支持 OpenAI 兼容接口 datasette-llm 是 Datasette 的大语言模型配置中间层插件，负责为其他 Datasette 插件配置模型。 0.1a11 版本新增了 OpenAI 兼容接口支持 。只要模型服务提供兼容接口，就可以接入 Datasette，不必限定模型的部署位置。对于通过 LM Studio、Ollama 或 llama.cpp 运行本地模型的开发者，这也提供了将本地模型与 Datasette Agent 连接起来的方式。 对于关注本地模型与数据工具集成的 写好标智库 读者，这次更新值得关注的重点是：模型服务通过兼容接口接入后，可以配合 Datasette Agent 完成数据库对话查询。 配置示例：连接 LM Studio 下面通过 uvx 启动 Datasette，并加载 datasette-agent 。运行前需要准备： 一个可用的 content.db 数据库文件。 已启动的本地模型服务。 与实际服务一致的接口地址和模型名称。 uvx --with datasette-agent datasette \ --root --secret 1 \ -s plugins.datasette-llm.default_model '{ "model": "lmstudio-qwen", "model_name": "qwen/qwen3.8-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/arthur1988/datasette-llm-01a11tong-guo-openai-jian-rong-jie-kou-jie-ru-ben-di-mo-xing-4oj

## Related notes
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-09-07-gate-agent-success-on-closed-spans]]
- [[2026-11-06-reconcile-a-dashboard-number-with-the-source-table-in-sql]]
- [[2026-02-25-glue-ai-agents-to-enterprise-data-with-universal-sql]]
- [[2026-03-30-dataai-a-local-ai-database-client-from-plain-language-to-executable-sql]]
- [[2026-10-27-sqlcmd-scripting-variable-not-defined-why-breaks-your-script-and-how-to-fix-it]]
