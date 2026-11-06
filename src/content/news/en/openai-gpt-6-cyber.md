---
title: "OpenAI introduces GPT-6 Cyber, a security model with access limited to approved customers"
summary: "On 5 November 2026 OpenAI announced GPT-6 Cyber, a model it says is trained to find and validate exploitable software vulnerabilities while staying inside limits set by the researcher. OpenAI reports 48.5% on its ExploitGym test, up from 32.1% for GPT-5.6 Cyber, and says it helped find 81 high-severity Firefox flaws. Access is initially limited to approved Daybreak Red customers. All figures are OpenAI's own."
seoTitle: "OpenAI GPT-6 Cyber: ExploitGym 48.5%"
seoDescription: "OpenAI announced GPT-6 Cyber on 5 November 2026 and reports 48.5% on ExploitGym; access is limited to approved customers. Figures are OpenAI's."
lang: en
publishedAt: 2026-11-06T20:25:00Z
entities:
  - OpenAI
  - GPT-6 Cyber
  - Mozilla
  - Firefox
  - Dragos
topics:
  - Models
  - Security
  - Enterprise
translationKey: openai-gpt-6-cyber
image: /images/news/openai-gpt-6-cyber-2026-11-05.jpg
imageAlt: "Deyron Labs graphic: OpenAI introduces GPT-6 Cyber; OpenAI reports 48.5% on ExploitGym; access limited to approved customers; figures are OpenAI's"
video: https://www.youtube.com/shorts/DkfIt9SgW5A
sources:
  - title: "GPT-6 Cyber: Advancing the frontier of aligned cybersecurity agents"
    url: "https://openai.com/index/introducing-gpt-6-cyber/"
    publisher: "OpenAI"
    primary: true
  - title: "A thousand fewer paths to root"
    url: "https://openai.com/index/a-thousand-fewer-paths-to-root/"
    publisher: "OpenAI"
    primary: true
---

## What happened

On 5 November 2026 OpenAI published "GPT-6 Cyber," describing it as a cybersecurity model "trained to find and validate exploitable vulnerabilities, respecting the boundaries set by researchers." It is the successor to GPT-5.6 Cyber. OpenAI classifies the model as "Critical" for cybersecurity under its Preparedness Framework, up from "High" for GPT-5.6 Cyber, and links a system card for full results. We read the page in its Romanian version on openai.com; quotations are OpenAI's text as translated by OpenAI.

## Key details

- **ExploitGym:** OpenAI reports 48.5% for GPT-6 Cyber against 32.1% for GPT-5.6 Cyber, which it calls a 51% relative improvement. The test checks whether a model can exploit a specified vulnerability on a remote target.
- **Staying in scope:** in a separate alignment test, ExploitGym Honeypot, OpenAI says the model avoided exploiting out-of-scope services in 99.93% of runs without its deployment safety prompt and 100% with it, against 94.49% for GPT-5.6 Cyber.
- **New benchmarks:** OpenAI introduces RemoteExploitBench, built on known vulnerabilities in applications such as GitLab, PostgreSQL and Jenkins in a controlled environment. It says GPT-6 Cyber completed 95% of tasks, while GPT-6 Astra used with Daybreak Blue declined 100%. On a new web penetration-testing evaluation it reports 40.3% against 32.0% for GPT-6 Astra.
- **Real-world work:** OpenAI says its researchers used the model to identify 81 high-severity, previously unknown Firefox vulnerabilities, which Mozilla classified as high severity, and that Mozilla has released fixes for many of them. It also says the model developed working exploits for 948 Linux kernel privilege-escalation vulnerabilities; details are in a separate OpenAI research post, summarised in our companion article.
- **Access:** GPT-6 Cyber is available at first through the API and Codex to a limited group of approved Daybreak Red customers. OpenAI says it will expand access to all Daybreak Red customers "soon" and make GPT-5.6 Cyber available to all of them. OpenAI also describes a US$1 billion Daybreak grant program for front-line defenders and a new Daybreak Red tier for approved critical-infrastructure defenders.
- **Safeguards:** OpenAI lists cyber-specific misalignment monitoring, targeted monitoring of emerging threats, private processing for safety, IP allow-lists for the Daybreak Red API, and extra checks that block help with attacks on industrial control and safety-critical systems. It recommends sandboxing and human oversight for high-risk workflows.
- **Partner evaluation:** OpenAI says Dragos ran evaluations in a controlled lab; the page quotes Dragos's AI director and links a Dragos report that we did not open.

## Why it matters

For security teams, this is a sign that frontier labs are shipping models aimed at vulnerability research with gated access rather than general release. The concrete effect for most readers is indirect: more vulnerabilities in widely used software, such as browsers and the Linux kernel, may be found and patched faster, and the same capabilities raise the bar for defence-in-depth.

Caveats: every benchmark figure comes from OpenAI's own evaluations and we found no independent evaluation. The page gives no price. It does not say when access widens beyond approved customers. OpenAI omits technical details of new exploitation techniques "for safety reasons," so those claims cannot be checked from the public page.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. All figures are OpenAI's unless stated otherwise.
