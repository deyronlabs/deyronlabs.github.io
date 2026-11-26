---
title: "SenseTime releases SenseNova U1.6, open-sourcing an 8B image model with built-in self-correction"
summary: "SenseTime announced SenseNova U1.6 on 24 November 2026 and says it has open-sourced the weights of the series' 8B model, which checks its own first draft against the prompt and produces a corrected image. SenseTime reports about 10% better aesthetics than U1.5 Lite and 86.04 to 92.28 on a dense-infographic test; figures are SenseTime's own."
seoTitle: "SenseNova U1.6: 8B open image model"
seoDescription: "SenseTime open-sourced the 8B SenseNova U1.6 on 24 Nov 2026; it self-corrects drafts, and SenseTime reports 92.28 on UltraTextBench."
lang: en
publishedAt: 2026-11-26T07:00:00Z
entities:
  - SenseTime
  - SenseNova U1.6
  - SenseNova U1.5 Lite
  - UltraTextBench
  - ComfyUI
topics:
  - Models
  - Open-weight
  - Image generation
  - China
translationKey: sensetime-sensenova-u1-6-open-source-8b
image: /images/news/sensetime-sensenova-u1-6-open-source-8b.jpg
imageAlt: "Deyron Labs graphic: SenseTime's SenseNova U1.6, an open-sourced 8B image model with self-correction; SenseTime reports UltraTextBench 86.04 rising to 92.28 with self-correction"
sources:
  - title: "SenseNova U1.6 正式发布：美学进阶，字准意达 (SenseNova U1.6 officially released)"
    url: "https://www.sensetime.com/cn/news/sensenova-u1-6-open-source-20261124-1152"
    publisher: "SenseTime, 24 November 2026, read 26 November 2026 (Chinese; our translation)"
    primary: true
---

## What happened

SenseTime announced **SenseNova U1.6** on 24 November 2026 and said it has officially open-sourced the model weights of the series' 8B model. The announcement is in Chinese and the translations here are ours. The page does not state a license. It lists Hugging Face (Comfy-Org/SenseNova-U1), GitHub (OpenSenseNova/SenseNova-U1) and ModelScope, and says ComfyUI is supported.

## Key details

- **Self-correction:** after producing a first draft, the model checks it against the original prompt and generates a corrected version.
- **Reported results (SenseTime's internal evaluations):** about 10% higher aesthetics than U1.5 Lite in an internal user evaluation; on the UltraTextBench dense-infographic test, 86.04 for a single pass and 92.28 with self-correction, which SenseTime describes as a relative gain of about 7%.
- **API:** a SenseNova U1.6 Lite API is offered through the SenseNova Token Plan, free for a limited time to registered users. The page does not say whether the open 8B weights and the Lite API are the same model.
- **Not stated:** license, a full parameter breakdown beyond "8B", and any independent evaluation.

## Why it matters

An 8B open image model with text-heavy output and a self-check step is small enough for local ComfyUI workflows, which is the practical draw. Because the license is not on the announcement page, check the model card before using it commercially, and treat the benchmark figures as SenseTime's own until independent tests appear.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. SenseTime is not affiliated with Deyron Labs; all claims are SenseTime's own.
