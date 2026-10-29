---
title: "LlamaIndex proposes the Document Parsing Protocol, a 140-rule 'answer key' for how AI agents should read documents"
summary: "On 28 October 2026 LlamaIndex published draft 0.1 of the Document Parsing Protocol, a set of 140 rules for how tables, forms, charts and diagrams should be turned into text for AI agents. It is a proposal open for public feedback, grown out of the rules used for LlamaIndex's ParseBench benchmark. The post does not state a license."
seoTitle: "LlamaIndex Document Parsing Protocol draft 0.1"
seoDescription: "LlamaIndex published draft 0.1 of the Document Parsing Protocol on 28 Oct 2026: 140 rules for parsing tables, forms, charts and diagrams."
lang: en
publishedAt: 2026-10-29T06:55:00Z
entities:
  - LlamaIndex
  - Document Parsing Protocol
  - ParseBench
topics:
  - Agents
  - Research
translationKey: llamaindex-document-parsing-protocol
image: /images/news/llamaindex-document-parsing-protocol-2026-10-29.jpg
imageAlt: "Deyron Labs graphic: LlamaIndex Document Parsing Protocol draft 0.1, published 28 October 2026; 140 rules for tables, forms, charts and diagrams; open for public feedback"
sources:
  - title: "Introducing the Document Parsing Protocol"
    url: "https://www.llamaindex.ai/blog/introducing-the-document-parsing-protocol"
    publisher: "LlamaIndex (28 October 2026)"
    primary: true
---

## What happened

On 28 October 2026 LlamaIndex published "Introducing the Document Parsing Protocol", authored by Gauthami Polasani and Pierre-Loic Doulcet. The company describes the protocol as "an answer key for document parsing" and is releasing working draft 0.1, which it says has 140 rules covering text, tables, forms, charts, diagrams and more.

LlamaIndex says the rules grew out of the guidelines annotators followed when building ParseBench, its document-parsing benchmark. The protocol is hosted at parseprotocol.com, and feedback goes through a public GitHub repository.

## Key details

This is LlamaIndex's proposal, read from its post on 29 October 2026. It is a draft, not an adopted standard.

- **Tables:** the post's example is a sales table with two header rows. The protocol outputs HTML rather than Markdown, because Markdown cannot show spanning headers.
- **Forms:** an empty field becomes "[blank]", and checkboxes become "[x]" and "[ ]".
- **Charts and diagrams:** charts become tables, and diagrams become Mermaid where possible.
- **Edge cases:** unreadable text is marked "[illegible]", hidden text is omitted, and positions are optional. Wrapping rows in thead and tbody is acceptable "as long as a document uses one form throughout".
- **Use with assistants:** the post explains how to load the protocol as a skill in Claude or as a reference file in ChatGPT.
- **License:** the post does not state one for the protocol or the repository.

## Why it matters

Agents that read invoices, forms and reports often disagree on what a table or checkbox means, which makes parsing tools hard to compare. A shared set of rules gives developers a common target, but only if other parsing vendors and users adopt it.

Because LlamaIndex wrote the rules and also sells parsing tools, the protocol should be judged on whether independent parties use it, not on the post alone.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and the LlamaIndex post mentions using the protocol with Claude. Details are LlamaIndex's, taken from its 28 October 2026 post.
