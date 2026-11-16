---
title: "Thinking Machines details end-to-end 4-bit training, reporting 8% faster pretraining than MXFP8 for Inkling 2 Small"
summary: "On 13 November 2026 Thinking Machines Lab published a technical post on training Inkling 2 Small with NVFP4, a 4-bit format, on NVIDIA GB300 hardware. The lab reports 8% faster pretraining and 20% faster reinforcement learning than full MXFP8 at about 2% cost in compute efficiency. All figures are the lab's own."
seoTitle: "Thinking Machines: 4-bit training, 8% faster"
seoDescription: "Thinking Machines Lab's 13 Nov 2026 post reports 4-bit NVFP4 training of Inkling 2 Small: 8% faster pretraining, 20% faster RL than MXFP8, lab figures."
lang: en
publishedAt: 2026-11-16T18:48:00Z
entities:
  - Thinking Machines Lab
  - Inkling 2 Small
  - NVFP4
  - MXFP8
  - NVIDIA GB300 NVL72
topics:
  - Research
  - Hardware
  - Models
translationKey: thinking-machines-4bit-training
image: /images/news/thinking-machines-4bit-training-2026-11-16.jpg
imageAlt: "Deyron Labs graphic: Thinking Machines Lab reports end-to-end 4-bit NVFP4 training of Inkling 2 Small, 8% faster pretraining and 20% faster RL than MXFP8, pretrained in 68 hours on GB300 NVL72; lab figures"
sources:
  - title: "End-to-End 4-Bit Training"
    url: "https://thinkingmachines.ai/blog/end-to-end-4-bit-training/"
    publisher: "Thinking Machines Lab (Connectionism blog), 13 November 2026"
    primary: true
---

## What happened

On 13 November 2026 Thinking Machines Lab published "End-to-End 4-Bit Training" on its Connectionism blog, written by Jack Cook and colleagues. The post describes how the lab trained Inkling 2 Small, the model it released on 5 November, using the BF16, MXFP8 and NVFP4 number formats on NVIDIA GB300 hardware, with NVFP4 as a 4-bit format used in the forward pass.

We read the post on 16 November 2026. It is a technical description by the lab itself: the numbers below are the lab's, and we have not seen independent replication.

## Key details

- **Format claims (lab-reported):** NVFP4 is stored with 3.6 times fewer bits than BF16 and runs up to 6 times faster on GB300.
- **Recipe:** the forward pass uses NVFP4 in the expert layers, the backward pass uses MXFP8 with re-quantization and stochastic rounding, and communication is also quantized.
- **Speed (lab-reported):** the recipe gives an 8% speedup in pretraining and 20% in reinforcement learning compared with using MXFP8 throughout.
- **Cost:** the lab says the approach costs about 2% in compute efficiency during pretraining.
- **Scale:** the lab calls Inkling 2 Small the largest known model trained with a native 4-bit forward pass, pretrained in 68 hours on GB300 NVL72 racks.
- **Not stated:** how the 4-bit run compares with higher-precision training on final model quality outside the lab's own evaluations, and any release of the training code.

## Why it matters

Lower-precision training is one of the main ways labs cut the cost of large models, and this post is a concrete account of doing it at the scale of a 594-billion-parameter model on current NVIDIA hardware. An 8% to 20% speedup for a small efficiency penalty, if it holds, is meaningful at that scale.

It is research that explains how an existing model was made, not a new product or release. The claims will carry more weight once others reproduce them on their own hardware.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Thinking Machines Lab is not affiliated with Deyron Labs; all claims in the post are the lab's own.
