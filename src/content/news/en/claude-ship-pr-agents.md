---
title: "Anthropic launches Claude Ship: agents that review pull requests, fix them and approve changes your policy allows"
summary: "Anthropic launched Claude Ship on 23 November 2026, a set of agents that review pull requests, fix them and approve the ones a team's policy allows. Code Review is generally available; PR Steward and Claude Approvals are in beta for Team and Enterprise plans on GitHub."
seoTitle: "Claude Ship: Anthropic PR review agents"
seoDescription: "Anthropic launched Claude Ship on 23 Nov 2026: Code Review (GA) plus PR Steward and Claude Approvals (beta) for Team and Enterprise on GitHub."
lang: en
publishedAt: 2026-11-24T09:56:00Z
entities:
  - Anthropic
  - Claude Ship
  - Claude Code
  - GitHub
topics:
  - Products
  - Coding
  - Agents
translationKey: claude-ship-pr-agents
image: /images/news/claude-ship-pr-agents-2026-11-24.jpg
imageAlt: "Deyron Labs graphic: Anthropic launches Claude Ship on 23 Nov 2026; Code Review generally available, PR Steward and Claude Approvals in beta; Team and Enterprise plans, GitHub repositories"
sources:
  - title: "Introducing Claude Ship"
    url: "https://claude.com/resources/articles/introducing-claude-ship"
    publisher: "Claude (Anthropic), 23 November 2026"
    primary: true
  - title: "Claude Ship (documentation)"
    url: "https://code.claude.com/docs/en/claude-ship"
    publisher: "Claude Code Docs (Anthropic)"
    primary: true
  - title: "Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes"
    url: "https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/"
    publisher: "TechCrunch, 23 November 2026"
    primary: false
---

## What happened

On 23 November 2026 Anthropic introduced Claude Ship. In Anthropic's words, Claude can now review pull requests, fix them, and approve the ones that a team's policy allows. We read Anthropic's announcement and the Claude Ship documentation.

Claude Ship combines three agents: Code Review, which is generally available, and PR Steward and Claude Approvals, which are in beta. Developers start it by running `/ship` in Claude Code and in the desktop app.

## Key details

- **Availability (Anthropic):** Claude Team and Enterprise plans, for repositories on GitHub. It is not available to organizations with Zero Data Retention, a HIPAA configuration, or customer-managed encryption keys.
- **Setup (documentation):** configured under Organization settings > Claude Ship, which requires the Owner role.
- **Approvals and policy:** according to TechCrunch, approvals follow a policy file kept in the repository, written in natural language, and Anthropic suggests starting in observe-only mode. The documentation says Claude Approvals blocks merges only where an organization makes it a required check in GitHub, and normally not in observe mode.
- **Limits (documentation):** "Claude Ship uses AI and may miss bugs, security vulnerabilities, or other issues."
- **Credits:** Anthropic says eligible Claude Enterprise organizations can claim at least $10,000 in Claude Ship credits by 15 January 2027.
- **Not confirmed here:** accuracy or false-approval rates, pricing beyond the credits, and any independent evaluation. We did not find any in the pages we read.

## Why it matters

Reviewing and fixing pull requests is already common for AI coding tools; the notable step is letting an agent approve changes under a written policy. That moves a human sign-off from "every change" to "the changes the policy does not cover", which teams will need to weigh against the documented risk that the agent can miss bugs or vulnerabilities.

Starting in observe-only mode, as TechCrunch reports Anthropic suggests, lets a team compare the agent's decisions with its human reviewers before it can block or approve anything. Watch for independent measurements of how often approved changes later need fixes.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Claude Ship is an Anthropic product. Deyron Labs is not affiliated with Anthropic.
