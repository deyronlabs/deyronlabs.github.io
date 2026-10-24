---
title: "Microsoft says a China-aligned group used the open-source ARTEX AI framework in a ConnectWise supply-chain attack"
summary: "Microsoft's threat intelligence team assesses that the actor Storm-0940 used ARTEX, an open-source multi-agent penetration-testing framework, to automate attacks on hundreds of organizations, including the ConnectWise supply-chain compromise. Microsoft says its own products were not compromised and publishes mitigation steps."
seoTitle: "Storm-0940 used ARTEX AI in ConnectWise attack"
seoDescription: "Microsoft assesses Storm-0940 used the agentic AI framework ARTEX against hundreds of organizations in a ConnectWise attack (post of 21 October 2026)."
lang: en
publishedAt: 2026-10-24T06:10:00Z
entities:
  - Microsoft
  - Storm-0940
  - ARTEX
  - ConnectWise
topics:
  - Security
  - Agents
translationKey: microsoft-storm-0940-artex-connectwise
image: /images/news/microsoft-storm-0940-artex-connectwise-2026-10-24.jpg
imageAlt: "Deyron Labs graphic: Microsoft on Storm-0940 and ARTEX; hundreds of organizations targeted, 327 accounts sprayed in one campaign, privileged cloud access in some cases within 3 hours"
sources:
  - title: "Storm-0940 uses ARTEX agentic AI in ConnectWise supply chain compromise"
    url: "https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/"
    publisher: "Microsoft Security"
    primary: true
---

## What happened

On 21 October 2026 Microsoft Security Research and Microsoft Threat Intelligence published an analysis of a threat actor it tracks as Storm-0940. Microsoft describes it as China-state aligned and active since 2021, and says it used ARTEX, an open-source agentic AI penetration-testing framework, to automate attacks on hundreds of organizations worldwide. Microsoft assesses that Storm-0940 was responsible for the compromise of a multi-tenant ConnectWise application; ConnectWise's own advisory followed on 16 October, according to Microsoft. These are Microsoft's assessments, and this article has not seen independent confirmation of the attribution.

## Key details

- **What ARTEX is:** Microsoft describes it as a multi-agent LLM system that runs autonomous penetration tests from reconnaissance through data exfiltration, and notes that threat actors in several regions use it.
- **What was automated, per Microsoft:** scanning and reconnaissance, password spraying, and OAuth application abuse using stolen application credentials, which allowed sign-ins without an interactive user. In some environments the activity continued with Microsoft Graph reconnaissance, changes to application credentials for persistence, attempts to change identities, groups or privileged roles, and bulk Azure Key Vault secret reads.
- **Scale (Microsoft's figures):** targeting of hundreds of organizations in sectors including defense, finance, government and energy. One password-spraying campaign on 10-14 October hit 327 accounts at eight organizations and produced more than 151,000 failed logons, peaking at about 2,900 failures per minute on 11 October. Microsoft says no successful authentication was observed in that campaign. After the ConnectWise compromise, sign-in attempts reached more than 2,250 tenants.
- **Impact:** Microsoft says most targeting was unsuccessful, but some attacks gave the actor privileged access to victims' cloud infrastructure, in some cases within 3 hours of initial targeting. It says the activity did not result from a compromise of, or vulnerability in, Microsoft's own systems or products.
- **Guidance:** keep affected ConnectWise app connections disabled until ConnectWise issues restoration instructions; preserve configuration and logs before deleting anything; inventory the four affected application IDs in every tenant; review sign-ins and audit records from at least 15 October; check for unusual credential additions, new service principals, role assignments and Conditional Access changes; and rotate credentials where suspicious activity is confirmed. Microsoft's post lists detections, hunting queries and indicators of compromise.

## Why it matters

The report is a vendor account of an AI agent framework being used to speed up routine intrusion steps against many targets at once, which makes multi-tenant app permissions and application credentials a practical priority for administrators. The attribution and figures are Microsoft's, and this article has not established how much of the activity was carried out by the AI agents rather than by human operators.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Details come from Microsoft's post of 21 October 2026, read on 24 October 2026.
