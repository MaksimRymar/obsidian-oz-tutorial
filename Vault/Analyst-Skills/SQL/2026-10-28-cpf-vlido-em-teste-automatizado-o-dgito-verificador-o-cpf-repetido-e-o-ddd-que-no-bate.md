---
title: 'CPF válido em teste automatizado: o dígito verificador, o CPF repetido e o
  DDD que não bate'
date: '2026-10-28'
source: https://dev.to/evpaula/cpf-valido-em-teste-automatizado-o-digito-verificador-o-cpf-repetido-e-o-ddd-que-nao-bate-5gna
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-04-21-constru-uma-biblioteca-python-que-unifica-apis-de-mercado-financeiro-brasileiro]]'
- '[[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]'
- '[[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]'
- '[[2026-07-22-sql-melhores-prticas-de-segurana]]'
- '[[2026-06-09-do-pdf-ao-discord-com-rag-como-constru-um-agente-rag-para-eliminar-interrupes-operacionais-na-empresa]]'
- '[[2026-10-04-brasil-x-argentina-como-desmontar-a-falcia-do-crescimento-com-dados-e-uma-analogia-com-gado]]'
status: unread
---

> **TL;DR:** Quase todo sistema brasileiro tem um formulário que pede CPF. E quase toda suíte de teste desse sistema tem, em algum canto, um "123.456.789-09" fixo no código. Funciona por um tempo. Depois aparecem três problemas, quas…

## What’s new and why it matters
Quase todo sistema brasileiro tem um formulário que pede CPF. E quase toda suíte de teste desse sistema tem, em algum canto, um "123.456.789-09" fixo no código. Funciona por um tempo. Depois aparecem três problemas, quase sempre nesta ordem. 1. O CPF repetido 123.456.789-09 passa no dígito verificador. O problema começa quando o segundo teste cadastra outro usuário com o mesmo CPF e o banco devolve duplicate key value violates unique constraint . A saída de sempre é uma lista de CPFs "que funcionam" num arquivo compartilhado, que ninguém sabe de onde veio e que acaba no meio dos dados de produ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/evpaula/cpf-valido-em-teste-automatizado-o-digito-verificador-o-cpf-repetido-e-o-ddd-que-nao-bate-5gna

## Related notes
- [[2026-04-21-constru-uma-biblioteca-python-que-unifica-apis-de-mercado-financeiro-brasileiro]]
- [[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]
- [[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]
- [[2026-07-22-sql-melhores-prticas-de-segurana]]
- [[2026-06-09-do-pdf-ao-discord-com-rag-como-constru-um-agente-rag-para-eliminar-interrupes-operacionais-na-empresa]]
- [[2026-10-04-brasil-x-argentina-como-desmontar-a-falcia-do-crescimento-com-dados-e-uma-analogia-com-gado]]
