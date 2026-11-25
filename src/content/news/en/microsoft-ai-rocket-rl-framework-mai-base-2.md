---
title: "Microsoft AI details Rocket, the RL framework it says post-trains the 3-trillion-parameter MAI Base 2"
summary: "Microsoft AI published a technical post on Rocket, its reinforcement-learning framework for post-training MAI Base 2, described as a three-trillion-parameter base model. The post gives infrastructure numbers such as a 15-second weight transfer and makes benchmark claims that are Microsoft's own."
seoTitle: "Microsoft AI Rocket RL framework, MAI Base 2"
seoDescription: "Microsoft AI's 23 Nov 2026 post details Rocket, its in-house RL framework for the 3T-parameter MAI Base 2; benchmark claims are Microsoft's own."
lang: en
publishedAt: 2026-11-25T07:15:00Z
entities:
  - Microsoft AI
  - Rocket
  - MAI Base 2
topics:
  - Research
  - Models
image: /images/news/microsoft-ai-rocket-rl-framework-mai-base-2.jpg
imageAlt: "Deyron Labs graphic: Microsoft AI Rocket RL framework for MAI Base 2, 3 trillion parameters, 15-second weight transfer, claims are Microsoft's own"
translationKey: microsoft-ai-rocket-rl-framework-mai-base-2
sources:
  - title: "RL infrastructure at Microsoft AI"
    url: "https://microsoft.ai/news/rl-infrastructure-at-microsoft-ai/"
    publisher: "Microsoft AI"
    primary: true
---

## What happened

Microsoft AI published "RL infrastructure at Microsoft AI" on 23 November 2026. The post describes Rocket, the team's in-house reinforcement-learning framework, and says it was used to post-train MAI Base 2 (described as a three-trillion-parameter base model) through RL "without distillation from third-party models". Runs span thousands of training steps over weeks to months on thousands of GPUs. The post says this work is separate from the MAI Code 2 models. We read the post on 25 November 2026; the figures below are Microsoft's.

## Key details

- **Update cadence:** the sampler receives updated weights every 4 training steps, with sampler lag of 0 to 3 steps; weight transfer takes 15 seconds in the current configuration.
- **Long rollouts:** in one example a rollout waited 24 minutes before its first inference request, and the slowest sampled from six successive weight versions; the fastest waited 7.6 hours for its group.
- **Model and precision:** MoE expert weights are over 95% of parameters, stored in MXFP8 and dequantized to BF16 for compute. MAI Base 2 mixes local and global attention at 5:1, and the KV configuration fits about 67% more global-context tokens than BF16. Bitwise parity between sampler and learner was achieved on a 7B-active, 180B-total-parameter test model.
- **Reliability:** learner-only recovery takes roughly five minutes and saved over 7% of GPU hours in a recent run; in-job recovery saved 0.42% of training compute; runtime elasticity gave a 9.88% improvement in training compute.
- **Claim to treat carefully:** the post says the MAI model "recently passed Claude Opus 4.8" on the company's aggregate reasoning benchmark and is "on track to overtake GPT-5.6 Sol in a few weeks". These are Microsoft's statements about its own benchmark, not independent results.
- **Stack and caveats:** built on open-source verl and slime plus an MAI-maintained SGLang fork, running on Ray. Microsoft notes that dropping failed rollouts can add noise or bias to the GRPO baseline. No availability, pricing or licence is stated; this is internal infrastructure.

## Why it matters

The post is a rare look at how a large lab runs RL at multi-trillion-parameter scale, and it shows Microsoft building its own training stack rather than relying on partner models. For readers, the practical signal is the engineering detail; the forward-looking benchmark claims should wait for an independent evaluation or a public model release.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic's Claude Opus 4.8 is named in the source; Microsoft is not affiliated with Deyron Labs.
