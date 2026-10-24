---
title: Testando um agente de IA antes de deixar ele escrever no CRM (com pytest)
date: '2026-10-24'
source: https://dev.to/jhonatan_alvesdasilva_5/testando-um-agente-de-ia-antes-de-deixar-ele-escrever-no-crm-com-pytest-4kb0
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]'
- '[[2026-06-09-do-pdf-ao-discord-com-rag-como-constru-um-agente-rag-para-eliminar-interrupes-operacionais-na-empresa]]'
- '[[2026-07-13-sql-data-constraints]]'
- '[[2026-08-13-hello-world]]'
- '[[2026-10-15-validando-cpf-dentro-do-postgresql-funo-check-constraint-e-domnio]]'
- '[[2026-02-25-construindo-seu-prprio-bi-com-python-o-fim-do-vendor-lock-in-duckdb-marimo-e-polars]]'
status: unread
---

> **TL;DR:** Agente de IA conectado ao CRM costuma ser testado assim: manda umas mensagens no WhatsApp, vê se a resposta ficou boa e libera. Só que a resposta boa não diz nada sobre o que foi gravado no banco . A ideia aqui é tirar o…

## What’s new and why it matters
Agente de IA conectado ao CRM costuma ser testado assim: manda umas mensagens no WhatsApp, vê se a resposta ficou boa e libera. Só que a resposta boa não diz nada sobre o que foi gravado no banco . A ideia aqui é tirar o LLM da equação e testar a camada que decide gravar. O modelo devolve uma proposta de ação, e o backend valida antes de executar. Essa camada é código determinístico, então dá para cobrir com testes comuns. A camada de decisão # decisao.py import unicodedata import phonenumbers def chave_nome ( nome : str ) -> str : """ Chave só para BUSCAR possíveis duplicados. Nunca para sobr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jhonatan_alvesdasilva_5/testando-um-agente-de-ia-antes-de-deixar-ele-escrever-no-crm-com-pytest-4kb0

## Related notes
- [[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]
- [[2026-06-09-do-pdf-ao-discord-com-rag-como-constru-um-agente-rag-para-eliminar-interrupes-operacionais-na-empresa]]
- [[2026-07-13-sql-data-constraints]]
- [[2026-08-13-hello-world]]
- [[2026-10-15-validando-cpf-dentro-do-postgresql-funo-check-constraint-e-domnio]]
- [[2026-02-25-construindo-seu-prprio-bi-com-python-o-fim-do-vendor-lock-in-duckdb-marimo-e-polars]]
