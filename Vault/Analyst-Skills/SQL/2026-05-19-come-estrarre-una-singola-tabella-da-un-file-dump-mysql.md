---
title: Come estrarre una singola tabella da un file dump MySQL
date: '2026-05-19'
source: https://dev.to/minnogit/come-estrarre-una-singola-tabella-da-un-file-dump-mysql-35jm
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-09-nlp-in-azienda-dai-chatbot-allanalisi-testuale]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
- '[[2026-04-13-understanding-sql-ddldmlfiltering-and-dcl]]'
- '[[2026-02-26-mensajes-de-whatsapp-iniciados-por-el-agente-desde-amazon-connect]]'
- '[[2026-02-23-sql-dump-cli]]'
status: unread
---

> **TL;DR:** Ti è mai capitato di dover ripristinare una sola tabella ma di avere a disposizione solo un file dump .sql gigante dell'intero database? Invece di perdere tempo cercando di aprire un file da svariati gigabyte con un edit…

## What’s new and why it matters
Ti è mai capitato di dover ripristinare una sola tabella ma di avere a disposizione solo un file dump .sql gigante dell'intero database? Invece di perdere tempo cercando di aprire un file da svariati gigabyte con un editor di testo, o peggio, importare tutto il database su un server locale solo per recuperare poche righe, c'è un trucco da riga di comando velocissimo che sfrutta sed : sed -n -e '/DROP TABLE.*`nome_tabella`/,/UNLOCK TABLES/p' dump_completo.sql > backup_singola_tabella.sql Otterrai un nuovo file chiamato backup_singola_tabella.sql contenente esclusivamente la struttura e i dati d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/minnogit/come-estrarre-una-singola-tabella-da-un-file-dump-mysql-35jm

## Related notes
- [[2026-03-09-nlp-in-azienda-dai-chatbot-allanalisi-testuale]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
- [[2026-04-13-understanding-sql-ddldmlfiltering-and-dcl]]
- [[2026-02-26-mensajes-de-whatsapp-iniciados-por-el-agente-desde-amazon-connect]]
- [[2026-02-23-sql-dump-cli]]
