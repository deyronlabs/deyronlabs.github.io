---
title: "Baidu publishes ERNIE 5.5 Flash Preview weights under Apache 2.0: a 280B MoE with 14B active and a 1M-token context"
summary: "Baidu's ERNIE 5.5 Flash Preview, a 280-billion-parameter mixture-of-experts model with 14 billion active parameters and a context of 1,048,576 tokens, now has open weights under Apache 2.0 on Hugging Face, which the page metadata dates to 23 November 2026. Baidu still calls it an intermediate checkpoint, and the benchmark scores on the model card are Baidu's own evaluations."
seoTitle: "Baidu ERNIE 5.5 Flash: Apache 2.0 weights"
seoDescription: "Baidu released ERNIE 5.5 Flash Preview weights under Apache 2.0: 280B MoE, 14B active, 1M-token context; scores are Baidu's own evaluations."
lang: en
publishedAt: 2026-11-11T18:42:00Z
updatedAt: 2026-11-25T21:30:00Z
entities:
  - Baidu
  - ERNIE 5.5 Flash Preview
  - ERNIE 5.5 Flash Base
  - Qianfan
  - Hugging Face
topics:
  - Models
  - Open-weight
  - China
translationKey: baidu-ernie-5-5-flash-preview
image: /images/news/baidu-ernie-5-5-flash-preview-weights-2026-11-25.jpg
imageAlt: "Deyron Labs graphic: Baidu ERNIE 5.5 Flash Preview weights are now on Hugging Face under Apache 2.0, a 280B mixture-of-experts model with 14B active parameters and a 1,048,576-token context; scores are Baidu's own"
sources:
  - title: "baidu/ERNIE-5.5-Flash-Preview (model card)"
    url: "https://huggingface.co/baidu/ERNIE-5.5-Flash-Preview"
    publisher: "Baidu on Hugging Face, read 25 November 2026"
    primary: true
  - title: "ERNIE 5.5 Flash Preview (product update)"
    url: "https://ernie.baidu.com/release/ernie-5-5-flash-preview/"
    publisher: "Baidu ERNIE Team, 11 November 2026"
    primary: true
  - title: "Introducing ERNIE 5.5 Flash Base"
    url: "https://ernie.baidu.com/release/ernie-5-5-flash-base/"
    publisher: "Baidu ERNIE Team, 5 November 2026"
    primary: true
  - title: "Baidu opens ERNIE 5.5 Flash Preview weights with million-token context"
    url: "https://technode.com/2026/11/25/baidu-opens-ernie-5-5-flash-preview-weights-with-million-token-context/"
    publisher: "TechNode, 25 November 2026"
    primary: false
---

## What happened

Baidu has published the weights of **ERNIE 5.5 Flash Preview** on Hugging Face under the Apache 2.0 license. On 11 November 2026 Baidu announced the model, a post-trained model built on ERNIE 5.5 Flash Base, available through its Qianfan API, and said the weights "will be open-sourced under Apache 2.0 soon". The model card at `baidu/ERNIE-5.5-Flash-Preview` now lists the `apache-2.0` license. The card has no explicit release date; Hugging Face's metadata dates the repository to 23 November 2026.

We read Baidu's model card and its release page on 25 November 2026. The specifications and scores below are Baidu's own; we have not run the model and found no independent evaluation.

## Key details

- **Size and context:** a sparse mixture-of-experts model with 280 billion total and 14 billion active parameters per token, and a context of 1,048,576 tokens, according to the card. It has 43 layers (one dense, 42 MoE) and 512 routed experts, 10 of them selected per token, plus one shared expert.
- **Precision and variants:** the card lists FP8 weights in blocks, with the routed experts in MXFP4 (trained with quantization awareness). The default repository holds the FP4-expert version; separate `-FP8` and `-BF16` variants are listed, and the card also mentions a draft head called DSpark. Thinking mode is on by default.
- **Status:** the card still calls the model "an intermediate checkpoint from post-training", so it remains a preview rather than a final release.
- **Scores are Baidu's:** the card says all ERNIE 5.5 Flash Preview scores come from Baidu's own evaluations. One example from its table: 46.5 on Terminal-Bench 4.0, next to 56.1 for GPT-6.1 Sol and 66.4 for Claude Opus 5.5 (the table also shows a 63.6 figure for Opus marked with an asterisk). Claude is Anthropic's model; see the disclosure below.
- **License on the Base model:** the Base checkpoint from 5 November has separate terms; we did not re-check them for this update.
- **Not on the card:** any independent evaluation, and prices (the Qianfan API price was not in the text we read).

## Why it matters

The promise from 11 November has been kept: builders can now download a 280B-class sparse model with a 1M-token context under a permissive license, and Apache 2.0 allows self-hosting and fine-tuning without custom terms.

The caution is unchanged: this is an unfinished checkpoint and the benchmark numbers are the lab's. Watch for independent results and for a final, non-preview release before relying on it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Baidu's comparison table includes Anthropic's Claude Opus 5.5. Baidu is not affiliated with Deyron Labs; all claims are Baidu's own.
