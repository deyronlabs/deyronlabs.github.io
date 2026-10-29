---
title: "Microsoft opens the GitHub-built Copilot harness to developers through Foundry for multi-model agents"
summary: "On 28 October 2026 Microsoft said the multi-model harness built by GitHub engineers, which powers Copilot Code, Copilot Studio, the GitHub Copilot app and more, is available through Microsoft Foundry. Microsoft says it runs the agent loop and sandbox and supports more than 20 frontier models plus bring-your-own-key. No pricing was given."
seoTitle: "Microsoft Copilot harness now in Foundry"
seoDescription: "Microsoft said on 28 Oct 2026 that the GitHub-built Copilot harness is available via Foundry, supporting 20+ frontier models; no pricing given."
lang: en
publishedAt: 2026-10-29T17:30:00Z
entities:
  - "Microsoft"
  - "GitHub"
  - "Microsoft Foundry"
  - "Copilot harness"
  - "Copilot SDK"
topics:
  - Agents
  - Coding
  - Products
translationKey: microsoft-copilot-harness-foundry-multi-model-agents
image: /images/news/microsoft-copilot-harness-foundry-multi-model-agents-2026-10-29.jpg
imageAlt: "Deyron Labs graphic: Microsoft Copilot harness available through Foundry from 28 October 2026, supporting 20+ frontier models plus bring-your-own-key"
sources:
  - title: "Introducing the Microsoft Copilot harness: Unlocking the potential of truly multi-model agentic work"
    url: "https://blogs.microsoft.com/blog/2026/10/28/introducing-the-microsoft-copilot-harness-unlocking-the-potential-of-truly-multi-model-agentic-work/"
    publisher: "The Official Microsoft Blog (28 October 2026)"
    primary: true
---

## What happened

On 28 October 2026 Microsoft published a post by Tina Schuchman, corporate vice president for Foundry, and Vladimir Fedorov, GitHub's CTO, introducing the Microsoft Copilot harness. Microsoft says the multi-model harness created by GitHub's engineering team has been adopted company-wide and powers Copilot Code, Copilot Studio, the GitHub Copilot app, the CLI, VS Code and other products. It is now available to developers and enterprises through Microsoft Foundry.

## Key details

Details come from Microsoft's post, read on 29 October 2026.

- **Division of work:** "With the Copilot harness, Microsoft runs the agent loop and sandbox, with governance and optimization built in from day one. You bring the instructions, skills, tools, and model choice."
- **Models:** support for "20+ frontier models plus bring your own key".
- **Performance claim:** Microsoft says the runtime was ported to Rust, which it credits with lower session overhead and time-to-first-token. The post gives no figures.
- **SDK:** the post points to the Copilot SDK on GitHub.
- **Not stated:** pricing, plan details and a general-availability date.

## Why it matters

A harness is the layer that runs an agent's loop, tools and sandbox around whichever model is chosen. By exposing the one it uses internally, Microsoft is offering a managed alternative to building that layer from scratch and tying it to Foundry. The post does not say what it costs or how it differs in practice from running agents on a model provider's own tools, so those are the questions to check before depending on it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Details come from Microsoft's 28 October 2026 post, read on 29 October 2026.
