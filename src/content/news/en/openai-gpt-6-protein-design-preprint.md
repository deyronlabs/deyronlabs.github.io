---
title: "OpenAI preprint: GPT-6 models designed protein binders; 35 of 322 minibinders bound in lab tests"
summary: "OpenAI published a preprint claiming GPT-6-family models can design protein structures and sequences using reasoning and code alone. In wet-lab tests with partner Onava, 35 of 322 minibinders (10.9%) bound their targets. OpenAI says specialized models still filtered candidates, so end-to-end design is not yet shown."
seoTitle: "OpenAI GPT-6 protein design: 35 of 322 bound"
seoDescription: "OpenAI's 24 Nov 2026 preprint reports GPT-6 models designed protein binders; 35 of 322 minibinders bound in lab tests, with caveats on filtering."
lang: en
publishedAt: 2026-11-25T07:00:00Z
entities:
  - OpenAI
  - GPT-6
  - GPT-6.2
  - Onava
topics:
  - Research
  - Models
image: /images/news/openai-gpt-6-protein-design-preprint.jpg
imageAlt: "Deyron Labs graphic: OpenAI GPT-6 protein design preprint, 35 of 322 minibinders bound (10.9%), 70% of 182 redesigned VHHs bound IL-4R alpha"
translationKey: openai-gpt-6-protein-design-preprint
sources:
  - title: "GPT-6 models demonstrate intrinsic protein-design capabilities"
    url: "https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities"
    publisher: "OpenAI"
    primary: true
---

## What happened

On 24 November 2026 OpenAI published a page and linked preprint titled "GPT-6 as a Universal Foundation Model for Protein Biology: Beyond Specialized Models". OpenAI says GPT-6-family models (it names GPT-6.2, GPT-6, GPT-5.6 and an unnamed internal research model) can design protein structures and sequences using reasoning and code, without calling specialized biology models for the designs themselves. Laboratory tests were run with research partner Onava. We read the OpenAI page on 25 November 2026; we did not read the full PDF. All figures below are OpenAI's own and have not been independently reproduced.

## Key details

- **New minibinders (experiment 1):** 322 minibinders were tested against 5 targets and 35 (10.9%) bound. Hits by target: PD-L1 5, IL-7Rα 3, TrkA 1, VEGF-A 8, IL-17A 18. OpenAI notes that the original RFdiffusion study reported higher hit rates and that rates depend on filtering and how binding is defined.
- **New sequences for existing structures (experiment 2):** MDM2 75 of 88 (85%), VEGF-A 26 of 42 (62%), PD-1 8 of 59 (14%). Unpublished minibinder shapes: 14 of 107 (13.1%).
- **Antibodies:** 128 of 182 (70%) redesigned VHHs bound IL-4Rα; 179 of 272 (66%) redesigned fragments from five therapeutic antibodies bound PD-1 or PD-L1.
- **Computational benchmarks (OpenAI's numbers):** MotifBench, 30 challenges, 43.7% for the internal model versus 27.8% for RFdiffusion (preliminary); PoseBusters docking 93% (GPT-6.2) and 96% (internal model) versus 50% for DiffDock-L. Whole-protein structure prediction is much weaker: mean TM-score 0.26 for GPT-6.2 and 0.38 for the internal model, against 0.93 for ESMFold2.
- **Stated limits:** specialized models (SolubleMPNN, ProteinMPNN, Boltz-2, OpenDDE, ESMFold2, ESMFold) were used for sequences and for filtering candidates, so the work does not yet establish end-to-end zero-shot de novo minibinder design. Some inverse-folding results may reflect memorization. Binding is one step; specificity, stability and activity were not tested. OpenAI also notes biosecurity risk and references its Preparedness Framework.
- **Not stated:** availability, pricing or a release of the internal model.

## Why it matters

If the results hold up, general-purpose reasoning models could become a cheaper front end for protein engineering, but OpenAI's own caveats matter: filtering with specialized tools and the lack of independent replication mean this is a promising preprint, not a finished capability. The gap between strong docking scores and weak full-structure prediction shows where these models are still behind purpose-built tools. Watch for outside replication and for any release of the internal model.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. OpenAI is not affiliated with Deyron Labs.
