---
title: 'SAP Business One: query de contas a receber vencidas por faixa de atraso (aging)
  em SQL Server'
date: '2026-10-29'
source: https://dev.to/sheetsandsql_br/sap-business-one-query-de-contas-a-receber-vencidas-por-faixa-de-atraso-aging-em-sql-server-161g
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]'
- '[[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]'
- '[[2026-07-11-how-to-usar-ctes-para-consultas-sql-mais-legiveis]]'
- '[[2026-07-12-data-manipulation-language-dml]]'
- '[[2026-07-22-sql-views]]'
- '[[2026-07-22-sql-sub-queries]]'
status: unread
---

> **TL;DR:** Quem dá suporte a SAP Business One cedo ou tarde ouve do financeiro: "me passa quanto está vencido por cliente, separado por faixa de atraso". Dá para resolver com uma query só, direto nas tabelas de documentos de nota d…

## What’s new and why it matters
Quem dá suporte a SAP Business One cedo ou tarde ouve do financeiro: "me passa quanto está vencido por cliente, separado por faixa de atraso". Dá para resolver com uma query só, direto nas tabelas de documentos de nota de saída. As tabelas que entram OINV : cabeçalho das notas fiscais de saída (A/R Invoice). Campos usados: CardCode , CardName , DocNum , DocDate , DocDueDate , DocTotal , PaidToDate , DocStatus e CANCELED . O saldo em aberto de cada nota é DocTotal - PaidToDate . Nota com DocStatus = 'O' está aberta, e CANCELED = 'N' tira as canceladas. A query SELECT T0 . CardCode , T0 . CardNa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sheetsandsql_br/sap-business-one-query-de-contas-a-receber-vencidas-por-faixa-de-atraso-aging-em-sql-server-161g

## Related notes
- [[2026-06-25-de-tabela-html-a-insert-sql-em-um-clique]]
- [[2026-02-20-python-opensearch-e-bi-construindo-dashboards-em-tempo-real]]
- [[2026-07-11-how-to-usar-ctes-para-consultas-sql-mais-legiveis]]
- [[2026-07-12-data-manipulation-language-dml]]
- [[2026-07-22-sql-views]]
- [[2026-07-22-sql-sub-queries]]
