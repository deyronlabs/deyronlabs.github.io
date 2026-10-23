---
title: "OpenAI makes its Decisions API generally available, priced at $0.10 per million input tokens"
summary: "On 22 October 2026 OpenAI made the Decisions API generally available. Built with GPT-6 Luna, it returns probabilities, choices or scores for bounded questions and, per OpenAI, runs up to 10x faster than GPT-6 Luna through the Responses API. It costs $0.10 per million input tokens with no output-token charge."
seoTitle: "OpenAI Decisions API: GA at $0.10 per M tokens"
seoDescription: "OpenAI made its GPT-6 Luna-based Decisions API generally available on 22 October 2026, at $0.10 per million input tokens and no output charge."
lang: en
publishedAt: 2026-10-23T18:30:00Z
entities:
  - OpenAI
  - Decisions API
  - GPT-6 Luna
topics:
  - Products
  - Pricing
translationKey: openai-decisions-api-general-availability
image: /images/news/openai-decisions-api-general-availability-2026-10-23.jpg
imageAlt: "Deyron Labs graphic: OpenAI Decisions API generally available on 22 October 2026, up to 10x faster than GPT-6 Luna per OpenAI, $0.10 per million input tokens, up to 400 questions per request"
sources:
  - title: "Build more responsive apps with the Decisions API"
    url: "https://openai.com/index/decisions-api"
    publisher: "OpenAI"
    primary: true
  - title: "Decisions API developer guide"
    url: "https://developers.openai.com/api/docs/guides/decisions"
    publisher: "OpenAI"
    primary: true
---

## What happened

On 22 October 2026 OpenAI announced that the Decisions API is generally available. OpenAI says it is built with GPT-6 Luna and "focuses Luna's intelligence on questions with bounded answers", so that applications and agents can make near real-time decisions from text, images and structured inputs.

## Key details

All figures below are from OpenAI's announcement, checked on 23 October 2026. Speed and customer results are OpenAI's own claims and were not independently tested.

- **Speed:** OpenAI says decisions can run "up to 10x faster than GPT-6 Luna through the Responses API".
- **Answer types:** a predicate returns a probability from 0 to 1 that a condition is true; a choice returns one of the supplied values plus probabilities and confidence; a score returns the probability-weighted average of the level indices.
- **Price:** $0.10 per million input tokens, and $0.01 per million for cached input. OpenAI says you pay only for input tokens, with no output-token charges.
- **Limits and data:** up to 400 questions per request, "twice the previous limit". Processing is available in the US and EU, and Zero Data Retention is available to eligible customers.
- **Added since the public beta:** a native GPT-Live integration, prompt caching for reused context, inference residency in the US and EU, and native JSON inputs and images in instructions.
- **Customer figures quoted by OpenAI:** Box reports about 5x faster route selection on 30 test cases with the same accuracy as the Responses API; Datadog reports 40x faster p95 latency with comparable accuracy; Ramp reports 4x faster and 30% cheaper cost attribution than GPT-6 Luna; Sierra reports under 280 ms p95 and 90% lower cost per call.

## Why it matters

Many production calls to a large model only need a yes/no, a pick from a list or a rating. A dedicated endpoint that bills input tokens only, at $0.10 per million, lowers both latency and cost for that kind of routing, filtering and classification work. Whether the quoted speedups hold on a given workload will need developers' own testing.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic competes with OpenAI. All facts are attributed to OpenAI's announcement.
