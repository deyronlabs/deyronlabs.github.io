---
title: "Empero releases Quark, a 165M-parameter language model trained for about $4,200, under Apache 2.0"
summary: "On 15 November 2026 Empero published Quark, a small language model of about 165 million parameters that it says was trained end to end for roughly $4,200 of compute. Four checkpoints are on Hugging Face under Apache 2.0. The benchmark results are Empero's own runs, and the authors list several limitations."
seoTitle: "Empero Quark: 165M model trained for $4,200"
seoDescription: "Empero released Quark on 15 Nov 2026: a 165M-parameter model trained for about $4,200, four Apache 2.0 checkpoints, results from its own evaluations."
lang: en
publishedAt: 2026-11-16T18:47:00Z
entities:
  - Empero
  - Quark
  - SmolLM2
  - Hugging Face
topics:
  - Models
  - Open-weight
  - Research
translationKey: quark-165m-training-stack
image: /images/news/quark-165m-training-stack-2026-11-16.jpg
imageAlt: "Deyron Labs graphic: Empero's Quark is a 165M-parameter model trained for about $4,200 with four Apache 2.0 checkpoints; benchmark results are Empero's own; Empero post, 15 November 2026"
sources:
  - title: "Quark: our whole training stack, end to end, for $4,200"
    url: "https://empero.org/writing/quark"
    publisher: "Empero, 15 November 2026"
    primary: true
---

## What happened

On 15 November 2026 Empero published "Quark: our whole training stack, end to end, for $4,200", written by Leon Lehmann and "The Emperor". It describes Quark, a language model of about 165 million parameters (140 million without embeddings) with a 128K-token context, trained from scratch for roughly $4,200 of compute, about 1,300 H100 hours. Empero says the figure includes abandoned designs, failed attempts, data generation and every evaluation, and that part of the compute was sponsored by lium.io.

We read the post on 16 November 2026 (our browser translated it into Romanian; the figures match the English summaries we saw). Quark is a small research model from a small lab, and all performance numbers come from Empero's own runs.

## Key details

- **Release:** four checkpoints on Hugging Face under Apache 2.0: Quark-150M-32K-Raw, 32K-Base, 128K-Base and 128K-Zero. The last was trained with reinforcement learning only (GRPO), without supervised fine-tuning or distillation.
- **Training:** pretraining on 500 billion tokens on a single node of eight H100 GPUs.
- **Benchmarks (Empero-reported, lm-eval 0.4.13):** Quark-150M-128K-Base averages 52.8 across nine tasks, which Empero describes as the best in its group of open models of 120 to 170 million parameters. The post also lists SmolLM2-135M, trained on 2 trillion tokens (about four times as many), at 55.3, ahead of Quark on 7 of the 9 tasks.
- **Reinforcement learning (Empero-reported):** the share of simple terminal tasks solved rose from 3% to 65% in training rollouts, which the post does not present as a separate benchmark; correct answers on an internal suite rose from 13% to 36%.
- **Limitations the authors state:** web search did not improve, one of 15 harness formats never worked, long-context scores fell during RL, there was no safety evaluation, and they call the models "research artifacts, not products".

## Why it matters

Quark is evidence about cost, not capability: a usable small model trained for about the price of a used car, with the failures included in the bill. For researchers and hobbyists, an Apache 2.0 release with several checkpoints is a base they can inspect and modify.

It does not beat the strongest small model in its own comparison, and the results have not been reproduced by others. The value is in the openness and the stated limits, so treat the headline cost as Empero's accounting until someone repeats the run.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Empero is not affiliated with Deyron Labs; all claims about the model are Empero's own.
