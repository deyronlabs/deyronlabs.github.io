---
title: "Microsoft unveils seven MAI models at Ignite 2026 and a licensed-weights program for its own Azure"
summary: "On 17 November 2026 Microsoft AI announced seven new MAI models at Ignite, covering cyber, coding, image, realtime voice and decision tasks, and said licensed weights are coming through its Frontier Company engagements. All performance and price comparisons are Microsoft's own."
seoTitle: "Microsoft MAI Ignite 2026: seven new models"
seoDescription: "Microsoft AI announced seven MAI models at Ignite on 17 Nov 2026, from Code 2 to Cyber 2 Flash; benchmark and price claims are Microsoft's own."
lang: en
publishedAt: 2026-11-18T06:40:00Z
updatedAt: 2026-11-18T09:40:00Z
entities:
  - Microsoft AI
  - MAI Code 2
  - MAI Code 2 Flash
  - MAI Cyber 2 Flash
  - MAI Image 2.7
  - MAI Realtime 1
  - Microsoft Foundry
  - GitHub Copilot
topics:
  - Models
  - Coding
  - Pricing
translationKey: microsoft-ignite-mai-seven-models
image: /images/news/microsoft-ignite-mai-seven-models-2026-11-18.jpg
imageAlt: "Deyron Labs graphic: Microsoft Ignite 2026, seven new MAI models; MAI Code 2 at 98% of GPT-6.1 Sol coding performance at about 40% of the price, per Microsoft; MAI Cyber 2 Flash 92.3% on CyberGym-E2E; Microsoft's own comparisons"
sources:
  - title: "Seven new world class models at scalable price-performance"
    url: "https://microsoft.ai/news/microsoft-ignite-2026/"
    publisher: "Microsoft AI, 17 November 2026"
    primary: true
  - title: "MAI Licensed Weights: Frontier performance you control"
    url: "https://microsoft.ai/news/introducing-mai-licensed-weights/"
    publisher: "Microsoft AI, 17 November 2026"
    primary: true
  - title: "MAI Code 2 and Code 2 Flash: Everyday coding at scalable prices"
    url: "https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/"
    publisher: "Microsoft AI, 17 November 2026"
    primary: true
  - title: "MAI Cyber 2 Flash: Leading security. Lower cost"
    url: "https://microsoft.ai/news/introducing-mai-cyber-2-flash/"
    publisher: "Microsoft AI, 17 November 2026"
    primary: true
  - title: "Introducing MAI Image 2.7"
    url: "https://microsoft.ai/news/introducing-mai-image-2-7/"
    publisher: "Microsoft AI, 17 November 2026"
    primary: true
  - title: "Introducing MAI Realtime 1"
    url: "https://microsoft.ai/news/introducing-mai-realtime-1/"
    publisher: "Microsoft AI, 17 November 2026"
    primary: true
---

## What happened

On 17 November 2026, at its Ignite conference, Microsoft AI published an announcement titled "Seven new world class models at scalable price-performance", with separate pages for MAI Code 2 and Code 2 Flash, MAI Cyber 2 Flash and a licensed-weights program. Every benchmark and price comparison below is Microsoft's own claim; none has been independently reproduced.

## Key details

- **MAI Code 2:** Microsoft says it reaches 98% of GPT-6.1 Sol's coding performance at about 40% of the price, and 96% of Claude Opus 5.5 at 5% of the price. MAI Code 2 Flash is described as comparable to GPT-6 Luna at 65% of the price, and to Haiku 5.5 at 20% of the price. Prices on the Code 2 page are shown at a "50% promotional price".
- **Where Code 2 runs:** both Code 2 models are in GitHub Copilot; Code 2 Flash is in limited-access preview in Microsoft Foundry. Microsoft lists OpenRouter, Vercel, Hermes, OpenCode and Kilo as "soon".
- **MAI Cyber 2 Flash:** Microsoft reports 92.3% on CyberGym-E2E against 91.5% for GPT-6 Astra at half the reasoning budget, and says it excluded 92 of 905 tasks and reported results on 813. The page footnote lists $0.10 / $0.01 / $0.50 per million tokens for the model against $10 / $1 / $50 for GPT-6 Astra; the footnote does not label the three values. Context is one million tokens. It is offered only inside Microsoft security products, replacing the current model for eligible customers "starting mid-December".
- **MAI Image 2.7 and 2.7 Flash:** Microsoft says MAI Image 2.7 ranks first for image editing on Artificial Analysis, ahead of GPT Image 2.6 Sunburst at max setting, at one fifth of the cost, and that on Arena it is in the "top two labs" for both generation and editing. It is in public preview on Microsoft Foundry at about $35 per 1,000 images for Image 2.7 and about $10 per 1,000 for Flash. Microsoft also lists a Canvas in MAI Labs and transparent-background output, and says MAI Image is the default model in Bing Image Creator, with usage up about 15% a week, compounding, since June. We have not checked the Artificial Analysis ranking itself.
- **MAI Realtime 1:** Microsoft calls it its first speech-to-speech model, priced from $0.01 per minute of audio. It says the model beats GPT Realtime 2.1 on quality, speed and price, citing Big Bench Audio and Tau-Voice, and that it is compatible with the OpenAI Realtime API. Customers named are Agoda and Reservations.ai, and it is used in Dynamics 365 Contact Center and Dragon Copilot. In Foundry it is a limited-access preview that is not billed until public preview.
- **Decision 1.1:** described on the Ignite page as 50x faster and 79x cheaper than GPT-Sol 6.1. Its own page and the MAI keynote transcript were not read for this article, so that claim rests on the Ignite summary alone.
- **Licensed weights:** organizations will be able to deploy and customize MAI models in their own Azure environments. Microsoft says this is "coming soon through our Frontier Company engagements". Prices, license terms and download terms are not stated. Customer examples are Microsoft's: AT&T (1/50th of the cost versus GPT-6.1 Sol on standard tasks), Woven by Toyota (ready-to-merge fixes in 44% of cases) and Alaska Airlines (classification accuracy from 81.2% to 91.1%).
- **Inconsistent figures:** the Ignite page gives 64% preference over GPT-6 Sol in a frontend blind evaluation, while the Code 2 page gives 67%.
- **Not stated:** context sizes for most models, per-token prices outside the Cyber footnote and the Image and Realtime pages, and independent evaluations.

## Why it matters

For developers, the concrete change is two cheaper coding models inside GitHub Copilot and a security model that Microsoft prices far below a competing frontier model. Because the comparisons are Microsoft's own and the Code 2 prices are promotional, the real cost and quality gap will only be clear once outside tests appear. The licensed-weights program shows Microsoft positioning MAI models as something enterprises can run in their own Azure tenants, but it has no terms yet.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Microsoft is not affiliated with Deyron Labs; all claims about the models are Microsoft's own.
