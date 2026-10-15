---
title: "xAI releases Grok Voice 3.0, a speech-to-speech model it prices at $0.08 per minute, the same as Grok Voice 2.0"
summary: "On 14 October 2026 xAI (now SpaceXAI) announced Grok Voice 3.0, a speech-to-speech model for its Voice Agent API. It costs $0.08 per minute, unchanged from Grok Voice 2.0, and xAI says latency is under one second. xAI's own table shows it leading most voice benchmarks but trailing GPT-Live-1 on τ-Voice."
seoTitle: "Grok Voice 3.0: $0.08/min, sub-second latency"
seoDescription: "xAI's Grok Voice 3.0, announced 14 Oct 2026, is a speech-to-speech API model at $0.08 per minute; it trails GPT-Live-1 on one benchmark, τ-Voice."
lang: en
publishedAt: 2026-10-15T16:40:00Z
entities:
  - xAI
  - SpaceXAI
  - Grok Voice 3.0
  - Grok Voice 2.0
  - Voice Agent API
  - GPT-Live-1
  - Gemini 3.8 Live
  - Artificial Analysis
topics:
  - Models
  - Voice
  - Pricing
translationKey: xai-grok-voice-3-speech-to-speech-model
image: /images/news/xai-grok-voice-3-speech-to-speech-model-2026-10-15.jpg
imageAlt: "Deyron Labs graphic: xAI Grok Voice 3.0, speech-to-speech model in the Voice Agent API; $0.08 per minute, same as Grok Voice 2.0; sub-second latency; Artificial Analysis Speech-to-Speech Index 86.9 versus 83.2 for GPT-Live-1; benchmarks are xAI's own"
sources:
  - title: "Introducing Grok Voice 3.0"
    url: "https://x.ai/news/grok-voice-3"
    publisher: "xAI (14 October 2026)"
    primary: true
---

## What happened

On 14 October 2026 xAI, which now operates as SpaceXAI, announced Grok Voice 3.0. The company calls it "the world's most intelligent speech-to-speech model": a model that takes spoken audio in and produces spoken audio out directly, which is the kind of model used to build phone and customer-support agents. It also powers the voice mode of the Grok app.

xAI says Grok Voice 3.0 is available now in its Voice Agent API. Developers whose agents already call `grok-voice-latest` were switched to the new model automatically and, according to the announcement, need no code changes.

## Key details

Figures below are xAI's, read from its announcement on 15 October 2026. Most scores are attributed to Artificial Analysis, an independent benchmarking firm, but xAI selected and published the table, and we have not run the model.

- **Price:** $0.08 per minute ($4.80 per hour) in the Voice Agent API, the same as Grok Voice 2.0. xAI also lists a cost per task on Big Bench Audio of $0.025 for Grok Voice 3.0, against $0.030 for GPT-Live-1 (Astra, Medium) and $0.055 for GPT-Realtime-2.1 (High).
- **Latency:** xAI says latency is "under one second" and gives no exact figure. It claims 40% lower latency than GPT-Live-1 on τ-Voice.
- **Benchmarks in xAI's table, Grok Voice 3.0 against Grok Voice 2.0, GPT-Live-1 and Gemini 3.8 Live:** Artificial Analysis Speech-to-Speech Index 86.9 (81.3, 83.2, 82.6); Big Bench Audio 98.5% (97.2%, 90.1%, 97.7%); Speech Agent Arena Elo 1070 (1011, 1048, 990); task success rate 94.8% (94.6%, 87.4%, 89.1%); Full Duplex Bench 97.0% (95.1%, 94.9%, 91.9%).
- **Where it does not lead:** on τ-Voice, a test of voice agents completing tasks, xAI reports 71.6% for Grok Voice 3.0, behind GPT-Live-1 at 74.5% and ahead of Gemini 3.8 Live at 68.6% and Grok Voice 2.0 at 56.5%. On EVA-Bench, from ServiceNow, xAI says Grok Voice 3.0 has the highest accuracy score, at 74%.
- **Languages:** the announcement does not list supported languages. It says only that Starlink call centers use Grok Voice to handle calls in multiple languages.

## Why it matters

For teams already running voice agents on xAI, the practical news is that the upgrade is free and automatic: the price did not change and the `grok-voice-latest` alias moved on its own. That also means anyone who relies on that alias will see different behavior without having chosen it, so it is worth re-running call-quality tests.

The comparison is less settled than the headline claim. The table is xAI's choice of tests and competitors, one competitor model (GPT-Live-1) beats it on τ-Voice, the latency claim has no number, and the language coverage is not stated. Independent tests on real call audio would show whether the lead holds outside the benchmark suite.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is not a party to this announcement. Figures are xAI's own, taken from its 14 October 2026 announcement.
