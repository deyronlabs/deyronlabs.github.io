---
title: "Anthropic opens Enterprise Frontier Safeguards in public beta with misuse monitoring that fits zero data retention"
summary: "Anthropic says Enterprise Frontier Safeguards (EFS) is now in public beta for business customers who use zero data retention. Safety data goes to the customer's own storage, and flagged cases produce a Safety Case without inputs and outputs. EFS runs on the Claude Platform and major cloud providers."
seoTitle: "Anthropic Enterprise Frontier Safeguards beta"
seoDescription: "Anthropic put Enterprise Frontier Safeguards in public beta on 23 Nov 2026: misuse monitoring that stays compatible with zero data retention."
lang: en
publishedAt: 2026-11-24T18:15:00Z
entities:
  - Anthropic
  - Claude Platform
  - Amazon Bedrock
  - Claude on Google Cloud
topics:
  - Safety
  - Enterprise
  - Security
image: /images/news/anthropic-enterprise-frontier-safeguards-beta.jpg
imageAlt: "Deyron Labs graphic: Anthropic Enterprise Frontier Safeguards enters public beta, misuse monitoring compatible with zero data retention"
translationKey: anthropic-enterprise-frontier-safeguards-beta
sources:
  - title: "Zero data retention with Enterprise Frontier Safeguards is now in beta"
    url: "https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards"
    publisher: "Anthropic, 23 November 2026"
    primary: true
---

## What happened

On 23 November 2026 Anthropic published an article saying that Enterprise Frontier Safeguards (EFS), announced in September, is now open in public beta. According to Anthropic, EFS "provides state-of-the-art detection of sophisticated misuse, while remaining compatible with zero data retention (ZDR)". We read the article on 24 November 2026.

## Key details

- **How it works, per Anthropic:** a second layer of automated safety monitoring looks for patterns of misuse across many requests. It writes safety data to the customer's own storage (Amazon S3 or Google Cloud Storage). When risk is found it creates a "Safety Case" for review; Safety Cases do not include inputs and outputs.
- **ZDR terms, per Anthropic:** Anthropic and the cloud provider do not retain data; there is no operator human review; inputs and outputs are used only for monitoring, never for training, and are deleted promptly after being written to the customer's storage.
- **Availability:** the Claude Platform, Claude Platform on AWS, Amazon Bedrock and Claude on Google Cloud. Support in Microsoft Foundry is "coming soon". Eligible customers "will be notified with instructions on how to get started". Storage costs are billed by the cloud provider.
- **Background:** Anthropic says EFS was developed with over 100 customers and names Bridgewater, Salesforce and Stripe as private-beta evaluators.
- **Not stated:** pricing, which plan tiers are covered, or any measured detection rates. These claims are Anthropic's own and we have not tested them.

## Why it matters

Companies that require zero data retention have often had to choose between that and the provider's misuse monitoring. EFS is Anthropic's attempt to offer both by keeping the evidence in the customer's own cloud. It affects enterprise API customers rather than individual users, and it is a beta whose accuracy is unpublished. Watch for independent assessments and for the Microsoft Foundry date.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and EFS is an Anthropic product. Deyron Labs is not affiliated with Anthropic.
