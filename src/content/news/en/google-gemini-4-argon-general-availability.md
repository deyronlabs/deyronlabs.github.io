---
title: "Google makes Gemini 4 Argon generally available in the API, with introductory prices that double on 1 December"
summary: "Google's API changelog lists Gemini 4 Argon (gemini-4-argon) as generally available from 13 October 2026, two weeks after its 30 September announcement. Standard API prices are $2 per million input tokens and $10 per million output tokens through 30 November, then $4 and $20. Benchmark results are Google's own."
seoTitle: "Gemini 4 Argon is GA: $2/$10 until 30 Nov"
seoDescription: "Gemini 4 Argon reached general availability in Google's API on 13 Oct 2026 at $2/$10 per million tokens, rising to $4/$20 from 1 December."
lang: en
publishedAt: 2026-10-14T17:00:00Z
entities:
  - Google
  - Google DeepMind
  - Gemini 4 Argon
  - Gemini API
  - Google AI Studio
  - Fairwind Program
topics:
  - Models
  - Pricing
  - Google
translationKey: google-gemini-4-argon-general-availability
image: /images/news/google-gemini-4-argon-general-availability-2026-10-14.jpg
imageAlt: "Deyron Labs graphic: Gemini 4 Argon generally available in the Gemini API from 13 October 2026; $2 input and $10 output per million tokens through 30 November, then $4 and $20; benchmarks are Google's own"
sources:
  - title: "Gemini 4 Argon: our next era of frontier intelligence"
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/"
    publisher: "Google (Koray Kavukcuoglu, 30 September 2026)"
    primary: true
  - title: "Gemini API release notes (changelog)"
    url: "https://ai.google.dev/gemini-api/docs/changelog"
    publisher: "Google AI for Developers"
    primary: true
  - title: "Gemini Developer API pricing"
    url: "https://ai.google.dev/gemini-api/docs/pricing"
    publisher: "Google AI for Developers"
    primary: true
  - title: "Gemini models: Gemini 4 Argon"
    url: "https://deepmind.google/models/gemini/"
    publisher: "Google DeepMind"
    primary: true
---

## What happened

Google's Gemini API changelog has an entry dated 13 October 2026 saying that Gemini 4 Argon, model ID `gemini-4-argon`, reached general availability. Google first announced the model on 30 September 2026, when it was released only to a set of trusted cyber defenders through its Fairwind Program, with broader access promised to paid API customers and Google AI Ultra subscribers.

Google's DeepMind model page now says Gemini 4 Argon is available to Google AI Pro and Ultra subscribers, and links to Google AI Studio and Google Antigravity. Google describes it as built for complex coding, agentic, math and science tasks.

## Key details

Figures below are Google's, read from its announcement, pricing page and model page on 14 October 2026. We have not run the model.

- **Price (paid API, Standard tier, per million tokens):** $2.00 input and $10.00 output, with cached input at $0.10, through 30 November 2026. From 1 December the listed prices are $4.00, $20.00 and $0.20. The September announcement called $2 and $10 an introductory price and gave $4 and $20 as the price that applies after it ends; the pricing page now gives the 1 December date.
- **Other tiers:** Batch and Flex are $1 input and $5 output until 30 November, then $2 and $10. Priority is $3.60 and $18, then $7.20 and $36. The pricing page lists the model as not available on the free tier.
- **Output limit:** Google says the output token limit is raised to 1 million tokens from 64,000. Neither the announcement nor the pricing page states an input context window.
- **Benchmarks (Google-reported):** 77.9% on DeepSWE v1.1, 51.3% on Zapier's AutomationBench, 91.7% on LVBench and 68.0% on CWE-bench v1, where Google says it ties for first. Google's model page lists 68.9% on the Vals Index. The same page shows it behind rivals on two tests: FrontierSWE v2 (55.0% against 65.5% for GPT-6 Astra) and Terminal-bench 4.0 (57.4% against 66.4% for Claude Opus 5.5).
- **Security:** Google says it will release the model without cyber guardrails to trusted defenders and its own teams, and that it is taking part in the U.S. government's voluntary pre-release access process. It lists safeguards against misuse, prompt injection and misalignment.

## Why it matters

For developers the most practical detail is the date. The prices that Google calls introductory run out after 30 November, so anyone budgeting a production workload on $2 and $10 should plan for $4 and $20 from 1 December, which doubles the cost of the same usage.

The benchmark picture is mixed and self-reported. Google leads on several agent and coding tests it chose to show, while its own page shows OpenAI and Anthropic models ahead on two others. Independent evaluations have not appeared yet in the sources we checked.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and a Claude model appears in Google's comparison. Figures are Google's own, taken from its 30 September 2026 announcement, its API changelog, its pricing page and its model page.
