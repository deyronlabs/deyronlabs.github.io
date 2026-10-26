---
title: "Nanbeige releases Nanbeige4.3-33B, an Apache 2.0 open-weight agent model with a 512K-token context"
summary: "Nanbeige LLM Lab, the research team of Chinese recruitment platform BOSS Zhipin, has published Nanbeige4.3-33B, a dense 33-billion-parameter agentic coding model with up to 524,288 tokens of context under Apache 2.0. All benchmark scores come from Nanbeige and have not been independently reproduced."
seoTitle: "Nanbeige4.3-33B: Apache 2.0 open-weight model"
seoDescription: "Nanbeige4.3-33B is a dense 33B open-weight agentic coding model with 512K context under Apache 2.0, released 25 October 2026; scores are self-reported."
lang: en
publishedAt: 2026-10-26T06:30:00Z
entities:
  - Nanbeige
  - Nanbeige4.3-33B
  - BOSS Zhipin
  - Hugging Face
  - Qwen3.8-27B
  - Gemma4-31B
topics:
  - Models
  - Open-weight
  - China
  - Coding
translationKey: nanbeige-4-3-33b-open-weights
image: /images/news/nanbeige-4-3-33b-open-weights-2026-10-26.jpg
imageAlt: "Deyron Labs graphic: Nanbeige4.3-33B, dense 33B open-weight agent model, 512K context, Apache 2.0, scores reported by Nanbeige"
sources:
  - title: "Nanbeige/Nanbeige4.3-33B-Base model card"
    url: "https://huggingface.co/Nanbeige/Nanbeige4.3-33B-Base"
    publisher: "Hugging Face (Nanbeige)"
    primary: true
  - title: "Nanbeige4.3-33B model coverage (NeMo AutoModel)"
    url: "https://docs.nvidia.com/nemo/automodel/model-coverage/large-language-models/nanbeige/Nanbeige4.3-33B"
    publisher: "NVIDIA"
  - title: "Nanbeige Releases Nanbeige4.3-33B, a 33B Open Agentic Coding Model"
    url: "https://www.marktechpost.com/2026/10/25/nanbeige-releases-nanbeige4-3-33b-open-agentic-coding-model/"
    publisher: "MarkTechPost"
  - title: "Nanbeige4.3-33B: Apache 2.0 dense agentic coding model with 512K context and benchmarks"
    url: "https://www.datastudios.org/post/nanbeige-4-3-33b-open-weight-dense-agentic-model-512k-context"
    publisher: "Data Studios"
---

## What happened

Nanbeige, an AI research group that sits inside the Chinese recruitment platform BOSS Zhipin, has published **Nanbeige4.3-33B** on Hugging Face, along with a **Nanbeige4.3-33B-Base** checkpoint meant for custom post-training. MarkTechPost reported the release on 25 October 2026; a secondary write-up says the weights were uploaded on 24 October. We read the Base model card directly. The card for the post-trained model, the launch post on X and Nanbeige's full benchmark chart were not available to us, so the figures for that model below come from secondary coverage and are attributed accordingly.

## Key details

- **Size and license (Hugging Face, NVIDIA):** a dense (not mixture-of-experts) model of about 33 billion parameters, listed as Apache 2.0 on the Base model card. NVIDIA's NeMo documentation describes the post-trained model as a 33.1B-parameter reasoning and agent model with 52 layers that loads through the standard Llama architecture; that page does not state a license.
- **Context (secondary sources):** up to 524,288 tokens (512K) for the post-trained model, according to MarkTechPost and NVIDIA's configuration notes. NVIDIA lists 131,072 positions for the Base checkpoint.
- **Base model scores (model card, reported by Nanbeige):** against Gemma4-31B-Base the card lists MMLU-Pro 66.9 vs 59.3, GPQA 62.0 vs 41.5, GSM8K 92.9 vs 88.9 and MATH 57.3 vs 43.6, with Nanbeige ahead on all eight rows it shows.
- **Post-trained model scores (reported by Nanbeige via MarkTechPost):** 80.9 on Terminal-Bench 2.1 (Qwen3.8-27B: 73.0), 65.5 on DeepSWE (42.5) and 95.2 on AIME 2026. The same coverage notes it trails Qwen3.8-27B on SWE-Bench Pro (60.3 vs 61.7) and Gemma4-31B on GPQA Diamond (89.5 vs 91.3).
- **Caveats:** no independent evaluation had been published when we checked. MarkTechPost says several competitor figures in Nanbeige's table conflict with those labs' own model cards, and Data Studios notes that some tests used adapted harnesses or subsets. Training data, recipe and compute are not disclosed, and no technical report was linked.
- **Hardware:** the weights are about 66 GB in BF16 (MarkTechPost's calculation), so the full model needs multiple GPUs; Data Studios reports that Nanbeige's serving recipes use four.
- **What's next:** MarkTechPost says Nanbeige positions the 33B model as a "teacher" for smaller models, starting with a 3B version that has no announced date. The group's earlier public models were 3B-class.

Checked against the Hugging Face Base model card, NVIDIA's documentation and secondary coverage on 26 October 2026.

## Why it matters

Permissively licensed open weights with long context and an agent focus give developers another model they can run and fine-tune without negotiating terms, and this one comes from a lab that was previously known for much smaller models. The Apache 2.0 license is stated on the Base card; check the post-trained model's own card before commercial use.

The strong headline numbers are Nanbeige's own, measured against competitors' scores that other labs' cards do not always match. Until independent evaluations appear, treat the comparison with Qwen3.8-27B as a claim to test on your own coding tasks, not a ranking.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Performance claims are Nanbeige's own unless stated otherwise.
