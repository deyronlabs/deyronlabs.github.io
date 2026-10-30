---
title: "Mistral releases Mistral Large 4 as open weights under a modified MIT license"
summary: "Mistral AI has published the weights of Mistral Large 4, a 1-trillion-parameter multimodal model, under a license it calls a modified MIT license, and cut its API price to $0.70 and $2.10 per million input and output tokens. Benchmark figures are Mistral's own, and a technical report is still to come."
seoTitle: "Mistral Large 4 open weights, modified MIT"
seoDescription: "Mistral Large 4, a 1-trillion-parameter model, now has open weights under a modified MIT license and API prices of $0.70 and $2.10 per million tokens."
lang: en
publishedAt: 2026-10-07T09:20:00Z
updatedAt: 2026-10-30T07:00:00Z
entities:
  - Mistral AI
  - Mistral Large 4
  - Mistral Studio
  - Hugging Face
  - NVIDIA
  - Microsoft Foundry
  - GLM-5.3
  - Kimi K3
  - GPT-6 Astra
  - Claude Opus 5.5
topics:
  - Models
  - Europe
  - Open weights
  - Cybersecurity
translationKey: mistral-large-4-public-preview
video: "https://www.youtube.com/shorts/Em9MwL7Hyic"
videoPublishedAt: 2026-10-30
image: /images/news/mistral-large-4-open-weights-2026-10-30.jpg
imageAlt: "Deyron Labs graphic: Mistral Large 4 open weights, 1 trillion parameters, modified MIT license, API at $0.70 and $2.10 per million tokens"
sources:
  - title: "Mistral Large 4 open weights (Le Chonk)"
    url: "https://mistral.ai/news/mistral-large-4-oss/"
    publisher: "Mistral AI"
    primary: true
  - title: "Introducing Mistral Large 4"
    url: "https://mistral.ai/news/mistral-large-4/"
    publisher: "Mistral AI"
    primary: true
  - title: "OpenAI launches GPT-6 Astra"
    url: "https://www.constellationr.com/insights/news/openai-launches-gpt-6-astra"
    publisher: "Constellation Research"
  - title: "OpenAI Launches GPT-6 Astra: Pricing, Benchmarks and Who Gets It First"
    url: "https://pasqualepillitteri.it/en/news/14246/openai-launches-gpt-6-astra-pricing-benchmarks"
    publisher: "Pasquale Pillitteri"
---

## What happened

**Update, 30 October 2026:** Mistral AI has released the weights of Mistral Large 4, the model it nicknames "Le Chonk", which it first made available in public preview on 6 October. The announcement page carries no visible date; news coverage places it on 29 October. Mistral describes the model as a 1-trillion-parameter, natively multimodal, hybrid instruct-and-reasoning mixture-of-experts model, and says it "ranks as the best open-weight model for coding".

The weights are on Hugging Face (repository `mistralai/Mistral-Large-4-1T-A52B`) and the model is also served through the Mistral API, Mistral Studio, OpenRouter, NVIDIA-hosted endpoints and Microsoft Foundry. Mistral calls the license the "Mistral Ecosystem Open-Weight license, a modified MIT license".

On 6 October, Mistral announced the model as a public preview with 1 trillion parameters, 49 billion of them active, and promised weights by the end of the month. The original preview details follow below the update.

## Key details

**Open-weights release (Mistral's page, read 30 October):**

- **License:** free to use, modify, fine-tune and commercialize, with one condition: businesses that operate a Model-as-a-Service offering "must obtain a separate commercial license from Mistral before using the model commercially". The page gives no revenue threshold and does not define the term; the full license text is in the Hugging Face repository, which we have not reviewed.
- **API price:** $0.70 per million input tokens, $0.07 cached input and $2.10 per million output tokens, about half the $1.36 and $4.18 listed at the preview launch.
- **Parameters:** the page says 1 trillion in total and does not state the active count. The repository name suggests about 52 billion active, whereas the preview announcement said 49 billion; we have not resolved the difference.
- **Coding (Mistral's reported figures):** 41% on Terminal-Bench 4.0, up from 28% at preview, with 30% fewer output tokens; 48% on the Artificial Analysis Coding Agent Index, which Mistral describes as "effectively tied" with GLM-5.3 while using 47% fewer tokens per task; 19.7% on Cognition's private FrontierCode 2.0. In a blind pairwise human-preference test run by Surge, Mistral says it was preferred over GLM-5.3, Kimi K3 and DeepSeek V4.1 Flash, "ranking behind only Claude Opus 5.5 among the models evaluated".
- **Cybersecurity (Mistral's reported figures):** 51% on the Artificial Analysis Cyber Index; an average refusal rate of 96.6% on malicious cyber requests, which Mistral calls "the highest we measure among open models"; and 97.1% on the B3 agent-security benchmark, up from 93.3% at preview. Mistral also warns that although it saw the model refuse black-box attacks on live targets, it sees "a potential for uplift to conduct real attacks". A specialized cybersecurity variant is in preview for vetted design partners only.
- **Not stated on the page:** a publication date, the context window, hardware requirements and a technical report (described as "coming soon").

**Preview launch (6 October, Mistral's figures):**

- **Price at preview:** $1.36 per million input tokens and $4.18 per million output tokens.
- **Training and languages:** Mistral says it trained the model on 3,800 NVIDIA Grace Blackwell GPUs in its own European datacenters and that it supports more than 160 languages.
- **Cybersecurity at preview:** 82% on a vulnerability reproduction and patching test, 93% of the challenges in Cybench and 93.3% resistance to attacks on B3. Mistral said Claude Opus 5.5 and GPT-6 Astra scored close to zero on the same vulnerability test because they refuse the task.
- **Coding at preview:** 61.7% on DeepSWE v1.1, 59.4% on SWE-Atlas-QnA and 28.3% on Terminal-Bench 4.
- **Independent evaluation:** we found none for the preview, and the open-weights page cites third-party benchmarks run on Mistral's behalf. Treat every figure above as Mistral's.

## Why it matters

The open question from the preview, whether the weights would arrive and on what terms, now has an answer. The license is permissive for most users, but the Model-as-a-Service condition means companies that resell hosted access need a separate agreement with Mistral. Read the full license before you build a product on it.

The price cut matters as much for people who stay on the API. Per-token rates are now roughly half of the preview rates, and Mistral says the new version also uses fewer tokens on coding tasks, though the "improved" hosted model may differ from the preview you tested. A 1-trillion-parameter model is also large to self-host, and the page gives no hardware guidance, so check the memory requirements first.

The cybersecurity claims call for care. A high refusal rate on malicious requests and high scores on defensive tasks are Mistral's own measurements, and Mistral itself notes a potential for misuse. Wait for independent tests before you rely on the model for security work.

> Disclosure: Anthropic, the maker of Claude, is named in Mistral's comparison above, and Claude was one of the AI tools used to research and draft this article. Performance and pricing claims are the companies' own unless stated otherwise.
