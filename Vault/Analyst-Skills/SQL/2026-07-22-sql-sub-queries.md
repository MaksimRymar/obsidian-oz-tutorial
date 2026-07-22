---
title: 'SQL: Sub Queries'
date: '2026-07-22'
source: https://dev.to/yuripeixinho/sql-sub-queries-18c
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-07-13-sql-aggregate-queries]]'
- '[[2026-07-12-data-manipulation-language-dml]]'
- '[[2026-07-13-sql-join-queries]]'
- '[[2026-07-22-sql-views]]'
- '[[2026-07-12-sql-keyword-tipos-de-dados-operators]]'
- '[[2026-07-13-sql-data-constraints]]'
status: unread
---

> **TL;DR:** Introdução Uma subquery é uma consulta SQL aninhada dentro de outra. Assim como uma função pode chamar outra função, um SELECT pode conter outro SELECT — e o resultado do interno é usado pelo externo para filtrar, calcul…

## What’s new and why it matters
Introdução Uma subquery é uma consulta SQL aninhada dentro de outra. Assim como uma função pode chamar outra função, um SELECT pode conter outro SELECT — e o resultado do interno é usado pelo externo para filtrar, calcular ou compor o resultado final. Subqueries aparecem em três lugares possíveis: no SELECT , no FROM , ou no WHERE / HAVING . O comportamento muda dependendo do tipo de resultado que a subquery retorna — e é aí que a classificação em Scalar, Column, Row e Table faz sentido. Para os exemplos, usaremos: clientes : id , nome , cidade pedidos : id , cliente_id , valor , criado_em pro…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yuripeixinho/sql-sub-queries-18c

## Related notes
- [[2026-07-13-sql-aggregate-queries]]
- [[2026-07-12-data-manipulation-language-dml]]
- [[2026-07-13-sql-join-queries]]
- [[2026-07-22-sql-views]]
- [[2026-07-12-sql-keyword-tipos-de-dados-operators]]
- [[2026-07-13-sql-data-constraints]]
