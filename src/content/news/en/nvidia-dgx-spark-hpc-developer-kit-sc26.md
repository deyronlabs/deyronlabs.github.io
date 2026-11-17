---
title: "NVIDIA introduces DGX Spark HPC Developer Kit, a four-node desktop cluster with 512GB of memory, at SC26"
summary: "At SC26 on 16 November 2026 NVIDIA introduced the DGX Spark HPC Developer Kit, four DGX Spark systems linked in a switchless ring. NVIDIA says the cluster has 512GB of combined memory and can run models of up to 700B parameters with NVFP4. It is sold through OEM partners and NVIDIA Marketplace; no price is given."
seoTitle: "NVIDIA DGX Spark HPC Developer Kit at SC26"
seoDescription: "NVIDIA unveiled the DGX Spark HPC Developer Kit at SC26 on 16 Nov 2026: four GB10 nodes, 512GB memory, models up to 700B parameters."
lang: en
publishedAt: 2026-11-17T08:07:00Z
entities:
  - NVIDIA
  - DGX Spark
  - GB10 Grace Blackwell Superchip
  - SC26
topics:
  - Hardware
translationKey: nvidia-dgx-spark-hpc-developer-kit-sc26
image: /images/news/nvidia-dgx-spark-hpc-developer-kit-sc26-2026-11-17.jpg
imageAlt: "Deyron Labs graphic: NVIDIA DGX Spark HPC Developer Kit; four nodes; 512GB combined memory; 20TB NVMe; models up to 700B parameters with NVFP4; NVIDIA blog, 16 November 2026"
sources:
  - title: "NVIDIA DGX Spark Developer Kit Turns a Desk Into a Supercomputing Lab"
    url: "https://blogs.nvidia.com/blog/dgx-spark-hpc-developer-kit-sc26/"
    publisher: "NVIDIA Blog, 16 November 2026"
    primary: true
---

## What happened

On 16 November 2026, at the SC26 supercomputing conference in Chicago, NVIDIA introduced the DGX Spark HPC Developer Kit. The NVIDIA blog post describes it as a four-node cluster of DGX Spark systems, each built on the GB10 Grace Blackwell Superchip. The post says the kit is on display at SC26 and "available for sale".

## Key details

- **Topology:** each node connects directly to its two ring neighbours over ConnectX-7 networking, with no switch.
- **Capacity:** NVIDIA lists 512GB of combined memory and 20TB of NVMe storage across the four nodes.
- **Model size:** with NVFP4, NVIDIA says models of up to 700B parameters can run locally across the four nodes, giving DeepSeek V4.1 as an example.
- **Where to buy:** through OEM partners Acer, ASUS, Dell Technologies, GIGABYTE, H3C, HP, Lenovo, MSI and xFusion, and through NVIDIA Marketplace.
- **Customer examples cited by NVIDIA:** Kvantify (quantum-circuit simulation of up to 70 qubits and 975 gates on one Spark), the Rubin Lab at UC Berkeley (results 15x sooner than an 11-hour cluster queue) and Hartwig Group (LoRA fine-tuning of Nemotron 3 Super 120B-A12B on one device).
- **Not stated:** price, exact bundle contents, a licence and a date for the NVIDIA HPC SDK playbook, which the post says is "coming soon".

## Why it matters

The kit packages several small Grace Blackwell machines into a desk-side cluster aimed at HPC developers who want to test multi-node code without queueing for a shared system, and at people who want to run very large open models locally.

Memory and capacity figures are NVIDIA's and depend on NVFP4 quantization, so real throughput for a 700B-parameter model has not been shown in the post. Without a price, it is not yet possible to compare the kit with renting cloud GPUs.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. NVIDIA is not affiliated with Deyron Labs; all claims are NVIDIA's own.
