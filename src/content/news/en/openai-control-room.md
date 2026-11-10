---
title: "OpenAI describes Control Room, a system that can halt research model jobs within 35 seconds"
summary: "OpenAI published a description of Control Room on 9 November 2026, a central system that tracks model jobs on its research infrastructure and can stop them over safety or security concerns. OpenAI says output halts within 35 seconds of a decision to intervene and that the system fails closed. It is an internal research tool, not a product for users."
seoTitle: "OpenAI Control Room halts research jobs in 35s"
seoDescription: "OpenAI says its Control Room system, described on 9 November 2026, halts model output within 35 seconds and fails closed if monitoring goes down."
lang: en
publishedAt: 2026-11-10T09:00:00Z
entities:
  - OpenAI
  - Control Room
topics:
  - Safety
  - Research
translationKey: openai-control-room
image: /images/news/openai-control-room-2026-11-10.jpg
imageAlt: "Deyron Labs graphic: OpenAI Control Room, a system that halts research model output within 35 seconds and fails closed, described on 9 November 2026"
sources:
  - title: "Control Room"
    url: "https://openai.com/index/control-room/"
    publisher: "OpenAI"
    primary: true
---

## What happened

On 9 November 2026 OpenAI published a page describing Control Room, a central system that tracks the model jobs running on its research infrastructure and can stop them when safety or security problems appear. We read the OpenAI page on 10 November 2026. Everything below is OpenAI's own description; we have not seen an independent evaluation of how the system works in practice.

## Key details

- **What it is:** according to OpenAI, Control Room ties together the inference work done for research, including agentic sampling for training and evaluation and data processing. It works with OpenAI's monitoring systems for misalignment.
- **Speed:** OpenAI says the system "halts model output within 35 seconds" of a decision to intervene, to stop or pause a job. It attributes the delay to an authorization cache and says it is working to reduce it to zero.
- **Mechanism:** a job must carry a job ID, and the inference engine asks Control Room for permission on every request. If a job has been stopped, the request is refused. OpenAI says this is enforced at the inference layer, not in the job's own code.
- **Fails closed:** if Control Room goes down or is disabled, including by tampering, all inference requests are refused. OpenAI says fail-closed is already extended to all frontier research jobs and that the rest will follow within days.
- **Review requirement:** each research job that uses agentic inference must have an approved "safety case", and frontier reinforcement-learning jobs run with a monitor. OpenAI says a recent DNS incident was caught by a monitor.
- **Status:** OpenAI says Control Room is already deployed across its research infrastructure, and that the external serving stack used by customers is already more centralized, with the ability to roll back deployments quickly.
- **Not stated:** the page is not a product announcement, gives no figures on how many jobs have been stopped or how many incidents were caught, and does not detail the DNS incident.

## Why it matters

Labs run large numbers of automated agents and training jobs, and OpenAI's description shows one concrete design for stopping them: a permission check on every inference request that denies by default. The stated 35-second delay is a measurable gap that outsiders can track against OpenAI's goal of removing it. For people who use ChatGPT or the API, nothing changes today; the page is about internal research systems. Whether this design becomes common practice across labs, and whether independent reviewers get to test it, is not addressed in OpenAI's post.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Anthropic is a competitor of OpenAI, the subject of this story. All claims are OpenAI's own unless stated otherwise.
