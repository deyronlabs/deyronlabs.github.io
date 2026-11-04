---
title: "Deep Principle releases Hydrogen-1.0, a 753B science model post-trained from GLM-5.3, with MIT-licensed weights"
summary: "Deep Principle published Hydrogen-1.0, a model post-trained from GLM-5.3 on chemistry, materials and life-science data. The Hugging Face card lists 753B parameters, a 1M-token context and an MIT license for the weights. The company says it beats GPT-6 Astra on one science benchmark; those results are its own."
seoTitle: "Deep Principle Hydrogen-1.0: 753B, MIT license"
seoDescription: "Deep Principle's Hydrogen-1.0, post-trained from GLM-5.3, lists 753B parameters and MIT-licensed weights; benchmark claims are its own."
lang: en
publishedAt: 2026-11-04T06:15:00Z
entities:
  - Deep Principle
  - Hydrogen-1.0
  - GLM-5.3
  - GPT-6 Astra
  - Kimi-K3
topics:
  - Models
  - Open-weight
  - Science
  - China
translationKey: deep-principle-hydrogen-1-0-open-weights
image: /images/news/deep-principle-hydrogen-1-0-open-weights-2026-11-04.jpg
imageAlt: "Deyron Labs graphic: Deep Principle Hydrogen-1.0, 753B parameters post-trained from GLM-5.3, MIT-licensed weights on Hugging Face, benchmark claims are the company's"
sources:
  - title: "Introducing Hydrogen-1.0 (Deep Principle blog)"
    url: "https://blog.deepprinciple.com/introducing-hydrogen-1.0/"
    publisher: "Deep Principle"
    primary: true
  - title: "deep-principle/Hydrogen-1.0 (Hugging Face model card)"
    url: "https://huggingface.co/deep-principle/Hydrogen-1.0"
    publisher: "Hugging Face"
    primary: true
---

## What happened

Deep Principle introduced Hydrogen-1.0, which it describes as "post-training GLM-5.3 on domain data from chemistry, materials science, and life sciences." The blog post carries no explicit date on the page; file paths in it suggest 2 November 2026, which we have not confirmed. GLM-5.3 is from Zhipu (Z.ai). We report the company's claims as the company's.

## Key details

- **Model card (Hugging Face):** 753B parameters, 1M-token context, 128K maximum output. Weights are "provided under the MIT License"; the company's own code and docs are Apache-2.0. The repository is gated: users must agree to share Hugging Face information. NVFP4 and MXFP4 variants are listed, and the card says it was tested with SGLang on 8 GPUs.
- **Benchmark claims (blog):** Hydrogen-1.0 "outperforms GPT-6-Astra on FrontierScience-Research (FSR)," improves on GLM-5.3 on GPQA-Diamond and roughly matches Kimi-K3. The text gives no numeric FSR or GPQA scores; they appear only in figures.
- **Internal evaluations:** the company reports leads over Astra of 5.13 and 4.76 percentage points on scientific computing and forward reactions at maximum thinking, and says Astra "still scores higher on NMR structure elucidation by 3.33 points."
- **Not released:** training data and recipes. The model card has no benchmark table and warns that outputs "should not be treated as verified experimental findings."

## Why it matters

Open weights under MIT make a large science-tuned model available for self-hosting, which is rare at this size. The comparison with GPT-6 Astra is the company's, on a benchmark and internal tests that outside groups have not run, so it is best read as a claim to check. The size also means self-hosting needs serious GPU capacity.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. All statements are Deep Principle's own, read from its blog and model card on 4 November 2026.
