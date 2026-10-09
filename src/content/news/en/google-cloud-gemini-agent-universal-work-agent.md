---
title: "Google Cloud introduces the Gemini agent, a universal agent for enterprise work, with identity, audit and spend controls"
summary: "On 8 October 2026 Google Cloud announced the Gemini agent at its Gemini at Work event. Google describes a single agent and API for knowledge work, media creation and coding that runs in the cloud, uses Gemini and Claude models, and carries per-agent identity, audit trails and spend caps. The post gives no price or general availability date."
seoTitle: "Google Cloud launches the Gemini agent for work"
seoDescription: "Google Cloud's Gemini agent, announced 8 October 2026, handles knowledge work and coding with per-agent identity and spend caps. No price or GA date."
lang: en
publishedAt: 2026-10-09T16:40:00Z
entities:
  - Google Cloud
  - Gemini agent
  - Gemini Enterprise
  - Google Workspace
  - Anthropic
  - Claude
topics:
  - Agents
  - Products
  - Security
translationKey: google-cloud-gemini-agent-universal-work-agent
image: /images/news/google-gemini-agent-universal-work-agent-2026-10-09.jpg
imageAlt: "Deyron Labs graphic: Google Cloud launches the Gemini agent for enterprise work, with per-agent identity, audit trail, sandbox and spend caps; no price or general availability date given; features are Google's own"
sources:
  - title: "Gemini at Work 2026: Introducing Gemini agent"
    url: "https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026"
    publisher: "Google Cloud"
    primary: true
  - title: "Google Cloud introduces the Gemini agent"
    url: "https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-at-work/"
    publisher: "Google"
    primary: true
---

## What happened

On 8 October 2026, in a keynote by Thomas Kurian of Google Cloud at the Gemini at Work 2026 event, Google Cloud introduced the Gemini agent. Google calls it "a universal agent for work": one agent, also available as an API, that plans the work, uses skills and tools, connects to a company's business systems, and picks the best model for each job.

Google's announcement does not say whether the Gemini agent is in preview or generally available, and it lists no price or plan tiers. The only status it gives is for industry add-ons: Gemini for Financial Services and for Legal are "now in preview", and Government, Healthcare and Retail are "coming soon".

## Key details

- **What it does:** answers questions, does knowledge work, creates media and writes code. Google says it works across Workspace apps (Gmail, Drive, Docs, Sheets, Slides, Chat, Calendar) and can be reached from the web, iOS and Android, Windows and Mac, a command line, Microsoft 365 or Slack, or run headless.
- **Runs in the cloud:** Google says work "that takes hours or days keeps running after you close your laptop".
- **Multi-agent:** the agent can create temporary sub-agents, and "coworker agents" get their own email addresses on a company domain. Memory comes in four kinds: session, semantic, procedural and episodic.
- **Model choice:** Google says the agent can use Gemini and Claude models "today", with other models planned. It routes each workload to the model it expects to give the best result at the lowest cost.
- **Governance:** each agent gets its own cryptographically attested identity with least-privilege, role-based permissions. Every action goes to an audit trail attributed to the agent rather than to a person. Agents run in a sandbox with their own network boundary, and traffic passes through what Google calls Agent Gateway, "an AI network firewall enforcing your organization's policies in real time".
- **Cost controls:** per-project spend caps in the Cloud Billing Console. When a cap is hit, the project's agent pauses and can be resumed "with a single click".
- **Customer figures:** Google cites, among others, "nearly 90% of the Fortune 100" using Gemini Enterprise and SOMPO running "over 10,000 custom AI agents". These are Google's own figures from a marketing post and are not independently verified.

## Why it matters

Most companies that try AI agents hit the same questions: who is this agent, what can it touch, who pays when it runs for days, and how do we audit it? Google's answer is to treat each agent like an employee account, with an identity, permissions, a log and a budget. If it works as described, that lowers the barrier for security teams to say yes. Nothing in the post shows how well the agent does the work itself.

Two things are missing for now: when and for whom the agent is available, and what it costs beyond the spend caps. Until Google publishes them, treat the announcement as a statement of direction rather than a product you can buy today. The mention of Claude models also shows that large cloud platforms are offering rival models side by side in the same agent.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic's Claude models are named in Google's announcement. Deyron Labs is independent of Anthropic and Google. Feature and customer claims are Google's own.
