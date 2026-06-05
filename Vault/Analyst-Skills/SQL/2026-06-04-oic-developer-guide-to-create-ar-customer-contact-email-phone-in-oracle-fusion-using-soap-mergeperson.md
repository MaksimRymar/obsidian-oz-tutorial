---
title: OIC Developer Guide to Create AR Customer Contact Email & Phone in Oracle Fusion
  Using SOAP (mergePerson)
date: '2026-06-04'
source: https://dev.to/naveen6735/oic-developer-guide-to-create-ar-customer-contact-email-phone-in-oracle-fusion-using-soap-24h6
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-04-understanding-joins-and-window-functions-in-sql]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-05-31-calling-get-api-mapping-response-in-vbcs-service-connection]]'
- '[[2026-03-08-understanding-sql-joins-with-practical-examples-beginner-friendly-guide]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-04-26-unlocking-data-potential-why-sql-skills-are-a-must-have-for-developers-in-2026]]'
status: unread
---

> **TL;DR:** In Oracle Fusion, AR Customer Contacts are stored as Party Relationships . Adding or updating contact details such as phone number and email address requires interaction with the Foundation Person Service SOAP API . This…

## What’s new and why it matters
In Oracle Fusion, AR Customer Contacts are stored as Party Relationships . Adding or updating contact details such as phone number and email address requires interaction with the Foundation Person Service SOAP API . This guide walks you through: Identifying required data (PartyId & RelationshipId) Using SOAP API to create contact points Verifying data in backend tables Step 1: Identify Customer Contact Details Relationship Information select * from fusion . hz_relationships where relationship_id = 300000159607279 Party Information select * from fusion . hz_parties where party_id = 300000159607…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/naveen6735/oic-developer-guide-to-create-ar-customer-contact-email-phone-in-oracle-fusion-using-soap-24h6

## Related notes
- [[2026-03-04-understanding-joins-and-window-functions-in-sql]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-05-31-calling-get-api-mapping-response-in-vbcs-service-connection]]
- [[2026-03-08-understanding-sql-joins-with-practical-examples-beginner-friendly-guide]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-04-26-unlocking-data-potential-why-sql-skills-are-a-must-have-for-developers-in-2026]]
