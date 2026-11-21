---
title: "OpenAI says new safeguards cut adversarial-distillation attack success on GPT-6.2 Astra from 54.0% to 0.2%"
summary: "OpenAI published a post on defenses against adversarial distillation, where an actor uses a frontier model's outputs to train a model without its safeguards. It reports attack success falling from 54.0% to 0.2% in its internal test and says it acts against thousands to tens of thousands of accounts weekly. The figures are OpenAI's own."
seoTitle: "OpenAI cuts distillation attack success to 0.2%"
seoDescription: "OpenAI's 20 Nov 2026 post says safeguards cut adversarial-distillation attack success on GPT-6.2 Astra from 54.0% to 0.2% in its internal test."
lang: en
publishedAt: 2026-11-21T15:30:00Z
entities:
  - OpenAI
  - GPT-6.2 Astra
  - GPT-6 Astra
  - Moonshot AI
  - DeepSeek
topics:
  - Safety
  - Security
  - Policy
translationKey: openai-combatting-adversarial-distillation
image: /images/news/openai-combatting-adversarial-distillation-2026-11-21.jpg
imageAlt: "Deyron Labs graphic: OpenAI reports adversarial-distillation attack success fell from 54.0% to 0.2% on GPT-6.2 Astra in its internal test"
sources:
  - title: "Combatting adversarial distillation (read 21 November 2026)"
    url: "https://openai.com/index/combatting-adversarial-distillation/"
    publisher: "OpenAI, listed in its news feed on 20 November 2026"
    primary: true
---

## What happened

OpenAI published "Combatting adversarial distillation" (listed in its news feed on 20 November 2026). It describes how the company is trying to stop actors from using a frontier model's outputs, without authorization, to train a model that lacks the original safeguards. The post focuses on protecting the model's reasoning traces.

The fetched page shows no publication date; the date here comes from OpenAI's feed. All figures below are OpenAI's own measurements.

## Key details

- **Internal test:** with strong automated red-teaming, OpenAI says average attack success "fell from 54.0% against GPT-6 Astra with its original safeguards to 0.2%" against GPT-6.2 Astra with updated safeguards. In an adaptive black-box test on GPT-6.2 Astra it reports success below 1% for each attack type. It says GPT-6 Astra is also receiving some of the same improvements.
- **Why reasoning matters:** in a cyber-distillation study, a student model trained on exact reasoning traces generally beat one trained on summaries after supervised fine-tuning. After a light reinforcement-learning round, the exact-trace student still scored higher at the largest inference budget, while the summary-trained student scored higher at lower budgets.
- **Defenses:** input classifiers; output classifiers that check assistant messages and tool-call arguments; and API controls. Protected reasoning is tied to the conversation that produced it, so encrypted reasoning from one conversation can no longer be moved into another, and older model families cannot read GPT-6.2 Astra and Sol's protected reasoning.
- **Enforcement:** OpenAI says its weekly actions against campaigns have ranged "from thousands to tens of thousands of accounts".
- **Attribution and policy:** OpenAI says it briefed Congress in February on DeepSeek distillation attempts and that its September report attributed a core part of one campaign to individuals associated with Moonshot AI (Kimi). It says it supports the Chip Security Act, the AI OVERWATCH Act and the MATCH Act. These are OpenAI's allegations and positions; the post links no technical report, and we did not find a response from either company.

## Why it matters

Distillation is how a lab's capabilities can be copied cheaply, and it can strip safety behavior in the copy. OpenAI is describing both a technical fix (tying reasoning to a conversation) and a policy push, so the post is as much a position statement as an engineering note.

The 54.0% to 0.2% result comes from OpenAI's own adaptive test and has not been reproduced by anyone else, and attackers adapt. For developers on OpenAI's API, the practical effect to watch is that reasoning handling and account enforcement are tightening.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic competes with OpenAI and has published its own distillation defenses. Details come from OpenAI's post, read on 21 November 2026.
