---
title: "Anthropic says daily code merges grew 12x in four months and it replaced Git with an in-house system called Scion"
summary: "In an engineering post dated 13 October 2026, Anthropic says its monorepo went from about 2,500 merged code changes a day in May to over 30,000 by September, and that Git could no longer keep up. It built a server-side system called Scion, which it says needs 200x less infrastructure. Anthropic says Scion is not a replacement for Git for general use."
seoTitle: "Anthropic swaps Git for Scion at 30K merges/day"
seoDescription: "Anthropic's 13 Oct 2026 engineering post says daily merges rose from 2,500 to over 30,000 and describes Scion, its in-house replacement for Git."
lang: en
publishedAt: 2026-10-15T17:20:00Z
entities:
  - Anthropic
  - Scion
  - Antique
  - Git
topics:
  - Developer tools
  - Anthropic
translationKey: anthropic-scion-replaces-git-source-control
image: /images/news/anthropic-scion-replaces-git-source-control-2026-10-15.jpg
imageAlt: "Deyron Labs graphic: Anthropic's engineering post says merges rose from about 2,500 a day in May to over 30,000 by September 2026, and that its in-house system Scion replaced Git with 200x less infrastructure; figures are Anthropic's own"
sources:
  - title: "Redesigning source control for the agent era"
    url: "https://anthropic.com/engineering/redesigning-source-control"
    publisher: "Anthropic Engineering (13 October 2026)"
    primary: true
---

## What happened

Anthropic published an engineering post on 13 October 2026 describing why it stopped using Git for its main code repository. The company says it averaged around 2,500 code changes merged per day in May 2026 and over 30,000 per day by September, about twelve times as many. At that rate, it says, Git's design became the bottleneck.

Its answer is Scion, an in-house version control system that replaced Git for its monorepo. Anthropic says the move took five months and that a seven-person team built Scion and a companion code review tool called Antique.

## Key details

All figures are Anthropic's, from its own post, read on 15 October 2026. We could not check them independently.

- **Scale:** the main branch history is almost 100 GB and a compressed working copy is over 25 GB. Anthropic says it performs on the order of 25 million code checkouts per day for continuous integration, which with ordinary Git fetching would mean over 600 PB of Git traffic per day.
- **Why Git struggled:** at peak the company ran several hundred internal Git mirrors, which grew harder to operate as merge rates rose. Anthropic also argues that Git is designed for distributed, offline clients, while nearly all of its clients are always-online agents and automated jobs.
- **How Scion works:** changes are recorded as "changesets" in a write-ahead log and created on the server, rather than as commits pushed from clients. The server handles history, blame, commits, merges and rebases, and clients keep a bounded local cache.
- **Reported results:** Anthropic says Scion's infrastructure footprint is 200x smaller than the previous Git mirroring setup in CPU and memory, that CI and research checkouts dropped from minutes to seconds, and that CI alone gained 25% CPU capacity.
- **Availability:** the post does not announce an open-source release or a product. Anthropic says Scion "is by no means a suitable replacement for git for general use" and that it is sharing its design thinking so others can apply some of the ideas to Git.

## Why it matters

The post is a concrete data point on what AI coding agents do to engineering infrastructure: Anthropic reports that the number of changes landing per day grew tenfold in months, and that this broke tooling that had worked for years. Teams that expect to run many agents against one repository may meet the same limits earlier than they expect, although Anthropic's repository and merge rate are far beyond most organizations'.

For most readers there is nothing to adopt: Scion is internal and Anthropic says it is not a general replacement. The figures are also a company describing its own system. This article follows Anthropic's account and does not include an independent measurement.

> Disclosure: Claude, made by Anthropic, was one of the AI tools used to research and draft this article, and Anthropic is the subject and the source of every figure here. Treat the numbers as Anthropic's own claims.
