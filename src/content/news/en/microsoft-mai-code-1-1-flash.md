---
title: "Microsoft releases MAI-Code-1.1-Flash, a coding model it says costs a quarter of MAI-Code-1.0"
summary: "On 7 October 2026 Microsoft AI released MAI-Code-1.1-Flash, which it says costs a quarter of MAI-Code-1.0 and uses 25% fewer tokens per task. It is live in GitHub Copilot and can be downloaded to run locally, with more than 120 GB of RAM recommended. Microsoft gives no dollar price, license or download location, and all figures are its own."
lang: en
publishedAt: 2026-10-08T16:30:00Z
entities:
  - Microsoft AI
  - MAI-Code-1.1-Flash
  - MAI-Code-1.0
  - GitHub Copilot
  - Visual Studio Code
topics:
  - Models
  - Coding
translationKey: microsoft-mai-code-1-1-flash
image: /images/news/mai-code-1-1-flash-2026-10-07.jpg
imageAlt: "Deyron Labs graphic: Microsoft AI released MAI-Code-1.1-Flash, a coding model it says costs a quarter of MAI-Code-1.0 and can run locally"
sources:
  - title: "MAI-Code-1.1-Flash: better, faster, at a quarter of the cost"
    url: "https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/"
    publisher: "Microsoft AI"
    primary: true
---

## What happened

On 7 October 2026, Microsoft AI published "MAI-Code-1.1-Flash: better, faster, at a quarter of the cost". It describes an update to MAI-Code-1.0, the coding model Microsoft launched at Build in June. Microsoft says the new model is in production in GitHub Copilot now, and that it is "available to download and run locally".

## Key details

- **Cost:** Microsoft says the model costs "a quarter of the cost" of MAI-Code-1.0 and uses 25% fewer tokens per task. It gives no dollar prices. It also says local model calls carry zero inference charges.
- **Speed and quality, as reported by Microsoft:** tokens stream 25% faster in GitHub Copilot; a 22% improvement on Terminal-Bench 2.1 in GitHub Copilot CLI and 15% on .NET tasks, both against the previous version; in production use, code survival rose 4% and return visits rose 9%.
- **Local use:** Microsoft recommends devices with more than 120 GB of RAM. A 3-bit quantized version reduces memory needs and keeps a 256K context window, and Microsoft says it keeps coding performance comparable to the full-precision model on SWE-Bench Verified and Terminal-Bench 2.1.
- **Availability:** experimental access in the GitHub Copilot app, GitHub Copilot CLI and Visual Studio Code is expected by the end of October.
- **What the page does not say:** the license, where to download the model, its parameter count, whether it counts as open-weight, or any independent evaluation. We read the page on 8 October 2026.

## Why it matters

For people who use GitHub Copilot, the practical change is a cheaper and faster default model, if Microsoft's comparisons hold. Every performance figure compares the model to Microsoft's own earlier version or to its own production metrics, so they say little about how it ranks against models from other labs.

The local option is the part to watch. Running it as described needs more than 120 GB of RAM, which limits it to high-end machines. Until Microsoft names a license and a download location, it is not clear who can use the weights, or for what.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claims about the model are Microsoft's own unless stated otherwise.
