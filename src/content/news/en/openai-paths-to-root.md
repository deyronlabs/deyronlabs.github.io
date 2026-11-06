---
title: "OpenAI describes an autonomous workflow that produced 948 Linux privilege-escalation exploits"
summary: "On 4 November 2026 OpenAI published research on an agent workflow that scanned the Linux kernel, reproduced 1,724 vulnerabilities and produced 948 distinct local privilege-escalation exploits, at a reported API cost of about US$1.2 million. OpenAI says it sent hundreds of reports and patches to maintainers. All figures are OpenAI's own."
seoTitle: "OpenAI: 948 Linux privilege-escalation exploits"
seoDescription: "OpenAI says an autonomous workflow produced 948 Linux kernel privilege-escalation exploits for about US$1.2 million in API credits; figures are OpenAI's."
lang: en
publishedAt: 2026-11-06T20:25:00Z
entities:
  - OpenAI
  - Linux kernel
  - Patch the Planet
topics:
  - Research
  - Security
translationKey: openai-paths-to-root
image: /images/news/openai-paths-to-root-2026-11-04.jpg
imageAlt: "Deyron Labs graphic: OpenAI says an autonomous workflow produced 948 Linux kernel privilege-escalation exploits for about US$1.2 million in API credits; figures are OpenAI's"
sources:
  - title: "A thousand fewer paths to root"
    url: "https://openai.com/index/a-thousand-fewer-paths-to-root/"
    publisher: "OpenAI"
    primary: true
  - title: "GPT-6 Cyber: Advancing the frontier of aligned cybersecurity agents"
    url: "https://openai.com/index/introducing-gpt-6-cyber/"
    publisher: "OpenAI"
    primary: true
---

## What happened

On 4 November 2026 OpenAI published "A thousand fewer paths to root," a research write-up of an autonomous workflow for finding, validating and patching vulnerabilities in the Linux kernel, run in a controlled research environment on a recent kernel at mid-October 2026. OpenAI says the workflow used a not-yet-released cyber model; the next day it announced GPT-6 Cyber and cited the same 948 figure. We read the page in its Romanian version on openai.com.

## Key details

- **Funnel (OpenAI's numbers):** 5,034 audit targets (about 2.8 million lines, roughly 7% of the kernel); 2,308 potential vulnerabilities; 1,724 reproduced (about 74.7%); 291 information-disclosure proofs of concept; 948 distinct local privilege-escalation (LPE) exploits for a widely used Linux distribution, with human researchers reviewing results before reporting.
- **Cost:** OpenAI reports US$1,213,430 in API credits for the run, or US$1,279 per LPE exploit, and says that is an upper bound.
- **Comparison:** in July 2026 GPT-5.6 Sol found and exploited 166 distinct LPE vulnerabilities for US$513,690, according to OpenAI; it says the newer run found "over 5 times" more.
- **kernelCTF:** on a hardened Google kernelCTF target OpenAI reports 25 information-disclosure proofs and 21 LPE exploits for about US$32,936, with one protection removed because the kernel version was incompatible with it.
- **Maintainer response:** after 10 days, OpenAI says 61 of the LPE issues had been fixed upstream, 43 had patches in progress and 299 were being discussed publicly. It says it sent hundreds of reports and patches and is working with Patch the Planet partners on the rest.
- **Limits it reports:** in an early run, 20 of 200 apparent successes obtained root through a different zero-day than the one assigned, so OpenAI added an independent check. OpenAI says it omitted technical details of ten new exploitation techniques for safety.

## Why it matters

OpenAI's conclusion is that rescanning code with each new model generation can surface bugs earlier models missed, and that automated patch generation matters as fast as discovery does. For users, its practical advice is to keep software updated, because fixes are landing quickly.

Caveats: all results are OpenAI's own, from one run on one target configuration, and the model is not named on this page. The ranges comparing costs with past bug-bounty payouts are OpenAI's hypothetical calculations, not rewards earned.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. All figures are OpenAI's unless stated otherwise.
