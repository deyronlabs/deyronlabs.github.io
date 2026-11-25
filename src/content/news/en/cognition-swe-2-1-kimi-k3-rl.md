---
title: "Cognition releases SWE-2.1, a Kimi K3-based coding model, and reports 50.0 on Terminal-Bench 4.1"
summary: "Cognition says its new SWE-2.1 model, trained with reinforcement learning on top of Moonshot's Kimi K3, scores 50.0 on Terminal-Bench 4.1, up from 24.2 for SWE-2. Cognition's own table still shows Claude Opus 5.5 ahead at 65.8. SWE-2.1 is free through 12/8 on Devin Desktop and CLI; the benchmark figures are Cognition's."
seoTitle: "Cognition SWE-2.1: 50.0 on Terminal-Bench 4.1"
seoDescription: "Cognition's SWE-2.1, trained with RL on Kimi K3, scores 50.0 on Terminal-Bench 4.1 (SWE-2: 24.2), per Cognition; free through 12/8 on Desktop and CLI."
lang: en
publishedAt: 2026-11-25T20:40:00Z
entities:
  - Cognition
  - SWE-2.1
  - Devin
  - Kimi K3
  - Moonshot AI
  - Cerebras
topics:
  - Models
  - Coding
  - Agents
translationKey: cognition-swe-2-1-kimi-k3-rl
image: /images/news/cognition-swe-2-1-kimi-k3-rl.jpg
imageAlt: "Deyron Labs graphic: Cognition SWE-2.1, trained with RL on Kimi K3, scores 50.0 on Terminal-Bench 4.1 versus 24.2 for SWE-2 and 65.8 for Claude Opus 5.5, per Cognition"
sources:
  - title: "Introducing SWE-2.1"
    url: "https://cognition.com/blog/swe-2-1"
    publisher: "Cognition"
    primary: true
---

## What happened

On 24 November 2026, Cognition, the company behind Devin, published a post introducing SWE-2.1, an upgraded model for coding and agent work. Cognition says it trained SWE-2.1 with reinforcement learning on top of Kimi K3, the open-weight model from Moonshot AI, which makes it a fine-tune of a Chinese lab's model rather than a model trained from scratch.

We read the post on 25 November 2026. All benchmark numbers below are reported by Cognition; we have not run them and found no independent evaluation.

## Key details

- **Benchmarks (SWE-2.1 / SWE-2 / Claude Opus 5.5, as listed by Cognition):** Terminal-Bench 4.1: 50.0 / 24.2 / 65.8. FrontierCode 2.0: 41.3 / 24.1 / 47.3. ProgramBench: 44.0 / 17.0 / 65.0. SWE-Atlas QA: 71.0 / 63.7 / 77.4. SWE Marathon v1.2: 54.9 / 32.5 / 73.1. In Cognition's own table, SWE-2.1 roughly doubles SWE-2 on Terminal-Bench but stays below Claude Opus 5.5 on every row shown.
- **Security skills:** Cognition reports 80.0 on ExploitBench (SWE-2: 36.1), plus 27.3 success and 44.8 flag capture on ExploitGym. It also announces SWE-2.1 Cyber, a variant for Devin Security.
- **Speed:** SWE-2.1 Ultrafast, built with Cerebras, is described by Cognition as about 10x faster; we have not tested that claim.
- **Availability:** according to the post, SWE-2.1 is free through 12/8 in Devin Desktop and the CLI, and discounted until 1/30 in Devin Desktop, Cloud and the CLI.
- **Not stated in the post we read:** a license, whether weights are released, and per-token prices after the promotion.

## Why it matters

For people choosing a coding agent, SWE-2.1 is a cheaper, faster option from a tool vendor that now builds on an open-weight base instead of a closed frontier model. The reported jump on Terminal-Bench 4.1 is large, but it is a vendor's own comparison, and the same table places Claude Opus 5.5 clearly ahead.

Two things to watch: independent results on the same benchmarks, and what pricing looks like once the free and discounted periods end.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Cognition's comparison table includes Anthropic's Claude Opus 5.5, and Cognition's products compete with Anthropic's coding tools; all figures are Cognition's.
