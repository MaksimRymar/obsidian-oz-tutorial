---
title: How to usar CTEs para consultas SQL mais legiveis
date: '2026-07-11'
source: https://dev.to/isaias_velasquez_d2261770/how-to-usar-ctes-para-consultas-sql-mais-legiveis-19d2
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tutorial'
related:
- '[[2026-07-11-how-to-criar-indices-no-sql-que-realmente-fazem-diferenca]]'
- '[[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]'
- '[[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]'
- '[[2026-02-27-jsonb-e-gin-index-otimizando-consultas-no-postgresql]]'
- '[[2026-03-05-a-pegadinha-do-auto-incremento-como-o-serial-do-postgresql-se-compara-a-outros-sgbds]]'
- '[[2026-07-11-how-to-versionar-o-banco-de-dados-com-flyway-sem-medo]]'
status: unread
---

> **TL;DR:** CTEs (Common Table Expressions) tornam consultas SQL mais legiveis ao dividir logicas complexas em blocos nomeados. E como criar variaveis temporarias dentro da query. A sintaxe basica: WITH vendas_recentes AS ( SELECT *…

## What’s new and why it matters
CTEs (Common Table Expressions) tornam consultas SQL mais legiveis ao dividir logicas complexas em blocos nomeados. E como criar variaveis temporarias dentro da query. A sintaxe basica: WITH vendas_recentes AS ( SELECT * FROM vendas WHERE data >= '2025-01-01' ) SELECT cliente_id, SUM(valor) as total FROM vendas_recentes GROUP BY cliente_id ORDER BY total DESC; O WITH define um bloco temporario chamado vendas_recentes . A query principal usa esse bloco como se fosse uma tabela. CTEs sao uteis para reutilizar a mesma subconsulta em varios lugares: WITH gastos_por_cliente AS ( SELECT cliente_id,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/isaias_velasquez_d2261770/how-to-usar-ctes-para-consultas-sql-mais-legiveis-19d2

## Related notes
- [[2026-07-11-how-to-criar-indices-no-sql-que-realmente-fazem-diferenca]]
- [[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]
- [[2026-04-07-writing-sql-that-doesnt-come-back-to-haunt-you]]
- [[2026-02-27-jsonb-e-gin-index-otimizando-consultas-no-postgresql]]
- [[2026-03-05-a-pegadinha-do-auto-incremento-como-o-serial-do-postgresql-se-compara-a-outros-sgbds]]
- [[2026-07-11-how-to-versionar-o-banco-de-dados-com-flyway-sem-medo]]
