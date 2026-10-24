---
title: "Moonshot AI launches Kimi K3.1 Pro, a 2.8T-parameter model at $2 per million input tokens, weights due 4 November"
summary: "On 23 October 2026 Moonshot AI released Kimi K3.1 Pro through its apps and API: a mixture-of-experts model with 2.8 trillion total and 104 billion active parameters and a 1M-token context. Moonshot says the weights will follow by 4 November; the license is not yet announced. Artificial Analysis scores it 55, but most other figures are Moonshot's own."
seoTitle: "Kimi K3.1 Pro: 2.8T model, weights due 4 Nov"
seoDescription: "Moonshot AI released Kimi K3.1 Pro on 23 Oct 2026: 2.8T parameters (104B active), $2 input, $10 output per million tokens, open weights promised by 4 Nov."
lang: en
publishedAt: 2026-10-24T17:30:00Z
entities:
  - Moonshot AI
  - Kimi K3.1 Pro
  - Kimi K3
  - Artificial Analysis
  - Claude Opus 5.5
  - GPT-6 Astra
topics:
  - Models
  - Open-weight
  - China
  - Pricing
translationKey: moonshot-kimi-k3-1-pro
image: /images/news/moonshot-kimi-k3-1-pro-2026-10-23.jpg
imageAlt: "Deyron Labs graphic: Kimi K3.1 Pro has 2.8T parameters, costs $2 per million input tokens and scores 55 on Artificial Analysis; weights promised by 4 November"
sources:
  - title: "Introducing Kimi K3.1 Pro (Moonshot AI blog)"
    url: "https://www.kimi.ai/blog/kimi-k3-1-pro"
    publisher: "Moonshot AI"
    primary: true
  - title: "Kimi K3.1 Pro API quickstart"
    url: "https://platform.kimi.ai/docs/guide/kimi-k3-1-pro-quickstart"
    publisher: "Moonshot AI"
    primary: true
  - title: "Introducing Kimi K3.1 Pro"
    url: "https://simonwillison.net/2026/Oct/23/kimi-k31-pro/"
    publisher: "Simon Willison"
  - title: "Moonshot AI releases Kimi K3.1 Pro: a 2.8T total / 104B active params (MoE) model with 1M context"
    url: "https://www.marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model/"
    publisher: "MarkTechPost"
  - title: "Moonshot releases Kimi K3.1 Pro and says it cut its hacking skills"
    url: "https://thenextweb.com/news/moonshot-kimi-k3-1-pro-open-weight-cyber"
    publisher: "The Next Web"
---

## What happened

On 23 October 2026, Moonshot AI, the Chinese lab behind the Kimi models, released **Kimi K3.1 Pro**. It is available now in the Kimi apps and through Moonshot's API under the model IDs `kimi-k3.1-pro` and `kimi-k3.1-pro-highspeed`. Moonshot describes it as its most capable open-weight model, but the weights are not public yet: according to Simon Willison, quoting Moonshot's announcement, "full model weights will be released by Nov 4, 2026."

The model is a post-trained version of Kimi K3 with the same architecture. Moonshot's launch post is the primary source for this story. When this article was prepared, our tools could not open Moonshot's own pages, so the details below come from three outlets that quote or link to them (MarkTechPost, The Next Web and Simon Willison) and are attributed accordingly. We will update this article once the primary pages and the Hugging Face repository can be checked directly.

## Key details

- **Size (as reported by MarkTechPost):** a sparse mixture-of-experts model with 2.8 trillion total parameters and 104 billion active per token, a 1-million-token context window, and multimodal input. Moonshot calls it "3T-class."
- **Price on Moonshot's API (per MarkTechPost; Simon Willison reports the same $2 and $10):** $2.00 per million input tokens, $0.20 for cache hits and $10.00 per million output tokens. A *Highspeed* variant that Moonshot says is two to three times faster costs $4.00 and $20.00. The earlier Kimi K3 was priced at $3.00 and $15.00.
- **One independent score:** Artificial Analysis rates Kimi K3.1 Pro at 55 on its Intelligence Index, behind Claude Opus 5.5 (58) and ahead of Claude Fable 5.1, GPT-6 Astra and Gemini 4 Argon (53 each), according to Simon Willison.
- **Moonshot's own benchmarks (not independently verified):** on Terminal-Bench 4.0 it reports 65.7% against 66.4% for Claude Opus 5.5 and 58.2% for GPT-6 Astra. Moonshot reports 51.7 on SWE-Marathon against 46.3 for Opus 5.5, but 38.1 on Terminal-Bench Science 0.1 against 68.1 for GPT-6 Astra. The comparison figures for rival models come from Moonshot's chart and were not confirmed on those companies' pages.
- **Hallucination and cyber claims (Moonshot's internal tests):** Moonshot says the rate of false claims on its own stress test fell from 23.4% for K3 to 8.3%. It also says it removed cyberattack-related material from training before release: on its in-house exploit test the shipped model solves 81% of tasks, against 90.5% for an unfiltered checkpoint and 33.3% for the original K3, and Moonshot says it still trails the best closed models.
- **Not yet known:** the license for the weights, the platform they will be published on, and the memory needed to run them. MarkTechPost notes that K3 needed supernodes of 64 or more accelerators; this is not a model for a single GPU.

## Why it matters

If the weights ship on schedule, K3.1 Pro would be one of the largest openly downloadable models, and a lab outside the US would again be the one setting the pace for open weights. Artificial Analysis's score of 55, within a few points of the best closed model, is the most reliable signal in the launch, because it does not depend on Moonshot's own tests.

For people who use AI tools rather than host models, the practical news is the price: $2 per million input tokens is a third lower than K3, and Simon Willison notes it is half of Claude Opus 5.5's price. Reading the numbers needs care. The coding and agent results are self-reported and mixed, the hallucination figure comes from an internal test, and "open" will mean little until the license is published. The cyber-capability reduction is an unusual step for an open-weight release and will be worth checking when outside evaluators can test the weights.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic's Claude Opus 5.5 and Claude Fable 5.1 are compared with Kimi K3.1 Pro in the figures above. Performance claims are Moonshot's own unless stated otherwise. The details were not checked against Moonshot's own pages.
