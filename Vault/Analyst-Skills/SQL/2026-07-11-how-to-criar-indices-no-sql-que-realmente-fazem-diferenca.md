---
title: How to criar indices no SQL que realmente fazem diferenca
date: '2026-07-11'
source: https://dev.to/isaias_velasquez_d2261770/how-to-criar-indices-no-sql-que-realmente-fazem-diferenca-lp6
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tutorial'
related:
- '[[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]'
- '[[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]'
- '[[2026-03-01-normalizao-de-banco-de-dados-das-origens-s-5-formas-normais-bcnf-com-exemplos-prticos]]'
- '[[2026-07-07-as-12-regras-de-codd-o-que-torna-um-banco-de-dados-realmente-relacional]]'
- '[[2026-03-05-a-pegadinha-do-auto-incremento-como-o-serial-do-postgresql-se-compara-a-outros-sgbds]]'
- '[[2026-06-02-window-functions-no-sql-o-que-so-e-como-diferem-do-group-by]]'
status: unread
---

> **TL;DR:** Ter um indice certo pode fazer uma query ir de 10 segundos para milissegundos. Mas indices demais ou errados atrapalham mais que ajudam. O comando basico para criar um indice: CREATE INDEX idx_clientes_email ON clientes(…

## What’s new and why it matters
Ter um indice certo pode fazer uma query ir de 10 segundos para milissegundos. Mas indices demais ou errados atrapalham mais que ajudam. O comando basico para criar um indice: CREATE INDEX idx_clientes_email ON clientes(email); Isso acelera buscas por email . Sem o indice, o banco faz uma varredura completa na tabela. Para indices compostos (mais de uma coluna): CREATE INDEX idx_pedidos_cliente_data ON pedidos(cliente_id, data_criacao); A ordem das colunas importa. Esse indice ajuda queries que filtram por cliente_id ou por cliente_id + data_criacao . Mas nao ajuda queries que filtram so por d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/isaias_velasquez_d2261770/how-to-criar-indices-no-sql-que-realmente-fazem-diferenca-lp6

## Related notes
- [[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]
- [[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]
- [[2026-03-01-normalizao-de-banco-de-dados-das-origens-s-5-formas-normais-bcnf-com-exemplos-prticos]]
- [[2026-07-07-as-12-regras-de-codd-o-que-torna-um-banco-de-dados-realmente-relacional]]
- [[2026-03-05-a-pegadinha-do-auto-incremento-como-o-serial-do-postgresql-se-compara-a-outros-sgbds]]
- [[2026-06-02-window-functions-no-sql-o-que-so-e-como-diferem-do-group-by]]
