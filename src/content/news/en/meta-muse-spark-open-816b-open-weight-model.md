---
title: "Meta releases Muse Spark Open, an 816B-parameter open-weight model with a 1M-token context and a revenue-capped license"
summary: "On 15 October 2026 Meta Superintelligence Labs released Muse Spark Open, a multimodal mixture-of-experts model with 816B total and 42B active parameters and a 1M-token context. Weights are downloadable under the Muse Model License, which requires a separate agreement from companies over $20 million in revenue that sell the model as a service. On Meta's own table it trails Kimi K3 and GLM 5.3 on several tests."
seoTitle: "Meta Muse Spark Open: 816B open weights"
seoDescription: "Meta's Muse Spark Open, released 15 Oct 2026, has 816B parameters (42B active) and open weights under a license with a $20M revenue condition for hosting."
lang: en
publishedAt: 2026-10-16T06:20:00Z
entities:
  - Meta
  - Meta Superintelligence Labs
  - Muse Spark Open
  - Muse Model License
  - Kimi K3
  - GLM 5.3
  - Qwen3.8
  - Hugging Face
topics:
  - Models
  - Open-weight
translationKey: meta-muse-spark-open-816b-open-weight-model
video: https://www.youtube.com/shorts/nniyyF897gU
videoPublishedAt: 2026-10-16T06:15:00Z
image: /images/news/meta-muse-spark-open-816b-open-weight-model-2026-10-15.jpg
imageAlt: "Deyron Labs graphic: Meta releases Muse Spark Open on 15 October 2026; 816B parameters, 42B active, 1M-token context; open weights under the Muse Model License, separate agreement above $20 million revenue to offer it as a service; Artificial Analysis Intelligence Index 39 versus 45 for GLM 5.3 and 44 for Kimi K3, Meta's own table"
sources:
  - title: "Introducing Muse Spark Open, The Most Capable US Open-Weight Model to Date"
    url: "https://research.meta.ai/blog/muse-spark-open"
    publisher: "Meta Superintelligence Labs (15 October 2026)"
    primary: true
  - title: "meta-models/Muse-Spark-Open-816B-A42B (model card and license)"
    url: "https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B"
    publisher: "Meta on Hugging Face (15 October 2026)"
    primary: true
  - title: "Welcome Muse Spark Open: open-weight frontier multimodal mixture-of-experts model from Meta"
    url: "https://huggingface.co/blog/meta-muse-spark-open"
    publisher: "Hugging Face (15 October 2026)"
    primary: false
---

## What happened

On 15 October 2026 Meta Superintelligence Labs released Muse Spark Open, a multimodal model whose weights anyone can download. Meta describes it as "the most capable US open-weight model to date", and says it is aimed at coding and agentic work such as long software-engineering tasks and multi-step reasoning. It follows Meta's closed Muse Wonder models, released three days earlier, which are only available through an API and Meta's own plans.

Weights are on Hugging Face (behind a gated sign-up form) and on Amazon SageMaker AI, Google Cloud Model Garden and Microsoft Foundry Models. Meta also lists hosted APIs at Baseten, Fireworks AI, Groq, Modal, Nebius, OpenRouter and Together AI. The announcement does not state an API price.

## Key details

Everything below comes from Meta's announcement and model card, read on 16 October 2026. The benchmark table is Meta's own selection, and we have not run the model.

- **Size:** 816B total parameters, 42B active per token, in a mixture-of-experts design with 256 experts and 8 activated per token over 62 layers. The file metadata lists 822B. Context is 1M tokens.
- **Modalities:** input can be text, images, video and audio; output is text only. Training data covers more than 100 languages, though Meta says not all were evaluated.
- **License:** the Muse Model License allows use, modification (including fine-tuning), distillation, merging, redistribution and sale. Products built on it must prominently display "Built with Muse Spark Open". If a licensee's affiliates have combined gross revenue above $20 million in any 12 consecutive months, they must notify Meta and sign a separate agreement before offering the model as a service. Internal use, research and embedding it in your own product (not as a service) are exempt. The model is not intended for people under 18. Whether this counts as "open source" is a separate question; Meta calls it open-weight.
- **Hardware:** the NVFP4 weights need at least 700GB of GPU memory and the BF16 weights 2TB, according to the model card. Meta shows it running on two Apple Mac Studios with M5 Ultra chips.
- **Benchmarks in Meta's model card** (Muse Spark Open at "xhigh" reasoning, against Qwen3.8, GLM 5.3 and Kimi K3): Artificial Analysis Intelligence Index 39 (40, 45, 44); MCP-Atlas 89.2 (84.5, 84.2, 82.3); JobBench 61.8 (52.7, 61.4, 54.3); HLE-Diamond without tools 26.1 (17.3, 16.4, 22.2); Terminal-Bench 2.1 76.4 (82.0, 83.9, 85.0); GPQA Diamond 89.0 (93.5, 91.7, 93.5); OSWorld Verified 80.4 (no Qwen or GLM score, Kimi 84.8). Meta's own table therefore shows mixed results against the Chinese open models rather than a clear lead.
- **Safety:** Meta says it added safety post-training because the weights are open, evaluated the model under its Superintelligence Scaling Framework and found it met the framework's release thresholds. The detailed evaluation report is described as "available soon".

## Why it matters

For developers, this is a large model they can legally self-host or fine-tune. In practice the hardware bar is high: roughly 700GB of GPU memory at the smallest official quantization, so most teams will use one of the hosted APIs instead. The license is the other practical point. Small teams can build freely, but a company above $20 million in revenue that wants to resell access has to negotiate with Meta first.

The headline claim is narrower than it sounds. "Most capable US open-weight model" is Meta's wording, and on Meta's own table the Chinese open models Kimi K3 and GLM 5.3 score higher on the Artificial Analysis index and on Terminal-Bench. Independent tests of agent and coding work, and the promised safety report, will show how it holds up outside Meta's table.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is not a party to this announcement. Figures are Meta's own, taken from its 15 October 2026 announcement and model card.
