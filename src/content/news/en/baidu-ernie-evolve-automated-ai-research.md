---
title: "Baidu details ERNIE Evolve, an automated research system, and reports gains on public AI R&D benchmarks"
summary: "On 9 November 2026 Baidu published ERNIE Evolve, a multi-agent system that edits code and runs experiments to automate AI research. Baidu reports slight gains over the best public results on NanoChat and NanoGPT benchmarks and faster inference for ERNIE-5.5-Flash. The results are Baidu's own; the system itself is not released."
seoTitle: "Baidu ERNIE Evolve: automated AI research"
seoDescription: "Baidu's ERNIE Evolve, published 9 Nov 2026, automates AI R&D experiments; Baidu reports 0.8763 BPB on NanoChat versus 0.8878 for the best public result."
lang: en
publishedAt: 2026-11-09T07:20:00Z
entities:
  - Baidu
  - ERNIE Evolve
  - ERNIE-5.5-Flash
  - Kunlunxin P800
topics:
  - Research
  - China
translationKey: baidu-ernie-evolve-automated-ai-research
image: /images/news/baidu-ernie-evolve-automated-ai-research-2026-11-09.jpg
imageAlt: "Deyron Labs graphic: Baidu ERNIE Evolve reports 0.8763 validation BPB on NanoChat AutoResearch versus 0.8878 for the best public result, per Baidu"
sources:
  - title: "ERNIE Evolve: Toward Automated Research for Real-World AI R&D"
    url: "https://ernie.baidu.com/research/posts/ernie-evolve/"
    publisher: "Baidu ERNIE Team"
    primary: true
  - title: "ERNIE Evolve results (GitHub)"
    url: "https://github.com/ernie-research/ERNIE-Evolve-Results"
    publisher: "Baidu ERNIE Research"
---

## What happened

On 9 November 2026 Baidu's ERNIE team published a research post describing ERNIE Evolve, a system for automating AI research and development. It uses five roles (Director, Selector, Executor, Evaluator and Reviewer) in two nested loops, and modifies code and runs experiments in isolated environments.

## Key details

All figures below are reported by Baidu; we have not seen independent replication.

- **NanoChat AutoResearch (validation BPB, lower is better):** ERNIE Evolve 0.8763, versus 0.8878 for the best public result.
- **NanoGPT Speedrun Track 1 (time to target loss):** 38.9 seconds versus 39.9 for the best public result. **Track 3 (steps):** 2,590 versus 2,690.
- **SOL-ExecBench (mean SOL, higher is better):** ERNIE Evolve 0.819, slightly below the best public 0.827.
- **Production use, on pre-release ERNIE-5.5-Flash:** Baidu reports generation speed at 623.6% of baseline on Kunlunxin P800 chips over four rounds; on GPUs, deterministic inference throughput up 33.7%, time per output token down 26% and time to first token down 12% after about three days of research; peak decoding speed up 14.9% with accuracy unchanged.
- **Release status:** Baidu says the optimized results are open-sourced on GitHub. The post does not release the ERNIE Evolve system or state a license, and does not say the production changes to ERNIE-5.5-Flash are public.

## Why it matters

Automating the experiment loop of model training and inference tuning is a direction several labs are pursuing. Baidu's reported margins on public benchmarks are small, and one score is below the best public result, so the clearest claim is the production speedups, which are reported for an unreleased model and cannot be checked from outside.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article.
