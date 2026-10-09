---
title: "Xiaomi releases MiMo-V2.6 under an MIT license, including a 1-trillion-parameter open-weight Pro model"
summary: "Xiaomi announced MiMo-V2.6 on 22 September 2026: a 1.02-trillion-parameter Pro model and a 309-billion-parameter Flash model, both multimodal, with weights on Hugging Face tagged MIT. Artificial Analysis lists Pro at 46 on its Intelligence Index; most other scores are Xiaomi's own."
seoTitle: "Xiaomi MiMo-V2.6: 1T open-weight Pro under MIT"
seoDescription: "Xiaomi announced MiMo-V2.6 on 22 September 2026: a 1.02-trillion-parameter Pro model and a 309-billion-parameter Flash model, both multimodal, with…"
lang: en
publishedAt: 2026-10-08T07:30:00Z
entities:
  - Xiaomi
  - MiMo-V2.6
  - MiMo-V2.6-Pro
  - MiMo-V2.6-Flash
  - MiMo-V2.6-Distill-Qwen-9B
  - Artificial Analysis
  - Kimi K3
  - GLM-5.3
  - Claude Opus 5
topics:
  - Models
  - Open-weight
  - China
translationKey: xiaomi-mimo-v2-6-open-weights
image: /images/news/xiaomi-mimo-v2-6-2026-09-22.jpg
imageAlt: "Deyron Labs graphic: Xiaomi MiMo-V2.6 Pro is a 1T-parameter MIT-licensed open-weight model that Artificial Analysis lists at 46; most other scores are Xiaomi's own"
sources:
  - title: "MiMo-V2.6 release announcement (Xiaomi MiMo, in Chinese)"
    url: "https://mimo.mi.com/docs/zh-CN/news/latest/v2-6"
    publisher: "Xiaomi"
    primary: true
  - title: "XiaomiMiMo/MiMo-V2.6-Pro-RL model card"
    url: "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL"
    publisher: "Hugging Face (Xiaomi)"
    primary: true
  - title: "XiaomiMiMo/MiMo-V2.6-Flash-RL model card"
    url: "https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL"
    publisher: "Hugging Face (Xiaomi)"
    primary: true
  - title: "MiMo-V2.6-Pro: intelligence, performance and price analysis"
    url: "https://artificialanalysis.ai/models/mimo-v2-6-pro"
    publisher: "Artificial Analysis"
  - title: "Xiaomi open-sources MiMo-V2.6 models after scaling reinforcement learning"
    url: "https://technode.com/2026/09/22/xiaomi-open-sources-mimo-v2-6-models-after-scaling-reinforcement-learning/"
    publisher: "TechNode"
---

## What happened

On 22 September 2026, Xiaomi announced MiMo-V2.6, a family of multimodal models that handle text, images, video and audio. The announcement covers two main models, **MiMo-V2.6-Pro** and **MiMo-V2.6-Flash**, plus a small research model, **MiMo-V2.6-Distill-Qwen-9B**, and the reinforcement-learning environments and code used to train them. The translation of Xiaomi's Chinese-language post is ours.

The weights are public. The Hugging Face repositories for Pro (`MiMo-V2.6-Pro-RL`) and Flash (`MiMo-V2.6-Flash-RL`) were created on 21 September (UTC) and carry an MIT license tag. Xiaomi's announcement page does not name the license, so the license tag on the Hugging Face model cards is our source for it.

This story is about two weeks old: we missed it in our first scans of Chinese sources, which is why it appears now.

## Key details

- **Sizes (Hugging Face model cards):** Pro is a sparse mixture-of-experts model with 1.02 trillion parameters in total and 42 billion active per token. Flash has 309 billion in total and 15 billion active. Both list a 1-million-token context window.
- **Independent index:** Artificial Analysis lists MiMo-V2.6-Pro at 46 on its Intelligence Index and Flash at 38, both with an MIT license. Citing Xiaomi's comparison, TechNode reports that Kimi K3 scores 44, GLM-5.3 scores 45 and the leading closed models score 53. Xiaomi calls Pro the strongest open-source model on that index.
- **Price on Xiaomi's API (as listed by Artificial Analysis):** Pro costs $0.43 per million input tokens and $0.87 per million output tokens; Flash costs $0.14 and $0.28. Xiaomi says API prices are unchanged from V2.5.
- **Agent and coding scores are Xiaomi's own.** For Pro, the model card lists 89.9 on Terminal Bench 2.1, 82.0 on OSWorld-Verified, 76.9 on Toolathlon-Verified and 71.9 on DeepSWE v1.1; for Flash, 87.6, 80.8, 73.6 and 67.9. Xiaomi's announcement page quotes slightly different DeepSWE figures (72.6 for Pro and 65.7 for Flash). Xiaomi says Pro is comparable to Claude Opus 5 and GPT-5.6 Sol on most agent benchmarks and behind Claude Fable 5.1 and GPT-6 Astra. On several agentic and coding rows of the model card's own table, Claude Opus 5 scores higher, and some cells are blank. We found no independent evaluation of these benchmark rows.
- **Training cost, as reported by TechNode from Xiaomi's post:** about $2.62 million for Pro and $850,000 for Flash, for a reinforcement-learning run of 30 steps in under six days. Xiaomi does not say here whether this covers the whole training of the models or only that stage.
- **Small model:** the 9B distilled model is MIT-licensed and, according to Xiaomi, raises its SWE-bench Verified score from 61.1 to 66.2. Community quantized versions of Flash and the 9B model appeared on Hugging Face within a day.
- **Practical limits:** the Pro model card gives no minimum memory requirement. Its example setups use two nodes for SGLang or eight-way tensor parallelism for vLLM, and both require custom code (`trust-remote-code`).

Checked against the primary pages and Artificial Analysis on 8 October 2026.

## Why it matters

An MIT license is one of the most permissive a model can carry: you can run it, modify it and use it commercially without asking. That a trillion-parameter model with agent skills close to the top closed models, on Xiaomi's own numbers, comes with that license is the main reason to pay attention. A phone and electronics maker is now competing with the specialist AI labs on open weights.

Most people will not run Pro on their own hardware. At 1.02 trillion parameters it needs a multi-GPU cluster, so for most users the realistic ways in are Xiaomi's cheap API or a third-party host. The 9B distilled model and community quantizations of Flash are the options for local use.

Treat the headline numbers with care. The one independent measure we found, Artificial Analysis, puts Pro at 46, ahead of Kimi K3 and GLM-5.3 on that index but below the best closed models. The agent scores that make the comparison to Claude Opus 5 and GPT-5.6 Sol are Xiaomi's own, and the company's announcement and model card do not agree on every figure. Test the model on your own tasks before relying on it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Xiaomi's announcement is in Chinese, and the translation is ours. Performance claims are Xiaomi's own unless stated otherwise.
