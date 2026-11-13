---
title: "Anthropic opens self-hosted Claude Managed Agents in private beta, running agents inside the customer's own environment"
summary: "On 12 November 2026 Anthropic said self-hosted Claude Managed Agents is in private beta. Customers run the agent harness, sandboxes, credentials and session history in their own cloud or on-premise environment. Access is through Anthropic account teams, and the post gives no pricing."
seoTitle: "Self-hosted Claude Managed Agents: private beta"
seoDescription: "Anthropic put self-hosted Claude Managed Agents into private beta on 12 Nov 2026, so agents run inside the customer's own environment."
lang: en
publishedAt: 2026-11-13T18:00:00Z
entities:
  - Anthropic
  - Claude
  - Claude Managed Agents
  - Claude Platform
  - Amazon Bedrock
  - Microsoft Foundry
topics:
  - Agents
  - Products
  - Security
translationKey: claude-self-hosted-managed-agents
image: /images/news/claude-self-hosted-managed-agents-2026-11-12.jpg
imageAlt: "Deyron Labs graphic: Anthropic announced self-hosted Claude Managed Agents in private beta on 12 November 2026; agents, sandboxes, credentials and session history run in the customer's environment; access via account team"
sources:
  - title: "Operate Claude Managed Agents inside your security perimeter"
    url: "https://claude.com/resources/articles/self-hosted-claude-managed-agents"
    publisher: "Anthropic (Claude Platform), 12 November 2026"
    primary: true
---

## What happened

On 12 November 2026 Anthropic published "Operate Claude Managed Agents inside your security perimeter" and said self-hosted Claude Managed Agents is "now available in private beta." The post says developers can build agents that work in their company's code and internal systems and run them in their own environment.

Anthropic says access is by request: customers should "contact your Anthropic account team."

## Key details

All details are from Anthropic's post, read on 13 November 2026. We have not tested the product, and we did not open the linked documentation.

- **What runs where:** the customer's cloud or on-premise environment hosts the agent harness, sandboxes, credentials and session history. The customer operates the Managed Agents server, its database and the workers, and session history is stored in the customer's own database.
- **Model access:** requests to Claude can go to Anthropic directly, to Amazon Bedrock, to Google's Agent Platform, to Microsoft Foundry or through the customer's own gateway.
- **Data controls:** Anthropic says zero data retention applies to Claude requests as with any Messages API call, and that activity can be exported over OpenTelemetry.
- **Not stated:** the post gives no pricing, no regional availability and no date for general availability.

## Why it matters

The change is who operates the infrastructure: teams with strict data or network rules can keep agent execution, credentials and logs inside their own perimeter instead of using an Anthropic-hosted service. The trade-off is that the customer now runs and secures the server, database and workers.

Because it is a private beta behind an account team, most developers cannot try it yet, and the claims about security and data handling are Anthropic's own description.

> Disclosure: this article is about a product made by Anthropic, the maker of Claude, which was one of the AI tools used to research and draft it. Anthropic is a conflict of interest here; details are Anthropic's own, from its 12 November 2026 post.
