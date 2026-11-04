---
title: "Anthropic adds message threads in beta to the Messages API so agents send only new messages"
summary: "On 2 November 2026 Anthropic put message threads into beta on the Claude Messages API. The server keeps the conversation for a short time, so each later request sends only new messages. Anthropic says this gives a lower time to first token; its documentation gives no figures. A thread expires five minutes after its last request."
seoTitle: "Claude API message threads beta"
seoDescription: "Anthropic's message threads beta (2 Nov 2026) keeps a conversation on the server so API requests send only new messages; threads expire in 5 minutes."
lang: en
publishedAt: 2026-11-04T00:29:00Z
entities:
  - Anthropic
  - Claude API
  - Messages API
  - Claude Platform on AWS
  - Claude in Microsoft Foundry
topics:
  - Products
  - Coding
  - Agents
translationKey: anthropic-message-threads-beta-messages-api
image: /images/news/anthropic-message-threads-beta-messages-api-2026-11-02.jpg
imageAlt: "Deyron Labs graphic: Anthropic message threads beta, send only new messages, threads expire 5 minutes after last request and are deleted within 1 hour, not ZDR eligible"
sources:
  - title: "Claude Platform release notes (2 November 2026 entry)"
    url: "https://platform.claude.com/docs/en/release-notes/overview"
    publisher: "Anthropic"
    primary: true
  - title: "Message threads (Claude Platform documentation)"
    url: "https://platform.claude.com/docs/en/build-with-claude/message-threads"
    publisher: "Anthropic"
    primary: true
---

## What happened

Anthropic's release notes for 2 November 2026 say: "Long conversations and agent loops on the Messages API can now send smaller requests and get a lower time to first token with message threads, in beta with the `message-threads-2026-08-12` beta header." In the release notes' words, "the API keeps the conversation on the server, so each later request sends only the new messages."

## Key details

- **How it works:** the developer sends the full conversation once, with the system prompt and tools, in a request with `"thread": {"type": "create"}`. Later turns use `"thread": {"type": "continue"}` with the `id` of the previous response and only the new messages. System prompts and tools are left out on continue requests; sending either returns an error.
- **Lifetime:** "A thread expires 5 minutes after its last request and is deleted no more than 1 hour after its last use." If a continue request fails because the thread is gone, the developer replays the full conversation in a new request.
- **Where it runs:** the Claude API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed) and Claude in Microsoft Foundry.
- **Restrictions:** the documentation lists the feature as not eligible for zero data retention or HIPAA. Each response can be continued once, threads are append-only and a request can carry at most four cache breakpoints.
- **Latency:** Anthropic says time to first token "stays lower and steadier as the conversation grows" but gives no numbers in the pages we read. A newsletter summary cited a roughly 35% improvement for very long requests; we did not find that figure in Anthropic's documentation, so it is unconfirmed.

## Why it matters

Agents that run long loops resend a growing history on every call, which adds delay and network traffic. Message threads move that history to the server for a short window, which should help most when conversations are very long. The trade-offs are the short expiry, the lack of zero data retention and the beta status, so developers will need fallback code that replays a conversation when a thread disappears.

> Disclosure: Claude is made by Anthropic and is one of the AI tools Deyron Labs uses to research and draft articles, including this one, which is about an Anthropic product. All statements about message threads are Anthropic's own, read from its documentation on 3 November 2026.
