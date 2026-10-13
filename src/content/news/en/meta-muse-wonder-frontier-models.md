---
title: "Meta releases Muse Wonder and Muse Wonder Full, its first frontier-class models, as closed models with a $4/$20 API price"
summary: "On 12 October 2026 Meta Superintelligence Labs released Muse Wonder and Muse Wonder Full, two proprietary models with a 1 million token context window. Only the smaller Muse Wonder is on the API, at $4 per million input tokens and $20 per million output tokens; Full is limited to paid Muse Code plans. Weights are not released."
seoTitle: "Meta Muse Wonder: closed frontier model, $4/$20"
seoDescription: "Meta released Muse Wonder and Muse Wonder Full on 12 Oct 2026: closed models, 1M context, API at $4/$20 per million tokens, Full only in Muse Code."
lang: en
publishedAt: 2026-10-13T17:00:00Z
entities:
  - Meta
  - Meta Superintelligence Labs
  - Muse Wonder
  - Muse Wonder Full
  - Muse Code
  - Artificial Analysis
  - Claude Opus 5.5
  - GPT-6 Astra
topics:
  - Models
  - Pricing
  - Agents
translationKey: meta-muse-wonder-frontier-models
image: /images/news/meta-muse-wonder-frontier-models-2026-10-12.jpg
imageAlt: "Deyron Labs graphic: Meta releases Muse Wonder and Muse Wonder Full on 12 October 2026; API price $4 input and $20 output per million tokens, 1 million token context, Full only in Muse Code, no weights released"
video: "https://www.youtube.com/watch?v=mnDYnopAxP0"
videoPublishedAt: 2026-10-13
sources:
  - title: "Muse Wonder (Meta research blog, 12 Oct 2026)"
    url: "https://research.meta.ai/blog/muse-wonder"
    publisher: "Meta Superintelligence Labs"
    primary: true
  - title: "Muse Wonder Full model card"
    url: "https://research.meta.ai/static/muse-wonder-model-card"
    publisher: "Meta Superintelligence Labs"
    primary: true
  - title: "Muse Wonder (Max): intelligence, performance and price analysis"
    url: "https://artificialanalysis.ai/models/muse-wonder"
    publisher: "Artificial Analysis"
    primary: false
  - title: "Meta's new Muse Wonder and Muse Wonder Full models achieve frontier performance, but only the weaker one is available via API"
    url: "https://venturebeat.com/technology/metas-new-muse-wonder-and-muse-wonder-full-models-achieve-frontier-performance-but-only-the-weaker-one-is-available-via-api"
    publisher: "VentureBeat"
    primary: false
---

## What happened

On 12 October 2026 Meta Superintelligence Labs published two new models, Muse Wonder and Muse Wonder Full, which it calls the next step on its scaling ladder. In its blog post Meta says the models reach state-of-the-art results on benchmarks for personal and professional agents, memory and coding, and that they were trained at its Prometheus data center.

Muse Wonder is available now through the Meta Model API and the Muse Code tool. Muse Wonder Full is available now to Muse Code subscribers. Meta says Muse Wonder will soon power experiences in the Muse app, first for subscribers.

## Key details

**Confirmed by Meta (blog post and model card)**
- Both models accept text, image, video and audio input and produce text output. The Full model card gives a context length of 1 million tokens.
- Meta says Muse Wonder is its "most aligned model to date" with its "strongest safeguards to date" against chemical, biological, radiological and nuclear (CBRN) and cyber misuse.
- The model card says that without mitigations Meta cannot rule out that Muse Wonder Full reaches its high-risk threshold in the chemical and biological domain. With safety training and system-level classifiers, Meta rates all tracked domains "moderate or lower". A full safety report is promised "soon".
- The blog post gives no price and no license or weights information, and its benchmark scores appear in a figure, not in text.

**Reported by third parties (not verified against a Meta pricing page)**
- Pricing: VentureBeat reports $4.00 per million input tokens, $0.20 per million cached input tokens and $20.00 per million output tokens for Muse Wonder on the API. Artificial Analysis lists the same $4 and $20 and a 1 million token context window. VentureBeat reports no pay-as-you-go price for Muse Wonder Full, which it says is offered only on Muse Code plans at $50 and $200 per month.
- Independent index: Artificial Analysis scores Muse Wonder 52 on its Intelligence Index. VentureBeat reports 56 for Muse Wonder Full, against 58 for Claude Opus 5.5, 56 for Claude Sonnet 5.5 and 53 for GPT-6 Astra. We read the Muse Wonder score on Artificial Analysis directly; the other scores come from VentureBeat.
- Meta's own comparison: VentureBeat reports that Meta's table shows Muse Wonder Full ahead of GPT-6 Astra and Claude Opus 5.5 on coding and long-running tasks, for example 57.5 on SWE-Marathon against 46.3 for Opus 5.5, and behind on Terminal-Bench 4.0-AA and HealthBench Pro. VentureBeat notes that Meta's methodology mixes internal, vendor-supplied and third-party results.
- Licensing: VentureBeat reports that neither Wonder model has downloadable weights.

**Not confirmed:** when Muse Wonder reaches free users of the Muse app, whether Muse Wonder Full will get an API price, and when the full safety report will appear.

## Why it matters

Meta now sells a closed frontier-class model through an API, competing directly with models from OpenAI, Anthropic and Google. If the reported figures hold, its price matches that of Claude Opus 5.5, so the choice between them is likely to turn on task fit and independent test results, not on cost alone.

The practical catch for developers is that the stronger model is not on the API. The reported independent score of the API model, Muse Wonder, is lower than Muse Wonder Full and lower than the leading models in the same table. Meta's benchmark table was chosen by Meta, so independent evaluations over the coming weeks matter more than the launch chart. Because the models are closed, nothing here changes what can be run locally.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic's models, Claude Opus 5.5 and Claude Sonnet 5.5, appear in the comparisons above; we report them as the sources do. Pricing and index figures were checked on 13 October 2026 through third-party pages because Meta's pricing page could not be opened.
