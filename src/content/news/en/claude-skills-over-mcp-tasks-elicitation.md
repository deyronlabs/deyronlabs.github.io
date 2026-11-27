---
title: "Anthropic puts Skills over MCP in public beta for Claude, and makes MCP Tasks and Elicitation generally available"
summary: "In an article dated 24 November 2026, Anthropic said MCP servers can now ship skills to Claude and Claude Code in public beta, while MCP Tasks and Elicitation are generally available for Pro, Max and Ultra plans. File Uploads is 'rolling out soon'. Usage figures such as 700 million monthly SDK downloads are Anthropic's own."
seoTitle: "Claude: Skills over MCP beta, Tasks GA"
seoDescription: "Anthropic's 24 Nov 2026 post puts Skills over MCP in public beta in Claude and Claude Code; MCP Tasks and Elicitation are GA on Pro, Max and Ultra."
lang: en
publishedAt: 2026-11-27T10:00:00Z
entities:
  - Anthropic
  - Claude
  - Claude Code
  - Model Context Protocol
  - Agentic AI Foundation
topics:
  - Products
  - Agents
translationKey: claude-skills-over-mcp-tasks-elicitation
image: /images/news/claude-skills-over-mcp-tasks-elicitation.jpg
imageAlt: "Deyron Labs graphic: Anthropic, 24 Nov 2026: Skills over MCP in public beta; MCP Tasks and Elicitation generally available on Pro, Max and Ultra; File Uploads rolling out soon; Anthropic is the source and the vendor"
sources:
  - title: "MCP servers can now ship skills, run tasks, and more with Claude"
    url: "https://claude.com/resources/articles/skills-over-mcp-tasks-and-more"
    publisher: "Anthropic (claude.com), 24 November 2026, read 26 November 2026"
    primary: true
---

## What happened

Anthropic published an article dated 24 November 2026, "MCP servers can now ship skills, run tasks, and more with Claude". It announces three changes for how Model Context Protocol (MCP) servers work with Claude and Claude Code. We read the article on 26 November 2026; everything below is Anthropic's description. (Some newsletters carried it on 26 November, but the page itself is dated 24 November.)

## Key details

- **Skills over MCP (public beta):** an MCP server can publish skills, meaning workflows and guidance, alongside its tools, in Claude and Claude Code. It is on by default for Pro, Max and Ultra plans, available on Team once an admin enables it, and "coming soon" for Enterprise. Anthropic names Shopify, HubSpot and Atlassian as examples, with Carta coming soon.
- **Tasks (generally available):** MCP Tasks, for longer-running work, are generally available in Claude and Claude Code on Pro, Max and Ultra and rolling out to Team and Enterprise. The example given is ZoomInfo.
- **Elicitation (generally available):** MCP Elicitation lets a server ask the user for input mid-task. It has the same availability as Tasks. Anthropic's examples are Supabase, Railway and GitHub.
- **File Uploads:** "rolling out soon" for Pro, Max, Ultra and eligible Team and Enterprise plans.
- **Anthropic's figures:** more than 700 million MCP SDK downloads a month, more than 10,000 connectors for Claude, and tool search that can cut context use by more than 85% in multi-server setups. We have not verified these.
- **Specification:** Anthropic says the features are defined in the open MCP specification, which is stewarded by the Agentic AI Foundation.

## Why it matters

Shipping skills through MCP means a service can hand Claude both the tools and the instructions for using them well, instead of users installing skills separately. Tasks and Elicitation address two common gaps in agent workflows: long-running jobs and mid-run questions to the user.

Note the staging: only Tasks and Elicitation are generally available, and mainly on consumer-tier plans. Skills over MCP is a beta, and Enterprise access is still pending.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and the features described are Anthropic's own. Deyron Labs is not affiliated with Anthropic.
