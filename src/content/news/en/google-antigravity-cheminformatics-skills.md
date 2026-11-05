---
title: "Google DeepMind adds Cheminformatics Skills to Antigravity and offers 10,000 scientists a free six-month top usage tier"
summary: "On 3 November 2026 Google DeepMind published a suite of Cheminformatics Skills for its Antigravity workbench, built on RDKit with connectors to ChEMBL and PubChem. The skills are available now, and DeepMind is accepting applications for free top-tier usage for 10,000 scientists for six months. The post is a walkthrough, not a benchmark."
seoTitle: "Google Antigravity Cheminformatics Skills"
seoDescription: "Google DeepMind adds Cheminformatics Skills to Antigravity (3 Nov 2026) using RDKit, ChEMBL and PubChem, with free top usage for 10,000 scientists."
lang: en
publishedAt: 2026-11-05T06:30:00Z
entities:
  - Google DeepMind
  - Google Antigravity
  - Cheminformatics Skills
  - RDKit
  - ChEMBL
  - PubChem
topics:
  - Products
  - Research
  - Agents
translationKey: google-antigravity-cheminformatics-skills
image: /images/news/google-antigravity-cheminformatics-skills-2026-11-03.jpg
imageAlt: "Deyron Labs graphic: Google Antigravity Cheminformatics Skills, 3 November 2026, with free top usage tier for 10,000 scientists for 6 months"
sources:
  - title: "Agentic cheminformatics with Google Antigravity"
    url: "https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/"
    publisher: "Google DeepMind"
    primary: true
---

## What happened

On 3 November 2026 Google DeepMind published "Agentic cheminformatics with Google Antigravity". It describes a set of Cheminformatics Skills for Antigravity, which the post calls "a collaborative science workbench with full access to local tooling" for computational and bench chemists. According to DeepMind, the skills are available today.

## Key details

- **How it is split:** per DeepMind, the language model handles workflow orchestration, database navigation and scientific reasoning, while deterministic chemistry tools run the molecular calculations. The tools are grounded in RDKit, with connectors to the ChEMBL and PubChem databases.
- **What the skills cover:** literature and patent search with sourcing reports, filtering of buffers and solvents, an interactive viewer with scatter plots, matched molecular pair analysis, machine-learning potency models with chronological or scaffold splits, reaction tools (including curved-arrow diagrams and similar-reaction lookup), export to industry chemistry software, and hand-off to AlphaFold or molecular dynamics.
- **The demo:** DeepMind walks through crizotinib and lorlatinib, two lung-cancer kinase inhibitors; crizotinib has five major rotatable bonds, while lorlatinib is cyclized to zero. DeepMind says an agent searched thousands of compounds, ran matched molecular pair analysis and proposed novel rigidified macrocycles with synthetic routes "in just an hour". A dashboard shows 568 curated compounds, and the macrocycles were largely predicted to be brain-penetrant.
- **Access:** download the Antigravity app and install the Science plugin; enterprise users can sign in with Google Cloud credentials. DeepMind is offering "10,000 scientists the highest usage tier in Google Antigravity free of charge for 6 months", onboarded on a rolling basis and subject to eligibility, capacity and selection. Applications are open. No standard pricing is given.
- **Caveats in the post:** the potency model was benchmarked on four experimental read-outs with a scaffold split, but no metrics are reported. DeepMind writes that "computational designs are testable hypotheses, not finished drugs" and that every proposed design must be synthesized and validated experimentally. The post is inconsistent about which Gemini model ran the demo (screenshots show Gemini 3.8 Flash; one caption says Gemini 1.5 Flash).

## Why it matters

Chemistry is a clear test of the "model plus deterministic tools" pattern, where the model plans and checks while established software does the maths. For working chemists the practical news is the free access window. What the post does not show is independent validation: there are no reported accuracy numbers and no synthesized compounds, so the one-hour result is a demonstration of workflow speed, not of drug-design success.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Figures and claims are Google DeepMind's own, taken from its 3 November 2026 blog post.
