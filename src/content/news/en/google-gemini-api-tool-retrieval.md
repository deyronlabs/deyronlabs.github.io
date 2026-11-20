---
title: "Google adds Tool Retrieval to the Gemini API in preview, loading tool definitions on demand"
summary: "On 19 November 2026 Google announced Tool Retrieval, a preview feature of the Gemini API's Interactions API that loads a tool's parameter schema only when the model asks for it. Google says this means fewer input tokens, lower latency and more accurate tool selection for agents with large tool libraries, but it publishes no measured reduction."
seoTitle: "Gemini API Tool Retrieval: load tools on demand"
seoDescription: "Google's Gemini API Tool Retrieval, in preview from 19 Nov 2026, loads tool schemas on demand to cut tokens; Google gives no measured savings."
lang: en
publishedAt: 2026-11-20T20:27:00Z
entities:
  - Google
  - Gemini API
  - Interactions API
  - Google DeepMind
  - MCP
topics:
  - Agents
  - Products
  - Coding
translationKey: google-gemini-api-tool-retrieval
image: /images/news/google-gemini-api-tool-retrieval-2026-11-19.jpg
imageAlt: "Deyron Labs graphic: Gemini API Tool Retrieval, preview announced 19 November 2026, loads tool schemas on demand, no token savings published"
sources:
  - title: "Tool Retrieval in the Gemini API (Google, 19 November 2026)"
    url: "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/"
    publisher: "Google"
    primary: true
---

## What happened

On 19 November 2026 Google published a post by Lucia Loher, a product manager for the Gemini API, and Nora Kassner, a research scientist at Google DeepMind, announcing Tool Retrieval. It is in preview in the Interactions API of the Gemini API. Google says it loads a tool's parameter schema when the model asks for it, rather than sending an application's whole tool library with every request.

The stated aims are fewer input tokens, lower latency and more accurate tool selection. The post does not give a general-availability date.

## Key details

- **How it works (Google):** a developer adds a `tool_search` tool and sets `defer_loading: true` on the tools that should be deferred. The model sees only the name and description of each deferred tool. When it wants one, the full schema is loaded within the same request. The steps appear in `interaction.steps` as `tool_search_call`, `tool_search_result` and `function_call`.
- **Where the search runs:** on the server by default, with no index for the developer to host. A client-side option, `"execution": "client"`, is available and adds one round trip per search.
- **MCP and caching:** Google says it works with remote MCP servers, with `defer_loading` set on the `mcp_server` entry, and that it is compatible with prefix caching.
- **Models:** Gemini 3.6 and newer, including all Gemini 4 models, in the Interactions API.
- **Pricing:** Google says there is no separate charge. Tokens are billed at the model's normal rates; `tool_search` adds a small fixed block of tokens, and the schemas that get loaded are billed as input. Google's advice is to "measure it against your own traffic".
- **Not on the page we read:** any figure for token or latency reduction, a general-availability date, rate limits, or independent tests. The benefits above are Google's description of the design, not measured results.

## Why it matters

Agents that connect to many tools or several MCP servers can spend a large share of their input tokens on tool definitions the model never uses in a given request. Deferring them is a way to keep that cost down as the tool list grows, and the MCP support means it applies to the common way developers attach outside tools.

Whether it pays off depends on the workload: loading a schema on demand adds a search step, and Google itself says the saving varies with traffic. Developers who use many tools should test it on their own requests before relying on it, since no savings figure has been published.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article. Google is a competitor of Anthropic. All claims are Google's own.
