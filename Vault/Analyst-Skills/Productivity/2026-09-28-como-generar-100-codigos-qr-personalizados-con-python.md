---
title: Como generar 100 codigos QR personalizados con Python
date: '2026-09-28'
source: https://dev.to/luis_carias_526fe58acbbb/como-generar-100-codigos-qr-personalizados-con-python-36fe
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
related:
- '[[2026-09-17-como-automatizar-la-busqueda-de-clientes-con-python]]'
- '[[2026-07-01-de-tabla-html-a-sentencias-sql-insert-en-un-clic]]'
- '[[2026-06-02-rompiendo-la-cuarta-pared-en-renpy-el-efecto-monika-y-la-esfera-matemtica-parte-1]]'
- '[[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]'
- '[[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]'
- '[[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]'
status: unread
---

> **TL;DR:** Como generar 100 codigos QR personalizados con Python Pagar $9-$29 al mes por QRs con marca de agua es absurdo. Con Python es gratis. El problema Las webs de QR te cobran suscripcion para quitar marca de agua, personaliz…

## What’s new and why it matters
Como generar 100 codigos QR personalizados con Python Pagar $9-$29 al mes por QRs con marca de agua es absurdo. Con Python es gratis. El problema Las webs de QR te cobran suscripcion para quitar marca de agua, personalizar colores o generar en lote. La solucion: qrcode + pillow pip install qrcode[pil] pillow El codigo import qrcode, csv from qrcode.image.styledpil import StyledPilImage from PIL import Image def generar_qr(dato, salida, logo=None): qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H) qr.add_data(dato) qr.make(fit=True) if logo: img = qr.make_image(image_factory…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/luis_carias_526fe58acbbb/como-generar-100-codigos-qr-personalizados-con-python-36fe

## Related notes
- [[2026-09-17-como-automatizar-la-busqueda-de-clientes-con-python]]
- [[2026-07-01-de-tabla-html-a-sentencias-sql-insert-en-un-clic]]
- [[2026-06-02-rompiendo-la-cuarta-pared-en-renpy-el-efecto-monika-y-la-esfera-matemtica-parte-1]]
- [[2026-07-04-cmo-conversar-con-tu-base-de-datos-usando-ia-un-generador-de-sql-a-partir-de-lenguaje-natural]]
- [[2026-05-11-cmo-constru-un-morning-briefing-con-ia-que-se-ejecuta-solo-cada-maana]]
- [[2026-03-12-cmo-validar-nif-nie-cif-e-iban-en-python]]
