---
title: "Anthropic releases Claude Haiku 5.5 at $0.10 per million input tokens, 90% below Haiku 4.5"
summary: "Anthropic released Claude Haiku 5.5 on 7 October 2026. For prompts up to 100,000 tokens it costs $0.10 per million input tokens and $0.50 per million output tokens, the same list price as OpenAI's GPT-6 Luna. The benchmark scores are Anthropic's own."
lang: en
publishedAt: 2026-10-08T07:00:00Z
entities:
  - Anthropic
  - Claude Haiku 5.5
  - Claude Haiku 4.5
  - Claude Sonnet 5.5
  - OpenAI
  - GPT-6 Luna
topics:
  - Models
  - Pricing
  - Small models
translationKey: claude-haiku-5-5-price-cut
image: /images/news/claude-haiku-5-5-2026-10-07.jpg
imageAlt: "Deyron Labs graphic: Claude Haiku 5.5 costs $0.10 / $0.50 per million tokens and matches the list price of GPT-6 Luna; benchmarks are Anthropic's own"
video: "https://www.youtube.com/shorts/aNsgzkilr78"
videoPublishedAt: 2026-10-08
sources:
  - title: "Claude Haiku 5.5"
    url: "https://www.anthropic.com/claude-haiku-5-5"
    publisher: "Anthropic"
    primary: true
  - title: "GPT-6 Luna model page and pricing"
    url: "https://developers.openai.com/api/docs/models/gpt-6-luna"
    publisher: "OpenAI"
    primary: true
  - title: "Anthropic launches Claude Haiku 5.5 with 90% API price reduction, matching GPT-6 Luna"
    url: "https://venturebeat.com/technology/anthropic-launches-claude-haiku-5-5-with-90-api-price-reduction-matching-gpt-6-luna"
    publisher: "VentureBeat"
---

## What happened

On 7 October 2026, Anthropic released Claude Haiku 5.5, the small model in its Claude family. Anthropic's announcement page calls it the first Haiku-class model with an adjustable effort setting, and says it is available now on all platforms, including Amazon Web Services, Google Cloud and Microsoft Azure, under the model ID `claude-haiku-5-5`.

The main change is price. Anthropic says Haiku 5.5 is priced 90% lower than Claude Haiku 4.5 for requests up to 100,000 tokens, and 50% lower above that size. It also says the model costs around 75% less to run on average, once a larger token count per task is taken into account.

## Key details

- **Price per million tokens, up to 100K-token requests:** $0.10 input and $0.50 output, against $1.00 and $5.00 for Haiku 4.5 and $2.00 and $10.00 for Sonnet 5.5. Above 100K tokens the prices are $0.50 input and $2.50 output. Cache reads cost $0.01 (up to 100K) and cache writes $0.125.
- **Same list price as GPT-6 Luna:** OpenAI's documentation lists GPT-6 Luna at $0.10 input and $0.50 output per million tokens. The surcharge thresholds differ: Anthropic's higher tier starts above 100K tokens, while OpenAI's starts above 272K input tokens, where it doubles the input rate.
- **Benchmarks, as reported by Anthropic:** on its own table, Haiku 5.5 scores 72.4% on OSWorld 2.1 (offline subset), against 48.9% for GPT-6 Luna and 15.7% for Haiku 4.5. On Terminal-Bench 4.0 it scores 39.2%, against 16.4% for Luna. On FrontierCode 1.1 (Main) it scores 46.4%, against 42.4% for Luna. Sonnet 5.5 scores higher than Haiku 5.5 on every benchmark in the table.
- **Tokenizer:** Anthropic notes that the updated tokenizer "uses slightly more tokens per task", and says that is included in its cost comparison. VentureBeat reports that the Terminal-Bench score applies at maximum effort and is about 20% at the default medium effort. We did not find that detail on Anthropic's page, so treat it as reported by VentureBeat.
- **Speed:** Anthropic says it is its fastest model to date at each model's standard speed.
- **Sonnet 5.5 cache reads** also dropped from $0.20 to $0.10 per million tokens, which Anthropic says lowers its cost on most agentic tasks by around 20%.

## Why it matters

Small models do most of the high-volume work in AI products: classifying, extracting, routing and running sub-tasks for larger agents. A 90% list-price cut on that tier changes what is worth automating, but the real saving depends on your workload. Prompts over 100K tokens get a 50% cut instead, and a larger token count per task eats into the headline figure.

The match with GPT-6 Luna means the two labs now list the same price for their small models. That moves the comparison from price to results on your own tasks, and the scores in Anthropic's table come from Anthropic. We found no independent evaluation at the time of writing. Run your own prompts at the effort level you plan to use before you switch.

> Disclosure: Claude, made by Anthropic, is one of the AI tools used to research and draft this article, and Anthropic is the company whose model this article covers. Deyron Labs is independent of Anthropic. Performance and pricing claims are Anthropic's own unless stated otherwise.
