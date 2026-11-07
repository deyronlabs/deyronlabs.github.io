---
title: "Ant Group launches Ling-3.2-flash, a 560B-parameter multimodal model with a 1M-token context, free for two weeks"
summary: "Ant Group's platform changelog for 5 November 2026 announces Ling-3.2-flash: a natively multimodal model (text, image, video) with 560 billion parameters in total, 25 billion active and a 1-million-token context. It is free for the first two weeks. We could not confirm public weights, a license or benchmark scores."
seoTitle: "Ant Ling-3.2-flash: 560B multimodal, 1M context"
seoDescription: "Ant Group launched Ling-3.2-flash on 5 Nov 2026: 560B parameters, 25B active, 1M-token context, free for two weeks. Weights and license are unconfirmed."
lang: en
publishedAt: 2026-11-07T09:00:00Z
entities:
  - Ant Group
  - Ant Ling
  - Ling-3.2-flash
  - Inclusion AI
topics:
  - Models
  - China
translationKey: ant-ling-3-2-flash
image: /images/news/ant-ling-3-2-flash-2026-11-05.jpg
imageAlt: "Deyron Labs graphic: Ant Group Ling-3.2-flash has 560B total and 25B active parameters and a 1M-token context, free for the first two weeks; open weights not confirmed"
sources:
  - title: "Ant Ling platform changelog, v2.0.6, 5 November 2026 (in Chinese)"
    url: "https://developer.ant-ling.com/zh-CN/docs/getting-started/changelog/"
    publisher: "Ant Group (Ant Ling developer platform)"
    primary: true
  - title: "Ant launches Ling-3.2-flash multimodal model with million-token context"
    url: "https://technode.com/2026/11/06/ant-launches-ling-3-2-flash-multimodal-model-with-million-token-context/"
    publisher: "TechNode"
---

## What happened

On 5 November 2026, Ant Group's Ant Ling developer platform listed a new model, **Ling-3.2-flash**, in its changelog (version 2.0.6). The entry describes it as a natively multimodal model: it accepts text, images and video as input. The page is in Chinese, and the translation here is ours.

According to the changelog, the model can be tried online in the platform's chat page, and it is available through an API that is compatible with the OpenAI and Anthropic protocols. Use of the model is free for the first two weeks after launch. TechNode covered the launch on 6 November.

## Key details

- **Size (Ant Group's changelog):** 560 billion parameters in total, 25 billion active per token, which indicates a sparse design where only a small part of the model runs for each token. The changelog does not use the term "mixture of experts" for this model, so that is our reading of the active-versus-total figures.
- **Context window:** 1 million tokens, per the changelog.
- **Inputs and focus areas:** text, image and video. Ant lists complex visual understanding, long-running multimodal agents, 3D understanding and interaction, and medical multimodal use as areas of emphasis.
- **Access:** an online chat page and an API compatible with the OpenAI and Anthropic protocols. The free period is the first two weeks from launch; the changelog does not give an end date, and we did not find a pricing page for afterwards.
- **Family:** Ant's developer site describes Ant Ling as an open-source family from Ant Group, with results published through the Inclusion AI community, covering the Ling language models and the Ming multimodal models.
- **What we could not confirm:** the changelog names no license and links to no weights. When we checked the Hugging Face organization `inclusionAI` on 7 November 2026, it listed no Ling-3.2-flash; its most recent model was from 26 October. So we cannot say the weights are public. The changelog also gives no benchmark scores.

All figures above are as reported by Ant Group in its changelog. We read the page on 7 November 2026.

## Why it matters

A model with a 1-million-token window that reads video as well as text and images, and that is free to try through an API compatible with the OpenAI and Anthropic protocols, is easy to test: an app already written for one of those APIs can usually point at it with little change. That is the practical news for developers over the next two weeks.

What is missing matters just as much. With no published benchmark scores, no confirmed license and no weights, there is nothing yet to compare this model against others, and "open-source" cannot be assumed from the family's description. Treat the size and context figures as Ant's own claims, and check the license and pricing before building anything on it that needs to last beyond the free period.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Ant Group's changelog is in Chinese, and the translation is ours. All figures are Ant Group's unless stated otherwise.
