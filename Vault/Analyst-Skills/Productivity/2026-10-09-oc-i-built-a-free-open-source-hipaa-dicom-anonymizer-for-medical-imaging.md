---
title: '[OC] I built a free, open-source HIPAA DICOM anonymizer for medical imaging'
date: '2026-10-09'
source: https://dev.to/kaveenai/oc-i-built-a-free-open-source-hipaa-dicom-anonymizer-for-medical-imaging-1emi
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]'
- '[[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-10-using-llms-with-patient-data-de-identifying-clinical-text-before-api-calls]]'
- '[[2026-07-20-3-lines-of-code-to-build-an-ai-team-the-10k-star-python-framework-most-people-dont-know-about]]'
status: unread
---

> **TL;DR:** I just released dicom-clean — an open-source CLI tool for HIPAA-compliant DICOM de-identification. Here's how it works and why I built it. The Problem Medical imaging files (CT scans, MRIs, X-rays) use a format called DI…

## What’s new and why it matters
I just released dicom-clean — an open-source CLI tool for HIPAA-compliant DICOM de-identification. Here's how it works and why I built it. The Problem Medical imaging files (CT scans, MRIs, X-rays) use a format called DICOM , which contains two things: Metadata — patient name, birth date, MRN, hospital, referring physician, etc. Pixel data — the actual image When hospitals want to share DICOM data for research, AI training, or vendor evaluation, they must remove the patient identifiers first — this is required by HIPAA Safe Harbor (45 CFR §164.514(b)(2)). But existing options are problematic:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kaveenai/oc-i-built-a-free-open-source-hipaa-dicom-anonymizer-for-medical-imaging-1emi

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]
- [[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-10-using-llms-with-patient-data-de-identifying-clinical-text-before-api-calls]]
- [[2026-07-20-3-lines-of-code-to-build-an-ai-team-the-10k-star-python-framework-most-people-dont-know-about]]
