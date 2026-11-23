---
title: "Z.ai announces GLM-5.4, its first flagship built as a Loop Transformer that reruns 28 layers twice"
summary: "Z.ai (Zhipu) announced GLM-5.4 on 23 November 2026, a 750B-scale model that reruns 28 layers of its GLM-5 base for two passes with shared weights. Z.ai says its intelligence is comparable to 2T-3T-parameter models. The post shows no flagship benchmark scores, the API is listed as coming soon and open weights are only planned."
seoTitle: "Z.ai GLM-5.4: first Loop Transformer flagship"
seoDescription: "Z.ai announced GLM-5.4 on 23 Nov 2026: a Loop Transformer that reruns 28 layers twice; API is coming soon and no flagship benchmarks are shown."
lang: en
publishedAt: 2026-11-23T13:12:00Z
entities:
  - Z.ai
  - Zhipu
  - GLM-5.4
  - GLM-5
  - Loop Transformer
  - ZCode
topics:
  - Models
  - Research
  - Coding
  - China
translationKey: glm-5-4-loop-transformer
video: https://youtube.com/shorts/GLncP1snefo
image: /images/news/glm-5-4-loop-transformer-2026-11-23.jpg
imageAlt: "Deyron Labs graphic: Z.ai GLM-5.4, first Loop Transformer flagship, 23 Nov 2026; 28 layers looped for 2 passes; up to 200 tokens/s off-peak per Z.ai; API coming soon, weights planned; claims are Z.ai's own"
sources:
  - title: "GLM-5.4: Toward Generalized Coding with Our First Loop Transformer"
    url: "https://z.ai/blog/glm-5.4"
    publisher: "Z.ai blog, 23 November 2026"
    primary: true
  - title: "Hacker News discussion of the GLM-5.4 post"
    url: "https://news.ycombinator.com/item?id=50609685"
    publisher: "Hacker News"
    primary: false
---

## What happened

On 23 November 2026 Z.ai, the company also known as Zhipu, published a blog post announcing GLM-5.4, which it calls its first flagship model built on a Loop Transformer. In a Loop Transformer, a group of layers with shared weights runs more than once, so the model gets more depth without more parameters. We read the post on the Z.ai site on 23 November 2026; we have not used the model, and the post is the only primary source we found.

According to Z.ai, GLM-5.4 loops 28 layers of its GLM-5 base for two iterations, at a scale of 750B parameters. Z.ai says the result reaches "intelligence levels comparable to 2T-3T parameter models". That comparison is Z.ai's own and the post does not back it with a flagship benchmark table.

## Key details

Everything below is Z.ai's description unless noted. None of it has been independently evaluated.

- **Architecture:** a Loop Transformer built from an already pre-trained base through continued training, not trained from scratch. Z.ai lists three changes: Gated Progressive Updates, a Hybrid KV Cache (global sharing plus an independent sliding window) and Sparse Attention Index Reuse, where the second pass reuses the indices chosen in the first.
- **Evidence shown:** a controlled ablation on a 30B model with the same architecture. Z.ai says that with about 10% more total training compute the looped version shows gains, and average output length falls by 10-14% on most benchmarks, such as GPQA-Diamond and MMLU-Pro. The results appear as a chart image in the post; the post has no score table for the 750B-scale flagship.
- **Speed:** up to 200 tokens per second during off-peak hours and 70-80 tokens per second at peak.
- **Known weakness:** Z.ai says the model can fall into long "marathon thinking" loops.
- **Availability:** Z.ai Chat, the GLM Coding Plan and ZCode. The API is listed as "Coming Soon". On weights, Z.ai writes that it plans "to open-source the model weights responsibly after completing necessary safety hardening", with no date. We found no GLM-5.4 repository on the Z.ai Hugging Face organization on 23 November.
- **Not stated:** pricing, usage limits, license and a date for the API or the weights.
- **Next model:** Z.ai says a "significantly larger" model "will be ready soon". We have no further detail.

## Why it matters

Looping layers is a way to spend more compute per token on reasoning without growing the parameter count, which matters for anyone paying for memory and serving costs. The design also has a visible trade-off in Z.ai's own account: the model can overthink, and the speed figures depend on time of day.

For developers the practical point is narrow today. GLM-5.4 can be tried in Z.ai's own products, but there is no API, no published price or license, and no open weights to inspect, so claims about "2T-3T-parameter" capability cannot yet be checked. Watch for independent benchmark results, the API launch and whether the promised weights arrive with a license that allows commercial use.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Z.ai is not affiliated with Deyron Labs. All performance and speed figures are Z.ai's own.
