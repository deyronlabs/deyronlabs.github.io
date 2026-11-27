---
title: "NVIDIA releases Nemotron-Labs-Image-30B-A3B, a 30B image model with 3B active parameters, for research use"
summary: "NVIDIA published the weights of Nemotron-Labs-Image-30B-A3B on Hugging Face, an autoregressive image generator with 30B total and 3B active parameters, under a non-commercial research and evaluation license. NVIDIA's scores beat GPT Image 2 on GenEval but trail it on GenEval2 and Qwen-Image-Bench. The scores are NVIDIA's own and come from its full VisualCreation framework, which is not yet released."
seoTitle: "NVIDIA Nemotron-Labs-Image-30B-A3B: open weights"
seoDescription: "NVIDIA's Nemotron-Labs-Image-30B-A3B has 30B parameters (3B active) and non-commercial weights; its GenEval 92.86 trails GPT Image 2 on other tests."
lang: en
publishedAt: 2026-11-27T09:39:00Z
entities:
  - NVIDIA
  - Nemotron-Labs-Image-30B-A3B
  - Nemotron 3 Nano
  - GPT Image 2
  - Nano Banana Pro
topics:
  - Models
  - Open-weight
  - Image generation
translationKey: nvidia-nemotron-labs-image-30b-a3b
image: /images/news/nvidia-nemotron-labs-image-30b-a3b.jpg
imageAlt: "Deyron Labs graphic: NVIDIA Nemotron-Labs-Image-30B-A3B, 30B parameters with 3B active; non-commercial license; GenEval 92.86 vs GPT Image 2 89.00 but GenEval2 65.43 vs 81.00; scores are NVIDIA's own"
sources:
  - title: "nvidia/Nemotron-Labs-Image-30B-A3B (model card README)"
    url: "https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B"
    publisher: "NVIDIA on Hugging Face, read 26 November 2026 (the card does not show a release date)"
    primary: true
---

## What happened

NVIDIA published **Nemotron-Labs-Image-30B-A3B** on Hugging Face, with weights, a tokenizer and inference code. It is an autoregressive image generation model, part of what NVIDIA calls "Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation" (arXiv 2611.31358, authors from NVIDIA, UNC, UCSC, UMD and Nanjing University). We read the model card on 26 November 2026. The page does not give a release date; newsletters began reporting it on 25 November. We have not run the model.

## Key details

- **Architecture:** 30B total and 3B active parameters, built on the Nemotron 3 Nano architecture and initialized from it, with its own tokenizer of about 642M parameters (16x16 patches, a 196,560-vector codebook). Training included mid-training followed by reinforcement learning with GRPO.
- **License:** "non-commercial research and evaluation under the NVIDIA License" (Hugging Face tag `other`). It is not usable commercially under this release.
- **What is released:** the model, tokenizer and inference code. The VisualCreation harness and VisionCode are "will be released upon legal clearance".
- **Scores (NVIDIA's own):** NVIDIA says its scores come from the VisualCreation framework ("our best score across configurations evaluated"), not from the model alone. GenEval 92.86 versus 89.00 for GPT Image 2; GenEval2 65.43 versus 81.00 for GPT Image 2 and 59.00 for Nano Banana Pro; OneIG 54.63 versus 58.30 for Nano Banana Pro; Qwen-Image-Bench 52.46 versus 65.23 for GPT Image 2. NVIDIA also reports LongTextBench 97.98, CVTG-2K 92.53, WISE Verified 91.50, and BizGenEval 86.0 versus 83.2 and 76.7 for the comparison models it lists.
- **Tokenizer:** PSNR 29.57 versus 26.08 for the Emu3.5 IBQ tokenizer, and encoding in 41.30 ms versus 294.53 ms.
- **Running it:** the example setup uses four H100 80GB GPUs with vLLM 0.21.0 and requires `trust_remote_code`. NVIDIA notes generation is stochastic and text or counts in images can be wrong.
- **Not stated:** any independent evaluation. The card does not support a blanket claim of beating GPT Image 2; it trails on several of the tests above.

## Why it matters

Open weights for a mixture-style autoregressive image model give researchers something to study that is not a diffusion model, and the 3B active size is small relative to the 30B total. The non-commercial license and the unreleased harness limit what outside teams can do with it today.

Read the benchmark table as NVIDIA's own, taken under its own framework: the mixed results against GPT Image 2 and Nano Banana Pro are more informative than the single best number.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. NVIDIA is not affiliated with Deyron Labs; all claims are NVIDIA's own.
