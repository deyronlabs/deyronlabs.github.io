---
title: "Ai2 releases HiRO-ACEv2, an AI climate emulator that generates global 3 km data at about 1/300th the cost"
summary: "On 14 October 2026 the Allen Institute for AI (Ai2) released HiRO-ACEv2, which pairs its 100 km ACE climate model with a new downscaling model to produce global 3 km data. Ai2 says it costs about 1/300th as much as the X-SHiELD simulation it was trained on; the post names no license."
seoTitle: "Ai2 HiRO-ACEv2: 3 km AI climate, ~1/300 cost"
seoDescription: "Ai2's HiRO-ACEv2 downscales its ACE climate emulator to 3 km global data. Ai2 reports about 1/300th the cost of X-SHiELD; limits and open questions inside."
lang: en
publishedAt: 2026-10-15T06:00:00Z
entities:
  - Allen Institute for AI
  - Ai2
  - HiRO-ACEv2
  - ACE
  - X-SHiELD
  - Hugging Face
topics:
  - Research
  - Open-weight
  - Climate
translationKey: ai2-hiro-acev2-3km-climate-emulator
image: /images/news/ai2-hiro-acev2-3km-climate-emulator-2026-10-15.jpg
imageAlt: "Deyron Labs graphic: Ai2 HiRO-ACEv2 produces global 3 km climate data at about 1/300th the cost of X-SHiELD; figures are Ai2's own"
sources:
  - title: "HiRO-ACEv2: Simulating extreme weather at 3 km resolution for a fraction of the cost"
    url: "https://huggingface.co/blog/allenai/hiro-acev2"
    publisher: "Allen Institute for AI (Hugging Face blog)"
    primary: true
  - title: "Ai2 blog: HiRO-ACEv2"
    url: "https://allenai.org/blog/hiro-acev2"
    publisher: "Allen Institute for AI"
    primary: true
---

## What happened

On 14 October 2026, the Allen Institute for AI (Ai2) published "HiRO-ACEv2: Simulating extreme weather at 3 km resolution for a fraction of the cost". HiRO-ACEv2 is an update to Ai2's High Resolution Output ACE climate emulator. It pairs ACE, an AI climate model that runs at about 100 km resolution, with HiRO, a downscaling model that turns those coarse outputs into 3 km data. The new part is HiROv2, which predicts several high-resolution fields instead of only rainfall.

## Key details

All figures below are Ai2's own, taken from its post.

- **Cost:** Ai2 says HiRO-ACEv2 can generate global 3 km climate data at about 1/300th the cost of X-SHiELD, the physics-based simulation HiRO was trained on. For a single region, Ai2 says the saving can be larger, depending on the area.
- **Accuracy:** when given coarsened X-SHiELD data, Ai2 says HiROv2 matches the target simulation's high-resolution statistics to within 3%, including for events that occur about once in a million data points.
- **Scale:** Ai2 says it generated a full year of global 3 km data, and ran a 10-year simulation in which total hurricane energy is comparable to X-SHiELD's.
- **Limits stated by Ai2:** HiRO only works with the version of ACE tuned to match X-SHiELD, and it cannot yet produce data for other climates, such as a warmer future, or for historical datasets such as ERA5. Winds and pressure around hurricane eyes are somewhat more lopsided than in X-SHiELD. A faster version, which Ai2 says could be more than 10 times quicker, is in progress and not released.
- **Availability:** the models are listed for download on Hugging Face (allenai/HiRO-ACEv2), with tutorial notebooks and a web demo. The post does not state a license, and the compute hardware and run time behind the cost claim are not given.

## Why it matters

High-resolution climate data is expensive to produce with physics-based models, which limits how many scenarios researchers can run. If Ai2's cost and accuracy claims hold up outside its own tests, groups studying extreme rain, wind and storms could generate far more simulations for the same budget.

Two caveats apply. The accuracy figures come from Ai2's evaluation against the simulation the model learned from, so they say how well HiRO imitates X-SHiELD, not how well it matches the real atmosphere. The missing license also leaves commercial and downstream use unclear until the model card is checked.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claims and results are Ai2's own.
