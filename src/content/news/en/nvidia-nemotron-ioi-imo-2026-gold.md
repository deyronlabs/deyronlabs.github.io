---
title: "NVIDIA reports gold-level results at IOI and IMO 2026 with Nemotron-based systems and publishes the models and data"
summary: "NVIDIA says Nemotron-based systems scored 535.4 of 600 at IOI 2026, in an unofficial unsupervised run, and 30 of 42 at IMO 2026, graded by official IMO graders. It links checkpoints, training datasets and a 200-problem benchmark; the post names no license. The results are NVIDIA's own."
seoTitle: "NVIDIA Nemotron hits gold at IOI and IMO 2026"
seoDescription: "NVIDIA says Nemotron-based systems scored 535.4 of 600 at IOI 2026, in an unofficial unsupervised run, and 30 of 42 at IMO 2026, graded by official IMO…"
lang: en
publishedAt: 2026-10-09T05:30:00Z
entities:
  - NVIDIA
  - Nemotron
  - Nemotron-3-Nano-CC
  - Nemotron-3-Ultra-CC
  - IOI
  - IMO
topics:
  - Research
  - Open weights
  - Reasoning
translationKey: nvidia-nemotron-ioi-imo-2026-gold
image: /images/news/nvidia-nemotron-ioi-imo-2026-gold-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: NVIDIA reports gold-level IOI and IMO 2026 results with Nemotron systems; the IOI run was unofficial; results are NVIDIA's own"
sources:
  - title: "One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO"
    url: "https://huggingface.co/blog/nvidia/nemotron-ioi-and-imo-2026"
    publisher: "NVIDIA (Hugging Face blog)"
    primary: true
---

## What happened

On 7 October 2026, NVIDIA published a Hugging Face blog post, "One Model Family, Two Gold-Level Results: Fine-Tuning Nemotron for IOI and IMO". It reports gold-level results at the 2026 International Olympiad in Informatics (IOI) and International Mathematical Olympiad (IMO) using systems built on its Nemotron models.

## Key details

All results below are NVIDIA's own.

- **IOI 2026:** 535.4 of 600 points, above the 361.12 gold threshold and the top human score of 498.27. NVIDIA says this was an unofficial, unsupervised run that is not part of the official IOI ranking.
- **IMO 2026:** 30 of 42 points, above the official gold threshold of 29, with full credit on four of six problems. NVIDIA says official IMO graders graded the submitted proofs.
- **Models:** Nemotron-3-Nano-CC (30B total, 3B active parameters, trained with SFT and RL) and Nemotron-3-Ultra-CC (550B total, 55B active parameters, trained with SFT), the latter available on Hugging Face as an NVFP4 checkpoint. The IMO system uses checkpoints from Nemotron 3 Ultra in a generate-verify-refine loop.
- **Method:** NVIDIA writes that the medals "were not produced by fine-tuning alone, and they were not produced by brute-force sampling alone"; results combine specialized training with a system that searches, verifies and refines answers. It reports IOI 2025 progress for Nemotron-3-Nano-CC from 130 points before post-training to 468 with an added step it calls GenCorrect.
- **Released material:** the post links SFT and RL checkpoints, two training datasets, Nemotron-IMO-Bench (200 olympiad-level problems) and NeMo-Skills inference pipelines. It states no license for the models or code.

## Why it matters

The released checkpoints, datasets and benchmark let other researchers inspect and try to reproduce NVIDIA's approach, which is less common for olympiad-level results. The unofficial status of the IOI run and the missing license are the caveats to note, along with the fact that the numbers are self-reported.

For a general audience the practical point is the method, not the medals: NVIDIA says the results depend on a search-and-verify system around the model, so the model alone does not score at that level.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claims and results are NVIDIA's own.
