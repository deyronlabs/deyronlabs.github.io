---
title: "Prime Intellect says an unauthorized party swapped its DeepSeek V4.1 Flash endpoint for a model with refusals removed"
summary: "In security advisory PI-SA-2026-001, published 19 November 2026, Prime Intellect says that from 8 to 10 November an unauthorized party replaced the deployment behind its deepseek/deepseek-v4.1-flash endpoint with an abliterated copy, a version with refusal behaviour removed. Capability benchmarks were unaffected. The company says it found no evidence that prompts or completions left its cluster."
seoTitle: "Prime Intellect: DeepSeek endpoint swapped"
seoDescription: "Prime Intellect's advisory says an unauthorized party replaced its DeepSeek V4.1 Flash endpoint with an abliterated copy from 8 to 10 Nov 2026."
lang: en
publishedAt: 2026-11-20T14:00:00Z
entities:
  - Prime Intellect
  - DeepSeek
  - DeepSeek V4.1 Flash
topics:
  - Security
  - Safety
  - Models
translationKey: prime-intellect-deepseek-v4-1-flash-substitution-advisory
image: /images/news/prime-intellect-deepseek-v4-1-flash-substitution-advisory-2026-11-20.jpg
imageAlt: "Deyron Labs graphic: Prime Intellect advisory PI-SA-2026-001; DeepSeek V4.1 Flash endpoint replaced by an abliterated copy from 8 Nov 01:24 to 10 Nov 06:35 UTC; HarmBench refusals fell from 198 of 240 to 0; capability benchmarks unaffected"
sources:
  - title: "Security Advisory PI-SA-2026-001: deepseek-v4-1-flash model substitution (Prime Intellect, 19 November 2026)"
    url: "https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution"
    publisher: "Prime Intellect"
    primary: true
---

## What happened

Prime Intellect published security advisory PI-SA-2026-001 on 19 November 2026. It says that between 01:24 UTC on 8 November and 06:35 UTC on 10 November 2026, an unauthorized party replaced the deployment behind its `deepseek/deepseek-v4.1-flash` endpoint with an abliterated copy of the model. "Abliterated" refers to a technique that removes or sharply reduces a model's refusal behaviour. We read the full advisory on 20 November 2026; everything below is Prime Intellect's account, and the investigation is still in progress.

## Key details

- **Window:** 8 November 01:24 UTC to 10 November 06:35 UTC, about 53 hours by our arithmetic.
- **What changed:** the model weights behind the endpoint. According to the advisory the chat template, tokenizer and configuration were unchanged.
- **Safety behaviour (Prime Intellect's measurements):** refusal tallies fell from 98 to 1 out of 100 on JailbreakBench, from 304 to 2 out of 313 on StrongREJECT, and from 198 to 0 out of 240 on HarmBench. We have not seen the test setup behind these counts.
- **Capability:** results on GPQA Diamond and tau-bench were not affected, according to the advisory.
- **Data and credentials:** Prime Intellect says it found no evidence that prompts or completions left its cluster. The service runs with zero data retention and does not log them. API keys and credentials were not affected, and no other models were touched.
- **Customers:** affected customers have been contacted.
- **Not in the advisory:** how many customers were affected, how the party gained access, and any response from DeepSeek.

## Why it matters

For people who call a hosted open-weight model through a third-party endpoint, the weights behind the name are an assumption. Here the change did not alter capability scores, so ordinary quality checks would not have flagged it, while the refusal counts moved almost entirely to zero. Anyone who used the endpoint during the window and relied on its safety behaviour, for example in a product that exposes it to end users, should review what the advisory says and contact the provider. The open questions are how the substitution was carried out and what controls will prevent a repeat; the advisory leaves both unanswered for now.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. All facts are from Prime Intellect's advisory, read on 20 November 2026; we have not independently verified them.
