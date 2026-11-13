---
title: "Google launches Gemini 4 Hydrogen at $1.50/$7.50 per million tokens with a flat 1M-token context window"
summary: "On 12 November 2026 Google released Gemini 4 Hydrogen, a model it calls its daily driver for coding and agentic work, priced at $1.50 per million input tokens and $7.50 per million output tokens across the full 1M-token context. Google says it scores 51 on the Artificial Analysis Intelligence Index and is rolling out in the Gemini API, the Gemini app and Search. All results are Google's own."
seoTitle: "Gemini 4 Hydrogen: $1.50/$7.50, 1M context"
seoDescription: "Google released Gemini 4 Hydrogen on 12 Nov 2026: $1.50/$7.50 per 1M tokens, flat across a 1M context. Benchmark results are Google's own."
lang: en
publishedAt: 2026-11-13T19:29:00Z
entities:
  - Google
  - Google DeepMind
  - Gemini 4 Hydrogen
  - Gemini 4 Carbon
  - Gemini 4 Argon
  - Gemini 3.8 Flash
  - Google Antigravity
  - Gemini API
  - Artificial Analysis
topics:
  - Models
  - Pricing
  - Google
  - Coding
  - Agents
translationKey: google-gemini-4-hydrogen
image: /images/news/google-gemini-4-hydrogen-2026-11-12.jpg
video: "https://www.youtube.com/shorts/u1XTX0e_1B0"
videoPublishedAt: 2026-11-13
imageAlt: "Deyron Labs graphic: Google released Gemini 4 Hydrogen on 12 November 2026; $1.50 input and $7.50 output per million tokens, 1M-token context, Artificial Analysis Intelligence Index 51 per Google"
sources:
  - title: "Introducing Gemini 4 Hydrogen"
    url: "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/"
    publisher: "Google (Koray Kavukcuoglu, 12 November 2026)"
    primary: true
  - title: "Gemini 4 Hydrogen: everyday coding and agentic workflows for developers"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-hydrogen/"
    publisher: "Google, 12 November 2026"
    primary: true
  - title: "Gemini 4 Hydrogen model card (PDF, not opened by us)"
    url: "https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Hydrogen-Model-Card.pdf"
    publisher: "Google DeepMind"
    primary: true
---

## What happened

On 12 November 2026 (18:00 UTC) Google published "Introducing Gemini 4 Hydrogen", by Koray Kavukcuoglu, and began rolling the model out globally. Google describes Hydrogen as "our daily driver for agentic workflows" and positions it next to the larger Gemini 4 Carbon and Gemini 4 Argon models. A second post, aimed at developers, says it handles repository coding and debugging, interactive web development and multimodal workflows.

Per Google, Hydrogen is available in the Gemini API through Google AI Studio and Android Studio, in Gemini for business, and in Google Antigravity for paid AI Pro and Ultra subscribers. Consumers get it in the Gemini app model picker (free users through automatic model selection when it fits the prompt) and in Google Search for all users. It is also coming to Gemini in Google Sheets for eligible subscriptions.

## Key details

All figures below are Google's, read from its 12 November 2026 posts on 13 November. We have not run the model, and we did not open the model card or the developer documentation that the posts link.

- **Price and context:** $1.50 per million input tokens and $7.50 per million output tokens, "flat across" the full 1 million-token context window, with no higher tier for long prompts. For comparison, our earlier article on Gemini 4 Carbon reports an introductory $2 and $10 for Carbon and Argon.
- **Thinking levels:** four settings, low, medium, high (the default) and a new xhigh tier.
- **Benchmarks (vendor-reported):** Google says Hydrogen scores 51 on the Artificial Analysis Intelligence Index at the default setting, against 50 for Argon, and 54 at xhigh. It reports 57% on Terminal-Bench 4.1 versus 18.2% for Gemini 3.8 Flash, 58.8% on HLE-Diamond, 52.3% on Vals Tax Agent Bench (which it says is first overall), 55.8% on Vals Legal Research Bench (tied for first) and 71.6% on Agents' Last Exam v1.1. It also reports 53.4% on its own Multimodal Knowledge Agent benchmark and fifth place on the Agent Arena leaderboard.
- **Speed:** Google says Hydrogen is 2.5 times faster than Gemini 3.8 Flash at the high setting and quotes partners at 2x to 2.8x faster with 12% to 23% fewer tokens. These are Google and partner claims.
- **Safety (Google's internal tests):** Google reports up to 81% less overreach and up to 79% less under-service (the comparison baseline was not specified in what we read), a 96.7% score on an internal honesty evaluation, and false refusals below 0.4% on HealthBench Pro. Google does not label Hydrogen a preview.
- **Not yet in the docs we checked:** on 13 November, Google's public Gemini API pricing page and changelog, as returned to us, did not list Hydrogen, so confirm the price and model ID in AI Studio before budgeting.

## Why it matters

Hydrogen is a lower-priced option inside the Gemini 4 family. At $1.50 and $7.50 with no long-context surcharge, long-document and agent workloads that were expensive on larger models become cheaper to try, and Google says it scores slightly above Argon on the Artificial Analysis index. Its other measures are mostly Google-selected benchmarks, plus a third-party index that Google links to.

What to check yourself: tokens per task at each thinking level, because xhigh raises both quality and cost; the price against your own prompts rather than the headline rate; and independent results, which we did not find in the sources we checked.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic competes with Google. Figures are Google's own, from its 12 November 2026 announcements.
