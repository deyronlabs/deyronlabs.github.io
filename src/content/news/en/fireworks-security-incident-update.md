---
title: "Fireworks AI says an October attack reached billing data and, for some accounts, secrets, datasets and incomplete models"
summary: "In a security bulletin updated on 9 November 2026, inference provider Fireworks AI said an unauthorized third party reached its development machines on 24 October. It says account and billing information was affected, and for a limited set of accounts also secrets, datasets and incomplete models. Fireworks says payment card numbers are not stored."
seoTitle: "Fireworks AI security incident: what it said"
seoDescription: "Fireworks AI's 9 Nov 2026 bulletin: a 24 Oct breach reached billing data and, for some accounts, secrets, datasets and incomplete models."
lang: en
publishedAt: 2026-11-10T08:00:00Z
entities:
  - Fireworks AI
  - Palo Alto Networks Unit 42
topics:
  - Security
  - Infrastructure
translationKey: fireworks-security-incident-update
image: /images/news/fireworks-security-incident-update-2026-11-09.jpg
imageAlt: "Deyron Labs graphic: Fireworks AI security bulletin updated 9 November 2026; attack on 24 October reached account and billing data and, for a limited set of accounts, secrets, datasets and incomplete models; payment card numbers not stored"
sources:
  - title: "Update on October 2026 security incident (Fireworks AI security bulletin, last updated 9 Nov 2026)"
    url: "https://fireworks.ai/security/bulletins/october-2026-security-incident-update"
    publisher: "Fireworks AI"
    primary: true
  - title: "Fireworks cyberattack exposes customer data and AI models as fallout widens"
    url: "https://www.forbes.com/sites/annatong/2026/11/09/fireworks-cyberattack-exposes-customer-data-and-ai-models-as-fallout-widens/"
    publisher: "Forbes"
    primary: false
---

## What happened

Fireworks AI, a provider that hosts open-weight models for developers, updated its security bulletin on 9 November 2026. We read the bulletin on 10 November 2026; its status was "Active monitoring". Everything below is Fireworks's own account unless attributed to Forbes.

## Key details

- **How it happened:** per the bulletin, a third-party cloud provider that hosted Fireworks research and development machines had a security incident on 23 October. On 24 October an unauthorized third party used it to reach Fireworks development machines.
- **What was affected:** account and billing information. For a limited set of accounts, also secrets, datasets and incomplete models; for certain customers "a subset of incomplete model weights and datasets were accessed".
- **What Fireworks says was not affected:** payment card numbers, which it says it does not store. It says it detected no impact to Inference, Training SDK and Nexus, which it describes as zero data retention by default, and that as of 25 October it had not detected further successful unauthorized access to the platform customers use.
- **Response:** Fireworks names Palo Alto Networks Unit 42 as forensic firm and links the threat actor group to "LLMJacking".
- **Not stated:** the bulletin does not give the number of affected customers. Forbes reported on 9 November that two customers told it they had moved substantially off Fireworks; that is Forbes's reporting, not the bulletin's.

## Why it matters

Developers who send keys, fine-tuning datasets or custom models to a hosting provider are trusting its internal machines as well as its production service, and this incident reached the former. If you use Fireworks, the bulletin is the place to check whether your account is among the limited set, and rotating any secrets stored with the provider is a reasonable precaution. Claims beyond the bulletin, including reports linking the incident to other companies' data, were not confirmed in sources we could read.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article.
