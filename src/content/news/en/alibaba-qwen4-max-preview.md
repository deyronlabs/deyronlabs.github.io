---
title: "Alibaba opens Qwen4-Max-Preview, its next flagship with 1M-token context, to Token Plan users until 25 November"
summary: "On 11 November 2026 Alibaba opened a preview of Qwen4-Max, which it calls the next-generation flagship multimodal model in the Qwen family, with a 1-million-token context. QwenCloud documentation says it is available only through the Token Plan subscription from 11 to 25 November and will be retired after the preview. No price, parameter count, license or benchmark scores are published."
seoTitle: "Alibaba Qwen4-Max-Preview: 1M context, 25 Nov"
seoDescription: "Alibaba opened Qwen4-Max-Preview on 11 Nov 2026: 1M-token context, Token Plan only until 25 Nov. No price, weights or benchmarks published."
lang: en
publishedAt: 2026-11-13T19:28:00Z
entities:
  - Alibaba
  - Qwen
  - Qwen4-Max-Preview
  - QwenCloud
  - Token Plan
topics:
  - Models
  - China
translationKey: alibaba-qwen4-max-preview
image: /images/news/alibaba-qwen4-max-preview-2026-11-11.jpg
imageAlt: "Deyron Labs graphic: Alibaba Qwen4-Max-Preview opened on 11 November 2026 with a 1M-token context and 393,216-token maximum output, Token Plan only until 25 November; no price, weights or benchmarks published"
sources:
  - title: "Latest model: Qwen4-Max-Preview"
    url: "https://docs.qwencloud.com/developer-guides/getting-started/latest-model"
    publisher: "QwenCloud (Alibaba) developer documentation"
    primary: true
  - title: "Alibaba opens Qwen4-Max preview with a million-token context window"
    url: "https://technode.com/2026/11/11/alibaba-opens-qwen4-max-preview-with-a-million-token-context-window/"
    publisher: "TechNode, 11 November 2026"
    primary: false
---

## What happened

On 11 November 2026 Alibaba opened a preview of Qwen4-Max. Its QwenCloud developer documentation calls Qwen4-Max-Preview (model ID `qwen4-max-preview`) the "next-generation flagship multimodal model in the Qwen family", and the preview window runs from 10:00 on 11 November to 24:00 on 25 November 2026 (UTC+8). TechNode reported the opening the same day and added that Alibaba is also using the model early in its Qwen app and in the Qoder, QwenWork and QwenStudio products.

## Key details

Everything below comes from Alibaba's documentation, which we read on 12 November 2026. We have not run the model.

- **Access:** the documentation says the model is "available through Token Plan only" and that pay-as-you-go access is not supported. It also says the model will be retired after the preview ends.
- **Context and output:** a 1-million-token context window and a maximum output of 393,216 tokens, shared between the model's reasoning and its final answer.
- **Capabilities:** text generation with deep reasoning (thinking is on by default; `reasoning_effort` can be low, medium or xhigh, with xhigh the default), image and video understanding, tool calling (function calling, web search and built-in tools) and structured outputs (JSON object and JSON schema).
- **Compatibility:** the endpoint accepts OpenAI Chat Completions, OpenAI Responses and Anthropic Messages formats.
- **Not stated in the sources we read:** price, parameter count, training details, license, open weights, or any benchmark score. The Qwen blog pages could not be read by our tools, so an announcement there is possible but unconfirmed.

## Why it matters

Qwen4-Max-Preview is the first public sign of what Alibaba intends as its next top model, but it is a time-limited preview, not a release: it is sold only inside a subscription, it disappears on 25 November, and there is no published way to compare it with other frontier models. Developers who already use the Qwen API can test it on their own tasks during the two-week window, mainly to see how the long context and the reasoning-effort setting behave.

For everyone else the practical advice is to wait for the final release, pricing, a model card and independent evaluations. Alibaba has not said whether Qwen4-Max will follow the open-weight path of some earlier Qwen models.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Alibaba is not affiliated with Deyron Labs; all claims about the model are Alibaba's own.
