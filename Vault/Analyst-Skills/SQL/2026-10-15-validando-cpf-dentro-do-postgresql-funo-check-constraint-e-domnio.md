---
title: 'Validando CPF dentro do PostgreSQL: função, CHECK constraint e domínio'
date: '2026-10-15'
source: https://dev.to/cpfhub/validando-cpf-dentro-do-postgresql-funcao-check-constraint-e-dominio-3432
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-12-data-definition-language-ddl]]'
- '[[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]'
- '[[2026-07-12-data-manipulation-language-dml]]'
- '[[2026-07-13-sql-data-constraints]]'
- '[[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]'
- '[[2026-07-22-sql-views]]'
status: unread
---

> **TL;DR:** Transparência: sou fundador da CPFHub, citada no final. O conteúdo é puramente SQL e não depende de nenhum serviço. Validar CPF só na aplicação deixa uma porta aberta: scripts de importação, outro microsserviço, um UPDAT…

## What’s new and why it matters
Transparência: sou fundador da CPFHub, citada no final. O conteúdo é puramente SQL e não depende de nenhum serviço. Validar CPF só na aplicação deixa uma porta aberta: scripts de importação, outro microsserviço, um UPDATE manual feito às pressas. Se o banco é a fonte da verdade, faz sentido que ele recuse CPFs malformados. Vamos implementar isso no PostgreSQL. 1. Função de validação CREATE OR REPLACE FUNCTION cpf_valido ( p text ) RETURNS boolean LANGUAGE plpgsql IMMUTABLE STRICT PARALLEL SAFE AS $$ DECLARE d text : = regexp_replace ( p , ' \D ' , '' , 'g' ); soma int ; dv int ; BEGIN IF lengt…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cpfhub/validando-cpf-dentro-do-postgresql-funcao-check-constraint-e-dominio-3432

## Related notes
- [[2026-07-12-data-definition-language-ddl]]
- [[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]
- [[2026-07-12-data-manipulation-language-dml]]
- [[2026-07-13-sql-data-constraints]]
- [[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]
- [[2026-07-22-sql-views]]
