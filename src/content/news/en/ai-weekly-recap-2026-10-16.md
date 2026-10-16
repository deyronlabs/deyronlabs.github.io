---
title: "AI weekly recap: Meta's two Muse launches, Gemini 4 Argon's price clock, Anthropic's anti-distillation claims"
summary: "From 6 to 16 October 2026, Meta released a closed Muse Wonder and an open-weight Muse Spark Open, Google made Gemini 4 Argon generally available with a 1 December price rise, and Anthropic said new defenses cut distillation by 90 to 99%."
seoTitle: "AI weekly recap: Meta Muse, Gemini 4, 16 Oct"
seoDescription: "Meta's Muse Wonder and Muse Spark Open, Gemini 4 Argon's price doubling on 1 December, Grok Voice 3.0, Anthropic's distillation claims and more."
lang: en
publishedAt: 2026-10-16T17:10:00Z
entities:
  - Meta
  - Muse Wonder
  - Muse Spark Open
  - Google
  - Gemini 4 Argon
  - xAI
  - Grok Voice 3.0
  - Anthropic
  - Liquid AI
  - Mistral AI
  - Timestral
  - Xiaomi
  - NVIDIA
topics:
  - Weekly recap
  - Models
  - Open-weight models
  - Pricing
  - AI infrastructure
translationKey: ai-weekly-recap-2026-10-16
video: "https://www.youtube.com/watch?v=qptuDlX3mw8"
videoPublishedAt: 2026-10-16
image: /images/news/ai-weekly-recap-2026-10-16.jpg
imageAlt: "Deyron Labs AI News This Week, 16 October 2026: two Meta models, Gemini 4 Argon, Anthropic defenses"
sources:
  - title: "Muse Wonder (Meta research blog, 12 Oct 2026)"
    url: "https://research.meta.ai/blog/muse-wonder"
    publisher: "Meta Superintelligence Labs"
    primary: true
  - title: "Introducing Muse Spark Open, The Most Capable US Open-Weight Model to Date"
    url: "https://research.meta.ai/blog/muse-spark-open"
    publisher: "Meta Superintelligence Labs"
    primary: true
  - title: "Gemini API release notes (changelog)"
    url: "https://ai.google.dev/gemini-api/docs/changelog"
    publisher: "Google AI for Developers"
    primary: true
  - title: "Gemini Developer API pricing"
    url: "https://ai.google.dev/gemini-api/docs/pricing"
    publisher: "Google AI for Developers"
    primary: true
  - title: "Introducing Grok Voice 3.0"
    url: "https://x.ai/news/grok-voice-3"
    publisher: "xAI"
    primary: true
  - title: "Strengthening our defenses against distillation attacks"
    url: "https://www.anthropic.com/research/distillation-defenses"
    publisher: "Anthropic"
    primary: true
  - title: "AI models may be capable of self-replicating without access to a datacenter"
    url: "https://www.anthropic.com/research/self-replicating-ai"
    publisher: "Anthropic Frontier Red Team"
    primary: true
  - title: "Run fast, private agents on-device with LFM2.5-24B-A2B"
    url: "https://huggingface.co/blog/LiquidAI/lfm25-24b-a2b"
    publisher: "Liquid AI (Hugging Face blog)"
    primary: true
  - title: "Introducing Timestral"
    url: "https://mistral.ai/news/timestral/"
    publisher: "Mistral AI"
    primary: true
  - title: "XiaomiMiMo/MiMo-V2.6-Pro-RL model card"
    url: "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
    publisher: "Hugging Face (Xiaomi)"
    primary: true
  - title: "China to launch initiative to boost employment amid AI advances"
    url: "https://english.news.cn/20261010/db81c4f84519455da7b2946a563fe32d/c.html"
    publisher: "Xinhua"
    primary: true
  - title: "OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide"
    url: "https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories/"
    publisher: "NVIDIA Blog"
    primary: true
---

## What happened

### Meta ships a closed model and an open one

On 12 October Meta Superintelligence Labs released Muse Wonder and Muse Wonder Full, closed multimodal models with a 1 million token context. Muse Wonder is on Meta's API; Muse Wonder Full is only for Muse Code subscribers. Meta published no price. Third parties report $4 and $20 per million input and output tokens, and Artificial Analysis scores Muse Wonder 52 on its Intelligence Index. ([full article](/en/news/meta-muse-wonder-frontier-models/))

On 15 October Meta followed with Muse Spark Open, a model with downloadable weights: 816 billion parameters, 42 billion active, 1 million token context. Its license lets anyone use and fine-tune it, but a company above $20 million in revenue needs a separate agreement to offer it as a service. Meta calls it the most capable US open-weight model; on Meta's own table Kimi K3 and GLM 5.3 score higher on the Artificial Analysis index (44 and 45 against 39). The smallest official build needs about 700 GB of GPU memory. ([full article](/en/news/meta-muse-spark-open-816b-open-weight-model/))

### Gemini 4 Argon becomes generally available, with a price date

Google's changelog says Gemini 4 Argon reached general availability on 13 October. Paid API prices are $2 per million input tokens and $10 per million output tokens through 30 November. From 1 December the listed prices are $4 and $20, which doubles the cost of the same usage. Google's own page shows the model behind rivals on two tests, FrontierSWE v2 and Terminal-bench 4.0. ([full article](/en/news/google-gemini-4-argon-general-availability/))

### xAI upgrades its voice agents

xAI announced Grok Voice 3.0 on 14 October at $0.08 per minute, unchanged from version 2.0. Developers calling `grok-voice-latest` were switched automatically. In xAI's own table GPT-Live-1 still leads on τ-Voice (74.5% against 71.6%), and xAI gives no exact latency, only "under one second". ([full article](/en/news/xai-grok-voice-3-speech-to-speech-model/))

### Anthropic's distillation defenses and a self-replication study

Anthropic says new defenses reduced the data distillers harvest by around 90 to 99% and that it banned tens of thousands of accounts. It also accuses Zhipu AI and Moonshot AI of distillation. These are Anthropic's own claims; neither lab had responded in the sources we read and no outside party has confirmed them. ([full article](/en/news/anthropic-distillation-defenses-90-99-percent/))

Separately, Anthropic's Frontier Red Team studied whether small models could copy themselves across cheap internet-of-things devices. In a lab network of eight emulated Android devices, GLM-5.2 reached all eight in four of five trials, through a deliberately trivial entry point that the authors call an upper bound. ([full article](/en/news/anthropic-small-models-self-replication-iot-devices/))

### Open models and global AI

- **Liquid AI LFM2.5-24B-A2B (13 October):** 24 billion parameters with about 2 billion active, built for on-device agents; Liquid reports 184 tokens per second on an Apple M5 Max. ([full article](/en/news/liquid-ai-lfm2-5-24b-a2b-open-weight-agent-model/))
- **Mistral Timestral (15 October):** four time-series forecasting models from 5 million to 209 million parameters, under a modified MIT license. ([full article](/en/news/mistral-timestral-time-series-forecasting-models/))
- **Xiaomi MiMo-V2.6 (announced 22 September, covered 8 October):** a 1-trillion-parameter Pro model under an MIT license, scoring 46 on the Artificial Analysis index. ([full article](/en/news/xiaomi-mimo-v2-6-open-weights/))
- **China's AI employment plan (10 October):** Xinhua reports that the human resources ministry will launch an initiative on AI and jobs, including more than 200 national occupational standards by 2030. It is a statement of plans with no budget or timetable. ([full article](/en/news/china-human-resources-ministry-ai-employment-initiative/))
- **NVIDIA Vera Rubin at OCP (12 October):** NVIDIA opened parts of its rack designs, including support for racks up to 250 kW, without release dates or licenses. ([full article](/en/news/nvidia-opens-vera-rubin-designs-ocp-2026/))

## Key details

- **Muse Wonder:** closed; $4 / $20 per million tokens is reported by third parties, not published by Meta; Artificial Analysis index 52.
- **Muse Spark Open:** 816B parameters (42B active), 1M context; separate agreement above $20M revenue to offer it as a service; about 700 GB GPU memory for the smallest official build.
- **Gemini 4 Argon:** $2 / $10 until 30 November, then $4 / $20 (Google).
- **Grok Voice 3.0:** $0.08 per minute; auto-upgraded alias; GPT-Live-1 ahead on τ-Voice in xAI's table.
- **Anthropic distillation:** 90–99% less harvested data, a claim by Anthropic with no outside confirmation.
- **Self-replication study:** 8 of 8 emulated devices reached in 4 of 5 trials, under trivial access conditions.
- **Benchmarks:** nearly all figures this week come from the companies that released the models.
- **Next week:** NVIDIA's GTC Berlin keynote on 21 October; Mistral has promised Large 4 weights by the end of October.

## Why it matters

The most practical date of the week is 1 December: anyone budgeting Gemini 4 Argon at $2 and $10 should plan for $4 and $20 after 30 November.

Meta now sells one closed model and gives away another, and the open one comes with a license condition that matters to companies above $20 million in revenue. Its own comparison table shows two open models from Chinese labs ahead on one index, so independent tests should decide how it ranks.

Almost every claim this week is self-reported. Where an outside score exists, such as Artificial Analysis for Muse Wonder, it is lower than the launch story suggests, and where Anthropic reports on distillation, no one else has yet checked the numbers.

> Disclosure: Anthropic, the maker of Claude, appears in this recap (the distillation post and the self-replication study), and Claude was one of the AI tools used to research and draft it. Figures are the companies' own unless stated otherwise.
