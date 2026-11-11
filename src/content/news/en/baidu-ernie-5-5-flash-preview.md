---
title: "Baidu releases ERNIE 5.5 Flash Preview, a 280B MoE post-training checkpoint, in its Qianfan API with open weights promised"
summary: "On 11 November 2026 Baidu released ERNIE 5.5 Flash Preview, the first post-trained model built on ERNIE 5.5 Flash Base: 280 billion total and 14 billion active parameters, a 1-million-token context and a text-only design. It is available through Baidu's Qianfan platform; Baidu says the weights will be open-sourced under Apache 2.0 soon. Baidu calls it an intermediate checkpoint."
seoTitle: "Baidu ERNIE 5.5 Flash Preview: 280B MoE"
seoDescription: "Baidu released ERNIE 5.5 Flash Preview on 11 Nov 2026: a 280B MoE with 14B active, via Qianfan, with Apache 2.0 weights promised."
lang: en
publishedAt: 2026-11-11T19:30:00Z
entities:
  - Baidu
  - ERNIE 5.5 Flash Preview
  - ERNIE 5.5 Flash Base
  - Qianfan
topics:
  - Models
  - Open-weight
  - China
translationKey: baidu-ernie-5-5-flash-preview
image: /images/news/baidu-ernie-5-5-flash-preview-2026-11-11.jpg
imageAlt: "Deyron Labs graphic: Baidu ERNIE 5.5 Flash Preview, released 11 November 2026, has 280B total and 14B active parameters and a 1M-token context, is in the Qianfan API, and Baidu promises Apache 2.0 weights soon"
sources:
  - title: "ERNIE 5.5 Flash Preview (product update)"
    url: "https://ernie.baidu.com/release/ernie-5-5-flash-preview/"
    publisher: "Baidu ERNIE Team, 11 November 2026"
    primary: true
  - title: "Introducing ERNIE 5.5 Flash Base"
    url: "https://ernie.baidu.com/release/ernie-5-5-flash-base/"
    publisher: "Baidu ERNIE Team, 5 November 2026"
    primary: true
---

## What happened

On 11 November 2026 Baidu's ERNIE team announced **ERNIE 5.5 Flash Preview**. Baidu describes it as the first post-trained model built on ERNIE 5.5 Flash Base, the pre-trained checkpoint it published on 5 November. The preview is available through an API on Baidu Cloud's Qianfan platform. Baidu says the weights "will be open-sourced under Apache 2.0 soon"; they were not published when we read the page.

We read Baidu's release page on 11 November 2026. Facts below are Baidu's own, reported by the lab; we have not tested the model or seen independent evaluations.

## Key details

- **Size and context:** a sparse mixture-of-experts model with 280 billion total and 14 billion active parameters, and a context of 1 million tokens, according to Baidu. It is a text-only model.
- **Status:** Baidu calls it "an intermediate checkpoint from post-training" and says training is not finished, so some capabilities may still fall short. That makes this a preview, not a final release.
- **Access:** the Qianfan API is live. The page's text gives no prices, plans, regions or API model identifier.
- **License:** Apache 2.0 is promised for the weights, a more permissive license than the custom license used for the Base checkpoint on 5 November. Until the weights appear, the promise is not a release.
- **Benchmarks:** Baidu shows its results as images (a results chart and a table). We could not read numeric scores from the page text, so we do not quote any.

## Why it matters

Baidu now offers two things for this model family: a base checkpoint for fine-tuning and a post-trained preview for direct use. If the Apache 2.0 weights arrive as promised, builders would get a 280B-class sparse model with a permissive license, which matters for anyone who wants to self-host or fine-tune without custom license terms.

Until then, the practical advice is cautious: the model is explicitly unfinished, pricing is not published in the text we read, and the performance claims are Baidu's own and shown only as images. Watch for the weights, the final license text and independent evaluations before building on it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Baidu is not affiliated with Deyron Labs; all claims are Baidu's own.
