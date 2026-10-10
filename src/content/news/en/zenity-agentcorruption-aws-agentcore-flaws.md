---
title: "Zenity discloses AgentCorruption, a chain of flaws in AWS AgentCore that let one agent reach others in the same account"
summary: "On 8 October 2026 security firm Zenity Labs described a chain of flaws in AWS AgentCore: a public-facing agent with an outbound-request tool could fetch machine credentials and, through an overprivileged default role, reach other agents in the same AWS account and region. Zenity says it reported the issue to AWS on 25 December 2025 and that AWS has since tightened the defaults."
seoTitle: "Zenity AgentCorruption flaws in AWS AgentCore"
seoDescription: "Zenity Labs says a flaw chain in AWS AgentCore let one agent reach others in the same account; AWS made IMDSv2 the default and cut role permissions."
lang: en
publishedAt: 2026-10-10T07:00:00Z
entities:
  - Zenity Labs
  - AWS
  - AWS AgentCore
topics:
  - Security
  - Agents
translationKey: zenity-agentcorruption-aws-agentcore-flaws
image: /images/news/zenity-agentcorruption-aws-agentcore-flaws-2026-10-08.jpg
imageAlt: "Deyron Labs graphic: Zenity Labs says its AgentCorruption flaw chain let one AWS AgentCore agent reach others in the same account; AWS made IMDSv2 the default and reduced default role permissions; account is Zenity's own"
sources:
  - title: "Zenity Labs discloses AgentCorruption, a chain of AWS AgentCore flaws"
    url: "https://zenity.io/press-release/zenity-labs-discloses-agentcorruption-a-chain-of-aws-agentcore-flaws"
    publisher: "Zenity"
    primary: true
---

## What happened

On 8 October 2026 Zenity Labs, the research group of security company Zenity, announced research it calls AgentCorruption, a chain of flaws in AWS AgentCore, Amazon's service for running AI agents. Zenity presented it at SecTor 2026 in Toronto. Zenity says it reported the flaws to AWS on 25 December 2025.

This article relies on Zenity's own press release. We did not find an AWS advisory, a CVE identifier or a statement from AWS about the research, so the description and the fix status below are Zenity's.

## Key details

Everything below is Zenity's account unless stated otherwise.

- **Instance metadata access:** a public-facing agent that had a common outbound-request tool could reach the instance metadata service and retrieve credentials for its underlying machine.
- **Overprivileged default role:** the credentials came with a default execution role whose permissions extended beyond that one agent to all AgentCore agents in the same AWS account and region.
- **What that allowed:** Zenity says its researchers could list and invoke every agent in the account and region, including internal ones; read private conversations and long-term memories; download agent container images and source code; and retrieve credentials from AWS Secrets Manager and environment variables.
- **Persistence:** Zenity says it planted malicious memories that redirected later conversations to a destination the attacker controlled.
- **Scope:** Zenity says the underlying problems were systemic to AgentCore and affected any agent equipped with built-in tooling. The release does not give affected versions.
- **Fixes:** Zenity says AWS made IMDSv2, the more locked-down version of the metadata service, the default for AgentCore deployments, and reduced the default execution role so that agents can no longer invoke other agents, read private conversations or reach Secrets Manager secrets. Zenity says its testing confirmed the reduced permissions. The release does not say every existing deployment is fixed.

## Why it matters

The chain shows how a flaw in one exposed agent can become access to many when agents in an account share default permissions. For anyone running agents on a cloud platform, the practical points are to give each agent only the permissions it needs, to be cautious with tools that make outbound requests, and to check what the platform's default roles allow.

Because this is a researcher's disclosure without an AWS statement, it is worth checking AWS documentation for the current defaults before drawing conclusions about a specific deployment.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Claims about the flaws and the fixes are Zenity's own.
