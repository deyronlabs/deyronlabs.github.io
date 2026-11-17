---
title: "NVIDIA at SC26: Nemotron for Science, science agents and a Rubin HPC GPU expected in 2028"
summary: "At the SC26 supercomputing conference on 17 November 2026, NVIDIA announced Nemotron for Science, an open model, chemistry dataset and post-training recipes, plus agent results from Argonne and KTH and a science-focused Rubin GPU it expects in 2028. All results are NVIDIA's own."
seoTitle: "NVIDIA SC26: Nemotron for Science, Rubin HPC GPU"
seoDescription: "NVIDIA's SC26 keynote blog on 17 Nov 2026 covers Nemotron for Science, science agents and a Rubin HPC GPU with 50,000+ CUDA cores, expected 2028."
lang: en
publishedAt: 2026-11-17T18:30:00Z
entities:
  - NVIDIA
  - Nemotron for Science
  - Nemotron 3.5 Super VL
  - Rubin
  - DGX Spark
topics:
  - Hardware
  - Science
  - Open-weight
translationKey: nvidia-sc26-nemotron-for-science-rubin-hpc
image: /images/news/nvidia-sc26-nemotron-for-science-rubin-hpc-2026-11-17.jpg
imageAlt: "Deyron Labs graphic: NVIDIA at SC26; Nemotron for Science open model, dataset and recipes; Rubin HPC GPU expected in 2028; results are NVIDIA's own; NVIDIA blog, 17 November 2026"
sources:
  - title: "Ian Buck Kicks Off NVIDIA's Week at SC26 as Science Enters the Age of Agents"
    url: "https://blogs.nvidia.com/blog/ian-buck-sc26/"
    publisher: "NVIDIA Blog, 17 November 2026"
    primary: true
---

## What happened

On 17 November 2026 NVIDIA published a blog post on its SC26 announcements, written around Ian Buck's keynote. The post introduces Nemotron for Science, describes several science-agent results, and previews a science-focused Rubin GPU, among other items. The figures below are NVIDIA's, as stated in the post.

## Key details

- **Nemotron for Science:** combines the Nemotron 3.5 Super VL open model with a new open chemistry dataset and post-training recipes for life sciences and chemistry. NVIDIA says it runs locally on a DGX Spark, a workstation or a supercomputer.
- **Agent results (NVIDIA):** at Argonne, an agent built with the toolkit took one prompt, planned and tested hypotheses, and identified two new binding sites. A KTH agent that repairs broken GROMACS setups fixed 81% of test cases in one overnight run on a single DGX Spark.
- **Code porting:** NVIDIA says its Nsight AI Porting Agent ported a WRF model routine to GPUs for a speedup of "more than 5x", using about 150 million tokens.
- **Rubin HPC:** a science-focused GPU with "more than 50,000 CUDA cores", about 3x Hopper per the post, spanning FP64 to FP4, expected in 2028. DKRZ selected Vera CPUs for its HLRE-5 supercomputer, expected in early 2028.
- **Quantum:** NVIDIA says a CUDA-Q decoding algorithm cuts error-correction research computation from 12 weeks to 45 minutes, with a target of reducing decoding latency from about 300 microseconds to 10.
- **Photonics:** NVIDIA quotes Buck as saying co-packaged optics switches at Lambda are "15x more reliable on bit errors and link flaps".
- **Not stated:** prices, licence terms and availability dates for Nemotron for Science, and independent verification of any result.

## Why it matters

For researchers, the concrete items are an open model and dataset that can run on a single DGX Spark, and agent examples with measurable outcomes. Those outcomes come from NVIDIA and its partners and have not been independently reproduced, and the Rubin HPC GPU is a roadmap item for 2028 rather than a shipping product.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. NVIDIA is not affiliated with Deyron Labs; all claims are NVIDIA's own.
