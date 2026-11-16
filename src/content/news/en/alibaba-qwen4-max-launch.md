---
title: "Alibaba launches Qwen4-Max, a 2.4T-parameter-backbone model with 1M-token context, and reports 62% lower cost per task"
summary: "On 16 November 2026 Alibaba's Qwen team launched Qwen4-Max, a natively multimodal flagship with a 1-million-token context, now available on QwenCloud. Alibaba reports a 52.69 score on its Work360 evaluation against 47.74 for Qwen3.8-Max and an average cost per task of $1.67 instead of $4.43. All figures are Alibaba's own."
seoTitle: "Alibaba Qwen4-Max: 1M context, 62% lower cost"
seoDescription: "Alibaba launched Qwen4-Max on 16 Nov 2026: 1M-token context, live on QwenCloud. Cost and benchmark figures are Alibaba's own, not independent."
lang: en
publishedAt: 2026-11-16T19:35:00Z
entities:
  - Alibaba
  - Qwen
  - Qwen4-Max
  - QwenCloud
  - Qwen3.8-Max
topics:
  - Models
  - China
translationKey: alibaba-qwen4-max-launch
image: /images/news/alibaba-qwen4-max-launch-2026-11-16.jpg
video: "https://www.youtube.com/shorts/2O7k6OKdv9w"
videoPublishedAt: 2026-11-16
imageAlt: "Deyron Labs graphic: Alibaba launches Qwen4-Max on 16 November 2026 with a 1M-token context; Alibaba reports Work360 52.69 vs 47.74 and cost per task down from $4.43 to $1.67; figures are Alibaba's own"
sources:
  - title: "Qwen4-Max: Your New Teammate Has Arrived"
    url: "https://qwen.ai/blog?id=qwen4-max"
    publisher: "Qwen Team, Alibaba"
    primary: true
---

## What happened

On 16 November 2026 the Qwen team at Alibaba published "Qwen4-Max: Your New Teammate Has Arrived", the launch of its next flagship model. It follows the time-limited Qwen4-Max-Preview that Alibaba opened on 11 November, which we covered separately. The post says Qwen4-Max is "available now on QwenCloud", through the Token Plan or the API, and is also used in the QwenWork, Qoder and QwenStudio products.

We read the post on 16 November 2026. The performance and cost numbers below are Alibaba's own; we found no independent evaluation of Qwen4-Max, and the page links to third-party leaderboards only in footnotes without figures in the text.

## Key details

- **Architecture and size (per Alibaba):** a new Qwen4 architecture with a 2.4-trillion-parameter backbone, 71 billion parameters activated per token, plus 328 billion parameters in an "N-gram Embedding" component. The post names GDN and Qwen Sparse Attention (QSA) among the design choices.
- **Inputs and context:** native vision input and a context window of 1 million tokens.
- **Agent-work benchmark (Alibaba-reported):** Qwen4-Max scores 52.69 on Work360 against 47.74 for Qwen3.8-Max.
- **Token use and cost (Alibaba-reported):** on Work360, about 24% fewer tokens at the Xhigh setting and about 35% fewer at High; on Terminal-Bench 4.0, about 48% and 49% fewer. The average cost per task in the Work360 evaluation falls from $4.43 to $1.67, a 62% reduction. The post also says API prices were lowered compared with Qwen3.8-Max but gives no per-token figures.
- **Secure code (Alibaba-reported):** on Last Secure Code Bench, the share of tasks passing both function and security checks rises from 22.0% to 31.8%, and fully secure code across all three granularities from 8% to 14.7%. Alibaba says its internal cyber and CBRN evaluations did not show capabilities with large-scale risk.
- **Open source:** the post says smaller models in the Qwen4 family "are coming to open source". It does not say that Qwen4-Max itself will be open.
- **Not stated in the post:** per-token prices, weights or license for Qwen4-Max, independent benchmark results, and whether the preview's 25 November retirement date still applies.

## Why it matters

Qwen4-Max is Alibaba's answer to the current frontier models, and the headline claim is about efficiency: similar or better results on its own agent benchmark for a cost per task Alibaba puts at 62% lower. That is a claim about Alibaba's chosen evaluation, not a measured price comparison, so the useful next step is independent testing on real workloads.

For developers the immediate facts are narrow: the model is on QwenCloud now, with a 1M-token context, and prices are described only as lower. Whether Qwen4-Max or only its smaller siblings reach open weights is the main open question.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Alibaba is not affiliated with Deyron Labs; all claims about the model are Alibaba's own.
