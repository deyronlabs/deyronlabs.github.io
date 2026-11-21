---
title: "Amazon says a Chinese-nexus actor's Cairn AI agents found and exploited a zero-day on their own"
summary: "Amazon Threat Intelligence reports that an open-source AI penetration-testing framework called Cairn, run by an actor it assesses as China-nexus with moderate confidence, went from mapping an API to a root shell on a medical-imaging AI application in about 11 minutes. Amazon assesses with high confidence that the flaw was a zero-day; maintainers have since shipped a fix."
seoTitle: "Cairn AI agents found a zero-day, Amazon says"
seoDescription: "Amazon's 20 Nov 2026 report says autonomous Cairn AI agents, run by a China-nexus actor, reached a root shell via a zero-day in about 11 minutes."
lang: en
publishedAt: 2026-11-21T15:55:00Z
entities:
  - Amazon Threat Intelligence
  - AWS
  - Cairn
  - MONAI Label
topics:
  - Security
  - Agents
  - China
translationKey: aws-cairn-ai-agents-found-zero-day
image: /images/news/aws-cairn-ai-agents-found-zero-day-2026-11-21.jpg
imageAlt: "Deyron Labs graphic: Amazon reports Cairn AI agents reached a root shell via a zero-day in about 11 minutes; actor assessed as China-nexus with moderate confidence"
sources:
  - title: "Chinese-nexus actor's Cairn AI agents found a zero-day on their own (read 21 November 2026)"
    url: "https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/"
    publisher: "AWS Security Blog, Amazon Threat Intelligence, 20 November 2026"
    primary: true
  - title: "GitHub Security Advisory GHSA-qc22-rmgc-vg94 (MONAI Label), linked from the AWS post"
    url: "https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94"
    publisher: "Project MONAI"
    primary: false
---

## What happened

On 20 November 2026 the AWS Security Blog published a report by Amazon Threat Intelligence, written by CJ Moses, describing a campaign in which autonomous AI agents found and exploited a previously unknown vulnerability. The agents were driven by Cairn, an open-source framework for autonomous penetration testing, given the simple goal "obtain shell access".

Amazon attributes the activity to a China-nexus actor with moderate confidence. This article reports Amazon's findings as Amazon's; we have not independently verified them.

## Key details

All details below are from the AWS post.

- **How it was found:** on 10 September 2026 Amazon found a publicly hosted Cairn instance running without authentication. The prompts were in Simplified Chinese and script timestamps used China Standard Time, which Amazon cites in its attribution.
- **Targets:** IP addresses linked to universities in East Asia outside mainland China, over about 48 hours starting 8 September 2026.
- **What failed:** a roughly 16-hour, 148-action operation against a Redis instance that allowed unauthenticated access did not succeed. A GPU-server operation of more than 6 hours built about 80 usernames and tested more than 30,000 credential combinations without finding a login.
- **What worked:** Amazon says the agents found a path-traversal flaw in the filename parameter of an upload endpoint in an open-source medical-imaging AI application, went from mapping the API to arbitrary file writes in about 11 minutes, then obtained a root reverse shell. Amazon assesses with high confidence that this was a zero-day.
- **Follow-on use:** the actor then gave the agents a proxy into a second university network running the same vulnerable software.
- **Response:** the maintainers released a fix and a GitHub Security Advisory (GHSA-qc22-rmgc-vg94). Amazon says affected organizations outside AWS were notified through a government partner.
- **Related report:** the post points to a separate Gambit Security report on a financially motivated actor using Cairn against online retailers.

## Why it matters

The concrete lesson from Amazon's account is speed and persistence: autonomous agents kept probing for hours, and the one path that worked took minutes once found. That compresses the time defenders have between a bug existing and it being exploited.

Two cautions apply. Attribution here is Amazon's assessment at moderate confidence, not a government finding. And the post describes one campaign against a handful of targets; it does not measure how common AI-driven zero-day discovery is. For teams running AI or medical-imaging tools, the practical steps are the ordinary ones the advisory points to: patch the affected software and keep agent and admin interfaces behind authentication.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Details come from Amazon's 20 November 2026 post, read on 21 November 2026.
