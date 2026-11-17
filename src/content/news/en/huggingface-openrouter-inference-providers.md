---
title: "Hugging Face moves language-model Inference Providers to OpenRouter routing and drops bring-your-own provider keys"
summary: "On 16 November 2026 Hugging Face said its Inference Providers service now sends language-model requests through OpenRouter, which picks among 80+ providers per call and retries on failure. Hugging Face says it adds no markup, but you can no longer use your own provider API key for language models."
seoTitle: "Hugging Face routes Inference via OpenRouter"
seoDescription: "Hugging Face said on 16 Nov 2026 that language-model Inference Providers now route via OpenRouter, with no markup and no bring-your-own provider keys."
lang: en
publishedAt: 2026-11-17T18:30:00Z
entities:
  - Hugging Face
  - OpenRouter
  - Inference Providers
topics:
  - Products
  - Pricing
  - Open-weight
translationKey: huggingface-openrouter-inference-providers
image: /images/news/huggingface-openrouter-inference-providers-2026-11-17.jpg
imageAlt: "Deyron Labs graphic: Hugging Face moves Inference Providers to OpenRouter routing; 80+ providers; no markup; no bring-your-own provider key; PRO $2 a month in credits; Hugging Face blog, 16 November 2026"
sources:
  - title: "Hugging Face and OpenRouter join forces to make open-weight models easy to run"
    url: "https://huggingface.co/blog/openrouter"
    publisher: "Hugging Face blog, 16 November 2026"
    primary: true
---

## What happened

On 16 November 2026 Hugging Face published a post saying it is switching Inference Providers, its service for running models from the Hub through third-party providers, from its own custom router to OpenRouter's. According to the post, language-model requests now go through OpenRouter, which chooses a provider for each call based on "live price, speed and reliability" and retries on another provider if one fails. The post calls this "the first step" of the partnership.

## Key details

- **Routing:** Hugging Face says OpenRouter routes across 80+ providers. Routing preferences are set with suffixes on the model id, for example `:fastest`, `:cheapest` or a named provider such as `:novita`.
- **Pricing:** Hugging Face says it adds no markup, so you pay the provider's price on your Hugging Face bill. It cites average prices of $0.28 per million input tokens and $1.62 per million output tokens for open-weight models, against $1.27 and $6.36 for closed models. PRO accounts get $2 a month in credits; Team and Enterprise get $2 per seat.
- **Breaking change:** you can no longer use your own API key for a provider on language models. Image, video and audio generation still go directly through Inference Providers, and custom keys for image and video providers keep working.
- **Usage figures (Hugging Face's, citing OpenRouter):** open-weight models were 71.7% of OpenRouter tokens at the end of September 2026, up from 26.8% in October 2025.
- **Benchmark claim:** the post says Kimi K3.1 Pro scores 46 on the Artificial Analysis Intelligence Index against 65 for Claude Fable 5.2, at $3.68 against $26.54 per task. These are figures cited in Hugging Face's post; we have not checked them against the index.
- **Still to come, per the post:** connecting an OpenRouter account to a Hugging Face account and routing more tasks through OpenRouter.
- **Not stated:** the commercial terms between the two companies, and any effect on providers' rate limits.

## Why it matters

For developers who call open-weight models through Hugging Face, the practical changes are automatic failover and price-based routing, in exchange for losing the option to bill through their own provider account on language models. Teams that relied on bring-your-own keys, for example for negotiated rates or data-handling agreements with a specific provider, should check how their setup is affected before the change reaches them.

The price and usage comparisons come from Hugging Face's own post and are not independent measurements.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic's Claude is also named in the benchmark comparison cited above. Hugging Face and OpenRouter are not affiliated with Deyron Labs.
