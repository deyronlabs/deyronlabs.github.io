---
title: "MIT authors say GPT-6 Astra can edit neural network weights, lifting Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1%"
summary: "In a 2 November 2026 post, four MIT CSAIL researchers report that GPT-6 Astra edited the weights of small networks with no gradient descent. Changing 0.016% of Qwen3.5-0.8B's weights raised MATH-500 from 7.9% to 48.1%, but the same edit approach could not improve Gemma. The authors call the results early and limited."
seoTitle: "MIT: GPT-6 Astra edits weights, no training"
seoDescription: "MIT CSAIL authors report GPT-6 Astra edited 0.016% of Qwen3.5-0.8B's weights without training, lifting MATH-500 from 7.9% to 48.1% (2 Nov 2026)."
lang: en
publishedAt: 2026-11-04T06:30:00Z
entities:
  - MIT CSAIL
  - GPT-6 Astra
  - OpenAI
  - Qwen3.5-0.8B
  - Gemma 3
topics:
  - Research
  - Models
translationKey: mit-weight-space-programming-gpt-6-astra
image: /images/news/mit-weight-space-programming-gpt-6-astra-2026-11-02.jpg
imageAlt: "Deyron Labs graphic: MIT authors report GPT-6 Astra edited 0.016% of Qwen3.5-0.8B weights, MATH-500 7.9% to 48.1%, Gemma control not improved"
sources:
  - title: "Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights (Takehi, Teoh, Zhang, Khattab, 2 November 2026)"
    url: "https://rikiyat.github.io/blog/weight-space-programming/"
    publisher: "MIT CSAIL authors"
    primary: true
  - title: "Experiment logs (GitHub)"
    url: "https://github.com/RikiyaT/lm_understand-logs"
    publisher: "Rikiya Takehi"
    primary: false
---

## What happened

On 2 November 2026 four MIT CSAIL researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab) published "Sparks of Weight-Space Programming". They define the idea this way: "a general-purpose LLM reads and writes a network's weights directly (i.e., not through an optimizer, and in particular not with gradient descent)." The model they use is GPT-6 Astra. The post does not say how they accessed it, and calls the work "very early results."

## Key details

- **Reading weights:** Astra was shown the weights of four small networks (17,253 weights each) trained with PPO on Breakout, Pong, Pac-Man and Freeway. The authors say it "was still able to name the right game for all four networks." On a 7.16-million-weight transformer it named the right language for all three test cases and found "every copying head (induction head)."
- **Writing weights, no training:** on MinAtar Breakout the authors report scores of 15.8 and 25.3 for PPO trained 100 million and 500 million steps, against 517.4 for a network Astra wrote from scratch; Astra "beat PPO trained for 100 million steps in all three games." On Seaquest, Astra scored 53.1 against 88.9 for 500-million-step PPO.
- **Editing an existing model:** changing 0.016% of the weights (131,072) of Qwen3.5-0.8B, the post reports MATH-500 rose from 7.9% to 48.1%, GSM8K from 13.8% to 67.1% and IFEval from 21.0% to 62.3%. The rate of answers hitting the token limit fell from 93% to 33%.
- **Limits the authors state:** for Gemma 3 270M, "Astra could not improve it" (MATH-500 from 6.8 to at most 7.7). Detecting a sycophantic model from weights alone failed, though attention patterns worked. In the authors' words, "Editing weights could remove an obstacle that hid an ability, but it could not add an ability the model lacked." They add that the results are limited "due to inefficiencies in context length and harnesses."
- **Not stated:** a license, peer review, or an independent replication on the page. Newsletters we read on 3 November point to a reproduction attempt and to a skeptical response on social media; we have not verified either.

## Why it matters

If it holds up, the claim is that a general-purpose model can act as a tool for inspecting and patching other models, instead of using a training run. The Qwen result is large, but it is one small model, and the authors' own Gemma control shows it does not transfer automatically. The mechanism the authors suggest, removing something that was hiding an existing ability rather than adding a new one, is a narrower claim than "AI improves AI."

For practitioners the point is cost and access: the edits touch a tiny fraction of weights, but they were produced by a frontier model, so this is not something a small team can repeat without access to Astra. Treat the numbers as the authors' own until others reproduce them.

> Disclosure: Claude is made by Anthropic and is one of the AI tools Deyron Labs uses to research and draft articles. This article mentions OpenAI, not Anthropic, so there is no conflict of interest to declare; all statements are the authors' own, read on 4 November 2026.
