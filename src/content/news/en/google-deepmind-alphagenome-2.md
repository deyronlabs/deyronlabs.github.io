---
title: "Google DeepMind releases AlphaGenome 2, a conditional DNA model, for non-commercial research use"
summary: "On 11 November 2026 Google DeepMind introduced AlphaGenome 2, which predicts one cell type or tissue condition at a time from a 1-million-letter DNA sequence. DeepMind says it finds nearly twice as many expression-changing variants as the prior best model. It is available through an API for non-commercial research, with a private preview for commercial research."
seoTitle: "AlphaGenome 2: DeepMind DNA model, research API"
seoDescription: "Google DeepMind introduced AlphaGenome 2 on 11 Nov 2026, with an API for non-commercial research. Performance figures are DeepMind's own."
lang: en
publishedAt: 2026-11-13T19:21:00Z
entities:
  - Google DeepMind
  - AlphaGenome 2
  - AlphaGenome
  - Google Antigravity
topics:
  - Research
  - Google
translationKey: google-deepmind-alphagenome-2
image: /images/news/google-deepmind-alphagenome-2-2026-11-11.jpg
imageAlt: "Deyron Labs graphic: Google DeepMind introduced AlphaGenome 2 on 11 November 2026; 1-million-letter DNA input, nearly twice as many expression-changing variants per DeepMind; research use only"
sources:
  - title: "AlphaGenome 2: Deciphering how cells read DNA to better understand disease"
    url: "https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/"
    publisher: "Google DeepMind (Gayoso, Latysheva, Kohli, Avsec; 11 November 2026)"
    primary: true
---

## What happened

On 11 November 2026 (15:00 UTC) Google DeepMind published "AlphaGenome 2: Deciphering how cells read DNA to better understand disease", by Adam Gayoso, Natasha Latysheva, Pushmeet Kohli and Žiga Avsec. It describes a second version of AlphaGenome, DeepMind's model for predicting how DNA sequence affects gene regulation.

Unlike the first version, which predicted many outputs in parallel, AlphaGenome 2 is conditional: it predicts one biological condition, such as a tissue, cell type or cell state, at a time, with that condition supplied at every stage.

## Key details

All figures are DeepMind's, from its post as read on 13 November 2026. We did not open the linked paper or run the model.

- **Inputs and outputs:** it takes a DNA sequence of one million letters, can use a cell encoder on a researcher's own single-cell data, adds DNA methylation as an output alongside earlier readouts, and can estimate unmeasured readouts from one measurement.
- **Training data:** the post cites more than 100 million single-cell profiles across 68 tissues. It also gives a figure of "over 107 million," and we could not reconcile the two wordings.
- **Results (DeepMind's evaluations):** DeepMind says it finds "nearly twice as many variants that change gene expression" as the previous state-of-the-art model. On the TenK10K dataset of 28 immune cell types it reports causal variants identified at 30% versus 16%, and directional gene effects at 43% versus 23%, compared with the original AlphaGenome fine-tuned on single-cell data and other specialized tools.
- **Access:** available now for non-commercial research through the AlphaGenome API, with a private preview for commercial research and interactive Colab tutorials. A feedback form is open until 30 November. DeepMind says "AlphaGenome 2 Skills" are coming to Google Antigravity "soon." The post names no licence and no price.
- **Limits:** the post says the model is for research use only and has not been validated or approved for clinical or diagnostic purposes.

## Why it matters

For genomics researchers, the practical change is a model that can be conditioned on a specific cell type or on their own single-cell data and is reachable through an API. The headline gains come from DeepMind's own benchmarks and comparisons, and independent replication was not available in the sources we checked.

Anyone considering it should note the use restriction: non-commercial research through the public API, commercial work only through a private preview, and no clinical use.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic competes with Google in AI. Figures are Google DeepMind's own, from its 11 November 2026 post.
