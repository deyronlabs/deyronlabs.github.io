---
title: "NVIDIA presents GR00T 2, a robot world action model, and Isaac Lab 3.0 at CoRL, with results it reports itself"
summary: "At the CoRL robotics conference in Austin, NVIDIA presented GR00T 2, which it calls an open frontier world action model for robots, and Isaac Lab 3.0, its open-source robot learning framework. The success rates and speedups come from NVIDIA, as relayed by The Robot Report; the license and weights location were not stated in the sources read."
seoTitle: "NVIDIA GR00T 2 robot model and Isaac Lab 3.0"
seoDescription: "NVIDIA unveiled GR00T 2 and Isaac Lab 3.0 at CoRL on 9 Nov 2026; it reports 71% success with one demo per task and up to 2.5x faster training."
lang: en
publishedAt: 2026-11-13T19:00:00Z
entities:
  - NVIDIA
  - GR00T 2
  - Isaac Lab 3.0
  - Isaac Lab-Arena
  - DexBench
  - CoRL
topics:
  - Models
  - Research
  - Hardware
translationKey: nvidia-gr00t-2-isaac-lab-3
image: /images/news/nvidia-gr00t-2-isaac-lab-3-2026-11-09.jpg
imageAlt: "Deyron Labs graphic: NVIDIA GR00T 2 finished 40 of 50 tasks at least once, 71% success with one demo and 95% with five, and Isaac Lab 3.0 reports up to 2.5x throughput; figures are NVIDIA's"
sources:
  - title: "NVIDIA Newsroom listing, including 'Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation' (9 November 2026)"
    url: "https://nvidianews.nvidia.com/news"
    publisher: "NVIDIA"
    primary: true
  - title: "NVIDIA launches GR00T 2 and Isaac Lab 3.0 at CoRL"
    url: "https://www.therobotreport.com/nvidia-launches-gr00t-2-isaac-lab-3-0-corl/"
    publisher: "The Robot Report, 9 November 2026"
    primary: false
---

## What happened

At the CoRL robotics conference in Austin, NVIDIA presented GR00T 2, which it describes as an open frontier world action model for robots, together with Isaac Lab 3.0, an open-source robot learning framework. The presentation dates from 9 November 2026; NVIDIA's newsroom lists a release from that day titled "Practice Makes Precise". Our description of the details comes from The Robot Report's coverage of the launch. We did not open NVIDIA's release or research pages, so everything below is attributed to NVIDIA as relayed by The Robot Report.

## Key details

- **GR00T 2 results (NVIDIA's figures):** the model completed 40 of 50 evaluated tasks at least once without task-specific demonstrations. With one demonstration per task, average success across the 50 tasks was 71%; with five demonstrations it was 95%.
- **Data:** NVIDIA says GR00T 2 draws on 100,000 hours of open-source egocentric data.
- **Rankings (NVIDIA's claim):** NVIDIA says the model ranks in the top three on the RoboCasa365, RoboLab, RoboDojo and MolmoSpaces benchmarks. We have not seen an independent evaluation.
- **Isaac Lab 3.0:** with the Newton physics engine, it reportedly reaches up to 2.5x the throughput of Isaac Lab 2.3 on PhysX, in a visual dexterity benchmark. NVIDIA also cited an AlphaNIST result of over 98% training success versus 81%, using about 39 times less GPU time.
- **Also announced:** Isaac Lab-Arena 0.4 (developer preview) and two benchmarks, DexBench (with RLWRLD) and VABAR (with UC Berkeley).
- **Not stated in the sources we read:** the license of the GR00T 2 weights, where to download them, the model size and any pricing.

## Why it matters

A robot policy that works from one demonstration per task, if the 71% figure holds up, would cut the data collection that slows robotics projects. For now these are NVIDIA's own results on benchmarks it helped design, and the weights' license and availability are unconfirmed. Teams considering GR00T 2 should check the license and the repository before planning around it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. NVIDIA is not affiliated with Deyron Labs; all performance claims are NVIDIA's own.
