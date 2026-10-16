---
title: "Mistral releases Timestral, its first family of time-series forecasting models, from 5M to 209M parameters"
summary: "On 15 October 2026 Mistral AI introduced Timestral, four time-series foundation models of 5M, 28M, 123M and 209M parameters for probabilistic forecasting. Mistral says the largest ranks first on the GIFT-Eval, TIME and fev-bench leaderboards, and publishes code under a modified MIT license. Rankings and speeds are Mistral's own."
seoTitle: "Mistral Timestral: forecasting models, 5M-209M"
seoDescription: "Mistral's Timestral, introduced 15 Oct 2026, is a family of four time-series forecasting models (5M to 209M parameters) under a modified MIT license."
lang: en
publishedAt: 2026-10-16T06:20:00Z
entities:
  - Mistral AI
  - Timestral
  - Mistral Forge
  - GIFT-Eval
  - TIME
  - fev-bench
  - Chronos-2
topics:
  - Models
  - Open-weight
translationKey: mistral-timestral-time-series-forecasting-models
image: /images/news/mistral-timestral-time-series-forecasting-models-2026-10-15.jpg
imageAlt: "Deyron Labs graphic: Mistral introduces Timestral on 15 October 2026; four time-series forecasting models of 5M, 28M, 123M and 209M parameters; 32,768 time-step context; modified MIT license; leaderboard rankings and CPU speeds are Mistral's own"
sources:
  - title: "Introducing Timestral"
    url: "https://mistral.ai/news/timestral/"
    publisher: "Mistral AI (15 October 2026)"
    primary: true
---

## What happened

On 15 October 2026 Mistral AI introduced Timestral, which it describes as its first family of time-series foundation models. These are models that take a history of numbers, such as sales, energy use or sensor readings, and forecast what comes next, instead of generating text. Mistral says all four models share one architecture and training recipe and differ only in size.

Mistral links a GitHub repository for running Timestral on your own data, a Hugging Face collection and model documentation. The announcement does not use the phrase "open weights" and does not describe a hosted API or give prices. Companies that want fine-tuning or deployment on-premises, in a private cloud or air-gapped can use Mistral Forge, Mistral's customization product.

## Key details

All figures below are Mistral's, read from its announcement on 16 October 2026. Mistral evaluated the models itself, and we have not run them.

- **Sizes:** 5M, 28M, 123M and 209M parameters. Context is 32,768 time steps. The models forecast several series at once and output probabilistic forecasts at 21 quantiles, and they accept covariates that are known only in the past or also for the future.
- **License:** modified MIT.
- **Rankings:** Mistral says the 209M model ranks first on GIFT-Eval, TIME and fev-bench, and first among pre-trained zero-shot models on all five metrics, from a single checkpoint without ensembling. It says this beats the previous state of the art with "two-thirds of the model parameters", and that the 28M model beats Chronos-2, which it describes as about four times larger, on GIFT-Eval and TIME. The announcement gives these as rankings and charts, not exact scores in text.
- **Speed:** on a standard server CPU with 8 threads, forecasting one day ahead from three weeks of 15-minute history takes 10 ms with the 5M model and 140 ms with the 209M model. Mistral says the 123M model is within 0.2% of the 209M score at three quarters of its latency.
- **Method:** synthetic-first pre-training and a two-stage schedule with a 4x longer context in the second stage. Mistral says a technical report on a method it calls Decoupled Horizon Forecasting is still to come.

## Why it matters

Forecasting is one of the most common business uses of machine learning, and these models are small enough to run on an ordinary CPU in milliseconds, which makes them practical for teams that cannot send operational data to an outside API. A modified MIT license and a public repository lower the barrier further, but because the license is modified, teams should read its exact terms before building on it.

The ranking claims are the part to treat carefully. Mistral ran the evaluations and published charts, and the technical report that would explain the main method has not appeared. Independent runs on a team's own data will matter more than leaderboard position, since forecasting accuracy varies widely by domain.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is not a party to this announcement. Figures are Mistral's own, taken from its 15 October 2026 announcement.
