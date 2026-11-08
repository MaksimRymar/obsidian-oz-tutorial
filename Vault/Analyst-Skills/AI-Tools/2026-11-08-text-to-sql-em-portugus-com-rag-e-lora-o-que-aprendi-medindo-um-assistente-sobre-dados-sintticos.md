---
title: 'Text-to-SQL em português com RAG e LoRA: o que aprendi medindo um assistente
  sobre dados sintéticos'
date: '2026-11-08'
source: https://dev.to/david_vora_61c0753239dfd/text-to-sql-em-portugues-com-rag-e-lora-o-que-aprendi-medindo-um-assistente-sobre-dados-sinteticos-46ha
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-12-data-manipulation-language-dml]]'
- '[[2026-03-23-avaliador-sinttico-como-funciona-no-pitugus]]'
- '[[2026-07-23-do-navegador-ao-banco-de-dados-o-caminho-mais-curto-para-tabelas-web]]'
- '[[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]'
- '[[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]'
- '[[2026-07-13-sql-aggregate-queries]]'
status: unread
---

> **TL;DR:** Montei um assistente que transforma perguntas em português sobre uma frota de ônibus em SQL, e passei mais tempo medindo do que construindo. Este texto conta o que funcionou, o que errou e o que os números não provam. Av…

## What’s new and why it matters
Montei um assistente que transforma perguntas em português sobre uma frota de ônibus em SQL, e passei mais tempo medindo do que construindo. Este texto conta o que funcionou, o que errou e o que os números não provam. Aviso: o InfoFrota é um experimento independente, sem vínculo com a CETURB-ES. Os dados são sintéticos ; só os rótulos de linhas vêm de um CSV aberto (CC0) da CETURBES. Nada aqui representa desempenho em operação real. 1. O problema Perguntas operacionais sobre uma frota ("quais linhas mais lotam?", "em que horário?", "e se chover?") viram consultas SQL. Escolhi um banco SQLite s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/david_vora_61c0753239dfd/text-to-sql-em-portugues-com-rag-e-lora-o-que-aprendi-medindo-um-assistente-sobre-dados-sinteticos-46ha

## Related notes
- [[2026-07-12-data-manipulation-language-dml]]
- [[2026-03-23-avaliador-sinttico-como-funciona-no-pitugus]]
- [[2026-07-23-do-navegador-ao-banco-de-dados-o-caminho-mais-curto-para-tabelas-web]]
- [[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]
- [[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]
- [[2026-07-13-sql-aggregate-queries]]
