---
title: "OpenAI launches Ultrafast mode for GPT-6.1 Sol: up to 8x faster, at $12 and $60 per million tokens"
summary: "On 8 October 2026 OpenAI began rolling out Ultrafast mode for GPT-6.1 Sol in the API, Codex and ChatGPT Work. OpenAI says it offers near-Astra intelligence at up to 8x the speed of Sol Standard. API price is $12 per million input tokens and $60 per million output tokens, six times the Standard rate."
seoTitle: "OpenAI GPT-6.1 Sol Ultrafast: 8x faster, $12/$60"
seoDescription: "OpenAI's Ultrafast mode for GPT-6.1 Sol is up to 8x faster than Standard and costs $12 per million input tokens and $60 output. Speed claim is OpenAI's."
lang: en
publishedAt: 2026-10-09T16:30:00Z
entities:
  - OpenAI
  - GPT-6.1 Sol
  - GPT-6 Astra
  - Codex
  - ChatGPT Work
topics:
  - Models
  - Pricing
  - Products
translationKey: openai-gpt-6-1-sol-ultrafast-mode
image: /images/news/openai-gpt-6-1-sol-ultrafast-mode-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: OpenAI Ultrafast mode for GPT-6.1 Sol is up to 8x faster than Standard, at $12 input and $60 output per million tokens versus $2 and $10 Standard; the speed claim is OpenAI's"
sources:
  - title: "Ultrafast is rolling out today for GPT-6.1 Sol in the API, Codex, and ChatGPT Work"
    url: "https://community.openai.com/t/ultrafast-is-rolling-out-today-for-gpt-6-1-sol-in-the-api-codex-and-chatgpt-work/1404475"
    publisher: "OpenAI Developer Community (OpenAI announcement)"
    primary: true
  - title: "Ultrafast mode"
    url: "https://developers.openai.com/api/docs/guides/ultrafast-mode"
    publisher: "OpenAI"
    primary: true
  - title: "API pricing"
    url: "https://developers.openai.com/api/docs/pricing"
    publisher: "OpenAI"
    primary: true
---

## What happened

On 8 October 2026 OpenAI announced that Ultrafast mode is rolling out for GPT-6.1 Sol in the OpenAI API, in Codex and in ChatGPT Work. The announcement describes it as "near-Astra intelligence at up to 8x faster speeds than Sol Standard". It does not give a benchmark or a method behind the 8x figure, so treat it as OpenAI's own claim.

Ultrafast is a service tier, not a new model. In the API it is switched on per request with `service_tier` set to `ultrafast`, and it also works with GPT-6 Astra.

## Key details

- **API price for GPT-6.1 Sol in Ultrafast mode:** $12 per million input tokens and $60 per million output tokens, according to OpenAI's announcement. The pricing page lists Sol Standard at $2 and $10, so Ultrafast costs six times as much per token. OpenAI's post puts the Sol Ultrafast price at 1.2 times the cost of Astra.
- **Cached input:** the pricing page lists $0.60 per million tokens for Sol in Ultrafast mode, against $0.10 at Standard.
- **Astra in Ultrafast mode:** the pricing page lists GPT-6 Astra at $60 input and $300 output per million tokens in this tier.
- **Codex and ChatGPT Work:** access is included on Pro 500, on eligible usage-based Enterprise plans and on credit-based Edu plans. On Enterprise, administrators must enable it.
- **Regions:** Ultrafast for GPT-6.1 Sol is available in all supported regions, including US and EU data residency. OpenAI also added EU data residency for GPT-6.1 Sol Fast and GPT-6 Luna Fast.
- **Rate limits:** Ultrafast has its own limits, separate from Standard and Fast. For Sol the default is 1,000,000 tokens per minute on the Build tier, 4,000,000 on Launch and 40,000,000 on Grow.
- **Connection:** OpenAI's documentation strongly recommends WebSockets, especially for agents that make many quick tool calls. Without a persistent connection, network overhead can reduce the latency gains. HTTP is supported as an alternative.
- **What OpenAI says it is for:** debugging outages, agents that navigate apps, and live experiences where response time matters. The documentation says to use it "when speed justifies the higher cost".

## Why it matters

For work where a person or a live system waits on every response, a model that answers several times faster can change what is practical, such as interactive coding help or an agent that clicks through an app. The price is the trade-off. Six times the Standard rate means Ultrafast only makes sense where the saved time is worth more than the added cost, and a long agent run can add up quickly.

The 8x speed is a ceiling ("up to"), stated by OpenAI without a published method. We found no independent measurement at the time of writing. Test it on your own prompts and tool calls, with a persistent connection, before you budget around it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is a competitor of OpenAI. Speed and capability claims are OpenAI's own.
