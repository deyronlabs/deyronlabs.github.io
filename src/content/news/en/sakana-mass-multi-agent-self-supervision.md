---
title: "Sakana AI and UC Berkeley publish MASS, a method that lets one model improve itself through teams of its own agents"
summary: "On 8 October 2026 researchers from Sakana AI and UC Berkeley posted a paper on Multi-Agent Self-Supervision (MASS). Using Qwen3.6-27B, the authors report 1.2–1.6x higher performance per output token after two cycles on four open-ended benchmarks, with weaker transfer to software-engineering tests."
seoTitle: "Sakana MASS: one model improves via agent teams"
seoDescription: "Sakana AI and UC Berkeley's MASS paper reports 1.2–1.6x better score per output token on a 27B model; coding-test transfer was weaker."
lang: en
publishedAt: 2026-10-12T06:30:00Z
entities:
  - Sakana AI
  - UC Berkeley
  - MASS
  - Qwen3.6-27B
  - arXiv
topics:
  - Research
  - Agents
  - Japan
translationKey: sakana-mass-multi-agent-self-supervision
image: /images/news/sakana-mass-multi-agent-self-supervision-2026-10-12.jpg
imageAlt: "Deyron Labs graphic: Sakana AI and UC Berkeley's MASS paper reports 1.2 to 1.6 times better score per output token on a 27B model; results are the authors' own"
sources:
  - title: "Recursive Self-Improvement through Multi-Agent Self-Supervision (arXiv:2610.12176)"
    url: "https://arxiv.org/abs/2610.12176"
    publisher: "arXiv (Lee, Xu, Seely, Lee, Sojoudi, Zaharia, Tang)"
    primary: true
  - title: "MASS: Multi-Agent Self-Supervision (project page)"
    url: "https://pub.sakana.ai/mass/"
    publisher: "Sakana AI"
    primary: true
---

## What happened

On 8 October 2026, a team from UC Berkeley and Sakana AI posted a 39-page paper, "Recursive Self-Improvement through Multi-Agent Self-Supervision", on arXiv. Sakana AI, a Tokyo-based lab, published a project page for the method, called **MASS** (Multi-Agent Self-Supervision). The authors are Hyunin Lee, Jinglue Xu, Jeffrey Seely, Donghyun Lee, Somayeh Sojoudi, Matei Zaharia and Yujin Tang; Xu, Seely and Tang are listed with Sakana AI.

The paper addresses tasks with no automatic way to check the answer, such as open-ended research. In MASS, one base model plays three roles: it solves the task, proposes better multi-agent workflows (which agents exist and how they pass information), and judges the results. The best-judged team's runs are then used to fine-tune the same model, and the cycle repeats.

## Key details

All figures below are the authors' own; this is a preprint and we found no independent replication.

- **Setup:** the base model is Qwen3.6-27B, run in the `qwen-code` coding-agent environment and fine-tuned with LoRA. GPT-5.5 and Claude Opus 4.8 served as withheld external judges to measure progress; GPT-5.5 also wrote the task descriptions.
- **Main result:** after two MASS cycles, "score per output token" reached 1.2–1.6x the base model's level across four benchmarks (MLR-Bench, DSBench, ScienceAgentBench and AstaBench). The 1.6x figure is MLR-Bench alone. On the authors' synthetic test tasks, the win rate against the base model rose from 53.9% after round one to 69.9% after round two.
- **Training efficiency:** the abstract says a student model trained on multi-agent traces outperformed a single-agent student trained on 1.4x more tokens.
- **Limits stated by the authors:** transfer was uneven (0.96x on Terminal-Bench 2.0 and 0.94x on SWE-bench Verified); the training suite is only 12 synthetic tasks, three held out for testing; workflow search is noisy; and some comparisons are described as not fully fair, since team runs generate about 2.4x as many tokens. They also flag that a loop in which one model judges itself can reinforce shared blind spots, which they call a safety concern.
- **Code and weights:** the project page links a code repository. We did not find a statement about releasing model weights.

## Why it matters

Self-improvement methods usually need a task that can be scored automatically, such as a unit test. MASS tries to extend the idea to open-ended work, where the model has to grade itself. The reported gains come on research-style benchmarks, and the authors' own results show no improvement, and slight declines, on the two software-engineering tests they tried.

For readers who use AI tools, this is a research result, not a product: nothing here changes what an assistant can do today. It is worth tracking because the authors themselves name the main risk, that a model judging its own work can lock in its own mistakes.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic's Claude Opus 4.8 is one of the external judge models named in the paper. Results are the authors' own.
