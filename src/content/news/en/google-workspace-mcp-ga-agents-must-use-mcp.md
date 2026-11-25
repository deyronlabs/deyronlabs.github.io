---
title: "Google makes Workspace MCP servers generally available; AI agents must use MCP, not REST, from 1 February 2027"
summary: "Google announced general availability of Workspace MCP servers and a Workspace CLI, plus standardized usage tiers. AI agents must use MCP rather than calling Workspace REST APIs directly, with technical enforcement starting 1 February 2027. Over 99% of active developers are in the free Standard tier, Google says."
seoTitle: "Google Workspace MCP generally available"
seoDescription: "Google made Workspace MCP servers generally available on 24 Nov 2026; AI agents must use MCP from 1 Feb 2027, with usage billing from 1 Apr 2027."
lang: en
publishedAt: 2026-11-25T08:26:00Z
entities:
  - Google
  - Google Workspace
  - Model Context Protocol
topics:
  - Agents
  - Policy
image: /images/news/google-workspace-mcp-ga-agents-must-use-mcp.jpg
imageAlt: "Deyron Labs graphic: Google Workspace MCP servers generally available, agents must use MCP from 1 Feb 2027, Scaled tier billing from 1 Apr 2027"
translationKey: google-workspace-mcp-ga-agents-must-use-mcp
sources:
  - title: "MCP servers and CLI generally available, with standardized usage tiers"
    url: "https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html"
    publisher: "Google Workspace Updates"
    primary: true
---

## What happened

On 24 November 2026 the Google Workspace Updates blog announced that Workspace MCP servers and the Workspace CLI are generally available to all Google Workspace customers and developers. The same post introduces standardized usage tiers, a new Workspace AI Tools Addendum and expanded admin controls for agents. We read the post on 25 November 2026.

## Key details

- **What is available:** Google-hosted MCP servers for Gmail, Drive, Docs, Sheets, Slides, Calendar, Chat and Tasks (Keep is "coming soon"), and a CLI for local environments with packaged agent skills.
- **Usage tiers (starting with Gmail, Drive and Calendar):** a Standard tier at no cost with published rate limits, and a Scaled tier with higher limits. From 1 April 2027 Scaled is billed only for API or MCP usage above daily free allowances. Google says over 99% of active developers are in the Standard tier, and projects that take no action may be limited to Standard rate limits.
- **MCP requirement:** AI agents must use MCP instead of calling Workspace REST APIs directly; technical enforcement starts on 1 February 2027.
- **Terms and controls:** the Addendum restricts long-term storage of certain API-derived data and scraping of Workspace APIs. Admins get controls under Security > API Controls, human-in-the-loop confirmations, automatic DLP and audit logging. Rollout to Rapid Release and Scheduled Release domains takes about two weeks.
- **Other:** Workspace APIs are excluded from the Google Cloud Support variable fee calculation until at least December 2027, and Google says changes come with at least 90 days' notice. More granular agent policies are promised over the coming months.

## Why it matters

Developers who build agents against Gmail, Drive or Calendar have until 1 February 2027 to move from direct REST calls to MCP, and heavy users should check whether they fall into the billed Scaled tier from April. For admins, the new controls give a central place to govern agent access. Google's tier and "99%" figures are its own, so the real cost impact will only be visible once billing starts.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Google is not affiliated with Deyron Labs.
