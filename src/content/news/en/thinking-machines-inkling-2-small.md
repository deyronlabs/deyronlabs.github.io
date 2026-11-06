---
title: "Thinking Machines Lab launches Inkling 2 Small, a 594B-parameter model, and plans Apache 2.0 weights next week"
summary: "On 5 November 2026 Thinking Machines Lab released Inkling 2 Small, a mixture-of-experts model with 594 billion total and 17 billion active parameters and image input. It is available now on the lab's Tinker platform with closed weights; the lab says full weights will follow under Apache 2.0 next week, after external safety testing."
seoTitle: "Inkling 2 Small: 594B, weights due next week"
seoDescription: "Thinking Machines Lab released Inkling 2 Small on 5 Nov 2026: 594B parameters, 17B active, closed on Tinker now, Apache 2.0 weights promised next week."
lang: en
publishedAt: 2026-11-06T18:41:00Z
entities:
  - Thinking Machines Lab
  - Inkling 2 Small
  - Tinker
  - Artificial Analysis
  - Kimi K3
  - DeepSeek V4.1 Flash
  - GLM-5.3-Flash
topics:
  - Models
  - Open-weight
  - Coding
translationKey: thinking-machines-inkling-2-small
video: https://www.youtube.com/shorts/LXQ0kPo4sig
videoPublishedAt: 2026-11-06T18:35:00Z
image: /images/news/thinking-machines-inkling-2-small-2026-11-05.jpg
imageAlt: "Deyron Labs graphic: Inkling 2 Small has 594B total and 17B active parameters, scores 31 on the Artificial Analysis Intelligence Index, closed on Tinker now with Apache 2.0 weights promised next week"
sources:
  - title: "Introducing Inkling 2 Small"
    url: "https://thinkingmachines.ai/news/inkling-2-small/"
    publisher: "Thinking Machines Lab"
    primary: true
  - title: "Inkling 2 Small model card"
    url: "https://thinkingmachines.ai/model-card/inkling-2-small/"
    publisher: "Thinking Machines Lab"
    primary: true
  - title: "A safe path to open weights"
    url: "https://thinkingmachines.ai/blog/a-safe-path-to-open-weights/"
    publisher: "Thinking Machines Lab"
    primary: true
  - title: "Tinker models and pricing"
    url: "https://tinker-docs.thinkingmachines.ai/tinker/models/models_and_pricing/"
    publisher: "Thinking Machines Lab"
---

## What happened

On 5 November 2026, Thinking Machines Lab published "Introducing Inkling 2 Small", the second generation of its Inkling models. It is a mixture-of-experts model with 594 billion total parameters and 17 billion active per token. It accepts image input and has variable reasoning effort. The model is available now on Tinker, the lab's fine-tuning and sampling platform, and in the Tinker Playground, with **closed weights for now**.

The lab says it intends to release the full weights under an Apache 2.0 license "next week", after external safety testing and red-teaming is complete. The same post says the release "is pending further safety evaluations by us and our partners", so the weights are an announced plan, not a published fact. We read the lab's announcement on 6 November 2026; the weights and the model card had not been checked at that point. The latter part of the long post reached us only as a machine summary, so figures from it (training details, alignment results) are left out of this article.

## Key details

- **Size and inputs:** 594B total and 17B active parameters, image input, variable effort. The lab says the vision encoder has 292 million parameters.
- **Independent index:** the lab reports a score of 31 on the Artificial Analysis Intelligence Index, "far above" its earlier Inkling models. This is the lab's report of the index result; we did not check it on Artificial Analysis.
- **Lab-reported coding results** (tables compare against GLM-5.3-Flash, DeepSeek-V4.1-Flash-1017, Muse Spark Open and Kimi K3): FrontierCode v2.0 25.4% (DeepSeek 28.5%), DeepSWE v1.1 72.1% (DeepSeek 77.0%), SWEBench Pro v2 Hard 86.3% (Kimi K3 88.2%), Vibe Code Bench v1.1 81.6% (DeepSeek 87.7%). Inkling 2 Small is second on these four, not first.
- **Lab-reported areas where it leads its comparison set:** MMMU Pro 81.6%, HLE-Diamond 28.7%, Vals Legal Index 73.9%, Vals Finance Index 61.5%, JobBench 70.5%. On DesignArena's website leaderboard it shows 1,340, below Muse Wonder (1,366) and Muse Spark 1.3 (1,351).
- **Kernel optimization (PMPP-Hard, 69 tasks):** the lab's table puts GPT-6 Astra at 63 of 69 solved on average, Kimi K3.1 Pro at 60.5, Claude Opus 5.5 at 60 and Inkling 2 Small at 54.25.
- **Cost example:** in an end-to-end test the model autonomously trained a Qwen3.5-4B forecasting model on Tinker; the lab reports $426 of spend and a forecasting score that "more than doubled". No per-token price is given on the post; it links to Tinker's pricing page.
- **Safety:** the lab says cyber capability is a large step up from Inkling Small but behind the open-weight frontier, and that CBRN capability sits below it. These are the lab's own assessments.
- **Not yet known:** the exact date of the weights, whether external testers' findings will change the release, and independent reproductions of the benchmark tables.

## Why it matters

If the weights arrive next week under Apache 2.0, a 594B model that the lab itself places near current open models would be usable by anyone with the hardware, without a usage agreement. Until then, the only way to try it is through Tinker, which is aimed at developers who fine-tune models.

Reading the numbers needs care: all benchmark tables are the lab's own, the comparison set is open-weight models chosen by the lab (with closed models appearing only in a few tables), and the post itself shows Inkling 2 Small trailing DeepSeek-V4.1-Flash on several coding tests. The release also tests the lab's "safe path to open weights" approach: closed first, open after outside testing.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claude Opus 5.5 appears in the lab's comparison tables. Performance claims are Thinking Machines Lab's own unless stated otherwise. The announcement was read on 6 November 2026; the model card, Tinker pricing and the weights were not checked.
