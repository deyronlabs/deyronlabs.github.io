---
title: "Meta releases Muse Ember, its smallest model, at $0.10 per million input tokens and $0.50 per million output tokens"
summary: "On 9 November 2026 Meta introduced Muse Ember, which it calls its smallest and most efficient model, built for agent work such as tool calls, coding subtasks and long document parsing. The API price is $0.10 per million input tokens and $0.50 per million output tokens, with a 1 million token context window. The benchmark results are Meta's own table; the post does not say whether the weights are open."
seoTitle: "Meta Muse Ember: $0.10/$0.50 per 1M tokens"
seoDescription: "Meta released Muse Ember on 9 Nov 2026: 1M context, $0.10 input and $0.50 output per million tokens, with benchmark results reported by Meta."
lang: en
publishedAt: 2026-11-10T08:00:00Z
entities:
  - Meta
  - Meta Superintelligence Labs
  - Muse Ember
  - Muse Spark
  - Muse Wonder
  - Claude Haiku 5.5
  - GPT-6 Luna
  - Artificial Analysis
topics:
  - Models
  - Pricing
  - Agents
translationKey: meta-muse-ember
image: /images/news/meta-muse-ember-2026-11-09.jpg
imageAlt: "Deyron Labs graphic: Meta releases Muse Ember on 9 November 2026; API price $0.10 input and $0.50 output per million tokens, 1 million token context, up to 512K output tokens, benchmark results reported by Meta"
sources:
  - title: "Introducing Our Smallest, Most Efficient Model: Muse Ember (Meta research blog, 9 Nov 2026)"
    url: "https://research.meta.ai/blog/muse-ember"
    publisher: "Meta"
    primary: true
  - title: "AI News Today, November 10 (aggregator, secondary)"
    url: "https://aiweekly.co/ai-news-today"
    publisher: "AI Weekly"
    primary: false
---

## What happened

Meta published "Introducing Our Smallest, Most Efficient Model: Muse Ember" on its research blog on 9 November 2026. Meta describes Muse Ember as designed for complex reasoning execution and "the work agents repeat all day": tool calls, coding subtasks, routing, extraction and long document parsing. We read the Meta post on 10 November 2026. All figures below come from that post and are Meta's own unless stated otherwise.

## Key details

- **Price:** $0.10 per million input tokens, $0.004 per million cached input tokens and $0.50 per million output tokens. For prompts over 200K tokens the post lists $0.30, $0.012 and $1.50.
- **Context and modalities:** a 1 million token context window and up to 512K output tokens. The model accepts text, image, audio and video input and supports the Responses API.
- **Availability:** model ID `muse-ember-1.0`, on Muse Code and the Meta Model API. The post also says Muse Ember, Muse Spark and Muse Wonder are now available on Google Cloud and Oracle Cloud.
- **Benchmarks reported by Meta (maximum reasoning):** AutomationBench-AA 37.8% for Muse Ember against 20.2% for GPT-6 Luna and 13.9% for Claude Haiku 5.5 (source: Artificial Analysis, 9 November 2026); Terminal-Bench 4.0 40.9% against 39.2% for Haiku 5.5 and 16.4% for Luna, with harnesses that differ per model; Coding Agent Index-AA 46 against 37 for Haiku 5.5 and 31 for Luna. On FrontierCode 2.0-AA Haiku 5.5 leads, at 34.9% against 27.2% for Muse Ember. On the Artificial Analysis Index Muse Ember and Haiku 5.5 tie at 36.
- **Meta's cost claim:** the post says Muse Ember matches Haiku 5.5's best score at about a third of the cost. We did not verify this comparison.
- **Not stated:** the post does not say whether the weights are open or under what license.

## Why it matters

Small models that run agent loops all day are where per-token price decides what is affordable, and Meta has now put a 1 million token model with multimodal input at $0.10 per million input tokens on its API. Whether it holds up against Claude Haiku 5.5 and GPT-6 Luna in practice depends on your own workload: the table is Meta's, the harnesses differ between models, and Haiku 5.5 leads on one of the coding benchmarks. Independent evaluations had not been published when we read the post.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic's Claude Haiku 5.5, a competitor of Muse Ember, appears in Meta's comparisons; we report them as Meta does.
