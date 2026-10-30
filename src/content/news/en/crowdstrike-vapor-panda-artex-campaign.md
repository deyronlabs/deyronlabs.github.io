---
title: "CrowdStrike says a China-nexus group ran the ARTEX AI agent framework, mostly on DeepSeek, against 200+ organizations"
summary: "CrowdStrike reports that an adversary it tracks as VAPOR PANDA used the open-source ARTEX agent framework against more than 200 organizations in at least 14 countries over 11 days from 17 October 2026. It says the framework ran mainly on DeepSeek's model. The findings are CrowdStrike's own and not independently verified."
seoTitle: "CrowdStrike: VAPOR PANDA used ARTEX AI agents"
seoDescription: "CrowdStrike says VAPOR PANDA ran the ARTEX AI agent framework against 200+ organizations in 14 countries from 17 October 2026, mainly on DeepSeek."
lang: en
publishedAt: 2026-10-30T07:30:00Z
entities:
  - CrowdStrike
  - VAPOR PANDA
  - ARTEX
  - DeepSeek
  - BLOODALCHEMY
topics:
  - Security
  - Agents
translationKey: crowdstrike-vapor-panda-artex-campaign
image: /images/news/crowdstrike-vapor-panda-artex-campaign-2026-10-30.jpg
imageAlt: "Deyron Labs graphic: CrowdStrike on VAPOR PANDA and ARTEX; 200+ organizations, 14+ countries, 11 days, 9 confirmed intrusions"
sources:
  - title: "VAPOR PANDA uses ARTEX to scale global campaign"
    url: "https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/"
    publisher: "CrowdStrike Counter Adversary Operations"
    primary: true
  - title: "Storm-0940 uses ARTEX agentic AI in ConnectWise supply chain compromise"
    url: "https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/"
    publisher: "Microsoft Security"
---

## What happened

On 29 October 2026, CrowdStrike's Counter Adversary Operations team published a report on an adversary it tracks as VAPOR PANDA, which it describes as China-nexus. CrowdStrike says the group used ARTEX, an open-source multi-agent penetration-testing framework, to run a global campaign that began on 17 October. These are CrowdStrike's findings from its own telemetry, and this article has not seen independent confirmation of the attribution.

CrowdStrike says ARTEX ran "primarily with the Chinese-origin DeepSeek LLM", together with a second subscription-based commercial model that CrowdStrike says it "could not confirm". Microsoft described the use of ARTEX by a different actor, Storm-0940, in an analysis of 21 October that we covered separately.

## Key details

- **Scale (CrowdStrike's figures):** more than 200 distinct organizations were targeted, in at least 14 countries, over an 11-day window.
- **Outcomes:** CrowdStrike confirmed post-exploitation activity at nine organizations and password spraying against at least 12 more.
- **AI usage:** in one intrusion, the planning agents "consumed on the order of 1.4 billion input tokens", according to CrowdStrike.
- **Operator instructions:** CrowdStrike says the operator's instructions to the agents were written in Chinese and labeled 【人类指令】 ("human instruction"). One instruction told the agents to "find Windows machines in the domain without Falcon", CrowdStrike's own security sensor.
- **Malware:** the campaign used the BLOODALCHEMY backdoor, which CrowdStrike notes was first publicly documented in October 2023 and which Microsoft and Elastic have written about. The report lists three file hashes and six command-and-control indicators (three domains and three IP addresses).
- **Outlook:** CrowdStrike assesses that China-nexus adversaries "will highly likely continue adopting agentic frameworks such as ARTEX over the next 12 months".
- **What the report does not establish:** the summary we read does not say that DeepSeek took part in or knew of the campaign; it describes DeepSeek's model as the one the framework ran on.

## Why it matters

For defenders, the report is a vendor account of AI agents handling much of the routine work in intrusions across many targets at once, which raises the value of the basics: strong authentication, password-spray detection and monitoring of unusual agent-like activity. The indicators CrowdStrike published can be checked against logs directly.

It also shows that widely available open and hosted models can be pointed at offensive tasks by anyone with access. How much of the activity was carried out by the agents rather than by human operators is CrowdStrike's assessment, and other security vendors have not yet confirmed it.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. All figures and attributions are CrowdStrike's unless stated otherwise.
