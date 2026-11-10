---
title: "Ant Group's Robbyant releases LingBot-Touch, an open tactile model for robot hands trained on about 5,000 hours of data"
summary: "Robbyant, the robotics unit of Ant Group, released LingBot-Touch 1.0, a model that learns a shared representation of touch from three kinds of tactile sensors. Its page reports about 4,983 hours of pretraining data and tests on 26 real-world tasks with two robot hands. Model weights and code are public; the results are Robbyant's own."
seoTitle: "Robbyant LingBot-Touch tactile model, 4,983 h"
seoDescription: "Ant Group's Robbyant released LingBot-Touch 1.0, a tactile model trained on about 4,983 hours of data, with weights and code public as of 9-10 Nov 2026."
lang: en
publishedAt: 2026-11-10T17:50:00Z
entities:
  - Robbyant
  - Ant Group
  - LingBot-Touch
  - Hugging Face
  - Sharpa Wave
  - XHand
topics:
  - Research
  - Open weights
translationKey: robbyant-lingbot-touch
image: /images/news/robbyant-lingbot-touch-2026-11-10.jpg
imageAlt: "Deyron Labs graphic: Robbyant releases LingBot-Touch, a tactile model for robot hands; about 4,983 hours of pretraining data, 26 real-world tasks on two robot hands, results reported by Robbyant"
sources:
  - title: "LingBot-Touch 1.0: Learning Heterogeneous Tactile Representation for General Dexterous Manipulation (Robbyant project page)"
    url: "https://technology.robbyant.com/lingbot-touch"
    publisher: "Robbyant (Ant Group)"
    primary: true
  - title: "lingbot-touch-tiny and lingbot-touch-small (Hugging Face model listings)"
    url: "https://huggingface.co/robbyant/lingbot-touch-tiny"
    publisher: "Hugging Face"
    primary: true
  - title: "LingBot-Touch code repository"
    url: "https://github.com/Robbyant/lingbot-touch"
    publisher: "GitHub"
    primary: true
  - title: "Ant Group's Robbyant open-sources tactile AI model for robot hands (TechNode, 10 November 2026)"
    url: "https://technode.com/2026/11/10/ant-groups-robbyant-open-sources-tactile-ai-model-for-robot-hands/"
    publisher: "TechNode"
---

## What happened

Robbyant, a robotics company that is part of Ant Group, published LingBot-Touch 1.0, which its project page describes as a tactile foundation model for general dexterous manipulation. The page says the model learns one shared representation of touch from different tactile sensors, so that a robot hand can use it whichever sensor it carries. The Hugging Face listings for two sizes, `lingbot-touch-tiny` and `lingbot-touch-small`, were created on 9 November 2026, and TechNode reported the release on 10 November.

## Key details

All numbers below are from Robbyant's project page unless stated, and they are the lab's own reports; we did not find an independent evaluation.

- **Method:** a JEPA-based tactile representation model, meaning it predicts latent representations from touch context over time, with a shared "Haptic Transformer" encoder and a separate tokenizer for each sensor type.
- **Size:** the page gives 5.46 million parameters for the HaT-Tiny encoder. It names no other size, and we found no parameter count for the "small" release.
- **Pretraining data:** about 4,983 hours of recordings, 464,431 episodes and about 1.33 billion frames. By sensor type: piezoresistive 2,197 hours, magnetic 1,136 hours, visuotactile 1,650 hours. The data comes from tactile gloves and robot hands.
- **Evaluation:** 26 real-world dexterous tasks (20 on a Sharpa Wave hand and 6 on an XHand) with 20 trials each, and 12 simulated reinforcement-learning tasks. Examples on the page include unlocking with a key, dispensing toothpaste, handling a resealable bag, ejecting an SD card and twisting a cap. The page compares an original policy, raw tactile input, and adding LingBot-Touch features in post-training, and reports that real-world success rises as tactile pretraining grows from 0 to 5,000 hours. The exact success rates are in charts and a table in the technical report that we did not read, so we do not quote them.
- **Availability:** code at github.com/Robbyant/lingbot-touch and a technical report PDF linked from the page, plus a collection on Hugging Face and ModelScope. The Hugging Face listings carry an `apache-2.0` license tag; the project page we read does not state a license, so check the repository before reuse.

## Why it matters

Most robot-learning work leans on cameras, and touch data is scarce and differs from one sensor to the next. A pretrained tactile model that works across sensor types, with public weights, gives other labs a starting point for tasks where vision is blocked or ambiguous, such as small parts, bags or locks. For readers of this site who use AI tools rather than build robots, the near-term impact is limited; the item matters mainly as another sign that Chinese labs are releasing robotics models openly alongside language models.

Treat the performance claims as Robbyant's until an independent group reproduces them.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Figures are attributed to the lab.
