---
title: "OpenAI introduces MedChemBench, a 99-problem medicinal-chemistry benchmark; GPT-6.2 Astra scores 84.5%"
summary: "OpenAI released MedChemBench, a benchmark of 99 medicinal-chemistry problems drawn from 117 papers and patents. At its highest standard reasoning setting GPT-6.2 Astra scores 84.5%, with structure reconstruction near 95% but compound selection and numerical prediction only about half credit. OpenAI says the results do not show models can discover new drugs."
seoTitle: "OpenAI MedChemBench: GPT-6.2 Astra scores 84.5%"
seoDescription: "OpenAI's MedChemBench tests 99 medicinal-chemistry problems; GPT-6.2 Astra scored 84.5% at xhigh, a result OpenAI reports about its own models."
lang: en
publishedAt: 2026-11-21T15:55:00Z
entities:
  - OpenAI
  - MedChemBench
  - GPT-6.2 Astra
topics:
  - Research
  - Models
  - Science
translationKey: openai-medchembench-benchmark
image: /images/news/openai-medchembench-benchmark-2026-11-21.jpg
imageAlt: "Deyron Labs graphic: OpenAI MedChemBench, 99 problems, GPT-6.2 Astra 84.5% at xhigh; structure reconstruction about 95%, compound selection about half credit"
sources:
  - title: "Introducing MedChemBench (read 21 November 2026)"
    url: "https://openai.com/index/introducing-medchembench"
    publisher: "OpenAI, listed in its news feed on 20 November 2026"
    primary: true
---

## What happened

OpenAI published "Introducing MedChemBench" (listed in its news feed on 20 November 2026), a benchmark of AI reasoning on medicinal-chemistry tasks. The fetched page shows no publication date; the date here comes from OpenAI's feed. All scores below are OpenAI's own.

## Key details

- **Contents:** 99 problems from 117 papers and patents, covering 761 distinct molecular structures, across structure reconstruction, explaining evidence, ranking and selecting compounds, and predicting properties.
- **Scores:** eleven GPT models were tested at several reasoning settings. At the "xhigh" setting OpenAI lists GPT-6.2 Astra at 84.5%, GPT-6 Astra at 83.3%, GPT-6.1 Sol at 82.0%, GPT-6.1 Terra at 75.1% and GPT-5.6 Sol at 58.2%. At maximum effort GPT-6 Astra reached 83.8%.
- **By task:** structure reconstruction was about 95.4% at xhigh, while compound selection and numerical prediction earned only about half credit. The page's body text gives some figures without naming the model version.
- **Example:** OpenAI says GPT-6 Astra rebuilt an 18-atom ring correctly in all ten responses, while GPT-5.6 Sol produced a 15-atom ring.
- **Caveats stated by OpenAI:** each response was a single attempt with no tools or feedback, and prior exposure to the source papers cannot be ruled out. The page says the results "do not establish whether models can discover new drugs". A preprint is mentioned but no link is given.

## Why it matters

The split is the useful part: models handle reconstructing a structure well but are much weaker at the judgment tasks, such as choosing between compounds, that medicinal chemists spend their time on. That is a narrower claim than "AI can design drugs".

Because OpenAI wrote the benchmark and ran it on its own models, and the questions may overlap with training data, treat the headline score as a measure of this test rather than of lab performance.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic competes with OpenAI. Details come from OpenAI's page, read on 21 November 2026.
